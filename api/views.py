from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAdminUser

from djoser.views import UserViewSet

from .models import *
from .permissons import *
from .serializers import *
from .pagination import *

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# from offers.models import Offer
# from social.models import Post
from django.http import JsonResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle


# Create your views here.
# =================================================================
# *** accounts ***
class UserListView(generics.ListAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ["username", "first_name", "last_name", "email"]


class UserSingleView(generics.RetrieveDestroyAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissionUser]


# =================================================================
# *** skills ***
# class SkillsView(viewsets.ModelViewSet):
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
#     search_fields = ["name"]
#     ordering_fields = ["created_at"]
#     ordering = ["-created_at"]

#     def get_queryset(self):
#         allskills = Skills.objects.all()
#         # species = self.request.query_params.get("species")
#         # gender = self.request.query_params.get("gender")
#         # if gender:
#         #     allpets = allpets.filter(gender=gender)
#         # if species:
#         #     allpets = allpets.filter(species=species.capitalize())
#         return allskills

#     serializer_class = SkillsSerializer
#     permission_classes = [SkillsPermission]

#     def perform_create(self, serializer):
#         skill = serializer.save()
#         # adoption = Adoption(user=self.request.user, pet=pet)
#         # adoption.save()

#         files = self.request.FILES.getlist("photos")
#         if files:
#             [PhotoSkills.objects.create(pet=skill, photo=f) for f in files[0:4]]
#         else:
#             PhotoSkills.objects.create(skill=skill, photo="pets/images/cat_annon.png")
#             # if serializer.data.get("species") == "Cat":
#             #     PhotoSkills.objects.create(pet=pet, photo="pets/images/cat_annon.png")
#             # else:
#             #     Photo.objects.create(pet=pet, photo="pets/images/dog_annon.png")

#     def perform_update(self, serializer):
#         skill = serializer.save()
#         files = self.request.FILES.getlist("photos")
#         if files:
#             for old_photo in skill.photos.all():
#                 old_photo.delete()
#             for f in files[0:4]:
#                 PhotoSkills.objects.create(skill=skill, photo=f)

#     # def offerPet(self, request, pk):
#     #     offer = Offer.objects.create(
#     #         user=request.user,
#     #         pet=get_object_or_404(Pet, pk=self.kwargs["pk"]),
#     #         description=request.data.get("description"),
#     #     )
#     #     post = Post.objects.create(
#     #         user=request.user,
#     #         visible=True,
#     #         content=f"Hi, I am offering my pet, {offer.pet.name}, for adoption!",
#     #     )
#     #     return JsonResponse({"offer": offer.id}, status=status.HTTP_201_CREATED)


# =================================================================
# *** skills -2 ***
# class SkillsView(viewsets.ModelViewSet):
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
#     search_fields = ["name", "description"]
#     ordering_fields = ["created_at", "percentage"]
#     ordering = ["-created_at"]

#     def get_queryset(self):
#         allskills = Skill.objects.all()
#         name = self.request.query_params.get("name")
#         if name:
#             allskills = allskills.filter(name__icontains=name)
#         return allskills

#     serializer_class = SkillSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         skill = serializer.save()

#         # Handle image upload
#         files = self.request.FILES.getlist("image")
#         if files:
#             skill.image = files[0]
#             skill.save()

#     def perform_update(self, serializer):
#         skill = serializer.save()

#         # Handle updating the image
#         files = self.request.FILES.getlist("image")
#         if files:
#             skill.image.delete()  # Delete old image
#             skill.image = files[0]
#             skill.save()


# =================================================================
# *** skills -3 ***
# class SkillsView(viewsets.ModelViewSet):
#     serializer_class = SkillSerializer
#     permission_classes = [
#         permissions.IsAuthenticated
#     ]  # تأكد من أن المستخدم مسجل الدخول
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
#     pagination_class = CustomPagination  # إذا كنت تستخدم الـ Pagination

#     def get_queryset(self):
#         return Skill.objects.all()

#     def perform_create(self, serializer):
#         skill = serializer.save()
#         # إذا كنت بحاجة إلى معالجة الصور أو أي ملفات مرفقة
#         files = self.request.FILES.getlist("image")
#         if files:
#             Photo.objects.create(skill=skill, photo=files[0])

#     def perform_update(self, serializer):
#         skill = serializer.save()
#         files = self.request.FILES.getlist("image")
#         if files:
#             if skill.image:
#                 skill.image.delete()  # حذف الصورة القديمة
#             skill.image = files[0]
#             skill.save()


# =================================================================
# *** skills -4 ***
class AboutMeViewSet(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    permission_classes = [AboutMePermission]
    pagination_class = CustomPagination


# =================================================================
# *** skills -4 ***
class SkillViewSet(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [SkillPermission]
    pagination_class = CustomPagination


# =================================================================
# *** Experience ***
class ExperienceViewSet(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [ExperiencePermission]
    pagination_class = CustomPagination


# =================================================================
# *** services ***
class ServicesViewSet(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [ServicesPermission]
    pagination_class = CustomPagination


# =================================================================
# *** services ***
class MyWorkViewSet(viewsets.ModelViewSet):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MyWork.objects.all()
    serializer_class = MyWorkSerializer
    permission_classes = [MyWorkPermission]
    pagination_class = CustomPagination


# =================================================================
# ***  ***
