import datetime

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.utils import timezone


# Create your models here.
# =================================================================
# *** accounts ***
class User(AbstractUser, PermissionsMixin):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    email = models.EmailField(unique=True)

    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    phone = models.CharField(max_length=11, blank=True)
    picture = models.ImageField(
        # upload_to="accounts/images/%Y/%m/%d/%H/%M/%S/",
        upload_to="images/accounts/",
        null=True,
        default="images/accounts/annon.png",
    )
    birthdate = models.DateField(null=True, blank=True)
    profile_url = models.URLField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "password"]

    # objects = UserManager()
    def get_profile_picture(self):
        if self.picture:
            return self.picture.url
        return "/media/images/accounts/annon.png"

    def __str__(self) -> str:
        return self.username

    @property
    def full_name(self):
        if self.first_name:
            return self.first_name + " " + self.last_name
        return self.username


# =================================================================
# *** skills ***
# class Skills(models.Model):
#     # TYPE_CHOICES = (
#     #     ("Dog", "Dog"),
#     #     ("Cat", "Cat"),
#     #     ("Bird", "Bird"),
#     #     ("Turtle", "Turtle"),
#     #     ("Hamster", "Hamster"),
#     #     ("Other", "Other"),
#     # )

#     # GENDER_CHOICES = (
#     #     ("Male", "Male"),
#     #     ("Female", "Female"),
#     # )

#     name = models.CharField("Name", max_length=100)
#     brief = models.TextField(null=True)
#     percentage = models.CharField(max_length=3, null=True)

#     # gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
#     # species = models.CharField(max_length=10, choices=TYPE_CHOICES, null=True)
#     # breed = models.CharField(max_length=50, null=True)
#     # color = models.CharField(max_length=20, null=True)
#     # birthdate = models.DateField(default=datetime.date.today, null=True)
#     owner = models.ForeignKey(
#         "api.User", on_delete=models.CASCADE, related_name="skills"
#     )
#     created_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     def get_thumbnail(self):
#         try:
#             return self.photos.all().first().photo.url
#         except:
#             return None

#     # def get_age(self):
#     #     if self.birthdate:
#     #         res = ""
#     #         age = timezone.now().date() - self.birthdate
#     #         y = age.days // 365.25
#     #         if y:
#     #             res += f"{int(y)} years"

#     #         m = (age.days % 365.25) // 30
#     #         if m:
#     #             res += f" {int(m)} months "

#     #         d = age.days % 30
#     #         if d and not y:
#     #             res += f"{int(d)} days"

#     #         return res

#     #     return

#     class Meta:
#         unique_together = (
#             "owner",
#             "name",
#         )
#         ordering = ["-created_at"]


# class PhotoSkills(models.Model):
#     photo = models.ImageField(
#         upload_to="skills/images/%Y-%m-%d-%H-%M-%S/", null=True, blank=True
#     )
#     skills = models.ForeignKey(Skills, on_delete=models.CASCADE, related_name="photos")


# # class Adoption(models.Model):
# #     user = models.ForeignKey(
# #         "api.User", on_delete=models.CASCADE, related_name="adoptions"
# #     )
# #     pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="adoptions")
# #     start_at = models.DateField(auto_now_add=True)
# #     end_at = models.DateField(null=True)

# #     def __str__(self):
# #         return f"{self.user} adopted {self.pet}"


# =================================================================
# *** skills -2 ***
# class Skill(models.Model):
#     name = models.CharField("Skill Name", max_length=100)
#     description = models.TextField(null=True, blank=True)
#     percentage = models.DecimalField(max_digits=5, decimal_places=2)
#     created_at = models.DateField(auto_now_add=True)
#     image = models.ImageField(
#         upload_to="skills/images/%Y/%m/%d/", null=True, blank=True
#     )

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ["-created_at"]


# =================================================================
# *** skills -3 ***
# class Skill(models.Model):
#     name = models.CharField("Name", max_length=100)
#     description = models.TextField(null=True, blank=True)
#     percentage = models.IntegerField(default=0)  # النسبة
#     image = models.ImageField(
#         upload_to="skills/images/%Y/%m/%d/", null=True, blank=True
#     )
#     created_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ["-created_at"]


# =================================================================
# *** About Me  ***
class AboutMe(models.Model):
    description = models.TextField(null=True, blank=True)
    driveLink = models.TextField(null=True, blank=True)
    image_url = models.CharField(
        max_length=10000,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="images/aboutme/",
        null=True,
        blank=True,
        default="images/default.jpg",
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description


# =================================================================
# *** skills -4 ***
class Skill(models.Model):
    name = models.CharField("Name", max_length=1000)
    description = models.TextField(null=True, blank=True)
    percentage = models.IntegerField(default=0)
    image_url = models.CharField(
        max_length=10000,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="images/skills/",
        null=True,
        blank=True,
        default="images/default.jpg",
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# =================================================================
# *** Experience ***
class Experience(models.Model):
    name = models.CharField("Name", max_length=1000)
    description = models.TextField(null=True, blank=True)
    start_at = models.DateField(null=True)
    end_at = models.DateField(null=True)
    # end_at = models.DateField(auto_now_add=True)
    tag = models.CharField(max_length=300)
    image_url = models.CharField(
        max_length=10000,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="images/experience/",
        null=True,
        blank=True,
        default="images/default.jpg",
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# =================================================================
# *** services ***
class Services(models.Model):
    name = models.CharField("Name", max_length=1000)
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(
        max_length=10000,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="images/services/",
        null=True,
        blank=True,
        default="images/default.jpg",
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# =================================================================
# *** services ***
class MyWork(models.Model):
    name = models.CharField("Name", max_length=1000)
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(
        max_length=10000,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        upload_to="images/mywork/",
        null=True,
        blank=True,
        default="images/default.jpg",
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


# =================================================================
# ***  ***
