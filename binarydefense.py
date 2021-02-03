1   #!/usr/bin/python3
  1 import requests
  2 import pyufw as ufw
  3 import ipaddress
  4 #https://github.com/5tingray/pyufw
  5 
  6 def cleanup_banlist( LIST ):
  7     cleaned = []
  8     for item in LIST:
  9         try:
 10             ipaddress.ip_address( item )
 11         except:
 12             pass
 13         else:
 14             cleaned.append(item)
 15     return cleaned
 16 
 17 def get_banlist( URL ):
 18     ban_text = requests.get( URL ).text
 19     ban_list = ban_text.splitlines()
 20     return ban_list
 21 
 22 #sudo ufw deny from {ip-address-here} to any
 23 def add_rule_to_firewall( IP ):
 24     ufw.add( "deny from {} to any" ).fromat( IP )
 25 
 26 def main():
 27     ban_list = get_banlist('https://www.binarydefense.com/banlist.txt')
 28     cleaned_list = cleanup_banlist( ban_list )
 29     for ip in cleaned_list:
 30         add_rule_to_firewall( ip )
 31     print("All items have been added")
 32     #print(ban_list)
 33 
 34 if __name__ == "__main__":
 35     main()
