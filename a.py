def guess_the_type(event):
  
    print(
        "Guess whether this is a \n 1)dependent \n 2)independent \n 3)mutually exclusive \n 4)not mutually exclusive event \n"
    )
    print(event)
    answer = int(input("Enter your answer : "))
    if event == Dependence:
        if answer == 1:
            print("\n You guessed it right! \n \n \n")
            return 'correct'
        else:
            print("\n Your answer is wrong... \n \n \n")
            return 'wrong'
    if event == mutually_exclusive:
        if answer == 3:
            print("\n You guessed it right! \n \n \n")
            return 'correct'
        else:
            print("\n Your answer is wrong... \n \n \n")
            return 'wrong'
    if event == notmutuallyexclusive:
        if answer == 4:
            print("\n You guessed it right! \n \n \n")
            return 'correct'
        else:
            print("\n Your answer is wrong... \n \n \n")
            return 'wrong'
    if event == indipendent:
        if answer == 2:
            print("\n You guessed it right! \n \n \n")
            return 'correct'

        else:
            print("\n Your answer is wrong... \n \n \n")
            return 'wrong'

Dependence = "Dependent Event"
mutually_exclusive = "Mutually Exclusive Event"
notmutuallyexclusive = "Not Mutually Exclusive Event"
indipendent = "Independent Event"

firstanswer=guess_the_type(Dependence)
secondanswer=guess_the_type(mutually_exclusive)
thirdanswer=guess_the_type(notmutuallyexclusive)
fourthanswer=guess_the_type(indipendent)
if firstanswer=='correct' and secondanswer=='correct' and thirdanswer=='correct' and fourthanswer=='correct':
      print("\n \n \n You have guessed all the events correctly! Here's some cookies: 🍪🍪🍪 \n \n \n")