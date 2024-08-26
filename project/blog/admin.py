from django import forms
from django.contrib import admin
from .models import (
    Topic,
    Post,
    PostImage
)

from unfold.admin import (
    ModelAdmin,
    TabularInline

)
# from unfold.contrib.forms.widgets import WysiwygWidget

from unfold.widgets import UnfoldAdminTextareaWidget
from core.admin_utils import WysiwygWidget 
from core.admin_utils import RichTextEditorAdmin
from core.admin_utils import BaseWysiwygCustomForm


# form
class PostAdminForm(BaseWysiwygCustomForm):
    class Meta:
        model = Post
        fields = ["title", "image", "preview", "body", "topics"]
        widgets = {
            'preview': UnfoldAdminTextareaWidget(attrs={'rows':3}),
            'body': WysiwygWidget
        }


# form_required_fields
class PostMinimalCreateForm(forms.ModelForm):
    class Meta:
        fields = ['title']

# form_related_image
class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ["image"]

class PostImageInline(TabularInline):
    model = PostImage


    
@admin.register(Post)
class PostAdmin(RichTextEditorAdmin):
    form = PostAdminForm
    inlines = [PostImageInline]
    filter_horizontal = ["topics"]

    # custom required attributes
    form_required_fields = PostMinimalCreateForm
    model_image_related = PostImage
    form_related_image = PostImageForm
    name_image_field = "image"
    rel_image_to_model = "post"
    disable_inlines_on_delete_image = True
    disable_inlines_message = "Para usar esta seccion debe guardar"
   
@admin.register(Topic)
class TopicAdmin(ModelAdmin):
    pass