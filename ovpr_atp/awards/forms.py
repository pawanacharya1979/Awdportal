# encoding=utf8
# Definitions for the form classes used to display the input forms on the site.
# Makes use of crispy-forms for better layout handling.
#
# See Django documentation at https://docs.djangoproject.com/en/1.6/topics/forms/
# See crispy-forms documentation at https://django-crispy-forms.readthedocs.org/en/latest/

from dateutil import tz
from django.contrib.auth.models import User, Group
from django import forms
from django.core.urlresolvers import reverse
from django.db.models import ForeignKey, OneToOneField, Q
from django.forms import ValidationError
from django.forms.widgets import Textarea, DateInput, NumberInput, TextInput, HiddenInput, CheckboxInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Button, ButtonHolder, Submit, Field, Div, Reset, HTML
from crispy_forms.bootstrap import TabHolder, Tab, StrictButton, FormActions

from .models import (
    ProposalIntake,
    Proposal,
    KeyPersonnel,
    PerformanceSite,
    Award,
    AwardAcceptance,
    AwardNegotiation,
    AwardSetup,
    PTANumber,
    Subaward,
    AwardManagement,
    PriorApproval,
    ReportSubmission,
    AwardCloseout,
    FinalReport,
    NegotiationStatus,
    ReportIDS,
    TermsAndConditionsIDS,
    TermsAndConditions, )


