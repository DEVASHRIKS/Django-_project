from django.shortcuts import render,redirect,HttpResponse
from .models import Customer_Register,Serviceman_Register,Login,Service_Category,Service_City,Booking_Data
from django.contrib import messages
import razorpay

# Create your views here.
# def index(request):
#     return render(request,'index.html')

def index(request):
    if 'admin_id' in request.session:
        x = request.session['admin_id']
        return render(request,'adminhome_new.html')
    elif 'customer_id' in request.session:
        x = request.session['customer_id']
        return render(request,'customer_home.html')
    elif 'serviceman_id' in request.session:
        x = request.session['serviceman_id']
        return render(request,'servicemanhome_new.html')
    else:
        return redirect(log)


# def c_reg(request):
#     return render(request,'customerreg_new.html')

def c_reg(request):
    if request.method == 'POST':
        x1 = request.POST['u1']
        x2 = request.POST['u2']
        x3 = request.POST['u3']
        x4 = request.POST['u4']
        x5 = request.POST['u5']
        x6 = request.FILES['u6']
        x7 = request.POST['u7']
        x8 = request.POST['u8']
        x9 = request.POST['u9']
        x10 = request.POST['u10']
        x11 = request.POST['u11']
        x12 = request.POST['u12']
        x13 = request.POST['u13']
        x14 = request.POST['u14']
        Customer_Register.objects.create(username=x1,c_firstname=x3,c_lastname=x4,c_email=x5,c_image=x6,c_phoneno=x7,c_birthdate=x8,c_streetaddress=x9,c_city=x10,c_state=x11,c_pincode=x12,c_country=x13,c_dbooking=x14)
        Login.objects.create(username=x1,password=x2,status=1)
        return redirect(index)
    else:
        return render(request,'customerreg_new.html')

# def s_reg(request):
#     return render(request,'servicemanreg_new.html')

def s_reg(request):
    if request.method == 'POST':
        x1 = request.POST['s1']
        x2 = request.POST['s2']
        x3 = request.POST['s3']
        x4 = request.POST['s4']
        x5 = request.POST['s5']
        x6 = request.FILES['s6']
        x7 = request.POST['s7']
        x8 = request.POST['s8']
        x9 = request.POST['s9']
        x10 = request.POST['s10']
        x11 = request.POST['s11']
        x12 = request.POST['s12']
        x13 = request.POST['s13']
        x14 = request.POST['s14']
        x15 = request.POST['s15']
        x16 = request.POST['s16']
        x17 = request.POST['s17']
        x18 = request.POST['s18']
        x19 = request.FILES['s19']
        Serviceman_Register.objects.create(username=x1,s_firstname=x3,s_lastname=x4,s_email=x5,s_image=x6,s_phoneno=x7,s_birthdate=x8,s_streetaddress=x9,s_city=x10,s_state=x11,s_pincode=x12,s_country=x13,s_wexp=x14,s_dapp=x15,s_scity=x16,s_typid=x17,s_service=x18,s_idimg=x19,action='pending')
        Login.objects.create(username=x1,password=x2,status=2)
        return redirect(index)
    else:
        a=Service_Category.objects.all()
        b=Service_City.objects.all()
        return render(request,'servicemanreg_new.html',{'a1':a,'b1':b})


def login(request):
    return render(request,'login.html')

def log(request):
    if request.method == 'POST':
        u = request.POST['u']
        p = request.POST['p']
        try:
            data = Login.objects.get(username=u)

            if data.password == p and data.status == 0:
                request.session['admin_id'] = u
                return render(request,'adminhome_new.html')

            elif data.password == p and data.status == 1:
                request.session['customer_id'] = u
                return render(request,'customer_home.html')

            elif data.password == p and data.status == 2:
                request.session['serviceman_id'] = u
                print(u)
                return render(request,'servicemanhome_new.html')

            else:
                messages.info(request, "password incorrect")
                return render(request, "login.html")

        except Exception:
            messages.info(request, "Username incorrect")
            return render(request, "login.html")

    else:
        return render(request,'index.html')




# def c_home(request):
#     return render(request,'customer_home.html')
#
# def s_home(request):
#     return render(request,'serviceman_home.html')
#
# def admin_home(request):
#     return render(request,'admin_home.html')

def admin_logout(request):
    if 'admin_id' in request.session:
        request.session.flush()
        return redirect(log)
    else:
        return redirect(index)

def customer_logout(request):
    if 'customer_id' in request.session:
        request.session.flush()
        return redirect(log)
    else:
        return redirect(index)

def serviceman_logout(request):
    if 'serviceman_id' in request.session:
        request.session.flush()
        return redirect(log)
    else:
        return redirect(index)

