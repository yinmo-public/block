# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE ()
oepoll = OEPoll(yinmo)
for contact in yinmo.getAllContactIds():
    yinmo.blockContact(contact)
    print("已封鎖1位好友")