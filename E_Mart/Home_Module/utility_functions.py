from .models import User
from django.contrib import auth,messages
def isUserLogin(request,name):
    if name in request.session:
        user=User.objects.get(username=request.session[name])
        return user
    else:
        return None
def permission_check(request):
    user=isUserLogin(request,'user')
    if user is None:
        user=request.user
    if not user.is_authenticated or user.is_admin:
        messages.error(request,"You must login first to access this page")
        return None
    else:
        return user
     
