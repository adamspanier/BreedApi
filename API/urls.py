"""
Modified by Adam Spanier
"""

from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from API_App import views

router = routers.DefaultRouter()
router.register(r'dogs2', views.DogListViewSet)
router.register(r'dogs2/<int:id>', views.DogDetailViewSet)
router.register(r'breeds2', views.BreedListViewSet)
router.register(r'breeds2/<int:id>', views.BreedDetailViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(r'dogs', views.DogList.as_view()),
    path(r'breeds', views.BreedList.as_view()),
    path(r'dogs/<int:id>', views.DogDetail.as_view()),
    path(r'breeds/<int:id>', views.BreedDetail.as_view()),
    path('api/', include(router.urls))
]
