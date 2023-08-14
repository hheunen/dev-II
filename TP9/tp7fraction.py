def reduce_fraction(num, den):

            pgdc=0

            for number in range(1,den+1):

                if num % number == 0 and den % number == 0:

                    pgdc = number

            return (num // pgdc, den // pgdc)

class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(self,num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num, den are an integers
        POST : create an object Fraction
        RAISES : NulParamException if den==0
        """
        if den == 0:

            raise ValueError("Demoninator cannot be zero")

        self.__num = num
        self.__den =den

    @property
    def numerator(self):
        return self.__num
    
    @property
    def denominator(self):
        return self.__den

    @numerator.setter
    def numerator(self, new_num):
        self.__num = new_num
    
    @denominator.setter
    def denominator(self, new_den):
        self.__den = new_den


# ------------------ Textual representations ------------------

    def __str__(self) :

        num,dem = reduce_fraction(self.numerator, self.denominator)
        return str(num) + '/' + str(dem) 

    def as_mixed_number(self) :

        num,dem = reduce_fraction(self.numerator, self.denominator)
        count = 0
        string_fraction = ''
        
        while num/dem >= 1:

            count += 1
            num -= dem
        
        if num != 0:

            string_fraction=(' + '+ str(num) +'/'+ str(dem))

        return str(count) + string_fraction

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):

        num_self, dem_self = reduce_fraction(self.numerator, self.denominator)
        num_other, dem_other = reduce_fraction(other.numerator, other.denominator)
        new_numerator =  num_self * dem_other + dem_self * num_other
        new_denominator = dem_self * dem_other

        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):

        num_self, dem_self = reduce_fraction(self.numerator, self.denominator)
        num_other, dem_other = reduce_fraction(other.numerator, other.denominator)
        new_numerator =  num_self * dem_other - dem_self * num_other
        new_denominator = dem_self * dem_other

        return Fraction(new_numerator, new_denominator)
        


    def __mul__(self, other):
        """Overloading of the * operator for fractions
 
         PRE : self = object Fraction, other = object Fraction
         POST : (return self.num/self.den) * (other.num/other.den)
        """
        num_self, dem_self=reduce_fraction(self.numerator, self.denominator)
        num_other, dem_other=reduce_fraction(other.numerator, other.denominator)
        new_numerator =  num_self * num_other
        new_denominator = dem_self * dem_other

        return Fraction(new_numerator, new_denominator) 


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

         PRE : self = object Fraction, other = object Fraction
         POST : (self.num/self.den) / (other.num/other.den)
        """
        if other.numerator == 0:

            raise ValueError("Demoninator cannot be zero")

        num_self, dem_self = reduce_fraction(self.numerator, self.denominator)
        num_other, dem_other = reduce_fraction(other.numerator, other.denominator)
        new_numerator =  num_self * dem_other
        new_denominator = dem_self * num_other

        return Fraction(new_numerator, new_denominator)

        


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : self = object Fraction, other = integer
         POST : return (self.num/self.den) ^ (other.num/other.den)
        """
        num_self, dem_self = reduce_fraction(self.numerator, self.denominator)
        new_numerator = num_self ** other
        new_denominator = dem_self ** other

        return Fraction(new_numerator, new_denominator) 
        
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
         PRE : self = object Fraction, other = object Fraction
         POST : return self == other
        
        """
        num_self, dem_self = reduce_fraction(self.numerator, self.denominator)
        num_other, dem_other = reduce_fraction(other.numerator, other.denominator)

        return num_self == num_other and dem_self == dem_other
        
    def __float__(self) :
        return self.numerator / self.denominator
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : self is an object Fraction
        POST : return self.num == 0
        """
        return self.numerator == 0


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : self is an object Fraction
        POST : return if self.num / self.den is an integer  
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : self is an object Fraction
        POST : return |self.num/self.den| < 1
        """
        return self.numerator / self.denominator < 1 and self.numerator / self.denominator > -1

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : self is an object Fraction
        POST : return true if self.num/self.den at his reduced form is 1 else false
        """
        num, dem = reduce_fraction(self.numerator, self.denominator)
        
        return num == 1 

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

         PRE : self is an object Fraction, other is an object Fraction
        POST : return true when the fraction self and the fraction other are set at same denominator
                and |self.num-other.num| ==1 else false
        """
        fraction_diff = self-other
        num, dem = reduce_fraction(fraction_diff.numerator, fraction_diff.denominator)

        return num == 1
# ------------------ Exception ------------------
