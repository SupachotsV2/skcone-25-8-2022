from rest_framework import serializers
from .models import testRequest

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = testRequest
        fields = ('id', 'detailUrl', 'docNumber','title','department','requester','requestDate','lastUpdate','system','docStatus','attachment','approver')