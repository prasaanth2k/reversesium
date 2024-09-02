import os
import subprocess


class Environment:
    # It will build the container for will all the Environment purpose for all types of analysis
    # Binary analysis with secure environment
    def build(self):
        try:
            dockercommand = f"docker build -t reversesium:v1 ."
            result = os.system(dockercommand)
            if result != 0:
                print(result)
            print("[*] Build completed")
        except OSError as e:
            print(e)
    # It will start the session for binary analysis
    def start_session(self,sessionname,hostname):
        try:
            dockercommand = [
                "docker", "run", "-d", "--name", sessionname, "--hostname",hostname,
                "reversesium:v1", "/bin/bash", "-c", "tail -f /dev/null"
            ]
            result = subprocess.run(dockercommand, capture_output=True, text=True, check=True)
            if result.returncode == 0:
                print('[*] New session started')
            else:
                print('[*] Unable to start session')
        except subprocess.CalledProcessError as e:
            print(f'Error: {e.stderr}')
        except FileNotFoundError:
            print("Error: Docker command not found. Ensure Docker is installed and in your PATH.")
    # With this command you can able to stop the session after the tasks completed
    def spawn_shell(self,sessionname):
        try:
            dockercommand = [
                "docker","exec","-it",sessionname,"bash"
            ]
            subprocess.run(dockercommand)
        except subprocess.CalledProcessError as e:
            print(e)

    
    def stop_session(self,sessionname):
        try:
            dockercommand = [
                "docker","container","stop",sessionname
            ]
            dockercommandremove = [
                "docker","container","rm",sessionname
            ]
            result = subprocess.run(dockercommand,capture_output=True)
            stopresult = subprocess.run(dockercommandremove,capture_output=True)
            if result.returncode == 0 and stopresult.returncode == 0:
                print("[*] Session Stoped")
            else:
                print("[*] Unable to stop")
        except subprocess.CalledProcessError as e:
            print(e)