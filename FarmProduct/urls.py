from django.urls import re_path,path, include
from . import views

urlpatterns = [

    re_path(r'^login/*$',                       views.login,                        name='login'),
    re_path(r'^register/*$',                    views.register,                     name='register'),
    re_path(r'^browse_by_protype/*$',           views.browse_by_protype,            name='browse_by_protype'),
    re_path(r'^check_product/*$',               views.check_product,                name='check_product'),
    re_path(r'^purchase/*$',                    views.purchase,                     name='purchase'),
    re_path(r'^search/*$',                      views.search,                       name='search'),
    re_path(r'^new_arrival/*$',                 views.new_arrival,                  name='new_arrival'),
    re_path(r'^off_shelf/*$',                  views.off_shelf,                   name='off_shelf'),
    re_path(r'^browse_by_prostore/*$',          views.browse_by_prostore,           name='browse_by_prostore'),
    re_path(r'^yield1/*$',                       views.yield1,                        name='yield1'),
    re_path(r'^test/*$',                        views.test,                         name='test'),


    # #第一次迭代
    # re_path(r'^total/*$',                       views.total,                        name='total'),
    # re_path(r'^weather/*$',                     views.weather,                      name='weather'),
    # re_path(r'^per_month/*$',                   views.per_month,                    name='per_month'),
    # re_path(r'^total_per_province/*$',          views.total_per_province,           name='total_per_province'),
    # re_path(r'^total_per_product__per_year/*$', views.total_per_product__per_year,  name='total_per_product__per_year'),
    # re_path(r'^weather/*$',                     views.weather,                      name='weather'),
    # re_path(r'^/consume_ability*$',             views.consume_ability,              name='consume_ability'),
    # re_path(r'^sale_sum_per_product/*$',        views.sale_sum_per_product,         name='sale_sum_per_product'),
    # re_path(r'^sale_sum_per_day/*$',            views.sale_sum_per_day,             name='sale_sum_per_day'),
    # re_path(r'^sale_sum_per_month/*$',          views.sale_sum_per_month,           name='sale_sum_per_month'),

    #后续迭代

    # re_path(r'^pricepredict/*$',                views.pricepredict,                 name='pricepredict'),
    # re_path(r'^productpredict/*$',              views.productpredict,               name='productpredict'),



]