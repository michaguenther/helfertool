from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'news'
urlpatterns = [
    url(r'^manage/news/$',
        views.send,
        name='send'),

    url(r'^subscribe/$',
        views.subscribe,
        name='subscribe'),

    url(r'^subscribe/done/$',
        TemplateView.as_view(template_name='news/subscribe_done.html'),
        name='subscribe_done'),

    # empty tokens are allowed since this is used to generate the link once
    # and add the specific tokens
    # empty tokens are handled in the view with an 404
    url(r'^unsubscribe/(?P<token>[0-9a-f\-]*)/$',
        views.unsubscribe,
        name='unsubscribe'),

    url(r'^unsubscribe/done/$',
        TemplateView.as_view(template_name='news/unsubscribe_done.html'),
        name='unsubscribe_done'),
]
