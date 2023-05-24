from django.urls import path
from .views import AccountList, AccountDetail

urlpatterns = [
    path('account/', AccountList.as_view()),
    path('account/<int:pk>/', AccountDetail.as_view()),
]
