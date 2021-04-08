from django import forms
class ChangePasswordForm(forms.Form):
    #username=current_password=forms.HiddenInput(max_length=100,required=True,widget=forms.CharField(attrs={'hidden'}))
    current_password=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'placeholder':"Enter your password",'id':'current_passwd'}))
    new_password=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'placeholder':"Enter new password",'id':'new_passwd'}))
    cnfrm_passwd=forms.CharField(max_length=100,required=True,widget=forms.PasswordInput(attrs={'placeholder':"confirm new password",'id':'cnfrm_passwd'}))