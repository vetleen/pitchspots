#from datetime import datetime  
#from django.utils.timezone import utc
from django.http import HttpResponse
#from django.template.loader import get_template
#from django.shortcuts import render_to_response, redirect
#from django.template import Context, RequestContext
#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.core.context_processors import csrf
#from django.core.urlresolvers import reverse


#from todotracker.models import Todo

#from logic import edit_pitchspot ## LOL
import logic

def frontpageview(request):
    output = "'ello world.."
    return HttpResponse(output)

@login_required    
def create_pitchspot_view(request):
    title = "Test"#str(request.POST['title'])
    is_published = bool(request.POST['is_published'])
    owner = request.user
    logic.create_pitchspot(title=title, owner=owner, is_published=is_published)
    output = "It works.."
    return HttpResponse(output)
