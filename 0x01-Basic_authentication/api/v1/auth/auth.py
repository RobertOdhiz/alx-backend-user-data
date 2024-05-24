#!/usr/bin/env python3
""" Auth class Module """
from flask import request
from typing import List, TypeVar
import fnmatch


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ returns None """
        return None
