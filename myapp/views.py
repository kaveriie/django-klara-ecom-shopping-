from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
from random import randint
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# Create your views here.

def index(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        new_id=Products.objects.order_by('id').reverse()[0:3]

        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()

        newr_id=Reviews.objects.order_by('id').reverse()[0:5]

        wcount=Wishlist.objects.filter(c_id=cid).count()

        ocount=Billing.objects.filter(c_id=cid).count()


        return render(request,"myapp/index.html",{'new_id':new_id,'uid':uid,'count':count,'newr_id':newr_id,'wcount':wcount,'ocount':ocount})
    else:
        new_id=Products.objects.order_by('id').reverse()[0:3]
        newr_id=Reviews.objects.order_by('id').reverse()[0:3]
        return render(request,"myapp/index.html",{'new_id':new_id,'newr_id':newr_id})
        


def mindex(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Manager.objects.get(user_id=uid)
        newr_id=Reviews.objects.order_by('id').reverse()[0:5]

        return render(request,"myapp/mindex.html",{'uid':uid,'newr_id':newr_id,'mid':mid})
    else:
        newr_id=Reviews.objects.order_by('id').reverse()[0:3]
        return render(request,"myapp/mindex.html",{'newr_id':newr_id})


def cart(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        cart_id=Cart.objects.filter(c_id=cid)
        count=Cart.objects.filter(c_id=cid).count()
        data=Cart.objects.all()
        wcount=Wishlist.objects.filter(c_id=cid).count()
        ocount=Billing.objects.filter(c_id=cid).count()

        cart_total=0
        for i in cart_id:
            cart_total+=int(i.product_total)
        new_total=cart_total

        cid.billamt=new_total
        cid.save()
        return render(request,"myapp/cart.html",{'uid':uid,'cid':cid,'cart_id':cart_id,'data':data,'count':count,'wcount':wcount,'cart_total':cart_total,'new_total':new_total,'ocount':ocount})
    else:
        return render(request,"myapp/cart.html")

def categories(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Products.objects.all()
        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()
        wcount=Wishlist.objects.filter(c_id=cid).count()
        ocount=Billing.objects.filter(c_id=cid).count()

        return render(request,"myapp/categories.html",{'data':data,'uid':uid,'count':count,'wcount':wcount,'ocount':ocount})        
    else:
        data=Products.objects.all()
        return render(request,"myapp/categories.html",{'data':data})        


def checkout(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()
        cart_id=Cart.objects.filter(c_id=cid)
        wcount=Wishlist.objects.filter(c_id=cid).count()
        ocount=Billing.objects.filter(c_id=cid).count()



        cart_total=0
        for i in cart_id:
            cart_total+=int(i.product_total)

        if cart_total>cid.billamt:
            disc=float(cart_total-(cid.billamt))
            dmsg="Discount from Coupon"
            return render(request,"myapp/checkout.html",{'uid':uid,'cid':cid,'count':count,'ocount':ocount,'cart_id':cart_id,'wcount':wcount,'cart_total':cart_total,'dmsg':dmsg,'disc':disc})        
        else:            
            return render(request,"myapp/checkout.html",{'uid':uid,'cid':cid,'count':count,'ocount':ocount,'cart_id':cart_id,'wcount':wcount,'cart_total':cart_total})        
    else:
        return render(request,"myapp/checkout.html")

def contact(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()
        wcount=Wishlist.objects.filter(c_id=cid).count()
        ocount=Billing.objects.filter(c_id=cid).count()

        return render(request,"myapp/contact.html",{'uid':uid,'count':count,'wcount':wcount,'ocount':ocount})        
    else:
        return render(request,"myapp/contact.html")


def login(request):
    return render(request,"myapp/login.html")

def registrationpage(request):
    return render(request,"myapp/registrationpage.html")

def register(request):
    try:
        role=request.POST['role']
        firstname=request.POST['firstname']
        email=request.POST['email']
        password=request.POST['password']

        uid=User.objects.create(role=role,email=email,password=password)

        if uid:
            if role=="manager":
                mid=Manager.objects.create(user_id=uid,firstname=firstname)
            else:
                cid=Customer.objects.create(user_id=uid,firstname=firstname)

            return render(request,"myapp/login.html")
    except:
        return render(request,"myapp/registrationpage.html")

def loginevaluate(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        if uid.role=="manager":
            mid=Manager.objects.get(user_id=uid)
            return render(request,"myapp/mindex.html",{'uid':uid,'mid':mid})
        else:
            cid=Customer.objects.get(user_id=uid)
            new_id=Products.objects.order_by('id').reverse()[0:3]
            newr_id=Reviews.objects.order_by('id').reverse()[0:3]
            count=Cart.objects.filter(c_id=cid).count()
            wcount=Wishlist.objects.filter(c_id=cid).count()
            ocount=Billing.objects.filter(c_id=cid).count()
            return render(request,"myapp/index.html",{'uid':uid,'cid':cid,'count':count,'ocount':ocount,'new_id':new_id,'wcount':wcount,'newr_id':newr_id})

    else:
        email=request.POST['email']
        password=request.POST['password']

        uid=User.objects.get(email=email)
        if uid:
            if uid.password==password:
                if uid.role=="manager":
                    mid=Manager.objects.get(user_id=uid)
                    request.session['role']=uid.role
                    request.session['firstname']=mid.firstname
                    request.session['email']=uid.email
                    newr_id=Reviews.objects.order_by('id').reverse()[0:3]

                    return render(request,"myapp/mindex.html",{'uid':uid,'mid':mid,'newr_id':newr_id})
                else:
                    cid=Customer.objects.get(user_id=uid)
                    request.session['role']=uid.role
                    request.session['firstname']=cid.firstname
                    request.session['email']=uid.email
                    newr_id=Reviews.objects.order_by('id').reverse()[0:3]
                    count=Cart.objects.filter(c_id=cid).count()
                    wcount=Wishlist.objects.filter(c_id=cid).count()
                    ocount=Billing.objects.filter(c_id=cid).count()

                    return render(request,"myapp/index.html",{'uid':uid,'cid':cid,'count':count,'ocount':ocount,'wcount':wcount,'newr_id':newr_id})
            else:
                    e_msg="Invalid password"
                    return render(request,"myapp/login.html",{'e_msg':e_msg})

        else:
            e_msg="Invalid email"  
            return render(request,"myapp/login.html",{'e_msg':e_msg})


def logout(request):
    if "email" in request.session:
        del request.session['email']
        del request.session['role']
        del request.session['firstname']        
        s_msg="Succesfully logged out"
        return render(request,"myapp/login.html",{'s_msg':s_msg})



def forgotpassword(request):
    return render(request,"myapp/forgotpassword.html")


def sendotp(request):
    try:
        otp=randint(1111,9999)
        uid=User.objects.get(email=request.POST['email'])
        uid.otp=otp
        uid.save()
        msg="Your OTP is "+str(otp)
        send_mail("Forgot Password",msg,"k.kaveriie@gmail.com",[uid.email])
        return render(request,"myapp/resetpassword.html",{'uid':uid})
    except:
        e_msg="Email not found!"
        return render(request,"myapp/forgotpassword.html",{'e_msg':e_msg})




def resetpassword(request):
    email=request.POST['email']
    otp=request.POST['otp']
    newpassword=request.POST['newpassword']
    repassword=request.POST['repassword']
    uid=User.objects.get(email=email)

    if str(uid.otp)==str(otp):
        if newpassword==repassword:
            uid.password=newpassword
            uid.save()

            return render(request,"myapp/login.html")
        else:
            e_msg="Passwords do not match!"
            return render(request,"myapp/resetpassword.html",{'e_msg':e_msg,'uid':uid})

    else:
        e_msg="Invalid OTP"
        return render(request,"myapp/resetpassword.html",{'e_msg':e_msg,'uid':uid})





def addproduct(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        return render(request,"myapp/addproduct.html",{'uid':uid})
    else:
        return render(request,"myapp/addproduct.html")


def updateproduct(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
    try:
        productname=request.POST['productname']
        productprice=request.POST['productprice']
        productquantity=request.POST['productquantity']
        productimage=request.FILES['productimage']
        pid=Products.objects.create(productname=productname,productprice=productprice,productquantity=productquantity,productimage=productimage)

        data=Products.objects.all()
        return render(request,"myapp/allproducts.html",{'data':data,'pid':pid,'uid':uid})        
    except:
        return render(request,"myapp/addproduct.html")



def allproducts(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Products.objects.all()
        mid=Manager.objects.filter(user_id=uid)
        return render(request,"myapp/allproducts.html",{'data':data,'uid':uid,'mid':mid})
    else:
        return render(request,"myapp/allproducts.html")


def editproduct(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Products.objects.get(id=pk)
        mid=Manager.objects.filter(user_id=uid)

        return render(request,"myapp/editproduct.html",{'pid':pid,'uid':uid,'mid':mid})
    else:
        pid=Products.objects.get(id=pk)
        return render(request,"myapp/editproduct.html",{'pid':pid})


def deleteproduct(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Manager.objects.filter(user_id=uid)

        pid=Products.objects.get(id=pk)
        pid.delete()
        data=Products.objects.all()
        return render(request,"myapp/allproducts.html",{'data':data,'mid':mid,'uid':uid})
    else:
        return render(request,"myapp/allproducts.html")


def savechanges(request):
    if "productimage" in request.FILES:
        id=request.POST['id']
        productname=request.POST['productname']
        productquantity=request.POST['productquantity']
        productprice=request.POST['productprice']
        productimage=request.FILES['productimage']

        pid=Products.objects.get(id=id)
        pid.productname=productname
        pid.productquantity=productquantity
        pid.productprice=productprice
        pid.productimage=productimage
        pid.save()
        data=Products.objects.all()
        return render(request,"myapp/allproducts.html",{'pid':pid,'data':data}) 

    else:
        id=request.POST['id']
        productname=request.POST['productname']
        productquantity=request.POST['productquantity']
        productprice=request.POST['productprice']

        pid=Products.objects.get(id=id)
        pid.productname=productname
        pid.productquantity=productquantity
        pid.productprice=productprice
        pid.save()
        data=Products.objects.all()

        return render(request,"myapp/allproducts.html",{'pid':pid,'data':data}) 



def viewproduct(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Products.objects.get(id=pk)
        cid=Customer.objects.get(user_id=uid)
        rid=Reviews.objects.filter(p_id=pid)
        count=Cart.objects.filter(c_id=cid).count()
        wcount=Wishlist.objects.filter(c_id=cid).count()
        ocount=Billing.objects.filter(c_id=cid).count()


        return render(request,"myapp/viewproduct.html",{'pid':pid,'cid':cid,'uid':uid,'rid':rid,'count':count,'wcount':wcount,'ocount':ocount})
    else:            
        pid=Products.objects.get(id=pk)
        rid=Reviews.objects.filter(p_id=pid)
        return render(request,"myapp/viewproduct.html",{'pid':pid,'rid':rid})


def review(request):    
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])

    try:
        pid=request.POST['pid']
        firstname=request.POST['firstname']
        reviewrating=request.POST['reviewrating']
        reviewtext=request.POST['reviewtext']
        pid=Products.objects.get(id=pid)
        cid=Customer.objects.get(user_id=uid)
        rid=Reviews.objects.create(c_id=cid,p_id=pid,reviewrating=reviewrating,reviewtext=reviewtext)
        data=Reviews.objects.all()
        return render(request,"myapp/viewproduct.html",{'data':data,'rid':rid,'pid':pid,'firstname':firstname})        
    except:
        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()
        wcount=Wishlist.objects.filter(c_id=cid).count()
        ocount=Billing.objects.filter(c_id=cid).count()

        data=Products.objects.all()
        return render(request,"myapp/categories.html",{'data':data,'uid':uid,'count':count,'wcount':wcount,'ocount':ocount})        


def viewreviews(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Manager.objects.get(user_id=uid)
        data=Reviews.objects.all()
        return render(request,"myapp/viewreviews.html",{'data':data,'uid':uid,'mid':mid})        
    else:
        return render(request,"myapp/viewreviews.html")        
    



def addtocart(request):
    try:
        c_id=request.POST['c_id']
        p_id=request.POST['p_id']
        product_radio=request.POST['product_radio']
        product_quantity=request.POST['product_quantity']
        
        pid=Products.objects.get(id=p_id)
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        reviewdata=Reviews.objects.all()
        wcount=Wishlist.objects.filter(c_id=cid).count()

        product_total=int(product_quantity)*(int(pid.productprice))
        
        cart_id=Cart.objects.create(c_id=cid,p_id=pid,product_radio=product_radio,product_quantity=product_quantity,product_total=product_total)
        count=Cart.objects.filter(c_id=cid).count()
        

        s_msg="Added to cart!"
        return render(request,"myapp/viewproduct.html",{'cart_id':cart_id,'cid':cid,'pid':pid,'reviewdata':reviewdata,'s_msg':s_msg,'count':count,'uid':uid,'wcount':wcount})
    except:
        uid=User.objects.get(email=request.session['email'])
        pid=Products.objects.get(id=p_id)
        cid=Customer.objects.get(user_id=uid)
        reviewdata=Reviews.objects.all()
        count=Cart.objects.filter(c_id=cid).count()

        e_msg="There was an error.."
        return render(request,"myapp/viewproduct.html",{'cid':cid,'pid':pid,'reviewdata':reviewdata,'e_msg':e_msg,'count':count})



def deletecartproduct(request,pk):
    cartdelete_id=Cart.objects.get(id=pk)
    cartdelete_id.delete()
    data=Cart.objects.all()

    uid=User.objects.get(email=request.session['email'])
    cid=Customer.objects.get(user_id=uid)
    cart_id=Cart.objects.filter(c_id=cid)

    count=Cart.objects.filter(c_id=cid).count()
    wcount=Wishlist.objects.filter(c_id=cid).count()

    cart_total=0
    for i in cart_id:
        cart_total+=int(i.product_total)

    new_total=cart_total
    cid.billamt=new_total
    cid.save()
    return render(request,"myapp/cart.html",{'data':data,'count':count,'cart_id':cart_id,'uid':uid,'cid':cid,'wcount':wcount,'cart_total':cart_total,'new_total':new_total})




def clearcart(request):
    uid=User.objects.get(email=request.session['email'])
    cid=Customer.objects.get(user_id=uid)
    
    alldelete_id=Cart.objects.filter(c_id=cid)
    alldelete_id.delete()

    cart_id=Cart.objects.filter(c_id=cid)

    count=Cart.objects.filter(c_id=cid).count()

    return render(request,"myapp/cart.html",{'count':count,'cart_id':cart_id})



def postmessage(request):
    try:
        message_name=request.POST['message_name']
        message_email=request.POST['message_email']
        message_subject=request.POST['message_subject']
        message=request.POST['message']

        message_id=Messages.objects.create(message_name=message_name,message_email=message_email,message_subject=message_subject,message=message)
        s_msg="Successfully sent message!"
        return render(request,"myapp/contact.html",{'s_msg':s_msg})
    except:
        e_msg="Sorry! Try again..."
        return render(request,"myapp/contact.html",{'e_msg':e_msg})


def allmessages(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        data=Messages.objects.all()
        mid=Manager.objects.get(user_id=uid)
        return render(request,"myapp/allmessages.html",{'data':data,'uid':uid,'mid':mid})
    else:
        return render(request,"myapp/allmessages.html")


def myprofile(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])

        if uid.role=="customer":
            cid=Customer.objects.get(user_id=uid)
            wcount=Wishlist.objects.filter(c_id=cid).count()
            count=Cart.objects.filter(c_id=cid).count()
            ocount=Billing.objects.filter(c_id=cid).count()

            return render(request,"myapp/myprofile.html",{'cid':cid,'count':count,'wcount':wcount,'uid':uid,'ocount':ocount})

        else:
            mid=Manager.objects.get(user_id=uid)
            return render(request,"myapp/myprofile.html",{'mid':mid,'uid':uid})

    else:
        return render(request,"myapp/myprofile.html")


def editprofile(request):
    if "profilepic" in request.FILES:
        id=request.POST['id']
        firstname=request.POST['firstname']
        email=request.POST['email']
        password=request.POST['password']
        profilepic=request.FILES['profilepic']

        uid=User.objects.get(id=id)
        uid.email=email
        uid.password=password
        uid.profilepic=profilepic
        uid.save()

        if uid.role=="customer":
            cid=Customer.objects.get(user_id=uid)
            cid.firstname=firstname
            #request.session['firstname']=firstname
            cid.save()
            wcount=Wishlist.objects.filter(c_id=cid).count()
            count=Cart.objects.filter(c_id=cid).count()
            ocount=Billing.objects.filter(c_id=cid).count()
            return render(request,"myapp/myprofile.html",{'uid':uid,'cid':cid,'count':count,'wcount':wcount,'ocount':ocount}) 
        else:
            mid=Manager.objects.get(user_id=uid)
            mid.firstname=firstname
            mid.save()
            return render(request,"myapp/myprofile.html",{'uid':uid,'mid':mid}) 

    else:
        id=request.POST['id']
        firstname=request.POST['firstname']
        email=request.POST['email']
        password=request.POST['password']

        uid=User.objects.get(id=id)
        uid.email=email
        uid.password=password
        uid.save()

        if uid.role=="customer":
            cid=Customer.objects.get(user_id=uid)
            cid.firstname=firstname
            cid.save()
            wcount=Wishlist.objects.filter(c_id=cid).count()
            count=Cart.objects.filter(c_id=cid).count()
            ocount=Billing.objects.filter(c_id=cid).count()
            return render(request,"myapp/myprofile.html",{'uid':uid,'cid':cid,'count':count,'wcount':wcount,'ocount':ocount}) 
        else:
            mid=Manager.objects.get(user_id=uid)
            mid.firstname=firstname
            mid.save()
            return render(request,"myapp/myprofile.html",{'uid':uid,'mid':mid}) 



def subscribe(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])

    s_email=request.POST['email']
    sid=Subscribers.objects.create(email=s_email)
    subs_msg="Successfully subscribed.. Please check your email!"
    msg="Welcome to Klara! You have successfully subscribed!"
    send_mail("Welcome",msg,"k.kaveriie@gmail.com",[s_email])

    cid=Customer.objects.get(user_id=uid)
    count=Cart.objects.filter(c_id=cid).count()
    wcount=Wishlist.objects.filter(c_id=cid).count()

    new_id=Products.objects.order_by('id').reverse()[0:3]    
    return render(request,"myapp/subscribed.html",{'subs_msg':subs_msg,'new_id':new_id,'count':count,'wcount':wcount,'uid':uid})

def allsubscribers(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Manager.objects.get(user_id=uid)
        data=Subscribers.objects.all()

        return render(request,"myapp/allsubscribers.html",{'mid':mid,'data':data})

def deletesubscriber(request,pk):
    sid=Subscribers.objects.get(id=pk)
    sid.delete()
    data=Subscribers.objects.all()
    return render(request,"myapp/allsubscribers.html",{'data':data})


def subscribed(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        new_id=Products.objects.order_by('id').reverse()[0:3]

        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()

        return render(request,"myapp/subscribed.html",{'new_id':new_id,'uid':uid,'count':count})
    else:
        new_id=Products.objects.order_by('id').reverse()[0:3]
        return render(request,"myapp/subscribed.html",{'new_id':new_id})


def pushmessage(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])

    try:
        pushsubject=request.POST['pushsubject']
        pushmsg=request.POST['pushmsg']
        msg=pushmsg
        subject=pushsubject
        print(msg,subject)
        data=Subscribers.objects.all()
        subscriberlist=[]
        for i in data:
            subscriberlist.append(i.email)

        print(subscriberlist)
        send_mail(subject,msg,"k.kaveriie@gmail.com",subscriberlist)

        s_msg="Successfully sent push message!"
        mid=Manager.objects.get(user_id=uid)
        return render(request,"myapp/allsubscribers.html",{'data':data,'s_msg':s_msg,'uid':uid,'mid':mid})
    except:
        data=Subscribers.objects.all()
        e_msg="Sorry.. there was an error.."
        return render(request,"myapp/allsubscribers.html",{'data':data,'e_msg':e_msg})


def addtowishlist(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        pid=Products.objects.get(id=pk)
        cid=Customer.objects.get(user_id=uid)
        wid=Wishlist.objects.create(c_id=cid,p_id=pid)
        count=Cart.objects.filter(c_id=cid).count()
        data=Wishlist.objects.filter(c_id=cid)
        wcount=Wishlist.objects.filter(c_id=cid).count()

        return render(request,"myapp/wishlist.html",{'pid':pid,'cid':cid,'uid':uid,'wid':wid,'count':count,'data':data,'wcount':wcount})
    else:            
        pid=Products.objects.get(id=pk)
        return render(request,"myapp/wishlist.html",{'pid':pid})

def wishlist(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()
        data=Wishlist.objects.filter(c_id=cid)
        wcount=Wishlist.objects.filter(c_id=cid).count()
        ocount=Billing.objects.filter(c_id=cid).count()

        return render(request,"myapp/wishlist.html",{'cid':cid,'uid':uid,'count':count,'data':data,'wcount':wcount,'ocount':ocount})
    else:            
        return render(request,"myapp/wishlist.html")


def removefromwishlist(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()

        wid=Wishlist.objects.get(id=pk)
        wid.delete()
        data=Wishlist.objects.filter(c_id=cid)
        wcount=Wishlist.objects.filter(c_id=cid).count()

        return render(request,"myapp/wishlist.html",{'data':data,'wcount':wcount,'cid':cid,'uid':uid,'count':count,'wcount':wcount})
    else:
        return render(request,"myapp/wishlist.html")



def addcoupon(request):
    return render(request,"myapp/addcoupon.html")

def updatecoupon(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        couponcode=request.POST['couponcode']
        coupondesc=request.POST['coupondesc']
        couponamt=request.POST['couponamt']
        couponid=Coupon.objects.create(couponcode=couponcode,coupondesc=coupondesc,couponamt=couponamt)

        cdata=Coupon.objects.all()
        return render(request,"myapp/allcoupon.html",{'couponid':couponid,'cdata':cdata})

def allcoupon(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Manager.objects.filter(user_id=uid)
        cdata=Coupon.objects.all()
        return render(request,"myapp/allcoupon.html",{'cdata':cdata,'uid':uid,'mid':mid})
    else:
        return render(request,"myapp/allcoupon.html")


def deletecoupon(request,pk):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Manager.objects.filter(user_id=uid)

        coupon_id=Coupon.objects.get(id=pk)
        coupon_id.delete()
        cdata=Coupon.objects.all()
        return render(request,"myapp/allcoupon.html",{'cdata':cdata,'mid':mid,'uid':uid})
    else:
        return render(request,"myapp/allcoupon.html")



def applycoupon(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        cart_id=Cart.objects.filter(c_id=cid)
        count=Cart.objects.filter(c_id=cid).count()
        data=Cart.objects.all()
        wcount=Wishlist.objects.filter(c_id=cid).count()

        cart_total=0
        new_total=0
        for i in cart_id:
            cart_total+=int(i.product_total)

        new_total=cart_total
        usercode=request.POST['usercode']
        coupon_id=Coupon.objects.filter(couponcode=usercode)


        if coupon_id:
            msg="Successfully applied coupon"
            discount=coupon_id[0].couponamt
            new_total=cart_total*discount
        else:
            msg="Invalid coupon"

        cid.billamt=new_total
        cid.save()


        return render(request,"myapp/cart.html",{'uid':uid,'cid':cid,'cart_id':cart_id,'data':data,'count':count,'wcount':wcount,'cart_total':cart_total,'msg':msg,'coupon_id':coupon_id,'new_total':new_total})
    else:
        return render(request,"myapp/cart.html")


def removecoupon(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        cart_id=Cart.objects.filter(c_id=cid)
        count=Cart.objects.filter(c_id=cid).count()
        data=Cart.objects.all()
        wcount=Wishlist.objects.filter(c_id=cid).count()


        cart_total=0
        for i in cart_id:
            cart_total+=int(i.product_total)
        new_total=cart_total

        cid.billamt=new_total
        cid.save()


        return render(request,"myapp/cart.html",{'uid':uid,'cid':cid,'cart_id':cart_id,'data':data,'count':count,'wcount':wcount,'cart_total':cart_total,'new_total':new_total})
    else:
        return render(request,"myapp/cart.html")




def savebilling(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        count=Cart.objects.filter(c_id=cid).count()
        cart_id=Cart.objects.filter(c_id=cid)
        wcount=Wishlist.objects.filter(c_id=cid).count()
        cart_total=0
        for i in cart_id:
            cart_total+=int(i.product_total)            
    try:
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        country=request.POST['country']
        address=request.POST['address']
        city=request.POST['city']
        zipcode=request.POST['zipcode']
        phoneno=request.POST['phoneno']
        comment=request.POST['comment']
            
        bid=Billing.objects.create(c_id=cid,fname=fname,lname=lname,email=email,country=country,address=address,city=city,zipcode=zipcode,phoneno=phoneno,comment=comment)
        billmsg="Billing details saved. You can now place the order!"

        if cart_total>cid.billamt:
            disc=float(cart_total-(cid.billamt))
            dmsg="Discount from Coupon"
            return render(request,"myapp/checkout.html",{'bid':bid,'billmsg':billmsg,'uid':uid,'cid':cid,'count':count,'cart_id':cart_id,'wcount':wcount,'cart_total':cart_total,'dmsg':dmsg,'disc':disc})
        else:
            return render(request,"myapp/checkout.html",{'bid':bid,'billmsg':billmsg,'uid':uid,'cid':cid,'count':count,'cart_id':cart_id,'wcount':wcount,'cart_total':cart_total})
    except:
        billmsg="Error in saving billing details.."
        return render(request,"myapp/checkout.html",{'billmsg':billmsg,'uid':uid,'cid':cid,'count':count,'cart_id':cart_id,'wcount':wcount,'cart_total':cart_total})


def placeorder(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        cart_id=Cart.objects.filter(c_id=cid)
        cart_total=0
        for i in cart_id:
            cart_total+=int(i.product_total)
        
        billsid=Billing.objects.filter(c_id=cid).order_by('id').reverse()[0:1]
        lastbid=billsid[0].id
        bid=Billing.objects.get(id=lastbid)

        
        expecteddelivery=datetime.now()+timedelta(weeks=2)

        x=expecteddelivery.strftime("%Y-%m-%d")

        for i in cart_id:
            oid=Order.objects.create(b_id=bid,c_id=cid,p_id=i.p_id,expecteddelivery=x)

        if cart_total>cid.billamt:
            disc=float(cart_total-(cid.billamt))
            dmsg="Discount from Coupon"
            return render(request,"myapp/orderplaced.html",{'oid':oid,'bid':bid,'uid':uid,'cid':cid,'cart_id':cart_id,'cart_total':cart_total,'disc':disc,'dmsg':dmsg,'expecteddelivery':expecteddelivery})

        else:
            return render(request,"myapp/orderplaced.html",{'oid':oid,'bid':bid,'uid':uid,'cid':cid,'cart_id':cart_id,'cart_total':cart_total,'expecteddelivery':expecteddelivery})



def orderplaced(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        cart_id=Cart.objects.filter(c_id=cid)
        cart_total=0
        for i in cart_id:
            cart_total+=int(i.product_total)
        
        billsid=Billing.objects.filter(c_id=cid).order_by('id').reverse()[0:1]
        lastbid=billsid[0].id
        bid=Billing.objects.get(id=lastbid)

        ordersid=Order.objects.filter(c_id=cid).order_by('id').reverse()[0:1]
        lastorder=ordersid[0].id
        oid=Order.objects.get(id=lastorder)

        if cart_total>cid.billamt:
            disc=float(cart_total-(cid.billamt))
            dmsg="Discount from Coupon"
            return render(request,"myapp/orderplaced.html",{'oid':oid,'bid':bid,'uid':uid,'cid':cid,'cart_id':cart_id,'cart_total':cart_total,'disc':disc,'dmsg':dmsg})
        else:                    
            return render(request,"myapp/orderplaced.html",{'oid':oid,'bid':bid,'uid':uid,'cid':cid,'cart_id':cart_id,'cart_total':cart_total})


def myorders(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Customer.objects.get(user_id=uid)
        oid=Order.objects.filter(c_id=cid)
        bid=Billing.objects.filter(c_id=cid)


        count=Cart.objects.filter(c_id=cid).count()
        wcount=Wishlist.objects.filter(c_id=cid).count()
        ocount=Billing.objects.filter(c_id=cid).count()



        return render(request,"myapp/myorders.html",{'oid':oid,'bid':bid,'uid':uid,'cid':cid,'count':count,'ocount':ocount,'wcount':wcount})

    




def allorders(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Manager.objects.get(user_id=uid)
        orderdata=Order.objects.all()
        return render(request,"myapp/allorders.html",{'uid':uid,'mid':mid,'orderdata':orderdata})
    else:
        return render(request,"myapp/allmessages.html")

    
def editorderstatus(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        mid=Manager.objects.get(user_id=uid)
    
    
        id=request.POST['id']
        status=request.POST['status']


        oid=Order.objects.get(id=id)
        oid.status=status
        oid.save()
        orderdata=Order.objects.all()

        return render(request,"myapp/allorders.html",{'uid':uid,'mid':mid,'orderdata':orderdata,'oid':oid})

