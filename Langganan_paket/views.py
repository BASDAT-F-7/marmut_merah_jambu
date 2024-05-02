from django.shortcuts import render

def show_list_paket(request):
    context = {}
    return render(request, "langganan.html", context)

def show_pembayaran(request):
    context = {}
    return render(request, "pembayaran.html", context)

def show_riwayat(request):
    context = {}
    return render(request, "Riwayat.html", context)