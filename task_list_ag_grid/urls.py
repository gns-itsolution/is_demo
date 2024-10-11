from django.urls import path

from task_list_ag_grid.views.start import tasks_ag_grid

urlpatterns = [
    path('hello/', tasks_ag_grid, name='tasks_ag_grid'),
]