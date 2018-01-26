#!/usr/bin/env python
# -*- coding: utf-8 

def write_data(DIR,data):
    fo = open(DIR, "w")
    fo.write(data)
    fo.close()

def read_data(DIR):
    fo = open(DIR, "r")
    data = fo.read()
    fo.close()
    return data
