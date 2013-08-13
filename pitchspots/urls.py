from django.conf.urls import patterns, include, url
import os.path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

static = os.path.join(os.path.dirname(__file__), 'static')

urlpatterns = patterns('',
    
    url(r'^$', 'ps_editor.views.frontpageview', name='frontpageview'),
    url(r'^frontpage/$', 'ps_editor.views.frontpageview', name='frontpage-by-specific-url'),
    
    #### PS_EDITOR ####
    url(r'^pitchspot/create/$', 'ps_editor.views.create_pitchspot_view', name='create_pitchspot_view'),
    url(r'^pitchspot/JSON/(?P<pitchspot_id>\d*)/$', 'ps_editor.views.retrieve_pitchspot_as_JSON_view', name='retrieve_pitchspot_as_JSON_view'),   
    url(r'^pitchspot/(?P<pitchspot_id>\d*)/$', 'ps_editor.views.retrieve_pitchspot_view', name='retrieve_pitchspot_view'),   

    #### USER ####    
    url(r'^user/login/$', 'user_management.views.loginview', name='loginview'),
    url(r'^user/logout/$', 'user_management.views.logoutview', name='logoutview'),
    url(r'^user/create/$', 'user_management.views.createnewuserview', name='createnewuserview'),
    url(r'^user/edit/$', 'user_management.views.edituserview', name='edituserview'),
    url(r'^user/changepassword/$', 'user_management.views.changepasswordview', name='changepasswordview'),
    #url(r'^user/delete/$', 'user_management.views.deleteuserview', name='deleteuserview'),
    #url(r'^user/loginrequired/$', 'user_management.views.loginrequiredview', name='loginrequiredview'),
	
	#### STATIC ####
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': static }),
    # url(r'^ticked/', include('ticked.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
