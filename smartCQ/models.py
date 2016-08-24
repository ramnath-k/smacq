from __future__ import unicode_literals

from django.db import models

#Create your models here.
class Entity(models.Model):
    name = models.TextField(blank=True,default="")
    def __unicode__(self):
            return self.name

class Answer(models.Model):
    intent = models.TextField(blank=True,default="")
    entity = models.ManyToManyField(Entity,blank=True,null=True)
    answer = models.TextField(blank=True,default="")
    def __unicode__(self):
            return self.answer

class Question(models.Model):
    question = models.TextField(blank=True,default="")
    answer = models.ManyToManyField(Answer,blank=True,null=True)
    def __unicode__(self):
            return self.question
