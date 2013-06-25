from django.contrib	import admin
from demo.apps.ventas.models import client, production

admin.site.register(client)
admin.site.register(production)
