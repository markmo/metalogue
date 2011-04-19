from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from portfolio.forms import SwitchClientForm
from portfolio.models import Application, ApplicationAlias, ApplicationUserGroup, Client, ClientTechnology, Database, OrganisationalUnit, OperatingSystem, ProgrammingLanguage, UserGroup, UserProfile
import logging

logger = logging.getLogger(__name__)

class PortfolioAdminSite(admin.AdminSite):
    
    def app_index(self, request, app_label, extra_context=None):
        profile = request.user.get_profile()
        form = SwitchClientForm(initial={ 'client': profile.client.pk })
        context = { 'form': form, }
        context.update(extra_context or {})
        return super(PortfolioAdminSite, self).app_index(request, app_label, context)

class ApplicationAliasAdmin(admin.ModelAdmin):
    exclude = ['client',]

    def save_model(self, request, obj, form, change):
        obj.client = request.user.get_profile().client
        obj.save()
        
    def queryset(self, request):
        qs = self.model._default_manager.filter(client=request.user.get_profile().client)
        return qs

class ApplicationUserGroupInline(admin.TabularInline):
    model = ApplicationUserGroup
    extra = 1
    classes = ('collapse closed',)

class ApplicationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'description', 'organisational_units', 'pub_date']
        }),
        ('Assessment', {
            'classes': ['collapse closed'],
            'fields': ['business_criticality', 'complexity', 'usage_variance', 'life_expectancy'],
        }),
        ('Technology', {
            'classes': ['collapse closed'],
            'fields': ['client_technologies', 'language', 'os', 'database'],
        }),
        ('Issues and Change', {
            'classes': ['collapse closed'],
            'fields': ['known_issues', 'pending_changes'],
        }),
    ]
    inlines = (ApplicationUserGroupInline,)
    list_display = ('name', 'pub_date', 'was_published_today')
    list_filter = ['pub_date']
    search_fields = ['name']
    date_hierarchy = 'pub_date'
    filter_horizontal = ['organisational_units', 'client_technologies']

    def save_model(self, request, obj, form, change):
        obj.client = request.user.get_profile().client
        obj.save()
        
    def queryset(self, request):
        qs = self.model._default_manager.filter(client=request.user.get_profile().client)
        return qs

class OrganisationalUnitAdmin(admin.ModelAdmin):
    exclude = ['client',]

    def save_model(self, request, obj, form, change):
        obj.client = request.user.get_profile().client
        obj.save()
        
    def queryset(self, request):
        qs = self.model._default_manager.filter(client=request.user.get_profile().client)
        return qs

class UserGroupAdmin(admin.ModelAdmin):
    inlines = (ApplicationUserGroupInline,)

    def save_model(self, request, obj, form, change):
        obj.client = request.user.get_profile().client
        obj.save()
        
    def queryset(self, request):
        qs = self.model._default_manager.filter(client=request.user.get_profile().client)
        return qs

class UserProfileInline(admin.TabularInline):
    model = UserProfile
    fk_name = 'user'
    max_num = 1

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'client')
    inlines = [UserProfileInline,]

admin_site = PortfolioAdminSite()
admin_site.register(Application, ApplicationAdmin)
admin_site.register(ApplicationAlias, ApplicationAliasAdmin)
admin_site.register(Client)
admin_site.register(ClientTechnology)
admin_site.register(Database)
admin_site.register(OrganisationalUnit, OrganisationalUnitAdmin)
admin_site.register(OperatingSystem)
admin_site.register(ProgrammingLanguage)
admin_site.register(UserGroup, UserGroupAdmin)
# admin_site.unregister(User)
admin_site.register(User, CustomUserAdmin)