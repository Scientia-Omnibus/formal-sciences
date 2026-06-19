# Systems of Equations and Inequalities

## 9.8 Solving Systems with Cramer's Rule

---
We have learned how to solve systems of equations in two variables and three variables, and by multiple methods: substitution, addition, Gaussian elimination, using the inverse of a matrix, and graphing. Some of these methods are easier to apply than others and are more appropriate in certain situations. In this section, we will study two more strategies for solving systems of equations. Evaluating the Determinant of a 2 ×  2 Matrix A determinant is a real number that can be very useful in mathematics because it has multiple applications, such as calculating area, volume, and other quantities. Here, we will use determinants to reveal whether a matrix is invertible by using the entries of a square matrix to determine whether there is a solution to the system of equations. Perhaps one of the more interesting applications, however, is their use in cryptography. Secure signals or messages are sometimes sent encoded in a matrix. The data can only be decrypted with an invertible matrix and the determinant. For our purposes, we focus on the determinant as an indication of the invertibility of the matrix. Calculating the determinant of a matrix involves following the specific patterns that are outlined in this section. find the determinant of a 2 ×  2 matrix The determinant of a 2 ×  2 matrix, given

A = [ a b

c d ]  is defined as

det(A) = ∣ a b

c d ∣ = ad - cb Notice the change in notation. There are several ways to indicate the determinant, including det(A) and replacing the brackets in a matrix with straight lines, ∣ A ∣.

---
### 📐 **Example  1**
Finding the Determinant of a 2 ×  2 Matrix Find the determinant of the given matrix. A = [  5 2

-6 3 ] 

**Solution**

det(A) = ∣  5 2

-6 3 ∣

= 5(3) - (-6)(2)

= 27 Using Cramer’s Rule to Solve a System of Two Equations in Two Variables We will now introduce a final method for solving systems of equations that uses determinants. Known as Cramer’s Rule, this technique dates back to the middle of the 18th century and is named for its innovator, the Swiss mathematician Gabriel Cramer (1704-1752), who introduced it in 1750 in Introduction à l'Analyse des lignes Courbes algébriques. Cramer’s Rule is a viable and efficient method for finding solutions to systems with an arbitrary number of unknowns, provided that we have the same number of equations as unknowns. Learning Objectives
In this section, you will:
• Evaluate 2 ×  2 determinants.
• Use Cramer’s Rule to solve a system of equations in two variables.
• Evaluate 3 ×  3 determinants.
• Use Cramer’s Rule to solve a system of three equations in three variables.
• Know the properties of determinants.
Cramer’s Rule will give us the unique solution to a system of equations, if it exists. However, if the system has no solution or an infinite number of solutions, this will be indicated by a determinant of zero. To find out if the system is inconsistent or dependent, another method, such as elimination, will have to be used. To understand Cramer’s Rule, let’s look closely at how we solve systems of linear equations using basic row operations. Consider a system of two equations in two variables.

a¹x + b¹ y = c¹ (1)

a²x + b² y = c² (2) We eliminate one variable using row operations and solve for the other. Say that we wish to solve for x. If equation (2) is multiplied by the opposite of the coefficient of y in equation (1), equation (1) is multiplied by the coefficient of y in equation (2), and we add the two equations, the variable y will be eliminated.

b² a¹x + b² b¹ y = b²c¹ Multiply R¹ by b²

-b¹ a²x - b¹b² y = -b¹c² Multiply R² by -b¹

b² a¹x - b¹ a²x = b²c¹ - b¹c² Now, solve for x.

b² a¹x - b¹ a²x = b²c¹ - b¹c²

x(b² a¹ - b¹ a²) = b²c¹ - b¹c²

x =  b²c¹ - b¹c² _ b²a¹ - b¹a²  =  [ c¹ b¹

c² b² ]  _ [ a¹ b¹

a² b² ]    Similarly, to solve for y, we will eliminate x.

a²a¹x + a²b¹ y = a²c¹ Multiply R¹ by a²

-a¹a²x -a¹b²y = -a¹c² Multiply R² by -a¹

a²b¹ y - a¹b² y = a²c¹ - a¹c² Solving for y gives

a²b¹ y - a¹b² y = a²c¹ - a¹c²

y(a²b¹ - a¹b²) = a²c¹ - a¹c²

y =  a²c¹ - a¹c² _ a²b¹ - a¹b²  =  a¹c² - a²c¹ _ a¹b² - a²b¹  =  [ a¹ c¹

a² c² ]  _ [ a¹ b¹

a² b² ]   Notice that the denominator for both x and y is the determinant of the coefficient matrix. We can use these formulas to solve for x and y, but Cramer’s Rule also introduces new notation: • D : determinant of the coefficient matrix • Dx : determinant of the numerator in the solution of x

x =  D(x)/(D)  • Dy : determinant of the numerator in the solution of y

y =  D(y)/(D)  The key to Cramer’s Rule is replacing the variable column of interest with the constant column and calculating the determinants. We can then express x and y as a quotient of two determinants.

Cramer’s Rule for 2 ×  2 systems Cramer’s Rule is a method that uses determinants to solve systems of equations that have the same number of equations as variables. Consider a system of two linear equations in two variables.

a¹x + b¹ y = c¹

a²x + b² y = c² The solution using Cramer’s Rule is given as x =  D(x)/(D)  =  [ c¹ b¹

c² b² ]  _ [ a¹ b¹

a² b² ]  , D ≠  0; y =  D(y)/(D)  =  [ a¹ c¹

a² c² ]  _ [ a¹ b¹

a² b² ]  , D ≠  0. If we are solving for x, the x column is replaced with the constant column. If we are solving for y, the y column is replaced with the constant column.

---
### 📐 **Example  2**
Using Cramer’s Rule to Solve a 2 ×  2 System Solve the following 2 ×  2 system using Cramer’s Rule.

