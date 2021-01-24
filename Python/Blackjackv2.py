from tkinter import *
from tkinter import messagebox
import random
'''
- Fix aces
- Fix split action
- Dealer check for 21 on face ace
- Window fix
'''
def win():
  global money
  global bet
  global money_display
  global bet_display
  global player_value
  global dealer_value
  global side_board
  global root
  Button(side_board, text="Double Down", command=double_down, state=DISABLED).grid(row=4, column=3)
  Button(side_board, text="Stand", command=stand, state=DISABLED).grid(row=4, column=0)
  # Win Conditions
  if player_value == 21:
    money += (bet*2.5)
    money_display.destroy()
    bet_display.destroy()
    money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
    money_display.grid(row=0, column=0, columnspan=4, sticky=E)
    bet_display = Label(side_board, text="+"+str(bet*1.5), font=("Roboto", 15), bg="dark green", fg="green")
    bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
    response = messagebox.askyesno("21", "You won! Next hand?")
  elif dealer_value > 21:
    money += (bet*2)
    money_display.destroy()
    bet_display.destroy()
    money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
    money_display.grid(row=0, column=0, columnspan=4, sticky=E)
    bet_display = Label(side_board, text="+"+str(bet), font=("Roboto", 15), bg="dark green", fg="green")
    bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
    response = messagebox.askyesno("DEALER BUST", "You won! Next hand?")
  elif player_value > dealer_value:
    money += (bet*2)
    money_display.destroy()
    bet_display.destroy()
    money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
    money_display.grid(row=0, column=0, columnspan=4, sticky=E)
    bet_display = Label(side_board, text="+"+str(bet), font=("Roboto", 15), bg="dark green", fg="green")
    bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
    response = messagebox.askyesno("HAND WON", "You won! Next hand?")
  elif dealer_value > player_value:
    response = messagebox.askyesno("HAND LOSE", "Dealer won! Next hand?")
  else:
    money += bet
    money_display.destroy()
    bet_display.destroy()
    money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
    money_display.grid(row=0, column=0, columnspan=4, sticky=E)
    bet_display = Label(side_board, text="+0", font=("Roboto", 15), bg="dark green", fg="green")
    bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
    response = messagebox.askyesno("DRAW", "Draw! Next hand?")
  
  # Reset
  if response == 1:
    root.destroy()
    board_setup()
    
def new_stand():
  global split_yeah
  global dealer_value
  global dealer_card
  global player_value
  global money
  global bet
  global money_display
  global root
  global bet_display
  global split_value
  global new_bet
  global side_board
  split_yeah = False
  Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
  card_back.destroy()
  
  while dealer_value < 18:
    if dealer_value > split_value:
      break
    else:
      type_ = random.randint(0, 12)
      num = random.randint(0, 3)

      if type_ >=9:
        dealer_value += 10
      else:  
        dealer_value += (type_ + 1)
      dealer_card += deck[type_][num]

      dl_card = Label(dealer_side, text=dealer_card, font=("Courier", 100))
      dl_card.grid(row=0, column=1)
      Label(dealer_side, text=dealer_value).grid(row=1, column=0, columnspan=100)
  # Win Conditions
  if split_value == 21:
    money += (new_bet*2.5)
    res = ' +'+str(new_bet*1.5)
  elif dealer_value > 21:
    money += (new_bet*2)
    res = ' +'+str(new_bet)
  elif split_value > dealer_value:
    money += (new_bet*2)
    res = ' +'+str(new_bet)
  elif dealer_value > split_value:
    res = ' -'+str(new_bet)
  else:
    money += new_bet
    res = ' +0'

  if player_value == 21:
    money += (bet*2.5)
    money_display.destroy()
    bet_display.destroy()
    money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
    money_display.grid(row=0, column=0, columnspan=4, sticky=E)
    bet_display = Label(side_board, text="+"+str(bet*1.5)+res, font=("Roboto", 15), bg="dark green", fg="green")
    bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
    response = messagebox.askyesno("21", "You won! Next hand?")
  elif dealer_value > 21:
    money += (bet*2)
    money_display.destroy()
    bet_display.destroy()
    money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
    money_display.grid(row=0, column=0, columnspan=4, sticky=E)
    bet_display = Label(side_board, text="+"+str(bet)+res, font=("Roboto", 15), bg="dark green", fg="green")
    bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
    response = messagebox.askyesno("DEALER BUST", "You won! Next hand?")
  elif player_value > dealer_value:
    money += (bet*2)
    money_display.destroy()
    bet_display.destroy()
    money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
    money_display.grid(row=0, column=0, columnspan=4, sticky=E)
    bet_display = Label(side_board, text="+"+str(bet)+res, font=("Roboto", 15), bg="dark green", fg="green")
    bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
    response = messagebox.askyesno("HAND WON", "You won! Next hand?")
  elif dealer_value > player_value:
    response = messagebox.askyesno("HAND LOSE", "Dealer won! Next hand?")
  else:
    money += bet
    money_display.destroy()
    bet_display.destroy()
    money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
    money_display.grid(row=0, column=0, columnspan=4, sticky=E)
    bet_display = Label(side_board, text="+0"+' +'+str(new_bet), font=("Roboto", 15), bg="dark green", fg="green")
    bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
    response = messagebox.askyesno("DRAW", "Draw! Next hand?")

  # Reset
  if response == 1:
    root.destroy()
    board_setup() 
   
