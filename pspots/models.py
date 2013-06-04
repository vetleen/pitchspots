from datetime import datetime  
from django.utils.timezone import utc
from django.db import models
from django.contrib.auth.models import User

## Basic information and content for pitchspites
class Pitchspot(models.Model):
    ## The folowing is the meta information about the pitchspot
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, related_name="pitchspots_owned_set")
    keywords = models.CharField(max_length=500)
    administrators = models.ManyToManyField(User, related_name="pitchspots_administered_set")
    is_published = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.utcnow().replace(tzinfo=utc))
    cta_button_text = models.CharField(max_length=30, default="I'm interested!")
    
    ## The following part is for the information displayed at the pitchspot
    agent_first_name = models.CharField(max_length=100, default=owner.first_name)
    agent_last_name = models.CharField(max_length=100, default=owner.last_name)
    agent_organization = models.CharField(max_length=100, default='', blank=True)
    ## picture field??
    
    def __init__ (self):
        self.date_created = datetime.utcnow().replace(tzinfo=utc)
    
    def __unicode__(self):
        return self.title

class KeywordForPitchspot(models.Model):
    keyword = models.CharField(max_length=100)
    belongs_to = models.ManyToManyField(Pitchspot, related_name="keyword_set")
    
    def __unicode__(self):
        return self.keyword
        
class UpdateForPitchspot(models.Model):
    pitchspot = models.ForeignKey(Pitchspot, related_name="update_set")
    date = models.DateTimeField(default=datetime.utcnow().replace(tzinfo=utc))
    updater = models.ForeignKey(User, related_name="update_set")
    def __unicode__(self):
        return "%s was updated at: %s, by the user %s" % (self.pitchspot.title, self.date, self.updater.username)  
    
## Main content of pitchsites
class IntroductionMainPart(models.Model):
    ## This is the introduction of the pitchsite - it is mandatory, and there can be only one of these
    pitchspot = models.OneToOneField (Pitchspot, related_name="introduction_main_part_set")
    headline = models.CharField(max_length=100)
    body = models.CharField (max_length=500)
    call_to_action = models.BooleanField(default=True)
    priority = models.IntegerField(default=1)
    def __unicode__(self):
        return "Introduction for %s, by user %s" % (self.pitchspot.title, self.pitchspot.owner.username)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
