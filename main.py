import tls_client
TOKEN = "" #Put your token here
session = tls_client.Session(
                    client_identifier="okhttp4_android_9",
                    random_tls_extension_order=True
                )

headers = {
    'accept': '*/*',
    'accept-language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': TOKEN,
    'priority': 'u=1, i',
    'referer': 'https://discord.com/channels/@me',
    'sec-ch-ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'Europe/Madrid',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjQuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjQuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vd3d3LmJpbmcuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuYmluZy5jb20iLCJzZWFyY2hfZW5naW5lIjoiYmluZyIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTA0MTEsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0=',
}

response = session.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
with open("friends.txt", "a+") as file:
    for account in response.json():
        file.write(f"Username: {account['user']['username']} | Id: {account['id']}\n")
        print(f"Username: {account['user']['username']} | Id: {account['id']}")
