from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.contrib.auth.models import AbstractUser
# from django.utils import timezone
# from django.contrib.auth import get_user_model

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email



class UserInfo(models.Model):
    id = models.AutoField(primary_key=True, db_column='user_id', blank = True)
#    cust = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='user_info', blank = True, null = True)
    fname = models.CharField(max_length=50,default='')
    lname = models.CharField(max_length=50, default='')
    username = models.EmailField(max_length=100, default='')
    Mob_num = models.CharField(max_length=10,default='')
    password = models.CharField(max_length=20, default='')
    dob = models.DateField(null = True, blank = True)
    address = models.TextField(null = True, blank = True)
    city = models.CharField(max_length = 50, null = True, blank = True)
    state = models.CharField(max_length = 50, null = True, blank = True)
    country = models.CharField(max_length = 50, null = True, blank = True)
    pincode = models.IntegerField(null = True, blank = True)
    GCC = models.IntegerField(null = True, blank = True)
    tasks = models.IntegerField(null = True, blank = True, default = 0)


    def __str__(self):
        return self.uname


class Tasks(models.Model):
    id = models.AutoField(primary_key=True, db_column='task_id')
    task_name = models.CharField(max_length=80, default='')
    task_description = models.TextField()
    task_reward = models.IntegerField()


class User_tasks(models.Model):
    uid = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='user_id')
    task_time = models.DateTimeField(default=now, editable=False)
    task_id = models.ForeignKey(Tasks, on_delete = models.PROTECT, db_column='task_id')
    img1 = models.ImageField(upload_to='images/', blank = True)
    img2 = models.ImageField(upload_to='images/', blank = True)
    img3 = models.ImageField(upload_to='images/', blank = True)
    img4 = models.ImageField(upload_to='images/', blank = True)
    img5 = models.ImageField(upload_to='images/', blank = True)
    img6 = models.ImageField(upload_to='images/', blank = True)
    img7 = models.ImageField(upload_to='images/', blank = True)
    img8 = models.ImageField(upload_to='images/', blank = True)
    vid1 = models.FileField(upload_to='videos/', blank = True)



class Sellers(models.Model):
    Sel_name = models.CharField(max_length=50, default='', primary_key=True, db_column="Sel_name")
    Sel_add = models.CharField(max_length=100, default='')
    Sel_prod = models.CharField(max_length=100, default='')


class Products(models.Model):
    id = models.AutoField(primary_key=True, db_column='prod_id')
    Prod_name = models.CharField(max_length=50, default='')
    Prod_price = models.DecimalField(max_digits=20, decimal_places=2, default='')
    class Meta:
        unique_together = ('id', )


class Orders(models.Model):
    uid = models.ForeignKey(UserInfo, on_delete=models.PROTECT, db_column='user_id')
    pid = models.ForeignKey(Products, on_delete=models.PROTECT, db_column='prod_id')
    prod_name = models.ForeignKey(Products, on_delete = models.PROTECT, db_column = "Prod_name", related_name='name_orders', default = '')
    ordered_at = models.DateTimeField(default = now, editable = False)
    order_status = models.CharField(max_length = 14, default = 'Not Delivered')
    order_cost = models.ForeignKey(Products, on_delete = models.PROTECT, db_column = "Prod_price", related_name='cost_orders', default = 55.00)
#    time_of_order = models.DateTimeField()


class Prod_review(models.Model):
    uid = models.ForeignKey(UserInfo, on_delete=models.PROTECT, db_column='user_id')
    pid = models.ForeignKey(Products, on_delete=models.PROTECT, db_column='prod_id')
    rating = models.CharField(max_length=10)
    rev_title = models.CharField(max_length=50, default='')
    rev_desc = models.TextField()

class Idea_Forge(models.Model):
    uid = models.ForeignKey(UserInfo, on_delete=models.PROTECT, db_column='user_id', blank = True )
    task_name = models.CharField(max_length = 70, default = 'task')
    task_desc = models.TextField(null = True, blank = True)
    reward = models.IntegerField(default = 0)
    task_video = models.FileField(upload_to='videos/', blank = True)
    uploaded_at = models.DateTimeField(default = now, editable = False)
    
# Create your models here.
    
class EcoAware(models.Model):
    id = models.AutoField(primary_key=True, db_column='task_id')
    Etask_name = models.CharField(max_length=80, default='')
    Etask_description = models.TextField()
    Etask_reward = models.IntegerField()

class User_Ecoaware(models.Model):
    uid = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='user_id')
    task_time = models.DateTimeField(default=now, editable=False)
    task_id = models.ForeignKey(EcoAware, on_delete = models.PROTECT, db_column='task_id')
    img1 = models.ImageField(upload_to='images/', blank = True)
    img2 = models.ImageField(upload_to='images/', blank = True)
    img3 = models.ImageField(upload_to='images/', blank = True)
    img4 = models.ImageField(upload_to='images/', blank = True)
    img5 = models.ImageField(upload_to='images/', blank = True)
    img6 = models.ImageField(upload_to='images/', blank = True)
    img7 = models.ImageField(upload_to='images/', blank = True)
    img8 = models.ImageField(upload_to='images/', blank = True)
    vid1 = models.FileField(upload_to='videos/', blank = True)

class locationsig(models.Model):
    lat = models.IntegerField(blank=True)
    long = models.IntegerField(blank = True)

class Mav(models.Model):
    uid = models.ForeignKey(UserInfo, on_delete=models.CASCADE, db_column='user_id')
    total = models.CharField(max_length = 5)