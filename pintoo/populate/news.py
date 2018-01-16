# from populate import base
# from news.models import Volume, Article
# from django.contrib.auth.models import User
# 
# 
# titles = ['81', '82', '83', '84', '85']
# contents = ['朝陽科技大學', '資訊學院', '理工學院', '管理學院']
# 
# 
# def populate():
#     print('Populating Article and Comment ... ', end='')
#     Volume.objects.all().delete()
#     Article.objects.all().delete()
#     for title in titles:
#         volume = Volume()
#         volume.volumeTitle = title
#         volume.date = '2015-5-15'
#         volume.publish = True
#         volume.save()
#         article = Article()
#         for content in contents:
#             article.content += title + content + '\n'
#             article.articleTitle = '朝楊科技大學'
#             article.volume = volume
#             article.page = 1
#             article.num = 1
#         article.save()
#     print('done')
#     
# 
# if __name__ == '__main__':
#     populate()