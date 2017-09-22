"""
API Views.
"""

from edx_rest_framework_extensions.authentication import JwtAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework_oauth.authentication import OAuth2Authentication

from openedx.core.djangoapps.api_admin.api.v1 import serializers as api_access_serializers
from openedx.core.djangoapps.api_admin.models import ApiAccessRequest


class ApiAccessRequestView(viewsets.ViewSet):
    """
    List Api Access Requests.
    """
    authentication_classes = (JwtAuthentication, OAuth2Authentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = api_access_serializers.ApiAccessRequestSerializer

    queryset = ApiAccessRequest.objects.all()