class AwardForm(forms.ModelForm):
    """Used for creating awards"""

    def __init__(self, *args, **kwargs):
        super(AwardForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'awardForm'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-3'
        self.helper.layout = Layout(
            'award_acceptance_user',
            'award_negotiation_user',
            'award_setup_user',
            'award_modification_user',
            'quality_assurance_user',
            'subaward_user',
            'award_management_user',
            'award_closeout_user',
            HTML("<div class='pull-right'>"),
            FormActions(
                HTML('<a href="javascript:history.back()" class="btn">Cancel</a>'),
                Submit(
                    'save',
                    'Create award'),
            ),
            HTML("</div>"),
        )

        # Update the label_from_instance function to get full name instead of
        # just __unicode__
        for field in self.fields.keys():
            if 'user' in field:
                user_field = self.fields[field]
                user_field.label_from_instance = lambda obj: obj.get_full_name()
                user_field.queryset = user_field.queryset.order_by(
                    'first_name')

    class Meta:
        model = Award
        exclude = ['status']


class EditAwardForm(AwardForm):
    """Used for updating assignments on awards"""

    def __init__(self, *args, **kwargs):
        super(EditAwardForm, self).__init__(*args, **kwargs)
        self.helper.layout[-2][-1] = Submit('save', 'Update assignments')


class EASMappingForm(forms.Form):
    """Create a new mapping of EAS data"""

    def __init__(self, atp_model, *args, **kwargs):
        super(EASMappingForm, self).__init__(*args, **kwargs)

        self.fields['atp_value'] = forms.ModelChoiceField(
            queryset=atp_model.objects.filter(
                active=True),
            label='ATP value')

        if atp_model.__name__ in (
                'AwardManager',
                'FundingSource',
                'PrimeSponsor',
                'AwardOrganization'):
            css = 'select2 award-manager-select'
        else:
            css = 'select2'

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-3'
        self.helper.layout = Layout(
            Field(
                'atp_value',
                css_class=css),
            HTML("<div class='pull-right'>"),
            FormActions(
                HTML('<a href="{{ award_url|default:"/"}}" class="btn">Cancel</a>'),
                Submit(
                    'save',
                    'Continue with import'),
            ),
            HTML("</div>"),
        )


class PTANumberAutoFormMixin(object):
    """Dynamically populate django-crispy-form Layouts in a two-column format"""

    def _layout_fields(self, fields):
        fields_in_row = 0
        layout = []
        if self.Meta.model == TermsAndConditionsIDS and not self.instance.id:
            layout.append(
                HTML(
                    "<div class='disp-notes'><p><b style='color:red'>Note:</b> 1. PROPERTY & EQUIPMENT is required on every award</p>" \
                    "<p style='margin-left: 40px;'> 2. GUIDANCE is required for every Federal award (at least for the next 2 years)</p></br></div>"))

        layout.append(HTML('<div class="row">'))

        for field_name, field_value in fields:
            if field_name == 'qa_comments':
                try:
                    if self.instance.award.assigned_to_qa or self.instance.qa_comments:
                        self.comment_field = Field(field_name)
                except:
                    pass

            elif isinstance(field_value.widget, DateInput):
                layout.append(
                    Div(Field(field_name, css_class='datePicker'), css_class='col-md-4'))
                fields_in_row += 1

            elif isinstance(field_value.widget, CheckboxInput):
                try:
                    if self.instance.award.assigned_to_qa and self.instance.award.status == 3:
                        layout.append(
                            Div(Field(field_name), css_class='col-md-1'))
                        fields_in_row += 1
                    elif self.instance.award.qa_complete:
                        layout.append(
                            Div(Field(field_name, disabled=True), css_class='col-md-1'))
                        fields_in_row += 1
                    else:
                        layout.append(
                            Div(Field(field_name, disabled=True), css_class='col-md-1'))
                        fields_in_row += 1
                except:
                    pass

            elif isinstance(field_value.widget, Textarea):
                layout.append(HTML('</div>'))
                layout.append(
                    Div(Div(Field(field_name), css_class="col-md-10"), css_class="row"))
                layout.append(HTML('<div class="row">'))
                fields_in_row = 0

            elif isinstance(field_value.widget, HiddenInput):
                layout.append(
                    Field(field_name))

            elif field_name != 'move_to_next_step' and type(self.Meta.model._meta.get_field(field_name)) in (
            ForeignKey, OneToOneField):
                if self.Meta.model._meta.get_field(field_name).rel.to.__name__ in (
                        'AwardManager',
                        'FundingSource',
                        'PrimeSponsor',
                        'AwardOrganization'):
                    css = 'select2 award-manager-select'
                else:
                    css = 'select2'
                layout.append(
                    Div(Field(field_name, css_class=css), css_class='col-md-4'))

                fields_in_row += 1

            else:
                # Make sure we don't render any numberinput widgets (they cause
                # unnecessarily complicated browser validation)
                if isinstance(field_value.widget, NumberInput):
                    field_value.widget = TextInput()
                    layout.append(
                        Div(Field(field_name, css_class='number-input'), css_class='col-md-4'))
                else:
                    layout.append(Div(Field(field_name), css_class='col-md-4'))

                fields_in_row += 1

            if fields_in_row == 4:
                layout.append(HTML('</div><div class="row">'))
                fields_in_row = 0

        # Close the last open row
        layout.append(HTML('</div>'))

        return layout

    def __init__(self, *args, **kwargs):
        super(PTANumberAutoFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'section-form'
        self.helper.disable_csrf = True
        self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-md-4'
        # self.helper.field_class = 'col-md-3'
        self.helper.form_error_title = 'Errors'
        self.helper.layout = Layout()

        # Open the layout with a container and a row
        self.helper.layout.append(HTML('<div class="container">'))

        # Dynamically populate crispy layout with all our form fields
        all_fields = self.fields.copy()
        field_dict = dict(all_fields)
        self.comment_field = None

        self.helper.layout.append(HTML('<br />'))
        self.helper.layout.extend(self._layout_fields(all_fields.items()))


        # Comment field should always be last in field list
        if self.comment_field:
            self.helper.layout.append(
                Div(Div(self.comment_field, css_class="col-md-10"), css_class="row"))

        # Close the open container
        self.helper.layout.append(HTML('</div>'))


class AutoFormMixin(object):
    """Dynamically populate django-crispy-form Layouts in a two-column format"""

    def _layout_fields(self, fields):
        fields_in_row = 0
        layout = []
        if self.Meta.model == TermsAndConditionsIDS and not self.instance.id:
            layout.append(
                HTML(
                    "<div class='disp-notes'><p><b style='color:red'>Note:</b> 1. PROPERTY & EQUIPMENT is required on every award</p>" \
                    "<p style='margin-left: 40px;'> 2. GUIDANCE is required for every Federal award (at least for the next 2 years)</p></br></div>"))

        layout.append(HTML('<div class="row">'))

        for field_name, field_value in fields:
            if field_name == 'award_setup_priority':
                layout.append(Div(Field(field_name), css_class='col-md-5'))
                content = ' 1. Awards/modifications that have billing or reporting requirements that are ≤ 30 days ' \
                          'from the time of receipt or execution. </br> 2. Awards/modifications that have been ' \
                          'executed with an effective date that is ≥ 60 days after performance period start date or ' \
                          'budget period; whichever is applicable. </br> 3. Awards/modifications that have pending ' \
                          'revenue or checks that have been received that are ≥ 45 days after the time of receipt.</br>' \
                          '4. Awards/modifications that have been pending execution ≥ 90 days.</br> ' \
                          '5. Awards/modifications that alleviate failed funds or suspense accounts ≥30 days.</br>' \
                          '9. Awards/modifications that are of Normal priority.'
                content = content.decode('utf-8')
                layout.append(Div(
                    HTML('<div id="popup"><a href="#" id="close_popup_top" style="margin-left: 520px;">X</a><p>%s</p>'
                         '<a href="#" id="close_popup" style="margin-left: 250px;">Close</a></div>'
                         '<a href="#popup" id="open_popup">Award Setup Priority Definitions </a> ' % content),
                    css_class='col-md-5', style='border-left-width: 0px; left: 200px;'))
                layout.append(HTML('</div><div class="row">'))

            elif field_name == 'comments':
                self.comment_field = Field(field_name)

            elif field_name == 'qa_comments':
                try:
                    if self.instance.award.assigned_to_qa or self.instance.qa_comments:
                        self.comment_field = Field(field_name)
                except:
                    pass

            elif field_name == 'wait_for_reson':
                layout.append(Div(Field(field_name), css_class="col-md-5"))
                layout.append(HTML('</div><div class="row">'))
                fields_in_row = 0

            elif field_name == 'spa1':
                layout.append(Div(Field(field_name), css_class="col-md-5"))
                layout.append(HTML('</div><div class="row">'))
                fields_in_row = 0

            elif isinstance(field_value.widget, DateInput):
                layout.append(
                    Div(Field(field_name, css_class='datePicker'), css_class='col-md-5'))
                fields_in_row += 1

            elif isinstance(field_value.widget, CheckboxInput):
                try:
                    if self.instance.award.assigned_to_qa and self.instance.award.status == 3:
                        layout.append(
                            Div(Field(field_name), css_class='col-md-1'))
                        fields_in_row += 1
                    elif self.instance.award.qa_complete:
                        layout.append(
                            Div(Field(field_name, disabled=True), css_class='col-md-1'))
                        fields_in_row += 1
                    else:
                        layout.append(
                            Div(Field(field_name, disabled=True), css_class='col-md-1'))
                        fields_in_row += 1
                except:
                    pass

                try:
                    if self.Meta.model == ReportIDS or self.Meta.model == TermsAndConditionsIDS:
                        layout.append(
                            Div(Field(field_name), css_class='col-md-1'))
                        fields_in_row += 1

                    elif self.instance.pta_number.award.qa_complete:
                        layout.append(
                            Div(Field(field_name, disabled=True), css_class='col-md-1'))
                        fields_in_row += 1

                    else:
                        layout.append(
                            Div(Field(field_name, disabled=True), css_class='col-md-1'))
                        fields_in_row += 1
                except:
                    pass

            elif isinstance(field_value.widget, Textarea):
                layout.append(HTML('</div>'))
                layout.append(
                    Div(Div(Field(field_name), css_class="col-md-10"), css_class="row"))
                layout.append(HTML('<div class="row">'))
                fields_in_row = 0

            elif isinstance(field_value.widget, HiddenInput):
                layout.append(
                    Field(field_name))

            elif isinstance(field_value.widget, CheckboxInput) and self.Meta.model == PTANumber:
                pass

            elif field_name != 'move_to_next_step' and type(self.Meta.model._meta.get_field(field_name)) in (
            ForeignKey, OneToOneField):
                if self.Meta.model._meta.get_field(field_name).rel.to.__name__ in (
                        'AwardManager',
                        'FundingSource',
                        'PrimeSponsor',
                        'AwardOrganization'):
                    css = 'select2 award-manager-select'
                else:
                    css = 'select2'
                layout.append(
                    Div(Field(field_name, css_class=css), css_class='col-md-5'))

                fields_in_row += 1

            else:
                # Make sure we don't render any numberinput widgets (they cause
                # unnecessarily complicated browser validation)
                if isinstance(field_value.widget, NumberInput):
                    field_value.widget = TextInput()
                    layout.append(
                        Div(Field(field_name, css_class='number-input'), css_class='col-md-5'))
                else:
                    layout.append(Div(Field(field_name), css_class='col-md-5'))

                fields_in_row += 1

            if fields_in_row == 2:
                layout.append(HTML('</div><div class="row">'))
                fields_in_row = 0

        # Close the last open row
        layout.append(HTML('</div>'))

        return layout

    def __init__(self, *args, **kwargs):
        super(AutoFormMixin, self).__init__(*args, **kwargs)
        self.ptanum = kwargs.get("initial").get("pta_number") if kwargs.get("initial") else None
        self.form_name = kwargs.get("initial").get("form_name") if kwargs.get("initial") else None
        self.helper = FormHelper()
        self.helper.form_id = 'section-form'
        self.helper.disable_csrf = True
        self.helper.form_class = 'form-horizontal'
        if self.Meta.model == ReportIDS or self.Meta.model == TermsAndConditionsIDS:
            pass
        else:
            self.helper.label_class = 'col-md-5'
            self.helper.field_class = 'col-md-7'
        self.helper.form_error_title = 'Errors'
        self.helper.layout = Layout()
        if self.Meta.model == ReportIDS and self.form_name == "ReportsFormCreate":

            ptanum_obj = self.ptanum
            # pta_number = str(self.ptanum)
            award_template = str(ptanum_obj.award_template)
            project_number = str(ptanum_obj.project_number)
            task_number = str(ptanum_obj.task_number)
            award_number = str(ptanum_obj.award_number)
            award_setup_complete = str(ptanum_obj.award_setup_complete)
            total_pta_amount = str(ptanum_obj.total_pta_amount)
            parent_banner_number = str(ptanum_obj.parent_banner_number)
            banner_number = str(ptanum_obj.banner_number)
            cs_banner_number = str(ptanum_obj.cs_banner_number)
            project_title = str(ptanum_obj.project_title)
            eas_award_type = str(ptanum_obj.eas_award_type)
            eas_award_type = dict(PTANumber.EAS_AWARD_CHOICES).get(eas_award_type)
            preaward_date = str(ptanum_obj.preaward_date)
            start_date = str(ptanum_obj.start_date)
            end_date = str(ptanum_obj.end_date)
            final_reports_due_date = str(ptanum_obj.final_reports_due_date)
            sp_type = str(ptanum_obj.sp_type)
            sp_type = dict(PTANumber.SP_TYPE_CHOICES).get(sp_type)
            short_name = str(ptanum_obj.short_name)
            agency_award_number = str(ptanum_obj.agency_award_number)
            sponsor_award_number = str(ptanum_obj.sponsor_award_number)
            sponsor_banner_number = str(ptanum_obj.sponsor_banner_number)
            eas_status = str(ptanum_obj.eas_status)
            eas_status = dict(PTANumber.EAS_STATUS_CHOICES).get(eas_status)
            ready_for_eas_setup = str(ptanum_obj.ready_for_eas_setup)
            ready_for_eas_setup = dict(PTANumber.EAS_SETUP_CHOICES).get(ready_for_eas_setup)
            # is_edited = str(ptanum_obj.is_edited)
            # pta_number_updated = str(ptanum_obj.pta_number_updated)
            agency_name = str(ptanum_obj.agency_name)
            allowed_cost_schedule = str(ptanum_obj.allowed_cost_schedule)
            # award_id = str(ptanum_obj.award_id)
            # award_template = str(pta_obj.award_template.number) + "-" + str(pta_obj.award_template.short_name)
            cfda_number = str(ptanum_obj.cfda_number)
            department_name = str(ptanum_obj.department_name)
            federal_negotiated_rate = str(ptanum_obj.federal_negotiated_rate)
            indirect_cost_schedule = str(ptanum_obj.indirect_cost_schedule)
            principal_investigator = str(ptanum_obj.principal_investigator)
            who_is_prime = str(ptanum_obj.who_is_prime)
            award_lov = str(ptanum_obj.award_lov)
            award_lov = dict(PTANumber.AWARD_CHOICES).get(award_lov)
            tasks_lov = str(ptanum_obj.tasks_lov)
            tasks_lov = dict(PTANumber.TASKS_CHOICES).get(tasks_lov)
            HTML1 = "<style>table, th, td {border: 0px solid black; width: 100%; border-collapse: collapse;}th, td {padding: 5px; font-size: 10px; text-align: left;}</style>"
            HTML1 += '<table><tbody><tr><th >Project #</th><th >Task #</th><th >Award #</th><th >Award Setup Complete</th><th >Total PTA Amt</th><th >Prnt Banner #</th><th >Banner #</th><th >CS Banner #</th><th >PI*</th><th >Agency Name*</th><th >Department Code & Name*</th><th >Project Title*</th><th >Who is Prime</th><th >Allowed Cost Schedule*</th><th >Award Template*</th><th >CFDA number*</th><th >EAS Award Type* </th></tr><tr><td >' + str(
                project_number).replace('None', '') + '</td><td >' + str(task_number).replace('None',
                                                                                              '') + '</td><td >' + str(
                award_number).replace('None', '') + '</td><td >' + str(award_setup_complete).replace('None',
                                                                                                     '') + '</td><td >' + str(
                total_pta_amount).replace('None', '') + '</td><td >' + str(parent_banner_number).replace('None',
                                                                                                         '') + '</td><td >' + str(
                banner_number).replace('None', '') + '</td><td >' + str(cs_banner_number).replace('None',
                                                                                                  '') + '</td><td >' + str(
                principal_investigator).replace('None', '') + '</td><td >' + str(agency_name).replace('None',
                                                                                                      '') + '</td><td >' + str(
                department_name).replace('None', '') + '</td><td >' + str(project_title).replace('None',
                                                                                                 '') + '</td><td >' + str(
                who_is_prime).replace('None', '') + '</td><td >' + str(allowed_cost_schedule).replace('None',
                                                                                                      '') + '</td><td >' + str(
                award_template).replace('None', '') + '</td><td >' + str(cfda_number).replace('None',
                                                                                              '') + '</td><td >' + str(
                eas_award_type).replace('None',
                                        '') + '</td></tr><tr><th >Preaward date</th><th >Start Date*</th><th >End Date*</th><th >Final Reports/Final Invoice Due Date (Close Date)* </th><th >Federal Negotiated Rate*</th><th >Indirect Cost Schedule*</th><th >SP Type*</th><th >Award Short Name*</th><th >Agency Award Number*</th><th >Prime Award # (if GW is subawardee)*</th><th >Sponsor banner number</th><th >EAS Status*</th><th >Ready for EAS Setup?</th><th >Award*</th><th >Tasks*</th></tr><tr><td >' + str(
                preaward_date).replace('None', '') + '</td><td >' + str(start_date).replace('None',
                                                                                            '') + '</td><td >' + str(
                end_date).replace('None', '') + '</td><td >' + str(final_reports_due_date).replace('None',
                                                                                                   '') + '</td><td >' + str(
                federal_negotiated_rate).replace('None', '') + '</td><td >' + str(indirect_cost_schedule).replace(
                'None', '') + '</td><td >' + str(sp_type).replace('None', '') + '</td><td >' + str(short_name).replace(
                'None', '') + '</td><td >' + str(agency_award_number).replace('None', '') + '</td><td >' + str(
                sponsor_award_number).replace('None', '') + '</td><td >' + str(sponsor_banner_number).replace('None',
                                                                                                              '') + '</td><td >' + str(
                eas_status).replace('None', '') + '</td><td >' + str(ready_for_eas_setup).replace('None',
                                                                                                  '') + '</td><td >' + str(
                award_lov).replace('None', '') + '</td><td >' + str(tasks_lov).replace('None',
                                                                                       '') + '</td></tr></table>'
            self.helper.layout.append(Div(HTML(HTML1)))



        elif self.Meta.model == TermsAndConditionsIDS and self.form_name == "TermsAndConditionsFormCreate":
            ptanum_obj = self.ptanum
            # pta_number = str(self.ptanum)
            award_template = str(ptanum_obj.award_template)
            project_number = str(ptanum_obj.project_number)
            task_number = str(ptanum_obj.task_number)
            award_number = str(ptanum_obj.award_number)
            award_setup_complete = str(ptanum_obj.award_setup_complete)
            total_pta_amount = str(ptanum_obj.total_pta_amount)
            parent_banner_number = str(ptanum_obj.parent_banner_number)
            banner_number = str(ptanum_obj.banner_number)
            cs_banner_number = str(ptanum_obj.cs_banner_number)
            project_title = str(ptanum_obj.project_title)
            eas_award_type = str(ptanum_obj.eas_award_type)
            eas_award_type = dict(PTANumber.EAS_AWARD_CHOICES).get(eas_award_type)
            preaward_date = str(ptanum_obj.preaward_date)
            start_date = str(ptanum_obj.start_date)
            end_date = str(ptanum_obj.end_date)
            final_reports_due_date = str(ptanum_obj.final_reports_due_date)
            sp_type = str(ptanum_obj.sp_type)
            sp_type = dict(PTANumber.SP_TYPE_CHOICES).get(sp_type)
            short_name = str(ptanum_obj.short_name)
            agency_award_number = str(ptanum_obj.agency_award_number)
            sponsor_award_number = str(ptanum_obj.sponsor_award_number)
            sponsor_banner_number = str(ptanum_obj.sponsor_banner_number)
            eas_status = str(ptanum_obj.eas_status)
            eas_status = dict(PTANumber.EAS_STATUS_CHOICES).get(eas_status)
            ready_for_eas_setup = str(ptanum_obj.ready_for_eas_setup)
            ready_for_eas_setup = dict(PTANumber.EAS_SETUP_CHOICES).get(ready_for_eas_setup)
            # is_edited = str(ptanum_obj.is_edited)
            # pta_number_updated = str(ptanum_obj.pta_number_updated)
            agency_name = str(ptanum_obj.agency_name)
            allowed_cost_schedule = str(ptanum_obj.allowed_cost_schedule)
            # award_id = str(ptanum_obj.award_id)
            # award_template = str(pta_obj.award_template.number) + "-" + str(pta_obj.award_template.short_name)
            cfda_number = str(ptanum_obj.cfda_number)
            department_name = str(ptanum_obj.department_name)
            federal_negotiated_rate = str(ptanum_obj.federal_negotiated_rate)
            indirect_cost_schedule = str(ptanum_obj.indirect_cost_schedule)
            principal_investigator = str(ptanum_obj.principal_investigator)
            who_is_prime = str(ptanum_obj.who_is_prime)
            award_lov = str(ptanum_obj.award_lov)
            award_lov = dict(PTANumber.AWARD_CHOICES).get(award_lov)
            tasks_lov = str(ptanum_obj.tasks_lov)
            tasks_lov = dict(PTANumber.TASKS_CHOICES).get(tasks_lov)
            HTML1 = "<style>table, th, td {border: 0px solid black; width: 100%; border-collapse: collapse;}th, td {padding: 5px; font-size: 10px; text-align: left;}</style>"
            HTML1 += '<table><tbody><tr><th >Project #</th><th >Task #</th><th >Award #</th><th >Award Setup Complete</th><th >Total PTA Amt</th><th >Prnt Banner #</th><th >Banner #</th><th >CS Banner #</th><th >PI*</th><th >Agency Name*</th><th >Department Code & Name*</th><th >Project Title*</th><th >Who is Prime</th><th >Allowed Cost Schedule*</th><th >Award Template*</th><th >CFDA number*</th><th >EAS Award Type* </th></tr><tr><td >' + str(
                project_number).replace('None', '') + '</td><td >' + str(task_number).replace('None',
                                                                                              '') + '</td><td >' + str(
                award_number).replace('None', '') + '</td><td >' + str(award_setup_complete).replace('None',
                                                                                                     '') + '</td><td >' + str(
                total_pta_amount).replace('None', '') + '</td><td >' + str(parent_banner_number).replace('None',
                                                                                                         '') + '</td><td >' + str(
                banner_number).replace('None', '') + '</td><td >' + str(cs_banner_number).replace('None',
                                                                                                  '') + '</td><td >' + str(
                principal_investigator).replace('None', '') + '</td><td >' + str(agency_name).replace('None',
                                                                                                      '') + '</td><td >' + str(
                department_name).replace('None', '') + '</td><td >' + str(project_title).replace('None',
                                                                                                 '') + '</td><td >' + str(
                who_is_prime).replace('None', '') + '</td><td >' + str(allowed_cost_schedule).replace('None',
                                                                                                      '') + '</td><td >' + str(
                award_template).replace('None', '') + '</td><td >' + str(cfda_number).replace('None',
                                                                                              '') + '</td><td >' + str(
                eas_award_type).replace('None',
                                        '') + '</td></tr><tr><th >Preaward date</th><th >Start Date*</th><th >End Date*</th><th >Final Reports/Final Invoice Due Date (Close Date)* </th><th >Federal Negotiated Rate*</th><th >Indirect Cost Schedule*</th><th >SP Type*</th><th >Award Short Name*</th><th >Agency Award Number*</th><th >Prime Award # (if GW is subawardee)*</th><th >Sponsor banner number</th><th >EAS Status*</th><th >Ready for EAS Setup?</th><th >Award*</th><th >Tasks*</th></tr><tr><td >' + str(
                preaward_date).replace('None', '') + '</td><td >' + str(start_date).replace('None',
                                                                                            '') + '</td><td >' + str(
                end_date).replace('None', '') + '</td><td >' + str(final_reports_due_date).replace('None',
                                                                                                   '') + '</td><td >' + str(
                federal_negotiated_rate).replace('None', '') + '</td><td >' + str(indirect_cost_schedule).replace(
                'None', '') + '</td><td >' + str(sp_type).replace('None', '') + '</td><td >' + str(short_name).replace(
                'None', '') + '</td><td >' + str(agency_award_number).replace('None', '') + '</td><td >' + str(
                sponsor_award_number).replace('None', '') + '</td><td >' + str(sponsor_banner_number).replace('None',
                                                                                                              '') + '</td><td >' + str(
                eas_status).replace('None', '') + '</td><td >' + str(ready_for_eas_setup).replace('None',
                                                                                                  '') + '</td><td >' + str(
                award_lov).replace('None', '') + '</td><td >' + str(tasks_lov).replace('None',
                                                                                       '') + '</td></tr></table>'
            self.helper.layout.append(Div(HTML(HTML1)))
        # Open the layout with a container and a row
        self.helper.layout.append(HTML('<div class="container">'))

        # Dynamically populate crispy layout with all our form fields
        all_fields = self.fields.copy()
        field_dict = dict(all_fields)
        self.comment_field = None

        if hasattr(self.Meta.model, 'FIELDSETS'):
            for fieldset in self.Meta.model.FIELDSETS:
                fields = []
                for field in fieldset['fields']:
                    if field in field_dict:
                        fields.append((field, field_dict[field]))
                        del all_fields[field]

                # for field, value in all_fields.items():
                #     if field in fieldset['fields']:
                #         fields.append((field, value))
                #         del all_fields[field]

                self.helper.layout.append(
                    HTML(
                        '<h5 class="fieldset-title">%s</h5>' %
                        fieldset['title']))
                self.helper.layout.extend(self._layout_fields(fields))

        self.helper.layout.append(HTML('<br />'))
        self.helper.layout.extend(self._layout_fields(all_fields.items()))

        # Comment field should always be last in field list
        if self.comment_field:
            self.helper.layout.append(
                Div(Div(self.comment_field, css_class="col-md-10"), css_class="row"))

        if self.Meta.model == AwardNegotiation:
            negotiation_trail = NegotiationStatus.objects.filter(award_id=self.instance.award.id,
                                                                 negotiation_status__in=NegotiationStatus.
                                                                 NEGOTIATION_STATUS_CHOICES).order_by(
                '-negotiation_status_date')
            if negotiation_trail:
                from_zone = tz.gettz('UTC')
                to_zone = tz.gettz('America/New_York')
                self.helper.layout.extend([
                    HTML('<div class="row">'),
                    HTML('<div class="col-md-10">'),
                    HTML('<table id="negotiationStatusTable" class="table table-striped table-bordered">'),
                    HTML('<thead>'),
                    HTML('<th width="200px">Date/Time</th>'),
                    HTML('<th width="200px">Negotiation Status</th>'),
                    HTML('<th width="250px">Username</th>'),
                    HTML('<th>Notes</th>'),
                    HTML('</thead>')]
                )
                for award in negotiation_trail:
                    utc = award.negotiation_status_date.replace(tzinfo=from_zone)
                    central = utc.astimezone(to_zone)
                    self.helper.layout.extend([
                        HTML('<tbody>'),
                        HTML('<td>%s</td>' % central.strftime("%B, %d %Y %I:%M%p")),
                        HTML('<td>%s</td>' % award.negotiation_status),
                        HTML('<td>%s</td>' % award.negotiation_status_changed_user),
                        HTML('<td>%s</td>' % award.negotiation_notes),
                        HTML('</tbody>')]
                    )
                self.helper.layout.extend([
                    HTML('</table>'),
                    HTML('</div>'),
                    HTML('</div>')]
                )

        # Close the open container
        self.helper.layout.append(HTML('</div>'))


class AwardSectionForm(AutoFormMixin, forms.ModelForm):
    """Base class for all section forms - includes move_to_next_step field"""

    move_to_next_step = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    move_to_multiple_steps = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)
    do_not_send_to_next_step = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False
    )
    save_and_send_qa = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    return_assignment_submission = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    class Meta:
        exclude = ['award']

        widgets = {
            'date_assigned': forms.TextInput(attrs={'readonly': 'readonly'}),
            'is_edited': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        self.pta_modification_enable = kwargs.pop(
            'pta_modification_enable',
            False
        )
        self.save_and_send_qa = kwargs.pop(
            'save_and_send_qa',
            False
        )
        self.return_assignment_submission = kwargs.pop(
            'return_assignment_submission',
            False
        )
        self.enable_send_to_next_step = kwargs.pop(
            'enable_send_to_next_step',
            False)
        self.send_award_to_multiple_steps_steps = kwargs.pop(
            'send_award_to_multiple_steps_steps',
            False
        )
        self.do_not_send_to_next_step = kwargs.pop(
            'do_not_send_to_next_step', False
        )
        super(AwardSectionForm, self).__init__(*args, **kwargs)
        if self.Meta.model == ProposalIntake:
            user_list = User.objects.filter(is_active=True, groups__name='Proposal Intake').order_by('first_name')
            users = [(user.first_name + ' ' + user.last_name, user.first_name + ' ' + user.last_name) for user in
                     user_list]
            choices = [(self.initial['spa1'], self.initial['spa1']), (u'', u'---------')]
            choices.extend(users)
            self.fields['spa1'].choices = choices
        if self.Meta.model == AwardAcceptance:
            acceptance = AwardAcceptance.objects.get(award_id=self.instance.award.id, current_modification=True)
            if acceptance.award_setup_priority:
                self.initial['award_setup_priority'] = acceptance.award_setup_priority
            else:
                self.initial['award_setup_priority'] = 'ni'
            self.fields['award_setup_priority'].choices = [('on', 1), ('tw', 2), ('th', 3), ('fo', 4), ('fi', 5),
                                                           ('ni', 9)]

        if self.do_not_send_to_next_step:
            self.fields['do_not_send_to_next_step'].initial = True

        form_actions = [
            Reset(
                'reset', 'Cancel'), Submit(
                'save', 'Save changes and continue editing')]

        if self.enable_send_to_next_step:
            form_actions.append(
                StrictButton(
                    'Save and send award to next step',
                    css_id='submit-and-send',
                    css_class='btn btn-success submit-and-send'))
        if self.send_award_to_multiple_steps_steps:
            form_actions.append(
                StrictButton(
                    'Save and Send award to Negotiation & Award Setup',
                    css_id='submit-and-dual-send',
                    css_class='btn btn-success submit-and-dual-send'))
        if not self.pta_modification_enable:
            if 'pta_modification' in self.fields:
                self.fields['pta_modification'].widget = forms.HiddenInput()

        if self.Meta.model == AwardSetup:
            form_actions.insert(
                0,
                HTML('<a href="{% url \'award_setup_report\' award.id %}" class="btn">View EAS Report</a>'))
        if self.Meta.model == AwardSetup and not self.instance.award.assigned_to_qa:
            form_actions.append(
                StrictButton(
                    'Validate and Send to QA',
                    css_id='save-and-send-qa',
                    css_class='btn btn-success save-and-send-qa'))

        if self.Meta.model == AwardSetup and self.instance.award.assigned_to_qa and self.instance.award.status == 3:
            form_actions.append(
                StrictButton(
                    'Return to Award Setup',
                    css_id='return-assignment-submission',
                    css_class='btn btn-success return-assignment-submission'))

        if self.Meta.model == AwardNegotiation and not self.instance.award.award_dual_setup:
            form_actions.append(
                StrictButton(
                    'Save and Close Record',
                    css_id='submit-and-close',
                    css_class='btn btn-primary submit-and-close'))

        self.helper.layout.extend([
            HTML("<div class='pull-right'>"),
            FormActions(*form_actions),
            HTML("</div>"),
        ])

    def clean(self):
        """Check that an object has all its minimum_fields populated if trying to move to the next step"""
        if self.cleaned_data['move_to_next_step'] or self.cleaned_data['move_to_multiple_steps'] or self.cleaned_data[
            'save_and_send_qa']:
            section = self.instance
            validation_errors = []
            if self.cleaned_data.get('save_and_send_qa'):
                if not self.instance.award.quality_assurance_user:
                    validation_errors.append(
                        ValidationError(
                            'You must assign a Quality Assurance User before you can send this award to Quality Assurance.'
                        )
                    )
            if self.cleaned_data.get('move_to_multiple_steps'):
                if not self.instance.award.award_negotiation_user:
                    validation_errors.append(
                        ValidationError(
                            'You must assign a Negotiation User before you can send this award to Negotiation and Award Setup.'
                        )
                    )
            if self.cleaned_data.get('pta_modification'):
                if not self.instance.award.award_modification_user:
                    validation_errors.append(
                        ValidationError(
                            'You must assign a Modification User, Before you can send this award to the next step.'
                        )
                    )
            for field in section.minimum_fields:
                form_value = self.cleaned_data[field]
                if form_value is None or form_value == '':
                    validation_errors.append(
                        ValidationError(
                            'You must provide a value for %s before you can send this award to the next step.' %
                            section._meta.get_field_by_name(field)[0].verbose_name.title(),
                            code='%s-error' %
                                 field))

            if len(validation_errors) > 0:
                raise ValidationError(validation_errors)

        cleaned_data = super(AwardSectionForm, self).clean()
        cleaned_data['is_edited'] = True
        if self.cleaned_data.get('do_not_send_to_next_step'):
            cleaned_data['do_not_send_to_next_step'] = True

        return cleaned_data


class TabsectionFormMixin(object):
    """Base mixin used for all PTANumber Tab sections"""

    def __init__(self, *args, **kwargs):
        super(TabsectionFormMixin, self).__init__(*args, **kwargs)
        self.helper.disable_csrf = True

    def get_parent_url(self):
        if not self.instance.pk:
            return 'javascript:history.back()'

        return reverse(self.parent_edit_url, kwargs={
            'award_pk': self.instance.award.pk})


class SubsectionFormMixin(object):
    """Base mixin used for all award subsections"""

    def __init__(self, *args, **kwargs):
        super(SubsectionFormMixin, self).__init__(*args, **kwargs)
        self.helper.disable_csrf = True

        form_actions = [
            HTML('<a href="{0}" class="btn">Cancel</a>'.format(self.get_parent_url())),
            Submit('save', 'Save Changes'),
            StrictButton(
                'Save and Close',
                css_id='save-and-return',
                css_class='btn btn-primary save-and-return')
        ]
        if self.Meta.model == PTANumber and self.instance.pk and self.instance.award_setup_complete == None:
            form_actions.insert(0, HTML('<a href="javascript:getAwardNumber()" class="btn">Get Award Number</a>'))

        if self.Meta.model == PTANumber:
            form_actions.append(
                Submit('save_validate', 'Save and Validate', css_class='btn btn-primary save-and-validate'))

        self.helper.layout.extend([
            HTML("<div class='pull-right'>"),
            FormActions(*form_actions),
            HTML("</div>"),
        ])

    def get_parent_url(self):
        if not self.instance.pk:
            return 'javascript:history.back()'

        if 'proposal' in self.parent_edit_url:
            return reverse(
                self.parent_edit_url,
                kwargs={
                    'award_pk': self.instance.proposal.award.pk,
                    'proposal_pk': self.instance.proposal.pk})
        else:
            return reverse(
                self.parent_edit_url,
                kwargs={
                    'award_pk': self.instance.award.pk})


class PTASubsectionForm(SubsectionFormMixin, PTANumberAutoFormMixin, forms.ModelForm):
    """Base form class for pta section"""

    return_to_parent = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    def __init__(self, *args, **kwargs):
        super(PTASubsectionForm, self).__init__(*args, **kwargs)
        ptanum = kwargs['instance']
        award = ptanum.award
        if not award.assigned_to_qa and not ptanum.qa_work_flow:
            labels = self.fields.keys()
            for label in labels:
                if 'cbk_' in label:
                    self.fields[label].widget=forms.HiddenInput()

class SubsectionForm(SubsectionFormMixin, AutoFormMixin, forms.ModelForm):
    """Base form class for all award subsections"""

    return_to_parent = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    def __init__(self, *args, **kwargs):
        super(SubsectionForm, self).__init__(*args, **kwargs)


class ProposalIntakeStandaloneForm(AutoFormMixin, forms.ModelForm):
    """A separate form for ProposalIntake objects that aren't associated to an award."""

    save_and_continue = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)
    save_and_add = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    class Meta(AwardSectionForm.Meta):
        model = ProposalIntake
        exclude = ['award', 'five_days_requested', 'five_days_granted']

        widgets = {
            'is_edited': HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProposalIntakeStandaloneForm, self).__init__(*args, **kwargs)
        user_list = User.objects.filter(is_active=True, groups__name='Proposal Intake').order_by('first_name')
        users = [(user.first_name + ' ' + user.last_name, user.first_name + ' ' + user.last_name) for user in
                 user_list]
        if self.instance.id:
            intake_user = ProposalIntake.objects.get(id=self.instance.id)
            # Lock the dropdown values if the proposal status is submitted
            if intake_user.proposal_status == 'SB':
                choices = [(intake_user.spa1, intake_user.spa1)]
                self.fields['spa1'].choices = choices
                self.fields['spa1'].required = False
                self.fields['spa1'].widget.attrs['disabled'] = 'disabled'
            else:
                choices = [(intake_user.spa1, intake_user.spa1), (u'', u'---------')]
                choices.extend(users)
                self.fields['spa1'].choices = choices
                self.fields['spa1'].required = False
        else:
            choices = [(u'', u'---------')]
            choices.extend(users)
            self.fields['spa1'].choices = choices
        self.helper.disable_csrf = True
        self.helper.layout.extend([
            HTML("<div class='pull-right'>"),
            FormActions(
                HTML('<a href="{% url \'home\' %}" class="btn">Cancel</a>'),
                StrictButton(
                    'Save and Continue Editing',
                    css_id='save-and-continue',
                    css_class='btn btn-primary'),
                Submit('save', 'Save and Close'),
                StrictButton(
                    'Save and Add Another',
                    css_id='save-and-add',
                    css_class='btn btn-primary'),
            ),
            HTML("</div>"),
        ])

    def clean(self):
        """Overrides the base clean method to also add a value indicating the ProposalIntake has been edited"""

        cleaned_data = super(ProposalIntakeStandaloneForm, self).clean()
        cleaned_data['is_edited'] = True

        return cleaned_data


