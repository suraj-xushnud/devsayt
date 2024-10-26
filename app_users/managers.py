from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class MyUserManager(UserManager):
    def create_user(self, first_name: str,
                    last_name: str,
                    email: str,
                    password: str = None) -> User:
        if not first_name:
            raise ValidationError('Users must have first name')
        if not last_name:
            raise ValidationError('Users must have last name')
        if not email:
            raise ValidationError('Users must have email')

        email = self.normalize_email(email=email)
        username = email[:email.index('@')]

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name: str,
                         last_name: str,
                         email: str,
                         password: str) -> User:
        superuser = self.create_user(first_name, last_name, email, password)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)
        return superuser
