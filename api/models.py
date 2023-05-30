from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.



class UserAccountManager(BaseUserManager):
    
    def create_user(self, email,first_name, last_name, password =None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,
        first_name= first_name,
        last_name=last_name,
        )

        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, email,first_name, last_name, password =None):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(email=email,
        first_name =first_name,
        last_name = last_name, 
        is_superuser= True)

        user.set_password(password)
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
 
    first_name = models.CharField(max_length=100 , null=True)
    last_name = models.CharField(max_length=100 , null=True)
   
    email = models.EmailField(max_length=255, unique=True)
    department = models.CharField(max_length=200, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects  = UserAccountManager()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['first_name','last_name']

    # def get_fullname(self):
    #     return self.fullname
    
    # def get_shortname(self):
    #     return self.fullname
    

    def __str__(self):
        return str(self.email) 

class Project(models.Model):
    project_name = models.CharField(max_length=200, null= True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    description = models.CharField(max_length=300, null=True, )
    date_created =models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.project_name)




class Category(models.Model):
    title= models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=300, null= True)
    project= models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.title)





class Ticket(models.Model):
    
    STATUS=(
        ('OPEN', 'OPEN'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('IN REVIEW', 'IN REVIEW'),
        ('CLOSED', 'CLOSED')
    )
    
    title = models.CharField(max_length=200 , null=True)
    project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    status =  models.CharField(max_length=200, null= True,choices=STATUS, default='OPEN')
    description = models.CharField(max_length=300, null= True)
    department = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add= True)
    date_updated = models.DateField(auto_now=True)
    reporter = models.ForeignKey(User,null=True, on_delete=models.SET_NULL, related_name='reporter')
    # reporter_name = models.CharField(max_length=300, null= True)
    assignee = models.ForeignKey(User,null=True, on_delete=models.SET_NULL, related_name='assignee')
    # watcher = models.ForeignKey(User ,null=True, on_delete=models.SET_NULL)
    ticket_id = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.title)
    
    class Meta:
        ordering = ['-date_created']

class Comments(models.Model):
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(Ticket, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return str(self.description)
    
    class Meta:
        ordering = ['-date_created']