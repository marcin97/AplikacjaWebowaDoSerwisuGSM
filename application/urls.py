from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from main import views

urlpatterns = [
    path('<int:id>/generatePDF/', views.generatePDF, name='generatePDF'),
    path('<int:id>/sendMail/', views.sendMail, name='sendMail'),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]
