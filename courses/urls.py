from django.urls import path
from .views import course_detail, course_list

urlpatterns = [
    path('', course_list, name = "courses"),
    path('<slug:category_slug>/<int:course_id>', course_detail, name = "course_detail"),
    path('categories/<slug:category_slug>', course_list, name = "courses_by_category"),
    path('tags/<slug:tag_slug>', course_list, name = "courses_by_tag"),
    
]