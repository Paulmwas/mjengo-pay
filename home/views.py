from django.shortcuts import render, redirect
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
        'to': '+254711662784'  
    }

    try:
        response = requests.post(url, headers=headers, data=data)
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def foreman_dashboard(request):
    job = Job.objects.all()
    return render(request, 'foreman_dashboard.html', {'job':job})


from datetime import datetime
from django.shortcuts import redirect
import requests

def create_job(request):
    if request.method == 'POST':
        # Process form data
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        
        # Convert string dates to datetime objects
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        
        pay_amount = request.POST.get('pay_amount')
        pay_frequency = request.POST.get('pay_frequency')
        worker_type = request.POST.get('worker_type')
        num_workers_needed = request.POST.get('num_workers_needed')
        
        # Create new job with converted dates
        job = Job.objects.create(
            title=title,
            description=description,
            location=location,
            start_date=start_date,
            end_date=end_date,
            pay_amount=pay_amount,
            pay_frequency=pay_frequency,
            worker_type=worker_type,
            num_workers_needed=num_workers_needed,
            status='open'
        )
        
        # Send SMS notification
        send_job_created_sms(job)
        
        # Redirect back to dashboard
        return redirect('foreman_dashboard')
    
    # If not POST, redirect to dashboard
    return redirect('foreman_dashboard')

def send_job_created_sms(job):
    url = "https://api.sandbox.africastalking.com/version1/messaging"
    
    headers = {
        'ApiKey': 'atsk_af53c160d5e9d045c53cbcd5ef55a88bf6c276eba11fd74e21e17d0b1ae5fb568ec0ce72',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    
    # Format the date - now we know job.start_date is a proper date object
    start_date_str = job.start_date.strftime('%d-%m-%Y')
    
    # Create a job-specific message
    message = f"Wozaa Kuna Mjengo!!!: {job.title} in {job.location}. Malipo ni: Ksh{job.pay_amount} ({job.get_pay_frequency_display()}). Wanataka Wafanya Kazi: {job.num_workers_needed} {job.worker_type}. Inaanza: {start_date_str}."
    
    data = {
        'username': 'sandbox',
        'from': '42973',
        'message': message,
        'to': '+254711662784'  # You might want to make this dynamic or fetch from settings
    }
    
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.json()
    except Exception as e:
        # Log the error but don't interrupt the flow
        print(f"SMS sending error: {str(e)}")
        return {'error': str(e)}