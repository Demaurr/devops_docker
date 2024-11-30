from django.contrib import admin
from django.urls import path
from django_app.views import user_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_list, name='user-list'),
]

