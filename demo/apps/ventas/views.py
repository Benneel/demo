from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import production
from django.http import HttpResponseRedirect

def edit_product_view(request, id_prod):
	info = "initiated"
	prod = production.objects.get(pk = id_prod)
	form = addProductForm(request.POST, request.FILES, instance = prod)
	if form.is_valid():
		edit_prod = form.save(commit = False)
		form.save_m2m()
		edit_prod.status = True
		edit_prod.save()
		info = "edited successfully"
		return HttpResponseRedirect('/production/%s'%edit_prod.id)
	else:
		form = addProductForm(instance=prod)
	ctx = {'form':form, 'information':info}
	return render_to_response('sales/editProduct.html',ctx,context_instance=RequestContext(request))
def addProduct_view(request):
	info = "initiated"
	if request.method == "POST":
		form = addProductForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.status = True
			add.save()
			form.save_m2m()
			info = "successfully saved"
			return HttpResponseRedirect('/production/%s'%add.id)
	else:
		form = addProductForm()
	ctx = {'form':form, 'information':info}
	return render_to_response('sales/addProduct.html',ctx,context_instance=RequestContext(request))

"""
def addProduct_view(request):
	info = "Loading"
	if request.user.is_authenticated():
		if request.method == "POST":
			form = addProductForm(request.POST,request.FILES)
			if form.is_valid():
				number = form.cleaned_data['number']
				description = form.cleaned_data['description']
				image = form.cleaned_data['image']
				price = form.cleaned_data['price']
				stock = form.cleaned_data['stock']
				p = production()
				if image:
					p.image = image
				p.number = number
				p.description = description
				p.price = price
				p.stock = stock
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
"""
"""
def edit_product_view(request, id_prod):
	p = production.objects.get(id=id_prod)
	if request.method == "POST":
		form = addProductForm(request.POST, request.FILES)
		if form.is_valid():
			number = form.cleaned_data['number']
			description = form.cleaned_data['description']
			image = form.cleaned_data['image']
			price = form.cleaned_data['price']
			stock = form.cleaned_data['stock']
			p.number = number
			p.description = description
			p.price = price
			p.stock = stock
			if image:
				p.image = image
			p.save()
			return HttpResponseRedirect('/production/%s'%p.id)
	if request.method == "GET":
		form = addProductForm(initial={
				'number':p.number,
				'description':p.description,
				'price':p.price,
				'stock':p.stock,
			})
	ctx = {'form':form, 'production':p}
	return render_to_response('sales/editProduct.html',ctx,context_instance=RequestContext(request))
	"""