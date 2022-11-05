from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_home, name='post_home'),
    #path('<str:username>', views.post_list, name='post_list_test'),
    path('post/user/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/noedit/<int:pk>/', views.post_detail_noedit, name='post_detail_noedit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
]