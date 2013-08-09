#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
from datetime import datetime  
from django.utils.timezone import utc


from ps_editor.models import Pitchspot

def create_pitchspot(title):
    MyPitchspot = Pitchspot.objects.create(title)    
    MyPitchspot.save()




#def edit_pitchspot(title, owner, administrator, is_published, date_completed):



    
