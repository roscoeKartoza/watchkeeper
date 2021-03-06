# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Gateway.error_format'
        db.add_column('sms_gateway', 'error_format', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True), keep_default=False)

        # Adding field 'Gateway.query_balance_url'
        db.add_column('sms_gateway', 'query_balance_url', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True), keep_default=False)

        # Adding field 'Gateway.query_balance_params'
        db.add_column('sms_gateway', 'query_balance_params', self.gf('jsonfield.fields.JSONField')(default='[]'), keep_default=True)

        # Adding field 'Gateway.query_balance_response_format'
        db.add_column('sms_gateway', 'query_balance_response_format', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding unique constraint on 'Gateway', fields ['name']
        db.create_unique('sms_gateway', ['name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'Gateway', fields ['name']
        db.delete_unique('sms_gateway', ['name'])

        # Deleting field 'Gateway.error_format'
        db.delete_column('sms_gateway', 'error_format')

        # Deleting field 'Gateway.query_balance_url'
        db.delete_column('sms_gateway', 'query_balance_url')

        # Deleting field 'Gateway.query_balance_params'
        db.delete_column('sms_gateway', 'query_balance_params')

        # Deleting field 'Gateway.query_balance_response_format'
        db.delete_column('sms_gateway', 'query_balance_response_format')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'rank': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '5'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sms.gateway': {
            'Meta': {'object_name': 'Gateway'},
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'charge_keyword': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'content_keyword': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'error_format': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'query_balance_params': ('jsonfield.fields.JSONField', [], {'default': '[]'}),
            'query_balance_response_format': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'query_balance_url': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'recipient_keyword': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'reply_content': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'reply_date': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'reply_date_format': ('django.db.models.fields.CharField', [], {'default': "'%Y-%m-%d %H:%M:%S'", 'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'reply_sender': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'settings': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'status_date': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'status_date_format': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'status_error_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'status_mapping': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'status_msg_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'status_status': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'success_format': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'uuid_keyword': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        'sms.message': {
            'Meta': {'ordering': "('send_date',)", 'object_name': 'Message'},
            'billed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'delivery_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gateway': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sms.Gateway']", 'null': 'True', 'blank': 'True'}),
            'gateway_charge': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'gateway_message_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'recipient_number': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'reply_callback': ('picklefield.fields.PickledObjectField', [], {'null': 'True', 'blank': 'True'}),
            'send_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sent_sms_messages'", 'to': "orm['auth.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Unsent'", 'max_length': '16'}),
            'status_message': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'uuid': ('uuidfield.fields.UUIDField', [], {'max_length': '36', 'auto': 'True', 'null': 'True', 'blank': 'True'})
        },
        'sms.reply': {
            'Meta': {'object_name': 'Reply'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'replies'", 'to': "orm['sms.Message']"})
        }
    }

    complete_apps = ['sms']
