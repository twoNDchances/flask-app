from secrets import token_hex
from cryptography.fernet import Fernet, InvalidToken
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode

def generate_secret_key_1024() -> str:
    """
    :return: a random secret key 1024 characters
    """
    return token_hex(1024)


def generate_secret_key_64():
    """
    :return: a random secret key 64 characters
    """
    return token_hex(64)

##############THIS PART FOR ENCRYPT/DECRYPT USER FILES##############

def _encrypt_file(file, key, save_path) -> None:
    cipher = AES.new(key, AES.MODE_EAX)

    # Đọc dữ liệu từ tệp hình ảnh
    with open(file, 'rb') as f:
        file_data = f.read()

    # Mã hóa dữ liệu hình ảnh
    ciphertext, tag = cipher.encrypt_and_digest(file_data)

    # Lưu trữ khóa và các thông tin khác liên quan vào tệp
    with open(save_path, 'wb') as f:
        f.write(key)
        f.write(cipher.nonce)
        f.write(tag)
        f.write(ciphertext)


def _decrypt_file(file) -> bytes:
    with open(file, 'rb') as f:
        key = f.read(16)
        nonce = f.read(16)
        tag = f.read(16)
        ciphertext = f.read()

    # Khởi tạo đối tượng AES cho giải mã
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # Giải mã dữ liệu
    decrypted_image_data = cipher.decrypt_and_verify(ciphertext, tag)

    # Lưu trữ dữ liệu đã giải mã thành tệp hình ảnh gốc
    # with open('pdf.pdf', 'wb') as f:
    #     f.write(decrypted_image_data)
    return decrypted_image_data


def _encrypt_to_base64(data: bytes) -> str:
    return b64encode(data).decode('utf-8')


def _generate_bytes(bytes: int) -> bytes:
    return get_random_bytes(bytes)

def _generate_bytes_for_url_crypto() -> bytes:
    return Fernet.generate_key()

def _encrypt_string(string: str, key: bytes):
    fernet = Fernet(key)
    return fernet.encrypt(string.encode())

def _decrypt_string(encrypted_string: str, key: bytes) -> str:
    try:
        fernet = Fernet(key)
        return fernet.decrypt(encrypted_string).decode()
    except:
        return False