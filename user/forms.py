from django import forms

from user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'dating_sex',
            'location',
            'min_distance',
            'max_distance',
            'min_dating_age',
            'max_dating_age',
            'vibration',
            'only_matche',
            'auto_play',
        ]

    def clean_max_distance(self):
        '''检查最大距离'''
        cleaned_data = super().clean()
        if cleaned_data['min_distance'] > cleaned_data['max_distance']:
            raise forms.ValidationError('最小距离不能大于最大距离')
        return cleaned_data['max_distance']

    def clean_max_dating_age(self):
        '''检查最大年龄'''
        cleaned_data = super().clean()
        if cleaned_data['min_dating_age'] > cleaned_data['max_dating_age']:
            raise forms.ValidationError('最小年龄不能大于最大年龄')
        return cleaned_data['max_dating_age']
