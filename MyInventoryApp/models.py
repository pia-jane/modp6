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

from django.db import models

# Create your models here.

class Supplier(models.Model):
	name = models.CharField(max_length=300)
	city = models.CharField(max_length=300)
	country = models.CharField(max_length=300)
	createdAt = models.DateTimeField(blank=True, null=True)
	objects = models.Manager()
	
	def __str__(self):
		return '{} - {}, {} created at: {}'.format(self.name,self.city,self.country,self.createdAt)
	
class WaterBottle(models.Model):
	sku = models.CharField(max_length=3)
	brand = models.CharField(max_length=300)
	cost = models.DecimalField(max_digits=7,decimal_places=2)
	size = models.CharField(max_length=10)
	mouthSize = models.CharField(max_length=14)
	color = models.CharField(max_length=11)
	suppliedBy = models.ForeignKey(Supplier,on_delete=models.CASCADE)
	currentQuantity = models.PositiveSmallIntegerField()

	def __str__(self):
		return '{}: {}, {}, {}, {}, supplied by {}, {} : {}'.format(self.sku,self.brand,self.mouthSize,self.size,self.color,self.suppliedBy,self.cost,self.currentQuantity)
	

class Account(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password1 = models.CharField(max_length=200)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password1

