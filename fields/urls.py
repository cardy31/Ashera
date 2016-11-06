from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from fields import views
from django.views.generic.base import RedirectView

# app_name = 'fields'
urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^fields/$',
        views.FieldList.as_view(),
        name='field-list'),
    url(r'^fields/(?P<pk>[0-9]+)/$',
        views.FieldDetail.as_view(),
        name='field-detail'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^accounts/profile/$',
        RedirectView.as_view(url='/', permanent = False),
        name = 'login'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
