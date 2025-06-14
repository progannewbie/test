import socket

HOST = '192.168.1.10'  # IP address of the Kawasaki controller
PORT = 10000           # Port used by the Kawasaki controller

# Joint target angles in degrees
JOINT_ANGLES = [0, 0, 90, 0, -90, 0]


def move_robot(host=HOST, port=PORT, angles=JOINT_ANGLES):
    """Send joint angles to the Kawasaki robot via a TCP connection."""
    command = 'JMOVE ' + ','.join(str(a) for a in angles) + '\n'
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(command.encode('utf-8'))
        response = s.recv(1024)
        print('Controller response:', response.decode('utf-8', errors='ignore'))


if __name__ == '__main__':
    move_robot()
