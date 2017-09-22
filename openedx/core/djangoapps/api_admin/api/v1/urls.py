"""
API v1 URLs.
"""

from rest_framework.routers import DefaultRouter

from openedx.core.djangoapps.api_admin.api.v1 import views

router = DefaultRouter()
router.register("api_access_request", views.ApiAccessRequestView, base_name='api_access_request')
