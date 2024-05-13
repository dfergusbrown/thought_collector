from django.urls import path
from .views import Home, ThoughtList, ThoughtDetail, RecurrenceList, RecurrenceDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('thoughts', ThoughtList.as_view(), ),#name
    path('thoughts/<int:id>/', ThoughtDetail.as_view()),
    path('thoughts/<int:thought_id>/recurrences/', RecurrenceList.as_view()),
    path('thoughts/<int:thought_id>/recurrences/<int:id>', RecurrenceDetail.as_view()),
]