class ProposalForm(AutoFormMixin, forms.ModelForm):
    """The form for creating/editing Proposals"""

    class Meta:
        model = Proposal
        exclude = ['award', 'is_first_proposal', 'lotus_id', 'dummy', 'creation_date']

        widgets = {
            'is_edited': HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProposalForm, self).__init__(*args, **kwargs)
        self.helper.disable_csrf = True
        self.helper.layout.extend([
            HTML("<div class='pull-right'>"),
            FormActions(
                HTML('<a href="{% url \'award_detail\' award_pk=award.id %}" class="btn">Cancel</a>'),
                Submit('save', 'Save changes'),
            ),
            HTML("</div>"),
        ])

    def clean(self):
        """Overrides the base clean method to also add a value indicating the Proposal has been edited"""

        cleaned_data = super(ProposalForm, self).clean()
        cleaned_data['is_edited'] = True

        return cleaned_data


class ProposalIntakeForm(AwardSectionForm):
    """The form for editing ProposalIntakes from within an Award"""

    class Meta(AwardSectionForm.Meta):
        model = ProposalIntake
        exclude = AwardSectionForm.Meta.exclude + ['creation_date']


class KeyPersonnelForm(SubsectionForm):
    """The form for creating/editing KeyPersonnel"""

    parent_edit_url = 'edit_proposal'

    class Meta:
        model = KeyPersonnel
        exclude = ['proposal']


