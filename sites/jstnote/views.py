# -*- coding: UTF-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

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
            #messages.info(request, u'创建成功')
            return HttpResponseRedirect(reverse("note_detail", args=[paster.pk]))
    ctx['form'] = form
    ctx['preview'] = preview
    return render(request, template_name, ctx)

def detail(request, pk):
    template_name = 'jstnote/detail.html'
    paster = get_object_or_404(Paster, pk=pk)
    ctx = {}
    ctx['paster'] = paster
    return render(request, template_name, ctx)

def edit(request, pk):
    pass
