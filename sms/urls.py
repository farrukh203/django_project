from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.StdRegisterView.as_view() , name='register'),
    path('std-update/<int:pk>', views.StRegistrationUpdateView.as_view(), name='update_data'),
    path('std-delete/<int:pk>', views.StRegistrationDeleteView.as_view(), name='delete_data'),
    path('singup/', views.SingUpView.as_view(), name='singup'),
    path('user-login/', views.UserLoginView.as_view(), name='userlogin'),
    path('logout/', views.user_logout_view, name='logout'),
    path('changepassword/', views.ChangePasswordView.as_view(), name='changepassword'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
