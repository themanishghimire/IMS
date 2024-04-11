from django.urls import path
from .views import DepartmentView, ResourceView, ResourceDetailView, login, register, group_listing

urlpatterns = [
    path('department/',DepartmentView.as_view({'get':'list','post':'create'})),
    path('department/<int:pk>/',DepartmentView.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('resource/',ResourceView.as_view()),
    path('resource/<int:pk>/',ResourceDetailView.as_view()),
    path('login/',login),
    path('register/',register),
    path('role/',group_listing)
    ]

