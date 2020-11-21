# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import re


class ProgressBar(object):
    DEFAULT = 'Progress: %(bar)s %(percent)3d%%'
    FULL = '%(bar)s %(current)d/%(total)d (%(percent)3d%%) %(remaining)d to go'

    def __init__(self, total, width=40, fmt=DEFAULT, symbol='=',
                 output=sys.stderr):
        assert len(symbol) == 1

        self.total = total
        self.width = width
        self.symbol = symbol
        self.output = output
        self.fmt = re.sub(r'(?P<name>%\(.+?\))d',
            r'\g<name>%dd' % len(str(total)), fmt)

        self.current = 0

    def __call__(self):
        percent = self.current / float(self.total)
        size = int(self.width * percent)
        remaining = self.total - self.current
        bar = '[' + self.symbol * size + ' ' * (self.width - size) + ']'

        args = {
            'total': self.total,
            'bar': bar,
            'current': self.current,
            'percent': percent * 100,
            'remaining': remaining
        }
        print('\r' + self.fmt % args, file=self.output, end='')

    def done(self):
        self.current = self.total
        self()
        print('', file=self.output)

from time import sleep

progress = ProgressBar(60, fmt=ProgressBar.FULL)

#for x in xrange(progress.total):
progress.current += 10
progress()
import urllib
from json import load
from urllib2 import urlopen
from termcolor import colored, cprint

#Váriaveis
ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
progress.current += 10
progress()
tor = urllib.urlopen('https://check.torproject.org/exit-addresses')
progress.current += 10
progress()
NOT = str(colored("NOT", 'red', attrs=['underline','bold','blink']))
progress.current += 10
progress()
textsucess = colored("\n[+] Your public Ip: " + ip + "  ==> It's a TOR exit node", 'green', attrs=['bold','blink'])
progress.current += 10
progress()
textfail = colored("\n[+] Your public Ip:'"+ip+"'==> It's "+NOT+colored(" a TOR exit node", 'red', attrs=['bold', 'blink']), 'red', attrs=['bold','blink'])
progress.current += 10
progress()
for ip_tor in tor.readlines():
       ip_tor = ip_tor.replace("\n","")
       if "ExitAddress" in ip_tor:
           ip_tor = ip_tor.split(" ")[1]
           if ip == ip_tor:
               success = 1
               break
           else:
               success = 0
progress =+ 30 + 40

if success == 0:
    print(textfail)
else:
    print(textsucess)
#progress()
#progress.done()
