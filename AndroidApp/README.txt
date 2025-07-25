These are all of the files needed to build the android app or .apk file with buildozer
This can be done on Windows in WSL, it can be done in PowerShell but it's a bit more tricky and I recommend just install WSL ubuntu or use a Linux machine if you have one
To install all the packages needed to compile I recommend using Claude.ai and uploading the buildozer and main.py that will give Clause all the info needed to install the required packages to build
My appologies for this as I did not stop and take notes on everything I had to install to do the buildozer and make the .apk file but it worked and the apk is working on my phone just fine
You basically just put all of the files in a directory, run "buildozer android debug" (after all the needed packages are installed) and it will build the apk file in a subdirectory /bin of your working directory
