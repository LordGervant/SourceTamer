from django.contrib import admin

from ContentAggregator.Aggregator.models import article, feed
# Register your models here.

@admin.register(article.Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = [field.name for field in article.Article._meta.fields]

@admin.register(feed.Feed)
class FeedAdmin(admin.ModelAdmin):
	list_display = [field.name for field in feed.Feed._meta.fields]
