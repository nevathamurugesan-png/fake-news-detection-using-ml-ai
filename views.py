from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from .models import predict


def read_file(file_name):
    opened_file = open(file_name, 'r')
    lines_list = []
    for line in opened_file:
        line = line.split()
        lines_list.append(line)
    #print(lines_list)
    return lines_list



# Create your views here.
# Create your views here.  
def home(request):
	return render(request,'index.html')


def input(request):
    return render(request,'input.html')
       

class_names = ['False', 'Barelu true', 'Mostly-true', 'Half-true', 'Pants-Fire', 'True']



def output(request):
	text = str(request.POST.get('text'))
	algo=request.POST.get('algo')
	out=predict(text,algo)
	print(out)
    #SSclasses = class_names[out]
	print(class_names[out])
	return render(request,'output.html',{'out':class_names[out]})