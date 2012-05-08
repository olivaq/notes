# Create your views here.
from note.models import Webpage, Note
from django.http import HttpResponse
from django.core import serializers
from django import forms
from django.shortcuts import render_to_response

#class NoteForm(forms.Form):
#	url = forms.CharField()
#	text = forms.TextField()
from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField()
	sender = forms.EmailField()
	cc_myself = forms.BooleanField(required=False)

import json
def webpage(request, url):
	if request.POST:
		dopost(request, url)
	
	f = Note.objects.filter(url=url)
	
	return fixResponse( render_to_response('webpage.html', {'notes':f}))


def dopost(request, url):
	n = Note(url = url, note = request.POST['note'])
	n.save()
	return HttpResponse("This is a post")

def fixResponse(response):
	response['Access-Control-Allow-Origin'] = '*'
	response['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS'
	response['Access-Control-Max-Age'] = 1000
	response['Access-Control-Allow-Headers'] = '*'
	return response
