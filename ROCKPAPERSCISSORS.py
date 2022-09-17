#!/usr/bin/env python3
import random
def rpc(u_choice):
  p = random.randint(1,3)                   #random choice of computer
  if p == 1 :
    i='PAPER'
  elif p==2 :
    i = 'ROCK'
  else:
    i ='SCISSORS'
  k = u_choice.upper()
  print('COMPUTER CHOSE',i)
  cond(i,k)
def cond(i,k):
  u1 = 0
  u2 = 0
  if  i == k:                                    # conditional operators starting here
    print('Its a draw')
  elif i == 'PAPER':                             # computer generated paper here
    if k=='ROCK' :
      print('Paper destroyed your Rock!!')
      print('YOU LOST !!!')
      u2 += 1
    if k =='SCISSORS' :
      print('YOU WON !!')
      u1 += 1
  elif i =='ROCK':                                # computer generated rock here
    if k == 'PAPER':
       print('YOU WON !!')
       u1 += 1
    if k =='SCISSORS':
       print("YOU LOSE!!")
       u2 += 1
  elif i == 'SCISSORS':                            # computer generated scissors here
    if k =='ROCK':
        print('YOU WON ')
        u1 += 1
    elif k=='PAPER':
        print("YOU LOST !!")
        u2 += 1
  else :
       print('INVALID OPTION')
  print('COMPUTER:', u2, name, ':', u1)
#Main_program
print(' ....ROCK..PAPER..SCISSORS.... ')
ans = 'Y'
name = input('ENTER YOUR NAME: ')
while ans == 'Y':
  u_choice = input('YOUR CHOICE: ')
  rpc(u_choice)
  play = input('Want to play again (Y/N) ? ')
  ans = play.upper()
print('Game ended ')
