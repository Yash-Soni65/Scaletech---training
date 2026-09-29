import json

from django.test import TestCase

from roles.models import Role
from .models import User


class UserApiTests(TestCase):
	def setUp(self):
		self.user_role = Role.objects.create(roleName='User')
		self.admin_role = Role.objects.create(roleName='Admin')
		self.first_user = User.objects.create_user(
			email='first@example.com',
			password='password123',
			firstName='First',
			lastName='User',
			role=self.user_role,
		)
		self.second_user = User.objects.create_user(
			email='second@example.com',
			password='password123',
			firstName='Second',
			lastName='User',
			role=self.user_role,
		)

	def test_bulk_update_assigns_role_to_selected_users(self):
		response = self.client.put(
			'/users/bulk-update/',
			data=json.dumps({
				'userIds': [self.first_user.id, self.second_user.id],
				'role': self.admin_role.id,
			}),
			content_type='application/json',
		)

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			response.json()['updatedUserIds'],
			[self.first_user.id, self.second_user.id],
		)
		self.assertEqual(
			User.objects.filter(
				id__in=[self.first_user.id, self.second_user.id],
				role=self.admin_role,
			).count(),
			2,
		)

	def test_bulk_update_rejects_unknown_role_without_changes(self):
		response = self.client.put(
			'/users/bulk-update/',
			data=json.dumps({
				'userIds': [self.first_user.id],
				'role': 9999,
			}),
			content_type='application/json',
		)

		self.assertEqual(response.status_code, 404)
		self.first_user.refresh_from_db()
		self.assertEqual(self.first_user.role, self.user_role)
