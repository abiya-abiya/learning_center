from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('courses/', views.course_list_view, name='course_list'),
    path('courses/add/', views.course_create_view, name='course_create'),
    path('groups/', views.group_list_view, name='group_list'),
    path('students/', views.student_list_view, name='student_list'),
    path('students/add/', views.student_create_view, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update_view, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete_view, name='student_delete'),
]