2x - 3y = 13

**Solution**

Solve for x. x =  D(x)/(D)  =  ∣ 15 3

13 -3 ∣ _ ∣ 12 3

2 -3 ∣  =  -45 - 39 ________ -36 - 6  =  -84 ____ -42  = 2 Solve for y.

y =  D(y)/(D)  = 

2 13 ∣ _ ∣ 12 3

2 -3 ∣ ________ -36 - 6  = - 126 ___ 42  = -3 The solution is (2, -3).

---
### ✏️ **Try It #1**
Use Cramer’s Rule to solve the 2 ×  2 system of equations.

x + 2y = -11

-2x + y = -13 Evaluating the Determinant of a 3 ×  3 Matrix Finding the determinant of a 2 ×  2 matrix is straightforward, but finding the determinant of a 3 ×  3 matrix is more complicated. One method is to augment the 3 ×  3 matrix with a repetition of the first two columns, giving a 3 ×  5 matrix. Then we calculate the sum of the products of entries down each of the three diagonals (upper left to lower right), and subtract the products of entries up each of the three diagonals (lower left to upper right). This is more easily understood with a visual and an example. Find the determinant of the 3 ×  3 matrix.

A = [  a¹ b¹ c¹

a² b² c²

a³ b³ c³  ] 

1. Augment A with the first two columns.

det(A) = ∣  a¹ b¹ c¹

a² b² c²

a³ b³ c³  ∣     a¹ b¹

a² b²

a³ b³  ∣  2. From upper left to lower right: Multiply the entries down the first diagonal. Add the result to the product of entries down the second diagonal. Add this result to the product of the entries down the third diagonal. 3. From lower left to upper right: Subtract the product of entries up the first diagonal. From this result subtract the product of entries up the second diagonal. From this result, subtract the product of entries up the third diagonal.

det(A) = ∣  a¹ b¹ c¹

a² b² c²

a³ b³ c³  ∣     a¹ b¹

a² b²

a³ b³  ∣  The algebra is as follows:

∣ A ∣ = a¹ b² c³ + b¹ c² a³ + c¹ a² b³ - a³ b² c¹ - b³ c² a¹ - c³ a² b¹

---
### 📐 **Example  3**
Finding the Determinant of a 3 ×  3 Matrix Find the determinant of the 3 ×  3 matrix given

A = [ 

 ]

**Solution**

Augment the matrix with the first two columns and then follow the formula. Thus,

∣ A ∣ = ∣ 

 ∣    

3 -1

 ∣  = 0(-1)(1) + 2(1)(4) + 1(3)(0) - 4(-1)(1) - 0(1)(0) - 1(3)(2)

= 0 + 8 + 0 + 4 - 0 - 6

= 6

---
### ✏️ **Try It #2**
Find the determinant of the 3 ×  3 matrix. det(A) = ∣ 

 ∣  Can we use the same method to find the determinant of a larger matrix? No, this method only works for 2 ×  2 and 3 ×  3 matrices. For larger matrices it is best to use a graphing utility or computer software. Using Cramer’s Rule to Solve a System of Three Equations in Three Variables Now that we can find the determinant of a 3 ×  3 matrix, we can apply Cramer’s Rule to solve a system of three equations in three variables. Cramer’s Rule is straightforward, following a pattern consistent with Cramer’s Rule for 2 ×  2 matrices. As the order of the matrix increases to 3 ×  3, however, there are many more calculations required. When we calculate the determinant to be zero, Cramer’s Rule gives no indication as to whether the system has no solution or an infinite number of solutions. To find out, we have to perform elimination on the system.

Consider a 3 ×  3 system of equations.

a¹x + b¹ y + c¹z = d¹

a²x + b² y + c²z = d²

a³x + b³ y + c³z = d³ x =  D(x)/(D) , y =  D(y)/(D) , z =  D(z)/(D) , D ≠  0 where D = ∣  a¹ b¹ c¹

a² b² c²

a³ b³ c³  ∣ , Dx = ∣  d¹ b¹ c¹

d² b² c²

d³ b³ c³  ∣ , Dy = ∣  a¹ d¹ c¹

a² d² c²

a³ d³ c³  ∣ , Dz = ∣  a¹ b¹ d¹

a² b² d²

a³ b³ d³  ∣  If we are writing the determinant Dx, we replace the x column with the constant column. If we are writing the determinant Dy, we replace the y column with the constant column. If we are writing the determinant Dz, we replace the z column with the constant column. Always check the answer.

---
### 📐 **Example  4**: Solving a 3 ×  3 System Using Cramer’s Rule

Find the solution to the given 3 ×  3 system using Cramer’s Rule.

x + y - z = 6

3x - 2y + z = -5

x + 3y - 2z = 14

**Solution**

Use Cramer’s Rule. D = ∣  1 1 -1

3 -2 1

1 3 -2  ∣ , Dx = ∣  6 1 -1

-5 -2 1

14 3 -2  ∣ , Dy = ∣  1 6 -1

3 -5 1

 ∣ , Dz = ∣  1 1 6

3 -2 -5

 ∣  Then, x =  D(x)/(D)  =  -3 ___ -3  = 1

y =  D(y)/(D)  =  -9 ___ -3  = 3

z =  D(z)/(D)  =  6 ___ -3  = - 2 The solution is (1, 3, -2).

---
### ✏️ **Try It #3**
Use Cramer’s Rule to solve the 3 ×  3 matrix.

x - 3y + 7z = 13

x + y + z = 1

x - 2y + 3z = 4

---
### 📐 **Example  5**
Using Cramer’s Rule to Solve an Inconsistent System Solve the system of equations using Cramer’s Rule.

3x - 2y = 4 (1)

6x - 4y = 0 (2)

