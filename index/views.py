#_*_ coding:utf-8 _*_

from django.shortcuts import render,redirect
from index.models import Product
from django.views.generic import ListView

# Create your views here.
from django.http import HttpResponse
import csv

def myyear(request,year,month):
    return render(request,'myyear.html',{'month':month})

def download(reques):
    response = HttpResponse(content_type='text/csv')
    response['Content-Dispostion'] = 'attachment;filename="ljy.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row','a','b'])
    return response

def index(request):
    type_list = Product.objects.values('type').distinct()
    name_list = Product.objects.values('name','type')
    title = '首页'
    return render(request,'show.html',context=locals(),status=200)

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return redirect('/')
    else:
         if request.GET.get('name'):
            name = request.GET.get('name')
         else:
            name = 'everyone'
         return HttpResponse('user is {0}'.format(name))

class ProductList(ListView):
    context_object_name = ['type_list','name_list']
    template_name = 'show.html'
    queryset = Product.objects.values('type').distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name','type')
        return context

def test(request):
    title = "首页"
    type_list = [{'name':'小明'},{'name':'小才'},{'name':'年'}]
    return render(request,'text.html',context=locals())