from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from accounts.views import AccountLoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AccountLoginView.as_view()),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('', include(('projects.urls', 'projects'), namespace='projects')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
