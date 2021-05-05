#this is created by me
from django.http import HttpResponse#to send response for request
from django.shortcuts import render #for using templates



def index(request):
    # return HttpResponse(" Home ")
    params = {'name':'bobby','place':'mars'}
    return render(request , 'index.htm',params)
# def contacts(request):
#     return render(request , 'contacts.htm')

# def services(request): 
#     return render(request , 'services.htm')   

def analyze(request): 
    requested_text = request.POST.get("text" , "default")
    removepunc = request.POST.get("removepunc" , "off")
    capitalizer = request.POST.get("capitalizer" ,"off")
    inlineremover = request.POST.get("inlineremover" ,"off") 
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in requested_text:
            if char not in punctuations:
                analyzed+=char
        params = {"Purpose":"Removing Punctuations" ,"analyzed_text":analyzed }
        return render(request ,"analyze.htm" ,params)
    elif capitalizer == "on":
        uppercase = ""
        for char in requested_text:
            uppercase += char.upper()
        params = {"purpose":"capitalize text" , "analyzed_text":uppercase}
        return render(request,"analyze.htm",params)
        

    elif inlineremover == "on":
        result = ""
        for char in requested_text:
            if char != "\n" and char!="\r":
                result = result + char
        params = {"purpose":"capitalize text" , "analyzed_text":result}
        return render(request,"analyze.htm",params)
    else:
        return HttpResponse("Error plz select option")
def capitalizer(request):
    return HttpResponse('capitalizer')
def inlineremover(request):
    return HttpResponse('removing inline element')
