from django.contrib	import admin
from demo.apps.ventas.models import client, production, productCategory

admin.site.register(client)
admin.site.register(production)
admin.site.register(productCategory)
