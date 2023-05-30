from . import views
from django.urls import path

urlpatterns = [
    path('gettickets/', views.getTickets, name = 'get-tickets'),
    path('getusers/', views.getUsers, name = 'get-tickets'),
    path('createticket/<str:pk>/', views.createTicket, name = 'get-tickets'),
    path('taskdetail/<int:pk>/', views.taskDetail, name = 'task-detail'),
    path('createcomment/<str:pk>/', views.createComment, name = 'create-comment'),
    path('getcomments/<int:pk>/', views.getComments, name = 'get-comments'),
    path('updateticket/<str:pk>/', views.updateTicket, name= 'update-ticket')
    
]