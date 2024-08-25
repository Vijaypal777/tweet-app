from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tweet import views  # Import the views from the 'tweet' app
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Handles the root URL with the 'index' view
    path('tweet/', include('tweet.urls')),  # Routes to the 'tweet' app
    path('accounts/', include('django.contrib.auth.urls')),  # Routes to the 'tweet' app
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
