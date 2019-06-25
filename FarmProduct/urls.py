from django.urls import re_path,path, include
from . import views

urlpatterns = [
    #第一次迭代
    re_path(r'^total/*$',                       views.total,                        name='total'),
    re_path(r'^weather/*$',                     views.weather,                      name='weather'),
    re_path(r'^per_month/*$',                   views.per_month,                    name='per_month'),
    re_path(r'^total_per_province/*$',          views.total_per_province,           name='total_per_province'),
    re_path(r'^total_per_product__per_year/*$', views.total_per_product__per_year,  name='total_per_product__per_year'),
    re_path(r'^weather/*$',                     views.weather,                      name='weather'),
    re_path(r'^/consume_ability*$',             views.consume_ability,              name='consume_ability'),
    re_path(r'^sale_sum_per_product/*$',        views.sale_sum_per_product,         name='sale_sum_per_product'),
    re_path(r'^sale_sum_per_day/*$',            views.sale_sum_per_day,             name='sale_sum_per_day'),
    re_path(r'^sale_sum_per_month/*$',          views.sale_sum_per_month,           name='sale_sum_per_month'),

    #后续迭代
    re_path(r'^login/*$',                       views.login,                        name='login'),
    re_path(r'^register/*$',                    views.register,                     name='register'),
    re_path(r'^pricepredict/*$',                views.pricepredict,                 name='pricepredict'),
    re_path(r'^productpredict/*$',              views.productpredict,               name='productpredict'),



]