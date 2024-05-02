from django.shortcuts import render

def download_list(request):
    context = {}
    return render(request, "list_download.html", context)