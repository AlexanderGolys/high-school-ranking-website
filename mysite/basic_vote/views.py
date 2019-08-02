from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import VoteForm


@login_required
def vote_submit_view(request):
    form = VoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = VoteForm()
    context = {
        'form': form
    }
    return render(request, 'vote.html', context)


def login(request):
    return render(request, 'vote_not_logged.html')


def home(request):
    return render(request, 'home.html')


@login_required
def logged(request):
    return render(request, 'vote_logged.html')
