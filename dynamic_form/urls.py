from django.urls import path

from . import views

app_name = 'dynamic_form'

urlpatterns = [
    path('', views.dynamic_form_view, name='dynamic_form_view'),
    path('data/', views.show_data, name='show_data'),
]
