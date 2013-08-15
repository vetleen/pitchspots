from datetime import datetime  
from django.utils.timezone import utc
from django.db import models
from django.contrib.auth.models import User

class UserProfile(User):
    class Meta:
        proxy = True
        
    def get_dict(self):
        return {'username': self.username,
                'first_name': self.first_name,
                'last_name': self.last_name
                }

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
    
    def get_admins_dict(self):
        admindict = {}
        for n, admin in enumerate(self.admin.all()):
            admindict.update({n+1: UserProfile.objects.get(id=admin.id).get_dict()})
        return admindict
        
    def get_dict(self):
        return {'owner': UserProfile.objects.get(id=self.id).get_dict(),
                'date_created': 
                    {
                    'year': self.date_created.year,
                    'month': self.date_created.month,
                    'day': self.date_created.day,
                    'hour': self.date_created.hour,
                    'minute': self.date_created.minute,
                    'second': self.date_created.second,
                    },    
                'date_last_changed': 
                    {
                    'year': self.date_last_changed.year,
                    'month': self.date_last_changed.month,
                    'day': self.date_last_changed.day,
                    'hour': self.date_last_changed.hour,
                    'minute': self.date_last_changed.minute,
                    'second': self.date_last_changed.second,
                    },                
                'admins': self.get_admins_dict(),
                
                'title': self.title,
                'campaign_manager_firstname': self.campaign_manager_firstname,
                'campaign_manager_lastname': self.campaign_manager_lastname,

                'is_published': self.is_published,
                'campaign_manager_title': self.campaign_manager_title,
                'campaign_manager_organization': self.campaign_manager_organization,
                'call_to_action_text': self.call_to_action_text,
                }
                          
class IntroModule(models.Model):
    pitchspot = models.ForeignKey(Pitchspot, related_name="intromodule_set")
    title = models.CharField(max_length=75)
    bodytext = models.TextField()
    
    def get_dict(self):
        return {'title': self.title,
                'bodytext': self.bodytext
                }
    






