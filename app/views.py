from django.shortcuts import render, redirect

# Create your views here.

def test(request):
    return redirect('https://www.canva.com/design/DAFxgfD3J00/RBriToZ9Pe725_FbxXIzwg/view?utm_content=DAFxgfD3J00&utm_campaign=designshare&utm_medium=link&utm_source=editor')
    #return render(request, 'mysite.html')

def madik(request):
    return render(request, 'osnova.html')

def pres(request):
    return render(request, '2.html')

def erd(request):
    context = {
            "bruh": "This is django context",
    }
    return render(request, 'erd.html', context=context)

