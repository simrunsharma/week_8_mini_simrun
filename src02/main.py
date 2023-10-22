import sqlite3
import random
import csv
import click
import emoji
import fire 
import pytest

# import sys
# #sys.path.append('../week7_afraa_simrun_fortune_cookie/src/main.py')
# sys.path.insert(0,"./src02")
# from lib import fetch_value_from_db,random_no, createDB  # noqa: E401



def caesar_cipher_encrypt(text, shift=3):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = ((char_code - ord('a') + shift) % 26) + ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            encrypted_text += char_code
        else:
            encrypted_text += char  # Preserve non-alphabet characters
    return encrypted_text

def caesar_cipher_decrypt(text, shift=3):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()
            char = char.lower()
            char_code = ord(char)
            char_code = ((char_code - ord('a') - shift) % 26) + ord('a')
            if is_upper:
                char_code = chr(char_code).upper()
            else:
                char_code = chr(char_code)
            decrypted_text += char_code
        else:
            decrypted_text += char  # Preserve non-alphabet characters
    return decrypted_text

def fetch_value_from_db(rand_num):
      # Check if the random number is within the valid range
    if 1 <= rand_num <= 1017:
        conn = sqlite3.connect("fortune.db")
        cursor = conn.cursor()
        # Subtract 1 from the random number since Python uses 0-based indexing
        row_number = rand_num - 1
        cursor.execute('SELECT encrypted_fortune FROM fortune WHERE id = ?', (row_number,))
        temp = cursor.fetchone()
        # Decrypts value before sending back to terminal
        # temp = ('Zkhq qrwklqj jrhv uljkw… jr ohiw.',)
        # thus temp[0] should be used to fetch only the encrypted fortune i.e. Zkhq qrwklqj jrhv uljkw… jr ohiw.
        decrypted_fortune = caesar_cipher_decrypt(temp[0])
        
        return decrypted_fortune # Random number was out of range
    else:
        return "Random Number out of Range"

def random_no():
    random_number = random.randint(2, 1018)
    return random_number

def createDB(dbname="fortune.db"):
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS fortune')
    cursor.execute('''CREATE TABLE IF NOT EXISTS fortune (
                    id INTEGER PRIMARY KEY,
                    encrypted_fortune TEXT
                )''')

    # Read the fortunes from the CSV, encrypt them and insert them into the database
    with open('data_fortune/Fortune_Cookies_Dataset.csv', 'r') as encrypted_file:
        encrypted_fortunes = csv.reader(encrypted_file)
        for row in encrypted_fortunes:
            encrypted_fortune = caesar_cipher_encrypt(row[0])
            cursor.execute("INSERT INTO fortune (encrypted_fortune) VALUES (?)", (encrypted_fortune,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()



# try:
#     import lib
# except ModuleNotFoundError:
#     sys.path.insert(1, './src')
#     import lib

@click.command()

def main():
    createDB()
    # print("\nFortune db created \n")
    randNum = random_no()
    # print("Random number Generated is: ", randNum)
    fortune_text = fetch_value_from_db(randNum)
    x = emoji.emojize(":sparkles:")
    print(f"\nYour fortune for the day is:\n{x} {fortune_text} {x}")
    print("\n")

@pytest.mark.benchmark(group="Python")
def test_encrypt(benchmark):
    benchmark(caesar_cipher_encrypt,"Off to the bunker. Every person for themselves")

if __name__ == "__main__":
    fire.Fire(main)