from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basic_vote.models import CustomUser, School
from .forms import VoteForm
from django.shortcuts import redirect


@login_required
def vote_submit_view(request):
    schools = School.objects.all()
    user = CustomUser.objects.get(username=request.user.username)
    form = VoteForm(request.POST or None)
    if not user.has_answered:
        if form.is_valid():
            form.save()
            user.has_answered = True
            user.save()
            form = VoteForm()
        context = {
            'form': form,
            'schools': schools,
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
    return redirect('/vote')
