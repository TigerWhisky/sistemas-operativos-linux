#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>
int main(void){int p[2]; const char*m="Mensagem enviada pelo processo pai"; if(pipe(p)<0){perror("pipe");return 1;} pid_t pid=fork(); if(pid<0){perror("fork");return 1;} if(pid==0){char b[256]; close(p[1]); ssize_t n=read(p[0],b,255); if(n<0){perror("read");return 1;} b[n]='\0'; printf("[child] %s\n",b); close(p[0]); return 0;} close(p[0]); if(write(p[1],m,strlen(m))<0){perror("write");return 1;} close(p[1]); waitpid(pid,NULL,0); return 0;}
