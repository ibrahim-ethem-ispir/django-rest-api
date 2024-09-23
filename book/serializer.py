from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)  
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    year = serializers.IntegerField()
    stock = serializers.IntegerField()
    published = serializers.BooleanField()
    published_date = serializers.DateField()
    
    class Meta:
        model = Book  # Burada string yerine doğrudan Book modelini kullanmalısınız
        fields = "__all__"
        
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.year = validated_data.get('year', instance.year)
        instance.stock = validated_data.get('stock', instance.stock)
        instance.published = validated_data.get('published', instance.published)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.save()
        return instance
