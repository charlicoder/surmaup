from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base.html"), name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += i18n_patterns(
#     url(r’^{}/’.format(settings.DJANGO_ADMIN_URL), admin.site.urls),
# )