from rest_framework.authentication import BaseAuthentication


class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request._request.GET.get('token')
        if not token:
            raise Exception("用户认证失败")

        user = {
            'user_id': 1,
            'user_type': request._request.GET.get('user_type'),
        }

        return (user, None)
