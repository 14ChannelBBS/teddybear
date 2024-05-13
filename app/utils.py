import base64
import hashlib
import hmac
from datetime import datetime

from httpsig import HeaderSigner
from datetime import datetime

from .config import Config

def verify_signature(signature_header, method, path, headers, public_key):

    # 署名ヘッダーから署名情報を取得
    signature_info = {}
    for pair in signature_header.split(','):
        key, value = pair.strip().split('=', 1)
        signature_info[key] = value.strip('"')

    # 署名アルゴリズムのチェック
    if signature_info['algorithm'] != 'rsa-sha256':
        return False

    # 必要なヘッダーの抽出
    required_headers = signature_info['headers'].split()

    # メソッドとパスからリクエストターゲットを生成
    request_target = f"{method.lower()} {path}"

    # 署名計算用のメッセージを構築
    signing_string = ""
    for header_name in required_headers:
        if header_name == '(request-target)':
            signing_string += request_target + '\n'
        elif header_name in headers:
            signing_string += header_name.lower() + ': ' + headers[header_name] + '\n'

    signing_string += '\n'  # 最後に空行を追加

    # 署名を検証
    try:
        signature = base64.b64decode(signature_info['signature'])
        verifier = hmac.new(public_key, signing_string.encode('utf-8'), hashlib.sha256)
        return hmac.compare_digest(signature, verifier.digest())
    except Exception as e:
        print(f"Error verifying signature: {e}")
        return False
    
def sign_headers(mydata, method, path):
    sign = HeaderSigner(
        f'https://{Config.serverAddress}/u/{mydata["id"]}#main-key', # keyId Personのid
        mydata['publicKeyPem'], # 秘密鍵
        algorithm='rsa-sha256',
        headers=['post', 'date']
    ).sign({'Date': datetime.now().isoformat()}, method=method, path=path)
    auth = sign.pop('authorization')
    sign['Signature'] = auth[len('Signature '):] if auth.startswith('Signature ') else ''
    return sign