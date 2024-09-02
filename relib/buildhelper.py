import os
import subprocess


class Environment:
    # It will build the container for will all the Environment purpose for all types of analysis
    # Binary analysis with secure environment
    def build(self):
        try:
            dockercommand = ["docker", "build", "-t", "reversesium:v1", "."]
            process = subprocess.Popen(dockercommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Stream output live
            for line in process.stdout:
                print(line, end='')

            # Wait for the process to complete
            process.wait()

            if process.returncode == 0:
                print("[*] Build completed successfully")
            else:
                print("[!] Build failed")
                for line in process.stderr:
                    print(line, end='')

        except Exception as e:
            print(f"[!] An unexpected error occurred: {e}")
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