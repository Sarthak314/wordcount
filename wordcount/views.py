from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordcount = fulltext.split()
    worddick={}
    for word in wordcount:
        if word in worddick:
            worddick[word]+=1
        else:
            worddick[word]=1;
    for word in wordcount:
        print(word)
    return render(request,'count.html',{'fulltext':fulltext,'wordcount':len(wordcount),'worddick':worddick})

def about(request):
    return render(request,'about.html')
