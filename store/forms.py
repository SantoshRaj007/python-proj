from django import forms
from store.models import ReviewRating

class ReviewForm(forms.Form):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']