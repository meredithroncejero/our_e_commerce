from django.contrib import admin
from django.urls import path, include  # include is important

urlpatterns = [
    path('admin/', admin.site.urls),           # Django default admin
    path('admin-panel/', include('admin_panel.urls')),  # Your custom admin
]
