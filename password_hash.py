import bcrypt

# パスワードをハッシュ化する
hashed_password = bcrypt.hashpw(b'password', bcrypt.gensalt())

# ハッシュ化されたパスワードを表示する
print(hashed_password)

# パスワードの検証
if bcrypt.checkpw("password".encode('utf-8'), hashed_password):
    print("パスワードが一致しました")
else:
    print("パスワードが一致しません")