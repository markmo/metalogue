import datetime
from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

class ClientTechnology(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Client technologies"

class Database(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

class Vendor(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

class HardwarePlatform(models.Model):

    name = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor)

    def __unicode__(self):
        return str(self.name)

class OrganisationalUnit(models.Model):

    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.name)

class OperatingSystem(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

class ProgrammingLanguage(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

class SchemaType(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return str(self.name)

class StakeholderGroup(models.Model):

    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.name)

class StakeholderRole(models.Model):

    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.name)

class UserGroup(models.Model):

    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.name)

ANNUAL_DATA_VOLUME_GROWTH_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

APPLICATION_COMPLEXITY_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

BUSINESS_CRITICALITY_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

COMPLEXITY_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

DATA_VOLUME_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

DOCUMENT_COMPLETENESS_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

DOCUMENT_FRESHNESS_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

LIFE_EXPECTANCY_CHOICES = (
    (0, 'Past use by date'),
    (1, '< 2 years'),
    (2, '2-5 years'),
    (3, '> 5 years'),
)

MAX_CAPACITY_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

USAGE_VARIANCE_CHOICES = (
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High'),
)

class DataSourceType(models.Model):

    name = models.CharField(max_length=200)
    vendor = models.ForeignKey(Vendor)

    def __unicode__(self):
        return str(self.name)

class DataSource(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    business_criticality = models.CharField(max_length=1, choices=BUSINESS_CRITICALITY_CHOICES, blank=True, null=True)
    complexity = models.CharField(max_length=1, choices=COMPLEXITY_CHOICES, blank=True, null=True)
    life_expectancy = models.IntegerField(choices=LIFE_EXPECTANCY_CHOICES, blank=True, null=True)
    document_completeness = models.CharField(max_length=1, choices=DOCUMENT_COMPLETENESS_CHOICES, blank=True, null=True)
    document_freshness = models.CharField(max_length=1, choices=DOCUMENT_FRESHNESS_CHOICES, blank=True, null=True)
    schema_type = models.ForeignKey(SchemaType)
    data_source_type = models.ForeignKey(DataSourceType)
    hardware_platform = models.ForeignKey(HardwarePlatform, blank=True, null=True)
    # applications = models.ManyToManyField(Application)
    data_volume = models.CharField(max_length=1, choices=DATA_VOLUME_CHOICES, blank=True, null=True)
    maximum_capacity = models.CharField(max_length=1, choices=MAX_CAPACITY_CHOICES, blank=True, null=True)
    annual_data_volume_growth = models.CharField(max_length=1, choices=ANNUAL_DATA_VOLUME_GROWTH_CHOICES, blank=True, null=True)
    known_issues = models.TextField(blank=True)
    pending_changes = models.TextField(blank=True)
    user_groups = models.ManyToManyField(UserGroup, through='DataSourceUserGroup')

    pub_date = models.DateTimeField('date published')
    client = models.ForeignKey(Client)

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'

    def __unicode__(self):
        return str(self.name)

class Application(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    organisational_units = models.ManyToManyField(OrganisationalUnit)
    business_criticality = models.CharField(max_length=1, choices=BUSINESS_CRITICALITY_CHOICES, blank=True, null=True)
    complexity = models.CharField(max_length=1, choices=APPLICATION_COMPLEXITY_CHOICES, blank=True, null=True)
    usage_variance = models.CharField(max_length=1, choices=USAGE_VARIANCE_CHOICES, blank=True, null=True)
    life_expectancy = models.IntegerField(choices=LIFE_EXPECTANCY_CHOICES, blank=True, null=True)
    client_technologies = models.ManyToManyField(ClientTechnology, blank=True, null=True)
    language = models.ForeignKey(ProgrammingLanguage, verbose_name='Programming language', blank=True, null=True)
    os = models.ForeignKey(OperatingSystem, verbose_name='Operating system', blank=True, null=True)
    database = models.ForeignKey(Database, blank=True, null=True)
    data_sources = models.ManyToManyField(DataSource)
    known_issues = models.TextField(blank=True)
    pending_changes = models.TextField(blank=True)
    user_groups = models.ManyToManyField(UserGroup, through='ApplicationUserGroup')

    pub_date = models.DateTimeField('date published')
    client = models.ForeignKey(Client)

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'

    def __unicode__(self):
        return str(self.name)

class DataSourceStakeholderGroup(models.Model):
    
    data_source = models.ForeignKey(DataSource)
    stakeholder_group = models.ForeignKey(StakeholderGroup)
    stakeholder_role = models.ForeignKey(StakeholderRole)

    def __unicode__(self):
        return str(self.name)

class Alias(models.Model):

    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Aliases"

class ApplicationUserGroup(models.Model):

    application = models.ForeignKey(Application)
    user_group = models.ForeignKey(UserGroup)
    alias = models.ForeignKey(Alias, blank=True, null=True)

class DataSourceUserGroup(models.Model):

    data_source = models.ForeignKey(DataSource)
    user_group = models.ForeignKey(UserGroup)
    alias = models.ForeignKey(Alias, blank=True, null=True)

class UserProfile(models.Model):

    user = models.OneToOneField(User, unique=True)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.user.username)

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
User.client = property(lambda u: u.get_profile().client)