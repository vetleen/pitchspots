#from datetime import datetime  

#from django.utils.timezone import utc

from django.http import HttpResponse
#from django.template.loader import get_template
#from django.shortcuts import render_to_response, redirect
#from django.template import Context, RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login#, logout
#from django.core.context_processors import csrf
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


#    url(r'^user/edit/$', 'usermanagement.views.edituserview', name='edituserview'),
#    url(r'^user/changepassword/$', 'usermanagement.views.changepasswordview', name='changepasswordview'),
#    url(r'^user/delete/$', 'usermanagement.views.deleteuserview', name='deleteuserview'),

def createnewuserview (request):
    email = request.POST['email']
    username = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(username=username).count():
        output = "Username is taken."
        return HttpResponse(output)
    elif User.objects.filter(email=username).count():
        output = "Username is taken."
        return HttpResponse(output)
    else:
        #create the user
        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.save()
        #log the user in
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                output = "Account created, and user logged in."
                return HttpResponse(output)                
            else:
                #This shouldn't happen when you just created the user... Account is disabled..
                output = "Account disabled. This probably shouldn't happen."
                return HttpResponse(output)
        else:
                #This shouldn't happen when you just created the user... Password or username is incorrect.
            output = "Username and password does not match. This probably shouldn't happen."
            return HttpResponse(output)
    
def loginview (request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            #return redirect(frontpageview)
            output = "User logged in successfully."
            return HttpResponse(output)
        else:
            #return redirect(frontpageview)
            output = "Account disabled. Please contact support."
            return HttpResponse(output)
    else:
            #Should probably add a link to reset password in case it's forgotten here at some point
            output = "Username and password do not match."
            return HttpResponse(output)

def logoutview (request):
    output = "Successfully logged out."
    return HttpResponse(output)
