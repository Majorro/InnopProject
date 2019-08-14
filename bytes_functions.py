import base64


def bytes_to_base64(bytes_):
    encoded = str(base64.b64encode(bytes_))[2:-1]
    return encoded


def text_to_base64(text):
    encoded = base64.b64encode(text.encode('UTF-8'))
    return encoded


def base64_to_text(base64text):
    decoded = base64.b64decode(base64text).decode('UTF-8')
    return decoded


# testing code and decode data
'''
    text = 'привет как дела?31'
    encode = text_to_base64(text)
    print(encode)
    decoded = base64_to_text(encode)
    print(decoded)
'''




