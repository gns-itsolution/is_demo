
from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def tasks_ag_grid(request):
    """Функция собирает все незавершенные задачи"""
    but = request.bitrix_user_token
    tasks_list = but.call_list_method('tasks.task.list', {'filter': {'!STATUS': '5'}})['tasks']

    tasks = []
    for task in tasks_list:
        tasks.append({'TITLE': task['title'], 'DESCRIPTION': task['description']})
    return render(request, 'tasks_ag.html', {'tasks': tasks})
