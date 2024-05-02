Still a stupid name, still a useful service.

Use !rdpstatus to request a live update of the workstations' statuses.

Using a Discord webhook, server users can request a live status of the lab workstation RDP connections, including if the workstation is already logged in locally in an effot to prevent a session takeover.

The code in local_rdp_check.py needs to be turned into a service so that it can be run in the background when a workstation is logged off. 

Efforts with pywin32 and NSSM have so far been unsuccessful, I think due to the lab security setup. Maybe try building the service outside lab resources and install it after (hence the Github)

Pywin32 struggles to install the service, likely because I am missing something in the programming. NSSM can install the service, but py.exe quits and leaves the bot hanging. You can see the errors in Event Viewer. I'd like to think it is not my fault but you know how it goes.. it probably is the dev misunderstanding something.. until it isn't. 

So going forward:

Major Efforts:
* Convert local_rdp_check.py into a service or application that can run in the background

* Create a manager that can update the service for code changes

Minor Efforts:
* Refactor code for readability (that means useful commments as well)

* Discord bot needs to clean up it's messages in the chat - when user issues command, delete the previous bot status updates first, then print new updates

* The message wording can be improved

* Can the updates be displayed side-by-side in Discord or even in one single message? Multiple updates take up a lot of channel real-estate
