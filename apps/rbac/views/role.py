from rest_framework.views import APIView
from rest_framework.response import Response
from rbac.utils.my_permission import MyPermission
from ..models import Role, UserProfile
from ..utils.my_throttle import MySimpleRateThrottle
from rest_framework import serializers


class RoleSerializer(serializers.Serializer):
    type = serializers.IntegerField()
    type_meaning = serializers.CharField(source='get_type_display')
    name = serializers.CharField()
    u_id = serializers.CharField(source='user.id')
    departs = serializers.SerializerMethodField()


    def get_departs(self, row):
        departments = row.department.all()
        print(departments)
        ret = []
        for depart in departments:
            ret.append({'id': depart.id, 'name': depart.name})
        return ret



class RoleModelSerializer(serializers.ModelSerializer):
    type_meaning = serializers.CharField(source='get_type_display')
    user1 = serializers.HyperlinkedIdentityField(view_name='user', lookup_field='user_id', lookup_url_kwarg='pky')

    class Meta:
        model = Role
        fields = '__all__'
        depth = 0


class RoleView(APIView):

    # permission_classes = (MyPermission, )
    permission_classes = ()
    throttle_classes = ()

    def get(self, request):
        role_set = Role.objects.all()
        role_seri = RoleModelSerializer(instance=role_set, many=True, context={'request': request})
        return Response(role_seri.data)

    def post(self, request):
        print(request.data)
        return Response('POST')


