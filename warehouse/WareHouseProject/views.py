from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Company, Goods, Customer
from .import forms





def goods_detail(request):
	all_goods = Goods.objects.all()
	template = loader.get_template('WareHouseProject/goods_detail.html')
	context = {'all_goods': all_goods}
	return HttpResponse (template.render(context, request))
	

def good_info(request, good_id):
	good = Goods.objects.get(id=good_id)
	template = loader.get_template('WareHouseProject/good_info.html')
	context = {'good': good}
	return HttpResponse (template.render(context, request))


def company_detail(request):
	
	all_companies = Company.objects.all()
	template = loader.get_template('WareHouseProject/company_detail.html')
	context = {'all_companies': all_companies}
	return HttpResponse (template.render(context, request))
	
def company_info(request, company_id):
	company = Company.objects.get(id=company_id)
	template = loader.get_template('WareHouseProject/company_info.html')
	context = {'company': company}
	return HttpResponse (template.render(context, request))
	
def customer_info(request, customer_id):
	customer = Customer.objects.get(id=customer_id)
	template = loader.get_template('WareHouseProject/customer_info.html')
	context = {'customer': customer}
	return HttpResponse (template.render(context, request))

		
def customers_detail(request):
	all_customers = Customer.objects.all()
	template = loader.get_template('WareHouseProject/customers_detail.html')
	context = {'all_customers': all_customers}
	return HttpResponse (template.render(context, request))
	
	
def index(request):
	
	preview = {'F':"Companies", 'Z':"Goods", 'Za':"Customers", 'Form1':"Create_Company", 'Form2':"Create_Customer", 'Form3':"Create_Good"}
	template = loader.get_template('WareHouseProject/index.html')
	context = {'preview': preview}
	return HttpResponse (template.render(context, request))
	

def company_create(request):
	template = loader.get_template('WareHouseProject/create_company_form.html')
	
	if request.method =='POST':
		form = forms.CreateCompany(request.POST)
		if form.is_valid():
			form.save()
			form = forms.CreateCompany()
	else:
		form = forms.CreateCompany()
		
	context = {'form': form}
	return HttpResponse(template.render(context, request))
	
	
	
def customer_create(request):
	template = loader.get_template('WareHouseProject/create_customer_form.html')
	
	if request.method =='POST':
		form = forms. CreateCustomer(request.POST)
		if form.is_valid():
			form.save()
			form = forms.CreateCustomer()
	else:
		form = forms.CreateCustomer()
		
	context = {'form': form}
	return HttpResponse(template.render(context, request))

def good_create(request):
	template = loader.get_template('WareHouseProject/create_good_form.html')
	
	if request.method =='POST':
		form = forms. CreateGood(request.POST)
		if form.is_valid():
			form.save()
			form = forms.CreateGood()
	else:
		form = forms.CreateGood()
		
	context = {'form': form}
	return HttpResponse(template.render(context, request))


def delete_good(request, id):
	template = loader.get_template('WareHouseProject/good_info.html')
	obj = get_object_or_404(Goods, id=id)
	if request.method == "POST":
		obj.delete()
		return HttpResponseRedirect('../../')
	context = {"object":obj}
	return HttpResponse(template.render(context, request))

def delete_company(request, id):
	template = loader.get_template('WareHouseProject/company_info.html')
	obj = get_object_or_404(Company, id=id)
	if request.method == "POST":
		obj.delete()
		return HttpResponseRedirect('../../')
	context = {"object":obj}
	return HttpResponse(template.render(context, request))

def delete_customer(request, id):
	template = loader.get_template('WareHouseProject/customer_info.html')
	obj = get_object_or_404(Customer, id=id)
	if request.method == "POST":
		obj.delete()
		return HttpResponseRedirect('../../')
	context = {"object":obj}
	return HttpResponse(template.render(context, request))



# Create your views here.
