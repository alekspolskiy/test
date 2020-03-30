from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SomeObject, SomeObjectType
from .serializers import ObjectSerializer, ObjectTypeSerializer


def home(request):

	list_objects = SomeObject.objects.all()
	list_object_types = SomeObjectType.objects.all()

	context = {
		'list_objects': list_objects,
		'list_object_types': list_object_types
	}

	template = 'index.html'

	return render(request, template, context)


class ObjectView(ModelViewSet):
	queryset = SomeObject.objects.all()
	serializer_class = ObjectSerializer

class ObjectTypeView(ModelViewSet):
	queryset = SomeObjectType.objects.all()
	serializer_class = ObjectTypeSerializer