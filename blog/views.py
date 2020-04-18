from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
# Create your views here.
def index(request):

	if request.method == 'POST':
		print(request.POST)
		User.objects.create(
				nama_depan = request.POST.get('nama_depan'),
				nama_belakang = request.POST.get('nama_belakang'),
				alamat = request.POST.get('alamat')

			)
		return HttpResponseRedirect(reverse('blog:index'))
	context = {
			'pengguna' : User.objects.all(),
	}

	return render(request,'blog/index.html', context)

def hapus(request,input):
	print(User.objects.get(pk=input).delete())

	return HttpResponseRedirect(reverse('blog:index'))

def edit(request,input):
	user =  User.objects.get(pk=input)
	if request.method == 'POST':
		print(request.POST)
		user.nama_depan = request.POST.get('nama_depan')
		user.nama_belakang = request.POST.get('nama_belakang')
		user.alamat = request.POST.get('alamat')
		user.save()

		return HttpResponseRedirect(reverse('blog:index'))

	context = {
		'edit': user
	}	
	print(context)
	return render(request, 'blog/edit.html', context)
