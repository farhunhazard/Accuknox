# Accuknox Assignment 

This project demonstrates the use of Django signals and implements a simple `Rectangle` class in Python.

## Overview
This project explores how Django signals operate in terms of:
1. Synchronous or asynchronous execution.
2. Threading context.
3. Transactional behavior.

Additionally, the project includes a `Rectangle` class that can be iterated over to get its length and width and includes a method to calculate its area.

## Instructions

### Django Signal Testing
1. **Testing Synchronous/Asynchronous Execution:** A signal is connected to the `post_save` event of a model, with a delay to check if the signal executes synchronously.
2. **Testing Thread Context:** Prints thread information in both the signal receiver and the model instance creation to verify they run in the same thread.
3. **Testing Transactional Context:** Uses `transaction.atomic()` to demonstrate that signals operate within the same transaction as the model creation.

### To test the signals:
- Run the Django shell:
  python manage.py shell
- Inside the shell, run:
   from signals_app.signal_tests import test_signal_threading, test_signal_transaction
   test_signal_threading()
   test_signal_transaction()

### Rectangle Class
The Rectangle class is implemented to accept length and width, allowing iteration over these attributes and calculating the area.
To test the Rectangle class, run:
python signals_app/rectangle.py


### Conclusion
This project provided hands-on experience with Django signals and Python class iteration, demonstrating their synchronous nature, threading behavior, transactional context, and additional functionality through the Rectangle class.
