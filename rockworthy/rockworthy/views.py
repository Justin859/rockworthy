from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


def index(request):

    return render(request, 'index.html')