# Automate-Network-Commands

## This Python program is designed to automate the execution of network commands on remote servers

using the Paramiko library. It defines a class named Automate_networkCommands with methods to
create an SSH client, execute commands, and execute commands on remote servers.

### Dependencies
### paramiko
### time
### pprint
To install the required dependencies, use the following command:

## Class:
Automate_networkCommands

## Methods
__init__(self, ip, login_username, login_password)
Initialize the Automate_networkCommands class with the IP address, username, and password for the
remote server.

## create_ssh_client(self)
Create an SSH client using Paramiko and connect to the remote server with the provided credentials.

## Returns:

ssh_client (paramiko.SSHClient): An instance of the SSH client connected to the remote server.
execute_commands(self, ssh_client, list_of_commands)
Execute a list of commands on the remote server using the provided SSH client.

## Args:

ssh_client (paramiko.SSHClient): An instance of the SSH client connected to the remote server.
list_of_commands (list): A list of commands to execute on the remote server.
execute_commands_on_remoteServer(self, commands)
Execute a list of commands on the remote server by creating an SSH client and using the
execute_commands method.

## Args:

commands (list): A list of commands to execute on the remote server.