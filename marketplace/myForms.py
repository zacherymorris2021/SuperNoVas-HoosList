from django import forms
from .models import Item, Message, Seller


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item

        fields = [
        'item_name',
        'item_description',
        'item_price',
        'item_delivery',
        'item_preferred_payment_method',
        'item_condition',
        'item_categories',
        'item_photo',
        'latitude',
        'longitude'
        ]
        widgets={
        'item_name':forms.TextInput(attrs={'style':'line-height:7px;','class':'form-control'}),
        'item_description':forms.Textarea(attrs={'class':'form-control','style':' resize:none; line-height:120%;', 'rows':4}),
        'item_price':forms.NumberInput(attrs={'class':'form-control'}),
        'item_delivery':forms.CheckboxInput(attrs={'class':'form-control','style':'text-align:left'}),
        'item_preferred_payment_method':forms.Select(attrs={'class':'form-control'}),
        'item_condition':forms.Select(attrs={'class':'form-control'}),
        'item_categories':forms.Select(attrs={'class':'form-control'}),
        'item_photo':forms.FileInput(attrs={'class':'form-control'}),
        'latitude':forms.HiddenInput(attrs={'id':'latitude', 'class':'form-control','readonly':'readonly'}),
        'longitude':forms.HiddenInput(attrs={'id':'longitude', 'class':'form-control','readonly':'readonly'})
        }

        labels={
        'item_name':'Name',
        'item_description':'Description',
        'item_price':'Price',
        'item_delivery':'Delivery?',
        'item_preferred_payment_method':'Preferred Method of Payment',
        'item_condition':'Condition',
        'item_categories': 'Category',
        'item_photo':'Photo',
        }


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
        'receiver',
        'subject',
        'text'
        ]
        widgets = {
            'receiver': forms.TextInput,
            'text': forms.Textarea(attrs={'style':' resize:none; line-height:120%;', 'rows':5, 'cols':25})
            }

class SendReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
        'text'
        ]
        widgets = {'text': forms.Textarea(attrs={'style':' resize:none; line-height:120%;', 'rows':5, 'cols':25})}

class UserRatingForm(forms.ModelForm):
    class Meta:
        model = Seller
        exclude = ('user', 'posRate' , 'negRate',
        'numTransactions')

    options = [
    ('positive', 'I had a positive shopping experience!'),
    ('negative', 'I had a negative shopping experience!')
    ]

    user = forms.CharField(label="Seller")
    question = forms.CharField(label="How was your experience with this user? ", widget=forms.Select(choices=options))
