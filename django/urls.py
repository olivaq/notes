from django.conf.urls.defaults import *

from django_restapi.model_resource import Collection
from django_restapi.responder import JSONResponder
from django.http import HttpResponse
from notes.note.models import Note, Webpage

class XCollection(Collection):
    def __call__(self, request, *args, **kwargs):
    	print "READ"
        return self.fixResponse(Collection.__call__(self, request, *args, **kwargs))
    def create(self, request):
        return self.fixResponse(Collection.create(self, request))
    def read(self, request):
        return self.fixResponse(Collection.read(self, request))
    def fixResponse(self, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
        response['Access-Control-Max-Age'] = 1000
        response['Access-Control-Allow-Headers'] = '*'
        return response
    
note_resource = XCollection(
    queryset = Note.objects.all(),
    responder = JSONResponder(),
    )

webpage_resource = XCollection(
    queryset = Webpage.objects.all(),
    responder = JSONResponder(),
    )

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^notes/', include('notes.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   (r'^admin/', include(admin.site.urls)),
   url(r'^json/note/(.*?)/?$', note_resource),
   url(r'^json/webpage/(.*?)/?$', webpage_resource),
   url(r'^webpage/(?P<url>.+)$', 'note.views.webpage'),

)
