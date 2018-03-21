#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main( void )
{
  int   sckt;
  struct sockaddr_in  sckt_addr;
  char  buf[256];
  
  sckt = socket(AF_INET, SOCK_DGRAM,0);
  sckt_addr.sin_family = AF_INET;
  sckt_addr.sin_port = htons(20001);
  sckt_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
  
  while(1){
    fgets(buf, 256, stdin);
    sendto(sckt, buf, strlen(buf), 0, (struct sockaddr *)&sckt_addr, sizeof(sckt_addr));
  }
  close(sckt);
  
  return 0;
}
