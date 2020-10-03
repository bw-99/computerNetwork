import threading
import time

class copy_machine:

    def __init__(self,infile,outfile):
        self._infile=infile
        self._outfile=outfile
    
    def make_thread(self):
        thread=threading.Thread(target=self.copy)
        thread.start()

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

if __name__ == "__main__":
    p=open('log.txt','w')
    p.close()
    while(True):
        input_file=input("Input the file name : ")
        if(input_file=='exit'):
            break
        output_file=input("Input the new name : ")
        
        copy=copy_machine(input_file,output_file)
        copy.make_thread()