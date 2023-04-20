from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('<int:post_pk>/answer/<str:answer>', views.answer, name='answer'),
    path('<int:post_pk>/likes/', views.post_like, name='post_like')
]
