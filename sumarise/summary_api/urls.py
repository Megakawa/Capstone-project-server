from django.urls import path
from .views import SummaryTextView, SummaryLinkView

urlpatterns = [
    path('text/', SummaryTextView.as_view(), name='summarize-text'),
    path('link/', SummaryLinkView.as_view(), name='summarize-link'),
]
