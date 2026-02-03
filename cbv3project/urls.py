from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.StudentListView.as_view(), name='list'),

    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'),

    path('update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),

    path('create/', views.StudentCreateView.as_view(), name='create'),

    path('delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete'),
]
