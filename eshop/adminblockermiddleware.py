from django.utils.deprecation import MiddlewareMixin
from django.http import Http404
class AdminUrlBlocker(MiddlewareMixin):
    def process_request(self,request):
        if request.path.startswith("/admin") or request.path.startswith(""):
            user = request.user
            if not user.is_authenticated:
                raise Http404("you dont have access to this page")
            if not user.is_staff or not user.is_superuser:
                raise Http404("you dont have access to this page")
            return None
            