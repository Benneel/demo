from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import production

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
