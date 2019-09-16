from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'homepage.html')
def count(request):
    Fulltext=request.GET['fulltext']
    wordlist=Fulltext.split();
    wordcountdict={}
    for word in wordlist:
        if word in wordcountdict:
            #increase
            wordcountdict[word]+=1
        else:
            wordcountdict[word]=1
        sort=sorted(wordcountdict.items(),key=operator.itemgetter(1),reverse=True)
        
    return render(request,'count.html',{'fulltext':Fulltext,'count':len(wordlist),'wordcountdict':sort})
def about(request):
    return render(request,'about.html')