from drf_spectacular.utils import (
    extend_schema,
    OpenApiResponse,
)

from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import AllowAny

from django.http import HttpResponse, HttpRequest

from ..core import refresh_token_validation_core, sign_in_core, sign_up_core
from ..serializers import (
    UserRegistrationRequestSerializer,
)
from ..services import (
    get_tokens_for_user, 
    get_token_http_reponse,
)


# =============================================POST=============================================


@extend_schema(
    summary="WORKS: Sign-up by email and password",
    description="Take email and password, create user and return 'access' and 'refresh' tokens in cookies",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        201: OpenApiResponse(description="Successfully registrated."),
        400: OpenApiResponse(description="Error: Bad request"),
        404: OpenApiResponse(description="Error: Not found"),
        422: OpenApiResponse(description="Error: Unprocessable entity"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "users",
    ],
)
@api_view(["POST"])
def sign_up(request: HttpRequest) -> HttpResponse:
    sign_up_core(request=request)
    return HttpResponse(status=201)

@extend_schema(
    description="WORKS: Take user's email and password and return 'access' and 'refresh' tokens",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully registrated."),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "users",
    ],
)
@api_view(['POST'])
def sign_in(request: HttpRequest) -> HttpResponse:
    user = sign_in_core(request=request)
    return get_tokens_for_user(user)


@extend_schema(
    description="WORKS: Take user's email and password and return 'access' and 'refresh' tokens in cookies",
    request=UserRegistrationRequestSerializer,
    methods=["POST"],
    responses={
        200: OpenApiResponse(description="Successfully registrated."),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "users",
    ],
)
@api_view(['POST'])
def sign_in_cookies(request: HttpRequest) -> HttpResponse:
    user = sign_in_core(request=request)
    return get_token_http_reponse(user)


@extend_schema(
    summary="WORKS: Refresh access token",
    description="Take user's 'refresh' token from cookies, update 'access' token",
    methods=["POST"],
    request=None,
    responses={
        200: OpenApiResponse(description="Successfully refreshed token."),
        401: OpenApiResponse(description="Error: Unauthorized"),
        500: OpenApiResponse(description="Error: Internal server error"),
    },
    tags=[
        "users",
    ],
)
@api_view(["POST"])
def refresh_token_cookies(request: HttpRequest) -> HttpResponse:
    validated_data = refresh_token_validation_core(request=request)
    return get_token_http_reponse(
        user=request.user, refresh_token=validated_data.data["refresh"]
    )
    