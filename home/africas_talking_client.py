import africastalking

# Replace with your sandbox/production credentials
USERNAME = "sandbox"  # or your actual username in production
API_KEY = "atsk_af53c160d5e9d045c53cbcd5ef55a88bf6c276eba11fd74e21e17d0b1ae5fb568ec0ce72"

# Initialize SDK
africastalking.initialize(USERNAME, API_KEY)

# Get the SMS service
sms = africastalking.SMS
