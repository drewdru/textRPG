from django.conf.urls import url
from django.contrib import admin
from main import views
urlpatterns = [
    # url(r'^', admin.site.urls),
    # url(r'^admin/', admin.site.urls),
    # url(r'^', include('main.urls')),
    url(r'^', views.home),
]