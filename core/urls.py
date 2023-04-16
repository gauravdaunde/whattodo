from django.urls import path
from .views import IndexPage, CreateToDoCreateView, ToDoDeleteView

urlpatterns = [
    path('', IndexPage.as_view()),
    path('create-todo/', CreateToDoCreateView.as_view()),
    path('delete-todo/<int:todo_id>/', ToDoDeleteView.as_view())
]
