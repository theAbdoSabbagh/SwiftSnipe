import base64

def tokenToId(token: str):
    try:
        token = token.split('.')[0]
        token += '=' * (-len(token) % 4)
        decoded_token = base64.b64decode(token).decode('utf-8')
        token = decoded_token.split('"')[0]
        return token
    except (IndexError, base64.binascii.Error, UnicodeDecodeError) as e:
        # print(f"Error occurred during token conversion: {str(e)}")
        return None
