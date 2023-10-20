from modeltranslation.translator import translator, TranslationOptions
from blog.models import Blog

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Blog, CategoryTranslationOptions)