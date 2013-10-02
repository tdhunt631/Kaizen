from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import ModelForm
from suggestionbox.models import Suggestion, SuggestionForm, Comment, CommentForm, Status, StatusForm, Category

def index(request):
	suggestions = Suggestion.objects.all().order_by('-pub_date')
	context = {
			'suggestions': suggestions,
	}
	return render(request, 'suggestionbox/index.html', context)

@login_required
def detail(request, suggestion_id):
	suggestion = get_object_or_404(Suggestion, pk=suggestion_id)
	comments = Comment.objects.all().filter(sid=suggestion_id).order_by('-pub_date')
	currentStatus = get_object_or_404(Status, title=suggestion.status)
	statusForm = StatusForm(initial = {'status': currentStatus.pk })	
	commentForm = CommentForm()
	context = {
			'suggestion': suggestion,
			'commentForm': commentForm,
			'statusForm': statusForm,
			'comments': comments,
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

@login_required
def addComment(request, suggestion_id):
	if request.method == 'POST':
		data = CommentForm(request.POST)
		form = data.save(commit=False)
		form.user = request.user
		form.sid = get_object_or_404(Suggestion, id=suggestion_id) 
		form.save()
	return HttpResponseRedirect(reverse('suggestionbox:detail', args=(suggestion_id,)))

@login_required
def updateStatus(request, suggestion_id):
	if request.method == 'POST':
		instance = get_object_or_404(Suggestion, id=suggestion_id)
		form = StatusForm(request.POST or None, instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		return HttpResponseRedirect('/')
