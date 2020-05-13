Configuration for running keepalived on Hetzner Cloud with Floading IP on two Servers with heartbeat failover. 

# HowTo Use it 

- Clone this repo to /etc/keepalived (on both systems): `git clone https://github.com/chris2k20/keepalived-hcloud/ /etc/keepalived/`
- Install keepalived (on both systems) `sudo apt install keepalived`
- Install python3 (on both systems) `sudo apt install python3`
- Create API Token and Failover IP @hcloud -> https://console.hetzner.cloud/
- Configure IP Addresses (ips array), Hetzner API Token (api-token) and server-id (on both systems differnt values) in`vim hcloud-failover/config.json`
- Configure IP Addresses on master `vim keepalived.conf` and on backup-node `vim keepalived-backup.conf` 
- Save the keepalived-backup.conf (on backup node) to `/etc/keepalived/keepalived.conf`
- start/enable keepalived (on both systems) `sudo systemctl enable keepalived ; sudo systemctl start keepalived` 
