from pikepdf import Pdf
from tqdm import tqdm

passwords_file_name = "Python101/rockyou.txt"
pdf_file_name = "Python101/testfile.pdf"
new_pdf = Pdf.new()

with open(passwords_file_name, "rb") as passwords_file:
    for each_word in tqdm(passwords_file, unit=" word"):
        try:
            new_pdf.open(pdf_file_name,password=each_word.strip())
            print("\n Password found: ", each_word.strip())
            break
        except:
            continue
        else:
            print("BOOOOoooooo! The password was not found.")

'''
    for password in passwords_file:
        try:
            Pdf.open(pdf_file_name, password=password.strip())
            print(f"Password found! {password}")
            break
        except:
            continue
        else:
            print("Booo! No password found.")


new_pdf = Pdf.new()
with open(password_file, "rb") as pfile:
    for each_word in tqdm(pfile, total=num_words, unit=" word"):
        try:
            new_pdf.open(target_file,password=each_word.strip())
            print("\n Password found: ", each_word.strip())
            break
        except:
            continue
        else:
            print("BOOOOoooooo! The password was not found.")

'''