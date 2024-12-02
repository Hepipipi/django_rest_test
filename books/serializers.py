from rest_framework import serializers
from .models import Book, Movie, Review


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']


class ReviewSerializer(serializers.ModelSerializer):

    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'book', 'content', 'rating']



#
# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = ['id', 'title', 'author', 'published_date']

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=50)
#     published_date = serializers.DateField()
#
#     def validate_title(self, value):
#         if 'django' in value.lower():
#             raise serializers.ValidationError("Название книги не может содержать 'django'.")
#         return value
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)
#
#     def delete(self, instance):
#         instance.delete()
#         return {"message": f"Фильм '{instance.title}' был удалён."}



    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    director = serializers.CharField(max_length=50)
    release_date = serializers.DateField()


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def validate_director(self, value):
        if 'niga' in value.lower():
            raise serializers.ValidationError("Название директора не может содержать 'Niga'.")
        return value

