import urequests as requests
import wifi_connect
import uConfig

config = uConfig.Config("config.ini")
TOKEN = config['Discord']['token']
SERVER = config['Discord']['server']
CHANNEL = config['Discord']['channel']

SERVER = int(SERVER)
CHANNEL = int(CHANNEL)

wifi_connect.connect()


class DiscordAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://discord.com/api"
        self.headers = {"Authorization": f"Bot {token}"}

    def get_user(self, user_id):
        url = f"{self.base_url}/users/{user_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def send_message(self, channel_id, message):
        url = f"{self.base_url}/channels/{channel_id}/messages"
        data = {"content": message}
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()
    def get_server_members(self, server_id):
        url = f"{self.base_url}/guilds/{server_id}/members"
        response = requests.get(url, headers=self.headers)
        return response.json()
    def get_server(self, server_id):
        url = f"{self.base_url}/guilds/{server_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    def get_server_keys(self, server_id):
        url = f"{self.base_url}/guilds/{server_id}"
        response = requests.get(url, headers=self.headers)
        ans = response.json()
        ans = ans.keys()
        return ans
        
def base():
    disc =DiscordAPI(TOKEN)
    #serv = disc.get_server(SERVER)[name]
    #print(serv)
    
    #print(disc.get_server(SERVER))
    return disc
        
