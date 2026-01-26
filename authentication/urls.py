# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('authentication/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # O token terá validade de 5 minutos
    path('authentication/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # o refresh tem validade de 24 horas e serve para ficar renovando o token
    path('authentication/token/verify/', TokenVerifyView.as_view(), name='token_verify')      # Faz uma verificação se o token de acesso está válido. no postman mande um post com "token":"code_token"
]
