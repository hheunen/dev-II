from tp7conception import *

if __name__ == "__main__":
    #Création de fraction

    fraction_a = Fraction(9, 3) 
    fraction_b = Fraction(14, 3)
    fraction_c = Fraction(13, 11)

    #test d'affichage

    print("La fraction A :", fraction_a, ' sous sa forme réduite')
    print("La fraction A :", fraction_a.as_mixed_number(), ' sous sa forme réduite en "mixed number"')
    print("La fraction B :", fraction_b.as_mixed_number(), ' sous sa forme réduite en "mixed number"')
    print('La fraction B :', float(fraction_b), ' sous le format float')


    #test de +,-,*,/,**, ==

    bool = True
    string_erreurs = ''


    if (fraction_a + fraction_b) != Fraction(23, 3):

        bool = False
        string_erreurs += ' erreur de somme '

    if fraction_a - fraction_b != Fraction(-5, 3):

        bool = False
        string_erreurs += ' erreur de soustaction '

    if fraction_a * fraction_b != Fraction(126, 9):

        bool = False
        string_erreurs += ' erreur de multiplication '

    if fraction_a / fraction_b != Fraction(9, 14):

        bool = False
        string_erreurs += ' erreur de division '

    if fraction_c ** 3 != Fraction(13 ** 3 , 11 ** 3 ):

        bool = False
        string_erreurs += ' erreur d\'exponentiel '
        

    if bool:

        print("Tous les opérateurs fonctionnent")

    else:

        print('Voici les opérateurs qui ne fonctionnent pas : ' + string_erreurs)


    #test de is_zero, is_integer, is_proper, is_unit, is_adjacent_to
    bool2 = True
    string_erreurs2 = ''

    if not Fraction(0, 2).is_zero() or Fraction(1, 2).is_zero():
        
        bool2 = False
        string_erreurs2 = 'erreur is_zero'

    if not Fraction(2, 2).is_integer() or Fraction(1, 2).is_integer():
        
        bool2 = False
        string_erreurs2 = 'erreur is_integer'

    if not Fraction(1, 2).is_proper() or Fraction(3, 2).is_proper():
        
        bool2 = False
        string_erreurs2 = 'erreur is_proper'

    if not Fraction(1, 2).is_unit() or Fraction(3, 2).is_unit():
        
        bool2 = False
        string_erreurs2 = 'erreur is_unit'

    if (not Fraction(1, 2).is_adjacent_to(Fraction(2, 2)) or
        not Fraction(-3, 2).is_adjacent_to(Fraction(-2, 2)) or
        Fraction(1, 2).is_adjacent_to(Fraction(2/ 5))):
        
        bool2 = False
        string_erreurs2 = 'erreur is_zero'

    if bool:

        print("Tous les propriétes fonctionnent")

    else:

        print('Voici les propriétés qui ne fonctionnent pas : ' + string_erreurs)




    #test de la division de fraction avec un zéro
    try:
        fraction_a = Fraction(2, 3)
        fraction_b = Fraction(0 / 4)
        print(fraction_a / fraction_b)
    except ValueError as e:
        print(e)

    #test de création de fraction avec un 0 
    try:
        print(Fraction(0 , 0))
    except ValueError as e:
        print(e)