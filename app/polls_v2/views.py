from django.http import HttpResponseRedirect  # , HttpResponse
from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
# from django.template import loader

from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls_v2/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls_v2/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls_v2/result.html"


def vote(requset, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=requset.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the voting form.
        return render(
            requset,
            "polls_v2/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice."
            },)
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse("polls_v2:result", args=(question.id,)))