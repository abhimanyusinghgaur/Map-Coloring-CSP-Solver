from django.conf.urls import url, include
from . import views

app_name = 'MapColoring'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^result$', views.process_csp_and_color_map, name='result'),
]