from django.urls import path

from webapp.views.to_do import add_view, detail_view, delete_task, update_view, confirm_delete_task
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path('to_do/', index_view),
    path('to_do/add', add_view, name='to_do_add'),
    path('to_do/<int:pk>', detail_view, name='to_do_detail'),
    path('to_do/<int:pk>/delete/', delete_task, name='to_do_delete'),
    path('to_do/<int:pk>/confirm_delete/', confirm_delete_task, name='confirm_delete'),
    path('to_do/<int:pk>/update/', update_view, name='to_do_update'),
]