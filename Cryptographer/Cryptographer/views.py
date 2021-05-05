from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request , 'index.htm')

def convert(request):
    requested_text = request.POST.get("text" , "off")
    is_base64 = request.POST.get("base64" ,"off")
    is_binary = request.POST.get("binary" ,"off")
    is_reverse = request.POST.get("reverse" ,"off")
    is_ascii = request.POST.get("ascii" ,"off")
    result = ""

    if is_reverse == "on":
        result = requested_text[: : -1]


    params={"result_text":result}
    return render(request , "result.htm" ,params)

