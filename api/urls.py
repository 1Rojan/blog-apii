from django.urls import path
from .views import (
    Home,
    UserRegister,
    PostCreate,
    PostList,
    UserList,
    UserDetail,
    PostDetail,
    CommentList,
    CommentDetail,
)

urlpatterns = [
    path("", Home.as_view()),
    path("users/register/", UserRegister.as_view()),
    path(
        "users/",
        UserList.as_view(),
    ),
    path(
        "users/<pk>/",
        UserDetail.as_view(),
    ),
    path("posts/", PostList.as_view()),
    path("posts/create/", PostCreate.as_view()),
    path("posts/<pk>/", PostDetail.as_view()),
    path("comments/", CommentList.as_view()),
    path("comments/<pk>/", CommentDetail.as_view()),
]
