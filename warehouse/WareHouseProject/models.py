from django.db import models



class Company(models.Model):
	company_name = models.CharField(max_length = 250)
	
	def __str__(self):
		return self.company_name
	

class Goods(models.Model):
	stock_name = models.CharField(max_length = 250)
	stock_cost = models.DecimalField(max_digits=10, decimal_places=2)
	stock_company = models.ForeignKey(Company, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.stock_name + ' - ' + str(self.stock_cost) + ' - ' + str(self.stock_company)
	
	
class Customer(models.Model):
	customer_name = models.CharField(max_length = 20)
	customer_of_company = models.ForeignKey(Company, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.customer_name + ' - ' + str(self.customer_of_company)




















# Create your models here.
