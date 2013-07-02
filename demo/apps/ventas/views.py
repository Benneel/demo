from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import production
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "Loading"
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST)
			if form.is_valid():
				number = form.cleaned_data['number']
				description = form.cleaned_data['description']
				p = production()
				p.number = number
				p.description = description
				p.status = True
				p.save()
				info = "was saved successfully"

			else:
				info = "information was incorrect"
			form = addProductForm()
			ctx = {'form':form,'information':info}
			return render_to_response('sales/addProduct.html',ctx,context_instance=RequestContext(request))
		else:
			form = addProductForm()
			ctx = {'form':form}
			return render_to_response('sales/addProduct.html',ctx,context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
