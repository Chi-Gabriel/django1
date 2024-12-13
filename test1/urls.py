from django.urls import path
from . import views 

urlpatterns = [
    path( '' , views.getRoutes),
    path ( 'data/' , views.getTable),
    path ( 'data/<str:pk>/' , views.getRecord),
    path ( 'create/'  , views.createRecord  ),
    path ( 'change/<str:pk>/'  , views.updateRecord  ),
    path ( 'delete/<str:pk>/'  , views.deleteRecord ),
]