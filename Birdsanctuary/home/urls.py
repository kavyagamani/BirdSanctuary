from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   
     path('',views.index, name='index'),
     path('zoo',views.zoo, name='zoo'),

     path('admin_home',views.admin_home, name='admin_home'),
     path('user_home',views.user_home, name='user_home'),

     path('info',views.info, name='info'),
     path('tickets',views.tickets, name='tickets'),
     path('gallery',views.gallery, name='gallery'),
     path('contact',views.contact, name='contact'),
     path('login',views.login,name='login'),
     path('live',views.live,name='live'),
     path('reg/',views.reg,name='reg'),
     path('add_birds/',views.add_birds,name='add_birds'),
     path('take_app/',views.take_app,name='take_app'),
     path('generate_tic/',views.generate_tic,name='generate_tic'),
     path('birds_category/',views.birds_category,name='birds_category'),
     path('reg1/',views.reg1,name='reg1'),
     #view paths
     path('reg_view/',views.reg_view,name='reg_view'),
     path('my_ticket/',views.my_ticket,name='my_ticket'),
     path('take_app_search/',views.take_app_search,name='take_app_search'),
     path('take_app_status/',views.take_app_status,name='take_app_status'),
     path('add_bird_view/',views.add_bird_view,name='add_bird_view'),
     path('take_app_view/',views.take_app_view,name='take_app_view'),
     path('generate_view/',views.generate_view,name='generate_view'),
     path('bird_cat_view/',views.bird_cat_view,name='bird_cat_view'),
     #del paths
     path('add_bird_del/<int:pk>',views.add_bird_del,name='add_bird_del'),
     path('bird_cat_del/<int:pk>',views.bird_cat_del,name='bird_cat_del'),
     path('take_app_del/<int:pk>',views.take_app_del,name='take_app_del'),
     path('generate_del/<int:pk>',views.generate_del,name='generate_del'),
     path('register_del/<int:pk>',views.register_del,name='register_del'),
        
     #edit paths
     path('add_bird_edit/<int:pk>',views.add_bird_edit,name='add_bird_edit'),
     path('bird_cat_edit/<int:pk>',views.bird_cat_edit,name='bird_cat_edit'),
     path('generate_tic_edit/<int:pk>',views.generate_tic_edit,name='generate_tic_edit'),
     path('take_app_edit/<int:pk>',views.take_app_edit,name='take_app_edit'),
     path('register_edit/<int:pk>',views.register_edit,name='register_edit'),
       
    #forgot,reset,otp paths
     path('forgotpass/',views.forgotpass,name='forgotpass'),
     path('otp/',views.otp,name='otp'),
     path('resetpass/',views.resetpass,name='resetpass'),
     path('update_status/<int:pk>',views.update_status,name='update_status'),
     path('pay/<int:pk>',views.pay,name='pay'),
     path('view_ticket/<int:pk>',views.view_ticket,name='view_ticket'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)