from django.urls import path
from . import views


urlpatterns = [
    path('', views.role_list_create, name='role-list-create'),
    path('<int:role_id>/', views.role_detail, name='role-detail'),
        path(
        '<int:role_id>/modules/add/',
        views.add_module,
        name='add-module'
    ),

    path(
        '<int:role_id>/modules/remove/',
        views.remove_module,
        name='remove-module'
    ),
]