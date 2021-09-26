# coding=utf-8
from haystack import indexes
from post.models import *

# 注意格式 模型类名+Index
class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)  # 固定的

    # 给 title，content设置索引
    title = indexes.NgramField(model_attr='title')      # 字段名
    content = indexes.NgramField(model_attr='content')

    def get_model(self):            # 一定到重写，写哪个模型类返回哪个
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created') # 按照发帖时间降序排序建立索引








