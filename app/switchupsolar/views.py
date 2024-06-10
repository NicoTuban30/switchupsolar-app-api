from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from requests.structures import CaseInsensitiveDict
import json
import requests
from .serializers import SendMessageSerializer, WebhookSerializer


BOT_ID = "8c44cf8a3d72faa3e74fe2fb28"


def index(request):
    """
    This function handles the root route and returns a simple "Hello World!" message.
    """
    return HttpResponse("Hello World! -- from index()")


@api_view(["POST"])
def send(request):
    """
    This function handles the '/send' route and returns a simple "Hello World!" message.
    """
    return HttpResponse("Hello World! -- from send()")


@swagger_auto_schema(
    method="post",
    request_body=SendMessageSerializer,
    responses={200: openapi.Response("Message sent successfully")},
    operation_description="Send a message through the GroupMe API",
    request_body_examples={
        "application/json": {"msg": "Hello, World!", "num": "+1234567890"}
    },
)
@api_view(["POST"])
def send_message_api(request):
    """
    This view handles sending a message through the GroupMe API.
    """
    serializer = SendMessageSerializer(data=request.data)
    if serializer.is_valid():
        msg = serializer.validated_data["msg"]
        num = serializer.validated_data["num"]
        send_message(msg, num)
        return JsonResponse({"status": "Message sent successfully"})
    else:
        return JsonResponse(serializer.errors, status=400)


@swagger_auto_schema(
    method="post",
    request_body=WebhookSerializer,
    responses={200: openapi.Response("Webhook received successfully")},
    operation_description="Handle webhook from GroupMe API",
)
@api_view(["POST"])
def webhook(request):
    """
    This function handles the '/webhook' route and processes incoming webhook requests.
    It extracts the message and phone number from the request and calls the 'send_message' function.
    """
    serializer = WebhookSerializer(data=request.data)
    if serializer.is_valid():
        msg = serializer.validated_data["Body"].lower()
        phone_num = serializer.validated_data["From"]
        send_message(msg, phone_num)
        return HttpResponse(status=200)
    else:
        return JsonResponse(serializer.errors, status=400)


def send_message(msg, num):
    """
    This function sends a message to the GroupMe API using the provided message and phone number.
    It constructs the API request payload and sends a POST request to the API endpoint.
    """
    url = "https://api.groupme.com/v3/bots/post"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data_dict = {"bot_id": BOT_ID, "text": f"Number: {num} Message: {msg}"}

    data = json.dumps(data_dict)
    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)
