from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from . import models
#from django.db import models

# Create your views here.

#测试
def test(request):
    return HttpResponse("OK!")

def yield1(request):
    yield1 = models.Yield.objects.get(yie_id=1).yie_yield
    return JsonResponse({"yield1": yield1})

#注册
def register(request):
    username    = request.POST.get("user_name")
    userpwd     = request.POST.get("user_pwd")
    usertype    = request.POST.get("user_type")                       #三种类型用数字表示，1为用户，2为商家，3为政府
    useraddress = request.POST.get("user_address")
    if models.User.objects.filter(user_name=username).exists():       #如果用户已经存在，再进行注册时会出错
        return JsonResponse({"status": False,
                             "message": "user already exists"})
    else:
        models.User.objects.create(user_name=username, user_pwd=userpwd, user_type=usertype, user_address=useraddress)
        return JsonResponse({"status": True,
                             "message": "registration success"})
#登录
def login(request):
    username = request.POST.get("user_name")
    userpwd = request.POST.get("user_pwd")
    if models.User.objects.filter(user_name=username).filter(user_pwd=userpwd).exists():
        return JsonResponse({"status": True,
                             "message": "login success"})
    else:
        if models.User.objects.filter(user_name=username).exists():
            return JsonResponse({"status": False,
                                 "message": "password not correct"})
        else:
            return JsonResponse({"status": False,
                                 "message": "username not exists, register first please"})

#按产品类别浏览表
def browse_by_protype(request):
    protype = request.POST.get("pro_type")
    print(protype)
    proset = models.Products.objects.filter(pro_type=protype).filter(pro_state=1)
    x = proset.count()
    a = [0]*x
    for i in range(0, x):
        temp = [0, 1, 2, 3, 4, 5]
        temp[0] = proset[i].pro_id
        temp[1] = proset[i].pro_name
        temp[2] = proset[i].pro_price
        temp[3] = proset[i].pro_origin
        temp[4] = proset[i].pro_store.user_name
        temp[5] = proset[i].pro_img
        a[i] = temp
    return JsonResponse({"status": True,
                         "products": a})


#查找
def search(request):
    keyword = request.POST.get("key_word")
    proset = models.Products.objects.filter(pro_name__contains=keyword).filter(pro_state=1)
    x = proset.count()
    if x == 0:
        return JsonResponse({"status": False,
                             "message": "nothing found"})
    else:
        a = [0]*x
        for i in range(0, x):
            temp = [0, 1, 2, 3, 4, 5]
            temp[0] = proset[i].pro_id
            temp[1] = proset[i].pro_name
            temp[2] = proset[i].pro_price
            temp[3] = proset[i].pro_origin
            temp[4] = proset[i].pro_store.user_name
            temp[5] = proset[i].pro_img
            a[i] = temp
        return JsonResponse({"status": True,
                             "products": a})

#查看产品
def check_product(request):
    proid = request.POST.get("pro_id")
    pro = models.Products.objects.filter(pro_id=proid)
    return JsonResponse({"status": True,
                         "pro_name": pro.pro_name,
                         "pro_price": pro.pro_price,
                         "pro_des": pro.pro_des,
                         "pro_store": pro.pro_store,
                         "pro_img": pro.pro_img})

#购买
def purchase(request):
    purproduct  = request.POST.get("pro_id")
    #+name
    purquantity = request.POST.get("pur_quantity")
    #purdate     = request.POST.get("pur_date")
    pursumer = request.POST.get("user_name")
    purprice    = request.POST.get("pro_price")
    models.Purchase.objects.create(pur_product=purproduct, pur_quantity=purquantity, pur_date=purdate, pur_consumer=pursumer, pur_price=purprice)
    return JsonResponse({"status": "purchase success"})


