from django.utils.deprecation import MiddlewareMixin
from django.http import Http404
# from django.contrib.auth.models import User
class AdminUrlBlocker(MiddlewareMixin):
    def process_request(self,request):
        if request.path.startswith("/admin") or request.path.startswith(""):
            user = request.user
            if not user.is_authenticated:
                return Http404()
            if not user.is_staff or not user.is_superuser:
                return Http404()
            return None
            