from django.shortcuts import render , redirect
from django.http import  HttpResponse
from .forms import * 
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 

# Create your views here.

def index(request):
	return render(request , 'index.html')






class add_newCreateView(CreateView):
	model = TodoIem
	fields = ['text']
	template_name = 'new_todo.html'
	success_url = '/all/'


	 
class todolistview(ListView):
	model = TodoIem
	paginate_by = 3
	template_name = 'all_todo.html'
	def get_queryset(self):
		return TodoIem.objects.all().order_by('-id')


class todoDetailView(DetailView):
	model = TodoIem
	template_name = 'todo_detail.html'


class todoUpdateView(UpdateView):
    model = TodoIem
    fields = ['text']
    template_name = 'update_todo.html'
    success_url = '/all/'
    

	
class todoDeleteView(DeleteView):
    model = TodoIem
    fields = ['text']
    template_name = 'delete_view.html'
    success_url = '/all/'









