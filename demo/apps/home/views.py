from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import production
from demo.apps.home.forms import ContactForm

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	message = "This is a message"
	ctx ={'msg':message}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def productions_view(request):
	prod = production.objects.filter(status=True)
	ctx = {'productions':prod}
	return render_to_response('home/productions.html', ctx, context_instance=RequestContext(request))

def contacts_view(request):
	info_send =False
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		theform = ContactForm(request.POST)
		if theform.is_valid():
			info_send = True
			email = theform.cleaned_data('Email')
			title = theform.cleaned_data('Title')
			text = theform.cleaned_data('Text')
	else:
		theform = ContactForm()
	ctx = {'form':theform,'email':email,'title':title,'text':text,'info_send':info_send}
	return render_to_response('home/contacts.html',ctx,context_instance=RequestContext(request))

