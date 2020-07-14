

# Views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'MyApp/index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    removepuncfullcaps =  request.POST.get('removepuncfullcaps', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'MyApp/analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = " "
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capital Letters', 'analyzed_text': analyzed}
        return render(request, 'MyApp/analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = " "
        for char in djtext:
            if "/n" not in char and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        return render(request, 'MyApp/analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = " "
        for index, char in enumerate(djtext):
            if  not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'extraspaceremover', 'analyzed_text': analyzed}
        return render(request, 'MyApp/analyze.html', params)



    elif (removepuncfullcaps=="on" ):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~='''
        analyzed = ""
        analyzed1 = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char.upper()

        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'MyApp/analyze.html', params)

    else:
        return HttpResponse(djtext)

def about(request):
    return render(request, 'MyApp/about.html')
def contact(request):
    return render(request, 'MyApp/contact.html')


