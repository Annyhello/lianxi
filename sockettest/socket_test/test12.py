from socket import *
s=socket(AF_INET,SOCK_STREAM)
print getprotobyname('tcp')