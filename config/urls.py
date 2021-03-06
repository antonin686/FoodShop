from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

admin.site.site_header = "FoodShop Admin"
admin.site.index_title = "Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)