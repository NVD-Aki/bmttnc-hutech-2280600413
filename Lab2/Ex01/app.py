from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route('/', methods=['GET'])
def home():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.form.get('inputPlainText', '')
    try:
        shift = int(request.form.get('inputKeyPlain', 0))
    except ValueError:
        shift = 0
    encrypted_text = caesar_encrypt(text, shift)
    return render_template('caesar.html',
                           encrypt_result=encrypted_text,
                           decrypt_result=None,
                           encrypt_input_text=text,           # giữ lại input encrypt
                           decrypt_input_text=encrypted_text, # điền kết quả mã hóa vào ô decrypt
                           inputKeyPlain=shift)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.form.get('inputPlainText', '')
    try:
        shift = int(request.form.get('inputKeyPlain', 0))
    except ValueError:
        shift = 0
    decrypted_text = caesar_decrypt(text, shift)
    return render_template('caesar.html',
                           decrypt_result=decrypted_text,
                           encrypt_result=None,
                           decrypt_input_text=text,             # giữ lại input decrypt
                           encrypt_input_text=decrypted_text,   # điền kết quả giải mã vào ô encrypt
                           inputKeyPlain=shift)

if __name__ == '__main__':
    app.run(debug=True)
