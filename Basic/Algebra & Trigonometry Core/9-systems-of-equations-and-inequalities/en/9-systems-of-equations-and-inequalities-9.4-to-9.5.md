# Systems of Equations and Inequalities

## 9.4 Partial Fractions

---
Earlier in this chapter, we studied systems of two equations in two variables, systems of three equations in three variables, and nonlinear systems.
Here we introduce another way that systems of equations can be utilized—the decomposition of rational expressions.
Fractions can be complicated; adding a variable in the denominator makes them even more so.
The methods studied in this section will help simplify the concept of a rational expression.
Decomposing P(x ) Q(x ) Where Q(x ) Has Only Nonrepeated Linear Factors Recall the algebra regarding adding and subtracting rational expressions.
These operations depend on finding a common denominator so that we can write the sum or difference as a single, simplified rational expression.
In this section, we will look at partial fraction decomposition, which is the undoing of the procedure to add or subtract rational expressions.
In other words, it is a return from the single simplified rational expression to the original expressions, called the partial fractions.
For example, suppose we add the following fractions: x - 3 + -1 x + 2 We would first need to find a common denominator, (x + 2)(x - 3).
Next, we would write each expression with this common denominator and find the sum of the terms.

 x - 3 ( x + 2 x + 2 ) + -1 x + 2 ( x - 3 x - 3 ) = 2x + 4 - x + 3


(x + 2)(x - 3) = x + 7 x² - x - 6 Partial fraction decomposition is the reverse of this procedure.
We would start with the solution and rewrite (decompose) it as the sum of two fractions. x + 7 x² - x - 6 

Simplified sum = x - 3 + -1 x + 2 

Partial fraction decomposition We will investigate rational expressions with linear factors and quadratic factors in the denominator where the degree of the numerator is less than the degree of the denominator.
Regardless of the type of expression we are decomposing, the first and most important thing to do is factor the denominator.
When the denominator of the simplified expression contains distinct linear factors, it is likely that each of the original rational expressions, which were added or subtracted, had one of the linear factors as the denominator.
In other words, using the example above, the factors of x² - x - 6 are (x - 3)(x + 2), the denominators of the decomposed rational expression.
So we will rewrite the simplified form as the sum of individual fractions and use a variable for each numerator.
Then, we will solve for each numerator using one of several methods available for partial fraction decomposition.
Learning Objectives
In this section, you will:
• Decompose P (x )Q (x ), where Q (x ) has only nonrepeated linear factors.
• Decompose P (x )Q (x ), where Q (x ) has repeated linear factors.
• Decompose P (x )Q (x ), where Q (x ) has a nonrepeated irreducible quadratic factor.
• Decompose P (x )Q (x ), where Q (x ) has a repeated irreducible quadratic factor.
partial fraction decomposition of P(x) Q(x) : Q(x) has nonrepeated linear factors The partial fraction decomposition of P(x) Q(x) when Q(x) has nonrepeated linear factors and the degree of P(x) is less than the degree of Q(x) is P(x) Q(x) = A¹ __ ( a¹x + b¹ ) + A² __ ( a² x + b² ) + A³ __ ( a³x + b³ ) + ... + An __ ( anx + bn ) .

---
### 💡 **How To…**
Given a rational expression with distinct linear factors in the denominator, decompose it. 1.
Use a variable for the original numerators, usually A, B, or C, depending on the number of factors, placing each variable over a single factor.
For the purpose of this definition, we use An for each numerator P(x) Q(x) = A¹ __ ( a¹x + b¹ ) + A² __ ( a² x + b² ) + ... + An __ ( anx + bn ) . 2.
Multiply both sides of the equation by the common denominator to eliminate fractions. 3.
Expand the right side of the equation and collect like terms. 4.
Set coefficients of like terms from the left side of the equation equal to those on the right side to create a system of equations to solve for the numerators.

---
### 📐 **Example 1**:
Decomposing a Rational Function with Distinct Linear Factors

Decompose the given rational expression with distinct linear factors.

 3x 

(x + 2)(x - 1)

**Solution**

We will separate the denominator factors and give each numerator a symbolic label, like A, B, or C.

 3x 

(x + 2)(x - 1) = A (x + 2) + B (x - 1) Multiply both sides of the equation by the common denominator to eliminate the fractions:

(x + 2)(x - 1)[ 3x 

(x + 2)(x - 1) ] = (x + 2)(x - 1)[ A (x + 2) ] + (x + 2)(x - 1)[ B (x - 1) ] The resulting equation is

3x = A(x - 1) + B(x + 2) Expand the right side of the equation and collect like terms.

3x = Ax - A + Bx + 2B

3x = (A + B)x - A + 2B Set up a system of equations associating corresponding coefficients.

3 = A + B

0 = -A + 2B Add the two equations and solve for B.

3 = A + B

0 = -A + 2B

3 = 0 + 3B

1 = B Substitute B = 1 into one of the original equations in the system.

3 = A + 1

2 = A Thus, the partial fraction decomposition is

 3x 

(x + 2)(x - 1) = (x + 2) + (x - 1) 

Another method to use to solve for A or B is by considering the equation that resulted from eliminating the fractions and substituting a value for x that will make either the A- or B-term equal 0.
If we let x = 1, the A-term becomes 0 and we can simply solve for B.

3x = A(x - 1) + B(x + 2)

