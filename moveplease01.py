#!/usr/bin/env python3

#
import shutil
import os

#changing script start directory
os.chdir('/home/student/mycode/')
#moving folder to new dir
shutil.move('raynor.obj', 'ceph_storage/')
#Promt user for new name for kerriagan.obj file
xname = input('What is the new name for kerrigan.obj? ')
# Renaming the kerrigan.obj file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

