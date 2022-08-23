import datetime
import json
import os
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib.auth import login
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from HelloDjango.settings import SETTINGS_PATH, TEMPLATE_DIRS
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from . import models
from django.views.decorators.csrf import csrf_exempt

POSTED_RESPONSES = []

LAST_REQUESTS = {}

def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default

decorators = [ login_required]


def index(request):
    if not request.user.is_authenticated:
        return redirect("/admin/login/?next=/show_table/")
    return render(request, 'tds/index.html')
    # return HttpResponse("index")


@csrf_exempt
def post_resp(request):
    """ test function """
    print("reuest:", request.POST)
    if len(request.POST) > 0 :
        POSTED_RESPONSES.insert(0, {'id': len(POSTED_RESPONSES),
                                    'you_posted': request.POST})
    return JsonResponse({'POSTED_RESPONSES': POSTED_RESPONSES})

def cmd_string():
    q = models.Dogovor.objects.all()
    q = q.filter(~Q(command=''))
    ret = ''
    for d in q:
        ret += f' {d.command}{d.kod_open_close}'
    return ret

def cmdstrind(request):
    ret = cmd_string()
    return HttpResponse(ret)


@csrf_exempt
def post_get_status(request):
    """this ask every 10 sec from frontend """
    js = json.loads(request.body)
    docs = models.Dogovor.objects.filter(pk__in=js['list_id'])
    ret = {}
    for i in docs:
        mt = LAST_REQUESTS.get(i.pk, datetime.datetime(2000, 1, 1, 0, 0))
        t2 = datetime.datetime.now() - datetime.datetime(mt.year, mt.month, mt.day, mt.hour, mt.minute, mt.second)
        #t = datetime.datetime.now() - datetime.datetime(i.last_change.year, i.last_change.month, i.last_change.day, i.last_change.hour, i.last_change.minute, i.last_change.second)
        ret[i.pk] = {'r':i.result, 'c': i.command, 't': round(t2.total_seconds())}
    return JsonResponse({'ret': ret})

def ispolnenie(request, kod, sost):
    """ path('ispolnenie/<str:kod>/<str:sost>/', views.ispolnenie)
    this runs when command is done, and we want to know results
    """
    global LAST_REQUESTS
    dogs = models.Dogovor.objects.filter(kod_open_close=kod)
    if len(dogs) >= 1:
        changed = False
        if dogs[0].result != sost:
            dogs[0].result = sost
            changed = True
        if dogs[0].command != '':
            dogs[0].command = ''
            changed = True

        # dogs[0].last_change = datetime.datetime.now()
        if changed:
            dogs[0].save()
        LAST_REQUESTS[dogs[0].pk] = datetime.datetime.now()
        if len(dogs) == 1:
            return JsonResponse({'resp': f"OK {kod} / {sost} "})
        else:
            return JsonResponse({'resp': f"to many  FOUND {kod} I got first"})

    if len(dogs) == 0:
        return JsonResponse({'resp': f"NOT FOUND {kod} / {sost} "})


def setcommand(request, id, cmd):
    if not request.user.is_authenticated:
        return JsonResponse({'resp': f"No login"})
    d = models.Dogovor.objects.get(pk=id)
    if d:
        if cmd == '-':
            cmd = ''
        d.command = cmd
        d.save()
        return JsonResponse({'resp': f"OK {id} / {cmd} "})
    else:
        return JsonResponse({'resp': f"not found {id}  "})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def show_table(request):
    if not request.user.is_authenticated:
        return redirect("/admin/login/?next=/show_table/")
    q = models.Dogovor.objects.all()
    if 'id' in request.GET and request.GET['id'] != '':
        q = q.filter(dog_id__iexact=request.GET['id'])
    if 'CONTR_NUM' in request.GET and request.GET['CONTR_NUM'] != '':
        q = q.filter(CONTR_NUM__contains=request.GET['CONTR_NUM'])
    if 'UL' in request.GET and request.GET['UL'] != '':
        q = q.filter(UL__contains=request.GET['UL'])
    if 'DOM' in request.GET and request.GET['DOM'] != '':
        q = q.filter(DOM__startswith=request.GET['DOM'])
    if 'KORPUS' in request.GET and request.GET['KORPUS'] != '':
        q = q.filter(KORPUS__startswith=request.GET['KORPUS'])
    if 'PODEZD' in request.GET and request.GET['PODEZD'] != '':
        q = q.filter(PODEZD__startswith=request.GET['PODEZD'])
    if 'KOD_OPEN_CLOSE' in request.GET and request.GET['KOD_OPEN_CLOSE'] != '':
        q = q.filter(kod_open_close__iexact=request.GET['KOD_OPEN_CLOSE'])

    dogovors = q[:100]
    list_id = []
    list_dogs = []
    for dog in dogovors:
        list_id.append(int(dog.pk))
        list_dogs.append(dog)

    c = cmd_string()
    return render(request, 'tds/table.html', {'dogovors': list_dogs,
                                              'request': request,
                                              'RGET':request.GET,
                                              'cmd_string':c,
                                              'list_id':list_id
                                              })

def logout_view(request):
    logout(request)
    return redirect("/")

def delete_docs(request):
    if not request.user.is_authenticated:
        return redirect("/admin/login/?next=/delete_docs/")

    #models.Dogovor.objects.all().delete()
    return redirect("/")

def load_docs(request):
    if not request.user.is_authenticated:
        return redirect("/admin/login/?next=/load_docs/")

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
    return redirect("/")
