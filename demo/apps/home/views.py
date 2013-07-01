from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import production
from demo.apps.home.forms import ContactForm
from django.core.mail import EmailMultiAlternatives

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
			email = theform.cleaned_data['Email']
			title = theform.cleaned_data['Title']
			text = theform.cleaned_data['Text']
			
			# Configuration via email
			to_admin = 'benneel7@gmail.com'
			html_content = "information received %s<br><br><br>***Message***<br><br>%s"%(email,text)
			msg = EmailMultiAlternatives('To contact',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		theform = ContactForm()
	ctx = {'form':theform,'email':email,'title':title,'text':text,'info_send':info_send}
	return render_to_response('home/contacts.html',ctx,context_instance=RequestContext(request))

