from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('secret/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),


    path('api/v1/auth/', include('djoser.urls.jwt')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    header= show on logging screen
    title = 
    index_title = 
    """
admin.site.site_header = "Real Estate Admin"
admin.site.site_title = "Real Estate Admin Portal"
admin.site.index_title = "Welcome to the Real Estate Portal"
