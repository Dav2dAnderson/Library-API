from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'password', 'is_staff', 'is_active', 'downloaded_books', 'enrolled_books']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        downloaded_books = validated_data.pop('downloaded_books', [])
        enrolled_books = validated_data.pop('enrolled_books', [])

        user = Customer.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()

        user.downloaded_books.set(downloaded_books)
        user.enrolled_books.set(enrolled_books)
        return user
