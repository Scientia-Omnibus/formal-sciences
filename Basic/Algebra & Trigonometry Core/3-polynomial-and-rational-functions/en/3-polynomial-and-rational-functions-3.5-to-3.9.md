# Polynomial and Rational Functions

## 3.5 Dividing Polynomials

---
Learning Objectives
In this section, you will:
• Use long division to divide polynomials.
• Use synthetic division to divide polynomials.
The exterior of the Lincoln Memorial in Washington, D.C., is a large rectangular solid with length 61.5 meters ( m ), width 40 m, and height 30 m.[15] We can easily find the volume using elementary geometry.

V = l ⋅ w ⋅ h

So the volume is 73,800 cubic meters (m³). Suppose we knew the volume, length, and width. We could divide to find the height.

h =  V ____ l ⋅ w 

_______

= 30 As we can confirm from the dimensions above, the height is 30 m. We can use similar methods to find any of the missing dimensions. We can also use the same method if any or all of the measurements contain variable expressions. For example, suppose the volume of a rectangular solid is given by the polynomial 3x⁴ - 3x³ - 33x² + 54x. The length of the solid is given by 3x; the width is given by x - 2. To find the height of the solid, we can use polynomial division, which is the focus of this section. Using Long Division to Divide Polynomials We are familiar with the long division algorithm for ordinary arithmetic. We begin by dividing into the digits of the dividend that have the greatest place value. We divide, multiply, subtract, include the digit in the next place value position, and repeat. For example, let’s divide 178 by 3 using long division. Long Division

Step 1: 5 ×  3 = 15 and 17 - 15 = 2

Step 2: Bring down the 8

Step 3: 9 ×  3 = 27 and 28 - 27 = 1

Answer: 59 R 1 or 59 1/3  15. National Park Service. “Lincoln Memorial Building Statistics.” http://www.nps.gov/linc/historyculture/lincoln-memorial-building-statistics.htm. Accessed 4/3/2014/ 3)¹78 -15 -27

Another way to look at the solution is as a sum of parts. This should look familiar, since it is the same method used to check division in elementary arithmetic.

dividend = (divisor ⋅ quotient) + remainder

= 178 We call this the Division Algorithm and will discuss it more formally after looking at an example. Division of polynomials that contain more than one term has similarities to long division of whole numbers. We can write a polynomial dividend as the product of the divisor and the quotient added to the remainder. The terms of the polynomial division correspond to the digits (and place values) of the whole number division. This method allows us to divide two polynomials. For example, if we were to divide 2x³ - 3x² + 4x + 5 by x + 2 using the long division algorithm, it would look like this:

Set up the division problem.

2x³ divided by x is 2x².

Multiply x + 2 by 2x².

Subtract.

Bring down the next term.

-7x² divided by x is -7x.

Multiply x + 2 by -7x.

Subtract. Bring down the next term.

18x divided by x is 18.

Multiply x + 2 by 18.

Subtract. We have found  2x³ - 3x² + 4x + 5/x + 2  = 2x² - 7x + 18 -  31/x + 2  or

 2x³ - 3x² + 4x + 5/x + 2  = (x + 2)(2x² - 7x + 18) - 31 We can identify the dividend, the divisor, the quotient, and the remainder. 2x³ – 3x² + 4x + 5 = (x + 2) (2x² – 7x + 18) + (–31) Dividend Divisor Quotient Remainder Writing the result in this manner illustrates the Division Algorithm. x + 2)²x³ - 3x² + 4x + 5 2x² x + 2)²x³ - 3x² + 4x + 5 2x² x + 2)²x³ - 3x² + 4x + 5 -(2x³ + 4x²) -7x² + 4x 2x² - 7x x + 2)²x³ - 3x² + 4x + 5 -(2x³ + 4x²) -7x² + 4x -(-7x² + 14x) 2x² - 7x + 18 x + 2)²x³ - 3x² + 4x + 5 -(2x³ + 4x²) -7x² + 4x -(-7x² + 14x) -31

the Division Algorithm The Division Algorithm states that, given a polynomial dividend f (x) and a non-zero polynomial divisor d(x) where the degree of d(x) is less than or equal to the degree of f (x), there exist unique polynomials q(x) and r(x) such that f (x) = d(x)q(x) + r(x) q(x) is the quotient and r(x) is the remainder. The remainder is either equal to zero or has degree strictly less than d(x). If r(x) = 0, then d(x) divides evenly into f (x). This means that, in this case, both d(x) and q(x) are factors of f (x).

---
### 💡 **How To…**
Given a polynomial and a binomial, use long division to divide the polynomial by the binomial. 1. Set up the division problem. 2. Determine the first term of the quotient by dividing the leading term of the dividend by the leading term of the divisor. 3. Multiply the answer by the divisor and write it below the like terms of the dividend. 4. Subtract the bottom binomial from the top binomial. 5. Bring down the next term of the dividend. 6. Repeat steps 2–5 until reaching the last term of the dividend. 7. If the remainder is non-zero, express as a fraction using the divisor as the denominator.

---
### 📐 **Example  1**
Using Long Division to Divide a Second-Degree Polynomial Divide 5x² + 3x - 2 by x + 1.

**Solution**

Set up division problem.

5x² divided by x is 5x.

Multiply x + 1 by 5x.

Subtract. Bring down the next term.

-2x divided by x is -2.

Multiply x + 1 by -2.

Subtract. The quotient is 5x - 2. The remainder is 0. We write the result as

 5x² + 3x - 2 __________ x + 1  = 5x - 2 or

5x² + 3x - 2 = (x + 1)(5x - 2) Analysis This division problem had a remainder of 0. This tells us that the dividend is divided evenly by the divisor, and that the divisor is a factor of the dividend. x + 1)⁵x² + 3x - 2 5x x + 1)⁵x² + 3x - 2 5x x + 1)⁵x² + 3x - 2 -(5x² + 5x) -2x - 2 5x - 2 x + 1)⁵x² + 3x - 2 -(5x² + 5x) -2x - 2 -(-2x - 2)

---
### 📐 **Example  2**
Using Long Division to Divide a Third-Degree Polynomial Divide 6x³ + 11x² - 31x + 15 by 3x - 2.

**Solution**

6x³ divided by 3x is 2x².

Multiply 3x - 2 by 2x².

Subtract. Bring down the next term. 15x² divided by 3x is 5x.

Multiply 3x - 2 by 5x.

Subtract. Bring down the next term. -21x divided by 3x is -7.

Multiply 3x - 2 by -7.

Subtract. The remainder is 1. There is a remainder of 1. We can express the result as:

__________________

3x - 2  = 2x² + 5x - 7 +  _____ 3x - 2  Analysis We can check our work by using the Division Algorithm to rewrite the solution. Then multiply.

(3x - 2)(2x² + 5x - 7) + 1 = 6x³ + 11x² - 31x + 15 Notice, as we write our result, • the dividend is 6x³ + 11x² - 31x + 15 • the divisor is 3x - 2 • the quotient is 2x² + 5x - 7 • the remainder is 1

---
### ✏️ **Try It #1**
Divide 16x³ - 12x² + 20x - 3 by 4x + 5. Using Synthetic Division to Divide Polynomials As we’ve seen, long division of polynomials can involve many steps and be quite cumbersome. Synthetic division is a shorthand method of dividing polynomials for the special case of dividing by a linear factor whose leading coefficient is 1. To illustrate the process, recall the example at the beginning of the section. Divide 2x³ - 3x² + 4x + 5 by x + 2 using the long division algorithm. The final form of the process looked like this: 2x² + x + 18 x + 2)²x³ - 3x² + 4x + 5 -(2x³ + 4x²) -7x² + 4x -(-7x² - 14x) -31 There is a lot of repetition in the table. If we don’t write the variables but, instead, line up their coefficients in columns under the division sign and also eliminate the partial products, we already have a simpler version of the entire problem. 2x² + 5x - 7 -(6x³ - 4x²) -(-21x + 14)

-2 -4 -31 Synthetic division carries this simplification even a few more steps. Collapse the table by moving each of the rows up to fill any vacant spots. Also, instead of dividing by 2, as we would in division of whole numbers, then multiplying and subtracting the middle product, we change the sign of the “divisor” to -2, multiply and add. The process starts by bringing down the leading coefficient. -2 -3 -4 -36 -7 -31 We then multiply it by the “divisor” and add, repeating this process column by column, until there are no entries left. The bottom row represents the coefficients of the quotient; the last entry of the bottom row is the remainder. In this case, the quotient is 2x² - 7x + 18 and the remainder is -31. The process will be made more clear in Example 3. synthetic division Synthetic division is a shortcut that can be used when the divisor is a binomial in the form x - k. In synthetic division, only the coefficients are used in the division process.

---
### 💡 **How To…**
Given two polynomials, use synthetic division to divide. 1. Write k for the divisor. 2. Write the coefficients of the dividend. 3. Bring the lead coefficient down. 4. Multiply the lead coefficient by k. Write the product in the next column. 5. Add the terms of the second column. 6. Multiply the result by k. Write the product in the next column. 7. Repeat steps 5 and 6 for the remaining columns. 8. Use the bottom numbers to write the quotient. The number in the last column is the remainder and has degree 0, the next number from the right has degree 1, the next number from the right has degree 2, and so on.

---
### 📐 **Example  3**
Using Synthetic Division to Divide a Second-Degree Polynomial Use synthetic division to divide 5x² - 3x - 36 by x - 3.

**Solution**

Begin by setting up the synthetic division. Write k and the coefficients. Bring down the lead coefficient. Multiply the lead coefficient by k. Continue by adding the numbers in the second column. Multiply the resulting number by k. Write the result in the next column. Then add the numbers in the third column. The result is 5x + 12. The remainder is 0. So x - 3 is a factor of the original polynomial.

Analysis Just as with long division, we can check our work by multiplying the quotient by the divisor and adding the remainder. (x - 3)(5x + 12) + 0 = 5x² - 3x - 36

---
### 📐 **Example  4**
Using Synthetic Division to Divide a Third-Degree Polynomial Use synthetic division to divide 4x 3 + 10x 2 - 6x - 20 by x + 2.

**Solution**

The binomial divisor is x + 2 so k = -2. Add each column, multiply the result by -2, and repeat until the last column is reached. -2 4 -8 -4 -10 The result is 4x 2 + 2x - 10. The remainder is 0. Thus, x + 2 is a factor of 4x³ + 10x² - 6x - 20.

**Analysis**
The graph of the polynomial function f (x) = 4x³ + 10x² - 6x - 20 in Figure 2 shows a zero at x = k = -2. This confirms that x + 2 is a factor of 4x 3 + 10x² - 6x - 20. x y

---
### 📐 **Example  5**
Using Synthetic Division to Divide a Fourth-Degree Polynomial Use synthetic division to divide -9x⁴ + 10x³ + 7x² - 6 by x - 1.

**Solution**

Notice there is no x-term. We will use a zero as the coefficient for that term. 1 -9 -6 -9 -9 The result is -9x³ + x² + 8x + 8 +  2/x - 1 .

---
### ✏️ **Try It #2**
Use synthetic division to divide 3x⁴ + 18x³ - 3x + 40 by x + 7. Using Polynomial Division to Solve Application Problems Polynomial division can be used to solve a variety of application problems involving expressions for area and volume. We looked at an application at the beginning of this section. Now we will solve that problem in the following example.

---
### 📐 **Example  6**
Using Polynomial Division in an Application Problem The volume of a rectangular solid is given by the polynomial 3x⁴ - 3x³ - 33x² + 54x. The length of the solid is given by 3x and the width is given by x - 2. Find the height of the solid.

**Solution**

There are a few ways to approach this problem. We need to divide the expression for the volume of the solid by the expressions for the length and width. Let us create a sketch as in Figure 3. Length 3x Height Width x - 2 We can now write an equation by substituting the known values into the formula for the volume of a rectangular solid.

V = l ⋅ w ⋅ h

3x⁴ - 3x³ - 33x² + 54x = 3x ⋅ (x - 2) ⋅ h To solve for h, first divide both sides by 3x.

 3x ⋅ (x - 2) ⋅ h

____________ 3x  =  3x⁴ - 3x³ - 33x² + 54x

___________________ 3x 

(x - 2)h = x³ - x² - 11x + 18 Now solve for h using synthetic division.

h =  x³ - x² - 11x + 18

________________ x - 2  -1 -11 2 -18 -9 The quotient is x² + x - 9 and the remainder is 0. The height of the solid is x² + x - 9.

