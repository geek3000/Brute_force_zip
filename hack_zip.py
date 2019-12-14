from zipfile import ZipFile
from termcolor import colored

file_zip = "task_zip.zip"
file_wordlist = "dico.txt"

print(colored("--------------Geek3000 brute force tool------------------------------", "red"))

is_cracked=False
i=0
with ZipFile(file_zip) as zip_file:
    with open(file_wordlist) as wordlist:
        for word in wordlist.readlines():
            word = word.strip('\n')
            i+=1
            print(colored("Number of tried words", "blue"), colored(i, "yellow"))
            try:
                zip_file.extractall(pwd=word.encode())
                print(colored("The password is ", "green"), colored(word, "red"))
                exit(0)
                is_cracked=True
            except RuntimeError:
                pass
if(not is_cracked):
    print(colored("Sorry The password isn't in this wordlist try another!!", "red"))
