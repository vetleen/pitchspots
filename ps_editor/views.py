#from datetime import datetime  
#from django.utils.timezone import utc
from django.http import HttpResponse
#from django.template.loader import get_template
#from django.shortcuts import render_to_response, redirect
#from django.template import Context, RequestContext
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
#from django.core.context_processors import csrf
#from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import login_required

#from todotracker.models import Todo

#from logic import edit_pitchspot ## LOL

def frontpageview(request):
    output = "'ello world.."
    return HttpResponse(output)