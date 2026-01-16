START

Create window

Create checkbox called Confirm (checked by default)

Create buttons:

Ping

Tracert

Nslookup

IPConfig

Create text box to enter URL
Create output text box
Create Save button

FUNCTION DoCommand(command)
If command needs a URL

If URL box is empty

Use localhost

Else

Use URL from box

Clear output box
Show “command working…”
Run command
Display results in output box

FUNCTION Submit(command)
If Confirm checkbox is checked

Ask user “Are you sure?”

If user says NO

Stop

Run DoCommand(command)

FUNCTION SaveOutput
Ask user for filename
If user cancels

Stop

Save output text to file

Wait for user to click buttons