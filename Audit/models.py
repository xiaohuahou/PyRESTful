from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
STATUS = [('连载中', '连载中'), ('连载完', '连载完')]
CAT = [('悬疑惊悚', '悬疑惊悚'),('爱情', '爱情')]
CONTRACT_STATUS = [('未签约', '未签约'), ('已签约', '已签约')]

class Book(models.Model):

    title = models.CharField(max_length=100, blank=True, default='')
    chapter = models.IntegerField(default=0)
    author = models.CharField(max_length=100, blank=True, default='')

    status = models.CharField(choices=STATUS, default=STATUS[0], max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    cat = models.CharField(choices=CAT, max_length=100, blank=True, default=CAT[0])

    contract_status = models.CharField(choices=CONTRACT_STATUS, default=CONTRACT_STATUS[0], max_length=100)

    class Meta:
        ordering = ('created',)
