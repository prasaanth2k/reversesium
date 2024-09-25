import subprocess

class SessionController:
    def start_session_with_network(self, sessionname, hostname, username, network):
        session_start_command_with_network = [
            "reverser",
            "startsession",
            f"--session={sessionname}",
            f"--host={hostname}",
            "--network=true",
            f"--username={username}",
        ]
        session_start_command_without_network = [
            "reverser",
            "startsession",
            f"--session={sessionname}",
            f"--host={hostname}",
            "--network=false",
            f"--username={username}",
        ]
        if network:
            output = subprocess.run(
                session_start_command_with_network,
                capture_output=True,
                text=True,
                check=True,
            )
            return output.stdout
        else:
            output = subprocess.run(
                session_start_command_without_network,
                capture_output=True,
                text=True,
                check=True,
            )
            return output.stdout
    
    def get_current_running_session(self):
        get_running_session = ['reverser','currentsession']

        try:
            output = subprocess.run(get_running_session,capture_output=True,text=True,check=True)
            return output.stdout
        except subprocess.CalledProcessError as e:
            print(e)