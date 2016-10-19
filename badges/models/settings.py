from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from copy import deepcopy

import posixpath

from .defaults import BadgeDefaults


def _settings_upload_path(instance, filename):
    event = str(instance.event.pk)

    return posixpath.join('badges', event, 'template', filename)


class BadgeSettings(models.Model):
    """ Settings for badge creation

    Columns:
        :event: The event that uses the badge creation
    """

    event = models.OneToOneField(
        'registration.Event'
    )

    defaults = models.OneToOneField(
        'BadgeDefaults'
    )

    latex_template = models.FileField(
        verbose_name=_("LaTeX template"),
        upload_to=_settings_upload_path,
        null=True,
    )

    rows = models.IntegerField(
        default=5,
        verbose_name=_("Number of rows on one page"),
        validators=[MinValueValidator(1)],
    )

    columns = models.IntegerField(
        default=2,
        verbose_name=_("Number of columns on one page"),
        validators=[MinValueValidator(1)],
    )

    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default=settings.BADGE_LANGUAGE_CODE,
        verbose_name=_("Language of badges"),
    )

    coordinator_title = models.CharField(
        max_length=200,
        default="",
        verbose_name=_("Role for coordinators"),
    )

    helper_title = models.CharField(
        max_length=200,
        default="",
        verbose_name=_("Role for helpers"),
    )

    only_coordinators = models.BooleanField(
        default=False,
        verbose_name=_("Badges only for coordinators"),
    )

    barcodes = models.BooleanField(
        default=False,
        verbose_name=_("Print barcodes on badges to avoid duplicates"),
    )

    def save(self, *args, **kwargs):
        if not hasattr(self, 'defaults'):
            defaults = BadgeDefaults()
            defaults.save()

            self.defaults = defaults

        super(BadgeSettings, self).save(*args, **kwargs)

    def creation_possible(self):
        if not self.latex_template:
            return False

        if not self.defaults.role:
            return False

        if not self.defaults.design:
            return False

        return True

    def duplicate(self, event):
        # first duplicate the settings
        new_settings = deepcopy(self)
        new_settings.pk = None
        new_settings.event = event

        # role and design are from the old model until now
        new_settings.defaults = self.defaults.duplicate()

        # but we need the PK to update them, so save here
        new_settings.save()


        # new duplicate all roles, permissions and designs
        # mapping: old pk -> new pk
        permission_map = {}
        role_map = {}
        design_map = {}

        for permission in self.badgepermission_set.all():
            new_permission = permission.duplicate(new_settings)
            permission_map[permission] = new_permission

        for design in self.badgedesign_set.all():
            new_design = design.duplicate(new_settings)
            design_map[design] = new_design

        for role in self.badgerole_set.all():
            new_role = role.duplicate(new_settings, permission_map)
            role_map[role] = new_role

        # update role and design in new_settings.defaults
        new_settings.defaults.update_after_dup(role_map, design_map)

        # and now iterate all jobs and update the BadgeDefaults
        for job in event.job_set.all():
            if job.badge_defaults:
                job.badge_defaults.update_after_dup(role_map, design_map)

        return new_settings

        # TODO: latex
