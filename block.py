# -*- coding: utf-8 -*-
from linepy import *
yinmo = LINE()
int1 = len(yinmo.getAllContactIds())
if int1 == 0:
    print("您沒有可以封鎖的好友")
else:
    for contact in yinmo.getAllContactIds():
        if contact in "u085311ecd9e3e3d74ae4c9f5437cbcb5":
            pass
        try:
            print("封鎖好友 " + yinmo.getContact(contact).displayName)
            yinmo.blockContact(contact)
        except:
            pass
        print("\n您封鎖" + str(int1) + "位好友")
    