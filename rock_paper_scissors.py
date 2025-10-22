import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

chu_va_chi = [rock, paper, scissors]
robot1_choice = random.randint(0, 2)
robot2_choice = random.randint(0, 2)

print("Robot 1 chose:")
print(chu_va_chi[robot1_choice])
print("Robot 2 chose:")
print(chu_va_chi[robot2_choice])

if robot1_choice == robot2_choice:
    print("It's a draw!")

    # rock beats scissors
elif ((robot1_choice == 0 and robot2_choice == 2) or
    # paper beats rock
     (robot1_choice == 1 and robot2_choice == 0) or
    # scissors beats paper
     (robot1_choice == 2 and robot2_choice == 1)):
    print("Robot 1 wins!")
else:
    print("Robot 2 wins!")

