from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from SummerTrainning import settings
from django.db.models import F,Q
from FarmProduct import models
from django.views.decorators.cache import never_cache
import math
import os
import time
import datetime
import string,random
# Create your views here.

@never_cache
def login(request):
    pass


@never_cache
def register(request):
    pass