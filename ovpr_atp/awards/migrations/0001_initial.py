# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Award'
        db.create_table(u'awards_award', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('creation_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('imported_from_lotus', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('first_proposal', self.gf('django.db.models.fields.related.OneToOneField')(related_name='award_first_proposal', null=True, on_delete=models.SET_NULL, to=orm['awards.Proposal'], blank=True, unique=True)),
            ('award_acceptance_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('award_negotiation_user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('award_setup_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('subaward_user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='+', null=True, to=orm['auth.User'])),
            ('award_management_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('award_closeout_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['auth.User'])),
            ('subaward_done', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('award_management_done', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'awards', ['Award'])

        # Adding model 'ProposalIntake'
        db.create_table(u'awards_proposalintake', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('award', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['awards.Award'], unique=True, null=True, blank=True)),
            ('principal_investigator', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('prime_sponsor', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agency', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('program_announcement', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('announcement_link', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('proposal_due_to_sponsor', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('proposal_due_to_ovpr', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('proposal_due_to_aor', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('spa1', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('phs_funded', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('fcoi_submitted', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('proposal_outcome', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('jit_request', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('jit_response_submitted', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'awards', ['ProposalIntake'])

        # Adding model 'PrincipalInvestigator'
        db.create_table(u'awards_principalinvestigator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prefix_name', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('suffix_name', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('street1', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('street2', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('state', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('country', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('organization_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('department_name', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('division_name', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('employee_id', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('pi_status', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
        ))
        db.send_create_signal(u'awards', ['PrincipalInvestigator'])

        # Adding model 'Proposal'
        db.create_table(u'awards_proposal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('award', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Award'], null=True, blank=True)),
            ('dummy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_first_proposal', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('principal_investigator', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['awards.PrincipalInvestigator'], unique=True, null=True, on_delete=models.SET_NULL, blank=True)),
            ('lotus_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('employee_id', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('proposal_id', self.gf('django.db.models.fields.BigIntegerField')(unique=True, null=True, blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('opportunity_id', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('opportunity_title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cfda_number', self.gf('django.db.models.fields.CharField')(max_length=16, blank=True)),
            ('department_code', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('submission_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('sponsor_deadline', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('calendar_months', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('academic_months', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('summer_months', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('is_status_waiver_required', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_signed_ip_waiver_attached', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_signed_coi_disc_attached', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_agency_cert_doc_attached', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_cost_shr_auth_attached', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('agency_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('project_title', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('is_subcontract', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('who_is_prime', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('proposal_type', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('agency_type', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('application_type_code', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('federal_identifier', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('is_change_in_grantee_inst', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('project_type', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('responsible_entity', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('departmental_id_primary', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('departmental_id_secondary', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('departmental_name_primary', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('departmental_name_secondary', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('departmental_contact_info', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('are_vertebrate_animals_used', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_iacuc_review_pending', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('iacuc_protocol_number', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('iacuc_approval_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('are_human_subjects_used', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_irb_review_pending', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('irb_protocol_number', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('irb_review_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('is_haz_mat', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('budget_first_per_start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('budget_first_per_end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('project_start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('project_end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('cost_shr_mand_is_committed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cost_shr_mand_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('cost_shr_mand_source', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('cost_shr_vol_is_committed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cost_shr_vol_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('cost_shr_vol_source', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('will_involve_foreign_nationals', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('will_involve_shipment', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('will_involve_foreign_contract', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('award_proposal_status', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('sponsor_type', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('sponsor_name', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('sponsor_subdivision1', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('sponsor_subdivision2', self.gf('django.db.models.fields.CharField')(max_length=256, blank=True)),
            ('naics_code', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('tracking_number', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('duns_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('total_costs', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y5', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y7', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y8', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_costs_y10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y5', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y7', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y8', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_direct_costs_y10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y5', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y7', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y8', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('total_indirect_costs_y10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'awards', ['Proposal'])

        # Adding model 'KeyPersonnel'
        db.create_table(u'awards_keypersonnel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proposal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Proposal'])),
            ('employee_id', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=64, blank=True)),
            ('middle_name', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('project_role', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('calendar_months', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True)),
            ('academic_months', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True)),
            ('summer_months', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=3, blank=True)),
            ('effort', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'awards', ['KeyPersonnel'])

        # Adding model 'PerformanceSite'
        db.create_table(u'awards_performancesite', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('proposal', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Proposal'])),
            ('ps_organization', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ps_duns', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('ps_street1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ps_street2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ps_city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ps_state', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('ps_zipcode', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('ps_country', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
        ))
        db.send_create_signal(u'awards', ['PerformanceSite'])

        # Adding model 'AwardAcceptance'
        db.create_table(u'awards_awardacceptance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('award', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Award'])),
            ('current_modification', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('eas_status', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('phs_funded', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('fcoi_cleared_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('foreign_travel', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('full_f_a_recovery', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('mfa_investigators', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('admin_establishment', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('expedited_review', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('major_project', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('award_acceptance_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('award_issue_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sponsor_award_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('agency_award_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('award_direct_costs', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y5', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y7', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y8', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_direct_costs_y10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y5', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y7', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y8', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_indirect_costs_y10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y1', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y2', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y3', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y5', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y6', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y7', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y8', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y9', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('award_total_costs_y10', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('reduction_in_budget', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('contracting_official', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('gmo_co_phone_number', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('gmo_co_email', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('record_destroy_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('tdc_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
            ('mtdc_rate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=15, decimal_places=2, blank=True)),
        ))
        db.send_create_signal(u'awards', ['AwardAcceptance'])

        # Adding model 'AwardNegotiation'
        db.create_table(u'awards_awardnegotiation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('award', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Award'])),
            ('current_modification', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('subcontracting_plan', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('under_master_agreement', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('award_type', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('other_award_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('related_other_agreements', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('related_other_comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('negotiator', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('date_received', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('retention_period', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('gw_doesnt_own_ip', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('gw_background_ip', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('negotiation_status', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('negotiation_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('foreign_restrictions', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('certificates_insurance', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('insurance_renewal', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('government_property', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('data_security_restrictions', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('everify', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('publication_restriction', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'awards', ['AwardNegotiation'])

        # Adding model 'AwardSetup'
        db.create_table(u'awards_awardsetup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('award', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['awards.Award'], unique=True)),
            ('financial_reporting_req', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=14, blank=True)),
            ('financial_reporting_oth', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('technical_reporting_req', self.gf('multiselectfield.db.fields.MultiSelectField')(max_length=14, blank=True)),
            ('technical_reporting_oth', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('patent_reporting_req', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('invention_reporting_req', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('property_reporting_req', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('equipment_reporting_req', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('final_reports_due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('expanded_authority', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('budget_restrictions', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('setup_status', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('sp_type', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('award_setup_complete', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('included_gw_organizations', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('total_amount_organization', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('banner_number', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('cs_banner_number', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('qa_screening_complete', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('pre_award_spending_auth', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'awards', ['AwardSetup'])

        # Adding model 'PTANumber'
        db.create_table(u'awards_ptanumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('award', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Award'])),
            ('project_number', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('task_number', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('award_number', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('total_pta_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('organization_number', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'awards', ['PTANumber'])

        # Adding model 'Subaward'
        db.create_table(u'awards_subaward', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('award', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Award'])),
            ('recipient', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('agreement_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('modification_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('subrecipient_type', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('assist', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('date_received', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('risk', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('subaward_ready', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('gw_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('contact_information', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('subaward_start', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('subaward_end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('funding_mechanism', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('other_mechanism', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('approval_expiration', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('debarment_check', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('international', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('sent', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('reminder', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('cfda_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('received', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fcoi_cleared', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('citi_cleared', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ffata_reportable', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('duns_number', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('date_fully_executed', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'awards', ['Subaward'])

        # Adding model 'AwardManagement'
        db.create_table(u'awards_awardmanagement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('award', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['awards.Award'], unique=True)),
            ('next_budget_funded', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('funded_amount', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('gra_grf_included', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('gra_grf_supported', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rcr_training_required', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('rcr_training_complete', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'awards', ['AwardManagement'])

        # Adding model 'PriorApproval'
        db.create_table(u'awards_priorapproval', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('award', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Award'])),
            ('request', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('date_submitted', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('date_approved', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'awards', ['PriorApproval'])

        # Adding model 'ReportSubmission'
        db.create_table(u'awards_reportsubmission', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('award', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Award'])),
            ('report', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('submitted_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'awards', ['ReportSubmission'])

        # Adding model 'AwardCloseout'
        db.create_table(u'awards_awardcloseout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('award', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['awards.Award'], unique=True)),
        ))
        db.send_create_signal(u'awards', ['AwardCloseout'])

        # Adding model 'FinalReport'
        db.create_table(u'awards_finalreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('award', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['awards.Award'])),
            ('report', self.gf('django.db.models.fields.CharField')(max_length=2, blank=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('submitted_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'awards', ['FinalReport'])


    def backwards(self, orm):
        # Deleting model 'Award'
        db.delete_table(u'awards_award')

        # Deleting model 'ProposalIntake'
        db.delete_table(u'awards_proposalintake')

        # Deleting model 'PrincipalInvestigator'
        db.delete_table(u'awards_principalinvestigator')

        # Deleting model 'Proposal'
        db.delete_table(u'awards_proposal')

        # Deleting model 'KeyPersonnel'
        db.delete_table(u'awards_keypersonnel')

        # Deleting model 'PerformanceSite'
        db.delete_table(u'awards_performancesite')

        # Deleting model 'AwardAcceptance'
        db.delete_table(u'awards_awardacceptance')

        # Deleting model 'AwardNegotiation'
        db.delete_table(u'awards_awardnegotiation')

        # Deleting model 'AwardSetup'
        db.delete_table(u'awards_awardsetup')

        # Deleting model 'PTANumber'
        db.delete_table(u'awards_ptanumber')

        # Deleting model 'Subaward'
        db.delete_table(u'awards_subaward')

        # Deleting model 'AwardManagement'
        db.delete_table(u'awards_awardmanagement')

        # Deleting model 'PriorApproval'
        db.delete_table(u'awards_priorapproval')

        # Deleting model 'ReportSubmission'
        db.delete_table(u'awards_reportsubmission')

        # Deleting model 'AwardCloseout'
        db.delete_table(u'awards_awardcloseout')

        # Deleting model 'FinalReport'
        db.delete_table(u'awards_finalreport')


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
        u'awards.award': {
            'Meta': {'object_name': 'Award'},
            'award_acceptance_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'award_closeout_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'award_management_done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'award_management_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'award_negotiation_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'award_setup_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['auth.User']"}),
            'creation_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_proposal': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'award_first_proposal'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['awards.Proposal']", 'blank': 'True', 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imported_from_lotus': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'current_modification': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'eas_status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'expedited_review': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'fcoi_cleared_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'foreign_travel': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'full_f_a_recovery': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'gmo_co_email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'gmo_co_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'major_project': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'mfa_investigators': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'mtdc_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'phs_funded': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'record_destroy_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'reduction_in_budget': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sponsor_award_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'tdc_rate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'})
        },
        u'awards.awardcloseout': {
            'Meta': {'object_name': 'AwardCloseout'},
            'award': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.Award']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'awards.awardmanagement': {
            'Meta': {'object_name': 'AwardManagement'},
            'award': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.Award']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'funded_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'gra_grf_included': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'gra_grf_supported': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_budget_funded': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'rcr_training_complete': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'rcr_training_required': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'awards.awardnegotiation': {
            'Meta': {'object_name': 'AwardNegotiation'},
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'award_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'certificates_insurance': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'current_modification': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'data_security_restrictions': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
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
        u'awards.awardsetup': {
            'Meta': {'object_name': 'AwardSetup'},
            'award': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.Award']", 'unique': 'True'}),
            'award_setup_complete': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'banner_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'budget_restrictions': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cs_banner_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'equipment_reporting_req': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'expanded_authority': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'final_reports_due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'financial_reporting_oth': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'financial_reporting_req': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '14', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'included_gw_organizations': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'invention_reporting_req': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'patent_reporting_req': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'pre_award_spending_auth': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'property_reporting_req': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'qa_screening_complete': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'setup_status': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'sp_type': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'technical_reporting_oth': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'technical_reporting_req': ('multiselectfield.db.fields.MultiSelectField', [], {'max_length': '14', 'blank': 'True'}),
            'total_amount_organization': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'awards.finalreport': {
            'Meta': {'object_name': 'FinalReport'},
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']"}),
            'due_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'submitted_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
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
            'ps_state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ps_street1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ps_street2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ps_zipcode': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        },
        u'awards.principalinvestigator': {
            'Meta': {'object_name': 'PrincipalInvestigator'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'country': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'department_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'division_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'employee_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'organization_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'pi_status': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'prefix_name': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'state': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'street1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'street2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'suffix_name': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
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
            'Meta': {'object_name': 'Proposal'},
            'academic_months': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'agency_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'agency_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'application_type_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'are_human_subjects_used': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'are_vertebrate_animals_used': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'award': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['awards.Award']", 'null': 'True', 'blank': 'True'}),
            'award_proposal_status': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'budget_first_per_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'budget_first_per_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'calendar_months': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'cfda_number': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cost_shr_mand_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'cost_shr_mand_is_committed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost_shr_mand_source': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'cost_shr_vol_amount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '15', 'decimal_places': '2', 'blank': 'True'}),
            'cost_shr_vol_is_committed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cost_shr_vol_source': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'department_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'departmental_contact_info': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'departmental_id_primary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'departmental_id_secondary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'departmental_name_primary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'departmental_name_secondary': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'dummy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'duns_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'employee_id': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'federal_identifier': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'iacuc_approval_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'iacuc_protocol_number': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'irb_protocol_number': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'irb_review_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'is_agency_cert_doc_attached': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_change_in_grantee_inst': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_cost_shr_auth_attached': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_first_proposal': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_haz_mat': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_iacuc_review_pending': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_irb_review_pending': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_signed_coi_disc_attached': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_signed_ip_waiver_attached': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_status_waiver_required': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'is_subcontract': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lotus_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'naics_code': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'opportunity_id': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'opportunity_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'principal_investigator': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.PrincipalInvestigator']", 'unique': 'True', 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'project_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'project_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'proposal_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'proposal_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'responsible_entity': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'sponsor_deadline': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sponsor_name': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'sponsor_subdivision1': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'sponsor_subdivision2': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'sponsor_type': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
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
            'who_is_prime': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'will_involve_foreign_contract': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'will_involve_foreign_nationals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'will_involve_shipment': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'awards.proposalintake': {
            'Meta': {'object_name': 'ProposalIntake'},
            'agency': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'announcement_link': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'award': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['awards.Award']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fcoi_submitted': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jit_request': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'jit_response_submitted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'phs_funded': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'prime_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'principal_investigator': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'organization_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
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
            'date_fully_executed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_received': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'debarment_check': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'duns_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fcoi_cleared': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ffata_reportable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
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