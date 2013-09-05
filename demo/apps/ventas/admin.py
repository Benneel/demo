from django.contrib	import admin
from demo.apps.ventas.models import client, production, productCategory

class productAdmin(admin.ModelAdmin):
	list_display = ('number', 'thumbnail', 'price','stock')
	list_filter = ('number','price')
	search_fields = ('number','price')
	fields = ('number', 'description', ('price', 'stock'), 'image', 'category', 'status')

admin.site.register(client)
admin.site.register(production, productAdmin)
admin.site.register(productCategory)
