from django.shortcuts import redirect


class CheckPermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.session.get('is_authorized') and (
            request.path != '/permission/'
        ):

            return redirect('permission_access_app')
        response = self.get_response(request)
        return response
