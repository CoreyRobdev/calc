from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Blackjack")

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
bet = 0
money = 1000
grab = StringVar()
bets = [10, 50, 100, 500, 1000]
final = ''
final_=''


def start():
  global dl_card
  global ply_card
  global player_card
  global player_value
  global dealer_card
  global dealer_value
  global card_back
  global final_
  final_.destroy()
  
  dl_card=''
  ply_card=''
  player_card = ''
  dealer_card = ''
  final_ = ''
  final_ = Label(root, text=final, font=("Roboto", 18), padx=20)
  final_.grid(row=1, column=0, columnspan=3)
  dl_card = Label(board, text=dealer_card, font=("Courier", 100))
  dl_card.grid(row=0, column=1)
  ply_card = Label(hand, text=player_card, font=("Courier", 100))
  ply_card.grid(row=0, column=0)
  # Player
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)
  if type_ >=9:
    player_value=10
  else:  
    player_value = type_ + 1
  player_card += '' + deck[type_][num]

  type_ = random.randint(0, 12)
  num = random.randint(0, 3)
  if type_ >=9:
    player_value += 10
  else:  
    player_value += (type_ + 1)
  player_card += '' + deck[type_][num]

  # Dealer
  type_ = random.randint(0, 12)
  num = random.randint(0, 3)
  if type_ >=9:
    dealer_value=10
  else:  
    dealer_value = type_ + 1
  dealer_card = deck[type_][num]

  # Board setup
  card_back = Label(board, text='\N{PLAYING CARD BACK}', font=("Courier", 100))
  card_back.grid(row=0, column=0)
  dl_card = Label(board, text=dealer_card, font=("Courier", 100))
  dl_card.grid(row=0, column=1)
  Label(board, text=dealer_value).grid(row=1, column=0, columnspan=3)
  ply_card = Label(hand, text=player_card, font=("Courier", 100))
  ply_card.grid(row=0, column=0)
  Label(hand, text=player_value).grid(row=1, column=0, columnspan=3)

def hit():
  global player_card
  global ply_card
  global player_value
  global dealer_value
  global dealer_card
  if bet == 0:
    messagebox.askokcancel("Error", "PLACE A BET")
  else:
    new_val = player_value
    type_ = random.randint(0, 12)
    num = random.randint(0, 3)

    if type_ >=9:
      player_value = new_val + 10
    else:  
      player_value = new_val + (type_ + 1)
    player_card += '' + deck[type_][num]
    
    ply_card = Label(hand, text=player_card, font=("Courier", 100))
    ply_card.grid(row=0, column=0)
    Label(hand, text=player_value).grid(row=1, column=0, columnspan=3)
    if player_value > 21:
      Button(root, text="Hit", command=hit, state=DISABLED).grid(row=3, column=2)
      
      Label(root, text='HOUSE WINS!!!', font=("Roboto", 18), padx=20).grid(row=1, column=0, columnspan=3)
      type_ = random.randint(0, 12)
      num = random.randint(0, 3)

      if type_ >=9:
        dealer_value += 10
      else:  
        dealer_value += (type_ + 1)
      dealer_card += '' + deck[type_][num]

      card_back.destroy()
      dl_card = Label(board, text=dealer_card, font=("Courier", 100))
      dl_card.grid(row=0, column=1)
      Label(board, text=dealer_value).grid(row=1, column=0, columnspan=3)

def stand():
  global dealer_card
  global dl_card
  global dealer_value
  global player_value
  global money
  global final_
  
  if bet == 0:
    messagebox.askokcancel("Error", "PLACE A BET")
  else:
    Button(root, text="Hit", command=hit, state=DISABLED).grid(row=3, column=2)
    card_back.destroy()
    while dealer_value < player_value:
      type_ = random.randint(0, 12)
      num = random.randint(0, 3)

      if type_ >=9:
        dealer_value += 10
      else:  
        dealer_value += (type_ + 1)
      dealer_card += '' + deck[type_][num]
      
      dl_card = Label(board, text=dealer_card, font=("Courier", 100))
      dl_card.grid(row=0, column=1)
      Label(board, text=dealer_value).grid(row=1, column=0, columnspan=3)

    if dealer_value > 21:
      final = 'PLAYER WINS!!!'
      money += (bet*2)
    elif player_value > 21:
      final = 'HOUSE WINS!!!'
    elif player_value < dealer_value:
      final = 'HOUSE WINS!!!'
    elif dealer_value < player_value:
      final = 'PLAYER WINS!!!'
      money += (bet*2)
    else:
      final = 'DRAW!!!'
      money += bet
    final_=''
    final_ = Label(root, text=final, font=("Roboto", 18), padx=20)
    final_.grid(row=1, column=0, columnspan=3)
    Label(money_board, text="Money: $"+f'{money:,}', font=("Roboto", 15), bg="green", fg="white").grid(row=0, column=0, columnspan=2)

def split():
  return

def double():
  return

def confirm_bet():
  global money
  global bet
  money -= int(grab.get())
  if money < 0:
    money += int(grab.get())
    bet = 0
  else:
    bet = int(grab.get())
  Label(money_board, text="Money: $"+f'{money:,}', font=("Roboto", 15), bg="green", fg="white").grid(row=0, column=0, columnspan=2)

board = LabelFrame(root)
hand = LabelFrame(root)
money_board = LabelFrame(root, pady=200, bg="green")

Label(money_board, text="Money: $"+f'{money:,}', font=("Roboto", 15), bg="green", fg="white").grid(row=0, column=0, columnspan=2)
Label(money_board, text="Bet: ", font=("Roboto", 15), bg="green", fg="white").grid(row=1, column=0)
drop = OptionMenu(money_board, grab, *bets)
drop.grid(row=1, column=1, padx=(0, 10))
Button(money_board, text="Confirm Bet", font=("Roboto", 12), command=confirm_bet).grid(row=2, column=0, columnspan=2)

money_board.grid(row=0, column=5, rowspan=3)
board.grid(row=0, column=0, columnspan=4)
hand.grid(row=2, column=0, columnspan=5)
Button(root, text="Stand", command=stand).grid(row=3, column=1)
Button(root, text="Hit", command=hit).grid(row=3, column=2)
Button(root, text="Split", command=split).grid(row=3, column=3)
Button(root, text="Double Down", command=double).grid(row=3, column=4)
Button(root, text="Next Hand", command=start).grid(row=4, column=3, columnspan=3)

final_ = Label(root, text=final, font=("Roboto", 18), padx=20)
final_.grid(row=1, column=0, columnspan=3)


start()

mainloop()