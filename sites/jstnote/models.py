# -*- coding: UTF-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

markup_choices = (
        ('txt', _(u'Text')),
        ('html', _(u'Html')),
        ('md', _(u'Markdown')),
        ('textile', _(u'Textile')),
        ('rst', _(u'reStructuredText')),
        )

class Paster(models.Model):
    markup = models.CharField(u"格式", max_length=10, default='txt', choices=markup_choices)
    body = models.TextField(u'内容')
    tags = TaggableManager()

    title = models.CharField(u'标题', max_length=30, blank=True)
    username = models.CharField(u'用户名/E-Mail', max_length=30, blank=True, help_text=u'文本显示的作者名称，无需要注册')
    admin_pwd = models.CharField(u'密码', max_length=30, help_text=u'日后编辑该文件所需使用的密码。该密码为认领文本的唯一凭证')

    num_views = models.IntegerField(u'浏览次数', default=0, blank=True)
    num_replies = models.PositiveSmallIntegerField(u'回复数', default=0)#posts...

    created_by = models.ForeignKey(User, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(blank = True, null = True)
    
    def __unicode__(self):
        return self.title

    def get_created_by(self):
        if self.username:
            return self.username
        return u'匿名'
