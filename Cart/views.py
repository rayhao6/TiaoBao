from django.http import HttpResponse
from SqlHelper.SqlHelper import SqldbHelper
import json
from django.shortcuts import get_object_or_404, render, redirect


def index(request):
    id, num, name, price, type = searchAll()
    results = {
            'id': id,
            'name': name,
            'price': price,
            'num': num,
            'type': type
        }
    results_json = json.dumps(results, indent=4, ensure_ascii=False)
    return HttpResponse(results_json, content_type="application/json,charset=utf-8")


def getTotalPrice(request):
    _, num, _, price, _ = searchAll()
    totalPrice = 0
    for i in range(0,len(num)):
        totalPrice += num[i] * price[i]
    price = {
        'totalPrice' : totalPrice
    }
    price_json = json.dumps(price, indent=4, ensure_ascii=False)
    return HttpResponse(price_json, content_type="application/json,charset=utf-8")


def addToCart(request, goodid):
    mydb = SqldbHelper()
    table = "cart"
    cond_dict = {"id": str(goodid)}
    try:
        if mydb.select(table, cond_dict):
        # print(mydb.select(table, cond_dict, fields=["num"]))  # [(1,)]
            num = mydb.select(table, cond_dict, fields=["num"])
            num = int(num[0][0]) + 1
            params = {"id": str(goodid), "num": str(num)}
            mydb.update(table, params, cond_dict)
        else:
            params = {"id": str(goodid), "num": "1"}
            mydb.insert(table, params)
        success = {
            'success': 1,
            'id': str(goodid)
        }
        success_json = json.dumps(success, indent=4, ensure_ascii=False)
        return HttpResponse(success_json, content_type="application/json,charset=utf-8")

    except:
        success = {
            'success': 0
        }
        success_json = json.dumps(success, indent=4, ensure_ascii=False)
        return HttpResponse(success_json, content_type="application/json,charset=utf-8")

def deleteone(request, goodid):
    mydb = SqldbHelper()
    table = "cart"
    # params = {"id": str(id), "num": "1"}
    # mydb.insert(table, params)
    cond_dict = {"id": str(goodid)}
    if mydb.select(table, cond_dict):
        mydb.delete(table, cond_dict)
    else:
        print("购物车中不存在该商品！！！")
    success = {
        'success': 1,
        'id': str(goodid)
    }
    success_json = json.dumps(success, indent=4, ensure_ascii=False)
    return HttpResponse(success_json, content_type="application/json,charset=utf-8")


def deleteInCart(request, goodid):
    mydb = SqldbHelper()
    table = "cart"
    # params = {"id": str(id), "num": "1"}
    # mydb.insert(table, params)
    cond_dict = {"id": str(goodid)}
    if mydb.select(table, cond_dict):
        num = mydb.select(table, cond_dict, fields=["num"])
        num = int(num[0][0])
        if num == 1:
            mydb.delete(table, cond_dict)
        else:
            num = num - 1
            params = {"id": str(goodid), "num": str(num)}
            mydb.update(table, params, cond_dict)
        success = {
            'success': 1,
            'id':str(goodid)
        }
        success_json = json.dumps(success, indent=4, ensure_ascii=False)
        return HttpResponse(success_json,content_type="application/json,charset=utf-8")

    else:
        success = {
            'success': 0
        }
        success_json = json.dumps(success, indent=4)
        return HttpResponse(success_json)


def deleteAllCart(request):
    mydb = SqldbHelper()
    table = "cart"
    mydb.deleteTable(table)
    success = {
        'success': 1
    }
    success_json = json.dumps(success, indent=4)
    return HttpResponse(success_json)


def addToOrder(request):
    id = [1, 2, 3, 4]  # 传入参数
    num = [2, 3, 3, 2]  # 传入参数
    total_price = 199  # 传入参数
    mydb = SqldbHelper()
    table = "orders"
    sub_id = mydb.select(table, fields=["id"])
    sub_ids = []
    for i in sub_id:
        sub_ids.append(i[0])
    new_id = max(sub_ids) + 1

    ids = ""
    for i in id:
        ids = ids + ", " + str(i)
    ids = "[" + ids[2:] + "]"

    nums = ""
    for i in num:
        nums = nums + ", " + str(i)
    nums = "[" + nums[2:] + "]"

    params = {"id": str(new_id), "ids": str(ids), "num": str(nums), "total_price": str(total_price)}
    mydb.insert(table, params)
    return redirect('http://localhost:8000/Order')

    #有点小问题，应该在购物车中查数量和价格


def searchAll():
    mydb = SqldbHelper()
    id = []
    num = []
    name = []
    price = []
    type = []

    all_types = ["id", "name", "单价", "品牌", "口味", "保质期", "质量", "尺寸", "颜色", "材料", "性别",
                 "衣领", "类型", "体积", "摄像头", "电池", "网络类型", "CPU", "RAM", "频率", "核",
                 "threads", "storage"]
    table = "cart"
    for i in mydb.select(table, fields=["id"]):
        id.append(i[0])
    for i in mydb.select(table, fields=["num"]):
        num.append(i[0])
    table = "goods"
    for i in id:
        name_i = mydb.select(table, cond_dict={"id": str(i)}, fields=["name"])
        name.append(name_i[0][0])
    for i in id:
        types = mydb.select(table, cond_dict={"id": str(i)})
        types = types[0]
        print(types)
        one_type = ""
        for j in range(len(all_types)):
            if j == 0:
                continue
            if j == 1:
                continue
            if j == 2:
                price.append(types[j])
            if types[j] == "NONE":
                continue
            one_type = one_type + ", " + all_types[j] + ": " + str(types[j])
        one_type = one_type[2:]
        type.append(one_type)
    return id, num, name, price, type

from django.shortcuts import render

# Create your views here.
