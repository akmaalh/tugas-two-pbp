from django.urls import path
from todolist.views import show_todolist, add_task, delete_task, update_task, login_user, logout_user, register_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('create-task/', add_task, name='add_task'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register_user, name='register_user'),
]