3(1) = A[(1) - 1] + B[(1) + 2]

3 = 0 + 3B

1 = B Next, either substitute B = 1 into the equation and solve for A, or make the B-term 0 by substituting x = -2 into the equation.

3x = A(x - 1) + B(x + 2)

3(-2) = A[(-2) - 1] + B[(-2) + 2]

-6 = -3A + 0

 -6 -3 = A

2 = A We obtain the same values for A and B using either method, so the decompositions are the same using either method.

 3x 

(x + 2)(x - 1) = (x + 2) + (x - 1) Although this method is not seen very often in textbooks, we present it here as an alternative that may make some partial fraction decompositions easier.
It is known as the Heaviside method, named after Charles Heaviside, a pioneer in the study of electronics.

---
### ✏️ **Try It #1**
Find the partial fraction decomposition of the following expression. x 

(x - 3)(x - 2) Decomposing P(x ) Q(x ) Where Q(x ) Has Repeated Linear Factors Some fractions we may come across are special cases that we can decompose into partial fractions with repeated linear factors.
We must remember that we account for repeated factors by writing each factor in increasing powers. partial fraction decomposition of P(x) Q(x) : Q(x) has repeated linear factors The partial fraction decomposition of P(x) Q(x) when Q(x) has repeated linear factor occurring n times and the degree of P(x) is less than the degree of Q(x), is P(x) Q(x) = A¹ (ax + b) + A² (ax + b)² + A³ (ax + b)³ + ... + An (ax + b)n Write the denominator powers in increasing order.

---
### 💡 **How To…**
Given a rational expression with repeated linear factors, decompose it. 1.
Use a variable like A, B, or C for the numerators and account for increasing powers of the denominators.
P(x) Q(x) = A¹ (ax + b) + A² (ax + b)² + ... + An (ax + b)n 2.
Multiply both sides of the equation by the common denominator to eliminate fractions. 3.
Expand the right side of the equation and collect like terms. 4.
Set coefficients of like terms from the left side of the equation equal to those on the right side to create a system of equations to solve for the numerators.

---
### 📐 **Example 2**:
Decomposing with Repeated Linear Factors

Decompose the given rational expression with repeated linear factors.

 -x² + 2x + 4


x³ - 4x² + 4x

**Solution**

The denominator factors are x(x - 2)². To allow for the repeated factor of (x - 2), the decomposition will include three denominators: x, (x - 2), and (x - 2)². Thus,

 -x² + 2x + 4


x³ - 4x² + 4x = (A)/(x) + B (x - 2) + C (x - 2)² Next, we multiply both sides by the common denominator.

x(x - 2)²[ -x² + 2x + 4

 x(x - 2)²

 ] = [ (A)/(x) + B (x - 2) + C (x - 2)² ] x(x - 2)²

-x² + 2x + 4 = A(x - 2)² + Bx(x-2) + Cx On the right side of the equation, we expand and collect like terms.

-x² + 2x + 4 = A(x² - 4x + 4) + B(x² - 2x) + Cx

= Ax² - 4Ax + 4A + Bx² - 2Bx + Cx

= (A + B)x² + ( -4A - 2B + C)x + 4A Next, we compare the coefficients of both sides. This will give the system of equations in three variables:

-x² + 2x + 4 = (A + B)x² + (-4A - 2B + C)x + 4A

A + B = -1 (1)

-4A - 2B + C = 2 (2)

4A = 4 (3) Solving for A, we have

4A = 4

A = 1 Substitute A = 1 into equation (1).

A + B = -1

(1) + B = -1

B = -2 Then, to solve for C, substitute the values for A and B into equation (2).

-4A - 2B + C = 2

-4(1) - 2(-2) + C = 2

-4 + 4 + C = 2

C = 2 Thus,

 -x² + 2x + 4


x³ - 4x² + 4x = 1/x - (x - 2) + (x - 2)² 

---
### ✏️ **Try It #2**
Find the partial fraction decomposition of the expression with repeated linear factors.

 6x - 11 (x - 1)² 

### Decomposing P(x )

 Q(x ) Where Q(x ) Has a Nonrepeated Irreducible Quadratic Factor So far, we have performed partial fraction decomposition with expressions that have had linear factors in the denominator, and we applied numerators A, B, or C representing constants.
Now we will look at an example where one of the factors in the denominator is a quadratic expression that does not factor.
This is referred to as an irreducible quadratic factor.
In cases like this, we use a linear numerator such as Ax + B, Bx + C, etc. decomposition of P(x) Q(x): Q(x) has a nonrepeated irreducible quadratic factor The partial fraction decomposition of P(x) Q(x) such that Q(x) has a nonrepeated irreducible quadratic factor and the degree of P(x) is less than the degree of Q(x), is written as P(x) Q(x) = A¹ x + B¹ 

(a¹

x 2 + b¹ x + c¹) + A² x + B² 

(a² x² + b² x + c²) + ... + An x + Bn 

(an x² + bn x + cn) The decomposition may contain more rational expressions if there are linear factors. Each linear factor will have a different constant numerator: A, B, C, and so on.

---
### 💡 **How To…**
Given a rational expression where the factors of the denominator are distinct, irreducible quadratic factors, decompose it. 1.
Use variables such as A, B, or C for the constant numerators over linear factors, and linear expressions such as A¹ x + B¹, A²x + B², etc., for the numerators of each quadratic factor in the denominator.
P(x) Q(x) = A ax + b + A¹ x + B¹ 

