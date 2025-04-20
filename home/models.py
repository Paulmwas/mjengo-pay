from django.db import models

# Create your models here.
class Job(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    pay_amount = models.DecimalField(max_digits=20, decimal_places=2)
    pay_frequency = models.CharField(max_length=20,choices=(('daily', 'Daily'), ('weekly', 'Weekly'), ('on_completion', 'On Completion')),default='daily')
    worker_type = models.CharField(max_length=100)
    num_workers_needed = models.PositiveBigIntegerField(default=1)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='open')

    def __str__(self):
        return f"{self.title} at {self.location} ({self.status})"