---
### ✏️ **Try It #3**
The area of a rectangle is given by 3x³ + 14x² - 23x + 6. The width of the rectangle is given by x + 6. Find an expression for the length of the rectangle. Access these online resources for additional instruction and practice with polynomial division. • Dividing a Trinomial by a Binomial Using Long Division (http://openstaxcollege.org/l/dividetribild) • Dividing a Polynomial by a Binomial Using Long Division (http://openstaxcollege.org/l/dividepolybild) • Ex 2: Dividing a Polynomial by a Binomial Using Synthetic Division (http://openstaxcollege.org/l/dividepolybisd²) • Ex 4: Dividing a Polynomial by a Binomial Using Synthetic Division (http://openstaxcollege.org/l/dividepolybisd⁴)

### 3.5 section EXERCISES

Verbal 1. If division of a polynomial by a binomial results in a remainder of zero, what can be conclude? 2. If a polynomial of degree n is divided by a binomial of degree 1, what is the degree of the quotient? Algebraic For the following exercises, use long division to divide. Specify the quotient and the remainder. 3. (x² + 5x - 1) \div  (x - 1) 4. (2x² - 9x - 5) \div  (x - 5) 5. (3x² + 23x + 14) \div  (x + 7) 6. (4x² - 10x + 6) \div  (4x + 2) 7. (6x² - 25x - 25) \div  (6x + 5) 8. (-x² - 1) \div  (x + 1) 9. (2x² - 3x + 2) \div  (x + 2) 10. (x³ - 126) \div  (x - 5) 11. (3x² - 5x + 4) \div  (3x + 1) 12. (x³ - 3x² + 5x - 6) \div  (x - 2) 13. (2x³ + 3x² - 4x + 15) \div  (x + 3) For the following exercises, use synthetic division to find the quotient. 14. (3x³ - 2x² + x - 4) \div  (x + 3) 15. (2x³ - 6x² - 7x + 6) \div  (x - 4) 16. (6x³ - 10x² - 7x - 15) \div  (x + 1) 17. (4x³ - 12x² - 5x - 1) \div  (2x + 1) 18. (9x³ - 9x² + 18x + 5) \div  (3x - 1) 19. (3x³ - 2x² + x - 4) \div  (x + 3) 20. (-6x³ + x² - 4) \div  (2x - 3) 21. (2x³ + 7x² - 13x - 3) \div  (2x - 3) 22. (3x³ - 5x² + 2x + 3) \div  (x + 2) 23. (4x³ - 5x² + 13) \div  (x + 4) 24. (x³ - 3x + 2) \div  (x + 2) 27. (9x³ - x + 2) \div  (3x - 1) 28. (6x³ - x² + 5x + 2) \div  (3x + 1) 29. (x⁴ + x³ - 3x² - 2x + 1) \div  (x + 1) 30. (x⁴ - 3x² + 1) \div  (x - 1) 31. (x⁴ + 2x³ - 3x² + 2x + 6) \div  (x + 3) 32. (x⁴ - 10x³ + 37x² - 60x + 36) \div  (x - 2) 33. (x⁴ - 8x³ + 24x² - 32x + 16) \div  (x - 2) 34. (x⁴ + 5x³ - 3x² - 13x + 10) \div  (x + 5) 36. (4x⁴ - 2x³ - 4x + 2) \div  (2x - 1) 37. (4x⁴ + 2x³ - 4x² + 2x + 2) \div  (2x + 1) For the following exercises, use synthetic division to determine whether the first expression is a factor of the second. If it is, indicate the factorization. __ 2 , 2x⁴ - x³ + 2x - 1/3 , 3x⁴ + x³ - 3x + 1 Graphical For the following exercises, use the graph of the third-degree polynomial and one factor to write the factored form of the polynomial suggested by the graph. The leading coefficient is one. 44. Factor is x² - x + 3 x y 45. Factor is x² + 2x + 4 x y 46. Factor is x² + 2x + 5 x y

## 3.5 Section Exercises

---
47. Factor is x² + x + 1 x y 48. Factor is x² + 2x + 2 x y For the following exercises, use synthetic division to find the quotient and remainder. _______ x - 2  _______ x + 3  __________ x - 1 

____________ x + 4  ______ x + 2  Technology For the following exercises, use a calculator with CAS to answer the questions. 54. Consider  xk - 1 ______ x - 1  with k = 1, 2, 3. What do you expect the result to be if k = 4? 55. Consider  xk + 1 ______ x + 1  for k = 1, 3, 5. What do you expect the result to be if k = 7? 56. Consider  x⁴ - k⁴ ______ x - k  for k = 1, 2, 3. What do you expect the result to be if k = 4? 57. Consider  xk _____ x + 1  with k = 1, 2, 3. What do you expect the result to be if k = 4? 58. Consider  xk _____ x - 1  with k = 1, 2, 3. What do you expect the result to be if k = 4? Extensions For the following exercises, use synthetic division to determine the quotient involving a complex number. _____ x - i  _____ x - i  _____ x + i  _____ x + i  _____ x - i  Real-World Applications For the following exercises, use the given length and area of a rectangle to express the width algebraically. 64. Length is x + 5, area is 2x² + 9x - 5. 65. Length is 2x + 5, area is 4x³ + 10x² + 6x + 15 66. Length is 3x - 4, area is 6x⁴ - 8x³ + 9x² - 9x - 4 For the following exercises, use the given volume of a box and its length and width to express the height of the box algebraically. length is 2x + 3, width is 3x - 4. length is 3x - 4, width is 3x - 4. 69. Volume is 10x³ + 27x² + 2x - 24, length is 5x - 4, width is 2x + 3. 70. Volume is 10x³ + 30x² - 8x - 24, length is 2, width is x + 3. For the following exercises, use the given volume and radius of a cylinder to express the height of the cylinder algebraically. 71. Volume is π (25x³ - 65x² - 29x - 3), radius is 5x + 1. 72. Volume is π (4x³ + 12x² - 15x - 50), radius is 2x + 5. 73. Volume is π (3x⁴ + 24x³ + 46x² - 16x - 32), radius is x + 4.

Learning Objectives
In this section, you will:
• Evaluate a polynomial using the Remainder Theorem.
• Use the Factor Theorem to solve a polynomial equation.
• Use the Rational Zero Theorem to find rational zeros.
• Find zeros of a polynomial function.
• Use the Linear Factorization Theorem to find polynomials with given zeros.
• Use Decartes' Rule of Signs.
• Solve real-world applications of polynomial equations.

## 3.6 Zeros of Polynomial Functions

---
A new bakery offers decorated sheet cakes for children’s birthday parties and other special occasions. The bakery wants the volume of a small cake to be 351 cubic inches. The cake is in the shape of a rectangular solid. They want the length of the cake to be four inches longer than the width of the cake and the height of the cake to be one-third of the width. What should the dimensions of the cake pan be? This problem can be solved by writing a cubic function and solving a cubic equation for the volume of the cake. In this section, we will discuss a variety of tools for writing polynomial functions and solving polynomial equations. Evaluating a Polynomial Using the Remainder Theorem In the last section, we learned how to divide polynomials. We can now use polynomial division to evaluate polynomials using the Remainder Theorem. If the polynomial is divided by x - k, the remainder may be found quickly by evaluating the polynomial function at k, that is, f (k) Let’s walk through the proof of the theorem. Recall that the Division Algorithm states that, given a polynomial dividend f (x) and a non-zero polynomial divisor d(x) where the degree of d(x) is less than or equal to the degree of f (x), there exist unique polynomials q(x) and r(x) such that

f (x) = d(x)q(x) + r(x) If the divisor, d(x), is x - k, this takes the form f (x) = (x - k)q(x) + r Since the divisor x - k is linear, the remainder will be a constant, r. And, if we evaluate this for x = k, we have

f (k) = (k - k)q(k) + r

= 0 ⋅ q(k) + r

= r In other words, f (k) is the remainder obtained by dividing f (x) by x - k. the Remainder Theorem If a polynomial f (x) is divided by x - k, then the remainder is the value f (k).

---
### 💡 **How To…**
Given a polynomial function f, evaluate f (x) at x = k using the Remainder Theorem. 1. Use synthetic division to divide the polynomial by x - k. 2. The remainder is the value f (k).

---
### 📐 **Example  1**
Using the Remainder Theorem to Evaluate a Polynomial Use the Remainder Theorem to evaluate f (x) = 6x⁴ - x³ - 15x² + 2x - 7 at x = 2.

**Solution**

To find the remainder using the Remainder Theorem, use synthetic division to divide the polynomial by x - 2. -1 -15 -7 The remainder is 25. Therefore, f (2) = 25. Analysis We can check our answer by evaluating f (2).

f (x) = 6x⁴ - x³ - 15x² + 2x - 7

f (2) = 6(2)⁴ - (2)³ - 15(2)² + 2(2) - 7

= 25

---
### ✏️ **Try It #1**
Use the Remainder Theorem to evaluate f (x) = 2x⁵ - 3x⁴ - 9x³ + 8x² + 2 at x = -3. Using the Factor Theorem to Solve a Polynomial Equation The Factor Theorem is another theorem that helps us analyze polynomial equations. It tells us how the zeros of a polynomial are related to the factors. Recall that the Division Algorithm tells us f (x) = (x - k)q(x) + r. If k is a zero, then the remainder r is f (k) = 0 and f (x) = (x - k)q(x) + 0 or f (x) = (x - k)q(x). Notice, written in this form, x - k is a factor of f (x). We can conclude if k is a zero of f (x), then x - k is a factor of f (x). Similarly, if x - k is a factor of f (x), then the remainder of the Division Algorithm f (x) = (x - k)q(x) + r is 0. This tells us that k is a zero. This pair of implications is the Factor Theorem. As we will soon see, a polynomial of degree n in the complex number system will have n zeros. We can use the Factor Theorem to completely factor a polynomial into the product of n factors. Once the polynomial has been completely factored, we can easily determine the zeros of the polynomial. the Factor Theorem According to the Factor Theorem, k is a zero of f (x) if and only if (x - k) is a factor of f (x).

---
### 💡 **How To…**
Given a factor and a third-degree polynomial, use the Factor Theorem to factor the polynomial. 1. Use synthetic division to divide the polynomial by (x - k). 2. Confirm that the remainder is 0. 3. Write the polynomial as the product of (x - k) and the quadratic quotient. 4. If possible, factor the quadratic. 5. Write the polynomial as the product of factors.

---
### 📐 **Example  2**
Using the Factor Theorem to Solve a Polynomial Equation Show that (x + 2) is a factor of x³ - 6x² - x + 30. Find the remaining factors. Use the factors to determine the zeros of the polynomial.

**Solution**

We can use synthetic division to show that (x + 2) is a factor of the polynomial. -2 -6 -1 -2 -30 -8 The remainder is zero, so (x + 2) is a factor of the polynomial. We can use the Division Algorithm to write the polynomial as the product of the divisor and the quotient: (x + 2)(x² - 8x + 15) We can factor the quadratic factor to write the polynomial as (x + 2)(x - 3)(x - 5) By the Factor Theorem, the zeros of x³ - 6x² - x + 30 are -2, 3, and 5.

---
### ✏️ **Try It #2**
Use the Factor Theorem to find the zeros of f (x) = x³ + 4x² - 4x - 16 given that (x - 2) is a factor of the polynomial. Using the Rational Zero Theorem to Find Rational Zeros Another use for the Remainder Theorem is to test whether a rational number is a zero for a given polynomial. But first we need a pool of rational numbers to test. The Rational Zero Theorem helps us to narrow down the number of possible rational zeros using the ratio of the factors of the constant term and factors of the leading coefficient of the polynomial. Consider a quadratic function with two zeros, x =  2/5  and x =  3/4 . By the Factor Theorem, these zeros have factors associated with them. Let us set each factor equal to 0, and then construct the original quadratic function absent its stretching factor.

x -  2/5  = 0 or x -  3/4  = 0 Set each factor equal to 0.

5x - 2 = 0 or 4x - 3 = 0 Multiply both sides of the equation to eliminate fractions.

f (x) = (5x - 2)(4x - 3) Create the quadratic function, multiplying the factors.

f (x) = 20x² - 23x + 6 Expand the polynomial.

f (x) = (5 ⋅ 4)x² - 23x + (2 ⋅ 3) Notice that two of the factors of the constant term, 6, are the two numerators from the original rational roots: 2 and 3. Similarly, two of the factors from the leading coefficient, 20, are the two denominators from the original rational roots: 5 and 4. We can infer that the numerators of the rational roots will always be factors of the constant term and the denominators will be factors of the leading coefficient. This is the essence of the Rational Zero Theorem; it is a means to give us a pool of possible rational zeros. the Rational Zero Theorem The Rational Zero Theorem states that, if the polynomial f (x) = anxn + an - 1 xn - 1 + ... + a¹ x + a⁰ has integer coefficients, then every rational zero of f (x) has the form  (p)/(q)  where p is a factor of the constant term a⁰ and q is a factor of the leading coefficient an. When the leading coefficient is 1, the possible rational zeros are the factors of the constant term.

---
### 💡 **How To…**
Given a polynomial function f (x), use the Rational Zero Theorem to find rational zeros. 1. Determine all factors of the constant term and all factors of the leading coefficient. 2. Determine all possible values of  (p)/(q) , where p is a factor of the constant term and q is a factor of the leading coefficient. Be sure to include both positive and negative candidates. 3. Determine which possible zeros are actual zeros by evaluating each case of f (  (p)/(q)  ).

---
### 📐 **Example  3**
Listing All Possible Rational Zeros List all possible rational zeros of f (x) = 2x⁴ - 5x³ + x² - 4.

**Solution**

The only possible rational zeros of f (x) are the quotients of the factors of the last term, -4, and the factors of the leading coefficient, 2. The constant term is -4; the factors of -4 are p = ± 1, ± 2, ± 4. The leading coefficient is 2; the factors of 2 are q = ± 1, ± 2. If any of the four real zeros are rational zeros, then they will be of one of the following factors of -4 divided by one of the factors of 2.

 (p)/(q)  = ±  1/1 , ±  1/2   (p)/(q)  = ±  2/1 , ±  2/2   (p)/(q)  = ±  4/1 , ±  4/2  Note that  2/2  = 1 and  4/2  = 2, which have already been listed. So we can shorten our list.

 (p)/(q)  =  Factors of the las(t)/(F)actors of the first  = ± 1, ± 2, ± 4, ±  1/2 

---
### 📐 **Example  4**
Using the Rational Zero Theorem to Find Rational Zeros Use the Rational Zero Theorem to find the rational zeros of f (x) = 2x³ + x² - 4x + 1.

**Solution**

The Rational Zero Theorem tells us that if  (p)/(q)  is a zero of f (x), then p is a factor of 1 and q is a factor of 2.

 (p)/(q)  =  factor of constant term

___

factor of leading coefficient 

=  factor of 1/factor of 2  The factors of 1 are ± 1 and the factors of 2 are ± 1 and ± 2. The possible values for  (p)/(q)  are ± 1 and ±  1/2 . These are the possible rational zeros for the function. We can determine which of the possible zeros are actual zeros by substituting these values for x in f (x).

f (-1) = 2(-1)³ + (-1)² - 4(-1) + 1 = 4

f (1) = 2(1)³ + (1)² - 4(1) + 1 = 0

f ( - 1/2  ) = 2 ( - 1/2  ) + ( - 1/2  ) - 4 ( - 1/2  ) + 1 = 3

f (  1/2  ) = 2 (  1/2  ) + (  1/2  ) 2 - 4 (  1/2  ) + 1 = - 1/2  Of those, -1, - 1/2 , and  1/2  are not zeros of f (x). 1 is the only rational zero of f (x).

---
### ✏️ **Try It #3**
Use the Rational Zero Theorem to find the rational zeros of f (x) = x³ - 5x² + 2x + 1.

Finding the Zeros of Polynomial Functions The Rational Zero Theorem helps us to narrow down the list of possible rational zeros for a polynomial function. Once we have done this, we can use synthetic division repeatedly to determine all of the zeros of a polynomial function.

---
### 💡 **How To…**
Given a polynomial function f, use synthetic division to find its zeros. 1. Use the Rational Zero Theorem to list all possible rational zeros of the function. 2. Use synthetic division to evaluate a given possible zero by synthetically dividing the candidate into the polynomial. If the remainder is 0, the candidate is a zero. If the remainder is not zero, discard the candidate. 3. Repeat step two using the quotient found with synthetic division. If possible, continue until the quotient is a quadratic. 4. Find the zeros of the quadratic function. Two possible methods for solving quadratics are factoring and using the quadratic formula.

---
### 📐 **Example  5**
Finding the Zeros of a Polynomial Function with Repeated Real Zeros Find the zeros of f (x) = 4x³ - 3x - 1.

**Solution**

The Rational Zero Theorem tells us that if  (p)/(q)  is a zero of f (x), then p is a factor of -1 and q is a factor of 4.

 (p)/(q)  =  factor of constant term

___

factor of leading coefficient 

=  factor of -1/factor of 4  The factors of -1 are ± 1 and the factors of 4 are ± 1, ± 2, and ± 4. The possible values for  (p)/(q)  are ± 1, ±  1/2 , and ±  1/4 . These are the possible rational zeros for the function. We will use synthetic division to evaluate each possible zero until we find one that gives a remainder of 0. Let’s begin with 1. -3 -1 Dividing by (x - 1) gives a remainder of 0, so 1 is a zero of the function. The polynomial can be written as (x - 1)(4x² + 4x + 1). The quadratic is a perfect square. f (x) can be written as (x - 1)(2x + 1)². We already know that 1 is a zero. The other zero will have a multiplicity of 2 because the factor is squared. To find the other zero, we can set the factor equal to 0.

2x + 1 = 0

x = - 1/2  The zeros of the function are 1 and - 1/2  with multiplicity 2.

**Analysis**
Look at the graph of the function f in Figure 1. Notice, at x = -0.5, the graph bounces off the x-axis, indicating the even multiplicity (2, 4, 6...) for the zero -0.5. At x = 1, the graph crosses the x-axis, indicating the odd multiplicity (1, 3, 5...) for the zero x = 1. x y 1.5 0.5 0.5 1.5 2.5 Cross Bounce

Using the Fundamental Theorem of Algebra Now that we can find rational zeros for a polynomial function, we will look at a theorem that discusses the number of complex zeros of a polynomial function. The Fundamental Theorem of Algebra tells us that every polynomial function has at least one complex zero. This theorem forms the foundation for solving polynomial equations. Suppose f is a polynomial function of degree four, and f (x) = 0. The Fundamental Theorem of Algebra states that there is at least one complex solution, call it c¹. By the Factor Theorem, we can write f (x) as a product of x - c¹ and a polynomial quotient. Since x - c¹ is linear, the polynomial quotient will be of degree three. Now we apply the Fundamental Theorem of Algebra to the third-degree polynomial quotient. It will have at least one complex zero, call it c². So we can write the polynomial quotient as a product of x - c² and a new polynomial quotient of degree two. Continue to apply the Fundamental Theorem of Algebra until all of the zeros are found. There will be four of them and each one will yield a factor of f (x). The Fundamental Theorem of Algebra The Fundamental Theorem of Algebra states that, if f (x) is a polynomial of degree n > 0, then f (x) has at least one complex zero. We can use this theorem to argue that, if f (x) is a polynomial of degree n > 0, and a is a non-zero real number, then f (x) has exactly n linear factors f (x) = a(x - c¹)(x - c²)...(x - cn) where c¹, c², ..., cn are complex numbers. Therefore, f (x) has n roots if we allow for multiplicities. Does every polynomial have at least one imaginary zero? No. A complex number is not necessarily imaginary. Real numbers are also complex numbers.

---
### 📐 **Example  6**
Finding the Zeros of a Polynomial Function with Complex Zeros Find the zeros of f (x) = 3x³ + 9x² + x + 3.

**Solution**

The Rational Zero Theorem tells us that if  (p)/(q)  is a zero of f (x), then p is a factor of 3 and q is a factor of 3.

 (p)/(q)  =  factor of constant term

___

factor of leading coefficient 

=  factor of 3/factor of 3  The factors of 3 are ± 1 and ± 3. The possible values for  (p)/(q) , and therefore the possible rational zeros for the function, are ± 3, ± 1, and ±  1/3 . We will use synthetic division to evaluate each possible zero until we find one that gives a remainder of 0. Let’s begin with -3. -3 -9 -3 Dividing by (x + 3) gives a remainder of 0, so -3 is a zero of the function. The polynomial can be written as (x + 3)(3x² + 1) We can then set the quadratic equal to 0 and solve to find the other zeros of the function.

x² = - 1/3 

x = ± √____

- 1/3   = ±  i√3  _ 3  The zeros of f (x) are -3 and ±  i√3  _ 3 .

Analysis Look at the graph of the function f in Figure 2. Notice that, at x = -3, the graph crosses the x-axis, indicating an odd multiplicity (1) for the zero x = -3. Also note the presence of the two turning points. This means that, since there is a 3rd degree polynomial, we are looking at the maximum number of turning points. So, the end behavior of increasing without bound to the right and decreasing without bound to the left will continue. Thus, all the x-intercepts for the function are shown. So either the multiplicity of x = -3 is 1 and there are two complex solutions, which is what we found, or the multiplicity at x = -3 is three. Either way, our result is correct. x y Cross

---
### ✏️ **Try It #4**
Find the zeros of f (x) = 2x³ + 5x² - 11x + 4. Using the Linear Factorization Theorem to Find Polynomials with Given Zeros A vital implication of the Fundamental Theorem of Algebra, as we stated above, is that a polynomial function of degree n will have n zeros in the set of complex numbers, if we allow for multiplicities. This means that we can factor the polynomial function into n factors. The Linear Factorization Theorem tells us that a polynomial function will have the same number of factors as its degree, and that each factor will be in the form (x - c), where c is a complex number. Let f be a polynomial function with real coefficients, and suppose a + bi, b ≠  0, is a zero of f (x). Then, by the Factor Theorem, x - (a + bi) is a factor of f (x). For f to have real coefficients, x - (a - bi) must also be a factor of f (x). This is true because any factor other than x - (a - bi), when multiplied by x - (a + bi), will leave imaginary components in the product. Only multiplication with conjugate pairs will eliminate the imaginary parts and result in real coefficients. In other words, if a polynomial function f with real coefficients has a complex zero a + bi, then the complex conjugate a - bi must also be a zero of f (x). This is called the Complex Conjugate Theorem. complex conjugate theorem According to the Linear Factorization Theorem, a polynomial function will have the same number of factors as its degree, and each factor will be in the form (x - c), where c is a complex number. If the polynomial function f has real coefficients and a complex zero in the form a + bi, then the complex conjugate of the zero, a - bi, is also a zero.

---
### 💡 **How To…**
Given the zeros of a polynomial function f and a point (c, f (c)) on the graph of f, use the Linear Factorization Theorem to find the polynomial function. 1. Use the zeros to construct the linear factors of the polynomial. 2. Multiply the linear factors to expand the polynomial. 3. Substitute (c, f (c)) into the function to determine the leading coefficient. 4. Simplify.

---
### 📐 **Example  7**
Using the Linear Factorization Theorem to Find a Polynomial with Given Zeros Find a fourth degree polynomial with real coefficients that has zeros of -3, 2, i, such that f (-2) = 100.

**Solution**

Because x = i is a zero, by the Complex Conjugate Theorem x = -i is also a zero. The polynomial must have factors of (x + 3), (x - 2), (x - i), and (x + i). Since we are looking for a degree 4 polynomial, and now have four zeros, we have all four factors. Let’s begin by multiplying these factors.

f (x) = a(x + 3)(x - 2)(x - i)(x + i)

f (x) = a(x² + x - 6)(x² + 1)

f (x) = a(x⁴ + x³ - 5x² + x - 6) We need to find a to ensure f (-2) = 100. Substitute x = -2 and f (2) = 100 into f (x).

100 = a((-2)⁴ + (-2)³ - 5(-2)² + (-2) - 6)

-5 = a So the polynomial function is

f (x) = -5(x⁴ + x³ - 5x² + x - 6) or

f (x) = -5x⁴ - 5x³ + 25x² - 5x + 30 Analysis We found that both i and -i were zeros, but only one of these zeros needed to be given. If i is a zero of a polynomial with real coefficients, then -i must also be a zero of the polynomial because -i is the complex conjugate of i. If 2 + 3i were given as a zero of a polynomial with real coefficients, would 2 - 3i also need to be a zero? Yes. When any complex number with an imaginary component is given as a zero of a polynomial with real coefficients, the conjugate must also be a zero of the polynomial.

---
### ✏️ **Try It #5**
Find a third degree polynomial with real coefficients that has zeros of 5 and -2i such that f (1) = 10. Using Descartes’ Rule of Signs There is a straightforward way to determine the possible numbers of positive and negative real zeros for any polynomial function. If the polynomial is written in descending order, Descartes’ Rule of Signs tells us of a relationship between the number of sign changes in f (x) and the number of positive real zeros. For example, the polynomial function below has one sign change.

f (x) = x 4 + x 3 + x 2 + x - 1 This tells us that the function must have 1 positive real zero. There is a similar relationship between the number of sign changes in f (-x) and the number of negative real zeros.

f (-x) = (-x)⁴ + (-x)³ + (-x)² + (-x) - 1

f (-x) =+x 4 - x 3 + x 2 - x - 1 In this case, f (-x) has 3 sign changes. This tells us that f (x) could have 3 or 1 negative real zeros.

Descartes’ Rule of Signs According to Descartes’ Rule of Signs, if we let f (x) = anxn + an - 1 xn - 1 + ... + a¹ x + a⁰ be a polynomial function with real coefficients: • The number of positive real zeros is either equal to the number of sign changes of f (x) or is less than the number of sign changes by an even integer. • The number of negative real zeros is either equal to the number of sign changes of f (-x) or is less than the number of sign changes by an even integer.

---
### 📐 **Example  8**
Using Descartes’ Rule of Signs Use Descartes’ Rule of Signs to determine the possible numbers of positive and negative real zeros for f (x) = -x⁴ - 3x³ + 6x² - 4x - 12.

**Solution**

Begin by determining the number of sign changes.

f (x) = -x 4 - 3x 3 + 6x 2 - 4x - 12 There are two sign changes, so there are either 2 or 0 positive real roots. Next, we examine f (-x) to determine the number of negative real roots.

f (-x) = -(-x)⁴ - 3(-x)³ + 6(-x)² - 4(-x) - 12

f (-x) = -x 4 + 3x 3 + 6x 2 + 4x - 12

f (-x) = -x 4 + 3x 3 + 6x 2 + 4x - 12 Again, there are two sign changes, so there are either 2 or 0 negative real roots. There are four possibilities, as we can see in Table 1. Positive Real Zeros Negative Real Zeros Complex Zeros Total Zeros Analysis We can confirm the numbers of positive and negative real roots by examining a graph of the function. See positive real roots and 2 negative real roots. x = -1 x y f(x) = - x⁴ - 3x³ + 6x² - 4x - 12

---
### ✏️ **Try It #6**
Use Descartes’ Rule of Signs to determine the maximum possible numbers of positive and negative real zeros for f (x) = 2x⁴ - 10x³ + 11x² - 15x + 12. Use a graph to verify the numbers of positive and negative real zeros for the function. Solving Real-World Applications We have now introduced a variety of tools for solving polynomial equations. Let’s use these tools to solve the bakery problem from the beginning of the section.

---
### 📐 **Example  9**: Solving Polynomial Equations

A new bakery offers decorated sheet cakes for children’s birthday parties and other special occasions. The bakery wants the volume of a small cake to be 351 cubic inches. The cake is in the shape of a rectangular solid. They want the length of the cake to be four inches longer than the width of the cake and the height of the cake to be one-third of the width. What should the dimensions of the cake pan be?

**Solution**

Begin by writing an equation for the volume of the cake. The volume of a rectangular solid is given by V = lwh. We were given that the length must be four inches longer than the width, so we can express the length of the cake as l = w + 4. We were given that the height of the cake is one-third of the width, so we can express the height of the cake as h =  1/3 w. Let’s write the volume of the cake in terms of width of the cake.

V = (w + 4)(w)(  1/3 w )

V =  1/3 w 3 +  4/3 w 2 Substitute the given volume into this equation.

__ 3 w 3 +  4/3 w 2 Substitute 351 for V.

Multiply both sides by 3.

Subtract 1053 from both sides. Descartes’ rule of signs tells us there is one positive solution. The Rational Zero Theorem tells us that the possible rational zeros are ± 1, ± 3, ± 9, ± 13, ± 27, ± 39, ± 81, ± 117, ± 351, and ± 1053. We can use synthetic division to test these possible zeros. Only positive numbers make sense as dimensions for a cake, so we need not test any negative values. Let’s begin by testing values that make the most sense as dimensions for a small sheet cake. Use synthetic division to check x = 1. -1053

-1048 Since 1 is not a solution, we will check x = 3. -1053

-990 Since 3 is not a solution either, we will test x = 9. Synthetic division gives a remainder of 0, so 9 is a solution to the equation. We can use the relationships between the width and the other dimensions to determine the length and height of the sheet cake pan. l = w + 4 = 9 + 4 = 13 and h =  1/3 w =  1/3 (9) = 3 The sheet cake pan should have dimensions 13 inches by 9 inches by 3 inches.

---
### ✏️ **Try It #7**
A shipping container in the shape of a rectangular solid must have a volume of 84 cubic meters. The client tells the manufacturer that, because of the contents, the length of the container must be one meter longer than the width, and the height must be one meter greater than twice the width. What should the dimensions of the container be? Access these online resources for additional instruction and practice with zeros of polynomial functions. • Real Zeros, Factors, and Graphs of Polynomial Functions (http://openstaxcollege.org/l/realzeros) • Complex Factorization Theorem (http://openstaxcollege.org/l/factortheorem) • Find the Zeros of a Polynomial Function (http://openstaxcollege.org/l/findthezeros) • Find the Zeros of a Polynomial Function 2 (http://openstaxcollege.org/l/findthezeros²) • Find the Zeros of a Polynomial Function 3 (http://openstaxcollege.org/l/findthezeros³)

### 3.6 section EXERCISES

Verbal 1. Describe a use for the Remainder Theorem. 2. Explain why the Rational Zero Theorem does not guarantee finding zeros of a polynomial function. 3. What is the difference between rational and real zeros? 4. If Descartes’ Rule of Signs reveals a no change of signs or one sign of changes, what specific conclusion can be drawn? 5. If synthetic division reveals a zero, why should we try that value again as a possible solution? Algebraic For the following exercises, use the Remainder Theorem to find the remainder. 6. (x⁴ - 9x² + 14) \div  (x - 2) 7. (3x³ - 2x² + x - 4) \div  (x + 3) 8. (x⁴ + 5x³ - 4x - 17) \div  (x + 1) 9. (-3x² + 6x + 24) \div  (x - 4) 10. (5x⁵ - 4x⁴ + 3x³ - 2x² + x - 1) \div  (x + 6) 11. (x⁴ - 1) \div  (x - 4) 12. (3x³ + 4x² - 8x + 2) \div  (x - 3) 13. (4x³ + 5x² - 2x + 7) \div  (x + 2) For the following exercises, use the Factor Theorem to find all real zeros for the given polynomial function and one factor. 14. f (x) = 2x³ - 9x² + 13x - 6; x - 1 15. f (x) = 2x³ + x² - 5x + 2; x + 2 16. f (x) = 3x³ + x² - 20x + 12; x + 3 17. f (x) = 2x³ + 3x² + x + 6; x + 2 18. f (x) = -5x³ + 16x² - 9; x - 3 19. x³ + 3x² + 4x + 12; x + 3 20. 4x³ - 7x + 3; x - 1 For the following exercises, use the Rational Zero Theorem to find all real zeros. For the following exercises, find all complex solutions (real and non-real). 40. x³ + x² + x + 1 = 0 Graphical For the following exercises, use Descartes’ Rule to determine the possible number of positive and negative solutions. Then graph to confirm which of those possibilities is the actual combination. 46. f (x) = x³ - 1 47. f (x) = x⁴ - x² - 1 48. f (x) = x³ - 2x² - 5x + 6 49. f (x) = x³ - 2x² + x - 1 50. f (x) = x⁴ + 2x³ - 12x² + 14x - 5

## 3.6 Section Exercises

---
52. f (x) = x³ - 2x² - 16x + 32 53. f (x) = 2x⁴ - 5x³ - 5x² + 5x + 3 54. f (x) = 2x⁴ - 5x³ - 14x² + 20x + 8 Numeric For the following exercises, list all possible rational zeros for the functions. 56. f (x) = x⁴ + 3x³ - 4x + 4 57. f (x) = 2x³ + 3x² - 8x + 5 58. f (x) = 3x³ + 5x² - 5x + 4 59. f (x) = 6x⁴ - 10x² + 13x + 1 60. f (x) = 4x⁵ - 10x⁴ + 8x³ + x² - 8 Technology For the following exercises, use your calculator to graph the polynomial function. Based on the graph, find the rational zeros. All real solutions are rational. 61. f (x) = 6x³ - 7x² + 1 62. f (x) = 4x³ - 4x² - 13x - 5 63. f (x) = 8x³ - 6x² - 23x + 6 65. f (x) = 16x⁴ - 24x³ + x² - 15x + 25 Extensions For the following exercises, construct a polynomial function of least degree possible using the given information. 66. Real roots: -1, 1, 3 and (2, f (2)) = (2, 4) 67. Real roots: -1, 1 (with multiplicity 2 and 1) and (2, f (2)) = (2, 4) 68. Real roots: -2,  1/2  (with multiplicity 2) and (-3, f (-3)) = (-3, 5) 69. Real roots: - 1/2  and (-2, f (-2)) = (-2, 6) 70. Real roots: -4, -1, 1, 4 and (-2, f (-2)) = (-2, 10) Real-World Applications For the following exercises, find the dimensions of the box described. 71. The length is twice as long as the width. The height is 2 inches greater than the width. The volume is 192 cubic inches. 72. The length, width, and height are consecutive whole numbers. The volume is 120 cubic inches. 73. The length is one inch more than the width, which is one inch more than the height. The volume is 86.625 cubic inches. 74. The length is three times the height and the height is one inch less than the width. The volume is 108 cubic inches. 75. The length is 3 inches more than the width. The width is 2 inches more than the height. The volume is 120 cubic inches. For the following exercises, find the dimensions of the right circular cylinder described. 76. The radius is 3 inches more than the height. The volume is 16π  cubic meters. 77. The height is one less than one half the radius. The volume is 72π  cubic meters. 78. The radius and height differ by one meter. The radius is larger and the volume is 48π  cubic meters. 79. The radius and height differ by two meters. The height is greater and the volume is 28.125π  cubic meters. 80. The radius is  1/3  meter greater than the height. The volume is  98 ___ 9π  π  cubic meters.

Learning Objectives
In this section, you will:
• Use arrow notation.
• Solve applied problems involving rational functions.
• Find the domains of rational functions.
• Identify vertical asymptotes.
• Identify horizontal asymptotes.
• Graph rational functions.

## 3.7 Rational Functions

---
Suppose we know that the cost of making a product is dependent on the number of items, x, produced. This is given by the equation C(x) = 15,000x - 0.1x² + 1000. If we want to know the average cost for producing x items, we would divide the cost function by the number of items, x. The average cost function, which yields the average cost per item for x items produced, is

__________________

x  Many other application problems require finding an average value in a similar way, giving us variables in the denominator. Written without a variable in the denominator, this function will contain a negative integer power. In the last few sections, we have worked with polynomial functions, which are functions with non-negative integers for exponents. In this section, we explore rational functions, which have variables in the denominator. Using Arrow Notation We have seen the graphs of the basic reciprocal function and the squared reciprocal function from our study of toolkit functions. Examine these graphs, as shown in Figure 1, and notice some of their features. Graphs of Toolkit Functions x y y f (x) = x x f (x) = x²1 Several things are apparent if we examine the graph of f (x) =  1/x . 1. On the left branch of the graph, the curve approaches the x-axis (y = 0) as x → -∞ . 2. As the graph approaches x = 0 from the left, the curve drops, but as we approach zero from the right, the curve rises. 3. Finally, on the right branch of the graph, the curves approaches the x-axis (y = 0) as x → ∞ . To summarize, we use arrow notation to show that x or f (x) is approaching a particular value. See Table 1.

Symbol Meaning x → a- x approaches a from the left (x < a but close to a) x → a+ x approaches a from the right (x > a but close to a) x → ∞  x approaches infinity (x increases without bound) x → -∞  x approaches negative infinity (x decreases without bound) f (x) → ∞  The output approaches infinity (the output increases without bound) f (x) → -∞  The output approaches negative infinity (the output decreases without bound) f (x) → a The output approaches a Local Behavior of f (x ) =  1/x  Let’s begin by looking at the reciprocal function, f (x) =  1/x . We cannot divide by zero, which means the function is undefined at x = 0; so zero is not in the domain. As the input values approach zero from the left side (becoming very small, negative values), the function values decrease without bound (in other words, they approach negative infinity). We can see this behavior in Table 2. x -0.1 -0.01 f (x) =  1/x  -10 -100 -1000 We write in arrow notation as x → 0-, f (x) → -∞  As the input values approach zero from the right side (becoming very small, positive values), the function values increase without bound (approaching infinity). We can see this behavior in Table 3. x 0.1 0.01 0.001 f (x) =  1/x  We write in arrow notation As x → 0+, f (x) → ∞ . See Figure 2. x y f (x) → ∞  As x → 0+ f (x) → 0 As x → ∞  f (x) → -∞  As x → 0– f (x) → 0 As x → -∞ 

This behavior creates a vertical asymptote, which is a vertical line that the graph approaches but never crosses. In this case, the graph is approaching the vertical line x = 0 as the input becomes close to zero. See Figure 3. x y x = 0 vertical asymptote A vertical asymptote of a graph is a vertical line x = a where the graph tends toward positive or negative infinity as the inputs approach a. We write As x → a, f (x) → ∞ , or as x → a, f (x) → -∞ . End Behavior of f (x ) =  1/x  As the values of x approach infinity, the function values approach 0. As the values of x approach negative infinity, the function values approach 0. See Figure 4. Symbolically, using arrow notation As x → ∞ , f (x) → 0, and as x → -∞ , f (x) → 0. x y f (x) → ∞  As x → 0+ f (x) → 0 As x → ∞  f (x) → -∞  As x → 0– f (x) → 0 As x → -∞  Based on this overall behavior and the graph, we can see that the function approaches 0 but never actually reaches 0; it seems to level off as the inputs become large. This behavior creates a horizontal asymptote, a horizontal line that the graph approaches as the input increases or decreases without bound. In this case, the graph is approaching the horizontal line y = 0. See Figure 5. x y x = 0 y = 0

horizontal asymptote A horizontal asymptote of a graph is a horizontal line y = b where the graph approaches the line as the inputs increase or decrease without bound. We write As x → ∞  or x → -∞ , f (x) → b.

---
### 📐 **Example  1**: Using Arrow Notation

Use arrow notation to describe the end behavior and local behavior of the function graphed in Figure 6. x y

**Solution**

Notice that the graph is showing a vertical asymptote at x = 2, which tells us that the function is undefined at x = 2. As x → 2-, f (x) → -∞ , and as x → 2+, f (x) → ∞ . And as the inputs decrease without bound, the graph appears to be leveling off at output values of 4, indicating a horizontal asymptote at y = 4. As the inputs increase without bound, the graph levels off at 4. As x → ∞ , f (x) → 4 and as x → -∞ , f (x) → 4.

---
### ✏️ **Try It #1**
Use arrow notation to describe the end behavior and local behavior for the reciprocal squared function.

---
### 📐 **Example  2**
Using Transformations to Graph a Rational Function Sketch a graph of the reciprocal function shifted two units to the left and up three units. Identify the horizontal and vertical asymptotes of the graph, if any.

**Solution**

Shifting the graph left 2 and up 3 would result in the function f (x) =  1 _____ x + 2  + 3 or equivalently, by giving the terms a common denominator,

f (x) =  3x + 7 ______ x + 2  The graph of the shifted function is displayed in Figure 7. y x = -2 x y = 3

Notice that this function is undefined at x = -2, and the graph also is showing a vertical asymptote at x = -2. As x → -2-, f (x) → -∞ , and as x → -2+, f (x) → ∞ . As the inputs increase and decrease without bound, the graph appears to be leveling off at output values of 3, indicating a horizontal asymptote at y = 3. As x → ± ∞ , f (x) → 3. Analysis Notice that horizontal and vertical asymptotes are shifted left 2 and up 3 along with the function.

---
### ✏️ **Try It #2**
Sketch the graph, and find the horizontal and vertical asymptotes of the reciprocal squared function that has been shifted right 3 units and down 4 units. Solving Applied Problems Involving Rational Functions In Example 2, we shifted a toolkit function in a way that resulted in the function f (x) =  3x + 7 ______ x + 2 . This is an example of a rational function. A rational function is a function that can be written as the quotient of two polynomial functions. Many real-world problems require us to find the ratio of two polynomial functions. Problems involving rates and concentrations often involve rational functions. rational function A rational function is a function that can be written as the quotient of two polynomial functions P(x) and Q(x). f (x) =  P(x) ____ Q(x)  =  ap x p + ap - 1 x p - 1 + ... + a¹ x + a⁰

___

bq x q + bq - 1 x q - 1 + ... + b¹ x + b⁰  , Q(x) ≠  0

---
### 📐 **Example  3**: Solving an Applied Problem Involving a Rational Function

A large mixing tank currently contains 100 gallons of water into which 5 pounds of sugar have been mixed. A tap will open pouring 10 gallons per minute of water into the tank at the same time sugar is poured into the tank at a rate of 1 pound per minute. Find the concentration (pounds per gallon) of sugar in the tank after 12 minutes. Is that a greater concentration than at the beginning?

**Solution**

Let t be the number of minutes since the tap opened. Since the water increases at 10 gallons per minute, and the sugar increases at 1 pound per minute, these are constant rates of change. This tells us the amount of water in the tank is changing linearly, as is the amount of sugar in the tank. We can write an equation independently for each:

water: W(t) = 100 + 10t in gallons

sugar: S(t) = 5 + 1t in pounds The concentration, C, will be the ratio of pounds of sugar to gallons of water

C(t) =  5 + t ________ The concentration after 12 minutes is given by evaluating C(t) at t = 12. C(12) =  __________

=  17 ___ 220  This means the concentration is 17 pounds of sugar to 220 gallons of water. At the beginning, the concentration is C(0) =  5 + 0 _________

=  1/20  Since  17 ___ __ 20  = 0.05, the concentration is greater after 12 minutes than at the beginning.

Analysis To find the horizontal asymptote, divide the leading coefficient in the numerator by the leading coefficient in the denominator:

 1/Notice the horizontal asymptote is y = 0.1. This means the concentration, C, the ratio of pounds of sugar to gallons of water, will approach 0.1 in the long term.

---
### ✏️ **Try It #3**
There are 1,200 freshmen and 1,500 sophomores at a prep rally at noon. After 12 p.m., 20 freshmen arrive at the rally every five minutes while 15 sophomores leave the rally. Find the ratio of freshmen to sophomores at 1 p.m. Finding the Domains of Rational Functions A vertical asymptote represents a value at which a rational function is undefined, so that value is not in the domain of the function. A reciprocal function cannot have values in its domain that cause the denominator to equal zero. In general, to find the domain of a rational function, we need to determine which inputs would cause division by zero. domain of a rational function The domain of a rational function includes all real numbers except those that cause the denominator to equal zero.

---
### 💡 **How To…**
Given a rational function, find the domain. 1. Set the denominator equal to zero. 2. Solve to find the x-values that cause the denominator to equal zero. 3. The domain is all real numbers except those found in Step 2.

---
### 📐 **Example  4**: Finding the Domain of a Rational Function

Find the domain of f (x) =  x + 3/x² - 9 .

**Solution**

Begin by setting the denominator equal to zero and solving.

x² - 9 = 0

x² = 9

x = ± 3 The denominator is equal to zero when x = ± 3. The domain of the function is all real numbers except x = ± 3. Analysis A graph of this function, as shown in Figure 8, confirms that the function is not defined when x = ± 3. x = 3 y x y = 0 There is a vertical asymptote at x = 3 and a hole in the graph at x = -3. We will discuss these types of holes in greater detail later in this section.

---
### ✏️ **Try It #4**
Find the domain of f (x) =  4x _____________

5(x - 1)(x - 5) . Identifying Vertical Asymptotes of Rational Functions By looking at the graph of a rational function, we can investigate its local behavior and easily see whether there are asymptotes. We may even be able to approximate their location. Even without the graph, however, we can still determine whether a given rational function has any asymptotes, and calculate their location. Vertical Asymptotes The vertical asymptotes of a rational function may be found by examining the factors of the denominator that are not common to the factors in the numerator. Vertical asymptotes occur at the zeros of such factors.

---
### 💡 **How To…**
Given a rational function, identify any vertical asymptotes of its graph. 1. Factor the numerator and denominator. 2. Note any restrictions in the domain of the function. 3. Reduce the expression by canceling common factors in the numerator and the denominator. 4. Note any values that cause the denominator to be zero in this simplified version. These are where the vertical asymptotes occur. 5. Note any restrictions in the domain where asymptotes do not occur. These are removable discontinuities.

---
### 📐 **Example  5**: Identifying Vertical Asymptotes

Find the vertical asymptotes of the graph of k(x) =  5 + 2x² _________ 2 - x - x² .

**Solution**

First, factor the numerator and denominator. k(x) =  5 + 2x² ________ 2 - x - x² 

=  ___________

(2 + x)(1 - x)  To find the vertical asymptotes, we determine where this function will be undefined by setting the denominator equal to zero:

(2 + x)(1 - x) = 0

x = -2, 1 Neither x = -2 nor x = 1 are zeros of the numerator, so the two values indicate two vertical asymptotes. The graph in Figure 9 confirms the location of the two vertical asymptotes. x y y = -2 x = 1 x = -2

Removable Discontinuities Occasionally, a graph will contain a hole: a single point where the graph is not defined, indicated by an open circle. We call such a hole a removable discontinuity. For example, the function f (x) =  x² - 1 __________ x² - 2x - 3  may be re-written by factoring the numerator and the denominator. f (x) =  (x + 1)(x - 1)

____________

(x + 1)(x - 3)  Notice that x + 1 is a common factor to the numerator and the denominator. The zero of this factor, x = -1, is the location of the removable discontinuity. Notice also that x - 3 is not a factor in both the numerator and denominator. The zero of this factor, x = 3, is the vertical asymptote. See Figure 10. x y Vertical asymptote at x = 3 Removable discontinuity at x = -1 removable discontinuities of rational functions A removable discontinuity occurs in the graph of a rational function at x = a if a is a zero for a factor in the denominator that is common with a factor in the numerator. We factor the numerator and denominator and check for common factors. If we find any, we set the common factor equal to 0 and solve. This is the location of the removable discontinuity. This is true if the multiplicity of this factor is greater than or equal to that in the denominator. If the multiplicity of this factor is greater in the denominator, then there is still an asymptote at that value.

---
### 📐 **Example  6**: Identifying Vertical Asymptotes and Removable Discontinuities for a Graph

Find the vertical asymptotes and removable discontinuities of the graph of k(x) =  x - 2 _____ x² - 4 .

**Solution**

Factor the numerator and the denominator. k(x) =  x - 2 ___________

(x - 2)(x + 2)  Notice that there is a common factor in the numerator and the denominator, x - 2. The zero for this factor is x = 2. This is the location of the removable discontinuity. Notice that there is a factor in the denominator that is not in the numerator, x + 2. The zero for this factor is x = -2. The vertical asymptote is x = -2. See Figure 11.

x y x = -2 The graph of this function will have the vertical asymptote at x = -2, but at x = 2 the graph will have a hole.

---
### ✏️ **Try It #5**
Find the vertical asymptotes and removable discontinuities of the graph of f (x) =  ___________ x³ - 6x² + 5x . Identifying Horizontal Asymptotes of Rational Functions While vertical asymptotes describe the behavior of a graph as the output gets very large or very small, horizontal asymptotes help describe the behavior of a graph as the input gets very large or very small. Recall that a polynomial’s end behavior will mirror that of the leading term. Likewise, a rational function’s end behavior will mirror that of the ratio of the leading terms of the numerator and denominator functions. There are three distinct outcomes when checking for horizontal asymptotes: Case 1: If the degree of the denominator > degree of the numerator, there is a horizontal asymptote at y = 0. Example: f (x) =  4x + 2 _________ x² + 4x - 5  In this case, the end behavior is f (x) ≈  4(x)/(x)²  =  4/x . This tells us that, as the inputs increase or decrease without bound, this function will behave similarly to the function g(x) =  4/x , and the outputs will approach zero, resulting in a horizontal asymptote at y = 0. See Figure 12. Note that this graph crosses the horizontal asymptote. x y x = 1 x = -5 y = 0 ____ q(x ) , q(x ) ≠  0 where degree of p < degree of q. Case 2: If the degree of the denominator < degree of the numerator by one, we get a slant asymptote. Example: f (x) =  3x² - 2x + 1 __________ x - 1  In this case, the end behavior is f (x) ≈  3x² _ x  = 3x. This tells us that as the inputs increase or decrease without bound, this function will behave similarly to the function g(x) = 3x. As the inputs grow large, the outputs will grow and not level off, so this graph has no horizontal asymptote. However, the graph of g(x) = 3x looks like a diagonal line, and since f will behave similarly to g, it will approach a line close to y = 3x. This line is a slant asymptote.

To find the equation of the slant asymptote, divide  3x² - 2x + 1 ___________ x - 1 . The quotient is 3x + 1, and the remainder is 2. The slant asymptote is the graph of the line g(x) = 3x + 1. See Figure 13. x y x = 1 y = 3x + 1 ____ q( x ) , q( x ) ≠  0 where degree of p > degree of q by 1. Case 3: If the degree of the denominator = degree of the numerator, there is a horizontal asymptote at y =  a(n)/(b)n , where an and bn are the leading coefficients of p(x) and q(x) for f (x) =  p(x) ____ q(x) , q(x) ≠  0. Example: f (x) =  3x² + 2 _________ x² + 4x - 5  In this case, the end behavior is f (x) ≈  3x² _ x²  = 3. This tells us that as the inputs grow large, this function will behave like the function g(x) = 3, which is a horizontal line. As x → ± ∞ , f (x) → 3, resulting in a horizontal asymptote at y = 3. See x y x = 1 x = -5 y = 3/q( x ) , q( x ) ≠  0 where degree of p = degree of q. Notice that, while the graph of a rational function will never cross a vertical asymptote, the graph may or may not cross a horizontal or slant asymptote. Also, although the graph of a rational function may have many vertical asymptotes, the graph will have at most one horizontal (or slant) asymptote. It should be noted that, if the degree of the numerator is larger than the degree of the denominator by more than one, the end behavior of the graph will mimic the behavior of the reduced end behavior fraction. For instance, if we had the function f (x) =  3x⁵ - x² _______ x + 3  with end behavior f (x) ≈  3x⁵ ___ x  = 3x⁴, the end behavior of the graph would look similar to that of an even polynomial with a positive leading coefficient. x → ± ∞ , f (x) → ∞  horizontal asymptotes of rational functions The horizontal asymptote of a rational function can be determined by looking at the degrees of the numerator and denominator. • Degree of numerator is less than degree of denominator: horizontal asymptote at y = 0. • Degree of numerator is greater than degree of denominator by one: no horizontal asymptote; slant asymptote. • Degree of numerator is equal to degree of denominator: horizontal asymptote at ratio of leading coefficients.

---
### 📐 **Example  7**: Identifying Horizontal and Slant Asymptotes

For the functions below, identify the horizontal or slant asymptote. a. g(x) =  6x³ - 10x ________ b. h(x) =  x² - 4x + 1 _________ x + 2  c. k(x) =  x² + 4x ______ x³ - 8

**Solution**

For these solutions, we will use f (x) =  p(x) ____ q(x) , q(x) ≠  0. a. g(x) =  6x³ - 10x/2x³ + 5x² : The degree of p = degree of q = 3, so we can find the hori­zontal asymptote by taking the ratio of the leading terms. There is a horizontal asymptote at y =  6/2  or y = 3. b. h(x) =  x² - 4x + 1/x + 2 : The degree of p = 2 and degree of q = 1. Since p > q by 1, there is a slant asymptote found at  x² - 4x + 1/x + 2 .

The quotient is x - 2 and the remainder is 13. There is a slant asymptote at y = x - 2. c. k(x) =  x² + 4(x)/(x)³ - 8 : The degree of p = 2 < degree of q = 3, so there is a horizontal asymptote y = 0.

---
### 📐 **Example  8**: Identifying Horizontal Asymptotes

In the sugar concentration problem earlier, we created the equation C(t) =  5 + t ________ Find the horizontal asymptote and interpret it in context of the problem.

**Solution**

Both the numerator and denominator are linear (degree 1). Because the degrees are equal, there will be a horizontal asymptote at the ratio of the leading coefficients. In the numerator, the leading term is t, with coefficient 1. In the denominator, the leading term is 10t, with coefficient 10. The horizontal asymptote will be at the ratio of these values: t → ∞ , C(t) →  1/10  This function will have a horizontal asymptote at y =  1/10 . This tells us that as the values of t increase, the values of C will approach  1/10 . In context, this means that, as more time goes by, the concentration of sugar in the tank will approach one-tenth of a pound of sugar per gallon of water or  1/10  pounds per gallon.

---
### 📐 **Example  9**: Identifying Horizontal and Vertical Asymptotes

Find the horizontal and vertical asymptotes of the function f (x) =  (x - 2)(x + 3)

_________________

(x - 1)(x + 2)(x - 5)

**Solution**

First, note that this function has no common factors, so there are no potential removable discontinuities. The function will have vertical asymptotes when the denominator is zero, causing the function to be undefined. The denominator will be zero at x = 1, -2, and 5, indicating vertical asymptotes at these values. The numerator has degree 2, while the denominator has degree 3. Since the degree of the denominator is greater than the degree of the numerator, the denominator will grow faster than the numerator, causing the outputs to tend towards zero as the inputs get large, and so as x → ± ∞ , f (x) → 0. This function will have a horizontal asymptote at y = 0. See Figure 15. x y x = 5 x = -2 x = 1 y = 0 -4 -2 -6

---
### ✏️ **Try It #6**
Find the vertical and horizontal asymptotes of the function:

f (x) =  (2x - 1)(2x + 1)

_____________

(x - 2)(x + 3)  intercepts of rational functions A rational function will have a y-intercept when the input is zero, if the function is defined at zero. A rational function will not have a y-intercept if the function is not defined at zero. Likewise, a rational function will have x-intercepts at the inputs that cause the output to be zero. Since a fraction is only equal to zero when the numerator is zero, x-intercepts can only occur when the numerator of the rational function is equal to zero.

---
### 📐 **Example  10**
Finding the Intercepts of a Rational Function Find the intercepts of f (x) =  (x - 2)(x + 3)

__________________

(x - 1)(x + 2)(x - 5)  .

**Solution**

We can find the y-intercept by evaluating the function at zero

f (0) =  (0 - 2)(0 + 3)

_________________

(0 - 1)(0 + 2)(0 - 5) 

=  -6 ___ 10 

= - 3/5 

The x-intercepts will occur when the function is equal to zero:

0 =  (x - 2)(x + 3)

_________________

(x - 1)(x + 2)(x - 5)  This is zero when the numerator is zero.

0 = (x - 2)(x + 3)

x = 2, -3 The y-intercept is (0, -0.6), the x-intercepts are (2, 0) and (-3, 0). See Figure 16. x = 1 x = -2 x = 5 y x y = 0

---
### ✏️ **Try It #7**
Given the reciprocal squared function that is shifted right 3 units and down 4 units, write this as a rational function. Then, find the x- and y-intercepts and the horizontal and vertical asymptotes.

### Graphing Rational Functions

In Example 9, we see that the numerator of a rational function reveals the x-intercepts of the graph, whereas the denominator reveals the vertical asymptotes of the graph. As with polynomials, factors of the numerator may have integer powers greater than one. Fortunately, the effect on the shape of the graph at those intercepts is the same as we saw with polynomials. The vertical asymptotes associated with the factors of the denominator will mirror one of the two toolkit reciprocal functions. When the degree of the factor in the denominator is odd, the distinguishing characteristic is that on one side of the vertical asymptote the graph heads towards positive infinity, and on the other side the graph heads towards negative infinity. See x y x = 0 y = x When the degree of the factor in the denominator is even, the distinguishing characteristic is that the graph either heads toward positive infinity on both sides of the vertical asymptote or heads toward negative infinity on both sides. See Figure 18. x x = 0 y = x²1 For example, the graph of f (x) =  (x + 1)²(x - 3)

_____________

(x + 3)²(x - 2)  is shown in Figure 19. x y x = 2 x = -3 y = 1 f (x) = (x + 1)² (x - 3) (x + 3)² (x - 2)

• At the x-intercept x = -1 corresponding to the (x + 1)² factor of the numerator, the graph bounces, consistent with the quadratic nature of the factor. • At the x-intercept x = 3 corresponding to the (x - 3) factor of the numerator, the graph passes through the axis as we would expect from a linear factor. • At the vertical asymptote x = -3 corresponding to the (x + 3)² factor of the denominator, the graph heads towards positive infinity on both sides of the asymptote, consistent with the behavior of the function f (x) =  1/x 2 . • At the vertical asymptote x = 2, corresponding to the (x - 2) factor of the denominator, the graph heads towards positive infinity on the left side of the asymptote and towards negative infinity on the right side, consistent with the behavior of the function f (x) =  1/x .

---
### 💡 **How To…**
Given a rational function, sketch a graph. 1. Evaluate the function at 0 to find the y-intercept. 2. Factor the numerator and denominator. 3. For factors in the numerator not common to the denominator, determine where each factor of the numerator is zero to find the x-intercepts. 4. Find the multiplicities of the x-intercepts to determine the behavior of the graph at those points. 5. For factors in the denominator, note the multiplicities of the zeros to determine the local behavior. For those factors not common to the numerator, find the vertical asymptotes by setting those factors equal to zero and then solve. 6. For factors in the denominator common to factors in the numerator, find the removable discontinuities by setting those factors equal to 0 and then solve. 7. Compare the degrees of the numerator and the denominator to determine the horizontal or slant asymptotes. 8. Sketch the graph.

---
### 📐 **Example  11**: Graphing a Rational Function

Sketch a graph of f (x) =  (x + 2)(x - 3)

____________

(x + 1)²(x - 2)  .

**Solution**

We can start by noting that the function is already factored, saving us a step. Next, we will find the intercepts. Evaluating the function at zero gives the y-intercept: f (0) =  (0 + 2)(0 - 3)

__

(0 + 1)²(0 - 2) 

= 3 To find the x-intercepts, we determine when the numerator of the function is zero. Setting each factor equal to zero, we find x-intercepts at x = -2 and x = 3. At each, the behavior will be linear (multiplicity 1), with the graph passing through the intercept. We have a y-intercept at (0, 3) and x-intercepts at (-2, 0) and (3, 0). To find the vertical asymptotes, we determine when the denominator is equal to zero. This occurs when x + 1 = 0 and when x - 2 = 0, giving us vertical asymptotes at x = -1 and x = 2. There are no common factors in the numerator and denominator. This means there are no removable discontinuities. Finally, the degree of denominator is larger than the degree of the numerator, telling us this graph has a horizontal asymptote at y = 0. To sketch the graph, we might start by plotting the three intercepts. Since the graph has no x-intercepts between the vertical asymptotes, and the y-intercept is positive, we know the function must remain positive between the asymptotes, letting us fill in the middle portion of the graph as shown in Figure 20.

y x The factor associated with the vertical asymptote at x = -1 was squared, so we know the behavior will be the same on both sides of the asymptote. The graph heads toward positive infinity as the inputs approach the asymptote on the right, so the graph will head toward positive infinity on the left as well. For the vertical asymptote at x = 2, the factor was not squared, so the graph will have opposite behavior on either side of the asymptote. See Figure 21. After passing through the x-intercepts, the graph will then level off toward an output of zero, as indicated by the horizontal asymptote. y = 0 x = –1 x = 2 y x

---
### ✏️ **Try It #8**
Given the function f (x) =  (x + 2)²(x - 2)

______________

2(x - 1)² (x - 3) , use the characteristics of polynomials and rational functions to describe its behavior and sketch the function. Writing Rational Functions Now that we have analyzed the equations for rational functions and how they relate to a graph of the function, we can use information given by a graph to write the function. A rational function written in factored form will have an x-intercept where each factor of the numerator is equal to zero. (An exception occurs in the case of a removable discontinuity.) As a result, we can form a numerator of a function whose graph will pass through a set of x-intercepts by introducing a corresponding set of factors. Likewise, because the function will have a vertical asymptote where each factor of the denominator is equal to zero, we can form a denominator that will produce the vertical asymptotes by introducing a corresponding set of factors. writing rational functions from intercepts and asymptotes If a rational function has x-intercepts at x = x¹, x², ... , xn, vertical asymptotes at x = v¹, v², ... , vm, and no xi = any vj, then the function can be written in the form: f (x) = a  (x - x¹) p 1(x - x²) p 2 ... (x - xn) p n

___

(x - v¹) q¹(x - v²) q² ... (x - vm) qn where the powers pi or qi on each factor can be determined by the behavior of the graph at the corresponding intercept or asymptote, and the stretch factor a can be determined given a value of the function other than the x-intercept or by the horizontal asymptote if it is nonzero.

---
### 💡 **How To…**
Given a graph of a rational function, write the function. 1. Determine the factors of the numerator. Examine the behavior of the graph at the x-intercepts to determine the zeroes and their multiplicities. (This is easy to do when finding the “simplest” function with small multiplicities—such as 1 or 3—but may be difficult for larger multiplicities—such as 5 or 7, for example.) 2. Determine the factors of the denominator. Examine the behavior on both sides of each vertical asymptote to determine the factors and their powers. 3. Use any clear point on the graph to find the stretch factor.

---
### 📐 **Example  12**: Writing a Rational Function from Intercepts and Asymptotes

Write an equation for the rational function shown in Figure 22. x y

**Solution**

The graph appears to have x-intercepts at x = -2 and x = 3. At both, the graph passes through the intercept, suggesting linear factors. The graph has two vertical asymptotes. The one at x = -1 seems to exhibit the basic behavior similar to  1/x , with the graph heading toward positive infinity on one side and heading toward negative infinity on the other. The asymptote at x = 2 is exhibiting a behavior similar to  1/x 2 , with the graph heading toward negative infinity on both sides of the asymptote. See Figure 23. x y x-intercepts Vertical asymptotes We can use this information to write a function of the form f (x) = a (x + 2)(x - 3)

__

(x + 1)(x - 2)² 

To find the stretch factor, we can use another clear point on the graph, such as the y-intercept (0, -2).

-2 = a  (0 + 2)(0 - 3)

__

(0 + 1)(0 - 2)² 

-2 = a -6/4 

a =  -8 _ -6  =  4/3  This gives us a final function of f (x) =  4(x + 2)(x - 3)

______________

3(x + 1)(x - 2)² . Access these online resources for additional instruction and practice with rational functions. • Graphing Rational Functions (http://openstaxcollege.org/l/graphrational) • Find the Equation of a Rational Function (http://openstaxcollege.org/l/equatrational) • Determining Vertical and Horizontal Asymptotes (http://openstaxcollege.org/l/asymptote) • Find the Intercepts, Asymptotes, and Hole of a Rational Function (http://openstaxcollege.org/l/interasymptote)

## 3.7 Section Exercises

---
### 3.7 section EXERCISES

Verbal 1. What is the fundamental difference in the algebraic representation of a polynomial function and a rational function? 2. What is the fundamental difference in the graphs of polynomial functions and rational functions? 3. If the graph of a rational function has a removable discontinuity, what must be true of the functional rule? 4. Can a graph of a rational function have no vertical asymptote? If so, how? 5. Can a graph of a rational function have no x-intercepts? If so, how? Algebraic For the following exercises, find the domain of the rational functions. 6. f (x) =  x - 1 _____ x + 2  7. f (x) =  x + 1 _____ x² - 1  8. f (x) =  x² + 4 _________ x² - 2x - 8  9. f (x) =  x² + 4x - 3 _________

x⁴ - 5x² + 4  For the following exercises, find the domain, vertical asymptotes, and horizontal asymptotes of the functions. 10. f (x) =  4 ____ x - 1  11. f (x) =  _____ 5x + 2  12. f (x) =  x _____ x² - 9  13. f (x) =  x __________

x² + 5x - 36  14. f (x) =  3 + x ______ x³ - 27  15. f (x) =  3x - 4 _______ x³ - 16x  16. f (x) =  x² - 1 ___________

x³ + 9x² + 14x  17. f (x) =  x + 5 ______ x² - 25  18. f (x) =  x - 4 _____ x - 6  19. f (x) =  4 - 2x ______ 3x - 1  For the following exercises, find the x- and y-intercepts for the functions. 20. f (x) =  x + 5 _____ x² + 4  21. f (x) =  x _____ x² - x  22. f (x) =  x² + 8x + 7 ___________

x² + 11x + 30  23. f (x) =  x² + x + 6 ___________

x² - 10x + 24  24. f (x) =  94 - 2x² _______ For the following exercises, describe the local and end behavior of the functions. 25. f (x) =  x _____ 2x + 1  26. f (x) =  2x _____ x - 6  27. f (x) =  -2x _____ x - 6  28. f (x) =  x² - 4x + 3 _________ x² - 4x - 5  29. f (x) =  ___________

6x² + 13x - 5  For the following exercises, find the slant asymptote of the functions. 30. f (x) =  24x² + 6x ________ 2x + 1  31. f (x) =  4x² - 10 _______ 2x - 4  32. f (x) =  81x² - 18 ________ 3x - 2  33. f (x) =  6x³ - 5x _______ 3x² + 4  34. f (x) =  x² + 5x + 4 _________ x - 1 

Graphical For the following exercises, use the given transformation to graph the function. Note the vertical and horizontal asymptotes. 35. The reciprocal function shifted up two units. 36. The reciprocal function shifted down one unit and left three units. 37. The reciprocal squared function shifted to the right 2 units. 38. The reciprocal squared function shifted down 2 units and right 1 unit. For the following exercises, find the horizontal intercepts, the vertical intercept, the vertical asymptotes, and the horizontal or slant asymptote of the functions. Use that information to sketch a graph. 39. p(x) =  2x - 3 ______ x + 4  40. q(x) =  x - 5 _____ 3x - 1  41. s(x) =  ______ (x - 2)²  42. r(x) =  ______ (x + 1)²  43. f (x) =  3x 2 - 14x - 5/3x 2 + 8x - 16  44. g(x) =  2x 2 + 7x - 15/45. a(x) =  x 2 + 2x - 3/x 2 - 1  46. b(x) =  x 2 - x - 6/x 2 - 4  47. h(x) =  2x 2 + x - 1/x - 4  48. k(x) =  2x 2 - 3x - 20/x - 5  49. w(x) =  (x - 1)(x + 3)(x - 5)

__

(x + 2)²(x - 4)  50. z(x) =  (x + 2)²(x - 5)

__

(x - 3)(x + 1)(x + 4)  For the following exercises, write an equation for a rational function with the given characteristics. 51. Vertical asymptotes at x = 5 and x = -5, x-intercepts at (2, 0) and (-1, 0), y-intercept at (0, 4) 52. Vertical asymptotes at x = -4 and x = -1, x-intercepts at (1, 0) and (5, 0), y-intercept at (0, 7) 53. Vertical asymptotes at x = -4 and x = -5, x-intercepts at (4, 0) and (-6, 0), horizontal asymptote at y = 7 54. Vertical asymptotes at x = -3 and x = 6, x-intercepts at (-2, 0) and (1, 0), horizontal asymptote at y = -2 55. Vertical asymptote at x = -1, double zero at x = 2, y-intercept at (0, 2) 56. Vertical asymptote at x = 3, double zero at x = 1, y-intercept at (0, 4) For the following exercises, use the graphs to write an equation for the function. y x y x y x

y x y x y x y x y x Numeric For the following exercises, make tables to show the behavior of the function near the vertical asymptote and reflecting the horizontal asymptote. 65. f (x) =  1 _____ x - 2  66. f (x) =  x _____ x - 3  67. f (x) =  2x _____ x + 4  68. f (x) =  2x ______ (x - 3)²  69. f (x) =  x² _________ x² + 2x + 1  Technology For the following exercises, use a calculator to graph f (x). Use the graph to solve f (x) > 0. 70. f (x) =  2 _____ x + 1  71. f (x) =  _____ 2x - 3  72. f (x) =  ___________

(x - 1)(x + 2)  73. f (x) =  x + 2 ___________

(x - 1)(x - 4)  74. f (x) =  (x + 3)² ____________

(x - 1)²(x + 1)  Extensions For the following exercises, identify the removable discontinuity. 75. f (x) =  x² - 4 _____ x - 2  76. f (x) =  x³ + 1 _____ x + 1  77. f (x) =  x² + x - 6 ________ x - 2  78. f (x) =  2x² + 5x - 3 __________ x + 3  79. f (x) =  x³ + x² ______ x + 1 

Real-World Applications For the following exercises, express a rational function that describes the situation. 80. A large mixing tank currently contains 200 gallons of water, into which 10 pounds of sugar have been mixed. A tap will open, pouring 10 gallons of water per minute into the tank at the same time sugar is poured into the tank at a rate of 3 pounds per minute. Find the concentration (pounds per gallon) of sugar in the tank after t minutes. 81. A large mixing tank currently contains 300 gallons of water, into which 8 pounds of sugar have been mixed. A tap will open, pouring 20 gallons of water per minute into the tank at the same time sugar is poured into the tank at a rate of 2 pounds per minute. Find the concentration (pounds per gallon) of sugar in the tank after t minutes. For the following exercises, use the given rational function to answer the question. 82. The concentration C of a drug in a patient’s bloodstream t hours after injection in given by C(t) =  2t/3 + t² . What happens to the concentration of the drug as t increases? 83. The concentration C of a drug in a patient’s bloodstream t hours after injection is given by C(t) =  100t/2t² + 75 . Use a calculator to approximate the time when the concentration is highest. For the following exercises, construct a rational function that will help solve the problem. Then, use a calculator to answer the question. 84. An open box with a square base is to have a volume of 108 cubic inches. Find the dimensions of the box that will have minimum surface area. Let x = length of the side of the base. 85. A rectangular box with a square base is to have a volume of 20 cubic feet. The material for the base costs 30 cents/square foot. The material for the sides costs 10 cents/square foot. The material for the top costs 20 cents/square foot. Determine the dimensions that will yield minimum cost. Let x = length of the side of the base. 86. A right circular cylinder has volume of 100 cubic inches. Find the radius and height that will yield minimum surface area. Let x = radius. 87. A right circular cylinder with no top has a volume of 50 cubic meters. Find the radius that will yield minimum surface area. Let x = radius. 88. A right circular cylinder is to have a volume of 40 cubic inches. It costs 4 cents/square inch to construct the top and bottom and 1 cent/square inch to construct the rest of the cylinder. Find the radius to yield minimum cost. Let x = radius.

## 3.8 Inverses and Radical Functions

---
Learning Objectives
In this section, you will:
• Find the inverse of a polynomial function.
• Restrict the domain to find the inverse of a polynomial function.
A mound of gravel is in the shape of a cone with the height equal to twice the radius. The volume is found using a formula from elementary geometry.

V =  1/3 π r 2 h

=  1/3 π r 2(2r)

=  2/3 π r 3 We have written the volume V in terms of the radius r. However, in some cases, we may start out with the volume and want to find the radius. For example: A customer purchases 100 cubic feet of gravel to construct a cone shape mound with a height twice the radius. What are the radius and height of the new cone? To answer this question, we use the formula

r = √____

 3V ___ 2π    This function is the inverse of the formula for V in terms of r. In this section, we will explore the inverses of polynomial and rational functions and in particular the radical functions we encounter in the process. Finding the Inverse of a Polynomial Function Two functions f and g are inverse functions if for every coordinate pair in f, (a, b), there exists a corresponding coordinate pair in the inverse function, g, (b, a). In other words, the coordinate pairs of the inverse functions have the input and output interchanged. For a function to have an inverse function the function to create a new function that is one-to-one and would have an inverse function. For example, suppose a water runoff collector is built in the shape of a parabolic trough as shown in Figure 2. We can use the information in the figure to find the surface area of the water in the trough as a function of the depth of the water. 18 in 3 f 12 in

Because it will be helpful to have an equation for the parabolic cross-sectional shape, we will impose a coordinate system at the cross section, with x measured horizontally and y measured vertically, with the origin at the vertex of the parabola. See Figure 3. x y From this we find an equation for the parabolic shape. We placed the origin at the vertex of the parabola, so we know the equation will have form y(x) = ax². Our equation will need to pass through the point (6, 18), from which we can solve for the stretch factor a.

a =  18/36 

=  1/2  Our parabolic cross section has the equation

y(x) =  1/2 x² We are interested in the surface area of the water, so we must determine the width at the top of the water as a function of the water depth. For any depth y the width will be given by 2x, so we need to solve the equation above for x and find the inverse function. However, notice that the original function is not one-to-one, and indeed, given any output there are two inputs that produce the same output, one positive and one negative. To find an inverse, we can restrict our original function to a limited domain on which it is one-to-one. In this case, it makes sense to restrict ourselves to positive x values. On this domain, we can find an inverse by solving for the input variable:

y =  1/2 x²

2y = x²

x = ± √2y  This is not a function as written. We are limiting ourselves to positive x values, so we eliminate the negative solution, giving us the inverse function we’re looking for.

y =  x²

__ 2 , x > 0 Because x is the distance from the center of the parabola to either side, the entire width of the water at the top will be 2x. The trough is 3 feet (36 inches) long, so the surface area will then be:

Area = l ⋅ w

= 36 ⋅ 2x

= 72x

= 72√2y  This example illustrates two important points: 1. When finding the inverse of a quadratic, we have to limit ourselves to a domain on which the function is one-to-one. 2. The inverse of a quadratic function is a square root function. Both are toolkit functions and different types of power functions.

Functions involving roots are often called radical functions. While it is not possible to find an inverse of most polynomial functions, some basic polynomials do have inverses. Such functions are called invertible functions, and we use the notation f -1(x). Warning: f -1(x) is not the same as the reciprocal of the function f (x). This use of “-1” is reserved to denote inverse functions. To denote the reciprocal of a function f (x), we would need to write ( f (x))-1 =  1/f (x) . An important relationship between inverse functions is that they “undo” each other. If f -1 is the inverse of a function f, then f is the inverse of the function f -1. In other words, whatever the function f does to x, f -1 undoes it—and viceversa. More formally, we write

f -1 ( f (x)) = x, for all x in the domain of f and

f ( f -1 (x)) = x, for all x in the domain of f -1 verifying two functions are inverses of one another Two functions, f and g, are inverses of one another if for all x in the domain of f and g. g( f (x)) = f ( g(x)) = x

---
### 💡 **How To…**
Given a polynomial function, find the inverse of the function by restricting the domain in such a way that the new function is one-to-one. 1. Replace f (x) with y. 2. Interchange x and y. 3. Solve for y, and rename the function f -1(x).

---
### 📐 **Example  1**: Verifying Inverse Functions

Show that f (x) =  1/x + 1  and f -1(x) =  1/x  - 1 are inverses, for x ≠  0, -1.

**Solution**

We must show that f -1( f (x)) = x and f ( f -1(x)) = x. f -1(f (x)) = f -1(  1 _____ x + 1  )

=  _  1 _____ x + 1   - 1

= (x + 1) - 1

= x

f (f -1(x)) = f (  1/x  - 1 )

=  __

(  1/x  - 1 ) + 1 

=  1/1 __ x  

= x Therefore, f (x) =  1 _____ x + 1  and f -1 (x) =  1/x  - 1 are inverses.

---
### ✏️ **Try It #1**
Show that f (x) =  x + 5 _____  and f -1(x) = 3x - 5 are inverses.

---
### 📐 **Example  2**
Finding the Inverse of a Cubic Function Find the inverse of the function f (x) = 5x³ + 1.

**Solution**

This is a transformation of the basic cubic toolkit function, and based on our knowledge of that function, we know it is one-to-one. Solving for the inverse by solving for x.

y = 5x³ + 1

x = 5y³ + 1

x - 1 = 5y³

 x - 1 _____  = y³

f -1(x) =  √x - 1 _____   Analysis Look at the graph of f and f -1. Notice that the two graphs are symmetrical about the line y = x. This is always the case when graphing a function and its inverse function. Also, since the method involved interchanging x and y, notice corresponding points. If (a, b) is on the graph of f , then (b, a) is on the graph of f -1. Since (0, 1) is on the graph of f, then (1, 0) is on the graph of f -1. Similarly, since (1, 6) is on the graph of f, then (6, 1) is on the graph of f -1. See Figure 4. x y f (x) = 5x³ + 1 y = x

---
### ✏️ **Try It #2**
Find the inverse function of f (x) = 

√x + 4  Restricting the Domain to Find the Inverse of a Polynomial Function So far, we have been able to find the inverse functions of cubic functions without having to restrict their domains. However, as we know, not all cubic polynomials are one-to-one. Some functions that are not one-to-one may have their domain restricted so that they are one-to-one, but only over that domain. The function over the restricted domain would then have an inverse function. Since quadratic functions are not one-to-one, we must restrict their domain in order to find their inverses. restricting the domain If a function is not one-to-one, it cannot have an inverse. If we restrict the domain of the function so that it becomes one-to-one, thus creating a new function, this new function will have an inverse.

---
### 💡 **How To…**
Given a polynomial function, restrict the domain of a function that is not one-to-one and then find the inverse. 1. Restrict the domain by determining a domain on which the original function is one-to-one. 2. Replace f (x) with y. 3. Interchange x and y. 4. Solve for y, and rename the function or pair of functions f -1(x). 5. Revise the formula for f -1(x) by ensuring that the outputs of the inverse function correspond to the restricted domain of the original function.

---
### 📐 **Example  3**
Restricting the Domain to Find the Inverse of a Polynomial Function Find the inverse function of f : a. f (x) = (x - 4)², x ≥  4 b. f (x) = (x - 4)², x ≤  4

**Solution**

The original function f (x) = (x - 4)² is not one-to-one, but the function is restricted to a domain of x ≥  4 or x ≤  4 on which it is one-to-one. See Figure 5. x y f (x) = (x - 4)², x ≥  4 x y f (x) = (x - 4)², x ≤  4 To find the inverse, start by replacing f (x) with the simple variable y.

y = (x - 4)² Interchange x and y.

x = (y - 4)² Take the square root.

± √x  = y - 4 Add 4 to both sides.

4 ±  √x  = y This is not a function as written. We need to examine the restrictions on the domain of the original function to determine the inverse. Since we reversed the roles of x and y for the original f (x), we looked at the domain: the values x could assume. When we reversed the roles of x and y, this gave us the values y could assume. For this function, x ≥  4, so for the inverse, we should have y ≥  4, which is what our inverse function gives. a. The domain of the original function was restricted to x ≥  4, so the outputs of the inverse need to be the same, f (x) ≥  4, and we must use the + case: f -1(x) = 4 + √x  b. The domain of the original function was restricted to x ≤  4, so the outputs of the inverse need to be the same, f (x) ≤  4, and we must use the - case: f -1(x) = 4 - √x  Analysis On the graphs in Figure 6, we see the original function graphed on the same set of axes as its inverse function. Notice that together the graphs show symmetry about the line y = x. The coordinate pair (4, 0) is on the graph of f and the coordinate pair (0, 4) is on the graph of f -1. For any coordinate pair, if (a, b) is on the graph of f, then (b, a) is on the graph of f -1. Finally, observe that the graph of f intersects the graph of f -1 on the line y = x. Points of intersection for the graphs of f and f -1 will always lie on the line y = x.

x y x y f (x) f (x) f –1(x) f –1(x) y = x y = x

---
### 📐 **Example  4**
Finding the Inverse of a Quadratic Function When the Restriction Is Not Specified Restrict the domain and then find the inverse of

f (x) = (x - 2)² - 3.

**Solution**

We can see this is a parabola with vertex at (2, -3) that opens upward. Because the graph will be decreasing on one side of the vertex and increasing on the other side, we can restrict this function to a domain on which it will be one-to-one by limiting the domain to x ≥  2. To find the inverse, we will use the vertex form of the quadratic. We start by replacing f (x) with a simple variable, y, then solve for x.

y = (x - 2)² - 3 Interchange x and y.

x = (y - 2)² - 3 Add 3 to both sides.

x + 3 = (y - 2)² Take the square root.

± √x + 3  = y - 2 Add 2 to both sides.

2 ±  √x + 3  = y Rename the function.

f -1(x) = 2 ± √x + 3  Now we need to determine which case to use. Because we restricted our original function to a domain of x ≥  2, the outputs of the inverse should be the same, telling us to utilize the + case

f -1(x) = 2 + √x + 3  If the quadratic had not been given in vertex form, rewriting it into vertex form would be the first step. This way we may easily observe the coordinates of the vertex to help us restrict the domain.

**Analysis**
Notice that we arbitrarily decided to restrict the domain on x ≥  2. We could just have easily opted to restrict the domain on x ≤  2, in which case f -1(x) = 2 - √x + 3 . Observe the original function graphed on the same set of axes as its inverse function in Figure 7. Notice that both graphs show symmetry about the line y = x. The coordinate pair (2, -3) is on the graph of f and the coordinate pair (-3, 2) is on the graph of f -1. Observe from the graph of both functions on the same set of axes that

domain of f = range of f -1 = [2, ∞ ) and

domain of f -1 = range of f = [-3, ∞ ) Finally, observe that the graph of f intersects the graph of f -1 along the line y = x. x y f (x) f –1(x) y = x

---
### ✏️ **Try It #3**
Find the inverse of the function f (x) = x² + 1, on the domain x ≥  0. Solving Applications of Radical Functions Notice that the functions from previous examples were all polynomials, and their inverses were radical functions. If we want to find the inverse of a radical function, we will need to restrict the domain of the answer because the range of the original function is limited.

---
### 💡 **How To…**
Given a radical function, find the inverse. 1. Determine the range of the original function. 2. Replace f (x) with y, then solve for x. 3. If necessary, restrict the domain of the inverse function to the range of the original function.

---
### 📐 **Example  5**
Finding the Inverse of a Radical Function Restrict the domain and then find the inverse of the function f (x) = √x - 4 .

**Solution**

Note that the original function has range f (x) ≥  0. Replace f (x) with y, then solve for x.

y = √x - 4  Replace f (x) with y.

x = √y - 4  Interchange x and y.

x = √y - 4  Square each side.

x² = y - 4 Add 4.

x² + 4 = y Rename the function f-1(x).

f -1(x) = x² + 4 Recall that the domain of this function must be limited to the range of the original function. f -1(x) = x² + 4, x ≥  0 Analysis Notice in Figure 8 that the inverse is a reflection of the original function over the line y = x. Because the original function has only positive outputs, the inverse function has only positive inputs. x y f (x) f –1(x) y = x

---
### ✏️ **Try It #4**
Restrict the domain and then find the inverse of the function f (x) = √2x + 3 .

### Solving Applications of Radical Functions

Radical functions are common in physical models, as we saw in the section opener. We now have enough tools to be able to solve the problem posed at the start of the section.

---
### 📐 **Example  6**: Solving an Application with a Cubic Function

A mound of gravel is in the shape of a cone with the height equal to twice the radius. The volume of the cone in terms of the radius is given by

V =  2/3 π r 3 Find the inverse of the function V =  2/3 π r 3 that determines the volume V of a cone and is a function of the radius r. Then use the inverse function to calculate the radius of such a mound of gravel measuring 100 cubic feet. Use π  = 3.14.

**Solution**

Start with the given function for V. Notice that the meaningful domain for the function is r ≥  0 since negative radii would not make sense in this context. Also note the range of the function (hence, the domain of the inverse function) is V ≥  0. Solve for r in terms of V, using the method outlined previously.

V =  2/3 π r 3

r 3 =  3V ___ 2π   Solve for r 3.

r = √____

 3V ___ 2π    Solve for r. This is the result stated in the section opener. Now evaluate this for V = 100 and π  = 3.14.

r = √____

 3V ___ 2π   

= √_______ ______ ≈  √Therefore, the radius is about 3.63 ft. Determining the Domain of a Radical Function Composed with Other Functions When radical functions are composed with other functions, determining domain can become more complicated.

---
### 📐 **Example  7**: Finding the Domain of a Radical Function Composed with a Rational Function

Find the domain of the function f (x) = √___________

 (x + 2)(x - 3)

____________ (x - 1)  .

**Solution**

Because a square root is only defined when the quantity under the radical is non-negative, we need to determine where  (x + 2)(x - 3)

____________ (x - 1)  ≥  0. The output of a rational function can change signs (change from positive to negative or vice versa) at x-intercepts and at vertical asymptotes. For this equation, the graph could change signs at x = -2, 1, and 3. To determine the intervals on which the rational expression is positive, we could test some values in the expression or sketch a graph. While both approaches work equally well, for this example we will use a graph as shown in Figure 9. x y Outputs are non-negative Outputs are non-negative x = 1

This function has two x-intercepts, both of which exhibit linear behavior near the x-intercepts. There is one vertical asymptote, corresponding to a linear factor; this behavior is similar to the basic reciprocal toolkit function, and there is no horizontal asymptote because the degree of the numerator is larger than the degree of the denominator. There is a y-intercept at (0, √— 6 ). From the y-intercept and x-intercept at x = -2, we can sketch the left side of the graph. From the behavior at the asymptote, we can sketch the right side of the graph. From the graph, we can now tell on which intervals the outputs will be non-negative, so that we can be sure that the original function f (x) will be defined. f (x) has domain -2 ≤  x < 1 or x ≥  3, or in interval notation, [-2, 1) ∪ [3, ∞ ). Finding Inverses of Rational Functions As with finding inverses of quadratic functions, it is sometimes desirable to find the inverse of a rational function, particularly of rational functions that are the ratio of linear functions, such as in concentration applications.

---
### 📐 **Example  8**
Finding the Inverse of a Rational Function The function C =  20 + 0.4n ________ 100 + n  represents the concentration C of an acid solution after n mL of 40% solution has been added to 100 mL of a 20% solution. First, find the inverse of the function; that is, find an expression for n in terms of C. Then use your result to determine how much of the 40% solution should be added so that the final mixture is a 35% solution.

**Solution**

We first want the inverse of the function. We will solve for n in terms of C.

C =  20 + 0.4n ________ 100 + n 

n =  100C - 20 _________ 0.4 - C  Now evaluate this function for C = 0.35 (35%).

____________

=  15 ___

= 300 We can conclude that 300 mL of the 40% solution should be added.

---
### ✏️ **Try It #5**
Find the inverse of the function f (x) =  x + 3 _____ x - 2 .

Access these online resources for additional instruction and practice with inverses and radical functions. • Graphing the Basic Square Root Function (http://openstaxcollege.org/l/graphsquareroot) • Find the Inverse of a Square Root Function (http://openstaxcollege.org/l/inversesquare) • Find the Inverse of a Rational Function (http://openstaxcollege.org/l/inverserational) • Find the Inverse of a Rational Function and an Inverse Function Value (http://openstaxcollege.org/l/rationalinverse) • Inverse Functions (http://openstaxcollege.org/l/inversefunction)

### 3.8 section EXERCISES

Verbal 1. Explain why we cannot find inverse functions for all polynomial functions. 2. Why must we restrict the domain of a quadratic function when finding its inverse? 3. When finding the inverse of a radical function, what restriction will we need to make? 4. The inverse of a quadratic function will always take what form? Algebraic For the following exercises, find the inverse of the function on the given domain. 5. f (x) = (x - 4)², [4, ∞ ) 6. f (x) = (x + 2)², [-2, ∞ ) 7. f (x) = (x + 1)² - 3, [-1, ∞ ) 8. f (x) = 2 - √3 + x  9. f (x) = 3x 2 + 5, (-∞ , 0] 10. f (x) = 12 - x 2, [0, ∞ ) 11. f (x) = 9 - x 2, [0, ∞ ) 12. f (x) = 2x 2 + 4, [0, ∞ ) For the following exercises, find the inverse of the functions. 13. f (x) = x 3 + 5 14. f (x) = 3x 3 + 1 15. f (x) = 4 - x 3 16. f (x) = 4 - 2x 3 For the following exercises, find the inverse of the functions. 17. f (x) = √2x + 1  18. f (x) = √3 - 4x  19. f (x) = 9 + √4x - 4  20. f (x) = √6x - 8  + 5 21. f (x) = 9 + 2 √x  22. f (x) = 3 -  √x  23. f (x) =  2 _____ x + 8  24. f (x) =  3 _____ x - 4  25. f (x) =  x + 3 _____ x + 7  26. f (x) =  x - 2 _____ x + 7  27. f (x) =  3x + 4 ______ 5 - 4x  28. f (x) =  5x + 1 ______ 2 - 5x  29. f (x) = x 2 + 2x, [-1, ∞ ) 30. f (x) = x 2 + 4x + 1, [-2, ∞ ) 31. f (x) = x 2 - 6x + 3, [3, ∞ ) Graphical For the following exercises, find the inverse of the function and graph both the function and its inverse. 32. f (x) = x 2 + 2, x ≥  0 33. f (x) = 4 - x 2, x ≥  0 34. f (x) = (x + 3)², x ≥  -3 35. f (x) = (x - 4)², x ≥  4 36. f (x) = x 3 + 3 37. f (x) = 1 - x 3 38. f (x) = x 2 + 4x, x ≥  -2 39. f (x) = x 2 - 6x + 1, x ≥  3 40. f (x) =  2/x  41. f (x) =  1/x² , x ≥  0 For the following exercises, use a graph to help determine the domain of the functions. 42. f (x) = √_____________

 (x + 1)(x - 1)

__ x   43. f (x) = √_____________

 (x + 2)(x - 3)

__ x - 1   44. f (x) = √________

 x(x + 3) _ x - 4   45. f (x) = √___________  x² - x - 20/x - 2   46. f (x) = √______

 9 - x² _ x + 4  

## 3.8 Section Exercises

---
Technology For the following exercises, use a calculator to graph the function. Then, using the graph, give three points on the graph of the inverse with y-coordinates given. 47. f (x) = x³ - x - 2, y = 1, 2, 3 48. f (x) = x³ + x - 2, y = 0, 1, 2 49. f (x) = x³ + 3x - 4, y = 0, 1, 2 50. f (x) = x³ + 8x - 4, y = -1, 0, 1 51. f (x) = x⁴ + 5x + 1, y = -1, 0, 1 Extensions For the following exercises, find the inverse of the functions with a, b, c positive real numbers. 52. f (x) = ax³ + b 53. f (x) = x² + bx 54. f (x) = √ax² + b  55. f (x) = 

√ax + b  56. f (x) =  ax + b ______ x + c  Real-World Applications For the following exercises, determine the function described and then use it to answer the question. 57. An object dropped from a height of 200 meters has a height, h(t), in meters after t seconds have lapsed, such that h(t) = 200 - 4.9t 2. Express t as a function of height, h, and find the time to reach a height of 50 meters. 58. An object dropped from a height of 600 feet has a height, h(t), in feet after t seconds have elapsed, such that h(t) = 600 - 16t 2. Express t as a function of height h, and find the time to reach a height of 400 feet. 59. The volume, V, of a sphere in terms of its radius, r, is given by V(r) =  4/3 π r 3. Express r as a function of V, and find the radius of a sphere with volume of 200 cubic feet. 60. The surface area, A, of a sphere in terms of its radius, r, is given by A(r) = 4π r 2. Express r as a function of V, and find the radius of a sphere with a surface area of 1000 square inches. 61. A container holds 100 ml of a solution that is 25 ml acid. If n ml of a solution that is 60% acid is added, the function C(n) =  25 + 0.6n ________ 100 + n  gives the concentration, C, as a function of the number of ml added, n. Express n as a function of C and determine the number of mL that need to be added to have a solution that is 50% acid. 62. The period T, in seconds, of a simple pendulum as a function of its length l, in feet, is given by T(l) = 2π  √____

 l ____ 32.2  . Express l as a function of T and determine the length of a pendulum with period of 2 seconds. 63. The volume of a cylinder, V, in terms of radius, r, and height, h, is given by V = π r 2h. If a cylinder has a height of 6 meters, express the radius as a function of V and find the radius of a cylinder with volume of 300 cubic meters. 64. The surface area, A, of a cylinder in terms of its radius, r, and height, h, is given by A = 2π r² + 2π rh. If the height of the cylinder is 4 feet, express the radius as a function of V and find the radius if the surface area is 200 square feet. 65. The volume of a right circular cone, V, in terms of its radius, r, and its height, h, is given by V =  1/3 π r 2h. Express r in terms of h if the height of the cone is 12 feet and find the radius of a cone with volume of 50 cubic inches. 66. Consider a cone with height of 30 feet. Express the radius, r, in terms of the volume, V, and find the radius of a cone with volume of 1000 cubic feet.

Learning Objectives
In this section, you will:
• Solve direct variation problems.
• Solve inverse variation problems.
• Solve problems involving joint variation.

## 3.9 Modeling Using Variation

---
A used-car company has just offered their best candidate, Nicole, a position in sales. The position offers 16% commission on her sales. Her earnings depend on the amount of her sales. For instance, if she sells a vehicle for $4,600, she will earn $736. She wants to evaluate the offer, but she is not sure how. In this section, we will look at relationships, such as this one, between earnings, sales, and commission rate. Solving Direct Variation Problems In the example above, Nicole’s earnings can be found by multiplying her sales by her commission. The formula e = 0.16s tells us her earnings, e, come from the product of 0.16, her commission, and the sale price of the vehicle. If we create a table, we observe that as the sales price increases, the earnings increase as well, which should be intuitive. See Table 1. s, sales prices Interpretation A sale of a $4,600 vehicle results in $736 earnings. A sale of a $9,200 vehicle results in $1472 earnings. A sale of a $18,400 vehicle results in $2944 earnings. Notice that earnings are a multiple of sales. As sales increase, earnings increase in a predictable way. Double the sales of the vehicle from $4,600 to $9,200, and we double the earnings from $736 to $1,472. As the input increases, the output increases as a multiple of the input. A relationship in which one quantity is a constant multiplied by another quantity is called direct variation. Each variable in this type of relationship varies directly with the other. car. The formula y = kxn is used for direct variation. The value k is a nonzero constant greater than zero and is called the constant of variation. In this case, k = 0.16 and n = 1. s, Sales Prices in Dollars e, Earnings, $

direct variation If x and y are related by an equation of the form y = kx n then we say that the relationship is direct variation and y varies directly with the nth power of x. In direct variation relationships, there is a nonzero constant ratio k =  (y)/(x)n , where k is called the constant of variation, which help defines the relationship between the variables.

---
### 💡 **How To…**
Given a description of a direct variation problem, solve for an unknown. 1. Identify the input, x, and the output, y. 2. Determine the constant of variation. You may need to divide y by the specified power of x to determine the constant of variation. 3. Use the constant of variation to write an equation for the relationship. 4. Substitute known values into the equation to find the unknown.

---
### 📐 **Example  1**: Solving a Direct Variation Problem

The quantity y varies directly with the cube of x. If y = 25 when x = 2, find y when x is 6.

**Solution**

The general formula for direct variation with a cube is y = kx 3. The constant can be found by dividing y by the cube of x.

k =  (y)/(x)³ 

=  25/23 

=  25/8  Now use the constant to write an equation that represents this relationship.

y =  25/8 x³ Substitute x = 6 and solve for y.

y =  25 __

= 675 Analysis The graph of this equation is a simple cubic, as shown in Figure 2. y x

Do the graphs of all direct variation equations look like Example 1? No. Direct variation equations are power functions—they may be linear, quadratic, cubic, quartic, radical, etc. But all of the graphs pass through (0,0).

---
### ✏️ **Try It #1**
The quantity y varies directly with the square of x. If y = 24 when x = 3, find y when x is 4. Solving Inverse Variation Problems Water temperature in an ocean varies inversely to the water’s depth. Between the depths of 250 feet and 500 feet, the formula ______ d  gives us the temperature in degrees Fahrenheit at a depth in feet below Earth’s surface. Consider the Atlantic Ocean, which covers 22% of Earth’s surface. At a certain location, at the depth of 500 feet, the temperature may be 28°F. If we create Table 2, we observe that, as the depth increases, the water temperature decreases. d, dept(h)/(d)  Interpretatio(n)/(A)t a depth of 500 ft, the water temperature is 28° F. _ At a depth of 350 ft, the water temperature is 40° F. _ At a depth of 250 ft, the water temperature is 56° F. We notice in the relationship between these variables that, as one quantity increases, the other decreases. The two quantities are said to be inversely proportional and each term varies inversely with the other. Inversely proportional relationships are also called inverse variations. For our example, Figure 3 depicts the inverse variation. We say the water temperature varies inversely with the depth of the water because, as the depth increases, the temperature decreases. The formula y =  (k)/(x)  for inverse variation in this case uses k = 14,000. Depth, d (f) Temperature, T (°Fahrenheit) inverse variation If x and y are related by an equation of the form y =  (k)/(x)n  where k is a nonzero constant, then we say that y varies inversely with the nth power of x. In inversely proportional relationships, or inverse variations, there is a constant multiple k = xny.

---
### 📐 **Example  2**: Writing a Formula for an Inversely Proportional Relationship

A tourist plans to drive 100 miles. Find a formula for the time the trip will take as a function of the speed the tourist drives.

**Solution**

Recall that multiplying speed by time gives distance. If we let t represent the drive time in hours, and v represent the velocity (speed or rate) at which the tourist drives, then vt = distance. Because the distance is fixed at 100 miles, vt = 100. Solving this relationship for the time gives us our function.

t(v) =  100 ___ v 

We can see that the constant of variation is 100 and, although we can write the relationship using the negative exponent, it is more common to see it written as a fraction.

---
### 💡 **How To…**
Given a description of an indirect variation problem, solve for an unknown. 1. Identify the input, x, and the output, y. 2. Determine the constant of variation. You may need to multiply y by the specified power of x to determine the constant of variation. 3. Use the constant of variation to write an equation for the relationship. 4. Substitute known values into the equation to find the unknown.

---
### 📐 **Example  3**: Solving an Inverse Variation Problem

A quantity y varies inversely with the cube of x. If y = 25 when x = 2, find y when x is 6.

**Solution**

The general formula for inverse variation with a cube is y =  (k)/(x)³ . The constant can be found by multiplying y by the cube of x.

k = x³ y

= 200 Now we use the constant to write an equation that represents this relationship. y =  (k)/(y) =  200 ___ x³  Substitute x = 6 and solve for y.

y =  200 ___ 63 

=  25/27  Analysis The graph of this equation is a rational function, as shown in Figure 4. y x

---
### ✏️ **Try It #2**
A quantity y varies inversely with the square of x. If y = 8 when x = 3, find y when x is 4.

### Solving Problems Involving Joint Variation

Many situations are more complicated than a basic direct variation or inverse variation model. One variable often depends on multiple other variables. When a variable is dependent on the product or quotient of two or more variables, this is called joint variation. For example, the cost of busing students for each school trip varies with the number of students attending and the distance from the school. The variable c, cost, varies jointly with the number of students, n, and the distance, d. joint variation Joint variation occurs when a variable varies directly or inversely with multiple variables. For instance, if x varies directly with both y and z, we have x = kyz. If x varies directly with y and inversely with z, we have x =  k(y)/(z) . Notice that we only use one constant in a joint variation equation.

---
### 📐 **Example  4**: Solving Problems Involving Joint Variation

A quantity x varies directly with the square of y and inversely with the cube root of z. If x = 6 when y = 2 and z = 8, find x when y = 1 and z = 27.

**Solution**

Begin by writing an equation to show the relationship between the variables.

x =  ky²

_  √— z   Substitute x = 6, y = 2, and z = 8 to find the value of the constant k.

6 =  k²2 _  √8  

6 =  4k/2 

3 = k Now we can substitute the value of the constant into the equation for the relationship.

x =  3y²

_  √— z   To find x when y = 1 and z = 27, we will substitute values for y and z into our equation.

x =  3(1)² _  √27  

= 1

---
### ✏️ **Try It #3**
x varies directly with the square of y and inversely with z. If x = 40 when y = 4 and z = 2, find x when y = 10 and Access these online resources for additional instruction and practice with direct and inverse variation. • Direct Variation (http://openstaxcollege.org/l/directvariation) • Inverse Variation (http://openstaxcollege.org/l/inversevariatio) • Direct and Inverse Variation (http://openstaxcollege.org/l/directinverse)

## 3.9 Section Exercises

---
### 3.9 section EXERCISES

Verbal 1. What is true of the appearance of graphs that reflect a direct variation between two variables? 2. If two variables vary inversely, what will an equation representing their relationship look like? 3. Is there a limit to the number of variables that can jointly vary? Explain. Algebraic For the following exercises, write an equation describing the relationship of the given variables. 4. y varies directly as x and when x = 6, y = 12. 5. y varies directly as the square of x and when x = 4, y = 80. 6. y varies directly as the square root of x and when 7. y varies directly as the cube of x and when x = 36, y = 24. 8. y varies directly as the cube root of x and when 9. y varies directly as the fourth power of x and when x = 1, y = 6. 10. y varies inversely as x and when x = 4, y = 2. 11. y varies inversely as the square of x and when x = 3, y = 2. 12. y varies inversely as the cube of x and when x = 2, y = 5. 13. y varies inversely as the fourth power of x and when x = 3, y = 1. 14. y varies inversely as the square root of x and when x = 25, y = 3. 15. y varies inversely as the cube root of x and when 16. y varies jointly with x and z and when x = 2 and 17. y varies jointly as x, z, and w and when x = 1, z = 2, w = 5, then y = 100. 18. y varies jointly as the square of x and the square of z and when x = 3 and z = 4, then y = 72. 19. y varies jointly as x and the square root of z and when x = 2 and z = 25, then y = 100. 20. y varies jointly as the square of x the cube of z and the square root of w. When x = 1, z = 2, and w = 36, then y = 48. 21. y varies jointly as x and z and inversely as w. When x = 3, z = 5, and w = 6, then y = 10. 22. y varies jointly as the square of x and the square root of z and inversely as the cube of w. When x = 3, z = 4, and w = 3, then y = 6. 23. y varies jointly as x and z and inversely as the square root of w and the square of t. When x = 3, z = 1, w = 25, and t = 2, then y = 6. Numeric For the following exercises, use the given information to find the unknown value. 24. y varies directly as x. When x = 3, then y = 12. Find y when x = 20. 25. y varies directly as the square of x. When x = 2, then y = 16. Find y when x = 8. 26. y varies directly as the cube of x. When x = 3, then y = 5. Find y when x = 4. 27. y varies directly as the square root of x. When x = 16, then y = 4. Find y when x = 36. 28. y varies directly as the cube root of x. When x = 125, then y = 15. Find y when x = 1,000. 29. y varies inversely with x. When x = 3, then y = 2. Find y when x = 1. 30. y varies inversely with the square of x. When x = 4, then y = 3. Find y when x = 2. 31. y varies inversely with the cube of x. When x = 3, then y = 1. Find y when x = 1. 32. y varies inversely with the square root of x. When x = 64, then y = 12. Find y when x = 36. 33. y varies inversely with the cube root of x. When x = 27, then y = 5. Find y when x = 125. 34. y varies jointly as x and z. When x = 4 and z = 2, then y = 16. Find y when x = 3 and z = 3. 35. y varies jointly as x, z, and w. When x = 2, z = 1, and w = 12, then y = 72. Find y when x = 1, z = 2, and w = 3. 36. y varies jointly as x and the square of z. When x = 2 and z = 4, then y = 144. Find y when x = 4 and z = 5. 37. y varies jointly as the square of x and the square root of z. When x = 2 and z = 9, then y = 24. Find y when x = 3 and z = 25. 38. y varies jointly as x and z and inversely as w. When x = 5, z = 2, and w = 20, then y = 4. Find y when x = 3 and z = 8, and w = 48. 39. y varies jointly as the square of x and the cube of z and inversely as the square root of w. When x = 2, z = 2, and w = 64, then y = 12. Find y when x = 1, z = 3, and w = 4.

40. y varies jointly as the square of x and of z and inversely as the square root of w and of t. When x = 2, z = 3, w = 16, and t = 3, then y = 1. Find y when x = 3, z = 2, w = 36, and t = 5. Technology For the following exercises, use a calculator to graph the equation implied by the given variation. 41. y varies directly with the square of x and when x = 2, y = 3. 42. y varies directly as the cube of x and when x = 2, y = 4. 43. y varies directly as the square root of x and when 44. y varies inversely with x and when x = 6, y = 2. 45. y varies inversely as the square of x and when x = 1, y = 4. Extensions For the following exercises, use Kepler’s Law, which states that the square of the time, T, required for a planet to orbit the Sun varies directly with the cube of the mean distance, a, that the planet is from the Sun. 46. Using the Earth’s time of 1 year and mean distance of 93 million miles, find the equation relating T and a. 47. Use the result from the previous exercise to determine the time required for Mars to orbit the Sun if its mean distance is 142 million miles. 48. Using Earth’s distance of 150 million kilometers, find the equation relating T and a. 49. Use the result from the previous exercise to determine the time required for Venus to orbit the Sun if its mean distance is 108 million kilometers. 50. Using Earth’s distance of 1 astronomical unit (A.U.), determine the time for Saturn to orbit the Sun if its mean distance is 9.54 A.U. Real-World Applications For the following exercises, use the given information to answer the questions. 51. The distance s that an object falls varies directly with the square of the time, t, of the fall. If an object falls 16 feet in one second, how long for it to fall 144 feet? 52. The velocity v of a falling object varies directly to the time, t, of the fall. If after 2 seconds, the velocity of the object is 64 feet per second, what is the velocity after 5 seconds? 53. The rate of vibration of a string under constant tension varies inversely with the length of the string. If a string is 24 inches long and vibrates 128 times per second, what is the length of a string that vibrates 64 times per second? 54. The volume of a gas held at constant temperature varies indirectly as the pressure of the gas. If the volume of a gas is 1200 cubic centimeters when the pressure is 200 millimeters of mercury, what is the volume when the pressure is 300 millimeters of mercury? 55. The weight of an object above the surface of the Earth varies inversely with the square of the distance from the center of the Earth. If a body weighs 50 pounds when it is 3960 miles from Earth’s center, what would it weigh it were 3970 miles from Earth’s center? 56. The intensity of light measured in foot-candles varies inversely with the square of the distance from the light source. Suppose the intensity of a light bulb is 0.08 foot- candles at a distance of 3 meters. Find the intensity level at 8 meters. 57. The current in a circuit varies inversely with its resistance measured in ohms. When the current in a circuit is 40 amperes, the resistance is 10 ohms. Find the current if the resistance is 12 ohms. 58. The force exerted by the wind on a plane surface varies jointly with the square of the velocity of the wind and with the area of the plane surface. If the area of the surface is 40 square feet surface and the wind velocity is 20 miles per hour, the resulting force is 15 pounds. Find the force on a surface of 65 square feet with a velocity of 30 miles per hour. 59. The horsepower (hp) that a shaft can safely transmit varies jointly with its speed (in revolutions per minute (rpm)) and the cube of the diameter. If the shaft of a certain material 3 inches in diameter can transmit 45 hp at 100 rpm, what must the diameter be in order to transmit 60 hp at 150 rpm? 60. The kinetic energy K of a moving object varies jointly with its mass m and the square of its velocity v. If an object weighing 40 kilograms with a velocity of 15 meters per second has a kinetic energy of 1000 joules, find the kinetic energy if the velocity is increased to 20 meters per second.

### Key Terms

arrow notation a way to symbolically represent the local and end behavior of a function by using arrows to indicate that an input or output approaches a value axis of symmetry a vertical line drawn through the vertex of a parabola around which the parabola is symmetric; it is defined by x = -  b/2a . coefficient a nonzero real number multiplied by a variable raised to an exponent complex conjugate the complex number in which the sign of the imaginary part is changed and the real part of the number is left unchanged; when added to or multiplied by the original complex number, the result is a real number complex number the sum of a real number and an imaginary number, written in the standard form a + bi, where a is the real part, and bi is the imaginary part complex plane a coordinate system in which the horizontal axis is used to represent the real part of a complex number and the vertical axis is used to represent the imaginary part of a complex number constant of variation the non-zero value k that helps define the relationship between variables in direct or inverse variation continuous function a function whose graph can be drawn without lifting the pen from the paper because there are no breaks in the graph degree the highest power of the variable that occurs in a polynomial Descartes’ Rule of Signs a rule that determines the maximum possible numbers of positive and negative real zeros based on the number of sign changes of f (x) and f (-x) direct variation the relationship between two variables that are a constant multiple of each other; as one quantity increases, so does the other Division Algorithm given a polynomial dividend f (x) and a non-zero polynomial divisor d(x) where the degree of d(x) is less than or equal to the degree of f (x), there exist unique polynomials q(x) and r(x) such that f (x) = d(x) q(x) + r(x) where q(x) is the quotient and r(x) is the remainder. The remainder is either equal to zero or has degree strictly less than d(x). end behavior the behavior of the graph of a function as the input decreases without bound and increases without bound Factor Theorem k is a zero of polynomial function f (x) if and only if (x - k) is a factor of f (x) Fundamental Theorem of Algebra a polynomial function with degree greater than 0 has at least one complex zero general form of a quadratic function the function that describes a parabola, written in the form f (x) = ax 2 + bx + c, where a, b, and c are real numbers and a ≠  0. global maximum highest turning point on a graph; f (a) where f (a) ≥  f (x) for all x. global minimum lowest turning point on a graph; f (a) where f (a) ≤  f (x) for all x. horizontal asymptote a horizontal line y = b where the graph approaches the line as the inputs increase or decrease without bound. Intermediate Value Theorem for two numbers a and b in the domain of f, if a < b and f (a) ≠  f (b), then the function f takes on every value between f (a) and f (b); specifically, when a polynomial function changes from a negative value to a positive value, the function must cross the x-axis inverse variation the relationship between two variables in which the product of the variables is a constant inversely proportional a relationship where one quantity is a constant divided by the other quantity; as one quantity increases, the other decreases invertible function any function that has an inverse function imaginary number a number in the form bi where i = √-1  joint variation a relationship where a variable varies directly or inversely with multiple variables leading coefficient the coefficient of the leading term

leading term the term containing the highest power of the variable Linear Factorization Theorem allowing for multiplicities, a polynomial function will have the same number of factors as its degree, and each factor will be in the form (x - c), where c is a complex number multiplicity the number of times a given factor appears in the factored form of the equation of a polynomial; if a polynomial contains a factor of the form (x - h)p, x = h is a zero of multiplicity p. polynomial function a function that consists of either zero or the sum of a finite number of non-zero terms, each of which is a product of a number, called the coefficient of the term, and a variable raised to a non-negative integer power. power function a function that can be represented in the form f (x) = kxp where k is a constant, the base is a variable, and the exponent, p, is a constant rational function a function that can be written as the ratio of two polynomials Rational Zero Theorem the possible rational zeros of a polynomial function have the form  (p)/(q)  where p is a factor of the constant term and q is a factor of the leading coefficient. Remainder Theorem if a polynomial f (x) is divided by x - k, then the remainder is equal to the value f (k) removable discontinuity a single point at which a function is undefined that, if filled in, would make the function continuous; it appears as a hole on the graph of a function smooth curve a graph with no sharp corners standard form of a quadratic function the function that describes a parabola, written in the form f (x) = a(x - h)² + k, where (h, k) is the vertex. synthetic division a shortcut method that can be used to divide a polynomial by a binomial of the form x - k term of a polynomial function any aixi of a polynomial function in the form f (x) = anxn + ... + a²x² + a¹x + a⁰ turning point the location at which the graph of a function changes direction varies directly a relationship where one quantity is a constant multiplied by the other quantity varies inversely a relationship where one quantity is a constant divided by the other quantity vertex the point at which a parabola changes direction, corresponding to the minimum or maximum value of the quadratic function vertex form of a quadratic function another name for the standard form of a quadratic function vertical asymptote a vertical line x = a where the graph tends toward positive or negative infinity as the inputs approach a zeros in a given function, the values of x at which y = 0, also called roots Key Equations general form of a quadratic function f (x) = ax 2 + bx + c the quadratic formula x =  -b ±  √b² - 4ac 

_______________ 2a  standard form of a quadratic function f (x) = a(x - h)² + k general form of a polynomial function f (x) = an xn + ... + a² x² + a¹x + a⁰ Division Algorithm f (x) = d(x)q(x) + r(x) where q(x) ≠  0 Rational Function f (x) =  P(x) ____ Q(x)  =  ap x p + ap - 1x

p-1 + ... + a¹x + a⁰

___

bq x q + bq - 1 x q-1 + ... + b¹ x + b⁰ , Q(x) ≠  0 Direct variation y = kx n, k is a nonzero constant. Inverse variation y =  (k)/(x)n , k is a nonzero constant.

### Key Concepts

• The square root of any negative number can be written as a multiple of i. See Example 1. • To plot a complex number, we use two number lines, crossed to form the complex plane. The horizontal axis is the real axis, and the vertical axis is the imaginary axis. See Example 2. • Complex numbers can be added and subtracted by combining the real parts and combining the imaginary parts. See Example 3. • Complex numbers can be multiplied and divided. • To multiply complex numbers, distribute just as with polynomials. See Example 4, Example 5, and Example 8. • To divide complex numbers, multiply both the numerator and denominator by the complex conjugate of the denominator to eliminate the complex number from the denominator. See Example 6, Example 7, and Example 9. • The powers of i are cyclic, repeating every fourth one. See Example 10. 3.2 Quadratic Functions • A polynomial function of degree two is called a quadratic function. • The graph of a quadratic function is a parabola. A parabola is a U-shaped curve that can open either up or down. • The axis of symmetry is the vertical line passing through the vertex. The zeros, or x-intercepts, are the points at which the parabola crosses the x-axis. The y-intercept is the point at which the parabola crosses the y-axis. See Example 1,

**Example 7** — , and Example 8.
• Quadratic functions are often written in general form. Standard or vertex form is useful to easily identify the vertex of a parabola. Either form can be written from a graph. See Example 2. • The vertex can be found from an equation representing a quadratic function. See Example 3. • The domain of a quadratic function is all real numbers. The range varies with the function. See Example 4. • A quadratic function’s minimum or maximum value is given by the y-value of the vertex. • The minimum or maximum value of a quadratic function can be used to determine the range of the function and to solve many kinds of real-world problems, including problems involving area and revenue. See Example 5 and

**Example 6** — .
• Some quadratic equations must be solved by using the quadratic formula. See Example 9. • The vertex and the intercepts can be identified and interpreted to solve real-world problems. See Example 10. 3.3 Power Functions and Polynomial Functions • A power function is a variable base raised to a number power. See Example 1. • The behavior of a graph as the input decreases beyond bound and increases beyond bound is called the end behavior. • The end behavior depends on whether the power is even or odd. See Example 2 and Example 3. • A polynomial function is the sum of terms, each of which consists of a transformed power function with positive whole number power. See Example 4. • The degree of a polynomial function is the highest power of the variable that occurs in a polynomial. The term containing the highest power of the variable is called the leading term. The coefficient of the leading term is called the leading coefficient. See Example 5. • The end behavior of a polynomial function is the same as the end behavior of the power function represented by the leading term of the function. See Example 6 and Example 7. • A polynomial of degree n will have at most n x-intercepts and at most n - 1 turning points. See Example 8,

**Example 9** — , Example 10, Example 11, and Example 12.

• Polynomial functions of degree 2 or more are smooth, continuous functions. See Example 1. • To find the zeros of a polynomial function, if it can be factored, factor the function and set each factor equal to zero. See Example 2, Example 3, and Example 4. • Another way to find the x-intercepts of a polynomial function is to graph the function and identify the points at which the graph crosses the x-axis. See Example 5. • The multiplicity of a zero determines how the graph behaves at the x-intercepts. See Example 6. • The graph of a polynomial will cross the horizontal axis at a zero with odd multiplicity. • The graph of a polynomial will touch the horizontal axis at a zero with even multiplicity. • The end behavior of a polynomial function depends on the leading term. • The graph of a polynomial function changes direction at its turning points. • A polynomial function of degree n has at most n - 1 turning points. See Example 7. • To graph polynomial functions, find the zeros and their multiplicities, determine the end behavior, and ensure that the final graph has at most n - 1 turning points. See Example 8 and Example 10. • Graphing a polynomial function helps to estimate local and global extremas. See Example 11. • The Intermediate Value Theorem tells us that if f (a) and f (b) have opposite signs, then there exists at least one value c between a and b for which f (c) = 0. See Example 9. 3.5 Dividing Polynomials • Polynomial long division can be used to divide a polynomial by any polynomial with equal or lower degree. See

**Example 1** — and Example 2.
• The Division Algorithm tells us that a polynomial dividend can be written as the product of the divisor and the quotient added to the remainder. • Synthetic division is a shortcut that can be used to divide a polynomial by a binomial in the form x - k. See Example 3,

**Example 4** — , and Example 5.
• Polynomial division can be used to solve application problems, including area and volume. See Example 6. 3.6 Zeros of Polynomial Functions • To find f (k), determine the remainder of the polynomial f (x) when it is divided by x - k. See Example 1. • k is a zero of f (x) if and only if (x - k) is a factor of f (x). See Example 2. • Each rational zero of a polynomial function with integer coefficients will be equal to a factor of the constant term divided by a factor of the leading coefficient. See Example 3 and Example 4. • When the leading coefficient is 1, the possible rational zeros are the factors of the constant term. • Synthetic division can be used to find the zeros of a polynomial function. See Example 5. • According to the Fundamental Theorem, every polynomial function has at least one complex zero. See Example 6. • Every polynomial function with degree greater than 0 has at least one complex zero. • Allowing for multiplicities, a polynomial function will have the same number of factors as its degree. Each factor will be in the form (x - c), where c is a complex number. See Example 7. • The number of positive real zeros of a polynomial function is either the number of sign changes of the function or less than the number of sign changes by an even integer. • The number of negative real zeros of a polynomial function is either the number of sign changes of f (-x) or less than the number of sign changes by an even integer. See Example 8. • Polynomial equations model many real-world scenarios. Solving the equations is easiest done by synthetic division. See Example 9.

• We can use arrow notation to describe local behavior and end behavior of the toolkit functions f (x) =  1/x  and f (x) =  1/x² . See Example 1. • A function that levels off at a horizontal value has a horizontal asymptote. A function can have more than one vertical asymptote. See Example 2. • Application problems involving rates and concentrations often involve rational functions. See Example 3. • The domain of a rational function includes all real numbers except those that cause the denominator to equal zero. See Example 4. • The vertical asymptotes of a rational function will occur where the denominator of the function is equal to zero and the numerator is not zero. See Example 5. • A removable discontinuity might occur in the graph of a rational function if an input causes both numerator and denominator to be zero. See Example 6. • A rational function’s end behavior will mirror that of the ratio of the leading terms of the numerator and denominator functions. See Example 7, Example 8, Example 9, and Example 10. • Graph rational functions by finding the intercepts, behavior at the intercepts and asymptotes, and end behavior. See

**Example 11** — .
• If a rational function has x-intercepts at x = x¹, x², ..., xn, vertical asymptotes at x = v¹, v², ..., vm, and no xi = any vj, then the function can be written in the form f (x) = a  (x - x¹)p 1(x - x²)p 2...(x - xn)p n

___

(x - v¹)q 1(x - v²)q 2...(x - vm)q n  See Example 12. 3.8 Inverses and Radical Functions • The inverse of a quadratic function is a square root function. • If f -l is the inverse of a function f, then f is the inverse of the function f -l. See Example 1. • While it is not possible to find an inverse of most polynomial functions, some basic polynomials are invertible. See

**Example 2** — .
• To find the inverse of certain functions, we must restrict the function to a domain on which it will be one-to-one. See Example 3 and Example 4. • When finding the inverse of a radical function, we need a restriction on the domain of the answer. See Example 5 and Example 7. • Inverse and radical and functions can be used to solve application problems. See Example 6 and Example 8. 3.9 Modeling Using Variation • A relationship where one quantity is a constant multiplied by another quantity is called direct variation. See Example 1. • Two variables that are directly proportional to one another will have a constant ratio. • A relationship where one quantity is a constant divided by another quantity is called inverse variation. See Example 2. • Two variables that are inversely proportional to one another will have a constant multiple. See Example 3. • In many problems, a variable varies directly or inversely with multiple variables. We call this type of relationship joint variation. See Example 4.

You have reached the end of Chapter 3: Polynomial and Rational Functions. Let’s review some of the Key Terms, Concepts and Equations you have learned. Complex Numbers Perform the indicated operation with complex numbers. 1. (4 + 3i) + (-2 - 5i) 2. (6 - 5i) - (10 + 3i) 3. (2 - 3i)(3 + 6i) 4.  2 - i _____ 2 + i  Solve the following equations over the complex number system. 5. x² - 4x + 5 = 0 Quadratic Functions For the following exercises, write the quadratic function in standard form. Then, give the vertex and axes intercepts. Finally, graph the function. 7. f (x) = x² - 4x - 5 8. f (x) = -2x² - 4x For the following problems, find the equation of the quadratic function using the given information. 9. The vertex is (-2, 3) and a point on the graph is (3, 6). 10. The vertex is (-3, 6.5) and a point on the graph is Answer the following questions. 11. A rectangular plot of land is to be enclosed by fencing. One side is along a river and so needs no fence. If the total fencing available is 600 meters, find the dimensions of the plot to have maximum area. 12. An object projected from the ground at a 45 degree angle with initial velocity of 120 feet per second has height, h, in terms of horizontal distance traveled, x, given by h(x) =  -32 _____ (120)²  x² + x. Find the maximum height the object attains. Power Functions and Polynomial Functions For the following exercises, determine if the function is a polynomial function and, if so, give the degree and leading coefficient. 13. f (x) = 4x⁵ - 3x³ + 2x - 1 14. f (x) = 5x + 1 - x² 15. f (x) = x²(3 - 6x + x²) For the following exercises, determine end behavior of the polynomial function. 16. f (x) = 2x⁴ + 3x³ - 5x² + 7 17. f (x) = 4x³ - 6x² + 2 18. f (x) = 2x²(1 + 3x - x²) Graphs of Polynomial Functions For the following exercises, find all zeros of the polynomial function, noting multiplicities. 19. f (x) = (x + 3)²(2x - 1)(x + 1)³ 20. f (x) = x⁵ + 4x⁴ + 4x³ 21. f (x) = x³ - 4x² + x - 4

For the following exercises, based on the given graph, determine the zeros of the function and note multiplicity. x y x y 24. Use the Intermediate Value Theorem to show that at least one zero lies between 2 and 3 for the function f (x) = x³ - 5x + 1 Dividing Polynomials For the following exercises, use long division to find the quotient and remainder. 25.  x³ - 2x² + 4x + 4

______________

x - 2 

_______________

x + 1  For the following exercises, use synthetic division to find the quotient. If the divisor is a factor, then write the factored form. 27.  x³ - 2x² + 5x - 1

______________ x + 3  __________ x - 3 

_________________

x + 4 

_______________

x + 1  Zeros of Polynomial Functions For the following exercises, use the Rational Zero Theorem to help you solve the polynomial equation. For the following exercises, use Descartes’ Rule of Signs to find the possible number of positive and negative solutions. Rational Functions For the following rational functions, find the intercepts and the vertical and horizontal asymptotes, and then use them to sketch a graph. 37. f (x) =  x + 2 _____ x - 5  38. f (x) =  x² + 1 _____ x² - 4  39. f (x) =  3x² - 27 ________ x² + x - 2  40. f (x) =  x + 2 _____ x² - 9 

For the following exercises, find the slant asymptote. 41. f (x) =  x² - 1 _____ x + 2  42. f (x) =  2x³ - x² + 4 __________ x² + 1  Inverses and Radical Functions For the following exercises, find the inverse of the function with the domain given. 43. f (x) = (x - 2)², x ≥  2 44. f (x) = (x + 4)² - 3, x ≥  -4 45. f (x) = x² + 6x - 2, x ≥  -3 46. f (x) = 2x³ - 3 47. f (x) = √4x + 5  - 3 48. f (x) =  x - 3 _____ 2x + 1  Modeling Using Variation For the following exercises, find the unknown value. 49. y varies directly as the square of x. If when x = 3, y = 36, find y if x = 4. 50. y varies inversely as the square root of x. If when x = 25, y = 2, find y if x = 4. 51. y varies jointly as the cube of x and as z. If when x = 1 and z = 2, y = 6, find y if x = 2 and z = 3. 52. y varies jointly as x and the square of z and inversely as the cube of w. If when x = 3, z = 4, and w = 2, y = 48, find y if x = 4, z = 5, and w = 3. For the following exercises, solve the application problem. 53. The weight of an object above the surface of the earth varies inversely with the distance from the center of the earth.If a person weighs 150 pounds when he is on the surface of the earth (3,960 miles from center), find the weight of the person if he is 20 miles above the surface. 54. The volume V of an ideal gas varies directly with the temperature T and inversely with the pressure P. A cylinder contains oxygen at a temperature of 310 degrees K and a pressure of 18 atmospheres in a volume of 120 liters. Find the pressure if the volume is decreased to 100 liters and the temperature is increased to 320 degrees K.

Perform the indicated operation or solve the equation. 1. (3 - 4i)(4 + 2i) _____ 3 + 4i  Give the degree and leading coefficient of the following polynomial function. 4. f (x) = x³(3 - 6x² - 2x²) Determine the end behavior of the polynomial function. 5. f (x) = 8x³ - 3x² + 2x - 4 6. f (x) = -2x²(4 - 3x - 5x²) Write the quadratic function in standard form. Determine the vertex and axes intercepts and graph the function. 7. f (x) = x² + 2x - 8 Given information about the graph of a quadratic function, find its equation. 8. Vertex (2, 0) and point on graph (4, 12). Solve the following application problem. 9. A rectangular field is to be enclosed by fencing. In addition to the enclosing fence, another fence is to divide the field into two parts, running parallel to two sides. If 1,200 feet of fencing is available, find the maximum area that can be enclosed. Find all zeros of the following polynomial functions, noting multiplicities. 10. f (x) = (x - 3)³(3x - 1)(x - 1)² Based on the graph, determine the zeros of the function and multiplicities. x y Use long division to find the quotient. __________ x + 2  Use synthetic division to find the quotient. If the divisor is a factor, write the factored form. __________ x - 2 

________________

x + 3 

Use the Rational Zero Theorem to help you find the zeros of the polynomial functions. 16. f (x) = 2x³ + 5x² - 6x - 9 17. f (x) = 4x⁴ + 8x³ + 21x² + 17x + 4 19. f (x) = x⁵ + 6x⁴ + 13x³ + 14x² + 12x + 8 Given the following information about a polynomial function, find the function. 20. It has a double zero at x = 3 and zeroes at x = 1 and x = -2. Its y-intercept is (0, 12). 21. It has a zero of multiplicity 3 at x =  1/2  and another zero at x = -3. It contains the point (1, 8). Use Descartes’ Rule of Signs to determine the possible number of positive and negative solutions. For the following rational functions, find the intercepts and horizontal and vertical asymptotes, and sketch a graph. 23. f (x) =  x + 4 _________ x² - 2x - 3  24. f (x) =  x² + 2x - 3 _________ x² - 4  Find the slant asymptote of the rational function. 25. f (x) =  x² + 3x - 3 _________ x - 1  Find the inverse of the function. 26. f (x) = √x - 2  + 4 27. f (x) = 3x³ - 4 28. f (x) =  2x + 3 ______ 3x - 1  Find the unknown value. 29. y varies inversely as the square of x and when x = 3, y = 2. Find y if x = 1. 30. y varies jointly with x and the cube root of z. If when x = 2 and z = 27, y = 12, find y if x = 5 and z = 8. Solve the following application problem. 31. The distance a body falls varies directly as the square of the time it falls. If an object falls 64 feet in 2 seconds, how long will it take to fall 256 feet?
