from django.contrib.auth.models import User
from ps_editor.models import Pitchspot
from ps_editor import logic

def setup_shell():
    u=User.objects.get(id=1)
    print "User created and is available in variable 'u'"
    p1 = Pitchspot.objects.get(id=1)
    p2 = Pitchspot.objects.get(id=2)
    p3 = Pitchspot.objects.get(id=3)

p3 = logic.create_pitchspot(title="test3", owner=u, is_published=True)


    print "p1, p2 and p3 created with owner u"
#from ps_editor.setupshellfortesting import setup_shell

