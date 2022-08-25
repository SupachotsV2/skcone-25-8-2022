from tkinter import CASCADE
from turtle import Turtle, title
from urllib import request
from django.db import models
from django.utils.html import format_html

class System(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = 'System'

    def __str__(self):
        return self.name


class testRequest(models.Model):
    docNumber = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    requester = models.CharField(max_length=10)
    requestDate = models.DateTimeField(null=True, blank=True)
    lastUpdate = models.DateTimeField(null=True, blank=True)
    system = models.ForeignKey(System, null=True, blank=True, on_delete=models.CASCADE)
    docStatus = models.CharField(max_length=100)
    attachment = models.BooleanField(default=False)
    approver = models.CharField(max_length=10)
    detailUrl = models.URLField(null=True, blank=True)
    
    class Meta:
        ordering = ['requestDate']
        verbose_name_plural = 'testRequest'
        
    def __str__(self):
        return  f'{self.docNumber},{self.title},{self.department},{self.requester},{self.requestDate},{self.lastUpdate},{self.system},{self.docNumber},{self.attachment},{self.approver},{self.detailUrl}'
    
