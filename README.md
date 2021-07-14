
# CheckASum
Check/Verify the checksums (MD5, SHA1, SHA256) of various files with this very cool tool!
# Table of Content
|Content|Click To Go|
|--|--|
|What's CheckASum?|---->[🔽](#What's-CheckASum)<----|
|Why Does This Exist?|---->[🔽](#Why-Does-This-Exist)<----|
|How Can I Use It?|---->[🔽](#How-Can-I-Use-It)<----|
|Any Plans?|---->[🔽](#Any-Plans)<----|
# What's CheckASum
CheckASum is a tool that allows you to verify (& get) the hash of a file that you like.
# Why Does This Exist
So I was bored and decided to see what can I make in a few hours. I also wanted to play around with Python a little bit to use it on some other projects maybe. The main reason I made this was because I wanted a way to verify the checksums of the linux distros I download (eventhough I don't really even do that).
# How Can I Use It
Right Now, the program is very simple and has a very simple command syntax:
Notes:
 - You need to have Python 3 installed.
 - The following commands may be different depending on your OS and System.
 - You atleast need the first two arguments.

Use `-help` instead of the arguments to see the help menu in the program.

Windows 10:

    python .\CheckASum.py <FileName.Ext> <Checksum> [Type]
Linux:

    python3 .\CheckASum.py <FileName.Ext> <Checksum> [Type]
macOS:

    Lol No. You see I don't use a mac on a daily basis and I never will. But it's probably the same as Linux.
 **Bonus: You can add the folder containing [CheckASum.py](https://github.com/Its-pedram/CheckASum/blob/main/CheckASum/CheckASum.py) and cas.bat to your system's PATH so you can use this anywhere with the `cas` command.**
**How to use the arguments:**

 - FileName (Required): Just simply pass the file name or the file path.
 - Checksum (Required): This is basically the sum you currently have and want to compare it to the actual checksum of the file.
 - Type (Optional): This is the type of the checksum that you passed in the previous argument. Supported types are: MD5, SHA1, SHA256 & Auto.
 **If you use the auto argument, the program will try to generate all the hashes above until one matches the hash you passed in argument two.**
 # Any Plans
 
 - [x] Make a working cli version 
 - [ ] Add a `-get` command to skip comparing the hashes and directly prompt the user with the file's hash.
 - [ ] Add the program to the Windows Context Menu (Right Click Menu) so you can check and determine the hash of the file selected.
 - [ ] Build a GUI to go with the Context Menu entry.
 - [ ] Add support for more types.
