from django.shortcuts import render
from django.http import JsonResponse
from .africas_talking_client import sms
from .models import Job
# Create your views here.
def home_page(request):
    return render(request, 'home.html')


import requests
from django.http import JsonResponse

def send_sms_view(request):
    url = "https://api.sandbox.africastalking.com/version1/messaging"

    headers = {
        'ApiKey': 'atsk_af53c160d5e9d045c53cbcd5ef55a88bf6c276eba11fd74e21e17d0b1ae5fb568ec0ce72',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    data = {
        'username': 'sandbox',
        'from': '42973',
        'message': "Hello, Kuna Mjengo",
        'to': '+254711662784'  # replace with a valid simulator number
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def foreman_dashboard(request):
    job = Job.objects.all()
    return render(request, 'foreman_dashboard.html', {'job':job})


