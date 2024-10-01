import time
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class TestModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(post_save, sender=TestModel)
def my_receiver(sender, instance, **kwargs):
    print("Signal received!")
    # Introduce a delay to simulate a time-consuming task
    time.sleep(5)
    print("Signal processing finished.")

# Testing the signal execution
def create_instance():
    print("Creating instance...")
    start_time = time.time()
    TestModel.objects.create(name="Test")
    end_time = time.time()
    print(f"Instance created. Time taken: {end_time - start_time} seconds")
