from django.urls import path, include
from .views import *

urlpatterns = [
    # =================================================================
    # *** accounts ***
    path("accounts/users/list/", UserListView.as_view()),
    path("accounts/users/<int:pk>/", UserSingleView.as_view()),
    path("accounts/", include("djoser.urls")),
    path("accounts/", include("djoser.urls.jwt")),
    path("accounts/", include("djoser.social.urls")),
    # =================================================================
    # *** skills ***
    # path("skills/", SkillsView.as_view({"get": "list", "post": "create"}), name="pets"),
    # path(
    #     "skills/<int:pk>/",
    #     SkillsView.as_view(
    #         {
    #             "get": "retrieve",
    #             "patch": "partial_update",
    #             "post": "update",
    #             "delete": "destroy",
    #         }
    #     ),
    #     name="pets.details",
    # ),
    # path(
    #     "skills/<int:pk>/offer/",
    #     SkillsView.as_view({"post": "offerPet"}),
    #     name="pets.offer",
    # ),
    # =================================================================
    # *** skills -3 ***
    # path("skills/list/", SkillsView.as_view({"get": "list"}), name="skills-list"),
    # path(
    #     "skills/create/", SkillsView.as_view({"post": "create"}), name="skills-create"
    # ),
    # path(
    #     "skills/update/<int:pk>/",
    #     SkillsView.as_view({"patch": "partial_update"}),
    #     name="skills-update",
    # ),
    # path(
    #     "skills/detail/<int:pk>/",
    #     SkillsView.as_view({"get": "retrieve"}),
    #     name="skills-detail",
    # ),
    # path(
    #     "skills/delete/<int:pk>/",
    #     SkillsView.as_view({"delete": "destroy"}),
    #     name="skills-delete",
    # ),
    # =================================================================
    # *** skills -4 ***
    path("aboutme/list/", AboutMeViewSet.as_view({"get": "list"}), name="aboutme-list"),
    path(
        "aboutme/create/",
        AboutMeViewSet.as_view({"post": "create"}),
        name="aboutme-create",
    ),
    path(
        "aboutme/update/<int:pk>/",
        AboutMeViewSet.as_view({"patch": "partial_update"}),
        name="aboutme-update",
    ),
    path(
        "aboutme/detail/<int:pk>/",
        AboutMeViewSet.as_view({"get": "retrieve"}),
        name="aboutme-detail",
    ),
    path(
        "aboutme/delete/<int:pk>/",
        AboutMeViewSet.as_view({"delete": "destroy"}),
        name="aboutme-delete",
    ),
    # =================================================================
    # *** skills -4 ***
    path("skills/list/", SkillViewSet.as_view({"get": "list"}), name="skills-list"),
    path(
        "skills/create/", SkillViewSet.as_view({"post": "create"}), name="skills-create"
    ),
    path(
        "skills/update/<int:pk>/",
        SkillViewSet.as_view({"patch": "partial_update"}),
        name="skills-update",
    ),
    path(
        "skills/detail/<int:pk>/",
        SkillViewSet.as_view({"get": "retrieve"}),
        name="skills-detail",
    ),
    path(
        "skills/delete/<int:pk>/",
        SkillViewSet.as_view({"delete": "destroy"}),
        name="skills-delete",
    ),
    # =================================================================
    # *** experience ***
    path(
        "experience/list/",
        ExperienceViewSet.as_view({"get": "list"}),
        name="experience-list",
    ),
    path(
        "experience/create/",
        ExperienceViewSet.as_view({"post": "create"}),
        name="experience-create",
    ),
    path(
        "experience/update/<int:pk>/",
        ExperienceViewSet.as_view({"patch": "partial_update"}),
        name="experience-update",
    ),
    path(
        "experience/detail/<int:pk>/",
        ExperienceViewSet.as_view({"get": "retrieve"}),
        name="experience-detail",
    ),
    path(
        "experience/delete/<int:pk>/",
        ExperienceViewSet.as_view({"delete": "destroy"}),
        name="experience-delete",
    ),
    # =================================================================
    # *** services ***
    path(
        "services/list/",
        ServicesViewSet.as_view({"get": "list"}),
        name="services-list",
    ),
    path(
        "services/create/",
        ServicesViewSet.as_view({"post": "create"}),
        name="services-create",
    ),
    path(
        "services/update/<int:pk>/",
        ServicesViewSet.as_view({"patch": "partial_update"}),
        name="services-update",
    ),
    path(
        "services/detail/<int:pk>/",
        ServicesViewSet.as_view({"get": "retrieve"}),
        name="services-detail",
    ),
    path(
        "services/delete/<int:pk>/",
        ServicesViewSet.as_view({"delete": "destroy"}),
        name="services-delete",
    ),
    # =================================================================
    # *** MyWork ***
    path(
        "mywork/list/",
        MyWorkViewSet.as_view({"get": "list"}),
        name="mywork-list",
    ),
    path(
        "mywork/create/",
        MyWorkViewSet.as_view({"post": "create"}),
        name="mywork-create",
    ),
    path(
        "mywork/update/<int:pk>/",
        MyWorkViewSet.as_view({"patch": "partial_update"}),
        name="mywork-update",
    ),
    path(
        "mywork/detail/<int:pk>/",
        MyWorkViewSet.as_view({"get": "retrieve"}),
        name="mywork-detail",
    ),
    path(
        "mywork/delete/<int:pk>/",
        MyWorkViewSet.as_view({"delete": "destroy"}),
        name="mywork-delete",
    ),
    # =================================================================
    # ***  ***
]
