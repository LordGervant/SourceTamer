from django.db import models

from rest_framework import serializers

from ContentAggregator.Aggregator.models.feed import Feed


class Article(models.Model):
	feed = models.ForeignKey(Feed)
	title = models.CharField(max_length=200)
	url = models.URLField()
	description = models.TextField()
	publication_date = models.DateTimeField()

	def __str__(self):
		return self.title


class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = "__all__"