**Solution**

We begin by finding the determinants D, Dx, and Dy.

D = ∣ 3 -2

6 -4 ∣ = 3(-4) - 6(-2) = 0

We know that a determinant of zero means that either the system has no solution or it has an infinite number of solutions. To see which one, we use the process of elimination. Our goal is to eliminate one of the variables. 1. Multiply equation (1) by -2. 2. Add the result to equation (2).

-6x + 4y = -8

6x - 4y = 0

0 = -8 We obtain the equation 0 = -8, which is false. Therefore, the system has no solution. Graphing the system reveals two parallel lines. See Figure 1. x y y = 3 2 x - 2 y = 3 2 x

---
### 📐 **Example  6**
Use Cramer’s Rule to Solve a Dependent System Solve the system with an infinite number of solutions.

x - 2y + 3z = 0

(1)

3x + y - 2z = 0

(2)

2x - 4y + 6z = 0

(3)

**Solution**

Let’s find the determinant first. Set up a matrix augmented by the first two columns. ∣  1 -2 3

3 1 -2

2 -4 6  ∣     1 -2

2 -4  ∣  Then, 1(1)(6) + (-2)(-2)(2) + 3(3)(-4) - 2(1)(3) - (-4)(-2)(1) - 6(3)(-2) = 0 As the determinant equals zero, there is either no solution or an infinite number of solutions. We have to perform elimination to find out. 1. Multiply equation (1) by -2 and add the result to equation (3):

-2x + 4y - 6x = 0

2x - 4y + 6z = 0

0 = 0 2. Obtaining an answer of 0 = 0, a statement that is always true, means that the system has an infinite number of solutions. Graphing the system, we can see that two of the planes are the same and they both intersect the third plane on a line. See Figure 2.

x - 2y + 3z = 0 2x - 4y + 6z = 0 3x + y + 2z = 0 Understanding Properties of Determinants There are many properties of determinants. Listed here are some properties that may be helpful in calculating the determinant of a matrix. properties of determinants 1. If the matrix is in upper triangular form, the determinant equals the product of entries down the main diagonal. 2. When two rows are interchanged, the determinant changes sign. 3. If either two rows or two columns are identical, the determinant equals zero. 4. If a matrix contains either a row of zeros or a column of zeros, the determinant equals zero. 5. The determinant of an inverse matrix A-1 is the reciprocal of the determinant of the matrix A. 6. If any row or column is multiplied by a constant, the determinant is multiplied by the same factor.

---
### 📐 **Example  7**
Illustrating Properties of Determinants Illustrate each of the properties of determinants.

**Solution**

Property 1 states that if the matrix is in upper triangular form, the determinant is the product of the entries down the main diagonal.

A = [ 

 ]  Augment A with the first two columns.

A = [ 

 ∣    

 ]  Then det(A) = 1(2)(-1) + 2(1)(0) + 3(0)(0) - 0(2)(3) - 0(1)(1) + 1(0)(2)

= -2 Property 2 states that interchanging rows changes the sign. Given

A = [ -1 5

4 -3 ] , det(A) = (-1)(-3) - (4)(5) = 3 - 20 = -17

B = [  4 -3

-1 5 ] , det(B) = (4)(5) - (-1)(-3) = 20 - 3 = 17

Property 3 states that if two rows or two columns are identical, the determinant equals zero.

A = ∣ 

 ∣    

-1 2  ] 

det(A) = 1(2)(2) + 2(2)(-1) + 2(2)(2) + 1(2)(2) - 2(2)(1) - 2(2)(2)

= 4 - 4 + 8 + 4 - 4 - 8 = 0 Property 4 states that if a row or column equals zero, the determinant equals zero. Thus,

A = [ 1 2

0 0 ] , det(A) = 1(0) - 2(0) = 0 Property 5 states that the determinant of an inverse matrix A-1 is the reciprocal of the determinant A. Thus,

A = [ 1 2

3 4 ] , det(A) = 1(4) - 3(2) = -2

A-1 = [  -2    3/2  - 1/2  ] , det(A-1) = -2( - 1/2  )  - (  3/2  ) (1) = - 1/2  Property 6 states that if any row or column of a matrix is multiplied by a constant, the determinant is multiplied by the same factor. Thus,

A = [ 1 2

3 4 ] , det(A) = 1(4) - 2(3) = -2

B = [ 2(1) 2(2) 3 4 ] , det(B) = 2(4) - 3(4) = -4

---
### 📐 **Example  8**
Using Cramer’s Rule and Determinant Properties to Solve a System Find the solution to the given 3 ×  3 system.

2x + 4y + 4z = 2 (1)

3x + 7y + 7z = -5 (2)

x + 2y + 2z = 4 (3)

**Solution**

Using Cramer’s Rule, we have D = ∣ 

 ∣  Notice that the second and third columns are identical. According to Property 3, the determinant will be zero, so there is either no solution or an infinite number of solutions. We have to perform elimination to find out. 1. Multiply equation (3) by -2 and add the result to equation (1).

-2x - 4y - 4x = -8

2x + 4y + 4z = 2

