"""hotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from works import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('loginadmin',views.loginadmin,name='loginadmin'),
    path('loginadmin1',views.loginadmin1,name='loginadmin1'),
    path('explore',views.explore,name='explore'),
    path('login',views.login,name='login'),
    path('login1',views.login1,name='login1'),
    path('login2',views.login2,name='login2'),
    path('login3',views.login3,name='login3'),
    path('logout',views.logout,name='logout'),
    path('adminout',views.adminout,name='adminout'),
    path('signup',views.signup,name='signup'),
    path('contact',views.contact,name='contact'),
    path('contact1',views.contact1,name='contact1'),
    path('feedback',views.feedback,name='feedback'),
    path('signup1',views.signup1,name='signup1'),
    path('rooms',views.rooms,name='rooms'),
    path('book',views.book,name='book'),
    path('book1',views.book1,name='book1'),
    path('booking',views.booking,name='booking'),
    path('viewadmin',views.viewadmin,name='viewadmin'),
    path('deladmin/<int:id>', views.deladmin, name='deladmin'),

    path('adminregister',views.adminregister,name='adminregister'),
    path('adminregister1',views.adminregister1,name='adminregister1'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('customers', views.customers, name='customers'),
    path('bookings', views.bookings, name='bookings'),
    path('places',views.places,name='places'),
    path('place1',views.place1,name='place1'),
    path('delplace/<int:id>', views.delplace, name='delplace'),
    path('status/<int:id>',views.status,name='status'),
    path('cancel/<int:id>', views.cancel, name='cancel'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('payment/payment1', views.payment1, name='payment1'),
]
