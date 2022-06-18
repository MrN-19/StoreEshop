from django.utils.deprecation import MiddlewareMixin
from django.http import Http404

class AdminPanelBlock(MiddlewareMixin):
    def process_request(self,request):
        if request.path.startswith("/admin"):
            user = request.user
            if user.is_authenticated:
                if not user.is_staff:
                    # raise Http404()
                    pass
                return None
            # raise Http404()
        return None
