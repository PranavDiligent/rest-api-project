from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('students',views.student_list,name="student_list"),
    path('users',views.SignupApiView.as_view(),name="signup"),
    path('students/<int:id>',views.student_edit,name="student_list"),
    path('auth',obtain_auth_token),
    
]