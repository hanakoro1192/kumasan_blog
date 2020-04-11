from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
#ここがオブジェクトになる
class Post(models.Model):
    #デフォルトのUserモデルを利用することは非推奨となっているためsettings.AUTH_USER_MODEL.OneToOneでUserに紐づくProfileモデルを定義する
    #on_deleteとは参照するオブジェクトが削除されたときに、それと紐づけられたオブジェクトも一緒に削除するのか、それともそのオブジェクトは残しておくのかを設定するもの
    #ForeignKeyは外部キーとなっている.これは他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    #blankはDjangoのフォームからの投稿が空かどうかを判定するもの、nullはデータベースの中身が空かどうかを判定するものになります。それぞれ、blank=Trueとnull=Trueのときに、対象が空であることを許容すること
    published_date = models.DateTimeField(blank=True, null=True)

    #この部分がメソッドになる
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title