class PerformanceSiteForm(SubsectionForm):
    """The form for creating/editing PerformanceSite"""

    parent_edit_url = 'edit_proposal'

    class Meta:
        model = PerformanceSite
        exclude = ['proposal']


class AwardAcceptanceForm(AwardSectionForm):
    """The form for creating/editing AwardAcceptance"""

    class Meta(AwardSectionForm.Meta):
        model = AwardAcceptance
        exclude = AwardSectionForm.Meta.exclude + ['current_modification', 'creation_date',
                                                   'acceptance_completion_date']


class AwardNegotiationForm(AwardSectionForm):
    """The form for creating/editing AwardNegotiation"""

    close_award = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    class Meta(AwardSectionForm.Meta):
        model = AwardNegotiation
        exclude = AwardSectionForm.Meta.exclude + ['current_modification', 'date_assigned',
                                                   'date_received', 'negotiation_completion_date']


class AwardSetupForm(AwardSectionForm):
    """The form for creating/editing AwardSetup"""

    class Meta(AwardSectionForm.Meta):
        model = AwardSetup
        exclude = AwardSectionForm.Meta.exclude + [
            'date_assigned',
            'award_template',
            'short_name',
            'task_location',
            'start_date',
            'end_date',
            'final_reports_due_date',
            'eas_award_type',
            'sp_type',
            'indirect_cost_schedule',
            'allowed_cost_schedule',
            'cfda_number',
            'federal_negotiated_rate',
            'bill_to_address',
            'billing_events',
            'contact_name',
            'phone',
            'financial_reporting_req',
            'financial_reporting_oth',
            'property_equip_code',
            'onr_administered_code',
            'cost_sharing_code',
            'document_number',
            'performance_site',
            'award_setup_complete',
            'qa_screening_complete',
            'ready_for_eas_setup',
            'qa_assign_date',
            'setup_completion_date',
            'date_wait_for_updated',
        ]

        widgets = AwardSectionForm.Meta.widgets
        widgets['award_setup_complete'] = forms.TextInput(attrs={'readonly': 'readonly'})


