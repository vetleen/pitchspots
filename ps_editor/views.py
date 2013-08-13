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
import ps_editor_logic

def frontpageview(request):
    output = "'ello world.."
    return HttpResponse(output)

@login_required    
def create_pitchspot_view(request):
    title = request.POST['title']
    campaign_manager_firstname = request.POST['campaign_manager_firstname']
    campaign_manager_lastname = request.POST['campaign_manager_lastname']
    owner = request.user
    ps_editor_logic.create_pitchspot(   title=title, 
                                        owner=owner, 
                                        campaign_manager_firstname=campaign_manager_firstname,
                                        campaign_manager_lastname=campaign_manager_lastname
                                        )
    output = "Create pitchspot view.."
    return HttpResponse(output)

def retrieve_pitchspot_view(request, pitchspot_id):
    PitchspotToRetrieve = Pitchspot.objects.get(id=pitchspot_id)
    pitchspot_JSON = ps_editor_logic.get_pitch_spot_as_JSON(PitchspotToRetrieve)    
    output = pitchspot_JSON
    return HttpResponse(output)  



