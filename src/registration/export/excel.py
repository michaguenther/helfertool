from django.template import defaultfilters as filters
from django.utils.translation import ugettext as _
import re
import xlsxwriter


class Iterator():
    """ Returns ascending natural numbers beginning from 0. """
    def __init__(self):
        self.__v = -1

    def next(self):
        """ Returns the next number beginning from 0. """
        self.__v += 1
        return self.__v

    def get(self):
        """ Returns the current number.

        get() should only be used after next() to get the same number again.
        """
        return self.__v

    def reset(self):
        """ Resets the counter.

        The first call to next() after this returns 0. """
        self.__v = -1


def cleanName(name):
    """ Cleans the name to be a valid sheet name in excel.

    The characters [ ] : * ? / \ are removed.
    """
    return re.sub(r'[\[\]:*?\\\/]', '', name)


def escape(payload):
    if not payload:
        return ""

    # http://blog.zsec.uk/csv-dangers-mitigations/
    if payload[0] in ('@', '+', '-', '=', '|'):
        payload = payload.replace("|", "\|")
        payload = "'" + payload + "'"
    return payload


def xlsx(buffer, event, jobs, date):
    """ Exports the helpers for given jobs of an event as excel spreadsheet.

    Parameter:
        buffer: a writeable bytes buffer (e.g. io.BytesIO or a file)
        event:  the exported event
        jobs:   a list of all exported jobs
    """
    # create xlsx
    workbook = xlsxwriter.Workbook(buffer)

    # duplicated worksheet names are not allowed
    used_names = []

    # export jobs
    for job in jobs:
        # find unique worksheet name
        job_name = cleanName(job.name)[:20]  # worksheet name must be <= 31 chars

        job_name_use = job_name
        counter = 2
        while job_name_use in used_names:
            job_name_use = "{}{}".format(job_name, counter)
            counter += 1

        used_names.append(job_name_use)

        # add things
        worksheet = workbook.add_worksheet(job_name_use)
        bold = workbook.add_format({'bold': True})
        multiple_shifts = workbook.add_format({'bg_color': '#fFFF99'})

        row = Iterator()
        column = Iterator()

        # header
        worksheet.write(0, column.next(), _("First name"), bold)
        worksheet.write(0, column.next(), _("Surname"), bold)

        if event.ask_address:
            worksheet.write(0, column.next(), _("Street"), bold)
            worksheet.set_column(column.get(), column.get(), 20)
<<<<<<< HEAD
=======
            worksheet.write(0, column.next(), _("Street  number"), bold)
            worksheet.set_column(column.get(), column.get(), 10)
>>>>>>> 5c076aab6e06f1edbef1f810af72f60d4429fe2b
            worksheet.write(0, column.next(), _("Zipcode"), bold)
            worksheet.set_column(column.get(), column.get(), 10)
            worksheet.write(0, column.next(), _("City"), bold)
            worksheet.set_column(column.get(), column.get(), 20)

        worksheet.write(0, column.next(), _("E-Mail"), bold)
        worksheet.set_column(0, column.get(), 30)

        if event.ask_phone:
            worksheet.write(0, column.next(), _("Mobile phone"), bold)
            worksheet.set_column(column.get(), column.get(), 20)

        if event.ask_course:
            worksheet.write(0, column.next(), _("Academic course"), bold)
            worksheet.set_column(column.get(), column.get(), 20)

        if event.ask_shirt:
            worksheet.write(0, column.next(), _("T-shirt"), bold)
            worksheet.set_column(column.get(), column.get(), 10)

<<<<<<< HEAD
=======
        if event.ask_birthday:
            worksheet.write(0, column.next(), _("Birthday"), bold)
            worksheet.set_column(column.get(), column.get(), 10)

>>>>>>> 5c076aab6e06f1edbef1f810af72f60d4429fe2b
        if event.ask_fachschaft:
            worksheet.write(0, column.next(), _("Fachschaft"), bold)
            worksheet.set_column(column.get(), column.get(), 10)

        if event.ask_vegetarian:
            worksheet.write(0, column.next(), _("Vegetarian"), bold)
            worksheet.set_column(column.get(), column.get(), 10)

        if job.infection_instruction:
            worksheet.write(0, column.next(), _("Food handling"), bold)
            worksheet.set_column(column.get(), column.get(), 20)

        worksheet.write(0, column.next(), _("Comment"), bold)
        worksheet.set_column(column.get(), column.get(), 50)

        # last column, needed for merge later
        last_column = column.get()

        # freeze header
        worksheet.freeze_panes(1, 0)

        # skip first row
        row.next()

        # coordinators
        if not date and job.coordinators.exists():
            worksheet.merge_range(row.next(), 0, row.get(), last_column,
                                  _("Coordinators"), bold)
            add_helpers(worksheet, row, column, event, job,
                        job.coordinators.all(), multiple_shifts)

        # show all shifts
        for shift in job.shift_set.order_by('begin'):
            if date and shift.begin.date() != date:
                continue

            worksheet.merge_range(row.next(), 0, row.get(),
                                  last_column, shift.time(), bold)
            add_helpers(worksheet, row, column, event, job,
                        shift.helper_set.all(), multiple_shifts)

    # close xlsx
    workbook.close()


def add_helpers(worksheet, row, column, event, job, helpers,
                multiple_shifts_format):
    for helper in helpers:
        row.next()
        column.reset()

        num_shifts = helper.shifts.count()
        num_jobs = len(helper.coordinated_jobs)
        format = None
        if num_shifts + num_jobs > 1:
            format = multiple_shifts_format

        worksheet.write(row.get(), column.next(), escape(helper.firstname),
                        format)
        worksheet.write(row.get(), column.next(), escape(helper.surname),
                        format)

        if event.ask_address:
            worksheet.write(row.get(), column.next(), escape(helper.street), format)
<<<<<<< HEAD
=======
            worksheet.write(row.get(), column.next(), escape(helper.street_number), format)
>>>>>>> 5c076aab6e06f1edbef1f810af72f60d4429fe2b
            worksheet.write(row.get(), column.next(), escape(helper.zipcode), format)
            worksheet.write(row.get(), column.next(), escape(helper.city), format)

        worksheet.write(row.get(), column.next(), escape(helper.email), format)
        if event.ask_phone:
            worksheet.write(row.get(), column.next(), escape(helper.phone), format)
        if event.ask_course:
            worksheet.write(row.get(), column.next(), escape(helper.course), format)
        if event.ask_shirt:
            worksheet.write(row.get(), column.next(), escape(str(helper.get_shirt_display())), format)
<<<<<<< HEAD
=======
        if event.ask_birthday:
            worksheet.write(row.get(), column.next(), escape(str(helper.birthday)), format)
>>>>>>> 5c076aab6e06f1edbef1f810af72f60d4429fe2b
        if event.ask_fachschaft:
            worksheet.write(row.get(), column.next(),
                            escape(filters.yesno(helper.member)), format)
        if event.ask_vegetarian:
            worksheet.write(row.get(), column.next(),
                            escape(filters.yesno(helper.vegetarian)), format)
        if job.infection_instruction:
            worksheet.write(row.get(), column.next(), escape(str(helper.get_infection_instruction_short())), format)
        worksheet.write(row.get(), column.next(), escape(helper.comment),
                        format)
