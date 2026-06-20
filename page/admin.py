from django.contrib import admin
from .models import Poster
from .models import StaticPage
from .models import GaharChecklist
admin.site.register(Poster)
admin.site.register(StaticPage)
from .models import VisitorLog
@admin.register(GaharChecklist)
class GaharChecklistAdmin(admin.ModelAdmin):
    # الأعمدة التي تظهر في جدول قائمة المراجعات
    list_display = ('department', 'date', 'inspector')
    # إضافة فلاتر جانبية لتسهيل البحث
    #list_filter = ('department', 'date', 'inspector')
    # البحث بالقسم
    search_fields = ('department',)
    # ترتيب البيانات من الأحدث للأقدم
    ordering = ('-date',)





@admin.register(VisitorLog)
class VisitorLogAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'page_visited', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('ip_address', 'page_visited')
