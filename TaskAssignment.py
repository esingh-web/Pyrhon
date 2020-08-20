import os
import pyttsx3


print("*************************************************************************************************************************************************************************")
print()
print("Hello !!!")
print("Welcome to our service !!!")
print("How may we help you !!!")
print()

while True:
	print("*************************************************************************************************************************************************************************")
	print("Please enter your task, which you want us to perform for you : ", end = "")

	p=input().lower()
	
	if ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("notepad++" in p)):
			print("Starting notepad++....")
			os.startfile("notepad++")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("notepad" in p)):
			print("Starting notepad....")
			os.system("notepad")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("outlook" in p)):
			print("Starting outlook....")
			os.startfile("outlook")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and (("lync" in p) or ("skype" in p))):
			print("Starting skype/Lync application....")
			os.startfile("LYNC")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("excel" in p)):
			print("Starting excel....")
			os.startfile("EXCEL")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("msaccess" in p)):
			print("Starting MSACCESS....")
			os.startfile("MSACCESS")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and (("power point" in p) or ("powerpoint" in p) or ("ppt" in p))):
			print("Starting POWERPNT....")
			os.startfile("POWERPNT")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("cls" in p)):
			print("Starting eclipse....")
			os.system("eclipse")	
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("pycharm" in p)):
			print("Starting pycharm....")
			os.system("pycharm64")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("internet explorer" in p or "internetexplorer" in p)):
			print("Starting internet explorer....")
			os.system("iexplore")	
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("adobereader" in p or "adobe reader" in p)):
			print("Starting adobe reader....")
			os.startfile("AcroRd32")	
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("remote desktop connection" in p or "remote desktop connection" in p )):
			print("Starting remote desktop connection....")
			os.startfile("mstsc")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("controlpanel" in p or "control panel" in p)):
			print("Starting control panel....")
			os.system("Control Panel")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("camera" in p)):
			print("Starting camera....")
			os.startfile('microsoft.windows.camera:')
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("fileexplorer" in p or "file explorer" in p)):
			print("Starting file explorer....")
			os.system("explorer")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("wordpad" in p or "word pad" in p)):
			print("Starting word pad....")
			os.startfile("wordpad")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("word" in p)):
			print("Starting microsoft word....")
			os.startfile("WINWORD")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("paint" in p)):
			print("Starting paint....")
			os.startfile("mspaint")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("quick assistance" in p or "quickassistance" in p)):
			print("Starting quickassist....")
			os.startfile("quickassist")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("math input panel" in p or "mathinputpanel" in p)):
			print("Starting math input panel....")
			os.startfile("mip")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("snipping tool" in p or "snippingtool" in p)):
			print("Starting snipping tool....")
			os.system("snippingtool")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("teamviewer" in p or "team viewer" in p)):
			print("Starting team viewer...")
			os.system("TeamViewer")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("xphone" in p or "x phone" in p)):
			print("Starting xphone...")
			os.system("C4B.XPhone.Commander")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("xpsviewer" in p or "xps viewer" in p)):
			print("Starting XPS Viewer...")
			os.system("xpsrchvw")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("windows fax & scan" in p or "windowsfax&scan" in p or "windows fax and scan" in p or "windowsfaxandscan" in p or "windows fax" in p or "windows scan" in p)):
			print("Starting windows fax & scan...")
			os.startfile("WFS")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("window media player" in p or "windowmediaplayer" in p)):
			print("Starting window media player...")
			os.system("wmplayer")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("agentransack" in p or "agent ransack" in p)):
			print("Starting agent ransack...")
			os.system("AgentRansack")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("calculator" in p)):
			print("Starting calculator...")
			os.system("calc")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("bluetooth" in p)):
			print("Starting bluetooth...")
			os.startfile("fsquirt")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("systempropertiesadvanced" in p  in p or "system properties advanced" in p or "system properties" in p)):
			print("Starting System properties advance...")		
			os.system("SystemPropertiesAdvanced")
	elif ((("execute" in p) or ("launch" in p) or ("run" in p) or ("open" in p) or ("start" in p)) and ("notebook" or "jupyter notebook" in p or "jupyternotebook" in p)):
			print("Starting jupyter notebook...")
			os.system("jupyter notebook")
	elif (("close" in p) or ("quit" in p) or ("exit" in p) or ("terminate" in p)):
			print("*************************************************************************************************************************************************************************")
			print("Service has been closed...")
			break;
	else:
			print("*************************************************************************************************************************************************************************")
			print("Entered input is not supported..")
			print("Please check your input once again..")
			


 