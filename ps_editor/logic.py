#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
from datetime import datetime  
from django.utils.timezone import utc


from ps_editor.models import Pitchspot

def create_pitchspot(title, owner):
    MyPitchspot = Pitchspot.objects.create(title=title, owner=owner, administrator=owner)
    MyPitchspot.save()



#def edit_pitchspot(title, owner, administrator, is_published, date_completed):



    