def new_hit():
  global card_back
  global player_value
  global player_card
  global dealer_value
  global dealer_card
  global money
  global bet
  global money_display
  global bet_display
  global split_card
  global two_card
  global split_board
  global split_value
  Button(side_board, text="Stand", command=new_stand).grid(row=4, column=0)
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)
  
  if type_ >=9:
    split_value += 10
  else:  
    split_value += type_ + 1
  two_card += deck[type_][num]
  
  split_card = Label(split_board, text=two_card, font=("Courier", 100))
  split_card.grid(row=0, column=0)
  Label(split_board, text=split_value).grid(row=1, column=0, columnspan=3)

  if split_value > 21:
    Button(side_board, text="Double Down", command=double_down, state=DISABLED).grid(row=4, column=3)
    Button(side_board, text="Stand", command=stand, state=DISABLED).grid(row=4, column=0)
    Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
    card_back.destroy()
    while dealer_value < player_value:
      type_ = random.randint(0, 12)
      num = random.randint(0, 3)

      if type_ >=9:
        dealer_value += 10
      else:  
        dealer_value += (type_ + 1)
      dealer_card += deck[type_][num]

      dl_card = Label(dealer_side, text=dealer_card, font=("Courier", 100))
      dl_card.grid(row=0, column=1)
      Label(dealer_side, text=dealer_value).grid(row=1, column=0, columnspan=100)

def new_new_hit():
  global card_back
  global player_value
  global player_card
  global dealer_value
  global dealer_card
  global money
  global bet
  global money_display
  global bet_display
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)
  
  if type_ >=9:
    player_value += 10
  else:  
    player_value += type_ + 1
  player_card += deck[type_][num]
  
  ply_card = Label(player_side, text=player_card, font=("Courier", 100))
  ply_card.grid(row=0, column=0)
  Label(player_side, text=player_value).grid(row=1, column=0, columnspan=3)

  if player_value >= 21:
    Button(side_board, text="Hit", command=new_hit, state=DISABLED).grid(row=4, column=1)
    Button(side_board, text="Double Down", command=double_down, state=DISABLED).grid(row=4, column=3)

def stand():
 global dealer_value
 global dealer_card
 global player_value
 global money
 global bet
 global money_display
 global root
 global bet_display
 global split_yeah
 global player_side
 if split_yeah:
  Button(side_board, text="Hit", command=new_hit).grid(row=4, column=1)
 else:
  Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
  card_back.destroy()
  while dealer_value < 18:
    if dealer_value > player_value:
      break
    else:
      type_ = random.randint(0, 12)
      num = random.randint(0, 3)

      if type_ >=9:
        dealer_value += 10
      else:  
        dealer_value += (type_ + 1)
      dealer_card += deck[type_][num]

      dl_card = Label(dealer_side, text=dealer_card, font=("Courier", 100))
      dl_card.grid(row=0, column=1)
      Label(dealer_side, text=dealer_value).grid(row=1, column=0, columnspan=100)

  win()

