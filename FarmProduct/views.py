from django.shortcuts import render
import json
from django.http import HttpResponse
from django.http import JsonResponse
from . import models
from sklearn.externals import joblib
import numpy as np
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
    purdate     = request.POST.get("pur_date")
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
#价格预测
import datetime

def pricepredict(request):
    market = request.POST.get("market")
    name     = request.POST.get("name")
    #一些字典
    dict_market={
               '章丘市刁镇蔬菜批发市场': {'zone': '济南', 'numb': 0},
               '济南堤口果品批发市场':{'zone':'济南','numb':1},
               '济宁蔬菜批发市场':{'zone':'济宁','numb':2},
               '凯盛国际农产品物流园':{'zone':'济宁','numb':3},
               '山东金乡大蒜专业批发市场': {'zone': '济宁', 'numb': 4},
               '宁津县东崔蔬菜批发市场': {'zone': '德州', 'numb': 5},
               '临邑县临南蔬菜大市场': {'zone': '德州', 'numb': 6},
               '黑马农贸市场': {'zone': '德州', 'numb': 7},
               '青岛东庄头蔬菜批发市场':{'zone':'青岛','numb':8},
               '青岛南村蔬菜批发市场':{'zone':'青岛','numb':9},
               '青岛市城阳蔬菜水产品批发市场有限公司':{'zone':'青岛','numb':10},
               '山东省滨州市滨城区鲁北（六街）蔬菜批发市场':{'zone':'滨州','numb':11},
               '山东寿光果菜批发市场':{'zone':'潍坊','numb':12},
               '滕州市农副产品物流中心':{'zone':'枣庄','numb':13},
               '威海市农副产品批发市场':{'zone':'威海','numb':14},
               '威海水产品批发市场':{'zone':'威海','numb':15},
               }
    dict_name={"菠菜": 0, "蘑菇": 1, "红蒜6.0公分": 2, "油菜": 3, "莲藕": 4, "黄瓜": 5, "芸豆": 6, "丰水梨": 7, "西红柿": 8, "大白菜": 9, "香蕉": 10,
     "苦瓜": 11, "生菜": 12, "带鱼": 13, "大葱": 14, "红提子": 15, "白蒜5.0公分": 16, "土豆": 17, "青萝卜": 18, "芹菜": 19, "茄子": 20,
     "红蒜5.0公分": 21, "茴香": 22, "白萝卜": 23, "蒜薹": 24, "胡萝卜": 25, "香菇": 26, "冬瓜": 27, "山药": 28, "扇贝": 29, "巨峰葡萄": 30,
     "西葫芦": 31, "南瓜": 32, "圆葱": 33, "尖椒": 34, "雪梨": 35, "青椒": 36, "白蒜6.0公分": 37, "富士苹果": 38, "西兰花": 39, "鸡蛋": 40,
     "丝瓜": 41, "鲈鱼": 42, "鲅鱼": 43, "菜花": 44, "鸭梨": 45, "洋葱": 46, "平菇": 47, "活草鱼": 48, "韭菜": 49, "甘蓝": 50, "生姜": 51,
     "洋白菜": 52, "大黄花鱼": 53, "蛤蜊": 54, "白条鸡": 55, "香菜": 56, "豆角": 57, "海参": 58, "活鲫鱼": 59, "西瓜": 60, "黑鱼": 61, "活鲤鱼": 62,
     "甜瓜": 63, "小黄花鱼": 64, "酥梨": 65, "花鲢活鱼": 66, "蒜苗": 67, "樱桃西红柿": 68, "羊肉": 69, "核桃": 70, "黑美人西瓜": 71, "萝卜": 72,
     "石榴": 73, "佛手瓜": 74, "海蛎": 75, "梭子蟹": 76, "牛肉": 77, "猪肉": 78, "枣": 79, "葡萄": 80, "香瓜": 81, "玫瑰香葡萄": 82, "梨": 83,
     "苹果": 84, "大蒜": 85, "鲜蘑菇": 86, "草莓": 87, "油桃": 88, "莴笋": 89, "白菜花": 90, "水萝卜": 91, "板栗": 92}
    market_place=dict_market[market]['zone']#市场所属城市

    #一些模型用到的数据
    name_numb=dict_name[name]#名称编号
    market_numb=dict_market[market]['numb']#市场编号
    tem=[]#每一天的平均温度
    weather_state=[]#每一天的天气状况
    Y = []#要预测的时间所属年份
    M = []#要预测的时间所属月份
    D = []#要预测的时间所属日期
    #获取当前时间
    now_time = datetime.datetime.now()
    # 获取前十天和未来五天的年，月，日

    for i in range(-9,6):
        Y_M_D=now_time+datetime.timedelta(days=i)
        str_date=Y_M_D.strftime('%Y%m%d')
        Y.append(int(Y_M_D.strftime('%Y')))
        M.append(int(Y_M_D.strftime('%m')))
        D.append(int(Y_M_D.strftime('%d')))
        #找到当天的天气情况
        weather=models.Weather.objects.filter(wea_date__exact=str_date).filter(wea_place__exact=market_place)[0]
        wea_state=weather.wea_state#当天的天气是晴雨还是阴
        wea_tem=(weather.wea_temp_min+weather.wea_temp_max)/2.#当天的平均气温
        tem.append(wea_tem)
        weather_state.append(wea_state)

    #加载模型
    clf = joblib.load('./static/models/price_models/clf0.pkl')
    #输入矩阵
    p_data = np.zeros([15, 23])
    for i in range(30):
        p_data[i][15] = market_numb+0.
        p_data[i][16] = tem[i]
        p_data[i][17] = weather_state[i]
        p_data[i][18] = D[i]+0
        p_data[i][19] = M[i]+0.
        p_data[i][2019 - 1997] = Y[i]+0.
    #开始预测
    predic_data=clf.predict(p_data)
    past_price=predic_data[0:10]
    future_price=predic_data[10:15]
    return JsonResponse(
        {
            'status':200,
            'message':'success',
            'data':{
                'pastprice':past_price,
                'futureprice':future_price,
            },
        }
    )


# #产量预测
# def productpredict(request):
#     province = request.POST.get("province")
#     name     = request.POST.get("name")
#     product = 0
#     return JsonResponse({"product": product})



