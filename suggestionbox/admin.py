from django.contrib import admin

from suggestionbox.models import Category, Suggestion, Status, Comment

class CommentInlineAdmin(admin.TabularInline):
    model = Comment
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    pass

class SuggestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    search_fields = ['title', 'description']
    list_display = ('title', 'category', 'status', 'pub_date',)
    list_filter = ['pub_date', 'status', 'category']

    inlines = [CommentInlineAdmin]

class CommentAdmin(admin.ModelAdmin):
    pass

class StatusAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Suggestion, SuggestionAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Status, StatusAdmin)
