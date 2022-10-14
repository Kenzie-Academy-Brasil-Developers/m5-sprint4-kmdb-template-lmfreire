from ast import If
from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from reviews.exceptions import ValidationKeyError

from .models import Review
from users.models import User

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name"
        ]


class ReviewSerializer(serializers.ModelSerializer):
    
    users = UsersSerializer(read_only=True)
    
    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "recomendation",
            "movies",
            "users",
        ]
        read_only_fields = ["movies"]
        extra_kwargs = {"stars": {"min_value": 1, "max_value": 10}}
        
    
    def create(self, validated_data):
        user = validated_data.pop("user") 
        movie = validated_data.pop("movie")
        
        verify = Review.objects.filter(movies=movie.id, users=user) 
        
        if verify:
            raise ValidationKeyError("Review already exists.")
        
        review = Review.objects.create(**validated_data, users=user, movies=movie)
        
        return review