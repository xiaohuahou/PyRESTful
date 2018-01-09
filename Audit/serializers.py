from rest_framework import serializers
from Audit.models import Book, Auditing

class BookSerializer(serializers.HyperlinkedModelSerializer):

    auditing = serializers.StringRelatedField(many=False)

    class Meta:
        model = Book
        fields = ('url','title', 'chapter', 'auditing')

class AuditingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Auditing
        fields = ('url', 'content', 'rank', 'reason', 'note')