class PTANumberForm(PTASubsectionForm):
    """The form for editing PTANumber"""

    parent_edit_url = 'edit_award_setup'

    class Meta:
        model = PTANumber
        exclude = ['award', 'is_edited', 'pta_number_updated', 'qa_work_flow']

        widgets = {
            'award_number': forms.TextInput(attrs={'readonly': 'readonly'}),
            'award_setup_complete': forms.TextInput(attrs={'readonly': 'readonly'})
        }


class CreatePTANumberForm(SubsectionForm):
    """The form for creating PTANumber"""

    parent_edit_url = 'edit_award_setup'

    class Meta:
        model = PTANumber
        exclude = ['award', 'is_edited', 'pta_number_updated', 'qa_work_flow']

        widgets = {
            'award_number': forms.TextInput(attrs={'readonly': 'readonly'}),
            'award_setup_complete': forms.TextInput(attrs={'readonly': 'readonly'})
        }


class TabsectionForm(TabsectionFormMixin, AutoFormMixin, forms.ModelForm):
    """Base form class for all award subsections"""

    return_to_parent = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    def __init__(self, *args, **kwargs):
        super(TabsectionForm, self).__init__(*args, **kwargs)
        self.helper.form_id = 'tab-reports'
        instance = kwargs.get('instance')
        if not instance:
            labels = self.fields.keys()
            for label in labels:
                if 'cbk_' in label:
                    self.fields[label].widget=forms.HiddenInput()
        if instance:
            if not instance.pta_number.award.assigned_to_qa and not instance.pta_number.qa_work_flow:
                labels = self.fields.keys()
                for label in labels:
                    if 'cbk_' in label:
                        self.fields[label].widget=forms.HiddenInput()


