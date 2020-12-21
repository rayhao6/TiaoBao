from django.http import HttpResponse
from SqlHelper.SqlHelper import SqldbHelper
from django.shortcuts import get_object_or_404, render, redirect

from SqlHelper.SqlHelper import SqldbHelper
import json



def index(request):
    return render(request, 'index.html')


def getDetail(request):
    id, num, totalPrice, type = searchAll()

    #price_every = list(map(lambda a,b: a*b, num, price))
   # totalPrice = 0
    # for i in range(0,len(num)):
    #     totalPrice += num[i] *price[i]
    detail = {
        'id': id,
        'num': num,
        #'price': totalprice,
        #'price_every': price_every,
        'totalPrice': totalPrice,
        'detail': type
    }

    detail_json = json.dumps(detail, indent=4, ensure_ascii=False)
    return HttpResponse(detail_json, content_type="application/json,charset=utf-8")


def deleteOrder(request, id):
    mydb = SqldbHelper()
    id = 1  # 传入参数
    table = "orders"
    params = {"id": str(id)}
    mydb.delete(table, params)


def payment(request):
    return redirect('http://localhost:8000/Product')


def searchAll():
    mydb = SqldbHelper()
    idss_0 = []
    idss = []
    numss_0 = []
    numss = []
    total_prices = []
    typess = []
    all_types = ["id", "商品名", "单价", "品牌", "口味", "保质期", "质量", "尺寸", "颜色", "材料", "性别",
                 "衣领", "类型", "体积", "摄像头", "电池", "网络类型", "CPU", "RAM", "频率", "核",
                 "threads", "storage"]
    table = "orders"
    for i in mydb.select(table, fields=["ids"]):
        idss_0.append(i[0])
    for i in idss_0:
        ids = json.loads(i)
        idss.append(ids)
        # print(ids)
    for i in mydb.select(table, fields=["num"]):
        numss_0.append(i[0])
    for i in numss_0:
        nums = json.loads(i)
        numss.append(nums)
        # print(nums)
    for i in mydb.select(table, fields=["total_price"]):
        total_prices.append(i[0])
    table = "goods"

    for ids in idss:
        types_ = []
        for i in ids:
            types = mydb.select(table, cond_dict={"id": str(i)})
            types = types[0]
            one_type = ""
            for j in range(len(all_types)):
                if j == 0:
                    continue
                if types[j] == "NONE":
                    continue
                one_type = one_type + ", " + all_types[j] + ": " + str(types[j])
            one_type = one_type[2:]
            types_.append(one_type)
        typess.append(types_)
    print(idss)
    print(numss)
    print(total_prices)
    print(typess)
    return idss, numss, total_prices, typess









# Create your views here.
