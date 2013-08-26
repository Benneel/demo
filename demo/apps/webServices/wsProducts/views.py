# Create your views here.
from django.http import HttpResponse
from demo.apps.ventas.models import production

from django.core import serializers

def wsProducts_view(request):
	data = serializers.serialize("xml", production.objects.filter(status=True))
	return HttpResponse(data, mimetype='application/xml')