import json
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

from .models import User
from roles.models import Role


@csrf_exempt
def user_list_create(request):
    """
    Handle listing all users and creating a new user.
    """

    # GET - List all users
    if request.method == 'GET':
        
        search = request.GET.get('search', '')

        users = User.objects.select_related('role').filter (
            Q(firstName__icontains=search) |
            Q(lastName__icontains=search) |
            Q(email__icontains=search) 
        )
        
        user_list = []

        for user in users:
            user_list.append({
                'id': user.id,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'email': user.email,
                'role': {
                    'roleName': user.role.roleName if user.role else None,
                    'accessModules': user.role.accessModules
                    if user.role else []
                }
            })

        return JsonResponse(user_list, safe=False)

    # POST - Create a new user
    elif request.method == 'POST':

        try:
            data = json.loads(request.body)

            role = Role.objects.get(id=data['role'])

            user = User(
                firstName=data['firstName'],
                lastName=data['lastName'],
                email=data['email'],
                role=role
            )

            user.set_password(data['password'])

            # Django's built-in model validation
            user.full_clean()

            user.save()

            return JsonResponse({
                'message': 'User created successfully',
                'id': user.id
            }, status=201)

        except Role.DoesNotExist:
            return JsonResponse({
                'error': 'Role not found'
            }, status=404)

        except (KeyError, json.JSONDecodeError):
            return JsonResponse({
                'error': 'Invalid or missing data'
            }, status=400)

    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)
    
@csrf_exempt
def user_detail(request, user_id):
    """
    Retrieve, update, or delete a specific user.
    """

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': 'User not found'
        }, status=404)

    # GET - Get one user
    if request.method == 'GET':

        return JsonResponse({
            'id': user.id,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'email': user.email,
            'role': {
                'roleName': user.role.roleName if user.role else None,
                'accessModules': user.role.accessModules
                if user.role else []
            }
        })

    # PUT - Update user
    elif request.method == 'PUT':

        try:
            data = json.loads(request.body)

            if 'firstName' in data:
                user.firstName = data['firstName']

            if 'lastName' in data:
                user.lastName = data['lastName']

            if 'email' in data:
                user.email = data['email']

            if 'role' in data:
                try:
                    user.role = Role.objects.get(id=data['role'])
                except Role.DoesNotExist:
                    return JsonResponse({
                        'error': 'Role not found'
                    }, status=404)

            if 'password' in data:
                user.set_password(data['password'])

            # Django model validation
            user.full_clean()

            user.save()

            return JsonResponse({
                'message': 'User updated successfully'
            })

        except (KeyError, json.JSONDecodeError):
            return JsonResponse({
                'error': 'Invalid data'
            }, status=400)

    # DELETE - Delete user
    elif request.method == 'DELETE':

        user.delete()

        return JsonResponse({
            'message': 'User deleted successfully'
        })

    return JsonResponse({
        'error': 'Method not allowed'
    }, status=405)  

@csrf_exempt
def bulk_update_users(request):
    """
    Update common fields for multiple users in one request.
    """

    if request.method != 'PUT':
        return JsonResponse({
            'error': 'Method not allowed'
        }, status=405)

    try:
        data = json.loads(request.body)
        user_ids = data['userIds']
    except (KeyError, json.JSONDecodeError):
        return JsonResponse({
            'error': 'userIds are required'
        }, status=400)

    if (
        not isinstance(user_ids, list)
        or not user_ids
        or not all(isinstance(user_id, int) for user_id in user_ids)
    ):
        return JsonResponse({
            'error': 'userIds must be a non-empty list'
        }, status=400)

    users = list(User.objects.filter(id__in=user_ids))
    if len(users) != len(set(user_ids)):
        return JsonResponse({
            'error': 'One or more users were not found'
        }, status=404)

    role = None
    if 'role' in data:
        try:
            role = Role.objects.get(id=data['role'])
        except Role.DoesNotExist:
            return JsonResponse({
                'error': 'Role not found'
            }, status=404)

    for user in users:
        for field in ('firstName', 'lastName', 'email', 'is_active'):
            if field in data:
                setattr(user, field, data[field])

        if role is not None:
            user.role = role

        if 'password' in data:
            user.set_password(data['password'])

        try:
            user.full_clean()
        except ValidationError as error:
            return JsonResponse({
                'error': error.message_dict
            }, status=400)

    for user in users:
        user.save()

    return JsonResponse({
        'message': 'Users updated successfully',
        'updatedUserIds': [user.id for user in users]
    })
    
@csrf_exempt
def signup(request):
    """
    Create a new user account with the default User role.
    """

    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method not allowed'
        }, status=405)

    try:
        data = json.loads(request.body)

        # Get the default User role
        role = Role.objects.get(roleName='User')

        user = User(
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            role=role
        )

        # Hash password using Django's built-in method
        user.set_password(data['password'])

        # Django model validation
        user.full_clean()

        user.save()

        return JsonResponse({
            'message': 'Signup successful',
            'id': user.id
        }, status=201)

    except Role.DoesNotExist:
        return JsonResponse({
            'error': 'Default User role does not exist'
        }, status=404)

    except (KeyError, json.JSONDecodeError):
        return JsonResponse({
            'error': 'Invalid or missing data'
        }, status=400)
        
@csrf_exempt
def user_login(request):
    """
    Authenticate a user using email and password.
    """

    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method not allowed'
        }, status=405)

    try:
        data = json.loads(request.body)

        email = data['email']
        password = data['password']

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if user is None:
            return JsonResponse({
                'error': 'Invalid email or password'
            }, status=401)

        login(request, user)

        return JsonResponse({
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'email': user.email
            }
        })

    except (KeyError, json.JSONDecodeError):
        return JsonResponse({
            'error': 'Invalid or missing data'
        }, status=400)        

@csrf_exempt
def check_module_access(request, user_id):
    """
    Check whether a user has access to a specific module.
    """

    if request.method != 'POST':
        return JsonResponse({
            'error': 'Method not allowed'
        }, status=405)

    try:
        user = User.objects.select_related('role').get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({
            'error': 'User not found'
        }, status=404)

    try:
        data = json.loads(request.body)
        module = data['module']
    except (KeyError, json.JSONDecodeError):
        return JsonResponse({
            'error': 'Module is required'
        }, status=400)

    if not user.role:
        return JsonResponse({
            'hasAccess': False
        })

    has_access = module in user.role.accessModules

    return JsonResponse({
        'userId': user.id,
        'module': module,
        'hasAccess': has_access
    })        
        