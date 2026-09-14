from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .google_sheet import save_contact_to_sheet


@csrf_exempt
def contact_api(request):
    if request.method != "POST":
        return JsonResponse(
            {
                "success": False,
                "message": "Only POST method is allowed."
            },
            status=405
        )

    try:
        data = json.loads(request.body)

        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        phone = data.get("phone", "").strip()
        service = data.get("service", "").strip()
        details = data.get("details", "").strip()

        if not name or not email:
            return JsonResponse(
                {
                    "success": False,
                    "message": "Name and email are required."
                },
                status=400
            )

        save_contact_to_sheet(
            name=name,
            email=email,
            phone=phone,
            service=service,
            details=details
        )

        return JsonResponse(
            {
                "success": True,
                "message": "Message submitted successfully."
            }
        )

    except Exception as e:
        print("Google Sheet Error:", e)

        return JsonResponse(
            {
                "success": False,
                "message": "Something went wrong. Please try again."
            },
            status=500
        )



        
def health_check(request):
    return JsonResponse({
        "status": "ok"
    })
