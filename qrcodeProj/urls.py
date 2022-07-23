from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from qrcode_gen import views
# from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('qrcode_gen.urls')),
    # path("", TemplateView.as_view(template_name="home.html"), name="home"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
