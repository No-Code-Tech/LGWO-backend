from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from user.utils import create_custom_permission,add_permission_to_group


'''
only ADMIN,MANAGER,HR can create user

required group
    admin,manager,supervisor
'''



class Command(BaseCommand):
    help = "Create groups and permissions"
    def handle(self,*args,**kwargs):

        group_permissions = {
            "Supervisor":
                [{"codename":"timesheet_verification","name":"User can verify TimeSheet"},
                {"codename":"create_timesheet","name":"User can create TimeSheet"},]
        
           
        }


        for group_name,perms in group_permissions.items():
            print(group_name)
            for perm in perms:
                codename = perm["codename"]
                name = perm["name"]
                perm_obj = create_custom_permission(codename=codename,name=name)
                add_permission_to_group(permission=perm_obj,group_name=group_name)





