
#  Polyglot v3 node server iTach Copyright (C) 2021 Javier Refuerzo

Node server can send IR commands to the Global Cache iTach devices

## Installation
PG3 Node Server Store
Please reboot ISY before synchronization with UD Moble or human readable values may be shown as numbers. 

## Help
https://forum.universal-devices.com/forum/323-opensprinkler/

### Node Settings
The settings for this node are url, and manual code sets. All defined below. With the exception of Short Poll all items are set in custom params.

#### Short Poll
   * Not used

#### Long Poll
   * Not used


#### url
   * The local IP Address of the iTach devcie, this should be fully qualified starting with "http://".


## Requirements

1. Polyglot V3.
2. ISY firmware 5.3.x or later
3. Opensprinkler firmware 2.1.9 (2019) or later. Please be sure to backup open sprinkler before upgrading firmware as you settings will be removed! https://openthings.freshdesk.com/support/home see User Manuals and select your hardware 3.x or 2.x

## Known Issues and limitations

1. Canging the order of IR codes in a codeset will change which devcie is triggered in programs, if adding new codes to a codeset add to the end of any current codes.
2. UD Mobile will only show buttons if there are less then 150 buttons in the codeset. This will be changed on app side in the future.
3. Codesets may be cutoff in Custom Config view port, but should be sent to the Node Server Correctly.
4. As of 2022.01.22 Nodes are not automatically deleted, i.e. the example device.  To delete the device remove/replace in Polyglot Custom Config. Then from ISY rightclick the controller node, then select ungroup, then right click on the device which is to be deleted and select delete. Finally right click the controller node and select group devices.

# Release Notes

- 2022.1.22 01/22/2022
   - Initial version published to github

# General

Custom Parameters: 
url: The ip address of the iTach device 

All other custom params are user input devices with the Global Cache IR Codes
key: The Device i.e. "Onkyo Receiver"
value: A Global Cache Control Tower IR Database Format

An email from Global Cache with IR Codes look as follows, although there may be many more. The "function, code1, hexcode1, code2, hexcode2" is optional. When imputing the following commands, the custom param key: "Onkyo Receiver" and the value would be all codes for the device.

"
function, code1, hexcode1, code2, hexcode2

"3D","sendir,1:1,1,38000,1,1,171,171,21,65,21,65,21,65,21,21,21,21,21,21,21,21,21,21,21,65,21,65,21,65,21,21,21,21,21,21,21,21,21,21,21,65,21,65,21,65,21,65,21,65,21,21,21,21,21,65,21,21,21,21,21,21,21,21,21,21,21,65,21,65,21,21,21,1792","0000 006D 0000 0022 00AB 00AB 0015 0041 0015 0041 0015 0041 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0041 0015 0041 0015 0041 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0041 0015 0041 0015 0041 0015 0041 0015 0041 0015 0015 0015 0015 0015 0041 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0015 0041 0015 0041 0015 0015 0015 0700",,

"ADD/DELETE","sendir,1:1,1,38000,1,1,170,170,22,64,22,64,22,64,21,22,21,22,21,22,21,22,21,22,21,65,21,65,21,65,21,22,21,22,21,22,21,22,21,22,21,65,21,22,22,22,21,65,21,65,21,22,21,22,21,22,22,22,21,65,21,65,21,22,21,22,21,65,21,65,21,65,21,1769","0000 006D 0000 0022 00AA 00AA 0016 0040 0016 0040 0016 0040 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0041 0015 0041 0015 0041 0015 0016 0015 0016 0015 0016 0015 0016 0015 0016 0015 0041 0015 0016 0016 0016 0015 0041 0015 0041 0015 0016 0015 0016 0015 0016 0016 0016 0015 0041 0015 0041 0015 0016 0015 0016 0015 0041 0015 0041 0015 0041 0015 06E9",,

"

How to obtain Global Cache Control Tower IR Codes:

Create an account and login to: 
https://irdb.globalcache.com/Home/Database

Enter the Brand Name of the device you would like to control. Then Select a Device Type, then Select a Model.

Now select the "Send Code Set" button next to the Device Model. Selecting "Select function" will only give you one code.

After receiving the email verify that you can see all IR Codes when scrolling to the bottom of the page. Gmail will clip the message and have a "Message clipped" not at the bottom of the page along with a View Entire Message button. Copy the entire message from the commas in the last IR Code to the beginning of the "function, code1, hexcode1, code2, hexcode2" header then paste into a new custom param value. Set the custom param key to the device name.

After saving Custom Params, Restart Node Server.

There may be multiple code sets that need to be downloaded or a single manufacture. Each Code set should be put into the Node Server Separately. This node serve is installed with the Onkyo Receiver Codes as an example
