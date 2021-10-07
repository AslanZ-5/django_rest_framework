from django.urls import path
from .views import article_list, article_detail,ArticleAPIView,ArticleDetails
urlpatterns = [

    # path('article/',article_list,name='article'),
    path('article/',ArticleAPIView.as_view(),name='article'),
    # path('detail/<int:pk>',article_detail,name='detail'),
    path('detail/<int:id>',ArticleDetails.as_view(),name='detail')
]