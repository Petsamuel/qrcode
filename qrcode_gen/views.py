from django.shortcuts import render
from django.views.generic import ListView
from qrcode_gen.models import Qr_Code
# Create your views here.

# class Qr_CodeList(ListView):
#     model = Qr_Code
#     obj=Qr_Code.objects.get(id=1)
#     template_name='index.html'
    
def index(request):
    if request.method == "POST":
        text_link = request.POST['qr_code_text']
        Qr_Code.objects.create(Qr_Name=text_link)

    qr_code=Qr_Code.objects.all()
    return render(request, 'index.html', {'qr_code':qr_code})
        