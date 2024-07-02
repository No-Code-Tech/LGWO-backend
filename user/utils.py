from django.contrib.auth.models import Permission,Group
from django.contrib.contenttypes.models import ContentType

def create_custom_permission(codename,name):
    content_type = ContentType.objects.get_for_model(Permission)
    permission,created = Permission.objects.get_or_create(
        codename=codename,name=name,content_type=content_type
    )
    return permission



def add_permission_to_group(group_name,permission):
    group,created = Group.objects.get_or_create(name=group_name)
    group.permissions.add(permission)
    return group




