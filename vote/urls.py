from django.urls import path

from vote.views import ResultView, VoteView


urlpatterns = [
    path("votes/", VoteView.as_view(), name="vote"),
    path("today-result/", ResultView.as_view(), name="result")
]

app_name = "vote"
