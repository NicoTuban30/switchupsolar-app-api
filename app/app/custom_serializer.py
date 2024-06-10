from rest_framework import serializers

from drf_spectacular.openapi import AutoSchema


class CustomNullBooleanField(serializers.BooleanField):
    def to_representation(self, value):
        if value is None:
            return None
        return super().to_representation(value)

    def to_internal_value(self, data):
        if data in [None, "null", "None"]:
            return None
        return super().to_internal_value(data)


class CustomAutoSchema(AutoSchema):
    def _map_serializer_field(self, field, direction):
        if isinstance(field, CustomNullBooleanField):
            # Custom handling for CustomNullBooleanField
            # You might need to adapt this based on your requirements
            return {"type": "boolean", "x-nullable": True}

        # Call the original method for all other fields
        return super()._map_serializer_field(field, direction)
