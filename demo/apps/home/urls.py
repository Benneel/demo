from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('demo.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^about/$','about_view',name='vista_about'),
	url(r'^productions/$','productions_view',name='vista_productions'),
	url(r'^contacts/$','contacts_view',name='vista_contacts'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
)