class ReportsForm(TabsectionForm):
    """The form for creating/editing Reports for PTANumber"""

    parent_edit_url = 'edit_award_setup'

    class Meta:
        model = ReportIDS
        exclude = ['pta_number']

    def __init__(self, *args, **kwargs):
        super(ReportsForm, self).__init__(*args, **kwargs)
        self.fields['frequency'].required = True
        self.fields['due_within_days'].required = True
        self.fields['no_of_copies'].required = True


class TermsAndConditionsForm(TabsectionForm):
    """The form for creating/editing TermsAndConditionsIDS for PTANumber"""

    parent_edit_url = 'edit_award_setup'

    class Meta:
        model = TermsAndConditionsIDS
        exclude = ['pta_number']

    def __init__(self, *args, **kwargs):
        super(TermsAndConditionsForm, self).__init__(*args, **kwargs)
        if self.instance.id:
            CODE_CHOICES = [(u'', u'---------'),]
            tc_codes = TermsAndConditions.objects.filter(active=True, category_id=self.instance.category)
            for cd in tc_codes:
                CODE_CHOICES.append((str(cd.term_code_id), cd.term_code_name))
            self.fields['code'].choices = CODE_CHOICES
        else:
            CATEGORY_CHOICES = [(u'', u'---------'), ]
            CODE_CHOICES = [(u'', u'---------'),]
            tc_codes = TermsAndConditions.objects.filter(active=True).order_by('category_name')
            codes = TermsAndConditions.objects.filter(active=True).values('category_name').distinct()
            codes_list = []
            for cd in codes:
                codes_list.append(cd['category_name'])
            for tc in tc_codes:
                if tc.category_name in codes_list:
                    CATEGORY_CHOICES.append((str(tc.category_id), tc.category_name))
                    codes_list.remove(tc.category_name)
            tc_codes = TermsAndConditions.objects.filter(active=True)
            for cd in tc_codes:
                CODE_CHOICES.append((str(cd.term_code_id), cd.term_code_name))
            self.fields['code'].choices = CODE_CHOICES
            self.fields['category'].choices = CATEGORY_CHOICES


