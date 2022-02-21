from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
#from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Choice, Question

# Create your views here.

def index(request):
	return HttpResponse("Hola Mundo")

def detail(request, question_id):
	return HttpResponse("You're  looking at question %s ", question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s "
	return HttpResponse(response % question_id)

def vote(request, question_id):HttpResponse("You're looking at the results of question %s " % question_id)
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (keyError, Choice.DoesNotExist):
		return render(request, 'polls/details.html', {
				'question':question,
				'error_message' : "You didn't select a choice"
			})
	else:
		selected_choice += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
