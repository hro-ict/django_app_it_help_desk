import pyotp
import qrcode

import base64


def create_code():
    #key= pyotp.random_base32()
    key= "ThisMyScretKeyItHelpDesk"
    print(key)
    uri= pyotp.totp.TOTP(key).provisioning_uri(name="django", issuer_name="ithelpdesk")

    print(uri)

    qrcode.make(uri).save("otp.png")

def otp(token):
    ky= "ThisMyScretKeyItHelpDesk"
    totp= pyotp.TOTP(ky)
    result= totp.verify(token)
    print(token)
    print(result)
    
def convert_to_base64():
    with open("otp.png", "rb") as img_file:
        base64_encoded_image = base64.b64encode(img_file.read()).decode()

# README dosyasına QR kodunu ekleme
    with open("README.md", "a") as readme_file:
        readme_file.write(f"\n![OTP QR Code](data:image/png;base64,{base64_encoded_image})\n")

    


convert_to_base64()

                        