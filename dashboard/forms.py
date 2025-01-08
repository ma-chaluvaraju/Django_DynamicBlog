from django import forms
from blogs.models import Category,Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.get('instance')  # Access the current instance
        super().__init__(*args, **kwargs)

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        # Exclude the current instance from the uniqueness check
        if Category.objects.filter(category_name=category_name).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Category with this name already exists.")
        return category_name

class BlogPostForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields = ('title','category','blog_image','short_description','blog_body','status','is_feacherd')

# class AddUserForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')