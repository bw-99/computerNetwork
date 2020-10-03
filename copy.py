import threading
import time
import sys
class copy_machine:

    def __init__(self,infile,outfile):
        self._infile=infile
        self._outfile=outfile
    
    def make_thread(self):
        setattr(mod,self._infile,threading.Thread(target=self.copy))
        getattr(mod,self._infile).start()

    def copy(self):
        f=open(self._infile,'rb')
        self.write_ilog()
        p=open(self._outfile,'wb')
        data=f.read(100)
        while(data):
            p.write(data)
            data=f.read(100)
        self.write_olog()
        f.close()
        p.close()

    def write_ilog(self):
        p=open('log.txt','a')
        text=str(time.time()-start)+'\t\tStart copying '+self._infile+' to '+self._outfile+'\n'
        p.write(text)
        p.close()

    def write_olog(self):
        p=open('log.txt','a')
        text=str(time.time()-start)+'\t\t'+self._infile+' is copyied completely\n'
        p.write(text)
        p.close()

start=time.time()
mod=sys.modules[__name__]

i=1
if __name__ == "__main__":
    while(True):
        input_file=input("Input the file name : ")
        if(input_file=='exit'):
            break
        output_file=input("Input the new name : ")
        
        setattr(mod,'thread_{}'.format(i),copy_machine(input_file,output_file))
        getattr(mod,'thread_{}'.format(i)).make_thread()
        i+=1