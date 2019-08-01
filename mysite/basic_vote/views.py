from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'vote_not_logged.html')


def home(request):
    return render(request, 'home.html')


@login_required
def logged(request):
    return render(request, 'vote_logged.html')
