from django.http import HttpResponseForbidden
from functools import wraps

def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("You do not have permission to view this page <br><a href='http://127.0.0.1:8000/'>home</a> - <a href='http://127.0.0.1:8000/accounts/login'>login</a>")
    
    return _wrapped_view
