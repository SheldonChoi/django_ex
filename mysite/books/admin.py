from django.contrib import admin

from .models import Publisher, Book, Author, WorkTime

class AuthorAdmin(admin.ModelAdmin) :
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'pulication_date')
    list_filter = ('pulication_date', ) 
    ordering = ('-title',)
    filter_horizontal = ('authors', )


admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(WorkTime)
