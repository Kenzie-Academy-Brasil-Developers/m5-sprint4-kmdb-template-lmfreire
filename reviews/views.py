from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404

from movies.models import Movie
from reviews.models import Review
from reviews.permissions import IsAdminOrCritic, IsAdminOrCriticDetail
from reviews.serializers import ReviewSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class CreateReviewsReview(APIView, PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCritic]
    
    def get(self, request: Request, movie_id: int) -> Response:
        
        movie = Review.objects.filter(movies=movie_id)
        result_page = self.paginate_queryset(movie, request, view=self)
        serializer = ReviewSerializer(result_page, many=True)
        
        return self.get_paginated_response(serializer.data)
    
    
    def post(self, request: Request, movie_id: int) -> Response:
        movie = get_object_or_404(Movie, id=movie_id)
        
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save(movie=movie, user=request.user)
            
        
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class ReviewMovieDetailReview(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrCriticDetail]
    
    def get(self, request: Request, movie_id: int, review_id: int) -> Response:
        
        review_movie = Review.objects.filter(movies=movie_id, id=review_id)
        serializer = ReviewSerializer(review_movie, many=True)
        
        return Response(serializer.data)
    
    def delete(self, request: Request, movie_id: int, review_id: int) -> Response:
        review_movie = Review.objects.filter(movies=movie_id, id=review_id)
        
        self.check_object_permissions(request, review_movie)
        
        review_movie.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)