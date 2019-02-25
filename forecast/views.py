from django.shortcuts import render,HttpResponse
import json
# import pandas,seaborn,numpy
# from sklearn import neighbors
# from sklearn.preprocessing import LabelEncoder
# Create your views here.
result_list = []
from static import fit
def login(request):
    return render(request,"iris.html",{"result_list":result_list})


def classify(request):
    data = {"status":True,"error":None,"res":None}
    try:
        sl = float(request.POST.get("sl"))
        sw = float(request.POST.get("sw"))
        pl = float(request.POST.get("pl"))
        pw = float(request.POST.get("pw"))
        model,leb = fit.Fit()
        res1 = model.predict([[sl,sw,pl,pw]])
        res2 = leb.inverse_transform(res1)
        res=res2[0]
        res_data = (sl,sw,pl,pw,res)
        result_list.append(res_data)
        data["res"]=res
    except:
        data["status"]=False
        data["error"]="请求错误"
    return HttpResponse(json.dumps(data))