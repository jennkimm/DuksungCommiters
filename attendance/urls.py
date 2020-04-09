from django.conf.urls import url, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'attendance'

urlpatterns = [
    url(r'^$', views.Attendance.as_view(), name='attendance'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)