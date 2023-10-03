from rest_framework import serializers
from .models import SchoolInformation
import json

class SchoolInformationSerializer(serializers.ModelSerializer):
   
    props = serializers.SerializerMethodField()
    class Meta:
        model = SchoolInformation
        fields = ['name','description','address','email','phone','props']
    def get_props(self, obj):
        return json.loads(obj.props)
