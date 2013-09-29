from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm
from suggestionbox.models import Suggestion, SuggestionForm, Comment, Status, Category

def index(request):
	suggestions = Suggestion.objects.all().order_by('-pub_date')
	context = {
			'suggestions': suggestions,
	}
	return render(request, 'suggestionbox/index.html', context)

@login_required
def detail(request, suggestion_id):
	suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
	context = {
			'suggestion': suggestion,
	}
	return render(request, 'suggestionbox/detail.html', context)

@login_required
def addSuggestion(request):
	if request.method == 'POST':
		data = SuggestionForm(request.POST)
		form  = data.save(commit=False)
		form.user = request.user	
		form.status = get_object_or_404(Status, title="Pending")
		form.save()
		return HttpResponseRedirect('/')
	else:
		suggestionForm = SuggestionForm()
		context = {
			'suggestionForm': suggestionForm,
		}
	return render(request, 'suggestionbox/suggestionForm.html', context)
