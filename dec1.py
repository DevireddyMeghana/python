def login(func):
    def inner():
        un=input("Enter the Username:")
        psd=input("Enter the Password:")
        if un=="silent_soul" and psd=="Maggi":
           return func()
        else:
            return "Invalid Credentials"
    return inner
@login
def securefile():
    return "Secret File"
print(securefile())