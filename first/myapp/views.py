from django.shortcuts import render

def index(request):
    """/トップページ"""
    context = {
        'name': 'sangorou',
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    """アバウトページ"""
    return render(request, 'myapp/about.html')

def info(request):
    """インフォページ"""
    return render(request, 'myapp/info.html')