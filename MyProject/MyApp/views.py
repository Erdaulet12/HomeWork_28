from django.shortcuts import render, redirect
from django.http import JsonResponse
from forms import CustomForm
from models import Contact
# Create your views here.


def contact_view(request):
    if request.method == "POST":
        form = CustomForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["message"]
            )
            return JsonResponse({"status": "success", "message": "Сообщение отправлено!"})
        else:
            return JsonResponse({"status": "error", "errors": form.errors})

    form = CustomForm()
    return render(request, "contact.html", {"form": form})
