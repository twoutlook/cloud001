from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^flowchart/', include('flowchart.urls')),
    url(r'^polls/', include('polls.urls')),
   
    url(r'^projectnote/', include('projectnote.urls')),
    url(r'^app001/', include('app001.urls')),
    #
    url(r'^admin/', admin.site.urls),
    url(r'', include('portal.urls')),

]
