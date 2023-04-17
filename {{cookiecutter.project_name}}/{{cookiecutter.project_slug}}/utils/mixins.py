from typing import Sequence, Type, TYPE_CHECKING

from importlib import import_module

from django.conf import settings

from django.contrib import auth

from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import BaseAuthentication


def get_auth_header(headers):
    value = headers.get('Authorization')

    if not value:
        return None

    auth_type, auth_value = value.split()[:2]

    return auth_type, auth_value

