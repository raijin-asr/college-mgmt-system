from functools import wraps
from django.shortcuts import redirect


def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        request = args[1]
        user_session = request.session.get("current_user", None)
        print("user session", user_session)
        # current_user = session.get("current_user", None)
        # # print(request.url)
        if user_session == None:
            return redirect("/login")

        return f(*args, **kwargs)
    return decorated_function