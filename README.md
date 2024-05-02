Still a stupid name, still a useful service.

Use !rdpstatus to request a live update of the workstations' statuses.

Using a Discord webhook, server users can request a live status of the lab workstation RDP connections, including if the workstation is already logged in locally in an effot to prevent a session takeover.

The code in local_rdp_check.py needs to be turned into a service so that it can be run in the background when a workstation is logged off. 

Efforts with pywin32 and NSSM have so far been unsuccessful, I think due to the lab security setup. 

Pywin32 struggles to install the service, likely because I am missing something in the programming. NSSM can install the service, but py.exe quits and leaves the bot hanging. You can see the errors in Event Viewer. I'd like to think it is not my fault but you know how it goes.. it probably is the dev misunderstanding something. 

So going forward:

* Convert local_rdp_check.py into a service or application that can run in the background

* Create a manager that can update the service for code changes (no idea how but this would be a very helpful feature of the app)
