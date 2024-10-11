from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth


@main_auth(on_cookies=True)
def index(request):
    data = "Hello World"

    return render(request, 'to_vue.html', context={'data': data})
