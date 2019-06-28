from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import models
#from django.db import models

# Create your views here.

'''第一次迭代，数据可视化
   6.25
'''

#2017-2019生产总值
def total(request):
    total = models.Gdp.objects.get(gdp_id=1).gdp_mount
    return JsonResponse({"total": total})

#2017-2019每月总产量
def per_month():
    x = models.Gdp.objests.all().count()-1
    a = []
    for i in range(0, x):
        a[i] = {models.Gdp.objects.get(gdp_id=(i+2)).gdp_date: models.Gdp.objects.get(gdp_id=(i+2)).gdp_mount}
    return JsonResponse({"per_month": a})

#每个省2017-2019总产量
def total_per_province():
    x = 10
    a = []
    for i in range(0, x):
        a[i] = {"province": 0}
    return JsonResponse({"total_per_province": a})

#2017/2018各类别农产品生产总值
def total_per_product__per_year():
    x = 10
    a = [], b = []
    for i in range(0, x):
        a[i] = {"2017_type_of_farm_goods": 0}
    for i in range(0, x):
        b[i] = {"2018_type_of_farm_goods": 0}
    return JsonResponse({"2017": a,
                         "2018": b})

#天气
def weather(request):
    temperature  = 0
    weather_type = 0
    return JsonResponse({"temperature": temperature,
                         "weather_type": weather_type})

#各地区消费能力
def consume_ability():
    value = 0
    return JsonResponse({"consume_ability": value})

#每类产品销售总额
def sale_sum_per_product():
    x = 10
    a = []
    for i in range(0, x):
        a[i] = {"type_of_the_farm_goods": 0}
    return JsonResponse({"sale_sum_per_product": a})

#按时间消费额
def sale_sum_per_day(request):
    x = 10
    a = []
    for i in range(0, x):
        a[i] = {"day": 0}
    return JsonResponse({"sale_sum_per_day": a})

def sale_sum_per_month(request):
    x = 10
    a = []
    for i in range(0, x):
        a[i] = {"month": 0}
    return JsonResponse({"sale_sum_per_month": a})


'''后续迭代'''

#登录
def login(request):
    user_name = request.POST.get("user_name")
    pass_word = request.POST.get("pass_word")
    return JsonResponse({"status": "status",
                         "message": "login success",
                         "usertype": "usertype"})

#注册
def register(request):
    user_name = request.POST.get("user_name")
    pass_word = request.POST.get("pass_word")
    user_type = request.POST.get("user_type")
    return JsonResponse({"status": "status",
                         "message": "register success"})

#价格预测
def pricepredict(request):
    province = request.POST.get("province")
    name     = request.POST.get("name")
    past_price   = 0
    future_price = 0
    return JsonResponse({"past_price": past_price,
                         "future_price": future_price})

#产量预测
def productpredict(request):
    province = request.POST.get("province")
    name     = request.POST.get("name")
    product = 0
    return JsonResponse({"product": product})



