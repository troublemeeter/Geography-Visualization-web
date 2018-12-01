from django.conf.urls import url
from. import views as view

urlpatterns = [
    url('home/', view.index, name = 'home'),
    url('visualization/', view.Graph, name ='visualization'),
    url('about/', view.about, name ='visualization'),
]
