from django.urls import path, include
from views import contact_view

urlpatterns = [
    path("contact/", contact_view, name="contact"),
    path("captcha/", include("captcha.urls"))
]
