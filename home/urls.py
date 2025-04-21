from django.urls import path
from .views import home_page, send_sms_view,foreman_dashboard, create_job

urlpatterns = [
    path('', home_page, name='home'),
    path('send/', send_sms_view, name='send'),
    path('foreman-dashboard/',foreman_dashboard, name='foreman_dashboard'),
    path('create-job/', create_job, name='create_job'),
]
