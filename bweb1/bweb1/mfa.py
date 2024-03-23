import pyotp
import qrcode


def create_code():
    #key= pyotp.random_base32()
    key= "ThisMyScretKeyItHelpDesk"
    print(key)
    uri= pyotp.totp.TOTP(key).provisioning_uri(name="merhaba", issuer_name="ithelpdesk")

    print(uri)

    qrcode.make(uri).save("otp.png")

def otp(token):
    ky= "ThisMyScretKeyItHelpDesk"
    totp= pyotp.TOTP(ky)
    result= totp.verify(token)
    print(token)
    print(result)
    

otp("908308")
    




                        