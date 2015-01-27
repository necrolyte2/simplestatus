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

def main():
    from hosts import hostlist
    check_all(hostlist)

if __name__ == '__main__':
    main()
