from django.conf.urls import url
from lists import views

urlpatterns = [
    # Examples:
    url(r'^$', views.home_page, name='home'),
]
