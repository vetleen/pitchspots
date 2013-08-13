from datetime import datetime  
from django.utils.timezone import utc
from django.db import models
from django.contrib.auth.models import User

class Pitchspot(models.Model):
    #Automatic fields (Non-optional)
    owner = models.ForeignKey(User, related_name="pitchspots_owned_set")    
    date_created = models.DateTimeField() 
    date_last_changed = models.DateTimeField()
    admin = models.ManyToManyField(User, blank=True, null=True, related_name="pitchspots_administered_set")    

    #Required fields:
    title = models.CharField(max_length=75)
    campaign_manager_firstname = models.CharField(max_length=50)
    campaign_manager_lastname = models.CharField(max_length=50)
        
    #Optional fields
    is_published = models.BooleanField(default=False)
    campaign_manager_title = models.CharField(max_length=50, blank=True)        
    campaign_manager_organization = models.CharField(max_length=50, blank=True)
    call_to_action_text = models.CharField(max_length=20, default="I'm interested!")

    def __unicode__(self):
        return self.title	
          
class IntroModule(models.Model):
    pitchspot = models.ForeignKey(Pitchspot, related_name="intromodule_set")
    title = models.CharField(max_length=75)
    bodytext = models.TextField()
