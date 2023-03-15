from django.shortcuts import render

# Create your views here.

def compare(request):
    number1 = request.POST.get('number1')
    number2 = request.POST.get('number2')
    res = []
    number1 = number1.split(' ')
    number2 = number2.split(' ')
    for i in range(len(number1)):
        if int(number1[i]) > int(number2[i]):
            res.append(number1[i])
        else:
            res.append(number2[i])

    return render(request, 'main/compare.html',context={'res':res})