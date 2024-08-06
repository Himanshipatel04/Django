from django.contrib import admin
from .models import ChaiVariety
from .models import ChaiReview
from .models import chaiCertificate
from .models import store
# Register your models here.


class ChaiReviewInline(admin.TabularInline):
     model = ChaiReview
     extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
     list_display = ('name','type','date_added')
     inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
     list_display = ('name','location')
     filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
     list_display = ('chai','certificateNumber')


admin.site.register(ChaiVariety,ChaiVarietyAdmin)
admin.site.register(store,StoreAdmin)
admin.site.register(chaiCertificate,ChaiCertificateAdmin)
    
