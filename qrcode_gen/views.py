from django.shortcuts import render
from django.views.generic import ListView
from qrcode_gen.models import Qr_Code
import qrcode
import qrcode.image.svg
from io import BytesIO
# Create your views here.

class Qr_CodeList(ListView):
    model = Qr_Code
    obj=Qr_Code.objects.get(id=1)
    template_name='index.html'
    
def index(request):
    context = {}
    if request.method == "POST":
        holder = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get('qr_code_text', ''), image_factory=holder, box_size=20)
        img_io = BytesIO()
        img.save(img_io)
        context['svg'] = img_io.getvalue().decode()
    return render(request, 'index.html', context)