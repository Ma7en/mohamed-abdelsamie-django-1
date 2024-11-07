import re

from rest_framework import serializers
from django.core.files.images import get_image_dimensions

from .models import *
from .serializers import *

# from pets.serializers import PetSerializer, AdoptionSerializer
# from social.serializers import PostsSerializer


# =================================================================
# *** accounts 1 ***
# class UserSerializer(serializers.ModelSerializer):
#     # pets = PetSerializer(many=True, read_only=True)
#     # adoptions = AdoptionSerializer(many=True, read_only=True)
#     # posts = PostsSerializer(many=True, read_only=True)

#     def to_representation(self, obj):
#         data = super(UserSerializer, self).to_representation(obj)
#         for pet in data["pets"]:
#             del pet["owner"], pet["adoptions"], pet["photos"]
#         for post in data["posts"]:
#             del post["comments"], post["user"]

#         return data

#     class Meta:
#         model = User
#         # fields = '__all__' #['id', 'username','first_name', 'last_name', 'email', 'gender', 'password','phone','picture','birthdate','profile_url','created_at', 'pets']
#         exclude = ("last_login", "is_staff", "groups", "user_permissions")
#         read_only_fields = ("id", "created_at", "email", "username")
#         depth = 1
#         extra_kwargs = {"password": {"write_only": True}}

#     def validate_picture(self, picture):
#         w, h = get_image_dimensions(picture)

#         if picture and picture.size > 2000000:
#             raise serializers.ValidationError("Image size should be less than 2 Mbs")
#         elif w < 400 or h < 400:
#             raise serializers.ValidationError(
#                 "Image dimensions should be greater than 400 pixels"
#             )

#         return picture

#     def validate_phone(self, phone):
#         re.compile("^01[0125]{1}[0-9]{8}$")
#         if re.fullmatch("^01[0125]{1}[0-9]{8}$", phone) or phone == "":
#             return phone
#         else:
#             raise serializers.ValidationError("Phone must match Egyptian format")


# =================================================================
# *** skills ***
# class PhotoSkillsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PhotoSkills
#         fields = ("photo",)


# # class AdoptionSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = Adoption
# #         fields = "__all__"
# #         depth = 1

# #     def to_representation(self, obj):
# #         data = super(AdoptionSerializer, self).to_representation(obj)
# #         return {
# #             "username": obj.user.full_name,
# #             "user_id": obj.user.id,
# #             "user_picture": data["user"]["picture"],
# #             "petname": obj.pet.name,
# #             "pet_id": obj.pet.id,
# #             "start_at": obj.start_at,
# #             "end_at": obj.end_at,
# #         }


# class SkillsSerializer(serializers.ModelSerializer):
#     thumbnail = serializers.CharField(source="get_thumbnail", read_only=True)
#     photos = PhotoSkillsSerializer(many=True, read_only=True)
#     # age = serializers.CharField(source="get_age", read_only=True)
#     # adoptions = AdoptionSerializer(many=True, read_only=True)

#     def to_representation(self, obj):
#         data = super(SkillsSerializer, self).to_representation(obj)
#         data["owner"] = {
#             "username": obj.owner.full_name,
#             "user_id": obj.owner.id,
#             "user_picture": data["owner"]["picture"],
#         }

#         # data["offer"] = obj.offers.first().id if obj.offers.first() else 0

#         if data["photos"]:
#             data["thumbnail"] = data["photos"][0]["photo"]

#         return data

#     class Meta:
#         model = Skills
#         fields = "__all__"
#         read_only_fields = ("id", "created_at")
#         depth = 1
#         extra_kwargs = {
#             "password": {"write_only": True},
#         }

#     # def validate(self, attrs):
#     #     attrs["owner"] = self.context["request"].user
#     #     if attrs.get("birthdate") and attrs.get("birthdate") > timezone.now().date():
#     #         raise serializers.ValidationError("Birthdate cannot be greater than today!")

#     #     return attrs


# =================================================================
# *** skills -3 ***
# class SkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Skill
#         fields = "__all__"
#         read_only_fields = ("id", "created_at")

#     def validate_percentage(self, value):
#         if value < 0 or value > 100:
#             raise serializers.ValidationError("Percentage must be between 0 and 100.")
#         return value


# =================================================================
# *** About Me ***
class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMe
        fields = "__all__"


# =================================================================
# *** skills -4 ***
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

    def validate_percentage(self, value):
        if value < 0 or value > 100:
            raise serializers.ValidationError("Percentage must be between 0 and 100.")
        return value


# =================================================================
# *** Experience ***
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


# =================================================================
# *** Experience ***
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = "__all__"


# =================================================================
# *** Experience ***
class MyWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyWork
        fields = "__all__"


# =================================================================
# ***  ***


# =================================================================
# *** accounts 2 ***
class UserSerializer(serializers.ModelSerializer):
    # Uncomment these if they should be serialized
    skills = SkillSerializer(many=True, read_only=True)
    # posts = PostsSerializer(many=True, read_only=True)

    def to_representation(self, obj):
        data = super(UserSerializer, self).to_representation(obj)

        # Safely check and clean pets data if present
        pets = data.get("pets", [])
        for pet in pets:
            pet.pop("owner", None)
            pet.pop("adoptions", None)
            pet.pop("photos", None)

        # Safely check and clean posts data if present
        posts = data.get("posts", [])
        for post in posts:
            post.pop("comments", None)
            post.pop("user", None)

        return data

    class Meta:
        model = User
        exclude = ("last_login", "is_staff", "groups", "user_permissions")
        read_only_fields = ("id", "created_at", "email", "username")
        depth = 1
        extra_kwargs = {"password": {"write_only": True}}

    def validate_picture(self, picture):
        w, h = get_image_dimensions(picture)

        if picture and picture.size > 2000000:
            raise serializers.ValidationError("Image size should be less than 2 Mbs")
        elif w < 400 or h < 400:
            raise serializers.ValidationError(
                "Image dimensions should be greater than 400 pixels"
            )

        return picture

    def validate_phone(self, phone):
        re.compile("^01[0125]{1}[0-9]{8}$")
        if re.fullmatch("^01[0125]{1}[0-9]{8}$", phone) or phone == "":
            return phone
        else:
            raise serializers.ValidationError("Phone must match Egyptian format")
