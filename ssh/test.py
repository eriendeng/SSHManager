
import paramiko


if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="123.207.93.89", port=22, username="ubuntu", password="Change19980101")
    stdin, stdout, stderr = ssh.exec_command("ifconfig")
    result = stdout.read()
    if not result:
        result = stderr.read()
    ssh.close()

    print(result.decode())