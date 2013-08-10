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


#from ps_editor.models import Pitchspot

#from logic import edit_pitchspot ## LOL
import logic

def frontpageview(request):
    output = "'ello world.."
    return HttpResponse(output)

@login_required    
def create_pitchspot_view(request):
    title = str(request.POST['title'])
    is_published = request.POST['is_published']
    owner = request.user
    logic.create_pitchspot(title=title, owner=owner, is_published=is_published)
    output = "Create pitchspot works.."
    return HttpResponse(output)

def get_pitchspot_view(request, pitchspot_id):
    Pitchspot = Pitchspot.objects.get(id=pitchspot_id)
    pitchspot_dict = {'title': Pitchspot.title, 'owner': Pitchspot.owner, 'admin': 'Not implemented', 'is_published': Pitchspot.is_published, 'date_created': Pitchspot.date_created}
    output = pitchspot_dict
    return HttpResponse(output)  

