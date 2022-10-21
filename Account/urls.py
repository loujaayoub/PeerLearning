from django.urls import path
from . import views 
urlpatterns = [
    path('login',views.login_page, name ='login'),
    path('register',views.register_page, name ='register'),
    path('logout',views.logout_user, name ='logout'),
    path('forgetPassword',views.forget_password, name ='forgetPassword'),


    # path('detection_result',views.detection_result, name ='detection-result')
]
