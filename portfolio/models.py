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

class UserGroup(models.Model):

    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.name)

class Application(models.Model):

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

    LIFE_EXPECTANCY_CHOICES = (
        (0, 'Past use by date'),
        (1, '< 2 years'),
        (2, '2-5 years'),
        (3, '> 5 years'),
    )

    USAGE_VARIANCE_CHOICES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )

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

class ApplicationAlias(models.Model):

    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Application aliases"

class ApplicationUserGroup(models.Model):

    application = models.ForeignKey(Application)
    user_group = models.ForeignKey(UserGroup)
    application_alias = models.ForeignKey(ApplicationAlias, blank=True, null=True)

class UserProfile(models.Model):

    user = models.OneToOneField(User, unique=True)
    client = models.ForeignKey(Client)

    def __unicode__(self):
        return str(self.user.username)

# User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
User.client = property(lambda u: u.get_profile().client)