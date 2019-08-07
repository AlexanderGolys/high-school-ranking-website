from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basic_vote.models import CustomUser

from .forms import VoteForm


@login_required
def vote_submit_view(request):
    form = VoteForm(request.POST or None)
    if not request.user.has_answered:
        if form.is_valid():
            form.save()
            user = CustomUser.objects.get(username=request.user.username)
            user.has_answered = True
            user.save()
            form = VoteForm()
        context = {
            'form': form
        }
        return render(request, 'vote.html', context)
    else:
        return render(request, 'vote_done.html', {})


def login(request):
    return render(request, 'vote_not_logged.html')


def home(request):
    return render(request, 'home.html')


@login_required
def logged(request):
    return render(request, 'vote_logged.html')
