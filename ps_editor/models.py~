from datetime import datetime  
from django.utils.timezone import utc
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pitchspot(models.Model):
        
    ## Meta information
    title = models.CharField(max_length=75, blank=True)
    owner = models.ForeignKey(User, related_name="pitchspots_owned_set")
    admin = models.ManyToManyField(User, blank=True, null=True, related_name="pitchspots_administered_set")
    is_published = models.BooleanField(default=False)

    date_created = models.DateTimeField() #(default=datetime.utcnow().replace(tzinfo=utc))
    #date_completed = models.DateTimeField(blank=True, null=True)



    #def __unicode__(self):
    #    return self.title	
