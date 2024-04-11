from django.urls import path, re_path
from .views import index


urlpatterns = [
    path('menu/', index, name="index"),
    path('<path:path>/', index, name="draw_menu")
    # re_path(r'^(\w+)/$', index, name='draw_menu'),
    # re_path(r'^(\w+)/(\w+)/$', index, name='index'),
    # re_path(r'^(\w+)/(\w+)/(\w+)/$', index, name='index'),
    # re_path(r'^(\w+)/(\w+)/(\w+)/(\w+)/$', index, name='index')
]
