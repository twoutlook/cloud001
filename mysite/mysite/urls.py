from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^app001/', include('app001.urls')),
    #
    url(r'^admin/', admin.site.urls),
    url(r'', include('portal.urls')),
    
]
