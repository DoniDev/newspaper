from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    # register
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # password change
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password-change'),
    path('password-change-done', auth_views.PasswordChangeDoneView.as_view(template_name ='registration/password_change_done.html'), name='password-change-done'),
    # login&logout
    path('login/', auth_views.LoginView.as_view(template_name ='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='home.html'), name='logout'),
    # password-reset
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
