# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

markup_choices = (
        ('txt', _(u'Text')),
        ('textile', _(u'Textile')),
        ('html', _(u'Html')),
        ('md', _(u'Markdown')),
        ('rst', _(u'reStructuredText')),
        )

class Paster(models.Model):
    markup = models.CharField(u"格式", max_length=10, default='txt', choices=markup_choices)
    body = models.TextField(u'内容')
    num_views = models.IntegerField(u'浏览次数', default=0, blank=True)
    num_replies = models.PositiveSmallIntegerField(u'回复数', default=0)#posts...

    title = models.CharField(u'标题', max_length=30, blank=True)
    username = models.CharField(u'用户名/E-Mail', max_length=30, blank=True)
    admin_pwd = models.CharField(u'密码', max_length=30, help_text=u'日后编辑该文件时，所需使用的密码')

    created_by = models.ForeignKey(User, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(blank = True, null = True)
    
    def __unicode__(self):
        return self.title