def hit():
 global card_back
 global player_value
 global player_card
 global dealer_value
 global dealer_card
 global money
 global bet
 global money_display
 global bet_display
 type_ = random.randint(0, 12)
 num = random.randint(0, 3)
 
 if type_ >=9:
  player_value += 10
 else:  
  player_value += type_ + 1
 player_card += deck[type_][num]
 
 ply_card = Label(player_side, text=player_card, font=("Courier", 100))
 ply_card.grid(row=0, column=0)
 Label(player_side, text=player_value).grid(row=1, column=0, columnspan=3)

 if player_value > 21:
  Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)

  if type_ >=9:
   dealer_value += 10
  else:  
   dealer_value += (type_ + 1)
  dealer_card += deck[type_][num]

  card_back.destroy()
  dl_card = Label(dealer_side, text=dealer_card, font=("Courier", 100))
  dl_card.grid(row=0, column=1)
  Label(dealer_side, text=dealer_value).grid(row=1, column=0, columnspan=3)
  response = messagebox.askyesno("HAND BUST", "Dealer won! Next hand?")

  Button(side_board, text="Double Down", command=double_down, state=DISABLED).grid(row=4, column=3)
  Button(side_board, text="Stand", command=stand, state=DISABLED).grid(row=4, column=0)
  if response == 1:
   root.destroy()
   board_setup()
 elif player_value == 21:
  Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)

  if type_ >=9:
   dealer_value += 10
  else:  
   dealer_value += (type_ + 1)
  dealer_card += deck[type_][num]

  card_back.destroy()
  dl_card = Label(dealer_side, text=dealer_card, font=("Courier", 100))
  dl_card.grid(row=0, column=1)
  Label(dealer_side, text=dealer_value).grid(row=1, column=0, columnspan=3)
  money += (bet*2.5)
  money_display.destroy()
  bet_display.destroy()
  money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
  money_display.grid(row=0, column=0, columnspan=4, sticky=E)
  bet_display = Label(side_board, text="+"+str(bet*2.5), font=("Roboto", 15), bg="dark green", fg="green")
  bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
  response = messagebox.askyesno("21", "You won! Next hand?")

  Button(side_board, text="Double Down", command=double_down, state=DISABLED).grid(row=4, column=3)
  Button(side_board, text="Stand", command=stand, state=DISABLED).grid(row=4, column=0)
  if response == 1:
   root.destroy()
   board_setup()

def split():
 global board
 global player_side
 global one_card
 global two_card
 global player_value
 global ply_card
 global money
 global bet
 global money_display
 global bet_display
 global player_card
 global split_yeah
 global split_value
 global split_board
 global new_bet

 Button(side_board, text="Hit", command=new_new_hit).grid(row=4, column=1)
 Button(side_board, text="Split", command=split, state=DISABLED).grid(row=4, column=2)
 split_yeah = True
 ply_card.destroy()
 bet_display.destroy()
 money_display.destroy()
 money -= bet
 new_bet = bet
 bet_display = Label(side_board, text="-"+str(bet)+" -"+str(new_bet), font=("Roboto", 15), bg="dark green", fg="red")
 bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
 
 money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
 money_display.grid(row=0, column=0, columnspan=4, sticky=E)

 split_board = LabelFrame(board)
 split_board.grid(row=1, column=1)
 split_card = Label(split_board, text=two_card, font=("Courier", 100))
 split_card.grid(row=0, column=0)
 Label(split_board, text=str(player_value/2)).grid(row=1, column=0, columnspan=100)
 ply_card = Label(player_side, text=one_card, font=("Courier", 100))
 ply_card.grid(row=0, column=0)
 Label(player_side, text=str(player_value/2)).grid(row=1, column=0, columnspan=100)

 player_card = one_card
 player_value /= 2
 split_value = player_value
 
def double_down():
 global money
 global bet
 global money_display
 global bet_display
 global side_board
 global player_value
 global player_card
 global player_side
 global dealer_value
 global dealer_card
 global dealer_side
 Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
 Button(side_board, text="Double Down", command=double_down, state=DISABLED).grid(row=4, column=3)
 if money - bet >= 0:
  money -= bet
  bet += bet
  money_display.destroy()
  bet_display.destroy()
  money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
  money_display.grid(row=0, column=0, columnspan=4, sticky=E)
  bet_display = Label(side_board, text="-"+str(bet), font=("Roboto", 15), bg="dark green", fg="red")
  bet_display.grid(row=1, column=0, columnspan=3, sticky=E)

 type_ = random.randint(0, 12)
 num = random.randint(0, 3)
 
 if type_ >=9:
  player_value += 10
 else:  
  player_value += type_ + 1
 player_card += deck[type_][num]
    
 ply_card = Label(player_side, text=player_card, font=("Courier", 100))
 ply_card.grid(row=0, column=0)
 Label(player_side, text=player_value).grid(row=1, column=0, columnspan=3)

 if player_value > 21:
  Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)

  if type_ >=9:
   dealer_value += 10
  else:  
   dealer_value += (type_ + 1)
  dealer_card += deck[type_][num]

  card_back.destroy()
  dl_card = Label(dealer_side, text=dealer_card, font=("Courier", 100))
  dl_card.grid(row=0, column=1)
  Label(dealer_side, text=dealer_value).grid(row=1, column=0, columnspan=3)
  response = messagebox.askyesno("HAND BUST", "Dealer won! Next hand?")

  if response == 1:
   root.destroy()
   board_setup()
 elif player_value == 21:
  Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)

  if type_ >=9:
   dealer_value += 10
  else:  
   dealer_value += (type_ + 1)
  dealer_card += deck[type_][num]

  card_back.destroy()
  dl_card = Label(dealer_side, text=dealer_card, font=("Courier", 100))
  dl_card.grid(row=0, column=1)
  Label(dealer_side, text=dealer_value).grid(row=1, column=0, columnspan=3)
  money += (bet*2.5)
  money_display.destroy()
  bet_display.destroy()
  money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
  money_display.grid(row=0, column=0, columnspan=4, sticky=E)
  bet_display = Label(side_board, text="+"+str(bet*2.5), font=("Roboto", 15), bg="dark green", fg="green")
  bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
  response = messagebox.askyesno("21", "You won! Next hand?")
  if response == 1:
   root.destroy()
   board_setup()
 else:
  stand()

