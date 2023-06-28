from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

class Index(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response(
            {
                'greeting': 'hello'
            }
        )
    
class User(viewsets.ViewSet):
    def list(self, request):
        return Response(
            {
                'goodbye': 'bye bye'
            }
        )

    def delete(self, request):
        return Response(
            {
                'goodbye': 'bye bye'
            }
        )