# i have created this man! This is month of ramadan!

from django.http import HttpResponse
from django.shortcuts import render

#vdo 6
# def index(request):
#     return HttpResponse('''<h1> Hellow Man! </h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7 ">click here</a> ''')
#
#
# def about(request):
#     return HttpResponse("<h1>Yeah thats a new page or youu may call it as url!</h1> ")


def index(request):
    params={'name':'salman','age':'infinite'}
    return render(request,'index.html',params)


# def removepunc(request):
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     return HttpResponse("remove punc")
#

# def capitalize(request):
#     return HttpResponse("capitalize")
#
# def newlineremove(request):
#     return HttpResponse("newline remover")
# def spaceremove(request):
#     return HttpResponse("space remover  <a href= '/'> GO Back  </a>")
#
# def charcount(request):
#           return HttpResponse("char counter")


def analyze(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Punctuations Free Text:', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
