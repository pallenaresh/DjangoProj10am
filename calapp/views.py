from django.shortcuts import render
from django .http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'input.html')
def calculate(request):
    try:
        x=request.GET['t1']
        y=request.GET['t2']
        i=int(x)
        j=int(y)
        op=request.GET['operation']
    except(ValueError):
        return render(request,'input.html')
    if op=='add':
        z=i+j
        return HttpResponse("""<html><body bgcolor=red><h1>sumis:"""+str(z)+"""</h1></body></html>""")
    elif op=='sub':
        z=i-j
        return HttpResponse("""<html><body bgcolor=green><h1>subis:""" + str(z) + """</h1></body></html>""")
    elif op=='mul':
        z=i*j
        return HttpResponse("""<html><body bgcolor=yellow><h1>mulis:""" + str(z) + """</h1></body></html>""")
    elif op=='div':
        try:
            z=i/j
            return HttpResponse("""<html><body bgcolor=blue><h1>divis:""" + str(z) + """</h1></body></html>""")
        except(ZeroDivisionError):
            return HttpResponse('zero cant divd by num')

















