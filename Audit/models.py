from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
STATUS = [('连载中', '连载中'), ('连载完', '连载完')]
CAT = [('悬疑惊悚', '悬疑惊悚'),('爱情', '爱情')]
CONTRACT_STATUS = [('未签约', '未签约'), ('已签约', '已签约')]

class Auditing(models.Model):

    content = models.CharField(max_length=1000)

    rank = models.IntegerField(default=0)
    reason = models.CharField(max_length=500)
    note = models.CharField(max_length=500)


class Book(models.Model):

    title = models.CharField(max_length=100, blank=True, default='')
    chapter = models.IntegerField(default=0)
    author = models.CharField(max_length=100, blank=True, default='')

    status = models.CharField(choices=STATUS, max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    cat = models.CharField(choices=CAT, max_length=100, blank=True)

    contract_status = models.CharField(choices=CONTRACT_STATUS, max_length=100)

    auditing = models.OneToOneField(Auditing, related_name='auditing',on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)



