from django.urls import path
from .views import (
    Home,
    UserRegister,
    PostList,
    UserList,
    UserDetail,
    PostDetail,
    CommentList,
    CommentDetail,
    CategoryList,
    CategoryDetail,
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
    path("posts/<pk>/", PostDetail.as_view()),
    path("comments/", CommentList.as_view()),
    path("comments/<pk>/", CommentDetail.as_view()),
    path("categories/", CategoryList.as_view()),
    path("categories/<pk>/", CategoryDetail.as_view()),
]
