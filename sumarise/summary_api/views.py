from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .processing.summarize_text import summarize_text
from .serializers import SummaryTextSerializer

class SummaryTextView(APIView):
    """
    API endpoint that summarizes input text.
    """
    serializer_class = SummaryTextSerializer
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            percentage = serializer.validated_data['percentage']
            summary = summarize_text(text, percentage)
            return Response({'summary': summary})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
