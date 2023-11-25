from django.urls import path
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('records-list/', RecordsList.as_view(), name='records_list'),
    path('create-record', record_create, name='record_create'),
    path('change-record/<int:pk>', record_change, name='record_change'),
    path('delete-record/<int:pk>', RecordDelete.as_view(), name='record_delete'),
]
