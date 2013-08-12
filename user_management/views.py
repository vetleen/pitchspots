#from datetime import datetime  

#from django.utils.timezone import utc

from django.http import HttpResponse
#from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect
from django.template import Context, RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login#, logout
#from django.core.context_processors import csrf
#from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

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
        messages.add_message(request, messages.ERROR, 'Username is unavailable, this may be because it is already in use.')
        template = "test_template.html"
        return render_to_response(template, {}, context_instance=RequestContext(request))
    else:
        #create the user
        new_user = User.objects.create_user(username=username, password=password, email=email)
        new_user.save()
        messages.add_message(request, messages.SUCCESS, 'User was successfully created.')
        #log the user in
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                template = "test_template.html"
                return render_to_response(template, {}, context_instance=RequestContext(request))        
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
    
@login_required#(login_url='/user/loginrequired/')
def edituserview (request):
    if request.POST['email']:
        email=request.POST['email']
        request.user.email = email
        request.user.username = email
    if request.POST['first_name']:
        first_name=request.POST['first_name']
        request.user.first_name = first_name
    if request.POST['last_name']:
        last_name=request.POST['last_name']
        request.user.last_name = last_name
    request.user.save()
    output = "Profile was successfully updated"
            
@login_required(login_url='/user/loginrequired/')
def changepasswordview(request):
    old_password = request.POST['old_password']
    new_password1 = request.POST['new_password']
    new_password2 = request.POST['repeat_new_password']
    if request.user.check_password(old_password):
        if new_password1 == new_password2:
            request.user.set_password(new_password1)
            request.user.save()
            output = "Password changed"
            return HttpResponse(output)
        else:
            output = "The new passwords didn't match."
            return HttpResponse(output)
    else:
        output = "Could not verify the old password."
        return HttpResponse(output)


















