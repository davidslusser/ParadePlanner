from .gui import urlpatterns as gui_urls
from .rest import urlpatterns as rest_urls

app_name = "parademgr"

urlpatterns = rest_urls + gui_urls
