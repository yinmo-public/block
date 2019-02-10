# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE()
oepoll = OEPoll(yinmo)
int1 = len(yinmo.getAllContactIds())
if int1 == 0:
    print("您沒有可以封鎖的好友")
else:
    for contact in yinmo.getAllContactIds():
        print("封鎖好友 " + yinmo.getContact(contact).displayName)
        yinmo.blockContact(contact)
    print("\n您封鎖" + str(int1) + "位好友")
    