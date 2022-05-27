from tkinter import Widget
from django import forms
from .models import Book,Category

class Categoryform(forms.ModelForm):

        class Meta:
                model=Category
                fields=['name']

                Widget={'name': forms.TextInput(attrs={'class':'form-control'}),}


       

class Bookform(forms.ModelForm):

        class Meta:
                model=Book
                fields=[
                        'title',
                        'author',
                        'photo_book',
                        'photo_author',
                        'pages',
                        'prices',
                        'rental_price_day',
                        'rental_period',
                        'total_rental',
                        'active',
                        'status',
                        'category',
                        ]
        



                widgets={
                        
                        'title': forms.TextInput(attrs={'class':'form-control'}),
                        'author': forms.TextInput(attrs={'class':'form-control'}),
                        'photo_book': forms.TextInput(attrs={'class':'form-control'}),
                        'photo_author': forms.TextInput(attrs={'class':'form-control'}),
                        'pages': forms.TextInput(attrs={'class':'form-control'}),
                        'prices': forms.TextInput(attrs={'class':'form-control'}),
                        'rental_price_day': forms.TextInput(attrs={'class':'form-control', 'id':'rentalprice'}),
                        'rental_period': forms.NumberInput(attrs={'class':'form-control', 'id':'rentalperiods'}),
                        'total_rental': forms.NumberInput(attrs={'class':'form-control', 'id':'totalrental'}),
                        'active': forms.TextInput(attrs={'class':'form-control'}),
                        'status': forms.TextInput(attrs={'class':'form-control'}),
                        'category': forms.Select(attrs={'class':'form-control'}),
                }


