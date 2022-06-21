from django.http import HttpResponse
from django.shortcuts import render
import joblib
def home(request):
    return render(request,"home.html")

def results(request):
    cls=joblib.load('WeightPredictionLinRegModel.joblib')
    lis=[]
    lis.append(request.GET['SEX'])
    lis.append(request.GET['Height'])
    print(lis)
    ans=cls.predict([lis])
    return render(request,"results.html",{'ans':ans,'lis':lis})
