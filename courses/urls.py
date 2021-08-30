from django.urls import path

from courses import views


app_name = 'courses'
urlpatterns = [
    path('', views.CoursesView.as_view(template_name='courses/courses_list.html'), name='courses-list'),
    path('<int:_id>/', views.CoursesView.as_view(), name='courses-detail'),
]
