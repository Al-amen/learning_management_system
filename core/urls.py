from django.urls import path
from .import views
urlpatterns = [
    path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('lessons/', views.LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/',views.LessonDetailView.as_view(), name='lesson-detail'),
    path('materials/',views. MaterialListCreateView.as_view(), name='material-list-create'),
    path('materials/<int:pk>/', views.MaterialDetailView.as_view(), name='material-detail'),
]
