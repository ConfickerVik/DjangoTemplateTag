from django.urls import path, re_path
from .views import index


urlpatterns = [
    path('menu/', index, name="index"),
    path('<path:path>/', index, name="draw_menu"),
]
