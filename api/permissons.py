from rest_framework import permissions


# =================================================================
# *** accounts ***
class UserPermissionUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return (
                request.user.is_superuser
            )  # Only allow the owner of the pet to update or delete it
        return True


# =================================================================
# *** skills ***
# class SkillsPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if view.action == "create":
#             return (
#                 request.user.is_authenticated
#             )  # Only allow authenticated users to create pets
#         else:
#             return True  # Deny all other actions

#     def has_object_permission(self, request, view, obj):
#         if view.action in ["destroy", "partial_update", "update"]:
#             return (
#                 obj.owner == request.user
#             )  # Only allow the owner of the pet to update or delete it
#         else:
#             return True


# =================================================================
# *** AboutMe ***
class AboutMePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return (
                request.user.is_authenticated
            )  # Allow only authenticated users to create skills
        return True  # Allow all other actions

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update", "destroy"]:
            return (
                request.user.is_authenticated
            )  # Example: Only authenticated users can update/delete skills
        return True  # Read permissions are allowed for any request


# =================================================================
# *** skills -2 ***
class SkillPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return (
                request.user.is_authenticated
            )  # Allow only authenticated users to create skills
        return True  # Allow all other actions

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update", "destroy"]:
            return (
                request.user.is_authenticated
            )  # Example: Only authenticated users can update/delete skills
        return True  # Read permissions are allowed for any request


# =================================================================
# *** Experience ***
class ExperiencePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return (
                request.user.is_authenticated
            )  # Allow only authenticated users to create skills
        return True  # Allow all other actions

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update", "destroy"]:
            return (
                request.user.is_authenticated
            )  # Example: Only authenticated users can update/delete skills
        return True  # Read permissions are allowed for any request


# =================================================================
# *** Experience ***
class ServicesPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return (
                request.user.is_authenticated
            )  # Allow only authenticated users to create skills
        return True  # Allow all other actions

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update", "destroy"]:
            return (
                request.user.is_authenticated
            )  # Example: Only authenticated users can update/delete skills
        return True  # Read permissions are allowed for any request


# =================================================================
# *** Experience ***
class MyWorkPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == "create":
            return (
                request.user.is_authenticated
            )  # Allow only authenticated users to create skills
        return True  # Allow all other actions

    def has_object_permission(self, request, view, obj):
        if view.action in ["update", "partial_update", "destroy"]:
            return (
                request.user.is_authenticated
            )  # Example: Only authenticated users can update/delete skills
        return True  # Read permissions are allowed for any request


# =================================================================
# ***  ***