class SubawardListForm(forms.Form):
    """The form for editing the list of all Subawards"""

    move_to_next_step = forms.BooleanField(
        widget=forms.HiddenInput(),
        required=False)

    def __init__(self, *args, **kwargs):
        self.award = kwargs.pop('award')
        super(SubawardListForm, self).__init__(*args, **kwargs)

    def clean(self):
        """Overrides the base clean method to ensure the minimum fields are completed"""

        if self.cleaned_data['move_to_next_step']:
            validation_errors = []

            # We have to check minimum_fields on each subaward
            for subaward in self.award.subaward_set.all():
                for field in subaward.minimum_fields:
                    instance_value = getattr(subaward, field)
                    if instance_value is None or instance_value == '':
                        validation_errors.append(
                            ValidationError(
                                'You must provide a value for %s in %s before you can send this award to the next step.' %
                                (subaward._meta.get_field_by_name(field)[0].verbose_name, subaward),
                                code='%s-%s-error' %
                                     (subaward, field)))

            if len(validation_errors) > 0:
                raise ValidationError(validation_errors)
        return super(SubawardListForm, self).clean()


class AwardManagementForm(AwardSectionForm):
    """The form for creating/editing AwardManagements"""

    class Meta(AwardSectionForm.Meta):
        model = AwardManagement
        exclude = AwardSectionForm.Meta.exclude + ['date_assigned', 'management_completion_date']


