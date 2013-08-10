from django.contrib.auth.models import User
from ps_editor.models import Pitchspot
from ps_editor import logic

def setup_shell():
    u=User.objects.create_user(username="testuser", password="testpassword")
    print "User created and is available in variable 'u'"

    p1 = logic.create_pitchspot(title="test1", owner=u, is_published="True")
    p1.save()
    p2 = logic.create_pitchspot(title="test2", owner=u, is_published="True")
    p2.save()
    p3 = logic.create_pitchspot(title="test3", owner=u, is_published="True")
    p3.save()

    print "p1, p2 and p3 created with owner u"

