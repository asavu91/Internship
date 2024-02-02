import paramiko
import socket

def get_local_ip():
    return socket.gethostbyname(socket.gethostname())

def get_remote_ip(remote_host, remote_user, remote_password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(remote_host, username=remote_user, password=remote_password)
        transport = client.get_transport()
        remote_ip = transport.getpeername()[0]
        return remote_ip
    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {str(e)}")
    finally:
        client.close()

remote_host = "localhost"
remote_user = "adi"
remote_password = ""

local_ip = get_local_ip()
remote_ip = get_remote_ip(remote_host, remote_user, remote_password)

if remote_ip:
    print(f"Local IP: {local_ip}")
    print(f"Remote IP: {remote_ip}")

    if local_ip == remote_ip:
        print("The IP addresses match.")
    else:
        print("The IP addresses do not match.")
else:
    print("Unable to retrieve remote IP address.")
