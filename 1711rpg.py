# 17/11/2026

# RPG Game start

import random
# from random import randint




enenmy = ["Demon" ,"Dragon"]
hp_hero = 100
hp_enemy = 100

hero_name = 'SRT' #input("Enter Your Hero name: ")
Enemy = random.choice(enenmy)
# hero_name = input("Enter Your Hero name: ")


while(True):
    hploss = random.randint(1,20)
    hp_enemy -= hploss

    print(f"HP lost from {Enemy} : {hploss} \nHP remaining in {Enemy} : {hp_enemy} \n\n")
    if hp_enemy <= 0:
        print(f"Hero {hero_name} Won \nHP of {hero_name} : {hp_hero} \nHP of {Enemy} : {hp_enemy}")
        break


    hploss = random.randint(1,20)
    hp_hero -= hploss

    print(f"HP lost from Hero : {hploss} \nHP remaining in {hero_name} : {hp_hero}\n\n")
    if hp_hero <= 0:
        print(f"{Enemy} won \nHP of {Enemy} : {hp_enemy} \nHP of {hero_name} : {hp_hero}")
        break