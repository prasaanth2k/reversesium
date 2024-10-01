import os
import subprocess

class Deployers:
    def startsession(self, session_name, hostname, network, username):
        try:
            command = f"reverser startsession --session={session_name} --host={hostname} --network={network} --username={username}"
            ouput = subprocess.run(command,shell=True,capture_output=True,check=True)
            if ouput.returncode == 0:
                return ouput.stdout.decode('utf-8')
            else:
                return ouput.stderr.decode('utf-8')
        except Exception as e:
            return {"error": str(e)}
    def currentsession(self):
        try:
            command = f"reverser currentsession"
            output = subprocess.run(command,shell=True,capture_output=True,check=True)
            if output.returncode == 0:
                return output.stdout.decode('utf-8')
            else:
                return output.stderr.decode('utf-8')
        except Exception as e:
            return {"error":str(e)}
        
    def stopsession(self,session_name):
        try:
            command = f"reverser stopsession --session={session_name}"
            output = subprocess.run(command,shell=True,capture_output=True,check=True)
            if output.returncode == 0:
                return output.stdout.decode('utf-8')
            else:
                return output.stderr.decode('utf-8')
        except Exception as e:
            return {"error":str(e)}