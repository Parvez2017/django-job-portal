from django.shortcuts import render
import requests
from .forms import DictionaryForm, GithubJobForm

def oxford(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()
    else:
        form = DictionaryForm()
    return render(request, 'oxford.html', {'form': form, 'search_result': search_result})

def githubjobs(request):
    result = {}
    if 'description' in request.GET:
        form = GithubJobForm(request.GET)
        if form.is_valid():
            result = form.search_job()

    else:
        form = GithubJobForm()

    return render(request, 'github.html', {'form': form, 'result': result})
