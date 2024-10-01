import threading
from django.db import transaction
from signals_app.models import TestModel

# Question 2: Do Django Signals Run in the Same Thread as the Caller?
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=TestModel)
def my_receiver(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

def test_signal_threading():
    print(f"Creating instance in thread: {threading.current_thread().name}")
    TestModel.objects.create(name="Threading Test")

# Question 3: Do Django Signals Run in the Same Database Transaction as the Caller?
@receiver(post_save, sender=TestModel)
def transaction_receiver(sender, instance, **kwargs):
    print(f"Signal received for instance: {instance.name}")
    # Simulate some database operation in the receiver
    instance.name = "Updated in Signal"
    instance.save()

def test_signal_transaction():
    try:
        with transaction.atomic():
            print("Creating instance...")
            instance = TestModel.objects.create(name="Transaction Test")
            print(f"Instance created with name: {instance.name}")
            # Raise an exception to force a transaction rollback
            raise Exception("Simulating an error to rollback transaction")
    except Exception as e:
        print(f"Exception occurred: {e}")

    # Check if the instance exists in the database
    instance_exists = TestModel.objects.filter(name="Transaction Test").exists()
    print(f"Instance exists after rollback: {instance_exists}")
