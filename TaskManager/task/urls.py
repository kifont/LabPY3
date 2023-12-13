from django.urls import path
from task.views import CategoryListCreateView, CategoryDetailView, TaskListCreateView, TaskDetailView
from rest_framework.authtoken import views as auth_views
from .auth_view import CustomAuthToken, RegisterUserView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('register/', RegisterUserView.as_view(), name='register'),
]