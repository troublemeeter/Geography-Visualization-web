from django.conf.urls import url
from. import views as view

urlpatterns = [
    url('home/', view.index, name = 'home'),
    url('visualization1/', view.Graph1, name ='visualization1'),
    url('visualization2/', view.Graph2, name ='visualization2'),
    url('about/', view.about, name ='about'),
]
