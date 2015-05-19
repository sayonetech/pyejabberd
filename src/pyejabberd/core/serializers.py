# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .definitions import APIArgumentSerializer


class StringSerializer(APIArgumentSerializer):
    def to_api(self, python_value):
        return python_value

    def to_python(self, api_value):
        return api_value


class IntegerSerializer(APIArgumentSerializer):
    def to_api(self, python_value):
        assert isinstance(python_value, (int, long))
        return str(python_value)

    def to_python(self, api_value):
        return int(api_value)


class PositiveIntegerSerializer(IntegerSerializer):
    def to_api(self, python_value):
        assert isinstance(python_value, (int, long))
        assert python_value >= 0
        return super(PositiveIntegerSerializer, self).to_api(python_value)


class BooleanSerializer(APIArgumentSerializer):
    def to_api(self, python_value):
        assert isinstance(python_value, bool)
        return 'true' if python_value else 'false'

    def to_python(self, api_value):
        return api_value == 'true'
