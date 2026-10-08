from django.http import HttpResponse
from django.utils import timezone


def home(request):
    """
    Задача 3: Простое Django-приложение с приветственной страницей.
    Возвращает HTML-ответ с текстом "Привет из Django!" и текущим временем.
    """
    now = timezone.now().strftime("%d.%m.%Y %H:%M:%S")
    html = (
        "<!DOCTYPE html>"
        "<html lang='ru'>"
        "<head><meta charset='utf-8'><title>Привет из Django</title></head>"
        "<body style='font-family:Arial,sans-serif;text-align:center;margin-top:80px;'>"
        "<h1>Привет из Django! 👋</h1>"
        f"<p>Это страница из приложения <strong>demoapp</strong>.</p>"
        f"<p>Текущее время на сервере: <strong>{now}</strong></p>"
        "<p style='color:#666;'>Задача 3 выполнена успешно.</p>"
        "</body></html>"
    )
    return HttpResponse(html)
