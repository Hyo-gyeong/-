from django.db import models

#class 테이터 이름:
#     데이터 형식
#     데이터 형식  ....정의하고자 하는 데이터를 클래스(객체)로표현
# = ORM (Object Relational Mapping)
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def sum(self):
        return self.body[:50]

    def __str__(self):
        return self.title
