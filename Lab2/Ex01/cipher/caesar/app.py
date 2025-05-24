from flask import Flask, render_template, request
from cipher.cipher import CaesarCipher

app = Flask(__name__)
#router
@app.route('/')
def home():
    return render_template('index.html')

#router router for caesar cipher
@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form[inputPlaintext]
    key = int(request.form[inputKeyPlaintext])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key,)
    return f"text: {text}<br/>key: {key}<br/> encrypted text: {encrypted_text}"

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form[inputCiphertext]
    key = int(request.form[inputKeyCiphertext])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key,)
    return f"text: {text}<br/>key: {key}<br/> decrypted text: {decrypted_text}"

#main
if __name__ == '__main__':
    app.run(host="0.0.0.0", post=5000, debug=True)