(a¹ x² + b¹ x + c¹) + A² x + B² 

(a² x² + b² x + c²) + ... + An x + Bn 

(an x 2 + bn x + cn) 2.
Multiply both sides of the equation by the common denominator to eliminate fractions. 3.
Expand the right side of the equation and collect like terms. 4.
Set coefficients of like terms from the left side of the equation equal to those on the right side to create a system of equations to solve for the numerators.

---
### 📐 **Example 3**: Decomposing P(x)

 Q(x) When Q(x) Contains a Nonrepeated Irreducible Quadratic Factor Find a partial fraction decomposition of the given expression.

 8x² + 12x - 20


(x + 3)(x² + x + 2)

**Solution**

We have one linear factor and one irreducible quadratic factor in the denominator, so one numerator will be a constant and the other numerator will be a linear expression.
Thus,


(x + 3)(x² + x + 2) = A (x + 3) + Bx + C (x² + x + 2) We follow the same steps as in previous problems. First, clear the fractions by multiplying both sides of the equation by the common denominator.

(x + 3)(x² + x + 2)[ 8x² + 12x - 20


(x + 3)(x² + x + 2) ] = [ A (x + 3) + Bx + C (x² + x + 2) ] (x + 3)(x² + x + 2)

8x² + 12x - 20 = A(x² + x + 2) + (Bx + C)(x + 3)

Notice we could easily solve for A by choosing a value for x that will make the Bx + C term equal 0.
Let x = -3 and substitute it into the equation.

8x² + 12x - 20 = A(x² + x + 2) + (Bx + C)(x + 3)

8(-3)² + 12(-3) - 20 = A((-3)² + (-3) + 2) + (B(-3) + C)((-3) + 3)

A = 2 Now that we know the value of A, substitute it back into the equation.
Then expand the right side and collect like terms.

8x² + 12x - 20 = 2(x² + x + 2) + (Bx + C)(x + 3)

8x² + 12x - 20 = 2x² + 2x + 4 + Bx² + 3B + Cx + 3C

8x² + 12x - 20 = (2 + B)x² + (2 + 3B + C)x + (4 + 3C) Setting the coefficients of terms on the right side equal to the coefficients of terms on the left side gives the system of equations.

2 + B = 8 (1)

2 + 3B + C = 12 (2)

4 + 3C = -20 (3) Solve for B using equation (1) and solve for C using equation (3).

2 + B = 8 (1)

B = 6

4 + 3C = -20 (3)

C = -8 Thus, the partial fraction decomposition of the expression is

 8x² + 12x - 20


(x + 3)(x² + x + 2) = (x + 3) + 6x - 8 (x² + x + 2) Could we have just set up a system of equations to solve Example 3?
Yes, we could have solved it by setting up a system of equations without solving for A first.
The expansion on the right would be:

8x² + 12x - 20 = Ax² + Ax + 2A + Bx² + 3B + Cx + 3C

8x² + 12x - 20 = (A + B)x² + (A + 3B + C)x + (2A + 3C) So the system of equations would be:

A + B = 8

A + 3B + C = 12

2A + 3C = -20

---
### ✏️ **Try It #3**
Find the partial fraction decomposition of the expression with a nonrepeating irreducible quadratic factor. 5x² - 6x + 7


(x - 1)(x² + 1) 

### Decomposing P(x )

 Q(x ) Where Q(x ) Has a Repeated Irreducible Quadratic Factor Now that we can decompose a simplified rational expression with an irreducible quadratic factor, we will learn how to do partial fraction decomposition when the simplified rational expression has repeated irreducible quadratic factors.
The decomposition will consist of partial fractions with linear numerators over each irreducible quadratic factor represented in increasing powers. decomposition of P(x) Q(x) : when Q(x) has a repeated irreducible quadratic factor The partial fraction decomposition of P(x) Q(x) , when Q(x) has a repeated irreducible quadratic factor and the degree of P(x) is less than the degree of Q(x), is P(x) 

(ax 2 + bx + c) n = A¹ x + B¹ 

(ax 2 + bx + c) + A² x + B² 

(ax 2 + bx + c)² + A³ x + B³ 

(ax 2 + bx + c)³ + ... + An x + Bn 

(ax 2 + bx + c) n Write the denominators in increasing powers.

---
### 💡 **How To…**
Given a rational expression that has a repeated irreducible factor, decompose it. 1.
Use variables like A, B, or C for the constant numerators over linear factors, and linear expressions such as A¹x + B¹, A²x + B², etc., for the numerators of each quadratic factor in the denominator written in increasing powers, such as P(x) Q(x) = A ax + b + A¹ x + B¹ 

(ax² + bx + c) + A² x + B² 

(ax² + bx + c)² + ... + An x + Bn 

(ax 2 + bx + c) n 2.
Multiply both sides of the equation by the common denominator to eliminate fractions. 3.
Expand the right side of the equation and collect like terms. 4.
Set coefficients of like terms from the left side of the equation equal to those on the right side to create a system of equations to solve for the numerators.

---
### 📐 **Example 4**
Decomposing a Rational Function with a Repeated Irreducible Quadratic Factor in the Denominator Decompose the given expression that has a repeated irreducible factor in the denominator. x⁴ + x³ + x² - x + 1


