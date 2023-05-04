import plexgis
import plexmap_viewer.views
from django.conf.urls import include, url
from plexgis.urls import default_plexmap_urls
from plexmap_viewer.views import PlexMapHostnameView

urlpatterns = [
    url(r'^$', PlexMapHostnameView.as_view(views={
        'plexmap.gis.mycsn.be': 'MyCSN',
    })),
] + default_plexmap_urls()
