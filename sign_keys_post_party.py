import subprocess
import sys

filename = sys.argv[1]
with open(filename) as f:
    for line in f:
        key = line[:len(line)-1]
        get_key = subprocess.run(['gpg', '--keyserver', 'pgp.mit.edu', '--recv-keys', key], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(get_key.stdout)
        sign_key = subprocess.run(['gpg', '--sign-key', key] , stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(sign_key.stdout)
        send_key = subprocess.run(['gpg', '--keyserver', 'pgp.mit.edu', '--send-keys', key] , stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(send_key.stdout)
