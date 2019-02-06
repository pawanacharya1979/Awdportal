# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Subaward.date_assigned'
        db.delete_column(u'awards_subaward', 'date_assigned')

        # Adding field 'Subaward.creation_date'
        db.add_column(u'awards_subaward', 'creation_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Proposal.date_assigned'
        db.delete_column(u'awards_proposal', 'date_assigned')

        # Adding field 'Proposal.creation_date'
        db.add_column(u'awards_proposal', 'creation_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'AwardAcceptance.creation_date'
        db.add_column(u'awards_awardacceptance', 'creation_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'AwardAcceptance.date_assigned'
        db.delete_column(u'awards_awardacceptance', 'date_assigned')

        # Deleting field 'ProposalIntake.date_assigned'
        db.delete_column(u'awards_proposalintake', 'date_assigned')

        # Adding field 'ProposalIntake.creation_date'
        db.add_column(u'awards_proposalintake', 'creation_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Subaward.date_assigned'
        db.add_column(u'awards_subaward', 'date_assigned',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Subaward.creation_date'
        db.delete_column(u'awards_subaward', 'creation_date')

        # Adding field 'Proposal.date_assigned'
        db.add_column(u'awards_proposal', 'date_assigned',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Proposal.creation_date'
        db.delete_column(u'awards_proposal', 'creation_date')

        # Deleting field 'AwardAcceptance.creation_date'
        db.delete_column(u'awards_awardacceptance', 'creation_date')

        # Adding field 'AwardAcceptance.date_assigned'
        db.add_column(u'awards_awardacceptance', 'date_assigned',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'ProposalIntake.date_assigned'
        db.add_column(u'awards_proposalintake', 'date_assigned',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ProposalIntake.creation_date'
        db.delete_column(u'awards_proposalintake', 'creation_date')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'awards.allowedcostschedule': {
            'Meta': {'ordering': "['name']", 'object_name': 'AllowedCostSchedule'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'awards.award': {
            'Meta': {'object_name': 'Award'},
            'award_acceptance_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'award_closeout_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'award_management_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'award_management_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'award_negotiation_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'award_setup_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'extracted_to_eas': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'subaward_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'subaward_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'awards.awardacceptance': {
            'Meta': {'object_name': 'AwardAcceptance'},
            'admin_establishment': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'agency_award_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'award_acceptance_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'award_direct_costs': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y5': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y7': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y8': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_direct_costs_y9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y5': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y7': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y8': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_indirect_costs_y9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_issue_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'award_total_costs': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y5': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y7': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y8': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'award_total_costs_y9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contracting_official': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'current_modification': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'eas_status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'expedited_review': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'explanation': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'f_a_rate': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'fcoi_cleared_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'foreign_travel': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'full_f_a_recovery': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'gmo_co_email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gmo_co_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major_project': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'mfa_investigators': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'phs_funded': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'reduction_in_budget': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sponsor_award_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'awards.awardcloseout': {
            'Meta': {'object_name': 'AwardCloseout'},
            'award': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.Award']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_assigned': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'awards.awardmanagement': {
            'Meta': {'object_name': 'AwardManagement'},
            'award': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.Award']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_assigned': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'awards.awardmanager': {
            'Meta': {'object_name': 'AwardManager'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'gwid': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'system_user': ('django.db.models.fields.BooleanField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'})
        },
        u'awards.awardnegotiation': {
            'Meta': {'object_name': 'AwardNegotiation'},
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'award_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'certificates_insurance': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'current_modification': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_security_restrictions': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'date_assigned': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_received': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'everify': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'foreign_restrictions': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'government_property': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'gw_background_ip': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'gw_doesnt_own_ip': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insurance_renewal': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'negotiation_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'negotiation_status': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'negotiator': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'other_award_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'publication_restriction': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'related_other_agreements': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'related_other_comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'retention_period': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'subcontracting_plan': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'under_master_agreement': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'awards.awardorganization': {
            'Meta': {'ordering': "['name']", 'object_name': 'AwardOrganization'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'org_info1_meaning': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'org_info2_meaning': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'organization_type': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'awards.awardsetup': {
            'Meta': {'object_name': 'AwardSetup'},
            'allowed_cost_schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.AllowedCostSchedule']", 'null': 'True', 'blank': 'True'}),
            'award': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.Award']", 'unique': 'True'}),
            'award_setup_complete': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'award_template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.AwardTemplate']", 'null': 'True', 'blank': 'True'}),
            'bill_to_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'billing_events': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'budget_restrictions': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'cfda_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.CFDANumber']", 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'cost_sharing_code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'date_assigned': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'document_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'eas_award_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'equipment_reporting_req': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'expanded_authority': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'federal_negotiated_rate': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.FedNegRate']", 'null': 'True', 'blank': 'True'}),
            'final_reports_due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'financial_reporting_oth': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'financial_reporting_req': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '14', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indirect_cost_schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.IndirectCost']", 'null': 'True', 'blank': 'True'}),
            'invention_reporting_req': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nine_ninety_form_needed': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'onr_administered_code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'patent_reporting_req': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'performance_site': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'pre_award_spending_auth': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'property_equip_code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'property_reporting_req': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'qa_screening_complete': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'record_destroy_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'sp_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'task_location': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'technical_reporting_oth': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'technical_reporting_req': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '14', 'blank': 'True'}),
            'wait_for': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'awards.awardtemplate': {
            'Meta': {'ordering': "['number']", 'object_name': 'AwardTemplate'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'awards.cfdanumber': {
            'Meta': {'ordering': "['flex_value']", 'object_name': 'CFDANumber'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flex_value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150', 'primary_key': 'True'})
        },
        u'awards.easmapping': {
            'Meta': {'unique_together': "(('interface', 'field', 'incoming_value', 'atp_model', 'atp_pk'),)", 'object_name': 'EASMapping'},
            'atp_model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'atp_pk': ('django.db.models.fields.IntegerField', [], {}),
            'field': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'incoming_value': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'interface': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
        },
        u'awards.fednegrate': {
            'Meta': {'ordering': "['description']", 'object_name': 'FedNegRate'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '240'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'flex_value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150', 'primary_key': 'True'})
        },
        u'awards.finalreport': {
            'Meta': {'object_name': 'FinalReport'},
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'submitted_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'awards.fundingsource': {
            'Meta': {'ordering': "['number']", 'object_name': 'FundingSource'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'awards.indirectcost': {
            'Meta': {'ordering': "['rate_schedule']", 'object_name': 'IndirectCost'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'rate_schedule': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'awards.keypersonnel': {
            'Meta': {'object_name': 'KeyPersonnel'},
            'academic_months': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'calendar_months': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'}),
            'effort': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'employee_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'project_role': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'proposal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Proposal']"}),
            'summer_months': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '3', 'blank': 'True'})
        },
        u'awards.performancesite': {
            'Meta': {'object_name': 'PerformanceSite'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'proposal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Proposal']"}),
            'ps_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ps_country': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'ps_duns': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ps_organization': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ps_state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'ps_street1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ps_street2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ps_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'awards.primesponsor': {
            'Meta': {'ordering': "['name']", 'object_name': 'PrimeSponsor'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        },
        u'awards.priorapproval': {
            'Meta': {'object_name': 'PriorApproval'},
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'date_approved': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_submitted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'})
        },
        u'awards.proposal': {
            'Meta': {'object_name': 'Proposal', 'index_together': "[['award', 'is_first_proposal']]"},
            'academic_months': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'agency_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.FundingSource']", 'null': 'True', 'blank': 'True'}),
            'agency_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'application_type_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'are_human_subjects_used': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'are_vertebrate_animals_used': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'budget_first_per_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'budget_first_per_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'calendar_months': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cost_shr_mand_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'cost_shr_mand_is_committed': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'cost_shr_mand_source': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'cost_shr_vol_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'cost_shr_vol_is_committed': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'cost_shr_vol_source': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'department_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.AwardOrganization']", 'null': 'True', 'blank': 'True'}),
            'departmental_id_primary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'departmental_id_secondary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'departmental_name_primary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'departmental_name_secondary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'division_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'dummy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'duns_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'employee_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'federal_identifier': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'iacuc_approval_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'iacuc_protocol_number': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irb_protocol_number': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'irb_review_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_agency_cert_doc_attached': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_change_in_grantee_inst': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_cost_shr_auth_attached': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_first_proposal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_haz_mat': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_iacuc_review_pending': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_irb_review_pending': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_signed_coi_disc_attached': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_signed_ip_waiver_attached': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_status_waiver_required': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'is_subcontract': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'lotus_agency_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'lotus_department_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'lotus_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'naics_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'opportunity_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'opportunity_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'principal_investigator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.AwardManager']", 'null': 'True', 'blank': 'True'}),
            'project_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'project_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'proposal_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'proposal_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'responsible_entity': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'sponsor_deadline': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'submission_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'summer_months': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y5': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y7': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y8': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_costs_y9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y5': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y7': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y8': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_direct_costs_y9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y1': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y10': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y2': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y3': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y5': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y6': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y7': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y8': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'total_indirect_costs_y9': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'tracking_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'who_is_prime': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.PrimeSponsor']", 'null': 'True', 'blank': 'True'}),
            'will_involve_foreign_contract': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'will_involve_foreign_nationals': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'will_involve_shipment': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'awards.proposalintake': {
            'Meta': {'object_name': 'ProposalIntake'},
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'announcement_link': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'award': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.Award']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_received': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fcoi_submitted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'five_days_granted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'five_days_requested': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jit_request': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'jit_response_submitted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'phs_funded': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'prime_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'principal_investigator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.AwardManager']", 'null': 'True', 'blank': 'True'}),
            'program_announcement': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'proposal_due_to_aor': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'proposal_due_to_ovpr': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'proposal_due_to_sponsor': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'proposal_outcome': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'spa1': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'})
        },
        u'awards.ptanumber': {
            'Meta': {'object_name': 'PTANumber'},
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'award_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'banner_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'cs_banner_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'parent_banner_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'principal_investigator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.AwardManager']", 'null': 'True', 'blank': 'True'}),
            'project_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'task_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'total_pta_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        },
        u'awards.reportsubmission': {
            'Meta': {'object_name': 'ReportSubmission'},
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'submitted_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'awards.subaward': {
            'Meta': {'object_name': 'Subaward'},
            'agreement_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'approval_expiration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'assist': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'cfda_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'citi_cleared': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contact_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'date_fully_executed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_received': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'debarment_check': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'duns_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ein': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fain': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fcoi_cleared': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ffata_reportable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'ffata_submitted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'funding_mechanism': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'gw_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'international': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'modification_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'other_mechanism': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'received': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'reminder': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'risk': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'sent': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'subaward_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'subaward_ready': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'subaward_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'subrecipient_type': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'tech_report_due': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'tech_report_received': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['awards']