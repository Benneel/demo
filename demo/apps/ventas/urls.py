from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.ventas.views',
	url(r'^add/product/$','addProduct_view',name="vista_add_product"),
)
