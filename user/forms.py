from django import forms

class LoginForm(forms.Form):  #ders214 giris ekranı formu olustu
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget = forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50,label = "Kullanıcı Adı")   #Flasktaki WTF formu
    password = forms.CharField(max_length = 20,label = "Parola",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length = 20, label = "Parolayı Doğrula",widget = forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
        #yani parola ve confirm dolu mu demek (0 mı 1 mi gibi görecek)
            raise forms.ValidationError("Parolalar eşleşmiyor")
        #raise = kendimizin oluşturduğu bir hata fırlatmaya yarar.

        values = {
                "username" : username,
                "password" : password
        }
        return values