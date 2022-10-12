from django.urls import path
from todolist.views import show_todolist, add_task, delete_task, update_task, login_user, logout_user, register_user, show_json, add_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('json/', show_json, name='show_json'),
    # path('create-task/', add_task, name='add_task'),
    path('add/', add_task_ajax, name='add_task_ajax'),
    path('delete_task/<id>', delete_task, name='delete_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register_user, name='register_user'),
]
