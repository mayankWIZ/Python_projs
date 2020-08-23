from pyngrok import ngrok
import os
host=None
try:
    #print('Tunnels: '+str(len(ngrok.get_tunnels())))
    ngrok.connect(5000)
    host=ngrok.get_tunnels()
    print('host:\t'+host[0].public_url)
except Exception as e:
    print('Error in connection to ngrok')
    print(e)
os.system('start cmd /D /C "python main.py {0}"'.format(host[0].public_url))
input('Enter Anything to terminate:\n>\t')
ngrok.kill()
