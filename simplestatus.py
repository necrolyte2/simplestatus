import socket
import sys

def check_host(host, port):
    '''
    Checks a given host by simply connecting to a TCP port

    :param str host: IP addr or hostname of host to connect to
    :param int port: TCP port to connect to
    :return: Tuple of (True|False, error message|'')
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        return (True,'')
    except Exception as e:
        return (False, str(e))
    finally:
        s.close()

def check_all(hostsports):
    '''
    Iterate through host list and check them with simple connect test

    :param list hostsports: List of (hostaddr, port, description)
    '''
    for host, port, desc in hostsports:
        up, msg = check_host(host, port)
        sys.stdout.write(u'{0}'.format(desc))
        if up:
            sys.stdout.write(u' - UP\n')
        else:
            sys.stdout.write(u" - DOWN\n\t{0} on port {1} seems down: {2}\n".format(host,port,msg))

class MissingHostsError(Exception): pass

def load_hosts(hostfile):
    '''
    Just load the python hosts file
    Must contain a variable called hosts which points to a list
    of tuples of 3 elements each

    hosts = [
        ('www.example.com', 80, 'Web check for www.example.com'),
    ]

    :param file hostfile: opened hosts.py file
    '''
    contents = hostfile.read()
    exec(contents)
    try:
        return hosts
    except NameError:
        raise MissingHostsError('hostfile is missing host variable')

def main():
    from hosts import hosts
    check_all(hosts)

if __name__ == '__main__':
    main()
