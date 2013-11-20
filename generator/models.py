from django.db import models
from django.db.models import Max
from django.core.urlresolvers import reverse
from django.conf import settings

from cv.models import Employee

class ReportManager(models.Manager):
    def get_queryset(self):
        a = Generator.objects.values("employee").annotate(latest_id=Max('id'))
        a = list(v['latest_id'] for v in a)
        return Generator.objects.filter(id__in=a).order_by('-creation_date')

class Template(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add = True)
    last_change = models.DateTimeField(auto_now = True)

    #Functions
    def count_settings(self):
        return self.template_setting_set.count()
    count_settings.admin_order_field = 'count_settings'
    count_settings.short_description = '# of settings'

    # Self
    def __unicode__(self):
        return "%s" % (self.name)

class Generator(models.Model):
    # Fields
    ERROR = 'E'
    FINISHED = 'F'
    PROCESSING = 'P'
    QUEUED = 'Q'
    STATUS_AUSWAHL = (
        (ERROR, 'Fehler'),
        (FINISHED, 'Beendet'),
        (PROCESSING, 'Wird generiert'),
        (QUEUED, 'Warteschlange'),
    )
    status = models.CharField(max_length=1,
        choices=STATUS_AUSWAHL,
        default=QUEUED)
    creation_date = models.DateTimeField(auto_now_add = True)
    pdf_file = models.FileField(
        upload_to = settings.MEDIA_ROOT,
        blank = True,
        null = True,
        help_text = "Sample help text.",
    )
    tex_file = models.FileField(
        upload_to = settings.MEDIA_ROOT,
        blank = True,
        null = True,
        help_text = "Sample help text.",
    )

    # Foreign keys
    employee = models.ForeignKey(Employee)
    template = models.ForeignKey(Template)

    # Managers
    #latest_cv_by_employee = ReportManager()

    # Self
    def __unicode__(self):
        return "%s with template %s" % (self.employee, self.template)

    # Functions
    def get_absolute_url(self):
        return reverse('generator:detail', kwargs={'pk': self.pk})

    def generate_filename(self, id, employee, template, filetype):
        return str(id) + '_' + employee.first_name + '_' + employee.last_name + '_' + template.name + '.' + filetype

class Template_Setting(models.Model):
    # Fields
    ANONYMOUS_CUSTOMER = 'AC'
    ATTRIBUTE_AUSWAHL = (
        (ANONYMOUS_CUSTOMER, 'Anonyme Kunden'),
    )
    attribute = models.CharField(max_length=2,
        choices=ATTRIBUTE_AUSWAHL,
        default=ANONYMOUS_CUSTOMER)
    value = models.BooleanField()

    creation_date = models.DateTimeField(auto_now_add = True)
    last_change = models.DateTimeField(auto_now = True)

    # Foreign keys
    template = models.ForeignKey(Template)

    # Self
    def __unicode__(self):
        return "%s as %s" % (self.attribute, self.value)