x(x² + 1)²

**Solution**

The factors of the denominator are x, (x² + 1), and (x² + 1)².
Recall that, when a factor in the denominator is a quadratic that includes at least two terms, the numerator must be of the linear form Ax + B.
So, let’s begin the decomposition.

 x⁴ + x³ + x² - x + 1


x(x² + 1)²

 = (A)/(x) + Bx + C (x² + 1) + Dx + E (x² + 1)² We eliminate the denominators by multiplying each term by x(x² + 1)². Thus,

x⁴ + x³ + x² - x + 1 = A(x² + 1)² + (Bx + C)(x)(x² + 1) + (Dx + E)(x) Expand the right side. x⁴ + x³ + x² - x + 1 = A(x⁴ + 2x² + 1) + Bx⁴ + Bx² + Cx³ + Cx + Dx² + Ex

= Ax⁴ + 2Ax² + A + Bx⁴ + Bx² + Cx³ + Cx + Dx² + Ex Now we will collect like terms. x⁴ + x³ + x² - x + 1 = (A + B)x⁴ + (C)x³ + (2A + B + D)x² + (C + E)x + A

Set up the system of equations matching corresponding coefficients on each side of the equal sign.

A + B = 1

C = 1

2A + B + D = 1

C + E = -1

A = 1 We can use substitution from this point.
Substitute A = 1 into the first equation.

1 + B = 1

B = 0 Substitute A = 1 and B = 0 into the third equation.

2(1) + 0 + D = 1

D = -1 Substitute C = 1 into the fourth equation.

1 + E = -1

E = -2 Now we have solved for all of the unknowns on the right side of the equal sign.
We have A = 1, B = 0, C = 1, D = -1, and E = -2.
We can write the decomposition as follows: x⁴ + x³ + x² - x + 1


x(x² + 1)²

 = 1/x + (x² + 1) - x + 2 (x² + 1)² 

---
### ✏️ **Try It #4**
Find the partial fraction decomposition of the expression with a repeated irreducible quadratic factor.

 x³ - 4x² + 9x-5


