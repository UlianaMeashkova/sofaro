from django.shortcuts import render

# Create your views here.

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info(request.GET, request.POST)
    return HttpResponse("Sofaro index view")