def show_bet():
 global money
 global money_display
 global bet_display
 global bet
 global final_bet
 bet_display.destroy()
 money_display.destroy()
 final_bet = grab.get()
 try:
  money -= int(final_bet)
 except ValueError as err:
  # if valueerr  statement ?
  print(err)
  

 if money < 0:
  money += int(final_bet)
  bet = 0
 else:
  try:
   bet = int(final_bet)
  except ValueError as err:
   print(err)
 
 if bet == 0:
  Label(terminal, text="***ERROR***\nPlace a bet.").grid(row=0, column=0)
 else:
  deal()
  Button(side_board, text="Confirm Bet", state=DISABLED).grid(row=2, column=0, columnspan=4)

 bet_display = Label(side_board, text="-"+final_bet, font=("Roboto", 15), bg="dark green", fg="red")
 bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
 
 money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
 money_display.grid(row=0, column=0, columnspan=4, sticky=E)

def board_setup():
 global side_board
 global grab
 global money
 global money_display
 global bet_display
 global terminal
 global bet
 global deal
 global deck
 global dealer_side
 global player_side
 global root
 global board
 global final_bet
 root = Tk()
 root.title("Blackjack")
 
 grab = StringVar()
 deck = [
   ('\N{PLAYING CARD ACE OF SPADES}', '\N{PLAYING CARD ACE OF HEARTS}', '\N{PLAYING CARD ACE OF DIAMONDS}', '\N{PLAYING CARD ACE OF CLUBS}'),
   ('\N{PLAYING CARD TWO OF SPADES}', '\N{PLAYING CARD TWO OF HEARTS}', '\N{PLAYING CARD TWO OF DIAMONDS}', '\N{PLAYING CARD TWO OF CLUBS}'),
   ('\N{PLAYING CARD THREE OF SPADES}', '\N{PLAYING CARD THREE OF HEARTS}', '\N{PLAYING CARD THREE OF DIAMONDS}', '\N{PLAYING CARD THREE OF CLUBS}'),
   ('\N{PLAYING CARD FOUR OF SPADES}', '\N{PLAYING CARD FOUR OF HEARTS}', '\N{PLAYING CARD FOUR OF DIAMONDS}', '\N{PLAYING CARD FOUR OF CLUBS}'),
   ('\N{PLAYING CARD FIVE OF SPADES}', '\N{PLAYING CARD FIVE OF HEARTS}', '\N{PLAYING CARD FIVE OF DIAMONDS}', '\N{PLAYING CARD FIVE OF CLUBS}'),
   ('\N{PLAYING CARD SIX OF SPADES}', '\N{PLAYING CARD SIX OF HEARTS}', '\N{PLAYING CARD SIX OF DIAMONDS}', '\N{PLAYING CARD SIX OF CLUBS}'),
   ('\N{PLAYING CARD SEVEN OF SPADES}', '\N{PLAYING CARD SEVEN OF HEARTS}', '\N{PLAYING CARD SEVEN OF DIAMONDS}', '\N{PLAYING CARD SEVEN OF CLUBS}'),
   ('\N{PLAYING CARD EIGHT OF SPADES}', '\N{PLAYING CARD EIGHT OF HEARTS}', '\N{PLAYING CARD EIGHT OF DIAMONDS}', '\N{PLAYING CARD EIGHT OF CLUBS}'),
   ('\N{PLAYING CARD NINE OF SPADES}', '\N{PLAYING CARD NINE OF HEARTS}', '\N{PLAYING CARD NINE OF DIAMONDS}', '\N{PLAYING CARD NINE OF CLUBS}'),

   ('\N{PLAYING CARD TEN OF SPADES}', '\N{PLAYING CARD TEN OF HEARTS}', '\N{PLAYING CARD TEN OF DIAMONDS}', '\N{PLAYING CARD TEN OF CLUBS}'),
   ('\N{PLAYING CARD JACK OF SPADES}', '\N{PLAYING CARD JACK OF HEARTS}', '\N{PLAYING CARD JACK OF DIAMONDS}', '\N{PLAYING CARD JACK OF CLUBS}'),
   ('\N{PLAYING CARD KING OF SPADES}', '\N{PLAYING CARD KING OF HEARTS}', '\N{PLAYING CARD KING OF DIAMONDS}', '\N{PLAYING CARD KING OF CLUBS}'),
   ('\N{PLAYING CARD QUEEN OF SPADES}', '\N{PLAYING CARD QUEEN OF HEARTS}', '\N{PLAYING CARD QUEEN OF DIAMONDS}', '\N{PLAYING CARD QUEEN OF CLUBS}')
 ]
 grab.set(final_bet)
 player_card = ''
 dealer_card = ''
 # Board
 board = LabelFrame(root)
 side_board = LabelFrame(root, bg="dark green")
 dealer_side = LabelFrame(board)
 player_side = LabelFrame(board)
 terminal = LabelFrame(root)

 board.grid(row=0, column=0)
 dealer_side.grid(row=0, column=0)
 player_side.grid(row=1, column=0)
 side_board.grid(row=0, column=1, sticky=N)
 terminal.grid(row=0, column=1, sticky=S)

 # Side
 money_display = Label(side_board, text="$"+f'{money:,}', font=("Roboto", 15), bg="dark green", fg="white")
 money_display.grid(row=0, column=0, columnspan=4, sticky=E)
 bet_display = Label(side_board, text="-0", font=("Roboto", 15), bg="dark green", fg="red")
 bet_display.grid(row=1, column=0, columnspan=3, sticky=E)
 drop = OptionMenu(side_board, grab, *bets)
 drop.grid(row=1, column=1, columnspan=4, sticky=E)
 Button(side_board, text="Confirm Bet", command=show_bet).grid(row=2, column=0, columnspan=4)

 Button(side_board, text="Stand", command=stand, state=DISABLED).grid(row=4, column=0)
 Button(side_board, text="Hit", command=hit, state=DISABLED).grid(row=4, column=1)
 Button(side_board, text="Split", command=split, state=DISABLED).grid(row=4, column=2)
 Button(side_board, text="Double Down", command=double_down, state=DISABLED).grid(row=4, column=3)

 def deal():
  global player_card
  global dealer_card
  global player_value
  global dealer_value
  global card_back
  global dealer_card
  global player_card
  global dl_card
  global one_card
  global two_card
  global ply_card
  global money
  global bet

  player_card = ''
  dealer_card = ''
  # Player
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)
  if type_ >=9:
   one_value=10
  elif type_ == 0:
   one_value = 11
  else:
   one_value = type_ + 1
  one_card = deck[type_][num]
  one_c = type_

  # Player 2nd card
  two_value = 0
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)
  if type_ >=9:
   two_value += 10
  elif type_ == 0:
   two_value += 11
  else:
   two_value += type_ + 1
  two_card = deck[type_][num]
  two_c = type_

  player_value = two_value + one_value
  player_card = one_card + two_card
  # Dealer
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)
  if type_ >=9:
   dealer_value=10
  elif type_ == 0:
   dealer_value = 11
  else:
   dealer_value = type_ + 1
  dealer_card = deck[type_][num]
  

  # Board setup
  card_back = Label(dealer_side, text='\N{PLAYING CARD BACK}', font=("Courier", 100))
  card_back.grid(row=0, column=0)
  dl_card = Label(dealer_side, text=dealer_card, font=("Courier", 100))
  dl_card.grid(row=0, column=1)
  Label(dealer_side, text=dealer_value).grid(row=1, column=0, columnspan=100)
  ply_card = Label(player_side, text=player_card, font=("Courier", 100))
  ply_card.grid(row=0, column=0)
  Label(player_side, text=player_value).grid(row=1, column=0, columnspan=100)

  Button(side_board, text="Stand", command=stand).grid(row=4, column=0)
  Button(side_board, text="Hit", command=hit).grid(row=4, column=1)
  if one_c == two_c:
   Button(side_board, text="Split", command=split).grid(row=4, column=2)
  if money - bet >= 0:
   Button(side_board, text="Double Down", command=double_down).grid(row=4, column=3)
  else:
   Button(side_board, text="Double Down", command=double_down, state=DISABLED).grid(row=4, column=3)

split_yeah = False
money = 1000
bets = [10, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
final_bet = bets[2]

board_setup()
mainloop()
