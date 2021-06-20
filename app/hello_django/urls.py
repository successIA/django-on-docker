from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload, visitor_ip_address

urlpatterns = [
    path("", image_upload, name="upload"),
    path('visitor_ip_address/', visitor_ip_address),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
