from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import production
from demo.apps.home.forms import ContactForm, LoginForm
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage,InvalidPage
def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	message = "This is a message"
	ctx ={'msg':message}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def productions_view(request,pagina):
	list_prod = production.objects.filter(status=True)
	paginator = Paginator(list_prod,5) #3 items per page
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productions = paginator.page(page)
	except (EmptyPage, InvalidPage):
		productions = paginator.page(paginator.num_pages)
	ctx = {'productions':productions}
	return render_to_response('home/productions.html', ctx, context_instance=RequestContext(request))

def singleProduct_view(request, id_prod):
	prod = production.objects.get(id=id_prod)
	ctx = {'production':prod}
	return render_to_response('home/SingleProduct.html',ctx,context_instance=RequestContext(request))

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

def login_view(request):
	message = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username,password=password)
				if user is not None and user.is_active:
					login(request,user)
					return HttpResponseRedirect('/')
				else:
					message = "username or password incorrect"
		form = LoginForm()
		ctx = {'form':form,'message':message}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

