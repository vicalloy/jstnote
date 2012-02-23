# -*- coding: UTF-8 -*-
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

from bootstrap.forms import BootstrapModelForm

from jstnote.models import Paster

class PasterForm(BootstrapModelForm):

    def clean_admin_pwd(self):
        admin_pwd = self.cleaned_data['admin_pwd']
        if self.instance.pk and instance.admin_pwd != admin_pwd:#edit
            raise forms.ValidationError(u"您输入的编辑密码不正确")
        return admin_pwd

    def save(self, force_insert=False, force_update=False, commit=True):
        paster = super(PasterForm, self).save(commit=commit)
        #TODO update update_time
        return paster

    class Meta:
        model = Paster
        exclude = ['title', 'created_by', 'updated_on', 'num_views', 'num_replies']
        widgets = {
            'admin_pwd': forms.PasswordInput(),
        }
