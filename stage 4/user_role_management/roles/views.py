import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Role
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def role_list_create(request):
    """
    Handle listing all roles and creating a new role.
    """

    if request.method == 'GET':
        search = request.GET.get('search', '')

        if search:
            roles = Role.objects.filter(
                roleName__icontains=search
            )
        else:
            roles = Role.objects.all()

        role_list = []

        for role in roles:
            role_list.append({
                'id': role.id,
                'roleName': role.roleName,
                'accessModules': role.accessModules,
                'createdAt': role.createdAt,
                'active': role.active,
            })

        return JsonResponse(role_list, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)

        role = Role.objects.create(
            roleName=data['roleName'],
            accessModules=data.get('accessModules', []),
            active=data.get('active', True)
        )

        return JsonResponse({
            'message': 'Role created successfully',
            'id': role.id
        }, status=201)

    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)

@csrf_exempt
def role_detail(request, role_id):
    """
    Retrieve, update, or delete a specific role.
    """

    try:
        role = Role.objects.get(id=role_id)
    except Role.DoesNotExist:
        return JsonResponse({
            'error': 'Role not found'
        }, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'id': role.id,
            'roleName': role.roleName,
            'accessModules': role.accessModules,
            'createdAt': role.createdAt,
            'active': role.active,
        })

    elif request.method == 'PUT':
        data = json.loads(request.body)

        role.roleName = data.get('roleName', role.roleName)
        role.accessModules = data.get(
            'accessModules',
            role.accessModules
        )
        role.active = data.get('active', role.active)

        role.save()

        return JsonResponse({
            'message': 'Role updated successfully'
        })

    elif request.method == 'DELETE':
        role.delete()

        return JsonResponse({
            'message': 'Role deleted successfully'
        })

    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)    
    
@csrf_exempt
def add_module(request, role_id):
    """
    Add a unique access module to a role.
    """

    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method not allowed'
        }, status=405)

    try:
        role = Role.objects.get(id=role_id)
    except Role.DoesNotExist:
        return JsonResponse({
            'error': 'Role not found'
        }, status=404)

    data = json.loads(request.body)
    module = data.get('module')

    if not module:
        return JsonResponse({
            'error': 'Module is required'
        }, status=400)

    if module in role.accessModules:
        return JsonResponse({
            'error': 'Module already exists'
        }, status=400)

    role.accessModules.append(module)
    role.save()

    return JsonResponse({
        'message': 'Module added successfully',
        'accessModules': role.accessModules
    })
@csrf_exempt
def remove_module(request, role_id):
    """
    Remove an access module from a role.
    """

    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method not allowed'
        }, status=405)

    try:
        role = Role.objects.get(id=role_id)
    except Role.DoesNotExist:
        return JsonResponse({
            'error': 'Role not found'
        }, status=404)

    data = json.loads(request.body)
    module = data.get('module')

    if not module:
        return JsonResponse({
            'error': 'Module is required'
        }, status=400)

    if module not in role.accessModules:
        return JsonResponse({
            'error': 'Module not found'
        }, status=404)

    role.accessModules.remove(module)
    role.save()

    return JsonResponse({
        'message': 'Module removed successfully',
        'accessModules': role.accessModules
    })    