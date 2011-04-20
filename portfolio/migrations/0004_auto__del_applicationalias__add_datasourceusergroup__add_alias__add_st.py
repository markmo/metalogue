# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'ApplicationAlias'
        db.delete_table('portfolio_applicationalias')

        # Adding model 'DataSourceUserGroup'
        db.create_table('portfolio_datasourceusergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.DataSource'])),
            ('user_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.UserGroup'])),
            ('alias', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Alias'], null=True, blank=True)),
        ))
        db.send_create_signal('portfolio', ['DataSourceUserGroup'])

        # Adding model 'Alias'
        db.create_table('portfolio_alias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['Alias'])

        # Adding model 'StakeholderRole'
        db.create_table('portfolio_stakeholderrole', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['StakeholderRole'])

        # Adding model 'StakeholderGroup'
        db.create_table('portfolio_stakeholdergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['StakeholderGroup'])

        # Adding model 'DataSourceStakeholderGroup'
        db.create_table('portfolio_datasourcestakeholdergroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stakeholder_role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.StakeholderRole'])),
        ))
        db.send_create_signal('portfolio', ['DataSourceStakeholderGroup'])

        # Deleting field 'ApplicationUserGroup.application_alias'
        db.delete_column('portfolio_applicationusergroup', 'application_alias_id')

        # Adding field 'ApplicationUserGroup.alias'
        db.add_column('portfolio_applicationusergroup', 'alias', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Alias'], null=True, blank=True), keep_default=False)

        # Adding field 'DataSource.known_issues'
        db.add_column('portfolio_datasource', 'known_issues', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'DataSource.pending_changes'
        db.add_column('portfolio_datasource', 'pending_changes', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding M2M table for field data_sources on 'Application'
        db.create_table('portfolio_application_data_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm['portfolio.application'], null=False)),
            ('datasource', models.ForeignKey(orm['portfolio.datasource'], null=False))
        ))
        db.create_unique('portfolio_application_data_sources', ['application_id', 'datasource_id'])


    def backwards(self, orm):
        
        # Adding model 'ApplicationAlias'
        db.create_table('portfolio_applicationalias', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
        ))
        db.send_create_signal('portfolio', ['ApplicationAlias'])

        # Deleting model 'DataSourceUserGroup'
        db.delete_table('portfolio_datasourceusergroup')

        # Deleting model 'Alias'
        db.delete_table('portfolio_alias')

        # Deleting model 'StakeholderRole'
        db.delete_table('portfolio_stakeholderrole')

        # Deleting model 'StakeholderGroup'
        db.delete_table('portfolio_stakeholdergroup')

        # Deleting model 'DataSourceStakeholderGroup'
        db.delete_table('portfolio_datasourcestakeholdergroup')

        # Adding field 'ApplicationUserGroup.application_alias'
        db.add_column('portfolio_applicationusergroup', 'application_alias', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.ApplicationAlias'], null=True, blank=True), keep_default=False)

        # Deleting field 'ApplicationUserGroup.alias'
        db.delete_column('portfolio_applicationusergroup', 'alias_id')

        # Deleting field 'DataSource.known_issues'
        db.delete_column('portfolio_datasource', 'known_issues')

        # Deleting field 'DataSource.pending_changes'
        db.delete_column('portfolio_datasource', 'pending_changes')

        # Removing M2M table for field data_sources on 'Application'
        db.delete_table('portfolio_application_data_sources')


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
        'portfolio.alias': {
            'Meta': {'object_name': 'Alias'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.application': {
            'Meta': {'object_name': 'Application'},
            'business_criticality': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'client_technologies': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['portfolio.ClientTechnology']", 'null': 'True', 'blank': 'True'}),
            'complexity': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'data_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.DataSource']", 'symmetrical': 'False'}),
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
        'portfolio.applicationusergroup': {
            'Meta': {'object_name': 'ApplicationUserGroup'},
            'alias': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Alias']", 'null': 'True', 'blank': 'True'}),
            'application': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Application']"}),
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
        'portfolio.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'annual_data_volume_growth': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'business_criticality': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'complexity': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'data_source_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.DataSourceType']"}),
            'data_volume': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'document_completeness': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'document_freshness': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'hardware_platform': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.HardwarePlatform']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'known_issues': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'life_expectancy': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'maximum_capacity': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pending_changes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['portfolio.UserGroup']", 'through': "orm['portfolio.DataSourceUserGroup']", 'symmetrical': 'False'})
        },
        'portfolio.datasourcestakeholdergroup': {
            'Meta': {'object_name': 'DataSourceStakeholderGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stakeholder_role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.StakeholderRole']"})
        },
        'portfolio.datasourcetype': {
            'Meta': {'object_name': 'DataSourceType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Vendor']"})
        },
        'portfolio.datasourceusergroup': {
            'Meta': {'object_name': 'DataSourceUserGroup'},
            'alias': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Alias']", 'null': 'True', 'blank': 'True'}),
            'data_source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.DataSource']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.UserGroup']"})
        },
        'portfolio.hardwareplatform': {
            'Meta': {'object_name': 'HardwarePlatform'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Vendor']"})
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
        'portfolio.stakeholdergroup': {
            'Meta': {'object_name': 'StakeholderGroup'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'portfolio.stakeholderrole': {
            'Meta': {'object_name': 'StakeholderRole'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['portfolio.Client']"}),
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
        },
        'portfolio.vendor': {
            'Meta': {'object_name': 'Vendor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['portfolio']
