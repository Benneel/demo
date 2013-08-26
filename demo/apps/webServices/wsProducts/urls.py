from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('demo.apps.webServices.wsProducts.views',
	url(r'^ws/products/$','wsProducts_view',name="ws_products_url"),
)
