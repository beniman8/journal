from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """The entry point for the website."""
    context = {}
    template_name = "maincore/index_unauthenticated.html"
    if request.user.is_authenticated:
        template_name = "maincore/index.html"
    return render(request, template_name, context)
