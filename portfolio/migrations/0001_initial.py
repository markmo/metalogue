# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Client'
        db.create_table('portfolio_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('portfolio', ['Client'])

        # Adding model 'ClientTechnology'
        db.create_table('portfolio_clienttechnology', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('portfolio', ['ClientTechnology'])

        # Adding model 'Database'
        db.create_table('portfolio_database', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('portfolio', ['Database'])

        # Adding model 'OrganisationalUnit'
        db.create_table('portfolio_organisationalunit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['OrganisationalUnit'])

        # Adding model 'OperatingSystem'
        db.create_table('portfolio_operatingsystem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('portfolio', ['OperatingSystem'])

        # Adding model 'ProgrammingLanguage'
        db.create_table('portfolio_programminglanguage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('portfolio', ['ProgrammingLanguage'])

        # Adding model 'UserGroup'
        db.create_table('portfolio_usergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['UserGroup'])

        # Adding model 'Application'
        db.create_table('portfolio_application', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('business_criticality', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('complexity', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('usage_variance', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('life_expectancy', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.ProgrammingLanguage'], null=True, blank=True)),
            ('os', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.OperatingSystem'], null=True, blank=True)),
            ('database', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Database'], null=True, blank=True)),
            ('known_issues', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pending_changes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['Application'])

        # Adding M2M table for field organisational_units on 'Application'
        db.create_table('portfolio_application_organisational_units', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm['portfolio.application'], null=False)),
            ('organisationalunit', models.ForeignKey(orm['portfolio.organisationalunit'], null=False))
        ))
        db.create_unique('portfolio_application_organisational_units', ['application_id', 'organisationalunit_id'])

        # Adding M2M table for field client_technologies on 'Application'
        db.create_table('portfolio_application_client_technologies', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm['portfolio.application'], null=False)),
            ('clienttechnology', models.ForeignKey(orm['portfolio.clienttechnology'], null=False))
        ))
        db.create_unique('portfolio_application_client_technologies', ['application_id', 'clienttechnology_id'])

        # Adding model 'ApplicationAlias'
        db.create_table('portfolio_applicationalias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['ApplicationAlias'])

        # Adding model 'ApplicationUserGroup'
        db.create_table('portfolio_applicationusergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Application'])),
            ('user_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.UserGroup'])),
            ('application_alias', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.ApplicationAlias'], null=True, blank=True)),
        ))
        db.send_create_signal('portfolio', ['ApplicationUserGroup'])

        # Adding model 'UserProfile'
        db.create_table('portfolio_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['UserProfile'])


    def backwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('portfolio_client')

        # Deleting model 'ClientTechnology'
        db.delete_table('portfolio_clienttechnology')

        # Deleting model 'Database'
        db.delete_table('portfolio_database')

        # Deleting model 'OrganisationalUnit'
        db.delete_table('portfolio_organisationalunit')

        # Deleting model 'OperatingSystem'
        db.delete_table('portfolio_operatingsystem')

        # Deleting model 'ProgrammingLanguage'
        db.delete_table('portfolio_programminglanguage')

        # Deleting model 'UserGroup'
        db.delete_table('portfolio_usergroup')

        # Deleting model 'Application'
        db.delete_table('portfolio_application')

        # Removing M2M table for field organisational_units on 'Application'
        db.delete_table('portfolio_application_organisational_units')

        # Removing M2M table for field client_technologies on 'Application'
        db.delete_table('portfolio_application_client_technologies')

        # Deleting model 'ApplicationAlias'
        db.delete_table('portfolio_applicationalias')

        # Deleting model 'ApplicationUserGroup'
        db.delete_table('portfolio_applicationusergroup')

        # Deleting model 'UserProfile'
        db.delete_table('portfolio_userprofile')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('codename',)", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'portfolio.application': {
            'Meta': {'object_name': 'Application'},
            'business_criticality': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'client_technologies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['portfolio.ClientTechnology']", 'null': 'True', 'blank': 'True'}),
            'complexity': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'database': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Database']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_issues': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.ProgrammingLanguage']", 'null': 'True', 'blank': 'True'}),
            'life_expectancy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organisational_units': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.OrganisationalUnit']", 'symmetrical': 'False'}),
            'os': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.OperatingSystem']", 'null': 'True', 'blank': 'True'}),
            'pending_changes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'usage_variance': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'user_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.UserGroup']", 'through': "orm['portfolio.ApplicationUserGroup']", 'symmetrical': 'False'})
        },
        'portfolio.applicationalias': {
            'Meta': {'object_name': 'ApplicationAlias'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.applicationusergroup': {
            'Meta': {'object_name': 'ApplicationUserGroup'},
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Application']"}),
            'application_alias': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.ApplicationAlias']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.UserGroup']"})
        },
        'portfolio.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.clienttechnology': {
            'Meta': {'object_name': 'ClientTechnology'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.database': {
            'Meta': {'object_name': 'Database'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.operatingsystem': {
            'Meta': {'object_name': 'OperatingSystem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.organisationalunit': {
            'Meta': {'object_name': 'OrganisationalUnit'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.programminglanguage': {
            'Meta': {'object_name': 'ProgrammingLanguage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.usergroup': {
            'Meta': {'object_name': 'UserGroup'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['portfolio']
