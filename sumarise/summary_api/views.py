from django.shortcuts import render

# Create your views here.
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .processing.summarize_text import summarize_text
from .serializers import SummaryTextSerializer, SummaryLinkSerializer
from .processing.summarize_link import summarize_link

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
            n_sen = serializer.validated_data['n_sen']
            summary = summarize_text(text, n_sen)
            return Response({'summary': summary})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SummaryLinkView(APIView):
    """
    API endpoint that summarizes input link.
    """
    serializer_class = SummaryLinkSerializer
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            url = serializer.validated_data['url']
            n_sen = serializer.validated_data['n_sen']
            summary = summarize_link(url, n_sen)
            return Response({'summary': summary})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
