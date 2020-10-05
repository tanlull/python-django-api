from django.conf.urls import url
from countries import views
from django.urls import path

urlpatterns =[
    path('',views.index,name='index'),
    url(r'^api/countries$',views.countries_list),
    url(r'^api/countries/(?P<pk>[0-9]+)$',views.countries_detail)
]