#using corret one from here to
# def serviceman_profile_admin(request):
#     if 'serviceman_id' in request.session:
#         x = request.session['serviceman_id']
#         data = Serviceman_Register.objects.get(username=request.session['serviceman_id'])
#         return render(request, 'servicemanprofile_admin.html', {'i': data})
# upto here

#     else:
#         return render(request,'servicemanhome_new.html')
#         # return redirect(index)

# def serviceman_profile(request):
#        if 'serviceman_id' in request.session:
#            data = Serviceman_Register.objects.filter(username=request.session['serviceman_id'])
#            return render(request, 'servicemanprofile_admin.html', {'key': data})


def profile_new(request):
        print("pro")
        x = request.session['serviceman_id']
        print("x is:"+x)
        data = Serviceman_Register.objects.get(username=x)
        print(data)
        return render(request, 'profile_new.html', {'r': data})
def maid_pending(request):
    if request.method == 'GET':
        data= Serviceman_Register.objects.filter(action='pending')
        return render(request,'maid_pending.html',{'r':data})

def approval(request,n):
    if request.method == 'GET':
        data = Serviceman_Register.objects.filter(id=n)
        data.update(action='confirmed')
        return redirect(maid_pending)
    else:
        return render(request, 'maid_pending.html')

def reject(request,n):
    if request.method == 'GET':
        data = Serviceman_Register.objects.filter(id=n)
        data.delete()
        return redirect(maid_pending)
    else:
        return render(request, 'maid_pending.html')

def maid_total(request):
    if request.method == 'GET':
        data= Serviceman_Register.objects.filter(action='confirmed')
        return render(request,'maid_total_new.html',{'r':data})

def user_total(request):
    data= Customer_Register.objects.all()
    return render(request,'user_total.html',{'r':data})

def view_service(request):
    data = Service_Category.objects.all()
    return render(request, 'view_service.html', {'r': data})

def ba_table(request):
    return render(request,'basic_table.html')

def admin_home(request):
    return render(request,'adminhome_new.html')

# def profile_view(request,n):
#     if request.method == 'GET':
#         data = Serviceman_Register.objects.filter(id=n)
#         return redirect('serviceman')
#     else:
#         return render(request, 'maid_pending.html')

def serviceman_profile_admin(request,n):
    if request.method == 'GET':
        print(n)
        data= Serviceman_Register.objects.get(id=n)
        return render(request,'servicemanprofile_admin.html',{'i':data})
    else:
        print("gvhgvgvf")
        return render(request, 'servicemanprofile_admin.html')

# def serviceman_profile_admin(request):
#     print("hai")
#     if 'serviceman_id' in request.session:
#         # x = request.session['serviceman_id']
#         # print(x)
#         data = Serviceman_Register.objects.get(username=request.session['serviceman_id'])
#         print(data)
#         return render(request, 'servicemanprofile_admin.html', {'i': data})
#     else:
#         return render(request, 'servicemanprofile_admin.html')

# def serviceman_profile_admin(request):
#     if 'serviceman_id' in request.session:
#         print("pro")
#         x = request.session['serviceman_id']
#         print("x is:" + x)
#         data = Serviceman_Register.objects.get(username=x)
#         print(data)
#         return render(request, 'servicemanprofile_admin.html', {'i': data})


def services(request):
    return render(request,'services_new.html')


def maid_searching(request):
    if request.method == 'POST':
        x1 = request.POST['n1']
        x2 = request.POST['n2']

        data=Serviceman_Register.objects.filter(s_scity=x1,s_service=x2,action='confirmed')
        if list(data) != []:
            print("uyefuyfuyedg")
            return render(request, 'maid_booking_new.html', {'r': data})
        else:
            return render(request, 'maid_searching_new_2.html', {'message': 'Not Found'})
    else:
        a = Service_City.objects.all()
        b = Service_Category.objects.all()
        return render(request, 'maid_searching_new_2.html', {'a1': a, 'b1': b})


# def maid_booking(request,n):
#        # y=request.GET.get('d')
#        print(n)
#        for i in n:
#            print(i)
#        return render(request,'maid_booking.html',{'r':n})


def new2(request):
    return render(request,'new2.html')

