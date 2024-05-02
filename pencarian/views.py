from django.shortcuts import render

def show_search_bar(request):
    context = {}
    return render(request, "search_bar.html", context)

def show_search(request):
    context = {}
    return render(request, "search.html", context)