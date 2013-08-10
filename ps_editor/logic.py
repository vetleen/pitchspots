#from django.contrib.auth.models import User
#from django.contrib.auth import authenticate, login, logout
from datetime import datetime  
from django.utils.timezone import utc


from ps_editor.models import Pitchspot

def create_pitchspot(title, owner, is_published):
    ''' Creates a pitchspot '''
    def set_date_now ():
        ''' Returns current date in UTC-format'''
        return datetime.utcnow().replace(tzinfo=utc)
    MyPitchspot = Pitchspot.objects.create(title=title, owner=owner, is_published=is_published, date_created=set_date_now())

    MyPitchspot.admin.add(owner)
    MyPitchspot.save()
    #p.admin.all()


def get_pitch_spot_as_JSON(pitchspot):
    ''' Takes a pitchspot object as an argument and reads it's data into a dict, which it returns '''
    def get_admin_dict(pitchspot):
        ''' Returns a dict with all admins for the pitchsapot, and uses numbers for keys '''
        admin_dict = {}
        for key, user in enumerate(pitchspot.admin.all()):
            admin_dict.update({key+1: user.username})
        return admin_dict
    admin_dict = get_admin_dict(pitchspot)
    pitchspot_dict = {
                      'title': pitchspot.title, 
                      'owner': pitchspot.owner.username, 
                      'admin': admin_dict, #this is already a dictionary type
                      'is_published': pitchspot.is_published,
                      'date_created': 
                          {
                          'year': pitchspot.date_created.year,
                          'month': pitchspot.date_created.month,
                          'day': pitchspot.date_created.day,
                          'hour': pitchspot.date_created.hour,
                          'minute': pitchspot.date_created.minute,
                          'second': pitchspot.date_created.second,
                          },
                      } 
                      
    pitchspot_JSON = json.dumps(pitchspot_dict, sort_keys=True, indent=4, separators=(',', ': '))
    return pitchspot_JSON


#def edit_pitchspot(title, owner, administrator, is_published, date_completed):



    
