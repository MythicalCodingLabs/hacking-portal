import time,socket,pythonping
 

def portal():  
  print(">", end='')
  func = input();
  if func == "!help":
    time.sleep(0.5)
    print("--Commands--")
    time.sleep(0.5)
    print("!getip - gets ip from URL");
    portal();
  elif func == "!ping":
    print("Insert site IP:")
    print(">", end='')
    func = input();
    pythonping.ping(func, verbose=True)
  elif func == "!getip":
    print("Input website:");
    func = input();
    print("Grabbing ip from", func);
    print("Complete")
    print("IP:", socket.gethostbyname(func))
    portal();

print("--Hacking Portal V1.1.0--");
print("");
print("Welcome Hacker");
print("Type !help for list of commands");
portal();

    