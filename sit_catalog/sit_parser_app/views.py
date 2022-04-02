from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'sit_parser_app/index.html')
