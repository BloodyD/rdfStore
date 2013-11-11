from django.conf.urls.defaults import patterns

urlpatterns = patterns('store.views',
  (r'^load/$', "load"),
  (r'^query/$', "query"),
)