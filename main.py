

import random



import hangman_art
import hangman_words
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

chosen_word_LIST=list(chosen_word)

list1=[]
for x in range (len(chosen_word)):
  list1.append("_")

for x in range (0,2):
  a=random.randint(0,(len(chosen_word)-1))
  list1[a]=(chosen_word_LIST[a])

print(f'GUESS THE WORD, IT IS A "{word_length}" LETTERED WORD (you can have 6 wrong choices), HINT :\n\n {" ".join(list1)} \n\n "THIS IS FOR ONLY HINT , YOU HAVE TO GUESS EACH LETTER "\n')


display = []
for _ in range(word_length):
    display += "_"
chosen_before=[]
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for q in (chosen_before):
      if guess==q:
        print(f' WARNING!! "{guess}" already guessed')
    chosen_before.append(guess)

    


    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

   
    if guess not in chosen_word:
        
        print(f"{guess},the letter is not in the chosen_word")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"GAME OVER , THE WORD WAS {chosen_word}\n You lose!!.")
        if lives<=2 and lives>0:
          
          EXTRA_HINT= input ('BY TYPING YES YOU MAY HAVE EXTRA HINT OR MAY HAVE NOT ,TYPE YES OR HIT ANY BUTTON TO CONTINUE :\n')
          if EXTRA_HINT=="yes" or  EXTRA_HINT=="YES":
            b=random.randint(0,(len(chosen_word)-1))
            list1[b]=(chosen_word_LIST[b])
            print(f'{" ".join(list1)}')           
            
    
    print(f"{' '.join(display)}")

    
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(hangman_art.stages[lives])