(x² -2x + 3)² Access these online resources for additional instruction and practice with partial fractions.
• Partial Fraction Decomposition (http://openstaxcollege.org/l/partdecomp) • Partial Fraction Decomposition With Repeated Linear Factors (http://openstaxcollege.org/l/partdecomprlf) • Partial Fraction Decomposition With Linear and Quadratic Factors (http://openstaxcollege.org/l/partdecomlqu)

## 9.4 Section Exercises

---
### 9.4 Section Exercises

Verbal 1.
Can any quotient of polynomials be decomposed into at least two partial fractions?
If so, explain why, and if not, give an example of such a fraction 2.
Can you explain why a partial fraction decomposition is unique? (Hint: Think about it as a system of equations.) 3.
Can you explain how to verify a partial fraction decomposition graphically? 4.
You are unsure if you correctly decomposed the partial fraction correctly.
Explain how you could double check your answer. 5.
Once you have a system of equations generated by the partial fraction decomposition, can you explain another method to solve it?
For example if you had 

3x² + 8x + 15 = A x + 1 + B 3x + 5 , we eventually simplify to 7x + 13 = A(3x + 5) + B(x + 1).
Explain how you could intelligently choose an x-value that will eliminate either A or B and solve for A and B.
Algebraic For the following exercises, find the decomposition of the partial fraction for the nonrepeating linear factors. 6. 

x² + 10x + 24 7. x² - 5x - 24 8. -x - 24 x² - 2x - 24 x² + 7x + 10 10. x 

 11. 

 12. x + 1 x² + 7x + 10/x² - 9 x² - 25 x² - 4 16. 2x - 3 x² - 6x + 5/x² - x - 6 18. 4x + 3 x² + 8x + 15 19. 3x - 1 x² -5x + 6 For the following exercises, find the decomposition of the partial fraction for the repeating linear factors. (x + 4)² 21. x (x - 2)² (x + 3)² (4x + 5)² (6x - 7)² 25. 5 - x (x - 7)² 26. 

 2x(x + 1)² 


5x(3x + 5)² 


2x² (3x + 2)²

 30. x³ - 5x² + 12x + 144


x²(x² + 12x + 36) 

For the following exercises, find the decomposition of the partial fraction for the irreducible non repeating quadratic factor. 31. 4x² + 6x + 11


(x + 2)(x² + x + 3) 32. 4x² + 9x + 23


(x - 1)(x² + 6x + 11) 33. -2x² + 10x + 4


(x - 1)(x² + 3x + 8) 34. x² + 3x + 1


(x + 1)(x² + 5x - 2) 35. 4x² + 17x - 1


(x + 3)(x² + 6x + 1) 36. 4x² 

(x + 5)(x² + 7x - 5) 37. 4x² + 5x + 3 x³ - 1

 38. -5x² + 18x - 4

 x³ + 8

 x³ + 27

 40. x² + 2x + 40 


 42. -50x² + 5x - 3


x⁴ + 216x

 For the following exercises, find the decomposition of the partial fraction for the irreducible repeating quadratic factor. 44. 3x³ + 2x² + 14x + 15


(x² + 4)²

 45. x³ + 6x² + 5x + 9


(x² + 1)²

 46. x³ - x² + x - 1

 (x² - 3)²

 47. x² + 5x + 5 (x + 2)² 48. x³ + 2x² + 4x


(x² + 2x + 9)² 49. x² + 25 

(x² + 3x + 25)² 


(2x² + x + 14)²

 x(x² + 4)² 52. x⁴ + x³ + 8x² + 6x + 36


x(x² + 6)²

 (x² - x)² 54. 5x³ - 2x + 1 (x² + 2x)² Extensions For the following exercises, find the partial fraction expansion. 55. x² + 4 (x + 1)³ 56. x³ - 4x² + 5x + 4

 (x - 2)³

 For the following exercises, perform the operation and then find the partial fraction decomposition.
57. x + 8 + x - 2 - x - 1 x² -6x - 16 58. x - 4 - x + 6 - 2x + 7 x² + 2x - 24 59. 2x x² - 16 - 1-2x x² + 6x + 8 - x - 5 x² - 4x 

## 9.5 Matrices and Matrix Operations

---
Two club soccer teams, the Wildcats and the Mud Cats, are hoping to obtain new equipment for an upcoming season.
Wildcats Mud Cats Goals Balls Jerseys A goal costs $300; a ball costs $10; and a jersey costs $30.
How can we find the total cost for the equipment needed for each team?
In this section, we discover a method in which the data in the soccer equipment table can be displayed and used for calculating other information.
Then, we will be able to calculate the cost of the equipment.
Finding the Sum and Difference of Two Matrices To solve a problem like the one described for the soccer teams, we can use a matrix, which is a rectangular array of numbers.
A row in a matrix is a set of numbers that are aligned horizontally.
A column in a matrix is a set of numbers that are aligned vertically.
Each number is an entry, sometimes called an element, of the matrix.
Matrices (plural) are enclosed in [ ] or ( ), and are usually named with capital letters.
For example, three matrices named A, B, and C are shown below.
A = [ 1 2

 ] , B = [ 

 ] , C = [ -1 3

 ] Learning Objectives
In this section, you will:
• Find the sum and difference of two matrices.
• Find scalar multiples of a matrix.
• Find the product of two matrices.

### Describing Matrices

A matrix is often referred to by its size or dimensions: m × n indicating m rows and n columns.
Matrix entries are defined first by row and then by column.
For example, to locate the entry in matrix A identified as aij, we look for the entry in row i, column j.
In matrix A, shown below, the entry in row 2, column 3 is a²3.
A = [ a¹1 a¹2 a¹3

a²1 a²2 a²3

a³1 a³2 a³3 ] A square matrix is a matrix with dimensions n × n, meaning that it has the same number of rows as columns.
The 3 × 3 matrix above is an example of a square matrix.
A row matrix is a matrix consisting of one row with dimensions 1 × n. [a¹1 a¹2 a¹3] A column matrix is a matrix consisting of one column with dimensions m × 1. [ a¹1

a¹2 a¹3 ] A matrix may be used to represent a system of equations.
In these cases, the numbers represent the coefficients of the variables in the system.
Matrices often make solving systems of equations easier because they are not encumbered with variables.
We will investigate this idea further in the next section, but first we will look at basic matrix operations. matrices A matrix is a rectangular array of numbers that is usually named by a capital letter:
A, B, C, and so on.
Each entry in a matrix is referred to as aij, such that i represents the row and j represents the column.
Matrices are often referred to by their dimensions: m × n indicating m rows and n columns.

---
### 📐 **Example 1**
Finding the Dimensions of the Given Matrix and Locating Entries Given matrix A: a.
What are the dimensions of matrix A? b.
What are the entries at a³1 and a²2 ?

A = [ 

 ] 

**Solution**

a.
The dimensions are 3 × 3 because there are three rows and three columns. b.
Entry a³1 is the number at row 3, column 1, which is 3.
The entry a²2 is the number at row 2, column 2, which is 4.
Remember, the row comes first, then the column.
Adding and Subtracting Matrices We use matrices to list data or to represent systems.
Because the entries are numbers, we can perform operations on matrices.
We add or subtract matrices by adding or subtracting corresponding entries.
In order to do this, the entries must correspond.
Therefore, addition and subtraction of matrices is only possible when the matrices have the same dimensions.
We can add or subtract a 3 × 3 matrix and another 3 × 3 matrix, but we cannot add or subtract a 2 × 3 matrix and a 3 × 3 matrix because some entries in one matrix will not have a corresponding entry in the other matrix.

adding and subtracting matrices Given matrices A and B of like dimensions, addition and subtraction of A and B will produce matrix C or matrix D of the same dimension.
A + B = C such that aij + bij = cij A - B = D such that aij - bij = dij Matrix addition is commutative.

A + B = B + A It is also associative.

(A + B) + C = A + (B + C)

---
### 📐 **Example 2**
Finding the Sum of Matrices Find the sum of A and B, given

A = [ a b

c d ] and B = [ e f

g h ]

**Solution**

Add corresponding entries.

A + B = [ a b

c d ] + [ e f

g h ] 

= [ a + e b + f

c + g d + h ] 

---
### 📐 **Example 3**:
Adding Matrix A and Matrix B

Find the sum of A and B.

A = [ 4 1

 ] and B = [ 5 9

 ]

**Solution**

Add corresponding entries.
Add the entry in row 1, column 1, a¹1, of matrix A to the entry in row 1, column 1, b¹1, of B.
Continue the pattern until all entries have been added.

A + B = [ 4 1

 ] + [ 5 9

 ] 

= [ 4 + 5 1 + 9

3 + 0 2 + 7 ] 

= [ 9 10

 ] 

---
### 📐 **Example 4**:
Finding the Difference of Two Matrices

Find the difference of A and B.

A = [ -2 3

 ] and B = [ 8 1

 ]

**Solution**

We subtract the corresponding entries of each matrix.

A - B = [ -2 3

 ] - [ 8 1

 ] 

= [ -2 - 8 3 - 1

0 - 5 1 - 4 ] 

= [ -10 2

-5 -3 ] 

---
### 📐 **Example 5**
Finding the Sum and Difference of Two 3 x 3 Matrices Given A and B : a.
Find the sum. b.
Find the difference.
A = [ 

4 -2 2 ] and B = [ 6 10 -2

-5 2 -2 ] 

**Solution**

a.
Add the corresponding entries.

A + B = [ 

4 -2 2 ] + [ 6 10 -2

-5 2 -2 ] 

= [ 2 + 6 -10 + 10 -2 - 2

4 - 5 -2 + 2 2 - 2 ] 

= [ 

-1 0 -0 ] b.
Subtract the corresponding entries.

A - B = [ 

4 -2 2 ] - [ 6 10 -2

-5 2 -2 ] 

= [ 2 - 6 -10 - 10 -2 + 2

14 - 0 12 + 12 10 + 4

4 + 5 -2 - 2 2 + 2 ] 

= [ -4 -20 0

9 -4 4 ] 

---
### ✏️ **Try It #1**
Add matrix A and matrix B.
A = [ 1 0 -3 ] and B = [ -2 1 5 -4 ]
Finding Scalar Multiples of a Matrix Besides adding and subtracting whole matrices, there are many situations in which we need to multiply a matrix by a constant called a scalar.
Recall that a scalar is a real number quantity that has magnitude, but not direction.
For example, time, temperature, and distance are scalar quantities.
The process of scalar multiplication involves multiplying each entry in a matrix by a scalar.
A scalar multiple is any entry of a matrix that results from scalar multiplication.
Consider a real-world scenario in which a university needs to add to its inventory of computers, computer tables, and chairs in two of the campus labs due to increased enrollment.
They estimate that 15% more equipment is needed in both labs.
The school’s current inventory is displayed in Table 2.
Lab A Lab B Computers Computer Tables Chairs

Converting the data to a matrix, we have

C²013 = [ 

 ] To calculate how much computer equipment will be needed, we multiply all entries in matrix C by 0.15.

 ] = [ 

 ] We must round up to the next integer, so the amount of new equipment needed is

