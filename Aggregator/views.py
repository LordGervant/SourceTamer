from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics

from ContentAggregator.Aggregator.models.article import Article, ArticleSerializer
from ContentAggregator.Aggregator.models.feed import Feed, FeedSerializer


# Create your views here.


class AggregatorViewset(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

	def get(self, request, *args, **kwargs):
		if args.pk:
			return self.retrieve(request, *args, **kwargs)
		else:
			return self.list(request, *args, **kwargs)
	if None:
		pass
