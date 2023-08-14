from user import User
from duocount import Duocount
import os
import time

def route():
    cls()
    list_duocount = [Duocount("famille")]
    list_duocount[0].add_user('annie')
    list_duocount[0].add_user('c1arl')
    
    flag = True
    while flag:
        print("Voici la liste des Duocounts existants :\n")
        for duocount in list_duocount:
            print(duocount.name)
        print("\nSi vous voulez ouvrir un Duocount, taper son nom")
        print("Si vous voulez créer un Duocount, taper un nouveau nom\n")
        print("Si vous voulez quitter, taper 'quitter'")
        user_input = input("")

        duocount_names = [ducount.name for ducount in list_duocount]
        if user_input == "quitter":
            flag = False
        elif user_input in duocount_names:
            cls()
            selected_duocount = get_duocount_by_name(user_input, list_duocount)
            open_duocount(selected_duocount)
        else:
            add_duocount(user_input, list_duocount)
            cls()

def add_duocount(name, duocount_list):
    duocount_list.append(Duocount(name))

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def get_duocount_by_name(name, duocount_list):
    for duocount in duocount_list:
        if duocount.name == name:
            return duocount
    return None 

def open_duocount(duocount):
    cls()
    flag=True
    while flag:
        print(duocount)
        print('Pour ajouter des utilisateurs : adduser "user"')
        print('pour ajouter une dépense : add "prix"')
        print('Pour afficher les comptes à rendre : "show"')
        print('Pour revenir en arrière : quitter \n')
        user_input=input("")
        user_input_split=user_input.split(" ")
        if user_input == "quitter":
            flag=False
        elif user_input =="show":
            cls()
            for user in duocount.users:
                print(user)
            input('\nAppuyer sur une touche pour continuer')
            cls()
        elif len(user_input_split)==2:
            if user_input_split[0] == "adduser":
                duocount.add_user(user_input_split[1])
                cls()
            elif user_input_split[0] == "add":
                price=user_input_split[1]
                while not price.isdigit():
                    price=input("Veuillez entrer un nombre valide : ")
                username=input("Veuillez entrer l'user qui a payé : ")
                while not duocount.user_in(username):
                    username=input("Veuillez entrer un utilisateur valide : ")
                list_username=[]
                list_username.append(username)
                user_input=input("Veuillez entrer la liste des utilisateurs concernés, '0' pour finir : ")
                while not user_input=='0':
                    if duocount.user_in(user_input) and user_input not in list_username:
                        list_username.append(user_input)
                        print(user_input, " a été rajouté")
                    else:
                        print("non valable")
                    user_input=input("Veuillez entrer la liste des utilisateurs concernés, '0' pour finir : ")
                duocount.add_expense(username,price,list_username)
                print("Le compte a été complété")
                cls()
            else: 
                cls()
                print("erreur \n")
                
        else:
            cls()
            print("erreur \n")
    pass