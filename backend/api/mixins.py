from django.shortcuts import get_object_or_404

from api.permissions import IsAdminOrReadOnly
from api.serializers import SubscribeRecipeSerializer
from recipes.models import Recipe
from rest_framework import generics
from rest_framework.permissions import AllowAny


class GetObjectMixin:
    """Миксин для удаления/добавления рецептов избранных/корзины."""
    serializer_class = SubscribeRecipeSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        recipe_id = self.kwargs['recipe_id']
        recipe = get_object_or_404(Recipe, id=recipe_id)
        self.check_object_permissions(self.request, recipe)
        return recipe


class PermissionAndPaginationMixin:
    """Миксин для списка тегов и ингредиентов."""
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = None


class ListCreateDestroyViewSet(generics.RetrieveDestroyAPIView,
                               generics.ListCreateAPIView):
    """Вьюсет для переиспользования."""
    pass
