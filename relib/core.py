import subprocess
import sys


class CORE:
    def exec(self, cmd):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        while True:
            output = process.stdout.readline()
            if output == b"" and process.poll() is not None:
                break
            if output:
                sys.stdout.write(output.decode())

        return process.poll()
    def straceexec(self, cmd):
        process = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
        output_lines = []
        
        while True:
            output = process.stderr.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                sys.stdout.write(output)
                output_lines.append(output.strip())

        return output_lines
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