from django.contrib import admin
from django.urls import path, include
from .views import HomeView

urlpatterns = [
    ## /admin/ default
    path('admin/', admin.site.urls),

    ## Hace referencia a Homeview donde retorna un "return render(request, 'index.html', context)"
    path('', HomeView.as_view(), name='home'),

    ## Hace referencia a /blog/urls.py
    path('blog/', include('blog.urls', namespace='blog'))
]

