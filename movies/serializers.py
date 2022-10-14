from rest_framework import serializers
from genres.models import Genre

from genres.serializers import GenreSerializer
from movies.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()
    
    genres = GenreSerializer(many=True)
    
    def create(self, validated_data):
        genres_data = validated_data.pop("genres")
        
        movie_obj = Movie.objects.create(**validated_data)
        
        for genre in genres_data:
            genre_obj, _ = Genre.objects.get_or_create(**genre)
            movie_obj.genres.add(genre_obj)
            
        return movie_obj
            
    def update(self, instance, validated_data):
        
        data = {**validated_data}
        for key, value in data.items():
            
            if key == 'genres':
                genres_data = validated_data.pop("genres")
                instance.genres.set([])
                
                for genre in genres_data:
                    genre_obj, _ = Genre.objects.get_or_create(**genre)
                    instance.genres.add(genre_obj)
                    
                continue
            
            setattr(instance, key, value)
        
        instance.save()
        
        return instance 