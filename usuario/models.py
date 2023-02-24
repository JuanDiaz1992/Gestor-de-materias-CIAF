from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
import os
from django.conf import settings
from django.db.models.signals import post_save


# Create your models here.

def user_directory_path_profile(instance,filename):
    profile_picture_name = 'user/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name



def user_directory_path_banner(instance,filename):
    profile_picture_name = 'user/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

class USer(AbstractBaseUser):
    stripe_custome_id = models.CharField(max_length=50)

class Estudiante(models.Model):
    nombre1 = models.CharField(max_length=30)
    nombre2 = models.CharField(max_length=30)
    primerApellido = models.CharField(max_length=50)
    segundoApellido = models.CharField(max_length=50)
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    semestre = models.PositiveSmallIntegerField(null=False, blank=False)
    foto = models.ImageField(upload_to = user_directory_path_profile , default = 'images/usuarioDefault.png', null= True, blank=True)
    banner = models.ImageField(upload_to = user_directory_path_banner , default = 'images/banner.jpg', null= True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) :
        return self.nombre1


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Estudiante.objects.create (user = instance)

def save_user_profile(sender,instance, **kwargs):
    instance.estudiante.save()

post_save.connect(create_user_profile, sender = User)
post_save.connect(save_user_profile, sender = User)