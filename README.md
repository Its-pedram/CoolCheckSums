
# CoolCheckSums
Check/Verify the checksums (MD5, SHA1, SHA224, SHA256, SHA384, SHA512) of various files with this very cool tool!
# Table of Content
|Content|Click To Go|
|--|--|
|What's CoolCheckSums?|---->[🔽](#What-is-CoolCheckSums)<----|
|Why Does This Exist?|---->[🔽](#Why-Does-This-Exist)<----|
|How Can I Use It?|---->[🔽](#How-Can-I-Use-It)<----|
|Any Plans?|---->[🔽](#Any-Plans)<----|
# What is CoolCheckSums
CoolCheckSums is a tool that allows you to verify & get the hash of a file that you like.
# Why Does This Exist
So I was bored and decided to see what can I make in a few hours. I also wanted to play around with Python a little bit to use it on some other projects maybe. The main reason I made this was because I wanted a way to verify the checksums of the linux distros I download (eventhough I don't really even do that).
# How Can I Use It
Right Now, the program is very simple and has a very simple command syntax:
Notes:
 - You need to have Python 3 installed.
 - The following commands may be different depending on your OS and System.
 - You atleast need the first two arguments.

Use `-help` instead of the arguments to see the help menu in the program.

***Windows 10:***
Example For The `-compare` & `-c` arguments:

    python .\ccs.py -c <FileName.Ext> <Checksum> [Type]
Example For The `-get` & `-g` arguments:

    python .\ccs.py -g <FileName.Ext> [Type]

***Linux***:
Example For The `-compare` & `-c` arguments:

    python3 ccs.py -compare <FileName.Ext> <Checksum> [Type]
Example For The `-get` & `-g` arguments:

    python3 ccs.py -get <FileName.Ext> [Type]

***macOS***:

    Lol No. You see I don't use a mac on a daily basis and I never will. But it's probably the same as Linux.
 **Bonus (Windows Only (for now)): You can add the folder containing [ccs.py](https://github.com/Its-pedram/CoolCheckSums/blob/main/CoolCheckSums/CoolCheckSums.py) and [ccs.bat](https://github.com/Its-pedram/CoolCheckSums/blob/main/CoolCheckSums/ccs.bat) to your system's PATH so you can use this anywhere with the `ccs` command.**

**Description Of Each Argument:**

 - FileName: This option requires you to pass it the file path or the file name. **Required In All Cases.**
 - Checksum: This is basically the sum you currently have and want to compare it to the actual checksum of the file. **Required Only For `-c & -compare`.**
 - Type: If you need to compare the checksums, this is the type of the checksum that you passed in the previous argument. If you need to just simply get the checksum of your file, this is the type of checksum you want the program to output.
 - Supported types are: MD5, SHA1, SHA224, SHA256, SHA384, SHA512 & Auto/All.
 **If you use the *Auto* argument, the program will try to generate all the hashes above until one matches the hash you passed in argument two.**
  **If you use the *All* argument, the program will try to generate all the hashes above.**
 # Any Plans
 
 - [x] Make a working cli version 
 - [x] Add a `-get` command to skip comparing the hashes and directly prompt the user with the file's hash.
 - [ ] Add the program to the Windows Context Menu (Right Click Menu) so you can check and determine the hash of the file selected.
 - [ ] Build a GUI to go with the Context Menu entry.
 - [x] Add support for more types.
