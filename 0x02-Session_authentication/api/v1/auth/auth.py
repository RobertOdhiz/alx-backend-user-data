#!/usr/bin/env python3
""" Auth class Module """
from flask import request
from typing import List, TypeVar
import fnmatch
from os import getenv


class Auth():
    """ Authentication Class representation """
    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]) -> bool:
        """ checks if auth is required """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            if fnmatch.fnmatch(path, excluded_path):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ returns None """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None """
        return None

    def session_cookie(self, request=None):
        """ Returns a cookie value from request """
        if request is None:
            return None
        SESSION_NAME = getenv("SESSION_NAME")

        if SESSION_NAME is None:
            return None

        session_id = request.cookies.get(SESSION_NAME)

        return session_id
