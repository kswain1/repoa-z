from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdatePlayerProfile(permissions.BasePermission):
    """allows the trainer to add new information to their athelte"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.trainer_profile.id == request.user.id


class UpdatePlayerSession(permissions.BasePermission):
    """alllows trainers to update the players permissions"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.trainer_profile.id == request.user.id

class UpdateMVC(permissions.BasePermission):
    """allows trainer to update player profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

class UpdateMVCLog(permissions.BasePermission):
    """allows trainers to update their player profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_id.id == request.user.id
class UpdatePlayerProfile(permissions.BasePermission):
    """ allows trainer to upate player profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_id.id == request.user.id

class UserProfileAuthenticate(permissions.BasePermission):
    """allows users to authenticate their profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.id == request.user.id