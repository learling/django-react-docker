from rest_framework.views import APIView
from django.http import JsonResponse  

class SampleView(APIView):

  def get(self, request, format=None):
    return JsonResponse({"message": 'HELLO WORLD FROM DJANGO AND DOCKER'})