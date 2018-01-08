from rest_framework import serializers
from Audit.models import Book

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('url', 'title', 'chapter', 'author', 'status', 'created', 'cat', 'contract_status')