0 = -6 Obtaining a statement that is a contradiction means that the system has no solution. Access these online resources for additional instruction and practice with Cramer’s Rule. • Solve a System of Two Equations Using Cramer's Rule (http://openstaxcollege.org/l/system²cramer) • Solve a Systems of Three Equations using Cramer's Rule (http://openstaxcollege.org/l/system³cramer)

## 9.8 Section Exercises

---
### 9.8 Section Exercises

Verbal 1. Explain why we can always evaluate the determinant of a square matrix. 2. Examining Cramer’s Rule, explain why there is no unique solution to the system when the determinant of your matrix is 0. For simplicity, use a 2 ×  2 matrix. 3. Explain what it means in terms of an inverse for a matrix to have a 0 determinant. 4. The determinant of 2 ×  2 matrix A is 3. If you switch the rows and multiply the first row by 6 and the second row by 2, explain how to find the determinant and provide the answer. Algebraic For the following exercises, find the determinant.

3 4 ∣ 6. ∣ -1 2

3 -4 ∣ 7. ∣  2 -5

-1 6 ∣ 8. ∣ -8 4

-1 5 ∣ 9. ∣ 1 0

3 -4 ∣

0 -10 ∣

8 4 ∣ -3

 -1 0 0

 ∣   -1 4 0

 ∣  

 ∣  

-5 6 1  ∣   -2 1 4

-4 2 -8

2 -8 -3  ∣   6 -1 2

-4 -3 5

1 9 -1  ∣   5 1 -1

2 3 1

3 -6 -3  ∣  1.1   -1 

-4  0  0 

4.1  -0.4  2.5  ∣   -1.6  3.1 

1.1 3  -8 

-9.3    ∣  24.  ∣  - 1/2    1/3    1/4    1/5  - 1/6   1/7     1/8   ∣  For the following exercises, solve the system of linear equations using Cramer’s Rule. 4x + 5y = 9 26. 5x - 4y = 2 -4x + 7y = 6 27. 6x - 3y = 2 -8x + 9y = -1 5x - 2y = 13 2x - y = -1 -5x + 8y = -1 2x + 6y = -4 32. 4x - 5y = 7 -3x + 9y = 0 -3x - 5y = -105 34. 8x - 2y = -3 -4x + 6y = 4 For the following exercises, solve the system of linear equations using Cramer’s Rule. 35. x + 2y - 4z = - 1 7x + 3y + 5z = 26 -2x - 6y + 7z = - 6 36. -5x + 2y - 4z = - 47 4x - 3y - z = - 94 3x - 3y + 2z = 94 37. 4x + 5y - z = -7 -2x - 9y + 2z = 8 5y + 7z = 21 5x - 2z = - 2 3x + 2y - 5z = - 9 39. 4x - 2y + 3z = 6 - 6x + y = - 2 2x + 7y + 8z = 24 40. 5x + 2y - z = 1 -7x - 8y + 3z = 1.5 6x - 12y + z = 7 42. -4x - 3y - 8z = - 7 2x - 9y + 5z = 0.5 5x - 6y - 5z = - 2

43. 4x - 6y + 8z = 10 -2x + 3y - 4z = - 5 x + y + z = 1 44. 4x - 6y + 8z = 10 -2x + 3y - 4z = - 5 Technology For the following exercises, use the determinant function on a graphing utility.  

 ∣  ∣    1/2  1 7 4

0  1/2  100 5

0 0 0 2  ∣   

 ∣  Real-World Applications For the following exercises, create a system of linear equations to describe the behavior. Then, calculate the determinant. Will there be a unique solution? If so, find the unique solution. 49. Two numbers add up to 56. One number is 20 less than the other. 50. Two numbers add up to 104. If you add two times the first number plus two times the second number, your total is 208 51. Three numbers add up to 106. The first number is 3 less than the second number. The third number is 4 more than the first number. 52. Three numbers add to 216. The sum of the first two numbers is 112. The third number is 8 less than the first two numbers combined. For the following exercises, create a system of linear equations to describe the behavior. Then, solve the system for all solutions using Cramer’s Rule. 53. You invest $10,000 into two accounts, which receive 8% interest and 5% interest. At the end of a year, you had $10,710 in your combined accounts. How much was invested in each account? 54. You invest $80,000 into two accounts, $22,000 in one account, and $58,000 in the other account. At the end of one year, assuming simple interest, you have earned $2,470 in interest. The second account receives half a percent less than twice the interest on the first account. What are the interest rates for your accounts? 55. A movie theater needs to know how many adult tickets and children tickets were sold out of the 1,200 total tickets. If children’s tickets are $5.95, adult tickets are $11.15, and the total amount of revenue was $12,756, how many children’s tickets and adult tickets were sold? 56. A concert venue sells single tickets for $40 each and couple’s tickets for $65. If the total revenue was $18,090 and the 321 tickets were sold, how many single tickets and how many couple’s tickets were sold? 57. You decide to paint your kitchen green. You create the color of paint by mixing yellow and blue paints. You cannot remember how many gallons of each color went into your mix, but you know there were 10 gal total. Additionally, you kept your receipt, and know the total amount spent was $29.50. If each gallon of yellow costs $2.59, and each gallon of blue costs $3.19, how many gallons of each color go into your green mix? 58. You sold two types of scarves at a farmers’ market and would like to know which one was more popular. The total number of scarves sold was 56, the yellow scarf cost $10, and the purple scarf cost $11. If you had total revenue of $583, how many yellow scarves and how many purple scarves were sold? ∣     

0 -9 1 3 

3 0 -2 -1

   -2  ∣ 

59. Your garden produced two types of tomatoes, one green and one red. The red weigh 10 oz, and the green weigh 4 oz. You have 30 tomatoes, and a total weight of 13 lb, 14 oz. How many of each type of tomato do you have? 60. At a market, the three most popular vegetables make up 53% of vegetable sales. Corn has 4% higher sales than broccoli, which has 5% more sales than onions. What percentage does each vegetable have in the market share? 61. At the same market, the three most popular fruits make up 37% of the total fruit sold. Strawberries sell twice as much as oranges, and kiwis sell one more percentage point than oranges. For each fruit, find the percentage of total fruit sold. 62. Three bands performed at a concert venue. The first band charged $15 per ticket, the second band charged $45 per ticket, and the final band charged $22 per ticket. There were 510 tickets sold, for a total of $12,700. If the first band had 40 more audience members than the second band, how many tickets were sold for each band? 63. A movie theatre sold tickets to three movies. The tickets to the first movie were $5, the tickets to the second movie were $11, and the third movie was $12. 100 tickets were sold to the first movie. The total number of tickets sold was 642, for a total revenue of $6,774. How many tickets for each movie were sold? of the population at a prison last year. This year, the same age groups made up 82.08% of the population. The 20–29 age group increased by 20%, the 30–39 age group increased by 2%, and the 40–49 age group decreased to  3/4  of their previous population. Originally, the 30–39 age group had 2% more prisoners than the 20–29 age group. Determine the prison population percentage for each age group last year. 65. At a women’s prison down the road, the total number of inmates aged 20–49 totaled 5,525. This year, the 20–29 age group increased by 10%, the 30–39 age group decreased by 20%, and the 40–49 age group doubled. There are now 6,040 prisoners. Originally, there were 500 more in the 30–39 age group than the 20–29 age group. Determine the prison population for each age group last year. For the following exercises, use this scenario: A health-conscious company decides to make a trail mix out of almonds, dried cranberries, and chocolate-covered cashews. The nutritional information for these items is shown in Table 1. Fat (g) Protein (g) Carbohydrates (g) Almonds (10) Cranberries (10) 0.02 Cashews (10) 3.5 5.5 66. For the special “low-carb” trail mix, there are 1,000 pieces of mix. The total number of carbohydrates is 425 g, and the total amount of fat is 570.2 g. If there are 200 more pieces of cashews than cranberries, how many of each item is in the trail mix? 67. For the “hiking” mix, there are 1,000 pieces in the mix, containing 390.8 g of fat, and 165 g of protein. If there is the same amount of almonds as cashews, how many of each item is in the trail mix? 68. For the “energy-booster” mix, there are 1,000 pieces in the mix, containing 145 g of protein and 625 g of carbohydrates. If the number of almonds and cashews summed together is equivalent to the amount of cranberries, how many of each item is in the trail mix?

### Key Terms

addition method an algebraic technique used to solve systems of linear equations in which the equations are added in a way that eliminates one variable, allowing the resulting equation to be solved for the remaining variable; substitution is then used to solve for the first variable augmented matrix a coefficient matrix adjoined with the constant column separated by a vertical line within the matrix brackets break-even point the point at which a cost function intersects a revenue function; where profit is zero coefficient matrix a matrix that contains only the coefficients from a system of equations column a set of numbers aligned vertically in a matrix consistent system a system for which there is a single solution to all equations in the system and it is an independent system, or if there are an infinite number of solutions and it is a dependent system cost function the function used to calculate the costs of doing business; it usually has two parts, fixed costs and variable costs Cramer’s Rule a method for solving systems of equations that have the same number of equations as variables using determinants dependent system a system of linear equations in which the two equations represent the same line; there are an infinite number of solutions to a dependent system determinant a number calculated using the entries of a square matrix that determines such information as whether there is a solution to a system of equations entry an element, coefficient, or constant in a matrix feasible region the solution to a system of nonlinear inequalities that is the region of the graph where the shaded regions of each inequality intersect Gaussian elimination using elementary row operations to obtain a matrix in row-echelon form identity matrix a square matrix containing ones down the main diagonal and zeros everywhere else; it acts as a 1 in matrix algebra inconsistent system a system of linear equations with no common solution because they represent parallel lines, which have no point or line in common independent system a system of linear equations with exactly one solution pair (x, y) main diagonal entries from the upper left corner diagonally to the lower right corner of a square matrix matrix a rectangular array of numbers multiplicative inverse of a matrix a matrix that, when multiplied by the original, equals the identity matrix nonlinear inequality an inequality containing a nonlinear expression partial fraction decomposition the process of returning a simplified rational expression to its original form, a sum or difference of simpler rational expressions partial fractions the individual fractions that make up the sum or difference of a rational expression before combining them into a simplified rational expression profit function the profit function is written as P(x) = R(x) - C(x), revenue minus cost revenue function the function that is used to calculate revenue, simply written as R = xp, where x = quantity and p = price row a set of numbers aligned horizontally in a matrix row operations adding one row to another row, multiplying a row by a constant, interchanging rows, and so on, with the goal of achieving row-echelon form row-echelon form after performing row operations, the matrix form that contains ones down the main diagonal and zeros at every space below the diagonal row-equivalent two matrices A and B are row-equivalent if one can be obtained from the other by performing basic row operations scalar multiple an entry of a matrix that has been multiplied by a scalar solution set the set of all ordered pairs or triples that satisfy all equations in a system of equations substitution method an algebraic technique used to solve systems of linear equations in which one of the two equations is solved for one variable and then substituted into the second equation to solve for the second variable

system of linear equations a set of two or more equations in two or more variables that must be considered simultaneously. system of nonlinear equations a system of equations containing at least one equation that is of degree larger than one system of nonlinear inequalities a system of two or more inequalities in two or more variables containing at least one inequality that is not linear Key Equations Identity matrix for a 2 ×  2 matrix I² = [ 1 0

0 1 ]  Identity matrix for a 3 ×  3 matrix I³ = [ 

 ]  Multiplicative inverse of a 2 ×  2 matrix A-1 =  _______ ad - bc  [  d -b

-c a ] , where ad - bc ≠  0

### Key Concepts

• A system of linear equations consists of two or more equations made up of two or more variables such that all equations in the system are considered simultaneously. • The solution to a system of linear equations in two variables is any ordered pair that satisfies each equation independently. See Example 1. • Systems of equations are classified as independent with one solution, dependent with an infinite number of solutions, or inconsistent with no solution. • One method of solving a system of linear equations in two variables is by graphing. In this method, we graph the equations on the same set of axes. See Example 2. • Another method of solving a system of linear equations is by substitution. In this method, we solve for one variable in one equation and substitute the result into the second equation. See Example 3. • A third method of solving a system of linear equations is by addition, in which we can eliminate a variable by adding opposite coefficients of corresponding variables. See Example 4. • It is often necessary to multiply one or both equations by a constant to facilitate elimination of a variable when adding the two equations together. See Example 5, Example 6, and Example 7. • Either method of solving a system of equations results in a false statement for inconsistent systems because they are made up of parallel lines that never intersect. See Example 8. • The solution to a system of dependent equations will always be true because both equations describe the same line. See Example 9. • Systems of equations can be used to solve real-world problems that involve more than one variable, such as those relating to revenue, cost, and profit. See Example 10 and Example 11. 9.2 Systems of Linear Equations: Three Variables • A solution set is an ordered triple {(x, y, z)} that represents the intersection of three planes in space. See Example 1. • A system of three equations in three variables can be solved by using a series of steps that forces a variable to be eliminated. The steps include interchanging the order of equations, multiplying both sides of an equation by a nonzero constant, and adding a nonzero multiple of one equation to another equation. See Example 2. • Systems of three equations in three variables are useful for solving many different types of real-world problems. See

**Example 3** — .
• A system of equations in three variables is inconsistent if no solution exists. After performing elimination operations, the result is a contradiction. See Example 4. • Systems of equations in three variables that are inconsistent could result from three parallel planes, two parallel planes and one intersecting plane, or three planes that intersect the other two but not at the same location.

• A system of equations in three variables is dependent if it has an infinite number of solutions. After performing elimination operations, the result is an identity. See Example 5. • Systems of equations in three variables that are dependent could result from three identical planes, three planes intersecting at a line, or two identical planes that intersect the third on a line. 9.3 Systems of Nonlinear Equations and Inequalities: Two Variables • There are three possible types of solutions to a system of equations representing a line and a parabola: (1) no solution, the line does not intersect the parabola; (2) one solution, the line is tangent to the parabola; and (3) two solutions, the line intersects the parabola in two points. See Example 1. • There are three possible types of solutions to a system of equations representing a circle and a line: (1) no solution, the line does not intersect the circle; (2) one solution, the line is tangent to the parabola; (3) two solutions, the line intersects the circle in two points. See Example 2. • There are five possible types of solutions to the system of nonlinear equations representing an ellipse and a circle: (1) no solution, the circle and the ellipse do not intersect; (2) one solution, the circle and the ellipse are tangent to each other; (3) two solutions, the circle and the ellipse intersect in two points; (4) three solutions, the circle and ellipse intersect in three places; (5) four solutions, the circle and the ellipse intersect in four points. See Example 3. • An inequality is graphed in much the same way as an equation, except for > or <, we draw a dashed line and shade the region containing the solution set. See Example 4. • Inequalities are solved the same way as equalities, but solutions to systems of inequalities must satisfy both inequalities. See Example 5. 9.4 Partial Fractions • Decompose  P(x) ____ Q(x)  by writing the partial fractions as  A ________ a¹ x + b¹  +  B ________ a² x + b² . Solve by clearing the fractions, expanding the right side, collecting like terms, and setting corresponding coefficients equal to each other, then setting up and solving a system of equations. See Example 1. • The decomposition of  P(x) ____ Q(x)  with repeated linear factors must account for the factors of the denominator in increasing powers. See Example 2. • The decomposition of  P(x) ____ Q(x)  with a nonrepeated irreducible quadratic factor needs a linear numerator over the quadratic factor, as in  (A)/(x)  +  Bx + C ____________

(ax² + bx + c) . See Example 3. • In the decomposition of  P(x) ____ Q(x)  , where Q(x) has a repeated irreducible quadratic factor, when the irreducible quadratic factors are repeated, powers of the denominator factors must be represented in increasing powers as  Ax + B __

(ax² + bx + c)  +  A² x + B² __

(ax² + bx + c)²  + ... +  An x + Bn __

(ax² + bx + c) n . See Example 4. 9.5 Matrices and Matrix Operations • A matrix is a rectangular array of numbers. Entries are arranged in rows and columns. • The dimensions of a matrix refer to the number of rows and the number of columns. A 3 ×  2 matrix has three rows and two columns. See Example 1. • We add and subtract matrices of equal dimensions by adding and subtracting corresponding entries of each matrix. See Example 2, Example 3, Example 4, and Example 5. • Scalar multiplication involves multiplying each entry in a matrix by a constant. See Example 6. • Scalar multiplication is often required before addition or subtraction can occur. See Example 7. • Multiplying matrices is possible when inner dimensions are the same—the number of columns in the first matrix must match the number of rows in the second. • The product of two matrices, A and B, is obtained by multiplying each entry in row 1 of A by each entry in column 1 of B; then multiply each entry of row 1 of A by each entry in columns 2 of B, and so on. See Example 8 and Example 9.

• Many real-world problems can often be solved using matrices. See Example 10. • We can use a calculator to perform matrix operations after saving each matrix as a matrix variable. See Example 11. 9.6 Solving Systems with Gaussian Elimination • An augmented matrix is one that contains the coefficients and constants of a system of equations. See Example 1. • A matrix augmented with the constant column can be represented as the original system of equations. See Example 2. • Row operations include multiplying a row by a constant, adding one row to another row, and interchanging rows. • We can use Gaussian elimination to solve a system of equations. See Example 3, Example 4, and Example 5. • Row operations are performed on matrices to obtain row-echelon form. See Example 6. • To solve a system of equations, write it in augmented matrix form. Perform row operations to obtain row-echelon form. Back-substitute to find the solutions. See Example 7 and Example 8. • A calculator can be used to solve systems of equations using matrices. See Example 9. • Many real-world problems can be solved using augmented matrices. See Example 10 and Example 11. 9.7 Solving Systems with Inverses • An identity matrix has the property AI = IA = A. See Example 1. • An invertible matrix has the property AA-1 = A-1 A = I. See Example 2. • Use matrix multiplication and the identity to find the inverse of a 2 ×  2 matrix. See Example 3. • The multiplicative inverse can be found using a formula. See Example 4. • Another method of finding the inverse is by augmenting with the identity. See Example 5. • We can augment a 3 ×  3 matrix with the identity on the right and use row operations to turn the original matrix into the identity, and the matrix on the right becomes the inverse. See Example 6. • Write the system of equations as AX = B, and multiply both sides by the inverse of A: A-1 AX = A-1 B. See Example 7 and Example 8. • We can also use a calculator to solve a system of equations with matrix inverses. See Example 9. 9.8 Solving Systems with Cramer's Rule • The determinant for [ a b

c d ]  is ad - bc. See Example 1. • Cramer’s Rule replaces a variable column with the constant column. Solutions are x =  D(x)/(D) , y =  D(y)/(D) . See Example 2. • To find the determinant of a 3 ×  3 matrix, augment with the first two columns. Add the three diagonal entries (upper left to lower right) and subtract the three diagonal entries (lower left to upper right). See Example 3. • To solve a system of three equations in three variables using Cramer’s Rule, replace a variable column with the constant column for each desired solution: x =  D(x)/(D) , y =  D(y)/(D) , z =  D(z)/(D) . See Example 4. • Cramer’s Rule is also useful for finding the solution of a system of equations with no solution or infinite solutions. See

