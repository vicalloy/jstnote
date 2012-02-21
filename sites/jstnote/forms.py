from django.contrib.auth.forms import PasswordChangeForm
from django import forms

from bootstrap.forms import BootstrapModelForm

from jstnote.models import Paster

class PasterForm(BootstrapModelForm):

    class Meta:
        model = Paster
        exclude = ['created_by', 'updated_on', 'num_views', 'num_replies']
        widgets = {
            'admin_pwd': forms.PasswordInput(),
        }

    def save(self, force_insert=False, force_update=False, commit=True):
        paster = super(PasterForm, self).save(commit=commit)
        #TODO update update_time
        return paster
