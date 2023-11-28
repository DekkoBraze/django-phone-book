from django.urls import path
from django.urls import path, include
from .views import *

records_urls = [
    path('search/', RecordsSearch.as_view(), name='search'),
    path('list/', RecordsList.as_view(), name='records_list'),
    path('create', record_create, name='record_create'),
    path('update/<int:pk>', record_update, name='record_update'),
    path('delete/<int:pk>', RecordDelete.as_view(), name='record_delete'),
]

families_urls = [
    path('list/', FamiliesList.as_view(), name='families_list'),
    path('create', FamilyCreate.as_view(), name='family_create'),
    path('update/<int:pk>', FamilyUpdate.as_view(), name='family_update'),
    path('delete/<int:pk>', FamilyDelete.as_view(), name='family_delete'),
]

names_urls = [
    path('list/', NamesList.as_view(), name='names_list'),
    path('create', NameCreate.as_view(), name='name_create'),
    path('update/<int:pk>', NameUpdate.as_view(), name='name_update'),
    path('delete/<int:pk>', NameDelete.as_view(), name='name_delete'),
]

otchestvos_urls = [
    path('list/', OtchestvosList.as_view(), name='otchestvos_list'),
    path('create', OtchestvoCreate.as_view(), name='otchestvo_create'),
    path('update/<int:pk>', OtchestvoUpdate.as_view(), name='otchestvo_update'),
    path('delete/<int:pk>', OtchestvoDelete.as_view(), name='otchestvo_delete'),
]

streets_urls = [
    path('list/', StreetsList.as_view(), name='streets_list'),
    path('create', StreetCreate.as_view(), name='street_create'),
    path('update/<int:pk>', StreetUpdate.as_view(), name='street_update'),
    path('delete/<int:pk>', StreetDelete.as_view(), name='street_delete'),
]

mobs_urls = [
    path('list/', MobsList.as_view(), name='mobs_list'),
    path('create', MobCreate.as_view(), name='mob_create'),
    path('update/<int:pk>', MobUpdate.as_view(), name='mob_update'),
    path('delete/<int:pk>', MobDelete.as_view(), name='mob_delete')
]

urlpatterns = [
    path('', index, name='index'),
    path('records/', include(records_urls)),
    path('families/', include(families_urls)),
    path('names/', include(names_urls)),
    path('otchestvos/', include(otchestvos_urls)),
    path('streets/', include(streets_urls)),
    path('mobs/', include(mobs_urls)),
]
