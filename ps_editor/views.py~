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

    ## Gather the data required ## may ADD validation here, to ensure that all required values have been filled in... 
    #required fields
    title = request.POST['title']
    campaign_manager_firstname = request.POST['campaign_manager_firstname']
    campaign_manager_lastname = request.POST['campaign_manager_lastname']
    #optional fields
    campaign_manager_title = request.POST['campaign_manager_title']
    campaign_manager_organization = request.POST['campaign_manager_organization']
    call_to_action_text = request.POST['call_to_action_text']
    is_published = request.POST['is_published']
    
    ##Create the pitchspot
    ps_editor_logic.create_pitchspot(   #required fields
                                        title=title, 
                                        campaign_manager_firstname=campaign_manager_firstname,
                                        campaign_manager_lastname=campaign_manager_lastname,
                                        #automatic fields
                                        owner=request.user,
                                        #optional fields
                                        campaign_manager_title=campaign_manager_title,
                                        campaign_manager_organization=campaign_manager_organization,
                                        call_to_action_text=call_to_action_text,
                                        is_published = is_published
                                        )
    output = "Create pitchspot view.."
    return HttpResponse(output)

def retrieve_pitchspot_as_JSON_view(request, pitchspot_id):
    PitchspotToRetrieve = Pitchspot.objects.get(id=pitchspot_id)
    pitchspot_dict = PitchspotToRetrieve.get_dict()
    Pitchspot_JSON = ps_editor_logic.make_JSON_from_dict(pitchspot_dict)
    output = Pitchspot_JSON
    return HttpResponse(output)  

