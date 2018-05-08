from django.shortcuts import render
from rest_framework import serializers, viewsets, mixins, views, status
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Image

# Serializers define the API representation.
class ImageSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="api:image-detail")
    class Meta:
        model = Image
        fields = ('url', 'name', 'image', 'id')

# ViewSets define the view behavior.
class ImageViewSet( mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.RetrieveModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,
        viewsets.GenericViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# @csrf_exempt
# def photo(request): 
#   if(request.method == 'POST'):
#     photo = request.FILES['photo']
#     newPhoto = Image(image= photo)
#     newPhoto.save()
#     return HttpResponse('true')
#   else: 
#     data = serializers.serialize("json", Image.objects.all())
#     print(data)
#     return JsonResponse(data, safe=False)