**Example 5** — and Example 6.
• Certain properties of determinants are useful for solving problems. For example:

○ If the matrix is in upper triangular form, the determinant equals the product of entries down the main diagonal.

○ When two rows are interchanged, the determinant changes sign.

○ If either two rows or two columns are identical, the determinant equals zero.

○ If a matrix contains either a row of zeros or a column of zeros, the determinant equals zero.

○ The determinant of an inverse matrix A-1 is the reciprocal of the determinant of the matrix A.

○ If any row or column is multiplied by a constant, the determinant is multiplied by the same factor. See

**Example 7** — and Example 8.

Systems of Linear Equations: Two Variables For the following exercises, determine whether the ordered pair is a solution to the system of equations. 1. 3x - y = 4 x + 4y = - 3 and ( - 1, 1) -3x + 3y = 18 and (9, 15) For the following exercises, use substitution to solve the system of equations. 3x - 2y = -12/7 x +  1/5 y =  43 ___ 70   5/6 x -  1/3 y = - 2/3  4x + 8y = 8 For the following exercises, use addition to solve the system of equations. 6. 3x + 2y = -7 2x + 4y = 6 7. 3x + 4y = 2 9x + 12y = 3 8. 8x + 4y = 2 For the following exercises, write a system of equations to solve each problem. Solve the system of equations. 9. A factory has a cost of production C(x) = 150x + 15,000 and a revenue function R(x) = 200x. What is the break-even point? 10. A performer charges C(x) = 50x + 10,000, where x is the total number of attendees at a show. The venue charges $75 per ticket. After how many people buy tickets does the venue break even, and what is the value of the total tickets sold at that point? Systems of Linear Equations: Three Variables For the following exercises, solve the system of three equations using substitution or addition. 12. 5x + 3y - z = 5 3x - 2y + 4z = 13 4x + 3y + 5z = 22 13. x + y + z = 1 2x + 2y + 2z = 1 3x + 3y = 2 14. 2x - 3y + z = -1 x + y + z = -4 4x + 2y - 3z = 33 15. 3x + 2y - z = -10 x - y + 2z = 7 -x + 3y + z = -2 x - 2y = 5 4y - z = -10 17. 2x - 3y + z = 0 2x + 4y - 3z = 0 6x - 2y - z = 0 18. 6x - 4y - 2z = 2 3x + 2y - 5z = 4 6y - 7z = 5 For the following exercises, write a system of equations to solve each problem. Solve the system of equations. 19. Three odd numbers sum up to 61. The smaller is one-third the larger and the middle number is 16 less than the larger. What are the three numbers? 20. A local theatre sells out for their show. They sell all 500 tickets for a total purse of $8,070.00. The tickets were priced at $15 for students, $12 for children, and $18 for adults. If the band sold three times as many adult tickets as children’s tickets, how many of each type was sold?

