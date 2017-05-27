from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Choice, Question,Feedback,Sop
from django.views import generic
from django.utils import timezone

import time

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list = Question.objects.filter(is_active = True).order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def sop(request):
    item_list = Sop.objects.filter(is_active = True).order_by('code')[:500]
    context = {'item_list': item_list}
    return render(request, 'polls/sop_list.html', context)

def sop_detail(request, sop_id):
    sop = get_object_or_404(Sop, pk=sop_id)
    return render(request, 'polls/sop_detail.html', {'sop': sop})


def feedback(request):
    item_list = Feedback.objects.order_by('question','username',)[:500]
    context = {'item_list': item_list}
    return render(request, 'polls/feedback.html', context)



# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        user_info="【未登入】"
        if not request.user.is_authenticated:
            selected_choice.remark +="【未登入】"+" "+time.strftime("%Y-%m-%d %H:%M:%S")+" | "
            selected_choice.votes += 1


        else:
            user_info=request.user.last_name
            selected_choice.remark +=request.user.last_name+" "+time.strftime("%Y-%m-%d %H:%M:%S")+" | "
            selected_choice.votes += 1
    #     question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # username = models.CharField(max_length=200)
    # choice_text = models.IntegerField(default=0)
    # debug
                                  # feeback_textfeeback_text
        # f=Feedback(question="XXX",feedback="YYY",username="ZZZ")
        f=Feedback(question=question,feedback=selected_choice,username=user_info)

        f.save()
        # choice2.save()
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'

# #     def get_queryset(self):
# #         """Return the last five published questions."""
# #         return Question.objects.order_by('-pub_date')[:5]

#     def get_queryset(self):
#         """
#         Return the last five published questions (not including those set to be
#         published in the future).
#         """
#         return Question.objects.filter(
#             pub_date__lte=timezone.now()
#         ).order_by('-pub_date')[:5]


# class DetailView(generic.DetailView):
#     model = Question

    # template_name = 'polls/detail.html'
	# https://docs.djangoproject.com/en/1.10/intro/tutorial04/
	# default one is no need to state, it's working!
    # template_name = 'polls/question_detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
