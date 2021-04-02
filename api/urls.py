from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('task-list/', views.taskList, name="task-list"),
    path('task-detail/<str:pk>', views.taskDetail, name="task-detail"),
    path('task-update/<str:pk>', views.updateTask, name="task-update"),
    path('task-create/', views.taskCreate, name="task-create"),
    path('task-delete/<str:pk>', views.taskDelete, name="task-delete"),
]