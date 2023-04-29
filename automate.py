import paramiko
import time
import pprint

class Automate_networkCommands:
    """
    Automate Network Commands

    This class is designed to automate the execution of network commands on remote servers using the Paramiko library.
    It defines methods to create an SSH client, execute commands, and execute commands on remote servers.
    """

    def __init__(self, ip, login_username, login_password):
        """
        Initialize the Automate_networkCommands class with the IP address, username, and password for the remote server.
        """
        self.ip = ip
        self.login_username = login_username
        self.login_password = login_password

    def create_ssh_client(self):
        """
        Create an SSH client using Paramiko and connect to the remote server with the provided credentials.
        
        Returns:
            ssh_client (paramiko.SSHClient): An instance of the SSH client connected to the remote server.
        """
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.RejectPolicy())
        ssh_client.connect(self.ip, username=self.login_username, password=self.login_password)
        return ssh_client
    
    def execute_commands(self, ssh_client, list_of_commands):
        """
        Execute a list of commands on the remote server using the provided SSH client.

        Args:
            ssh_client (paramiko.SSHClient): An instance of the SSH client connected to the remote server.
            list_of_commands (list): A list of commands to execute on the remote server.
        """
        for command in list_of_commands:
            print(f"Executing the command----->{command}")
            standard_out = ssh_client.exec_command(command)
            standard_error = ssh_client.exec_command(command)
            command_output = standard_out.read().decode()
            command_error = standard_error.read().decode()

            if command_output:
                pprint.pprint(command_output)
            if command_error:
                pprint.pprint(command_error)

            time.sleep(2)

    def execute_commands_on_remoteServer(self, commands):
        """
        Execute a list of commands on the remote server by creating an SSH client and using the execute_commands method.

        Args:
            commands (list): A list of commands to execute on the remote server.
        """
        with self.create_ssh_client() as ssh_client:
            self.execute_commands(ssh_client, commands)




commands = [
    "ls",
    "uname -a",
    "df -h",
]
commands1 = [
    "ls",
    "uname -a",
    "df -h",
]

security= Automate_networkCommands(ip_address,username, password)
security.execute_commands_on_remoteServer(commands)
    

database= Automate_networkCommands()
database.execute_commands_on_remoteServer(commands1)
