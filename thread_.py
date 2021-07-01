from time import sleep
from threading import Thread
import sys
from termcolor import colored,cprint
from concurrent.futures import ThreadPoolExecutor


# def thread_fun(name):
#     cprint(f"[+] Thread {name} started !",'green',attrs=['bold'])
#     print("\t [*] Welcome to {0} thread !".format(name))
#     print("\t [*] We are happy to serve you !")
#     sleep(1)
#     cprint("\t [*] Thank You for Waiting !",'yellow',attrs=['bold'])
#     cprint(f"[-] Thread {name} ended !",'red',attrs=['bold'])
    

# cprint("[+] Main Thread started !",'green')
# t = Thread(target=thread_fun, args=("private",))
# t.start()
# cprint("[*] Waiting for Main Thread end !",'yellow')
# t.join()
# cprint("[-] Main Thread ended !",'red')

var = 0
cprint("[*] Calculating var........",'magenta',attrs=['bold'])
def thread_fun2(name):
    global var
    cprint(f"[+] Thread {name} started !",'green',attrs=['bold'])
    var += 1
    sleep(0.5)
    cprint(f"[-] Thread {name} ended !",'red',attrs=['bold'])


# thread pool executor example      
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_fun2, range(10))
    
    
# with ThreadPoolExecutor(max_workers=3) as executor:
#     executor.submit(thread_fun, 0)
#     executor.submit(thread_fun, 1)
#     executor.submit(thread_fun, 2)
#     executor.submit(thread_fun, 3)
#     executor.submit(thread_fun, 4)
    
    
cprint("Done",'blue','on_white',attrs=['bold'])
cprint(f"[*]  var = {var}",'magenta',attrs=['bold'])
