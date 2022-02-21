from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Question

# Create your views here.

#def index(request):
	#latest_question_list = Question.objects.order_by('-pub_date')[:5]
	#output = ', '.join([q.question_text for q in latest_question_list])
	#template=loader.get_template('polls/index.html')
	#context={
	#	'latest_question_list': latest_question_list,
	#}
	#return HttpResponse("Hola Mundo")
	#return HttpResponse(template.render(context, request))

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context={'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

#def detail(request, question_id):
	#try:
	#	question=Question.objects.get(pk=question_id)
	#except Question.DoesNotExist:
	#	raise Http404("Question does not exists.")
	#return render(request, 'polls/details.html', {'question': question_id})

def detail(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html', {'question': question})



def results(request, question_id):
	response = "You're looking at the results of question %s "
	return render(request, 'polls/results.html', {'response':response})

def vote(request, question_id):
	response = "You're looking at the results of question %s " % question_id
	return render(request, 'polls/vote.html', {'response':response})