from django import forms

class signupForm(forms.Form):
    fname = forms.CharField(max_length=50, label='Enter your First Name')
    lname = forms.CharField(max_length=50, label='Enter your Last Name')
    email = forms.CharField(max_length=100, label='Enter Your Email', widget=forms.EmailInput)
    password = forms.CharField(max_length=100, label='Enter your password', widget=forms.PasswordInput)

class loginForm(forms.Form):
    useremail = forms.CharField(max_length=100, label='Enter your Email', widget=forms.EmailInput)
    userpassword = forms.CharField(max_length=100, label='Enter your password', widget=forms.PasswordInput)

class contactForm(forms.Form):
    userfname = forms.CharField(max_length=50, label='Enter your First Name ', label_suffix="")
    userlname = forms.CharField(max_length=50, label='Enter your Last Name ', label_suffix="")
    useremail = forms.CharField(max_length=100, label='Enter your Email ', widget=forms.EmailInput, label_suffix="")
    usersub = forms.CharField(max_length=50, label_suffix="", label='Sub ')
    usermsg = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'cols': '100', 'rows': '5'}), label_suffix="", label='Type your msg...    ')

class sitedataForm(forms.Form):
    bikeimage = forms.ImageField(label='Add Bike Image ', label_suffix="")
    biketitle = forms.CharField(max_length=100, label='Enter Bike Title ', label_suffix="")
    bikeprice = forms.CharField(max_length=20, label='Enter Bike Price ', label_suffix="")
    bikeinfo = forms.CharField(max_length=100, label='Enter Bike Information ', label_suffix="")
    bikecategory = forms.CharField(max_length=100, label='Enter Bike Category ', label_suffix="")

    
    
