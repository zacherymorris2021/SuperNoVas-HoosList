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
        'item_location',
        'item_preferred_payment_method',
        'item_condition',
        'item_categories',
        'item_photo',
        'latitude',
        'longitude'
        ]
        widgets={
        'item_name':forms.TextInput(attrs={'style':'line-height:7px;'}),
        'item_description':forms.Textarea(attrs={'style':' resize:none; line-height:120%;', 'rows':5, 'cols':25}),
        'item_location':forms.TextInput(attrs={'style':'padding:0px;'}),
        'latitude':forms.TextInput(attrs={'readonly':'readonly'}),
        'longitude':forms.TextInput(attrs={'readonly':'readonly'})
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
            'text': forms.Textarea
            }

class SendReplyForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
        'text'
        ]
        widgets = {'text': forms.Textarea(attrs={'style':'line-height:7px;'})}

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
