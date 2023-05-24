from django.urls import path
from .views import SummaryTextView

urlpatterns = [
    path('summarize/', SummaryTextView.as_view(), name='summarize-text'),
]
