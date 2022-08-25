from django.contrib import admin
from .models import testRequest, System

class RequestAdmin(admin.ModelAdmin):
    list_display = ['docNumber','detailUrl','title','department','requester','requestDate','lastUpdate','system','docStatus','attachment','approver']
    search_fields = ['docNumber']
    list_filter = ['system']
    
    
admin.site.register(System)
admin.site.register(testRequest, RequestAdmin)
