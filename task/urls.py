from . import views
from django.urls import path
urlpatterns = [
    path("", views.home, name='home'),
    path("signup/",views.signup,name='signup'),
    path("tasks/",views.tasks, name="tasks"),
    path("tasks_completed/",views.tasks_completed, name="tasks_completed"),
    path("task/create/",views.create_task, name='create_task'),
    path("task/<int:task_id>/",views.task_detail, name='task_detail'),
    path("task/<int:task_id>/complete",views.complete_task, name='complete_task'),
    path("task/<int:task_id>/delete",views.delete_task, name='delete_task'),
    path("logout/",views.cerrar_sesion, name="logout"),
    path("signin/",views.iniciar_sesion, name="signin"),
]