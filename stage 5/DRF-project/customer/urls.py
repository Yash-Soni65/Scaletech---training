from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

router = DefaultRouter()
router.register('viewset', CustomerViewSet, basename='customer')

urlpatterns = [
    path('', views.CustomerListCreateView.as_view(), name='customer-list-create'),
    path('', include(router.urls)),
]