class PriorApprovalForm(SubsectionForm):
    """The form for creating/editing PriorApproval"""

    parent_edit_url = 'edit_award_management'

    class Meta:
        model = PriorApproval
        exclude = ['award']


class ReportSubmissionForm(SubsectionForm):
    """The form for creating/editing ReportSubmission"""

    parent_edit_url = 'edit_award_management'

    class Meta:
        model = ReportSubmission
        exclude = ['award']


class AwardCloseoutForm(AwardSectionForm):
    """The form for creating/editing AwardCloseout"""

    class Meta(AwardSectionForm.Meta):
        model = AwardCloseout
        exclude = AwardSectionForm.Meta.exclude + ['date_assigned', 'closeout_completion_date']


class FinalReportForm(SubsectionForm):
    """The form for creating/editing FinalReport"""

    parent_edit_url = 'edit_award_closeout'

    class Meta:
        model = FinalReport
        exclude = ['award']


class SubawardForm(AutoFormMixin, forms.ModelForm):
    """The form for creating/editing Subaward"""

    class Meta:
        model = Subaward
        exclude = ['award', 'creation_date', 'subaward_completion_date']

        widgets = {
            'is_edited': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(SubawardForm, self).__init__(*args, **kwargs)
        self.helper.layout.extend([
            HTML("<div class='pull-right'>"),
            FormActions(
                HTML('<a href="{% url \'edit_subawards\' award_pk=award.id %}" class="btn">Cancel</a>'),
                Submit('save', 'Save changes'),
            ),
            HTML("</div>"),
        ])

    def clean(self):
        """Overrides the base clean method to also add a value indicating the Subaward has been edited"""

        cleaned_data = super(SubawardForm, self).clean()
        cleaned_data['is_edited'] = True

        return cleaned_data


class ProposalStatisticsReportForm(forms.Form):
    """Simple form for the Proposal Statistics report"""

    from_date = forms.DateField()
    to_date = forms.DateField()
    show_all_fields = forms.TypedChoiceField(choices=((False, 'No'), (True, 'Yes')), coerce=lambda x: x == 'True',
                                             empty_value=False)

    def __init__(self, *args, **kwargs):
        super(ProposalStatisticsReportForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3'
        self.helper.field_class = 'col-md-3'
        self.helper.layout = Layout(
            Field('from_date', css_class='datePicker'),
            Field('to_date', css_class='datePicker'),
            Field('show_all_fields'),
            HTML("<div class='pull-right'>"),
            FormActions(
                Submit('run', 'Run report'),
            ),
            HTML("</div>"),
        )


class AwardREAssaignementForm(forms.Form):
    """
    This form is for re-assigning the work to active user
    """
    atp_users_choices = [(u'', u'---------')]
    assignment_users_choices = [(u'', u'---------')]
    for atp_user in User.objects.all().order_by('first_name'):
        assigns = Award.objects.filter(Q(Q(award_acceptance_user_id=atp_user.id) | Q(award_closeout_user_id=atp_user) |
                                         Q(award_management_user_id=atp_user.id) |
                                         Q(award_modification_user_id=atp_user.id) | Q(subaward_user_id=atp_user.id) |
                                         Q(award_negotiation_user_id=atp_user.id) | Q(award_setup_user_id=atp_user.id))
                                       & Q(status__lt=6))
        if len(assigns) > 0:
            atp_users_choices.append((atp_user.id, atp_user.first_name + ' ' + atp_user.last_name))
    assignment_users_list = [(user.id, user.first_name + ' ' + user.last_name) for user
                             in User.objects.filter(is_active=True, groups__name__in=['Administrative',
                                                                                      'Award Acceptance',
                                                                                      'Award Closeout',
                                                                                      'Award Management',
                                                                                      'Award Modification',
                                                                                      'Award Negotiation',
                                                                                      'Award Setup',
                                                                                      'Proposal Intake',
                                                                                      'Subaward Management'
                                                                                      ]).order_by(
            'first_name').distinct()]
    assignment_users_choices.extend(assignment_users_list)
    atp_user = forms.ChoiceField(choices=atp_users_choices, label='ATP User')
    user_department = forms.ChoiceField(label='Department', required=False)
    assignment_user = forms.ChoiceField(choices=assignment_users_choices, label='Re-assignment User')

    def __init__(self, *args, **kwargs):
        super(AwardREAssaignementForm, self).__init__(*args, **kwargs)
        assignment_users_choices = [(u'', u'---------')]

        assignment_users_list = [(user.id, user.first_name + ' ' + user.last_name) for user
                                 in User.objects.filter(is_active=True, groups__name__in=['Administrative',
                                                                                          'Award Acceptance',
                                                                                          'Award Closeout',
                                                                                          'Award Management',
                                                                                          'Award Modification',
                                                                                          'Award Negotiation',
                                                                                          'Award Setup',
                                                                                          'Proposal Intake',
                                                                                          'Subaward Management'
                                                                                          ]).order_by(
                'first_name').distinct()]
        assignment_users_choices.extend(assignment_users_list)
        self.fields['assignment_user'].choices = assignment_users_choices
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-4'
        self.helper.field_class = 'col-md-6'
        self.helper.layout = Layout(
            HTML('<div class="col-md-6">'),
            Field('atp_user'),
            Field('user_department'),
            Field('assignment_user'),
            HTML("<div class='col-md-8 pull-right'>"),
            FormActions(
                Submit('run', 'Re-assign User'),
            ),
            HTML("</div>"),
            HTML("</div>"),
        )

        self.helper.layout.extend([
            HTML('<div id="re_assign_awards_div" class="col-md-4 pull-right">'),
            HTML('</div>'),
            HTML('<div id="re_assign_no_data_div" class="col-md-4 pull-right">'),
            HTML('</div>'), ]
        )

    def clean(self):
        super(AwardREAssaignementForm, self).clean()
        if 'user_department' in self._errors:
            del self._errors['user_department']
            self.cleaned_data['user_department'] = self.data.get('user_department')
        return self.cleaned_data