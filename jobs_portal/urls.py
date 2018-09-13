from django.conf.urls import url
from . import views


urlpatterns=[

    url(r'^$',views.home,name='home'),
    url(r'^login/',views.login_user,name='login'),
    url(r'^logout/',views.logout_user,name='logout'),
    url(r'^hydjobs/',views.hyd,name='hydjobs'),
    url(r'^punejobs/',views.pune,name='punejobs'),
    url(r'^blrjobs/',views.blr,name='blrjobs'),
    url(r'^chennaijobs/',views.chennai,name='chennaijobs'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^register/',views.register_user,name='register'),

]
