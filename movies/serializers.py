from django.db.models import Avg
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    ''' Campo calculado precisa herdar de SerializerMethodField(read_only=True) e fazee uma método com get_nomedocampo(self, obj):'''
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    # Método do campo calculado def get_campo(self,obj)
    # def get_rate(self, obj):
    #     reviews = obj.reviews.all()
    #     if reviews:
    #         # Fazer a soma de todas reviews do sistema
    #         sum_reviews = 0
    #         for review in reviews:
    #             sum_reviews += review.stars
    #         # Conta o total de reviews do sistema
    #         reviews_count = reviews.count()
    #         return round(sum_reviews/reviews_count, 1)
    #     return None

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None

    ''' Para fazer validações nos campos ou regras de negócio use validate_nomedocampo(self,value):...validationError'''
    # function validate_name_field(self, value):
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('o resume não pode ter mais de 200 caracteres')
        return value


class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
