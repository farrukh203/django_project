from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.StdRegisterView.as_view() , name='register'),
    path('std-update/<int:pk>', views.StRegistrationUpdateView.as_view(), name='update_data'),
    path('std-delete/<int:pk>', views.StRegistrationDeleteView.as_view(), name='delete_data'),
]
