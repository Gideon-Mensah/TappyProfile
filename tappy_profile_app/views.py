from django.shortcuts import render
import qrcode

# Create your views here.
def profile_view(request):
    return render(request, 'index.html')

