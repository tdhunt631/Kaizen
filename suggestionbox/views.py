# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from suggestionbox.models import Suggestion, Comment, Status, Category

# view for our index
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
