from django.urls import path, include

from . import views

app_name = "polls"
urlpatterns = [
    path('', views.index, name='index'),
    path('community/<id>', views.getCommunity, name="communityDetail"),
    path('newCommunity/', views.newCommunity, name='index'),
    path('eleman', views.newDataType),
    path('deactivateCommunity', views.deactivateCommunity),
    path('community/<cmn_id>/<dt_id>/newPost', views.newPost, name="newPost"),
    path('createNewPost', views.createNewPost),
    path('login/<id>/', views.login),
    path('signup/', views.signup),
    path('c/<url>/', include([
        path('', views.getCommunity),
        path('members/', views.getCommunityMembers),
        path('datatypes/', views.getCommunityDataTypes),
        path('datafields/', views.getCommunityDataFields)
    ])
         ),
    path('tags', views.tags)
]
