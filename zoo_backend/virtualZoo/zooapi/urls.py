from django.urls import path 
from .views import AnimalList, AnimalDetail, AnimalCreate, AnimalListSortByWeight

name = 'zooapi'

urlpatterns = [
    path('<int:pk>/', AnimalDetail.as_view(), name='animaledit'),
    path('', AnimalList.as_view(), name='overviewcreate'),
    path('new', AnimalCreate.as_view(), name='animalcreate'),
]