# Tetanus

Helper script for mangling CS payloads to create a macro.


## Disclaimer

*This is not my own research and it is merely the weaponization of various techniques i have found online.I assume no responsibility for any misuse of this script* 

## Credits

Full credit goes to [Carlos Perez](https://twitter.com/Carlos_Perez) for his [ASR Rules](https://gist.github.com/infosecn1nja/24a733c5b3f0e5a8b6f0ca2cf75967e3) and the [Walmart Labs team](https://twitter.com/OrOneEqualsOne) for the [techniques](https://medium.com/walmartlabs/evasive-vba-advanced-maldoc-techniques-1365e9373f80) used in the tool.

## Background stuff

The Macro is executed via WMI is order to bypass the AMSI scan engine. In addition the script runs the payload.ps1 file through Invoke-Obfuscation to add another level of confusion either to AV vendor or analysts. The default commands used in Invoke-Obfuscation are TOKEN\ALL\1,COMPRESS\1 which is hardcoded in the script. The resulting code is then Base64 encoded and the strings are reversed. Finally all variables in the script are randomly generated every time the script is executed to avoid at least static signatures.


## Usage:

Extract a .ps1 payload from Cobalt Strike and save it in the tetanus directory. Run the script with:

`python tetanus.py -f <payload>.ps1`

Copy the output macro to a Microsoft Word/Excel document and save it. I have also succesfuly imported the macro in a PowerPoint (pptm) file by adding a [Custom UI](http://openxmldeveloper.org/blog/b/openxmldeveloper/archive/2006/05/26/customuieditor.aspx) to load the script on file open. 

## Requirements

You will need to have both [PowerShell/pwsh](https://github.com/PowerShell/PowerShell) and [Invoke-Obfuscation](https://github.com/danielbohannon/Invoke-Obfuscation)
for the script to work.