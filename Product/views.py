from django.http import HttpResponse
from SqlHelper.SqlHelper import SqldbHelper

from django.shortcuts import render
import json
from django.http import HttpResponse


def index(request):
    return render(request, 'products/index.html')


def detail(request):
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




def addToCart(request, goodid):
    mydb = SqldbHelper()
    table = "cart"
    cond_dict = {"id": str(goodid)}
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
        'id':str(goodid)
    }
    success_json = json.dumps(success, indent=4, ensure_ascii=False)
    return HttpResponse(success_json, content_type="application/json,charset=utf-8")


def showAll(request):
    _, _, name, price, _ = searchAll()
    results = {
            'name': name,
            'price': price,
        }
    results_json = json.dumps(results, indent=4, ensure_ascii=False)
    return HttpResponse(results_json, content_type="application/json,charset=utf-8")








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
        id.append(str(i[0]))
    for i in mydb.select(table, fields=["num"]):
        num.append(str(i[0]))
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















# Create your views here.
