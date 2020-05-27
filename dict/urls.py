from django.urls import path,re_path
from .views import word_search,get_word_meaning

urlpatterns = [
    path('',word_search,name='home'),
    re_path('get-meaning/(?P<pk>\d+)',get_word_meaning,name='meaning'),
]

app_name = 'dict'