from rest_framework.views import APIView
from rest_framework.response import Response
from rbac.models import Department
from rest_framework import serializers


class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class DepartmentView(APIView):

    authentication_classes = ()
    permission_classes = ()
    throttle_classes = ()

    def get(self, request, **kwargs):
        print(request.user)
        depart = Department.objects.all().first()
        depart_seria = DepartmentSerializer(depart, many=False)
        return Response(depart_seria.data)

    def post(self, request):
        print(request.data)
        return Response('POST')


