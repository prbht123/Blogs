from django.urls import path,include,re_path
#from django.urls import include, url

from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
app_name = "account"
urlpatterns = [
    path('login/',LoginView.as_view(template_name='registration/sign.html'),name="signin"),
    path('logout/',LogoutView.as_view(template_name='registration/signout.html'),name="logout"),
    path('passwordchange/',PasswordChangeView.as_view(template_name='account/registration/password_change_form.html'),name="password_change"),
    # path('passwordchangedone/',PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'),name="password_change_done"),
    
    path('passwordreset/',PasswordResetView.as_view(template_name='registration/password_reset.html'),name="password_reset"),
    path('passwordresetdone/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name="password_reset_done"),
    #path('passwordresetconfirm/<str:uuid>/<str:token>',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name="password_reset_confirm"),
    #re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',email_template_name = 'registration/password_reset_email.html'),name="password_reset_confirm"),
    
    # path('passwordresetcomplete/',PasswordResetCompleteView.as_view(template_name='account/registration/password_reset_complete.html'),name="password_reset_complete"),
    path('register/',views.register, name='register'),

]