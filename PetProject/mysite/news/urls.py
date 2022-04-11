from django.urls import path

from .views import *

urlpatterns = [
    #path('', index, name="home"),
    path('', HomePromod.as_view(), name="home"),
    path('category/<int:category_id>/', get_category, name="category"),
    path('news/<int:news_id>/', view_more, name="view_more"),
    path('news/add-comment/', add_comment, name="add_comment"),
    path('news/add_feedback/', add_feedback, name="add_feedback"),
    path('news/contacts/', contacts, name="contacts"),
    path('news/add_busket/', add_busket, name="add_busket"),

]
