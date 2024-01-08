"""
URL configuration for maid_servicepro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  django.conf import settings
from django.conf.urls.static import static
from maid_serviceapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('services',views.services),
    path('about',views.about),

    #registration
    path('c_reg',views.c_reg),
    path('s_reg',views.s_reg),

    #login
    path('login',views.login),
    path('log',views.log),

    #customerhome
    # path('c_home',views.c_home),
    #
    #  #servicemanhome
    # path('s_home',views.s_home),
    #
    # #adminhome
    # path('admin_home',views.admin_home),

    #logout
    path('admin_out',views.admin_logout),
    path('customer_out',views.customer_logout),
    path('serviceman_out',views.serviceman_logout),

    #profile
    path('profile_new',views.profile_new),
    # path('profile',views.profile),

    #total active maids&user
    path('confirm',views.maid_total),
    path('user_total',views.user_total),

    #maid pending
    path('maid_pending',views.maid_pending),
    path('approve/<n>', views.approval),
    path('reject/<n>', views.reject),

    #viewservice
    path('view_service',views.view_service),
    path('view_city',views.city_services),
    path('bt',views.ba_table),

    #adminhome
    path('adhome',views.admin_home),
    path('serviceman_pro/<n>',views.serviceman_profile_admin),
    path('serviceman_pro_confirmed/<n>',views.serviceman_profile_admin_confirmed),
    path('customer_pro/<n>',views.customer_profile_admin),
    path('view_order_admin',views.view_order_admin),


    path('maid_searching',views.maid_searching),
    # path('maid_booking/<n>',views.maid_booking,name='d')
    path('new2',views.new2),

    #booking
    path('booking/<n>',views.booking_reg),
    # path('amount_display/<n>',views.amount_display),


    #customerhome
    path('services_customer',views.services_customer),
    path('profile_customer',views.profile_customer),
    path('view_order_customer',views.view_order_customer),

    #serviceman profile update
    path('servicemanprofile_update',views.servicemanprofile_update),
    path('view_order_serviceman',views.view_order_serviceman),

    #serviceman home
    #payment
    path('payment',views.payment)

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)