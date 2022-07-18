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

def setcommand(request, id, cmd):
    print(request)
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
    print("IP: ", get_client_ip(request))
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
    c = cmd_string()
    return render(request, 'tds/table.html', {'dogovors': dogovors,
                                              'request': request,
                                              'RGET':request.GET,
                                              'cmd_string':c,
                                              })

def logout_view(request):
    logout(request)
    return redirect("/")

def delete_docs(request):
    if not request.user.is_authenticated:
        return redirect("/admin/login/?next=/delete_docs/")

    #models.Dogovor.objects.all().delete()
    return redirect("/")

def one(request):
    if not request.user.is_authenticated:
        return redirect("/admin/login/?next=/one/")
    response = "one"
    return HttpResponse(response)

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
