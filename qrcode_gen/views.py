from django.shortcuts import render
from django.views.generic import ListView
from qrcode_gen.models import Qr_Code
# Create your views here.

class Qr_CodeList(ListView):
    model = Qr_Code
    obj=Qr_Code.objects.get(id=1)
    template_name='home.html'
    