from django.urls import path
from . import views


urlpatterns = [
    path('', views.allchai, name="allchai"),
    path('<int:chai_id>/', views.chai_details, name="chai_details"),
    path('chaiStores/',views.chai_stores_view,name="chaiStores")
]