Systems of Nonlinear Equations and Inequalities: Two Variables For the following exercises, solve the system of nonlinear equations. 21. y = x² - 7 y = 5x - 13 22. y = x² - 4 y = 5x + 10 23. x² + y² = 16 y = x - 8 24. x² + y² = 25 y = x² + 5 25. x² + y² = 4 y - x² = 3 For the following exercises, graph the inequality. 26. y > x² - 1/4 x² + y² < 4 For the following exercises, graph the system of inequalities. 28. x² + y² + 2x < 3 y > - x² - 3 29. x² - 2x + y² - 4x < 4 y < - x + 4 30. x² + y² < 1 y² < x Partial Fractions For the following exercises, decompose into partial fractions. __________ x² + 3x + 2  32.  ___________ 4x² + 4x + 1  33.  ____________

x² + 10x + 25  34.  x - 18 ____________

x² - 12x + 36  35.  -x² + 36x + 70

_____________

 36.  -5x² + 6x - 2

____________ x³ + 27

 37.  x³ - 4x² + 3x + 11

________________

(x² - 2)²

 38.  4x⁴ - 2x³ + 22x² - 6x + 48

_______________________

x(x² + 4)²

 Matrices and Matrix Operations For the following exercises, perform the requested operations on the given matrices. A = [  4 -2

1 3 ] , B = [  6 7 -3

11 -2 4 ] , C = [ 

 ] , D = [  1 -4 9

10 5 -7

2 8 5  ] , E = [ 

2 -1 3

 ]  41. B + C Solving Systems with Gaussian Elimination For the following exercises, write the system of linear equations from the augmented matrix. Indicate whether there will be a unique solution. 51. [ 

 ∣   

-5  ]  52. [ 

 ∣    -9

 ]  For the following exercises, write the augmented matrix from the system of linear equations. 53. -2x + 2y + z = 7 2x - 8y + 5z = 0 54. 4x + 2y - 3z = 14 -12x + 3y + z = 100 9x - 6y + 2z = 31 55. x + 3z = 12 -x + 4y = 0 y + 2z = - 7

