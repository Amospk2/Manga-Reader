


def check_if_has_user_activate(request):
    return request.user if request.user.is_authenticated else None