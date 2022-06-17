from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class UserType(models.Model):
    name = models.CharField("name", max_length=50)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, realname=None):
        # if not username:
        #     raise ValueError('Users must have a username')
        if not email:
            raise ValueError("User must have an email")
        user = self.model(
            email=email,
            password = make_password(password, salt=None, hasher='default'),
  
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, email, password=None, realname=None):
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser):
    username = models.CharField("username", max_length=50)
    password = models.CharField("password", max_length=128)
    email = models.EmailField("email", max_length=50, unique=True)
    realname = models.CharField("realname", max_length=50)
    join_date = models.DateField("joindate", auto_now_add=True)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.email}"

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label): 
        return True
    
    @property
    def is_staff(self): 
        return self.is_admin


class UserLog(models.Model):
    pass