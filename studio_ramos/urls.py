from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('usuario.urls')),
    path('agendamento/', include('agendamento.urls')),
    path('captcha/', include('captcha.urls')),
    path('', include('app_site.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app_site.views.not_found'