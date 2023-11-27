from django.urls import path
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('search/', RecordsSearch.as_view(), name='search'),
    path('records-list/', RecordsList.as_view(), name='records_list'),
    path('create-record', record_create, name='record_create'),
    path('update-record/<int:pk>', record_update, name='record_update'),
    path('delete-record/<int:pk>', RecordDelete.as_view(), name='record_delete'),
    path('families-list/', FamiliesList.as_view(), name='families_list'),
    path('create-family', FamilyCreate.as_view(), name='family_create'),
    path('update-family/<int:pk>', FamilyUpdate.as_view(), name='family_update'),
    path('delete-family/<int:pk>', FamilyDelete.as_view(), name='family_delete'),
    path('names-list/', NamesList.as_view(), name='names_list'),
    path('create-name', NameCreate.as_view(), name='name_create'),
    path('update-name/<int:pk>', NameUpdate.as_view(), name='name_update'),
    path('delete-name/<int:pk>', NameDelete.as_view(), name='name_delete'),
    path('othestvos-list/', OtchestvosList.as_view(), name='otchestvos_list'),
    path('create-othestvo', OtchestvoCreate.as_view(), name='otchestvo_create'),
    path('update-othestvo/<int:pk>', OtchestvoUpdate.as_view(), name='otchestvo_update'),
    path('delete-othestvo/<int:pk>', OtchestvoDelete.as_view(), name='otchestvo_delete'),
    path('streets-list/', StreetsList.as_view(), name='streets_list'),
    path('create-street', StreetCreate.as_view(), name='street_create'),
    path('update-street/<int:pk>', StreetUpdate.as_view(), name='street_update'),
    path('delete-street/<int:pk>', StreetDelete.as_view(), name='street_delete'),
    path('mobs-list/', MobsList.as_view(), name='mobs_list'),
    path('create-mob', MobCreate.as_view(), name='mob_create'),
    path('update-mob/<int:pk>', MobUpdate.as_view(), name='mob_update'),
    path('delete-mob/<int:pk>', MobDelete.as_view(), name='mob_delete')
]

