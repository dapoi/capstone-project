from django.contrib import admin
from .models import Job, Category, Company, user_profile, Image_company, Image_user, FileUpload
from django.contrib.auth.models import Group


admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(user_profile)
admin.site.register(Image_company)
admin.site.register(Image_user)
admin.site.register(FileUpload)

# admin.register() decorator


class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content')


class JobAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_filter = ('category')


# to remove Groups table
admin.site.unregister(Group)
# to change header name
admin.site.site_header = "Job Finder Admin Page"