from django.urls import path , include
from .views import *

urlpatterns = [
   path('', index ,name='index' ),
   path('all/', todolistview.as_view() ,name='all_todo'),
   path('add/', add_newCreateView.as_view() ,name='add_new'),
   path('todo/<int:pk>/', todoDetailView.as_view() ,name='todo_detail'),
   path('edit/<int:pk>/', todoUpdateView.as_view() ,name='update_todo'),
   path('delete/<int:pk>/', todoDeleteView.as_view() ,name='delete_todo')


]