For the following exercises, solve the system of linear equations using Gaussian elimination. 56. 3x - 4y = - 7 -6x + 8y = 14 57. 3x - 4y = 1 -6x + 8y = 6 59. 2x + 3y + 2z = 1 -4x - 6y - 4z = - 2 60. -x + 2y - 4z = 8 3y + 8z = - 4 -7x + y + 2z = 1 Solving Systems with Inverses For the following exercises, find the inverse of the matrix.

  1/2  - 1/2 

- 1/4   3/4   ]  63. [  12 9 -6

-1 3 2

-4 -3 2  ]  64. [ 

 ]  For the following exercises, find the solutions by computing the inverse of the matrix. 5x - 4y - z = -6.1 x + z = -0.7 68. -2x - 3y + 2z = 3 -x + 2y + 4z = -5 -2y + 5z = -3 For the following exercises, write a system of equations to solve each problem. Solve the system of equations. 69. Students were asked to bring their favorite fruit to class. 90% of the fruits consisted of banana, apple, and oranges. If oranges were half as popular as bananas and apples were 5% more popular than bananas, what are the percentages of each individual fruit? 70. A sorority held a bake sale to raise money and sold brownies and chocolate chip cookies. They priced the brownies at $2 and the chocolate chip cookies at $1. They raised $250 and sold 175 items. How many brownies and how many cookies were sold? Solving Systems with Cramer's Rule For the following exercises, find the determinant.

