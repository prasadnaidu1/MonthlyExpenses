from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from.models import *

# Create your views here.
def showindex(request):
    #id=request.GET.get("update_id")
    #if id==None:
        #res=friends.objects.all()

        #return render(request,"index.html",{"res":res})
    #else:
        #id1=friends.objects.filter(entry=id).update()
        return render(request,"index.html")

def displaydetails(request):
    expense= request.POST.get("t2")
    date= request.POST.get("date")
    amount= request.POST.get("amt")
    members= request.POST.getlist("t1")
    i=(", ".join(members))
    t=len(members)
    t1=int(amount)/t
    fr=friends(expenses=expense,date=date,amount=amount,members=i,res=t1)
    fr.save()

    d1={"Date":date,"Type of expenses":expense,"No Of Persons":t,"Members":members,"Indivisual Amount":t1,"Total expenses":amount}
    return render(request,"index.html",{"ans":d1,"msg":"Details saved SuccessFully"})



#def deletedetails(request):
    #=request.POST.get("delete_id")
    #friends.objects.filter(entry=id).delete()
    #res=friends.objects.all()
    #return render(request,"index.html",{"res":res})
#def showdetails(request):
  #  exp=request.POST.get("t1")
   # str=request.POST.get("t2")
    #end=request.POST.get("t3")


    #return render(request,"index.html")