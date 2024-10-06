import os
import subprocess
from monisys.Managers.Systeminfo import SystemInfo
from relib.core import CORE
from relib.strace import STRACE
from relib.brooker import BROOKER
# Core things functionality
core = CORE()
class Environment(STRACE,BROOKER):
    def __init__(self) -> None:
        super().__init__()
        self.docker_containers = SystemInfo("docker_containers")
    # It will build the container for will all the Environment purpose for all types of analysis
    # Binary analysis with secure environment
    def build(self,tag,path):
        try:
            core.exec(cmd=f"docker build -t {tag} {path}")
        except OSError as e:
            print(e)
    # It will start the session for binary analysis
    def start_session(self,sessionname,hostname,network,username):
        try:
            if network:
                dockercommand = [
                    "docker", "run", "-d", "--name", sessionname, "--hostname",hostname,
                    "reversesium:v1", "/bin/bash"
                ]
                result = subprocess.run(dockercommand, capture_output=True, text=True, check=True)
                userstate = core.adduser(sessionname=sessionname,username=username)
                if result.returncode == 0 and userstate == 0:
                    print('[*] New session started')
                else:
                    print('[*] Unable to start session')
            else:
                dockercommand = [
                    "docker", "run" , "-d" , "--name", sessionname, "--hostname",hostname,"--network","none",
                    "reversesium:v1", "/bin/bash"
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
    def spawn_shell(self,sessionname, username):
        try:
            # It will spawn the session which that what user is specifically 
            os.system(f"docker exec -it {sessionname} su - {username}")
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
            print("[*] Hold on while stoping sessions")
            result = subprocess.run(dockercommand,capture_output=True)
            stopresult = subprocess.run(dockercommandremove,capture_output=True)
            if result.returncode == 0 and stopresult.returncode == 0:
                print("[*] Session Stoped")
            else:
                print("[*] Unable to stop / No session are running")
        except subprocess.CalledProcessError as e:
            print(e)
    def current_sessions(self):
        dockerrunningcontainers = self.docker_containers.get_all_data()
        for containers in dockerrunningcontainers:
                print("---------------------------")
                print(f"[*] Session Name : {containers['name']}")
                print(f"[*] ID : {containers['id']}")
                print(f"[*] State : {containers['state']}")