from rest_framework.permissions import BasePermission, SAFE_METHODS


def make_payment(request):
    #
    pass


class IsStudentOrIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_staff or request.user.is_student)

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or (request.user.is_authenticated and obj.user == request.user)


class ReadOnlyOrIsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_staff or request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or request.method in SAFE_METHODS
