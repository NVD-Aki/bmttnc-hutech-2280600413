from flask import Flask, render_template, request

app = Flask(__name__)

# --- Caesar Cipher functions ---
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

# --- Vigenere Cipher functions ---
def vigenere_encrypt(text, key):
    result = []
    key = key.lower()
    key_len = len(key)
    key_indices = [ord(k) - ord('a') for k in key]
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_index = key_indices[i % key_len]
            encrypted_char = chr((ord(char) - base + key_index) % 26 + base)
            result.append(encrypted_char)
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(text, key):
    result = []
    key = key.lower()
    key_len = len(key)
    key_indices = [ord(k) - ord('a') for k in key]
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            key_index = key_indices[i % key_len]
            decrypted_char = chr((ord(char) - base - key_index + 26) % 26 + base)
            result.append(decrypted_char)
        else:
            result.append(char)
    return "".join(result)

# --- Rail Fence Cipher functions ---
def rail_fence_encrypt(text, num_rails):
    if num_rails <= 1:
        return text
    rail = ['' for _ in range(num_rails)]
    row = 0
    direction = 1

    for char in text:
        rail[row] += char
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1

    return ''.join(rail)

def rail_fence_decrypt(cipher, num_rails):
    if num_rails <= 1:
        return cipher

    pattern = list(range(num_rails)) + list(range(num_rails - 2, 0, -1))
    pattern_len = len(pattern)

    row_idx = [pattern[i % pattern_len] for i in range(len(cipher))]
    sorted_rows = sorted(range(len(cipher)), key=lambda i: row_idx[i])
    sorted_cipher = [''] * len(cipher)

    i = 0
    for r in range(num_rails):
        for j in range(len(cipher)):
            if row_idx[j] == r:
                sorted_cipher[j] = cipher[i]
                i += 1

    return ''.join(sorted_cipher)

# --- Playfair Cipher functions ---
def generate_playfair_matrix(key):
    key = key.upper().replace('J', 'I')
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used:
            matrix.append(char)
            used.add(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def prepare_text(text):
    text = text.upper().replace('J', 'I')
    prepared = ''
    i = 0
    while i < len(text):
        char1 = text[i]
        char2 = text[i + 1] if i + 1 < len(text) else 'X'
        if char1 == char2:
            prepared += char1 + 'X'
            i += 1
        else:
            prepared += char1 + char2
            i += 2
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared

def playfair_encrypt(text, key):
    matrix = generate_playfair_matrix(key)
    text = prepare_text(''.join(filter(str.isalpha, text)))
    result = ''

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]

    return result

def playfair_decrypt(text, key):
    matrix = generate_playfair_matrix(key)
    result = ''

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]

    return result

# --- Transposition Cipher (Columnar) functions ---
def transposition_encrypt(text, key):
    # key = số cột
    key = int(key)
    text = text.replace(" ", "")
    # Tạo ma trận với key cột
    matrix = [''] * key
    for i, char in enumerate(text):
        matrix[i % key] += char
    return ''.join(matrix)

def transposition_decrypt(cipher, key):
    key = int(key)
    # Tính số hàng (row)
    num_rows = len(cipher) // key
    if len(cipher) % key != 0:
        num_rows += 1

    # Tạo danh sách độ dài cột (vì cột cuối có thể ít ký tự hơn)
    col_lengths = [num_rows] * key
    # Tính số ký tự thừa trong cột cuối
    excess = (num_rows * key) - len(cipher)
    for i in range(excess):
        col_lengths[-(i+1)] -= 1

    # Lấy ký tự từng cột
    cols = []
    index = 0
    for length in col_lengths:
        cols.append(cipher[index:index+length])
        index += length

    # Đọc hàng theo thứ tự để giải mã
    result = ''
    for i in range(num_rows):
        for col in cols:
            if i < len(col):
                result += col[i]
    return result

# --- Routes ---
@app.route('/')
def home():
    return render_template('home.html')

# --- Caesar Routes ---
@app.route('/caesar')
def caesar():
    return render_template('caesar.html',
                           encrypt_result=None,
                           decrypt_result=None,
                           encrypt_input_text='',
                           decrypt_input_text='',
                           inputKeyPlain='')

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
                           encrypt_input_text=text,
                           decrypt_input_text=encrypted_text,
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
                           decrypt_input_text=text,
                           encrypt_input_text=decrypted_text,
                           inputKeyPlain=shift)

# --- Vigenere Routes ---
@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html',
                           encrypt_result=None,
                           decrypt_result=None,
                           encrypt_input_text='',
                           decrypt_input_text='',
                           inputKeyPlain='')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt_route():
    text = request.form.get('inputPlainText', '')
    key = request.form.get('inputKeyPlain', '').strip()
    if not key.isalpha():
        encrypt_result = "Lỗi: Khóa phải là chuỗi chữ cái."
    else:
        encrypt_result = vigenere_encrypt(text, key)
    return render_template('vigenere.html',
                           encrypt_result=encrypt_result,
                           decrypt_result=None,
                           encrypt_input_text=text,
                           decrypt_input_text=encrypt_result,
                           inputKeyPlain=key)

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt_route():
    text = request.form.get('inputPlainText', '')
    key = request.form.get('inputKeyPlain', '').strip()
    if not key.isalpha():
        decrypt_result = "Lỗi: Khóa phải là chuỗi chữ cái."
    else:
        decrypt_result = vigenere_decrypt(text, key)
    return render_template('vigenere.html',
                           decrypt_result=decrypt_result,
                           encrypt_result=None,
                           decrypt_input_text=text,
                           encrypt_input_text=decrypt_result,
                           inputKeyPlain=key)

