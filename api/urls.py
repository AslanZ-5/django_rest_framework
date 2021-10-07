from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (article_list,
                    article_detail,
                    ArticleAPIView,
                    ArticleDetails,
                    GenericAPIView,
)

urlpatterns = [

    # path('article/',article_list,name='article'),
    path('article/', ArticleAPIView.as_view(), name='article'),
    path('generic/article/<int:id>/', GenericAPIView.as_view(), name='article'),
    # path('detail/<int:pk>',article_detail,name='detail'),
    path('detail/<int:id>', ArticleDetails.as_view(), name='detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
