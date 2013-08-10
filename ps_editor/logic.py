#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
from datetime import datetime  
from django.utils.timezone import utc


from ps_editor.models import Pitchspot

def create_pitchspot(title, owner, is_published):
    def set_date_now ():
        return datetime.utcnow().replace(tzinfo=utc)
    MyPitchspot = Pitchspot.objects.create(title=title, owner=owner, is_published=is_published, date_created=set_date_now())
    MyPitchspot.save()
    #MyPitchspot.owner.pitchspots_administered_set.add(MyPitchspot)
    #MyPitchspot.save()



#def edit_pitchspot(title, owner, administrator, is_published, date_completed):



    
