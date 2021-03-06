from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('demo.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^productions/pages/(?P<pagina>.*)/$','productions_view',name='vista_productions'),
	url(r'^production/(?P<id_prod>.*)/$','singleProduct_view',name='vista_single_product'),
	url(r'^contacts/$','contacts_view',name='vista_contacts'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^register/$','register_view',name='vista_register'),
	url(r'^logout/$','logout_view',name='vista_logout'),
)
