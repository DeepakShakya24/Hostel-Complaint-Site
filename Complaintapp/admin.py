from django.contrib import admin
from Complaintapp.models import ComplaintInfo,WardenInfo

# Register your models here.
class WardenAdmin(admin.ModelAdmin):
    fields=['name','year','enrollment_num','room_num','complaintbox','email']
    search_fields=['room_num','enrollment_num']
    list_display=['name','year','enrollment_num','room_num','complaintbox','email']
admin.site.register(ComplaintInfo,WardenAdmin)
admin.site.register(WardenInfo)