from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView



urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='list_view.html'), name='list-view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'demo/', include('demo.urls', namespace='demo'))
)
