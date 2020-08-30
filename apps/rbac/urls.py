from django.urls import path, re_path

from .views import user, role, department

urlpatterns = [
    re_path(r'user/(?P<pky>\d+)$', user.UserAuthView.as_view(), name="user"),
    path('role/', role.RoleView.as_view()),
    re_path(r'^department/(?P<pky>\d+)$', department.DepartmentView.as_view(), name='department'),
    re_path(r'^department1/', department.DepartmentView.as_view(), name='department'),
]

