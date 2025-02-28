from django.http import HttpResponse
from django.shortcuts import render 


def analyze(request):
    if request.method == "GET":

        text = request.GET.get("textname")
        removepunc =request.GET.get("removepunc","off")
        capital=request.GET.get("capital","off")
        lowercase=request.GET.get("lower",'off')
        print(text,removepunc)
        lst=[]
        count=0
        lst.append(removepunc)
        lst.append(capital)
        lst.append(lowercase)

        for req in lst:
            if req=="on":
                count+=1

        if count == 1:

            analyzed=''

            if removepunc == 'on':
                punctuation="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
                for i in text:
                    if i in punctuation:
                        continue
                    analyzed += i   
            elif capital == "on":
                analyzed = text.upper()                  
            elif lowercase == "on":
                analyzed = text.lower()         
            else:
                return HttpResponse("error")

            print(analyzed)  
            data={
                'text':analyzed       
                    }

            return render(request,'analyze.html',data)
        else:
            return HttpResponse( "<a href=http://127.0.0.1:8000>ERROR select any one option Return to homepage</a>  ")
         

def index(request):
    data1="helllo"
    data2='dfsfssffsfsfsdf'
    data={
        "data1":data1,
        "data2":data2
    }
    return render(request,'index.html',data)

def about(request):
    return render(request,"about.html")

def contact(request):
    return HttpResponse("<a href='https://www.instagram.com/shibinrsilva/'> welcome to my instagram for my contact </a>")