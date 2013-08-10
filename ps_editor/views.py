import json
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

from ps_editor.models import Pitchspot
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

def retrieve_pitchspot_view(request, pitchspot_id):
    PitchspotToRetrieve = Pitchspot.objects.get(id=pitchspot_id)
    pitchspot_dict = {'title': PitchspotToRetrieve.title, 'owner': PitchspotToRetrieve.owner, 'admin': 'Not implemented', 'is_published': PitchspotToRetrieve.is_published, 'date_created': PitchspotToRetrieve.date_created}
    pitchspot_JSON = json.dumps(pitchspot_dict, sort_keys=True, indent=4, separators=(',', ': '))
    
    output = pitchspot_JSON
    return HttpResponse(output)  

