from .models import PanierItem, Favori


def cart_count(request):
    session_key = request.session.session_key
    if session_key:
        count = PanierItem.objects.filter(session_key=session_key).count()
    else:
        count = 0
    return {'cart_count': count}


def favorites_count(request):
    if request.user.is_authenticated:
        count = Favori.objects.filter(utilisateur=request.user).count()
    else:
        count = 0
    return {'favorites_count': count}
