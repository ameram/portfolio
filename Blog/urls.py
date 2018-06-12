from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.gen_show, name="general"),
    path('<int:blog_id>/', views.detail, name='detail'),
]
