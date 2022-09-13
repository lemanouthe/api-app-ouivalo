from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


def contact(request):

    return render(request, "contact.html", locals())


@csrf_exempt
def postcontact(request):
    success = False
    message = ""
    if request.method == "POST":
        email = request.POST.get("email")
        date = request.POST.get("date")
        urlRelais = request.POST.get("urlRelais")
        message = request.POST.get("message")

        print(email, date, urlRelais, message)
        base_url = "https://script.google.com/macros/s/AKfycby-TJmFFUFTfiNUbMoSIZx8LVtiskQ-bUt4xO6hmrU0XQpJS8IPUBow/exec"

        data = {
            "cle": "CLE-TEST-IOT",
        }

        info = {
            "id": email,
            "date": date,
            "urlRelais": urlRelais,
            "message": message,
        }

        data["donnees"] = info
        reponse = requests.post(base_url, json=data)
        print(reponse.text)
        print(reponse.status_code)
        success, message = True, "Message envoyé avec succès !!!"
    else:
        success = False
        message = "Erreur de Requête"

    data = {
        "status": success,
        "message": message,
    }
    return JsonResponse(data, safe=False)
