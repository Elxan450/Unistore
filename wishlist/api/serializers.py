from rest_framework import serializers
from wishlist.models import FavoriteListProduct, City


class FavoriteListProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = FavoriteListProduct
        fields = (
            "id",
            "favorite_list",
            "product"
        )


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            "country",
            "name"
        )