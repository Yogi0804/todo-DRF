from django.urls import path
from . import views

urlpatterns = [
    path('',views.see,name="see"),
    path('task-list/',views.taskList,name="task-list"),
]
