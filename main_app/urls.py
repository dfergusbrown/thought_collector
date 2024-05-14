from django.urls import path
from .views import Home, ThoughtList, ThoughtDetail, RecurrenceList, RecurrenceDetail, AddTagToThought, TagList, TagDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('thoughts/', ThoughtList.as_view(), name="thought-list"),
    path('thoughts/<int:id>/', ThoughtDetail.as_view()),
    path('thoughts/<int:thought_id>/recurrences/', RecurrenceList.as_view()),
    path('thoughts/<int:thought_id>/recurrences/<int:id>', RecurrenceDetail.as_view()),
    path('tags/', TagList.as_view(), name='tag-list'),
    path('tags/<int:id>/', TagDetail.as_view(), name='tag-detail'),
    path('thoughts/<int:thought_id>/add_tag/<int:tag_id>/', AddTagToThought.as_view(), name='add-tag-to-cat'),
]