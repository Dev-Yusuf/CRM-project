from django.urls import URLPattern, path
from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.lead_list, name='lead_list'),
    path('<int:pk>/', views.lead_detail, name='lead-detail'),
    path('leads/create/', views.lead_create, name='lead-create'),
    path('<int:pk>/update/', views.lead_update, name='lead-update'),

]


