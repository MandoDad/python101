import os
from pikepdf import Pdf
from tqdm import tqdm

print("Current dir: ", os.getcwd())
password_file = "Python101/rockyou.txt"
target_file = "Python101/new_testfile.pdf"

#count and print the number of passwords
num_words = len(list(open(password_file, "rb")))

print("Number of total passwords: ", num_words)
#new_pdf = Pdf.new()
with open(password_file, "rb") as pfile:
    for each_word in tqdm(pfile, total=num_words, unit=" word"):
        try:
            Pdf.open(target_file,password=each_word.strip())
            print("\n Password found: ", each_word.strip())
            break
        except:
            continue
        else:
            print("BOOOOoooooo! The password was not found.")


