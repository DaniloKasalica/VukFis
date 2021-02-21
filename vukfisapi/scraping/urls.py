
from django.conf.urls import url
from scraping import views

urlpatterns = [
    url('', views.GetData.as_view(), name='getdata')
]