from pikepdf import Pdf
import os
print("current dir:", os.getcwd())
target_file = "Python101/Challenge-13-InfoSec101Day4_464967_soylamassexy.pdf"
password_file = "Python101/rockyou.txt"
#count and print the number of passwords
num_words = len(list(open(password_file, "rb")))
print("number of passwords:", num_words)
#new_pdf = Pdf.new()
with open(password_file, "rb") as pfile:
    for each_word in pfile:
        #print(f"Try: {each_word}")
        try:
            Pdf.open(target_file, password=each_word.strip())
            print("\n Password found: ", each_word.strip())
            break
        except:
            continue
        else:
            print("NOOOOOOOOOOOOOO! I wasted ALL THAT TIME.")