import subprocess
import sys


class CORE:
    def exec(self, cmd):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            output = process.stdout.readline()
            # Break the loop if no more output
            if output == b"" and process.poll() is not None:
                break
            if output:
                sys.stdout.write(output.decode())

        return process.poll()
    def adduser(self,sessionname, username):
        try:
            dockercommand = [
                "docker", "exec", "-it", sessionname, "/usr/local/bin/usermanagement.sh", username
            ]
            subprocess.run(dockercommand, check=True)
            return 0
        except subprocess.CalledProcessError as e:
            print(e)
            return 1