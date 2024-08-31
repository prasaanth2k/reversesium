import os

class Environment:
    def build(self):
        try:
            dockercommand = f"docker build -t reversesium:v1 ."
            result = os.system(dockercommand)
            if result != 0:
                print(result)
        except OSError as e:
            print(e)
    
    def get_shell(self,hostname):
        try:
            dockerruncommand = f"docker run -it --hostname {hostname} reversesium:v1 bash"
            os.system(dockerruncommand)
        except OSError as e:
            print(e)