from django.urls import path
from . import views

app_name = 'counter'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('submit/', views.submit_quote, name='submit_quote'),
    path('api/quotes/', views.approved_quotes_api, name='approved_quotes_api'),
]
