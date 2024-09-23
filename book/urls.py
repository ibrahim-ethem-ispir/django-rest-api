from django.urls import path
from .views import book_list, book_create, book_detail, book_update, book_delete

urlpatterns = [
    path('list', book_list),
    path('add', book_create),
    path('detail/<uuid:pk>', book_detail),
    path('update/<uuid:pk>', book_update),
    path('delete/<uuid:pk>', book_delete),
]
