from django.conf.urls import url
from .views import home_view, signin_view, guest_access_view, trip_view
urlpatterns = [
    url(r'^signup/$', home_view, name='signup-view'),
    url(r'^signin/$', signin_view, name='signin-view'),
    url(r'^guest/$', guest_access_view, name='guest-view'),
    url(r'^list/$', trip_view, name='list-view'),
]
