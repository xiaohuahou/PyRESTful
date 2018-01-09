from rest_framework import serializers
from Audit.models import Book, Auditing

class BookSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Book
        fields = ('url','title', 'chapter', 'author', 'status', 'created', 'cat', 'contract_status')

class AuditingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Auditing
        fields = ('url', 'content', 'rank', 'reason', 'note')