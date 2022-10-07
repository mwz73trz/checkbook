from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CheckbookViewSet

router = DefaultRouter()
router.register('checkbooks', CheckbookViewSet, basename='checkbook')

urlpatterns = [
    path('', include(router.urls)),
]