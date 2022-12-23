from django.urls import path
from .views import OptionDlete, poll_list, PollList, PollView,PollVote,PollCreate,PollEdit,PollDelete,OptionCreate,OptionEdit,OptionDlete

urlpatterns = [
    path('list/',poll_list),
    path('' , PollList.as_view()),
    path('<int:pk>/',PollView.as_view()),
    path('option/<int:oid>/', PollVote.as_view()),
    path('create/',PollCreate.as_view()),
    path('<int:pk>/edit/',PollEdit.as_view()),
    path('<int:pk>/delete/',PollDelete.as_view()),
    path('<int:pk>/add/',OptionCreate.as_view()),
    path('option/<int:oid>/edit/',OptionEdit.as_view()),
    path('option/<int:oid>/delete/',OptionDlete.as_view()),
]
