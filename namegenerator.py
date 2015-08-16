from __future__ import absolute_import
import nameslist
from nameslist import maleNames, femaleNames, lastNames
import random


def generateName():
  lengthMale = len(maleNames) -1
  lengthFemale = len(femaleNames) -1
  lengthLast = len(lastNames) -1
  genderChoice = random.randint(0,1)
  if genderChoice == 0:
    firstNameRandom = maleNames[random.randint(0,lengthMale)]
    gender = "Male"
  else:
    firstNameRandom = femaleNames[random.randint(0,lengthFemale)]
    gender = "Female"
  lastNameRandom = lastNames[random.randint(0,lengthLast)]
  name = [firstNameRandom, lastNameRandom, gender]
  return name


def batchNames(numberOfNames):
  for x in range (0,numberOfNames):
    name = generateName()
    print name[0] + " " + name[1] + " is a " + name[2]

batchNames(5)
