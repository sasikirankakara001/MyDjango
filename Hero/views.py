from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .forms import ContactForm,RegisterForm
from .models import Contact,Register
# Create your views here.
from django.contrib import messages
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
def index(request):
	return render(request,'Hero/base.html')

def Contacts(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/Hero/Show')

	form = ContactForm()
	return render(request,'Hero/Contact.html',{'form':form})


def Show(request):
	data=Contact.objects.all()
	return render(request,'Hero/showdata.html',{'data':data})

def Edit(request,id):
	data=Contact.objects.get(id=id)
	if request.method=="POST":
		form=ContactForm(request.POST,instance=data)
		if form.is_valid():
			form.save()
			return redirect('/Hero/Show')
	form=ContactForm(instance=data)
	return render(request,'Hero/edit.html',{"form":form,"data":data})
def delete(request,id):
	data=Contact.objects.get(id=id)
	data.delete()
	return redirect('/Hero/Show')

def RegShow(request):
	data=Register.objects.all()
	return render(request,'Hero/regshow.html',{'data':data})
def RegForm(request):
	if request.method=="POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			# name = form.cleaned_data.get('name')
			# messages.success(request, 'Account was created for ' + name)
		return redirect('/Hero/RegShow')

	form=RegisterForm()
	return render(request,'Hero/regform.html',{'form':form})

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/Hero/index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/Hero/index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'Hero/regform.html', context)


