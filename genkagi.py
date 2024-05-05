from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# 鍵の生成
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# 秘密鍵の PEM 形式でのエクスポート
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

# 公開鍵の取得
public_key = private_key.public_key()

# 公開鍵の PEM 形式でのエクスポート
pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# PEM 形式の文字列に変換
pem_private_str = pem_private.decode("utf-8")
pem_public_str = pem_public.decode("utf-8")

print(pem_private_str.strip())
print("////////////////////")
print(pem_public_str.strip())
