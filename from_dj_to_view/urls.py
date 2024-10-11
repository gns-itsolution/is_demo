from django.urls import path
from from_dj_to_view.views.to_vue import index

urlpatterns = [
    path('to/', index, name='index'),
]