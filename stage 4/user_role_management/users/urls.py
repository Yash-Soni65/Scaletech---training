from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('bulk-update/', views.bulk_update_users, name='bulk-update-users'),
    path('<int:user_id>/modules/check/', views.check_module_access, name='check-module-access'),
    path('', views.user_list_create, name='user-list-create'),
    path('<int:user_id>/', views.user_detail, name='user-detail'),
]