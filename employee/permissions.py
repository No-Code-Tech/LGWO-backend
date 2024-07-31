from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser





class IsInGroup(permissions.BasePermission):
    group_name = None
    def has_permission(self, request, view):
        return request.user and request.user.group.filter(name=self.group_name).exists()



class GroupRequiredMixin: 
    group_name = None
    def get_permission(self):   
        print("Here")
        class GroupRequiredPermission(IsInGroup):
            def __init__(self):
                self.group_name = self.group_name
        print("it was here")
        permission_classes = super().get_permissions()

        permission_classes.append(GroupRequiredPermission())     

        return permission_classes
        


'''
super_user; 
    --permission_y
    --permission_x
manager;
    --permission_x
    --permission_to_validate
team_leader->xyz_group
+add more
'''


