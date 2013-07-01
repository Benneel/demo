from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import production

def add_product_view(request):
	if request.method == "POST":
		form = addProductForm(request.POST)
		info = "Initialization"
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
