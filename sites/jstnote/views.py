# -*- coding: UTF-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from taggit.models import Tag

from jstnote.forms import PasterForm
from jstnote.models import Paster

def index(request):
    return new(request)

def new(request):
    ctx = {}
    template_name = 'jstnote/form.html'
    form = PasterForm()
    preview = request.POST.get('preview', '')
    if request.method == "POST":
        ctx['paster_body'] = request.POST.get('body', '')
        ctx['paster_markup'] = request.POST.get('markup', '')
        form = PasterForm(request.POST)
        if form.is_valid() and request.POST.get('submit', ''):
            paster = form.save()
            return HttpResponseRedirect(reverse("note_detail", args=[paster.pk]))
    ctx['form'] = form
    ctx['preview'] = preview
    return render(request, template_name, ctx)

def detail(request, pk):
    template_name = 'jstnote/detail.html'
    paster = get_object_or_404(Paster, pk=pk)
    ctx = {}
    ctx['paster'] = paster
    ctx['next'] = reverse("note_detail", args=[paster.pk])
    return render(request, template_name, ctx)

def edit(request, pk):
    ctx = {}
    template_name = 'jstnote/form.html'
    paster = get_object_or_404(Paster, pk=pk)
    ctx['paster'] = paster
    form = PasterForm(instance=paster)
    preview = request.POST.get('preview', '')
    if request.method == "POST":
        ctx['paster_body'] = request.POST.get('body', '')
        ctx['paster_markup'] = request.POST.get('markup', '')
        form = PasterForm(request.POST, instance=paster)
        if form.is_valid() and request.POST.get('submit', ''):
            form.save()
            messages.info(request, u'成功编辑')
            return HttpResponseRedirect(reverse("note_detail", args=[paster.pk]))
    ctx['form'] = form
    ctx['preview'] = preview
    return render(request, template_name, ctx)

def to_edit(request, pk):
    paster = get_object_or_404(Paster, pk=pk)
    if request.POST.get('pwd', '') == paster.admin_pwd:
        return HttpResponseRedirect(reverse("note_edit", args=[paster.pk]))
    messages.info(request, u'密码不正确，无法编辑')
    return HttpResponseRedirect(reverse("note_detail", args=[paster.pk]))

def delete(request, pk):
    paster = get_object_or_404(Paster, pk=pk)
    if request.POST.get('pwd', '') == paster.admin_pwd:
        paster.delete()
        messages.info(request, u'成功删除')
        return HttpResponseRedirect(reverse("note_idx"))
    messages.info(request, u'密码不正确，删除失败')
    return HttpResponseRedirect(reverse("note_detail", args=[paster.pk]))

def pasters(request, tag_name=''):
    template_name = 'jstnote/pasters.html'
    ctx = {}
    if tag_name:
        ctx['tag'] = get_object_or_404(Tag, name=tag_name)
        pasters = Paster.objects.filter(tags__name__in=[tag_name])
    else:
        pasters = Paster.objects.all()
    pasters = pasters.order_by('-created_on')
    ctx['pasters'] = pasters
    return render(request, template_name, ctx)

def tags(request):
    template_name = 'jstnote/tags.html'
    return render(request, template_name)
