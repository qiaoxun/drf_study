from rest_framework.versioning import BaseVersioning


class MyVersioning(BaseVersioning):

    def determine_version(self, request, *args, **kwargs):
        return 'v1'
