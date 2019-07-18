# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
# from rest_framework.reverse import reverse
#
#
# class UserProfile(AbstractUser):
#     CUSTOMER = 1
#     EXECUTOR = 2
#
#     USER_TYPES = (
#         (CUSTOMER, 'customer'),
#         (EXECUTOR, 'executor'),
#     )
#
#     name = models.CharField('Name of User', blank=True, max_length=255)
#     user_type = models.PositiveSmallIntegerField(choices=USER_TYPES, default=EXECUTOR)
#
#     def __str__(self):
#         return self.username
#
#     def get_absolute_url(self):
#         return reverse('users:detail', kwargs='username')
#
#     class Meta:
#         swappable = get_user_model()