# --- Rail Fence Routes ---
@app.route('/railfence')
def railfence():
    return render_template('railfence.html',
                           encrypt_result=None,
                           decrypt_result=None,
                           encrypt_input_text='',
                           decrypt_input_text='',
                           inputKeyPlain='')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt_route():
    text = request.form.get('inputPlainText', '')
    try:
        num_rails = int(request.form.get('inputKeyPlain', 2))
        if num_rails < 2:
            raise ValueError
    except ValueError:
        encrypt_result = "Lỗi: Số hàng phải là số nguyên ≥ 2."
        return render_template('railfence.html',
                               encrypt_result=encrypt_result,
                               decrypt_result=None,
                               encrypt_input_text=text,
                               decrypt_input_text='',
                               inputKeyPlain='')
    encrypted = rail_fence_encrypt(text, num_rails)
    return render_template('railfence.html',
                           encrypt_result=encrypted,
                           decrypt_result=None,
                           encrypt_input_text=text,
                           decrypt_input_text=encrypted,
                           inputKeyPlain=num_rails)

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt_route():
    text = request.form.get('inputPlainText', '')
    try:
        num_rails = int(request.form.get('inputKeyPlain', 2))
        if num_rails < 2:
            raise ValueError
    except ValueError:
        decrypt_result = "Lỗi: Số hàng phải là số nguyên ≥ 2."
        return render_template('railfence.html',
                               decrypt_result=decrypt_result,
                               encrypt_result=None,
                               decrypt_input_text=text,
                               encrypt_input_text='',
                               inputKeyPlain='')
    decrypted = rail_fence_decrypt(text, num_rails)
    return render_template('railfence.html',
                           decrypt_result=decrypted,
                           encrypt_result=None,
                           decrypt_input_text=text,
                           encrypt_input_text=decrypted,
                           inputKeyPlain=num_rails)

# --- Playfair Routes ---
@app.route('/playfair')
def playfair():
    return render_template('playfair.html',
                           encrypt_result=None,
                           decrypt_result=None,
                           encrypt_input_text='',
                           decrypt_input_text='',
                           inputKeyPlain='')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt_route():
    text = request.form.get('inputPlainText', '')
    key = request.form.get('inputKeyPlain', '').strip()
    if not key.isalpha():
        encrypt_result = "Lỗi: Khóa phải là chuỗi chữ cái."
    else:
        encrypt_result = playfair_encrypt(text, key)
    return render_template('playfair.html',
                           encrypt_result=encrypt_result,
                           decrypt_result=None,
                           encrypt_input_text=text,
                           decrypt_input_text=encrypt_result,
                           inputKeyPlain=key)

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt_route():
    text = request.form.get('inputPlainText', '')
    key = request.form.get('inputKeyPlain', '').strip()
    if not key.isalpha():
        decrypt_result = "Lỗi: Khóa phải là chuỗi chữ cái."
    else:
        decrypt_result = playfair_decrypt(text, key)
    return render_template('playfair.html',
                           decrypt_result=decrypt_result,
                           encrypt_result=None,
                           decrypt_input_text=text,
                           encrypt_input_text=decrypt_result,
                           inputKeyPlain=key)

# --- Transposition Routes ---
@app.route('/transposition')
def transposition():
    return render_template('transposition.html',
                           encrypt_result=None,
                           decrypt_result=None,
                           encrypt_input_text='',
                           decrypt_input_text='',
                           inputKeyPlain='')

@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt_route():
    text = request.form.get('inputPlainText', '')
    key = request.form.get('inputKeyPlain', '').strip()
    try:
        key_int = int(key)
        if key_int < 2:
            raise ValueError
        encrypt_result = transposition_encrypt(text, key_int)
    except ValueError:
        encrypt_result = "Lỗi: Khóa phải là số nguyên ≥ 2."
    return render_template('transposition.html',
                           encrypt_result=encrypt_result,
                           decrypt_result=None,
                           encrypt_input_text=text,
                           decrypt_input_text=encrypt_result,
                           inputKeyPlain=key)

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt_route():
    text = request.form.get('inputPlainText', '')
    key = request.form.get('inputKeyPlain', '').strip()
    try:
        key_int = int(key)
        if key_int < 2:
            raise ValueError
        decrypt_result = transposition_decrypt(text, key_int)
    except ValueError:
        decrypt_result = "Lỗi: Khóa phải là số nguyên ≥ 2."
    return render_template('transposition.html',
                           decrypt_result=decrypt_result,
                           encrypt_result=None,
                           decrypt_input_text=text,
                           encrypt_input_text=decrypt_result,
                           inputKeyPlain=key)

if __name__ == '__main__':
    app.run(debug=True)
