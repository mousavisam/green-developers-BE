from django.urls import path, include


urlpatterns = [
    path('auth/', include('main.api.dispatchers.registration.register_dispatcher')),
    path('category/', include('main.api.dispatchers.category.category_dispatcher')),
    path('skill/', include('main.api.dispatchers.skill.skill_dispatcher')),
    path('profile/', include('main.api.dispatchers.profile.profile_dispatcher'))
]
