from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    pass

@admin.register(Brand)
class ProductAdmin(TranslationAdmin):
    pass

@admin.register(Gender)
class ProductAdmin(TranslationAdmin):
    pass

@admin.register(Color)
class ProductAdmin(TranslationAdmin):
    pass

@admin.register(CaseShape)
class ProductAdmin(TranslationAdmin):
    pass

@admin.register(StrapType)
class ProductAdmin(TranslationAdmin):
    pass

@admin.register(GlassFeature)
class ProductAdmin(TranslationAdmin):
    pass

@admin.register(Style)
class ProductAdmin(TranslationAdmin):
    pass

@admin.register(Mechanism)
class ProductAdmin(TranslationAdmin):
    pass

 