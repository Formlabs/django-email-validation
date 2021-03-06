from django.urls import path, include

from django_email_verification import urls, verify_view

urlpatterns = [
    path('email/', include(urls)),
    path('confirm/', verify_view(lambda request: None)),
]
