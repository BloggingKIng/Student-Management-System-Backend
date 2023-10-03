from rest_framework import serializers
from rest_framework.fields import empty
from .models import CustomUser

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserSerializers, self).__init__(*args, **kwargs)
        self.fields.pop('password')
        self.fields.pop('user_permissions')
        self.fields.pop('groups')