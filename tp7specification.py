class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num, den are an integers
        POST : create an object Fraction
        RAISES : NulParamException if den==0
        """
        pass

    @property
    def numerator(self):
        pass
    @property
    def denominator(self):
        pass

# ------------------ Textual representations ------------------

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : self is an object Fraction
        POST : return "num / den" of the object Fraction
        """
        pass

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : self is an object Fraction
        POST : return the reduced form of the object Fraction, self.num and self.den has no more
                a commun divisor
        """
        pass

    
# ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : self = object Fraction, other = object Fraction
         POST : return self.num/self.den + other.num/other.den
                
                
         """
        pass


    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE : self = object Fraction, other = object Fraction
         POST : return self.num/self.den - other.num/other.den
        """
        pass


    def __mul__(self, other):
        """Overloading of the * operator for fractions
 
         PRE : self = object Fraction, other = object Fraction
         POST : (return self.num/self.den) * (other.num/other.den)
        """
        pass


    def __truediv__(self, other):
        """Overloading of the / operator for fractions

         PRE : self = object Fraction, other = object Fraction
         POST : (self.num/self.den) / (other.num/other.den)
        """
        pass


    def __pow__(self, other):
        """Overloading of the ** operator for fractions

         PRE : self = object Fraction, other = integer
         POST : return (self.num/self.den) ^ other
        """
        pass
    
    
    def __eq__(self, other) : 
        """Overloading of the == operator for fractions
        
         PRE : self = object Fraction, other = object Fraction
         POST : return self == other
        
        """
        
    def __float__(self) :
        """Returns the decimal value of the fraction

        PRE : self = object Fraction
         POST : return float(self.num/self.den)
        """
        pass
    
# TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)



# ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : self is an object Fraction
        POST : return self.num == 0
        """
        pass


    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : self is an object Fraction
        POST : return if self.num / self.den is an integer  
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : self is an object Fraction
        POST : return |self.num/self.den| < 1
        """

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : self is an object Fraction
        POST : return true if self.num/self.den at his reduced form is 1 else false
        """
        pass

    def is_adjacent_to(self, other) :
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

         PRE : self is an object Fraction, other is an object Fraction
        POST : return true when the fraction self and the fraction other are set at same denominator
                and |self.num-other.num| ==1 else false
        """
        pass

