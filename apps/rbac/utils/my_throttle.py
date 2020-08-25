from rest_framework.throttling import BaseThrottle, SimpleRateThrottle

ident_dict = {}


class MyThrottle(BaseThrottle):

    def allow_request(self, request, view):
        ident = self.get_ident(request)
        if ident in ident_dict:
            nums = ident_dict.get(ident, 1)
            if nums > 5:
                return False
            else:
                ident_dict[ident] = nums + 1
                return True
        else:
            ident_dict[ident] = 1
            return True


class MySimpleRateThrottle(SimpleRateThrottle):
    scope = 'Test'

    def get_cache_key(self, request, view):
        ident = self.get_ident(request)
        return ident