0 0 ] 

73. [  -1 4 3

 ]  74. [  √2  0 0

0 √2  0

0 0 

√2   ]  For the following exercises, use Cramer’s Rule to solve the linear systems of equations. 75. 4x - 2y = 23 -5x - 10y = -35 78. x + 6y + 3z = 4 2x + y + 2z = 3 3x - 2y + z = 0 79. 4x - 3y + 5z = - 5/2  7x - 9y - 3z =  3/2  x - 5y - 5z =  5/2  ___ 10 x -  1/5 y -  3 ___ 10 z = - 1 ___ 50   1 ___ 10 x -  1 ___ 10 y -  1/2 z = -  9 ___ 50   2/5 x -  1/2 y -  3/5 z = - 1/5 

Is the following ordered pair a solution to the system of equations? 1. -5x - y = 12 x + 4y = 9 with ( - 3, 3) For the following exercises, solve the systems of linear and nonlinear equations using substitution or elimination. Indicate if no solution exists. __ 2 x -  1/3 y = 4  3/2 x - y = 0/2 x - 4y = 4 2x + 16y = 2 4. 5x - y = 1 -10x + 2y = - 2 5. 4x - 6y - 2z =  1 ___ 10  x - 7y + 5z = - 1/4  3x + 6y - 9z =  6/5  6. x + z = 20 x + y + z = 20 x + 2y + z = 10 7. 5x - 4y - 3z = 0 2x + y + 2z = 0 x - 6y - 7z = 0 8. y = x² + 2x - 3 y = x - 1 9. y² + x² = 25 y² - 2x² = 1 For the following exercises, graph the following inequalities. 10. y < x² + 9 11. x 2 + y 2 > 4 y < x² + 1 For the following exercises, write the partial fraction decomposition. 12.  ____________

x² + 10x + 25  ________ (3x + 1)²  14.  x⁴ - x³ + 2x - 1

______________

x(x² + 1)²

 For the following exercises, perform the given matrix operations.

-2 3 ]  +  1/2 [ -6 12

4 -8 ]  16. [ 

-2 9 5

 ]  [  3 -4

 ]    1/2   1/3 

 1/4   1/5   ]  -1  18. det∣ 

 19. det  ∣   1/2   - 1/2   

- 1/2  0   1/2    1/2    ∣  20. If det(A) = -6, what would be the determinant if you switched rows 1 and 3, multiplied the second row by 12, and took the inverse? 21. Rewrite the system of linear equations as an augmented matrix. -2x + 3y - 6z = -1 x - 5y + 12z = 11 22. Rewrite the augmented matrix as a system of linear equations. [ 

 ∣    

-5

 ] 

For the following exercises, use Gaussian elimination to solve the systems of equations. 23. x - 6y = 4 2x - 12y = 0 24. 2x + y + z = -3 x - 2y + 3z = 6 x - y - z = 6 For the following exercises, use the inverse of a matrix to solve the systems of equations. -x + 2y = 80 ___ 100 x -  3 ___ 100 y +  1 ___  3 ___ 100 x -  7 ___ 100 y -  1 ___  9 ___ 100 x -  9 ___ 100 y -  9 ___ For the following exercises, use Cramer’s Rule to solve the systems of equations. For the following exercises, solve using a system of linear equations. 29. A factory producing cell phones has the following cost and revenue functions: C(x) = x 2 + 75x + 2,688 and R(x) = x 2 + 160x. What is the range of cell phones they should produce each day so there is profit? Round to the nearest number that generates profit. 30. A small fair charges $1.50 for students, $1 for children, and $2 for adults. In one day, three times as many children as adults attended. A total of 800 tickets were sold for a total revenue of $1,050. How many of each type of ticket was sold?