[ 

 ] Adding the two matrices as shown below, we see the new inventory amounts.

[ 

 ] + [ 

 ] = [ 

 ] This means

C²014 = [ 

 ]
Thus, Lab A will have 18 computers, 19 computer tables, and 19 chairs; Lab B will have 32 computers, 40 computer tables, and 40 chairs. scalar multiplication Scalar multiplication involves finding the product of a constant by each entry in the matrix.
Given

A = [ a¹1 a¹2

a²1 a²2 ] the scalar multiple cA is

cA = c[ a¹1 a¹2

a²1 a²2 ] 

= [ ca¹1 ca¹2

ca²1 ca²2 ] Scalar multiplication is distributive.
For the matrices A, B, and C with scalars a and b,

a(A + B) = aA + aB

(a + b)A = aA + bA

---
### 📐 **Example 6**:
Multiplying the Matrix by a Scalar

Multiply matrix A by the scalar 3.

A = [ 8 1

 ]

**Solution**

Multiply each entry in A by the scalar 3.

3A = 3[ 8 1

 ] 

= [ 3 ⋅ 8 3 ⋅ 1

3 ⋅ 5 3 ⋅ 4 ] 

= [ 24 3

---
### ✏️ **Try It #2**
Given matrix B, find -2B where A = [ 4 1

 ] 

---
### 📐 **Example 7**
Finding the Sum of Scalar Multiples Find the sum 3A + 2B.
A = [ 1 -2 0

0 -1 2

4 3 -6 ] and B = [ -1 2 1

0 -3 2

0 1 -4 ]

**Solution**

First, find 3A, then 2B.

3A = [ 3 ⋅ 1 3(-2) 3 ⋅ 0

3 ⋅ 0 3(-1) 3 ⋅ 2

3 ⋅ 4 3 ⋅ 3 3(-6) ] 

= [ 3 -6 0

0 -3 6

 ] 

2B = [ 2(-1) 2 ⋅ 2 2 ⋅ 1

2 ⋅ 0 2(-3) 2 ⋅ 2

2 ⋅ 0 2 ⋅ 1 2(-4) ] 

= [ -2 4 2

0 -6 4

0 2 -8 ] Now, add 3A + 2B.

3A + 2B = [ 3 -6 0

0 -3 6

 ] + [ -2 4 2

0 -6 4

0 2 -8 ] 

= [ 3 - 2 -6 + 4 0 + 2

0 + 0 -3 - 6 6 + 4

12 + 0 9 + 2 -18 - 8 ] 

= [ 1 -2 2

0 -9 10

 ] Finding the Product of Two Matrices In addition to multiplying a matrix by a scalar, we can multiply two matrices.
Finding the product of two matrices is only possible when the inner dimensions are the same, meaning that the number of columns of the first matrix is equal to the number of rows of the second matrix.
If A is an m × r matrix and B is an r × n matrix, then the product matrix AB is an m × n matrix.
For example, the product AB is possible because the number of columns in A is the same as the number of rows in B.
If the inner dimensions do not match, the product is not defined.
A ⋅ B 2 × 3 3 × 3 same We multiply entries of A with entries of B according to a specific pattern as outlined below.
The process of matrix multiplication becomes clearer when working a problem with real numbers.
To obtain the entries in row i of AB, we multiply the entries in row i of A by column j in B and add.
For example, given matrices A and B, where the dimensions of A are 2 × 3 and the dimensions of B are 3 × 3, the product of AB will be a 2 × 3 matrix.

A = [ a¹1 a¹2 a¹3

a²1 a²2 a²3 ] and B = [ b¹1 b¹2 b¹3

b²1 b²2 b²3

b³1 b³2 b³3 ] 

Multiply and add as follows to obtain the first entry of the product matrix AB. 1.
To obtain the entry in row 1, column 1 of AB, multiply the first row in A by the first column in B, and add.

[a¹1 a¹2 a¹3][ b¹1

b²1 b³1 ] = a¹1 ⋅ b¹1 + a¹2 ⋅ b²1 + a¹3 ⋅ b³1 2.
To obtain the entry in row 1, column 2 of AB, multiply the first row of A by the second column in B, and add.

[a¹1 a¹2 a¹3][ b¹2

b²2 b³2 ] = a¹1 ⋅ b¹2 + a¹2 ⋅ b²2 + a¹3 ⋅ b³2 3.
To obtain the entry in row 1, column 3 of AB, multiply the first row of A by the third column in B, and add.

[a¹1 a¹2 a¹3][ b¹3

b²3 b³3 ] = a¹1 ⋅ b¹3 + a¹2 ⋅ b²3 + a¹3 ⋅ b³3 We proceed the same way to obtain the second row of AB.
In other words, row 2 of A times column 1 of B; row 2 of A times column 2 of B; row 2 of A times column 3 of B.
When complete, the product matrix will be AB = [ a¹1 ⋅ b¹1 + a¹2 ⋅ b²1 + a¹3 ⋅ b³1 a¹1 ⋅ b¹2 + a¹2 ⋅ b²2 + a¹3 ⋅ b³2 a¹1 ⋅ b¹3 + a¹2 ⋅ b²3 + a¹3 ⋅ b³3

a²1 ⋅ b¹1 + a²2 ⋅ b²1 + a²3 ⋅ b³1 a²1 ⋅ b¹2 + a²2 ⋅ b²2 + a²3 ⋅ b³2 a²1 ⋅ b¹3 + a²2 ⋅ b²3 + a²3 ⋅ b³3 ] properties of matrix multiplication For the matrices A, B, and C the following properties hold.
• Matrix multiplication is associative: (AB)C = A(BC).

C(A + B) = CA + CB, • Matrix multiplication is distributive:

(A + B)C = AC + BC. Note that matrix multiplication is not commutative.

---
### 📐 **Example 8**:
Multiplying Two Matrices

Multiply matrix A and matrix B.
A = [ 1 2

 ] and B = [ 5 6

 ]

**Solution**

First, we check the dimensions of the matrices.
Matrix A has dimensions 2 × 2 and matrix B has dimensions 2 × 2.
The inner dimensions are the same so we can perform the multiplication.
The product will have the dimensions 2 × 2.
We perform the operations outlined previously.

AB = [ 1 2

 ] [ 5 6

 ] 

= [ 1(5) + 2(7) 1(6) + 2(8)

3(5) + 4(7) 3(6) + 4(8) ] 

= [ 19 22

 ] 

---
### 📐 **Example 9**:
Multiplying Two Matrices

Given A and B : a.
Find AB. b.
Find BA.

A = [ -1 2 3

4 0 5 ] and B = [ 5 -1

-4 0

 ] 

**Solution**

a.
As the dimensions of A are 2 × 3 and the dimensions of B are 3 × 2, these matrices can be multiplied together because the number of columns in A matches the number of rows in B.
The resulting product will be a 2 × 2 matrix, the number of rows in A by the number of columns in B.

AB = [ -1 2 3

4 0 5 ] [ 5 -1

-4 0

 ] 

= [ -1(5) + 2(-4) + 3(2) -1(-1) + 2(0) + 3(3)

4(5) + 0(-4) + 5(2) 4(-1) + 0(0) + 5(3) ] 

= [ -7 10

b.
The dimensions of B are 3 × 2 and the dimensions of A are 2 × 3.
The inner dimensions match so the product is defined and will be a 3 × 3 matrix.

BA = [ 5 -1

-4 0

 ] [ -1 2 3

4 0 5 ] 

= [ 5(-1) + -1(4) 5(2) + -1(0) 5(3) + -1(5)

-4(-1) + 0(4) -4(2) + 0(0) -4(3) + 0(5)

2(-1) + 3(4) 2(2) + 3(0) 2(3) + 3(5) ] 

= [ -9 10 10

10 4 21 ] Analysis Notice that the products AB and BA are not equal.
AB = [ -7 10

30 11 ] ≠ [ -9 10 10

10 4 21 ] = BA This illustrates the fact that matrix multiplication is not commutative.
Is it possible for AB to be defined but not BA?
Yes, consider a matrix A with dimension 3 × 4 and matrix B with dimension 4 × 2.
For the product AB the inner dimensions are 4 and the product is defined, but for the product BA the inner dimensions are 2 and 3 so the product is undefined.

---
### 📐 **Example 10**
Using Matrices in Real-World Problems Let’s return to the problem presented at the opening of this section.
We have Table 3, representing the equipment needs of two soccer teams.
Wildcats Mud Cats Goals Balls Jerseys We are also given the prices of the equipment, as shown in Table 4.
Goals $300 Balls $10 Jerseys $30

We will convert the data to matrices.
Thus, the equipment need matrix is written as

E = [ 

 ] The cost matrix is written as

We perform matrix multiplication to obtain costs for the equipment.

CE = [300 10 30][ 

 ] 

The total cost for equipment for the Wildcats is $2,520, and the total cost for equipment for the Mud Cats is $3,840.

---
### 💡 **How To…**
Given a matrix operation, evaluate using a calculator. 1.
Save each matrix as a matrix variable [A], [B], [C], ... 2.
Enter the operation into the calculator, calling up each matrix variable as needed. 3.
If the operation is defined, the calculator will present the solution matrix; if the operation is undefined, it will display an error message.

---
### 📐 **Example 11**
Using a Calculator to Perform Matrix Operations Find AB - C given A = [ 

 ] , B = [ 

-24 52 19

 ] , and C = [ 

 ] .

**Solution**

On the matrix page of the calculator, we enter matrix A above as the matrix variable [A], matrix B above as the matrix variable [B], and matrix C above as the matrix variable [C].
On the home screen of the calculator, we type in the problem and call up each matrix variable as needed. [A]× [B] - [C] The calculator gives us the following matrix. [ 

 ]
Access these online resources for additional instruction and practice with matrices and matrix operations.
• Dimensions of a Matrix (http://openstaxcollege.org/l/matrixdimen) • Matrix Addition and Subtraction (http://openstaxcollege.org/l/matrixaddsub) • Matrix Operations (http://openstaxcollege.org/l/matrixoper) • Matrix Multiplication (http://openstaxcollege.org/l/matrixmult)

### 9.5 Section Exercises

Verbal 1.
Can we add any two matrices together?
If so, explain why; if not, explain why not and give an example of two matrices that cannot be added together. 2.
Can we multiply any column matrix by any row matrix?
Explain why or why not. 3.
Can both the products AB and BA be defined?
If so, explain how; if not, explain why. 4.
Can any two matrices of the same size be multiplied?
If so, explain why, and if not, explain why not and give an example of two matrices of the same size that cannot be multiplied together. 5.
Does matrix multiplication commute?
That is, does AB = BA?
If so, prove why it does.
If not, explain why it does not.
Algebraic For the following exercises, use the matrices below and perform the matrix addition or subtraction.
Indicate if the operation is undefined.
A = [ 1 3

0 7 ] , B = [ 2 14

22 6 ] , C = [ 

 ] , D = [ 

 ] , E = [ 6 12

14 5 ] , F = [ 

 ] 6.
A + B 7.
C + D 8.
A + C 9.
B - E 10.
C + F 11.
D - B For the following exercises, use the matrices below to perform scalar multiplication.
A = [ 4 6

13 12 ] , B = [ 

 ] , C = [ 16 3 7 18

90 5 3 29 ] , D = [ 

 ] __ 2 C For the following exercises, use the matrices below to perform matrix multiplication.
A = [ -1 5

3 2 ] , B = [ 3 6 4

-8 0 12 ] , C = [ 

-2 6

 ] , D = [ 2 -3 12

9 3 1

0 8 -10 ] For the following exercises, use the matrices below to perform the indicated operation if possible.
If not possible, explain why the operation cannot be performed.
A = [ 2 -5

6 7 ] , B = [ -9 6

-4 2 ] , C = [ 0 9

7 1 ] , D = [ -8 7 -5

 ] , E = [ 4 5 3

7 -6 -5

1 0 9 ] 24.
A + B - C

## 9.5 Section Exercises

---
For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed. (Hint: A² = A ⋅ A) A = [ -10 20

5 25 ] , B = [ 40 10

-20 30 ] , C = [ -1 0

0 -1

 ] 38.
A² B² 39.
(AB)² 40.
(BA)² For the following exercises, use the matrices below to perform the indicated operation if possible.
If not possible, explain why the operation cannot be performed.
(Hint: A² = A ⋅ A) A = [ 1 0

2 3 ] , B = [ -2 3 4

-1 1 -5 ] , C = [ 

 ] , D = [ 

-6 7 5

 ] 48.
(AB)C 49.
A(BC) Technology For the following exercises, use the matrices below to perform the indicated operation if possible.
If not possible, explain why the operation cannot be performed.
Use a calculator to verify your solution.
A = [ -2 0 9

 ] , B = [ 

 ] , C = [ 

 ] Extensions For the following exercises, use the matrix below to perform the indicated operation on the given matrix.
B = [ 0 0 1 ] 59.
Using the above questions, find a formula for Bn.
Test the formula for B²01 and B²02, using a calculator.

