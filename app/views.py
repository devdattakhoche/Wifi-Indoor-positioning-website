from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from . import firebase as fb


@login_required(login_url="/login/")
def dashboard(request):
    return render(request, "geo/dashboard.html")

@login_required(login_url="/login/")
def all_user_tracking(request):
    return render(request, "geo/all-user-tracking.html")
    
@login_required(login_url="/login/")
def all_user_list(request):
    params = {'patients_data' : fb.get_all_active_paitent()}
    return render(request, "geo/all-user-list.html",params)


@login_required(login_url="/login/")
def blacklist(request):
    params = {'patients_data' : fb.get_blacklist()}
    return render(request, "geo/blacklist.html",params)

@login_required(login_url="/login/")
def individual_user(request,patient_id):
    return render(request, "geo/individual-user.html")

@login_required(login_url="/login/")
def admin_profile(request):
    return render(request, "geo/profile.html")

'''
DO NOT TOUCH THESE  FUNCTIONS BELOW
'''


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
