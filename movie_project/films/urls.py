from django.contrib import admin
from django.urls import path
import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.film_create_view, name='film_add'),
    path('list/', views.film_list_view, name='film_list'),
   ]