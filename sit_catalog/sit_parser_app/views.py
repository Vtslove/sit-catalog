from django.shortcuts import render
from .models import SITdb


def index(request):
    database = SITdb.objects.all()
    return render(request, 'sit_parser_app/index.html', {'database': database})

