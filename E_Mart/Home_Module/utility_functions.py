from .models import User
def isUserLogin(request,name):
    if name in request.session:
        user=User.objects.get(username=request.session[name])
        return user
    else:
        return None