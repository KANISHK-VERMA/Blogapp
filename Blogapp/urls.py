from django.urls import path
from . import views
from.views import PostListView,PostDetailView,PostCreate,PostUpdate,PostDeleteView
urlpatterns = [
    path('',PostListView.as_view(),name="nblog"),
    path('post/<int:pk>/',PostDetailView.as_view(), name="ndetail"),
    path('post/new/', PostCreate.as_view(), name="ncreate"),
    path('post/<int:pk>/update', PostUpdate.as_view(), name="nupdate"),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name="ndelete"),
    path('about/',views.about,name="nabout"),

]
