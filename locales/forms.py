from django import forms

class CategoryForm (forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'img']

class BusinessForm (forms.ModelForm):
    class Meta:
        model = Business
        filed =  ['name','mission','vision','email','phone','facebook','instagram','img','category']

class ProductForm (forms.ModelForm):
    class Meta:
        model = Product
        field = ['name','desciption','price','stock','business']

class LocalForm (forms.ModelForm):
    class Meta:
        model = Local
        field = ['name','width','deep','aviable','rent','administration','business']
