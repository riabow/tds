import os

from django.http import HttpResponse
from django.shortcuts import render
from HelloDjango.settings import SETTINGS_PATH, TEMPLATE_DIRS
from . import models
# Create your views here.


def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default


def index(request):
    dogovors = models.Dogovor.objects.all()
    return render(request, 'tds/index.html', {'dogovors':dogovors})
    # return HttpResponse("index")

def one(request):
    response = "one"
    return HttpResponse(response)

def two(request):
    # Using readline()
    file1 = open(os.path.dirname(__file__) + '/../dogovor.csv', 'r', encoding='utf-16')
    count = 0
    while True:
        count += 1
        line = file1.readline()
        if not line:
            break
        if count > 5000000:
            break
        l = line.split(";")
        # print("Line{}: {}".format(len(l), l))
        d = models.Dogovor()
        n = -2
        for f in models.Dogovor()._meta.get_fields():
            n += 1
            if f.name == 'id':
                continue
            curVal = safe_list_get(l, n, "")
            if curVal == 'NULL':
                curVal = ''
            setattr(d, f.name, curVal)
        d.save()

    file1.close()

    return HttpResponse("two")
