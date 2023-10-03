# DDOS-Scripts
Repo containing penetration testing DDOS scripts.

In implementing a DDOS script we need to send requests to a host on a specific port over and over again. This can be done with sockets. To speed the process up and make it more effective, we will use multi-threading as well.

We need the target’s IP address, the port we want to attack, and the fake IP address that we want to use. A fake IP - address doesn't necessarily make you anonymous.

A DDoS is never performed alone but with the help of botnets. In a botnet, one hacker infects many computers and servers of ordinary people, in order to use them as zombies. He uses them for a collective attack on a server. Instead of one DDOS script, he can now run thousands of them. Sooner or later the server will be overwhelmed with the amount of requests so that it is not even able to respond to an ordinary user. For smaller and weaker servers, sometimes one attacker is enough to get it down. However, usually, such an attack can be counteracted by blocking the IP addresses of the attackers.
### Clone the Repo
- To run, do:- E.g
```
python script.py
```