def booking_reg(request,n):
    if request.method == 'POST':
        x1 = request.POST['b1']
        x2 = request.POST['b2']
        x3 = request.POST['b3']
        x4 = request.POST['b4']
        x5 = request.POST['b5']
        x6 = request.POST['b6']
        x7 = request.POST['b7']
        x8 = request.POST['b8']
        x9 = request.POST['b9']
        # b=x9
        # a=x8
        # c=b-a
        x12 = request.POST['b12']
        x10 = request.POST['b10']
        x11 = float(x12) * int(x10)
        request.session['payment_id'] = x11
        print(x5)
        print(x11)
        print(x12,x10)
        Booking_Data.objects.create(c_username=x1,c_email=x2,c_phoneno=x3,s_servicemanname=x4,s_service=x5, s_scity=x6,
                                           serviceman_contact=x7,starting_date=x8, ending_date=x9,no_days=x10,tot_amount=x11,price_per_day=x12,action='pending')
        f=Booking_Data.objects.get(c_username=x1,s_servicemanname=x4)
        print(f.id)
        # f= request.session['customer_id']
        data = Booking_Data.objects.filter(id=f.id)
        print(data)
        return render(request, 'amount_display.html', {'r': data})
    else:
        data1=Customer_Register.objects.filter(username=request.session['customer_id'])
        print(n)
        data2 = Serviceman_Register.objects.filter(id=n)
        s=Serviceman_Register.objects.get(id=n)
        g = s.s_service
        data3=Service_Category.objects.filter(category=g)
        return render(request, 'book_now_reg.html', {'x': data1,'y':data2,'z':data3})

def services_customer(request):
    return render(request,'services_customer.html')

def profile_customer(request):
     print("pro")
     x = request.session['customer_id']
     print("x is:" + x)
     data = Customer_Register.objects.get(username=x)
     print(data)
     return render(request, 'profile_customer.html', {'r': data})

def serviceman_profile_admin_confirmed(request,n):
    if request.method == 'GET':
        print(n)
        data= Serviceman_Register.objects.get(id=n)
        return render(request,'servicemanprofile_admin_confirmed.html',{'i':data})
    else:
        print("gvhgvgvf")
        return render(request, 'servicemanprofile_admin_confirmed.html')

def customer_profile_admin(request,n):
    if request.method == 'GET':
        print(n)
        data= Customer_Register.objects.get(id=n)
        return render(request,'customerprofile_admin.html',{'i':data})
    else:
        print("gvhgvgvf")
        return render(request, 'customerprofile_admin.html')

# def my_order_serviceman(request):
#     data1 = Serviceman_Register.objects.filter(action='confirmed')
#     data2 = Serviceman_Register.objects.filter(action='pending')
#     if x=data1:
#         print("uyefuyfuyedg")
#         return render(request, 'my_order_serviceman.html', {'message': 'You can see your orders'})
#     else:
#         return render(request, 'maid_searching_new_2.html', {'message': 'Not Found'})


def about(request):
    return render(request,'about.html')

def servicemanprofile_update(request):
    if request.method == 'POST':
        x1 = request.POST['s1']
        # x2 = request.POST['s2']
        x3 = request.POST['s3']
        x4 = request.POST['s4']
        x5 = request.POST['s5']
        x6 = request.FILES['s6']
        x7 = request.POST['s7']
        x8 = request.POST['s8']
        x9 = request.POST['s9']
        x10 = request.POST['s10']
        x11 = request.POST['s11']
        x12 = request.POST['s12']
        x13 = request.POST['s13']
        x14 = request.POST['s14']
        x15 = request.POST['s15']
        x16 = request.POST['s16']
        x17 = request.POST['s17']
        x18 = request.POST['s18']
        x19 = request.FILES['s19']
        data=Serviceman_Register.objects.filter(username=request.session['serviceman_id'])
        data.update(username=x1,s_firstname=x3,s_lastname=x4,s_email=x5,s_image=x6,s_phoneno=x7,s_birthdate=x8,s_streetaddress=x9,s_city=x10,s_state=x11,s_pincode=x12,s_country=x13,s_wexp=x14,s_dapp=x15,s_scity=x16,s_typid=x17,s_service=x18,s_idimg=x19)
        return render(request,'servicemanhome_new.html')
    else:
        data1=Serviceman_Register.objects.filter(username=request.session['serviceman_id'])
        return render(request,'servicemanprofile_update.html',{'r':data1})

def payment(request):
    a=request.session['payment_id']
    if request.method=='GET':
        z=request.session['customer_id']
        data = Booking_Data.objects.filter(c_username=z)
        data.update(action='Completed')
    order_currency = 'INR'
    client = razorpay.Client(auth=("rzp_test_SROSnyInFv81S4", "WIWYANkTTLg7iGbFgEbwj4BM"))
    # payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    return render(request, "payment.html",{'b':a})


def view_order_customer(request):
    x = request.session['customer_id']
    data = Booking_Data.objects.filter(c_username=x,action='Completed')
    print(data)
    return render(request, 'view_order_customer.html', {'r': data})

def view_order_serviceman(request):
    x = request.session['serviceman_id']
    data = Booking_Data.objects.filter(s_servicemanname=x,action='Completed')
    print(data)
    return render(request, 'view_order_serviceman.html', {'r': data})

def city_services(request):
    data= Service_City.objects.all()
    return render(request,'view_city.html',{'r':data})

def view_order_admin(request):
    if request.method == 'GET':
        data= Booking_Data.objects.filter(action='Completed')
        return render(request,'view_order_admin.html',{'r':data})