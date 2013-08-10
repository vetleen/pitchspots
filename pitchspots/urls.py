from django.conf.urls import patterns, include, url
import os.path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

static = os.path.join(os.path.dirname(__file__), 'static')

urlpatterns = patterns('',
    
    url(r'^$', 'ps_editor.views.frontpageview', name='frontpageview'),
    url(r'^frontpage/$', 'ps_editor.views.frontpageview', name='frontpage-by-specific-url'),
    url(r'^pitchspot/create/$', 'ps_editor.views.create_pitchspot_view', name='create_pitchspot_view'),
    url(r'^pitchspot/(?P<pitchspot_id>\d*)/$', 'ps_editor.views.retrieve_pitchspot_view', name='retrieve_pitchspot_view'),   
    
    
    
#    #### TODO MANAGEMENT ####
#    url(r'^todos/view/$', 'todotracker.views.viewtodosview', name='viewtodosview'),
#    url(r'^todos/view/(?P<pgnumb>\d*)/$', 'todotracker.views.viewtodosview', name='pagesoftodosview'),
#    url(r'^todos/add/$', 'todotracker.views.addtodoview', name='addtodoview'),
#    url(r'^todos/tick/(?P<todoid>\d*)/$', 'todotracker.views.ticktodoview', name='ticktodoview'),
#    url(r'^todos/untick/(?P<todoid>\d*)/$', 'todotracker.views.unticktodoview', name='unticktodoview'),
#    url(r'^todos/view/ticked/$', 'todotracker.views.viewtickedtodoview', name='viewtickedtodo'),
#    url(r'^todos/delete/(?P<todoid>\d*)/$', 'todotracker.views.deletetodoview', name='deletetodoview'),
#    url(r'^todos/edit/(?P<todoid>\d*)/$', 'todotracker.views.edittodoview', name='edittodoview'),
#    url(r'^todos/update/(?P<todoid>\d*)/$', 'todotracker.views.updatetodoview', name='updatetodoview'),

    #### USER MANAGEMENT ####    
    url(r'^user/login/$', 'user.views.loginview', name='loginview'),
    url(r'^user/logout/$', 'user.views.logoutview', name='logoutview'),
    url(r'^user/create/$', 'user.views.createnewuserview', name='createnewuserview'),
    url(r'^user/edit/$', 'user.views.edituserview', name='edituserview'),
    url(r'^user/changepassword/$', 'user.views.changepasswordview', name='changepasswordview'),
    url(r'^user/delete/$', 'user.views.deleteuserview', name='deleteuserview'),
    url(r'^user/loginrequired/$', 'user.views.loginrequiredview', name='loginrequiredview'),
	#### STYLESHEETS ####
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': static }),
    # url(r'^ticked/', include('ticked.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
