from django.contrib import admin
from django.urls import path

from board import views

app_name = 'board'
urlpatterns = [
    path('', views.BoardList.as_view(), name='board_list'),
    path('<int:pk>/', views.BoardDetail.as_view(), name='board_detail'),
    path('rubric/<int:pk>/', views.RubricDetail.as_view(), name='rubric_detail'),
    path('rubric/', views.RubricList.as_view(), name='rubric_list'),
]
