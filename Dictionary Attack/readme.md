# Dictionary Attack - final

This is the main file to look at and what I ended up using for the file project. This file takes input in the format of: "python3 pass_atmpt.py 26 27"
The two numbers that follow are the indicies of the length array you wish to use. This was done so that the file could be broken up and multiple processes
could be run to speed up the runtime. It still takes many days to actually crack a password but this version is the fastest of the three. It took approximately
a week to break my test password

sshpass also needs to be installed for this program to work correctly since this is used to give the password and the account in the same line.

It also requires the crackstation-human-only.txt file to run properly. This file was too large to include in the commit. The link to downoad it is here: https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm
This list is a list of 64 million known human passwords.

# Evolution of Dictionary Attack

This attack was my intial brute force attack. The intial version generated all possible permutations of 4 characters and their capitilized versions. 
Then it combines every 4 letter permutation with every other 4 letter permutation and writes it to file to create a list of passwords. This attempts
to create a list of 400 billion words which is a file that is far too large. This file was reporposed for a different attack.

## Dictionary Attack v1

This version attempted to cut down the runtime significantly by using a list of dictionary words to generate the passwords file. The file used was pss_dict.py.
login_pass.py uses the generated passwords to then attempt to break into the account. To generate the passwords each word is combined with every other word
and added to the list if their length together is greater than 7. This program significantly cuts down on runtime and file sizes, however, the file size 
and runtime are still far too large.

## Dictionary Attack v2

This version is similar to the final version since it uses the same list of 64 million known passwords. The difference is this one tries to first generate
a file contained all passwords of length greater 7 and their capitilized versions then it attempts to test them on the server. This is a significant improvement
on the previous iterations but was not quite there. The final version speeds up runtime and storage significantly by not attempting to create a new file
and uses chunks of the list instead of the entire thing.
