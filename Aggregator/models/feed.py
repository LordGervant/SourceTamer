from django.db import models


class Feed(models.Model):
	title = models.CharField(max_length=200)
	url = models.URLField()
	# is_active = models.BooleanField(default=False)


class FeedSerializer(models.Model):
	class Meta:
		model = Feed
		fields = "__all__"
