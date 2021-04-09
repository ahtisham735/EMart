from .models import User
def isUserLogin(request):
    if 'user' in request.session:
        user=User.objects.get(username=request.session['user'])
        return user
    else:
        return None