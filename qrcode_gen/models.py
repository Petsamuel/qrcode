from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode

class Qr_Code(models.Model):
    Qr_Name = models.CharField(("Name"), max_length=200)
    Qr_Image = models.ImageField(("Code"), upload_to='qrMedia', blank = True)

    def __str__(self):
        return self.Qr_Name

    def save(self, *args, **kwargs):
        Qr_Code_img= qrcode.make(self.Qr_Name)
        canvas = Image.new('RGB',(290,290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(Qr_Code_img)
        fname= f'Qr_Code-{self.Qr_Name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.Qr_Image.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)
