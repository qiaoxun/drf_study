from rest_framework.views import APIView
from rest_framework.response import Response
from rbac.utils.my_authentication import MyAuthentication
from rbac.utils.my_permission import MyPermission
from rbac.utils.my_throttle import MyThrottle, MySimpleRateThrottle
from rbac.utils.my_versioning import MyVersioning
from rbac.models import UserProfile
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class UserAuthView(APIView):

    # authentication_classes = (MyAuthentication,)
    permission_classes = (MyPermission, )
    throttle_classes = (MySimpleRateThrottle, )
    # authentication_classes = ()
    versioning_class = MyVersioning

    def get(self, request, **kwargs):
        print(request.user)
        user = UserProfile.objects.all().first()
        user_seria = UserSerializer(user, many=False)
        return Response(user_seria.data)

    def post(self, request):
        print(request.data)
        return Response('POST')


