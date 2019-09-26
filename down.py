import wget
import sys

print('Beginning file download with wget module')

if(len(sys.argv)==4):
    print('three arguments, the first will be treated as the first ID to start downloading')
    print('the 3d is the number of files to download')
    prefix=sys.argv[1]
    paperidstart=int(sys.argv[2])
    nOfFiles=int(sys.argv[3])
else:
    print('no arguments, downloading default values')
    prefix='CFI0709869'
    paperidstart=287886
    nOfFiles = 2

for i in range(0,nOfFiles):
    url = 'http://www.internetculturale.it/jmms/objdownload?id=oai%3Awww.internetculturale.sbn.it%2FTeca%3A20%3ANT0000%3A'+str(prefix)+'_'+str(paperidstart+i)+'&teca=MagTeca%20-%20ICCU&resource=img&mode=all'
    print('downloading: '+str(paperidstart+i)+' pdf')
    wget.download(url, str(paperidstart+i)+'.pdf')
    print('----------------------------------------')
