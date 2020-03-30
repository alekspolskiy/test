from rest_framework.serializers import ModelSerializer
from .models import SomeObject, SomeObjectType

class ObjectSerializer(ModelSerializer):
	class Meta:
		model = SomeObject
		fields = ['description']

class ObjectTypeSerializer(ModelSerializer):
	class Meta:
		model = SomeObjectType
		fields = ['name']