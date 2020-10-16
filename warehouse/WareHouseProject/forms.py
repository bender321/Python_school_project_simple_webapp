from django import forms
from . import models


class CreateCompany(forms.ModelForm):
	class Meta:
		model = models.Company
		fields = ['company_name']
		
class CreateCustomer(forms.ModelForm):
	class Meta:
		model = models.Customer
		fields = ['customer_name','customer_of_company']
		
class CreateGood(forms.ModelForm):
	class Meta:
		model = models.Goods
		fields = ['stock_name','stock_cost', 'stock_company']