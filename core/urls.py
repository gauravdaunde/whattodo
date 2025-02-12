from django.urls import path
from .views import IndexPage, CreateToDoCreateView, ToDoDeleteView

urlpatterns = [
    path('', IndexPage.as_view()),
    path('todos', CreateToDoCreateView.as_view()),
    path('todos/<int:todo_id>', ToDoDeleteView.as_view())
]
