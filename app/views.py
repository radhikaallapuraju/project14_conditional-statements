from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':30,'b':40,'c':50,'d':45}
    return render(request,'conditional.html',d)
