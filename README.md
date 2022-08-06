# Hunt Stats Logger
<p>
  <img src="assets/screenshots/huntapp.png" width=30% height=30%>
  <img src="assets/screenshots/huntapp2.png" width=30% height=30%>
  <img src="assets/screenshots/huntappsettings.png" width=20% height=20%>
</p>

<p>
This program was made to record hunt statistics in the game <b>Hunt: Showdown</b>.
<br>It works by tracking changes in the attributes.xml file, which is updated after every game, logging those changes to a local .json file, and uploading them to a local sqlite database.
<br>If the user is logged in, the records can be stored in a remote webserver, from which they can later be restored.
</p>
<p>
App has to be running for hunts to be logged.
</p>

 When running the app for the first time, click on Settings, Select Folder, and choose your Hunt install directory ( something like C:/Steam/steamapps/common/Hunt Showdown ) .
 Then enter your Steam username and click Update Steam Name.

 If you choose, you can create a username and login, which will allow the app to store the records in a remote webserver, from which you can later restore them.

Restore old records by clicking "sync with server." 
# How to run
#
## Easiest method, maybe:
Requires pyinstaller.
<ol>
<li>Right click on <b>build.ps1</b>, and choose <b>Run with PowerShell</b>.
<li>Open <b>HuntStats.exe</b>.
</ol>

#
## To run script directly:
### You'll need to have Python3 and pip installed.  Get Python3 <a href="https://www.python.org/downloads/windows/">here</a>.  Pip should be included.
<p>To verify they're installed, open a cmd prompt or PowerShell, and execute `python --version; pip --version` which will output the version you have installed.</p>

open a PowerShell or cmd prompt, navigate to the git directory, and execute:
```
$ pip install -r requirements.txt;  python ./src/main.py
```
Alternatively, right click on <b>startapp.ps1</b> and choose <b>Run with PowerShell</b>, which will automatically execute the above command.

#
## To build executable:
Requires pyinstaller.
```
$ pip install -r requirements.txt; pyinstaller main.spec
```
executable will then be found at ./dist/main/main.exe
#


