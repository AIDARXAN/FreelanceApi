from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.customer == request.user


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.group == '1'
