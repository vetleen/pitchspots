#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout

import json
from datetime import datetime  
from django.utils.timezone import utc
from ps_editor.models import Pitchspot, IntroModule

def set_date_now ():
    ''' Returns current date in UTC-format'''
    return datetime.utcnow().replace(tzinfo=utc)
        
def create_pitchspot(   title, 
                        owner, 
                        campaign_manager_firstname, 
                        campaign_manager_lastname,
                        call_to_action_text=None,
                        campaign_manager_organization=None, 
                        campaign_manager_title=None,
                        is_published=None,
                    ):
    '''
    Creates a pitchspot
    '''
    #Create the pitchspot with the required and automatic fields
    MyPitchspot = Pitchspot.objects.create( title=title, 
                                            owner=owner, 
                                            date_created=set_date_now(), 
                                            date_last_changed=set_date_now(),
                                            campaign_manager_firstname = campaign_manager_firstname,
                                            campaign_manager_lastname = campaign_manager_lastname,
                                          )

    MyPitchspot.admin.add(owner)

    #Save optional arguments if they are given
    if (call_to_action_text is not None and len(call_to_action_text)>=1):
        MyPitchspot.call_to_action_text = call_to_action_text
    if (campaign_manager_organization is not None and len(campaign_manager_organization)>=1):
        MyPitchspot.campaign_manager_organization = campaign_manager_organization
    if (campaign_manager_title is not None and len(campaign_manager_title)>=1):
        MyPitchspot.campaign_manager_title=campaign_manager_title
    if (is_published == "True" or is_published == "False"):
        MyPitchspot.is_published=is_published    
    MyPitchspot.save()
    
def get_pitch_spot_as_JSON(pitchspot):
    '''
    Takes a pitchspot object as an argument and reads it's data into a dict, which it returns.
    '''
    #Get dictionaries that do into the final dictionary
    
    def get_admin_dict(pitchspot):
        ''' Returns a dict with all admins for the pitchsapot, and uses numbers for keys '''
        admin_dict = {}
        for key, user in enumerate(pitchspot.admin.all()):
            admin_dict.update({key+1: user.username})
        return admin_dict
        
    #Functions to get data from each kind of module
    def get_intromodule_dict (pitchspot):
        ''' Returns a dict with all intromodules for the pitchspot '''
        intromodule_dict = {}
        for n, im in enumerate (pitchspot.intromodule_set.all()):
            t_dict = {}
            t_dict.update({'intromodule_title': im.title})
            t_dict.update({'intromodule_bodytext': im.bodytext})
            intromodule_dict.update({n+1: t_dict})
        return intromodule_dict
    
    #Get, parse and return data
    admin_dict = get_admin_dict(pitchspot)
    intromodule_dict = get_intromodule_dict(pitchspot)
    pitchspot_dict = {
                      'title': pitchspot.title, 
                      'owner': pitchspot.owner.username, 
                      'admin': admin_dict, #this is already a dictionary type
                      'is_published': pitchspot.is_published,
                      'campaign_manager_firstname': pitchspot.campaign_manager_firstname,
                      'campaign_manager_lastname': pitchspot.campaign_manager_lastname,
                      'campaign_manager_organization': pitchspot.campaign_manager_organization,
                      'campaign_manager_title': pitchspot.campaign_manager_title,
                      'call_to_action_text': pitchspot.call_to_action_text,
                      'date_created': 
                          {
                          'year': pitchspot.date_created.year,
                          'month': pitchspot.date_created.month,
                          'day': pitchspot.date_created.day,
                          'hour': pitchspot.date_created.hour,
                          'minute': pitchspot.date_created.minute,
                          'second': pitchspot.date_created.second,
                          },
                      'intromodules': intromodule_dict,
                      } 
                      
    pitchspot_JSON = json.dumps(pitchspot_dict, sort_keys=True, indent=4, separators=(',', ': '))
    return pitchspot_JSON

def create_intro_module(pitchspot, title, bodytext):
    ''' creates an intro_module that will be attached to a pitchspot '''
    #Update information about when the Pitchspot was last changed
    pitchspot.date_last_changed=set_date_now()
    pitchspot.save()
    ingress = None
    #Create the intro-module
    im = IntroModule.objects.create(pitchspot=pitchspot, title=title, bodytext=bodytext)
    if ingress is not None:
        im.ingress = ingress
    im.save()














































