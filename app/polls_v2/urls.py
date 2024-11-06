from django.urls import path

from . import views

app_name = "polls_v2"
urlpatterns = [
    # /polls
    path("", views.IndexView.as_view(), name="index"),
    # /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # /polls/5/results/
    path("<int:pk>/result/", views.ResultsView.as_view(), name="result"),
    # /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote")
    ]
