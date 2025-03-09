def serialize_request(request):
    """Convierte el request en un diccionario serializable para Celery, incluyendo solo encabezados HTTP_"""
    return {
        "user": request.user.username if request.user.is_authenticated else "AnonymousUser",
        "get": request.GET.dict(),
        "post": request.POST.dict(),
        "files": {k: v.name for k, v in request.FILES.items()},
        "cookies": request.COOKIES,
        "meta": {k: v for k, v in request.META.items() if k.startswith("HTTP_")},  # Solo encabezados HTTP_
    }
