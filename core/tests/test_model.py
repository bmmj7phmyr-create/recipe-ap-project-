"""
Modeller için test.
"""
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.test import TestCase

from core import models


def create_user(email='user@example.com', password='testpass123'):
    """Create and return a new user."""
    return get_user_model().objects.create_user(email=email, password=password)


class ModelTests(TestCase):
    """Model testleri."""

    def test_create_user_with_email_successful(self):
        """Email ile kullanıcı oluşturma başarılı."""
        email = "test@example.com"
        password = "testpass123"

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Yeni kullanıcı için email normalize edilir."""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Email olmadan kullanıcı oluşturulursa hata verir."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """Süper kullanıcı oluşturma."""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test123",
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Recipe oluşturma başarılı."""
        user = get_user_model().objects.create_user(
            "test@example.com",
            "testpass123",
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title="sample recipe name",
            time_minutes=5,
            price=Decimal("5.50"),
            description="sample recipe description",
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a tag is successful."""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Vegan')

        self.assertEqual(str(tag), tag.name)

    def test_create_ingredient(self):
        """Test creating an ingredient is successful."""
        user = create_user()
        ingredient = models.Ingredient.objects.create(user=user, name='Cucumber')

        self.assertEqual(str(ingredient), ingredient.name)
