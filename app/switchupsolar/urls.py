"""Url mappings for the user API."""

from django.urls import path, re_path
from app.swagger import schema_view
from switchupsolar import views


app_name = "switchupsolar"

urlpatterns = [
    path("send", views.send, name="send"),
    path("webhook", views.webhook, name="webhook"),
    path("send-message", views.send_message_api, name="send_message"),
    path("webhook", views.webhook),
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
