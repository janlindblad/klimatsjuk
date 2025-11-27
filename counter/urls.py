from django.urls import path
from . import views

app_name = 'counter'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('planeten/', views.planeten, name='planeten'),
    path('radd/', views.radd, name='radd'),
    path('systemet/', views.systemet, name='systemet'),
    path('press/', views.press, name='press'),
    path('submit/', views.submit_quote, name='submit_quote'),
    path('api/quotes/', views.approved_quotes_api, name='approved_quotes_api'),
]