#商户上架产品
def new_arrival(request):
    pname = request.POST.get("pro_name")
    pimg = request.POST.get("pro_img")
    pdes = request.POST.get("pro_des")
    ptype = request.POST.get("pro_type")
    pprice = request.POST.get("pro_price")
    porigin = request.POST.get("pro_origin")
    userid = request.POST.get("user_id")
    models.Products.objects.create(pro_name=pname, pro_type=ptype, pro_price=pprice,
                                   pro_origin=porigin, pro_des=pdes, pro_img=pimg, pro_store=userid, pro_state=1)
    return JsonResponse({"status": True,
                         "message": "newly arrivals"})

#商户下架商品
def off_shelf(request):
    userid = request.POST.get("user_id")
    pname = request.POST.get("pro_name")
    models.Products.objects.filter(pro_name=pname).filter(pro_store=userid).update(pro_state=0)
    return JsonResponse({"status": True,
                         "message": "product is off shelf"})

#按商户浏览
def browse_by_prostore(request):
    userid = request.POST.get("user_id")
    proset = models.Products.objects.filter(pro_store=userid)
    x = proset.count()
    a = [0]*x
    for i in range(0, x):
        temp = [0, 1, 2, 3, 4]
        temp[0] = proset[i].pro_id
        temp[1] = proset[i].pro_name
        temp[2] = proset[i].pro_price
        temp[3] = proset[i].pro_origin
        temp[4] = proset[i].pro_img
        a[i] = temp
    return JsonResponse({"products": a})








# #2017-2019生产总值
# def total(request):
#     total = models.Gdp.objects.get(gdp_id=1).gdp_mount
#     return JsonResponse({"total": total})
#
# #2017-2019每月总产量
# def per_month():
#     x = models.Gdp.objests.all().count()-1
#     a = []
#     for i in range(0, x):
#         a[i] = {models.Gdp.objects.get(gdp_id=(i+2)).gdp_date: models.Gdp.objects.get(gdp_id=(i+2)).gdp_mount}
#     return JsonResponse({"per_month": a})
#
# #每个省2017-2019总产量
# def total_per_province():
#     x = 10
#     a = []
#     for i in range(0, x):
#         a[i] = {"province": 0}
#     return JsonResponse({"total_per_province": a})
#
# #2017/2018各类别农产品生产总值
# def total_per_product__per_year():
#     x = 10
#     a = [], b = []
#     for i in range(0, x):
#         a[i] = {"2017_type_of_farm_goods": 0}
#     for i in range(0, x):
#         b[i] = {"2018_type_of_farm_goods": 0}
#     return JsonResponse({"2017": a,
#                          "2018": b})
#
# #天气
# def weather(request):
#     temperature  = 0
#     weather_type = 0
#     return JsonResponse({"temperature": temperature,
#                          "weather_type": weather_type})
#
# #各地区消费能力
# def consume_ability():
#     value = 0
#     return JsonResponse({"consume_ability": value})
#
# #每类产品销售总额
# def sale_sum_per_product():
#     x = 10
#     a = []
#     for i in range(0, x):
#         a[i] = {"type_of_the_farm_goods": 0}
#     return JsonResponse({"sale_sum_per_product": a})
#
# #按时间消费额
# def sale_sum_per_day(request):
#     x = 10
#     a = []
#     for i in range(0, x):
#         a[i] = {"day": 0}
#     return JsonResponse({"sale_sum_per_day": a})
#
# def sale_sum_per_month(request):
#     x = 10
#     a = []
#     for i in range(0, x):
#         a[i] = {"month": 0}
#     return JsonResponse({"sale_sum_per_month": a})
#
#
# '''后续迭代'''
#
#
# #价格预测
# def pricepredict(request):
#     province = request.POST.get("province")
#     name     = request.POST.get("name")
#     past_price   = 0
#     future_price = 0
#     return JsonResponse({"past_price": past_price,
#                          "future_price": future_price})
#
# #产量预测
# def productpredict(request):
#     province = request.POST.get("province")
#     name     = request.POST.get("name")
#     product = 0
#     return JsonResponse({"product": product})



