from django.urls import path
from .views import home, StudentSignUpView, dashboard, dashboard_teacher, TeacherSignUpView

name = 'tests'

urlpatterns = [
    path('', home, name='home'),
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard_teacher', dashboard_teacher, name='dashboard_teacher'),
    path('student/', StudentSignUpView.as_view(), name='student'),
    path('teacher/', TeacherSignUpView.as_view(), name='teacher'),

]