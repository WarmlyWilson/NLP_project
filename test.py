#!/usr/bin/env python
# -*- coding: utf-8 -*-



file1 = 'file2.txt'
f1 = open(file1, 'rb')
#lines = f1.readlines()
txt=f1.read().decode("utf-8")
print (txt)