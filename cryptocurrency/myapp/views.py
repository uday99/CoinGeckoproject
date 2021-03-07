from django.shortcuts import render,redirect
from myapp.forms import UserForm,ForgetForm
from myapp.utils import search_coin,get_detail
from myapp.newsutils import get_news
from myapp.dummy import get_list
from django.contrib import messages
from myapp.models import UserModel,CryptoModel
from django.views.generic import View
from myapp.pwdcustom import pass_validator
from django.core.exceptions import ValidationError


# Create your views here.
def showIndex(request):

    s_coin=search_coin()

    # detail = get_detail()
    # for x in detail:
    #     print(x['id'], '--', x['symbol'], '--', x['name'], '--', x['image'], '--', x['current_price'],
    #           x['price_change_percentage_24h'], x['market_cap'], x['market_cap_change_percentage_24h'])

    un=request.session['username']
    print(un)
    object=UserModel.objects.get(username=un)

    data= CryptoModel.objects.filter(user=object)
    return render(request,"cryptocurrency/index.html",{"search":s_coin,'data':data})




def detailCryp(request):

    id=request.GET.get('mycrypto')
    print(id)

    data = get_news()
    print(data)



    return render(request,"cryptocurrency/Detail.html",{'id':id,'news':data})



def listData(request):
    data=get_list()


    return render(request,'demo.html',{'data':data})


def userlogin(request):
    if request.method=="POST":
        un=request.POST.get('email')
        pwd=request.POST.get('password')

        try:
            UserModel.objects.get(username=un,password=pwd)
            request.session['username']=un

            detail = get_detail()
            for x in detail:
                print(x['id'], '--', x['symbol'], '--', x['name'], '--', x['image'], '--', x['current_price'],
                      x['price_change_percentage_24h'], x['market_cap'], x['market_cap_change_percentage_24h']),x['sparkline_in_7d']['price']
                Cm=CryptoModel(name=x['name'],image=x['image'],symbol=x['symbol'],price=x['current_price'],percent_change=x['price_change_percentage_24h'],market_cap=x['market_cap'],market_cap_change_24h=x['market_cap_change_percentage_24h'],user=UserModel.objects.get(username=un))
                Cm.save()
            return redirect('main')
        except UserModel.DoesNotExist:

            return render(request,"user/login.html",{'error':"Invalid username/password"})




    else:

        return render(request,'user/login.html')


def registerUser(request):
    return render(request,"user/register.html",{'register':UserForm})


def signUp(request):
    un=request.POST.get('username')

    pwd=request.POST.get('password')
    cpwd=request.POST.get('confirm_password')
    print(un,pwd,cpwd)
    um=UserModel(username=un,password=pwd,confirmpass=cpwd)
    if pwd==cpwd:

        um.save()
        messages.success(request, "User Saved successfuly")
        return redirect('register')
        # pv=pass_validator()
        # pv.validate(pwd)
        #
        # if pv.validate(pwd) == True:
        #     um.save()
        #     messages.success(request, "User Saved successfuly")
        #     return redirect('register')
        # else:
        #     #data = pv.validate(pwd)
        #
        #     return render(request, "user/register.html", { 'register': UserForm})






    else:

        error="password and Confirm password is not matching"

    return render(request,"user/register.html",{'error':error,'register':UserForm()})


def forgetPwd(request):
    if request.method=='POST':
        un=request.POST.get('username')
        try:
            UserModel.objects.get(username=un)
            return render(request,'user/rset.html',{'un':un})
        except UserModel.DoesNotExist:
            return render(request,'user/forgetpwd.html',{"error":"Invalid EmailId DoesntExist...",'ff':ForgetForm()})
    else:
        return render(request,"user/forgetpwd.html",{'ff':ForgetForm()})


def resetPwd(request):
    if request.method == 'POST':
        un=request.GET.get('un')
        print(un)
        pwd=request.POST.get('password')
        cpwd=request.POST.get('confirmpwd')
        #print(pwd,cpwd)

        if pwd==cpwd:
            try:
                um=UserModel.objects.get(username=un)
                um.password=pwd
                um.confirmpass=cpwd
                um.save()
                messages.success(request,"Password Changed successfully")
                return redirect('login')


            except UserModel.DoesNotExist:
                return render(request, "user/forgetpwd.html", {'error': "Invalid username/password"})


        else:
            error = "password and Confirm password is not matching"
            return  render(request,"user/rset.html",{'error':error})

    else:
        return render(request,'user/rset.html')


def logoutUser(request):
    try:

        un=request.session['username']
        CryptoModel.objects.filter(user=un).delete()
        del request.session['username']
        return redirect('login')

    except KeyError:
        return render(request,"cryptocurrency/index.html")
