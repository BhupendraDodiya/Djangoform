from django.urls import path
from app import views


urlpatterns = [
    path('',views.show),
    path('add/',views.add),
    path('table/',views.table),
    path('delete/<int:uid>/',views.delete),
    path('update/<int:uid>/',views.update),
    path('ur/',views.ur),
]
