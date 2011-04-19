from django.conf.urls.defaults import patterns, include, url
from django.contrib import databrowse
from portfolio.models import Application, ApplicationAlias, ApplicationUserGroup, Client, ClientTechnology, Database, OrganisationalUnit, OperatingSystem, ProgrammingLanguage, UserGroup, UserProfile
from portfolio.admin import admin_site
import portfolio

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'metalogue.views.home', name='home'),
    # url(r'^metalogue/', include('metalogue.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^switch_client/', 'portfolio.views.switch_client'),
    (r'^grappelli/', include('grappelli.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin_site.urls)),
    (r'^db/(.*)', databrowse.site.root),
)

databrowse.site.register(Application)