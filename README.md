A work in progress tool for relaying the RDP status of particularly powerful lab computers to an API on PythonAnywhere so that a Discord bot can inform students if the RDP connection is available or not.

Ran into a networking issue where the wired network firewall is more strict than the wireless network firewall. At least I am guessing it's the firewall. I can curl the API subdomain just fine on wireless connections (eg my laptop) but can only curl the main domain of my PythonAnywhere webpage on the lab workstation. 

The solution is to build an intermediate device that communicates with the API over wireless so I can get the RDP connection stats out of the LAN. This is literally the PiBox idea I have in one of my repos (aka a JumpBoxJumpServer you see in embedded systems, aka a bastion host except mine knows how to read. You ever read a never ending story?).

Until someone gives me a job I will forego building it with a cell hat and focus on using SSH to tunnel into the LAN for rdp connection extraction extravaganza.
