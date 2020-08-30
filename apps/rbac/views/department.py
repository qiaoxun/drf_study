from rest_framework.views import APIView
from rest_framework.response import Response
from rbac.models import Department
from rest_framework import serializers


# class DepartmentSerializer(serializers.Serializer):
#     id = serializers.IntegerField(max_value=100, min_value=1, error_messages={'invalid': '必须是合法数字'})
#     name = serializers.CharField(max_length=10, min_length=1, allow_blank=False,
#                                  error_messages={'required': '必填字段.', 'blank': '不能为空'})
#
#     def validate_name(self, value):
#         if not value.startswith('Joey'):
#             raise serializers.ValidationError('Name should be start with %s' % 'Joey')

class NameValidate(object):
    def __init__(self, starts_with):
        self.starts_with = starts_with

    def __call__(self, value):
        if not value.startswith(self.starts_with):
            raise serializers.ValidationError('Name should be start with %s' % self.starts_with)

class DepartmentSerializer(serializers.Serializer):
    id = serializers.IntegerField(max_value=100, min_value=1, error_messages={'invalid': '必须是合法数字'})
    name = serializers.CharField(max_length=10, min_length=1, allow_blank=False,
                                 error_messages={'required': '必填字段.', 'blank': '不能为空'}, validators=[NameValidate('Jack')])


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
        ser = DepartmentSerializer(data=request.data)
        if ser.is_valid():
            print(ser)
        else:
            raise Exception(ser.errors)
        return Response('POST')


