#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
from datetime import datetime  
from django.utils.timezone import utc


from ps_editor.models import Pitchspot

def create_pitchspot(title, ps_owner, administrator, is_published, date_completed=None):
    Pitchspot.objects.create(title=title, ps_owner=ps_owner, administrator=administrator, date_created=datetime.utcnow().replace(tzinfo=utc), is_published=is_published)    




#def edit_pitchspot(title, owner, administrator, is_published, date_completed):



    
