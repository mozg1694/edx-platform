"""
URL definitions for api access request API endpoint.
"""
from django.conf.urls import include, url

from openedx.core.djangoapps.api_admin.api.v1.urls import router as api_v1_router
from openedx.core.djangoapps.api_admin.api.v1.views import ApiAccessRequestView

urlpatterns = [
    url(r'^v1/', include(api_v1_router.urls, namespace='v1')),
    url(r'^test/', ApiAccessRequestView.as_view({'get': 'list'})),
]
