from cgitb import text
from django.shortcuts import render

def homepage(request):
    try:
        text=request.GET.get('textarea')
        start=int(request.GET.get('start'))
        end=int(request.GET.get('end'))
        
        if start<0:
            return render(request, 'home.html', {'message': "Please enter a positie value for the indexes.",'text': text, 'start': start, 'end': end})
        elif end<0:
            return render(request, 'home.html', {'message': "Please enter a positie value for the indexes.",'text': text, 'start': start, 'end': end})
        elif start>end:
            return render(request, 'home.html', {'message': "Please enter the start index value smaller than the end index value.",'text': text, 'start': start, 'end': end})
        elif end>=len(text):
            return render(request, 'home.html', {'message': "Please enter the end index value smaller than the number of characters in the string.",'text': text, 'start': start, 'end': end})
        return render(request, 'home.html',{'text': text, 'start': start, 'end': end})
    except:
        return render(request, 'home.html',{'text': text})

def home(request):
    return render(request, 'home.html')