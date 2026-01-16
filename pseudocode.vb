BEGIN

FUNCTION DoCommand(command)
    IF URL box is empty THEN
        target ← localhost
    ELSE
        target ← URL from box
    END IF

    Clear output box
    Display "command working..."

    Run command with target
    Display command output in output box
END FUNCTION

FUNCTION Submit(command)
    IF Confirm checkbox is checked THEN
        Ask user to confirm
        IF user selects NO THEN
            RETURN
        END IF
    END IF

    DoCommand(command)
END FUNCTION

FUNCTION SaveOutput
    Ask user for filename
    IF user cancels THEN
        RETURN
    END IF

    Save output box text to file
END FUNCTION

Create main window

Create Confirm checkbox (checked by default)

Create Ping button → Submit("ping")
Create Tracert button → Submit("tracert")
Create Nslookup button → Submit("nslookup")

Create URL input box

Create output text box

Create Save button → SaveOutput

Wait for user actions

END