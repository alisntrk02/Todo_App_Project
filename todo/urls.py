from django.urls import path, include

from .views import todo_list_create, todo_detail

urlpatterns = [
    path("todos/", todo_list_create),
    path("todos/<int:pk>/", todo_detail)
]