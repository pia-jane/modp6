'''
I hereby attest to the truth of the following facts:

I have not discussed the Python code in my program with anyone
other than my instructor or the teaching assistants assigned to this course.

I have not used Python code obtained from another student, or
any other unauthorized source, whether modified or unmodified.

If any Python code or documentation used in my program was
obtained from another source, it has been clearly noted with citations in the
comments of my program.
'''

from django.contrib import admin
from .models import Supplier, WaterBottle, Account

# Register your models here.

admin.site.register(Supplier)
admin.site.register(WaterBottle)
admin.site.register(Account)
