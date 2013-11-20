from django.db import models
from django_countries import CountryField

class Customer(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField()
    industry = models.CharField(max_length=100)
    anonymous = models.CharField(max_length=100)

    # Self
    def __unicode__(self):
        return "%s" % (self.name)

class Employee(models.Model):
    # Fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    place_of_birth = models.CharField(max_length=50)
    year_of_birth = models.IntegerField()

    LEDIG = 'L'
    VERHEIRATET = 'V'
    FAMILIENSTAND_AUSWAHL = (
        (LEDIG, 'Ledig'),
        (VERHEIRATET, 'Verheiratet'),
    )
    family_status = models.CharField(max_length=1,
        choices=FAMILIENSTAND_AUSWAHL,
        default=LEDIG)

    CONSULTANT = 'CO'
    SENIOR_CONSULTANT = 'SC'
    POSITION_AUSWAHL = (
       (CONSULTANT, 'Consultant'),
       (SENIOR_CONSULTANT, 'Senior Consultant'),
    )
    position = models.CharField(max_length=2,
        choices=POSITION_AUSWAHL,
        default=CONSULTANT)

    citizenship = models.CharField(max_length=100)
    short_description = models.CharField(max_length=5000)

    creation_date = models.DateTimeField(auto_now_add = True)
    last_change = models.DateTimeField(auto_now = True)

    #Functions
    def count_skills(self):
        return self.skill_set.count()
    count_skills.admin_order_field = 'count_skills'
    count_skills.short_description = '# of skills'

    def count_projects(self):
        return self.project_set.count()
    count_projects.admin_order_field = 'count_projects'
    count_projects.short_description = '# of projects'

    # Self
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Skill(models.Model):
    # Fields
    APPLICATION_SERVER = 'AS'
    CERTIFICAT = 'C'
    COMMUNICATION_PROTOCOL = 'CP'
    MIDDLEWARE = 'M'
    MESSAGE_FORMAT = 'MF'
    MISC = 'MI'
    MESSAGE_STANDARD = 'MS'
    PROGRAMMING_LANGUAGE = 'PL'
    SAP_MODULE = 'SM'
    SAP_TECHNOLOGY = 'ST'
    KIND_OF_SKILL_AUSWAHL = (
       (APPLICATION_SERVER, 'Applikationsserver'),
       (CERTIFICAT, 'Zertifikat'),
       (COMMUNICATION_PROTOCOL, 'Kommunikationsprotokoll'),
       (MIDDLEWARE, 'Middleware'),
       (MESSAGE_FORMAT, 'Nachrichtenformat'),
       (MESSAGE_STANDARD, 'Nachrichtenstandard'),
       (MISC, 'Andere'),
       (PROGRAMMING_LANGUAGE, 'Programmiersprache'),
       (SAP_MODULE, 'SAP-Modul'),
       (SAP_TECHNOLOGY, 'SAP-Technologie'),
    )
    kind_of_skill = models.CharField(max_length=2,
        choices=KIND_OF_SKILL_AUSWAHL,
        default=APPLICATION_SERVER)

    skill = models.CharField(max_length=200)

    # Foreign key
    employee = models.ForeignKey(Employee, blank=True, null=True)

class Project(models.Model):
    name = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    country_iso_code = CountryField()
    position = models.CharField(max_length=100)
    work_start = models.DateField()
    work_end = models.DateField()
    project_start = models.DateField()
    project_end = models.DateField()
    # Kann berechnet werden
    #projektdauer_in_monaten = models.IntegerField()
    activities = models.CharField(max_length=5000)

    # Foreign key
    customer = models.ForeignKey(Customer, blank=True, null=True)

    # Foreign key
    employee = models.ForeignKey(Employee, blank=True, null=True)

    # Functions
    def project_duration_in_months(self):
        return self.project_end.month-self.project_start.month
    project_duration_in_months.admin_order_field = 'project_duration_in_months'
    project_duration_in_months.short_description = 'Project duration in months'

class Training(models.Model):
    trainings = models.CharField(max_length=5000)
    advanced_trainings = models.CharField(max_length=5000)

    # Foreign key
    employee = models.ForeignKey(Employee, blank=True, null=True)

class Education(models.Model):
    institute = models.CharField(max_length=200)
    branch_of_study = models.CharField(max_length=200)
    study_start = models.DateField()
    study_end = models.DateField()
    degree = models.CharField(max_length=200)
    degree_short = models.CharField(max_length=50)
    thesis_topic = models.CharField(max_length=200)

    # Foreign key
    employee = models.ForeignKey(Employee, blank=True, null=True)

class Spoken_Language(models.Model):
    # Fields
    language = models.CharField(max_length=50)

    MUTTERSPRACHE = 'MS'
    VERHANDLUNGSSICHER = 'VS'
    KOENNEN_AUSWAHL = (
        (MUTTERSPRACHE, 'Muttersprache'),
        (VERHANDLUNGSSICHER, 'Verhandlungssicher'),
        )
    skill = models.CharField(max_length=2,
        choices=KOENNEN_AUSWAHL,
        default=MUTTERSPRACHE
        )

    # Foreign key
    employee = models.ForeignKey(Employee, blank=True, null=True)