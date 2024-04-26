# teammatesmodule/urls.py
from django.urls import path,include
from . import views

app_name = 'teammatesmodule'

urlpatterns = [
    path('viewtasks/', views.viewtasks, name='viewtasks'),
    path('personaltaskpost/', views.personaltaskpost, name='personaltaskpost'),
    path('view_personal_task_details/', views.view_personal_task_details, name='view_personal_task_details'),
    path('add_personal_task_details/', views.add_personal_task_details, name='add_personal_task_details'),
    path('task_details_list/',views.task_details_list,name='task_details_list'),
    path('edit/<int:task_id>/', views.edit_personal_task_details, name='edit_personal_task_details'),
    path('delete/<int:task_id>/', views.delete_personal_task_details, name='delete_personal_task_details'),
]




