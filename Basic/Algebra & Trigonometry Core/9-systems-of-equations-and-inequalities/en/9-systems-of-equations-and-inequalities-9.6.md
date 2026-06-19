# Systems of Equations and Inequalities

## 9.6 Solving Systems with Gaussian EliMination

---
Carl Friedrich Gauss lived during the late 18th century and early 19th century, but he is still considered one of the most prolific mathematicians in history.
His contributions to the science of mathematics and physics span fields such as algebra, number theory, analysis, differential geometry, astronomy, and optics, among others.
His discoveries regarding matrix theory changed the way mathematicians have worked for the last two centuries.
We first encountered Gaussian elimination in Systems of Linear Equations:
Two Variables.
In this section, we will revisit this technique for solving systems, this time using matrices.
Writing the Augmented Matrix of a System of Equations A matrix can serve as a device for representing and solving a system of equations.
To express a system in matrix form, we extract the coefficients of the variables and the constants, and these become the entries of the matrix.
We use a vertical line to separate the coefficient entries from the constants, essentially replacing the equal signs.
When a system is written in this form, we call it an augmented matrix.
For example, consider the following 2 × 2 system of equations.

3x + 4y = 7

4x - 2y = 5 We can write this system as an augmented matrix: [ 3 4

4 -2 ∣ 7 5 ] We can also write a matrix containing just the coefficients.
This is called the coefficient matrix. [ 3 4

4 -2 ] Learning Objectives
In this section, you will:
• Write the augmented matrix of a system of equations.
• Write the system of equations from an augmented matrix.
• Perform row operations on a matrix.
• Solve a system of linear equations using matrices.
A three-by-three system of equations such as

3x - y - z = 0

x + y = 5

2x - 3z = 2 has a coefficient matrix [ 3 -1 -1

1 1 0

2 0 -3 ] and is represented by the augmented matrix [ 3 -1 -1

1 1 0

2 0 -3 ∣ 

 ] Notice that the matrix is written so that the variables line up in their own columns: x-terms go in the first column, y-terms in the second column, and z-terms in the third column.
It is very important that each equation is written in standard form ax + by + cz = d so that the variables line up.
When there is a missing variable term in an equation, the coefficient is 0.

---
### 💡 **How To…**
Given a system of equations, write an augmented matrix. 1.
Write the coefficients of the x-terms as the numbers down the first column. 2.
Write the coefficients of the y-terms as the numbers down the second column. 3.
If there are z-terms, write the coefficients as the numbers down the third column. 4.
Draw a vertical line and write the constants to the right of the line.

---
### 📐 **Example 1**:
Writing the Augmented Matrix for a System of Equations

Write the augmented matrix for the given system of equations.

x + 2y - z = 3

2x - y + 2z = 6

x - 3y + 3z = 4

**Solution**

The augmented matrix displays the coefficients of the variables, and an additional column for the constants. [ 1 2 -1

2 -1 2

1 -3 3 ∣ 

 ] 

---
### ✏️ **Try It #1**
Write the augmented matrix of the given system of equations.

4x - 3y = 11

3x + 2y = 4 Writing a System of Equations from an Augmented Matrix We can use augmented matrices to help us solve systems of equations because they simplify operations when the systems are not encumbered by the variables.
However, it is important to understand how to move back and forth between formats in order to make finding solutions smoother and more intuitive.
Here, we will use the information in an augmented matrix to write the system of equations in standard form.

---
### 📐 **Example 2**:
Writing a System of Equations from an Augmented Matrix Form

Find the system of equations from the augmented matrix. [ 1 -3 -5

2 -5 -4

-3 5 4 ∣ -2

 ]

**Solution**

When the columns represent the variables x, y, and z, [ 1 -3 -5

2 -5 -4

-3 5 4 ∣ -2

 ] → x - 3y - 5z = - 2

2x - 5y - 4z = 5

-3x + 5y + 4z = 6 

---
### ✏️ **Try It #2**
Write the system of equations from the augmented matrix. [ 

 ∣ 

-9 ]
Performing Row Operations on a Matrix Now that we can write systems of equations in augmented matrix form, we will examine the various row operations that can be performed on a matrix, such as addition, multiplication by a constant, and interchanging rows.
Performing row operations on a matrix is the method we use for solving a system of equations.
In order to solve the system of equations, we want to convert the matrix to row-echelon form, in which there are ones down the main diagonal from the upper left corner to the lower right corner, and zeros in every position below the main diagonal as shown.
Row-echelon form [ 1 a b

0 1 d

 ]
We use row operations corresponding to equation operations to obtain a new matrix that is row-equivalent in a simpler form.
Here are the guidelines to obtaining row-echelon form. 1.
In any nonzero row, the first nonzero number is a 1.
It is called a leading 1. 2.
Any all-zero rows are placed at the bottom on the matrix. 3.
Any leading 1 is below and to the right of a previous leading 1. 4.
Any column containing a leading 1 has zeros in all other positions in the column.
To solve a system of equations we can perform the following row operations to convert the coefficient matrix to row- echelon form and do back-substitution to find the solution. 1.
Interchange rows.
(Notation: Ri ↔ Rj ) 2.
Multiply a row by a constant.
(Notation: cRi ) 3.
Add the product of a row multiplied by a constant to another row.
(Notation: Ri + cRj) Each of the row operations corresponds to the operations we have already learned to solve systems of equations in three variables.
With these operations, there are some key moves that will quickly achieve the goal of writing a matrix in row-echelon form.
To obtain a matrix in row-echelon form for finding solutions, we use Gaussian elimination, a method that uses row operations to obtain a 1 as the first entry so that row 1 can be used to convert the remaining rows.

Gaussian elimination The Gaussian elimination method refers to a strategy used to obtain the row-echelon form of a matrix.
The goal is to write matrix A with the number 1 as the entry down the main diagonal and have all zeros below.
A = [ a¹1 a¹2 a¹3

a²1 a²2 a²3

a³1 a³2 a³3 ] After Gaussian elimination A = [ 1 b¹2 b¹3

0 1 b²3

 ] The first step of the Gaussian strategy includes obtaining a 1 as the first entry, so that row 1 may be used to alter the rows below.

---
### 💡 **How To…**
Given an augmented matrix, perform row operations to achieve row-echelon form. 1.
The first equation should have a leading coefficient of 1.
Interchange rows or multiply by a constant, if necessary. 2.
Use row operations to obtain zeros down the first column below the first entry of 1. 3.
Use row operations to obtain a 1 in row 2, column 2. 4.
Use row operations to obtain zeros down column 2, below the entry of 1. 5.
Use row operations to obtain a 1 in row 3, column 3. 6.
Continue this process for all rows until there is a 1 in every entry down the main diagonal and there are only zeros below. 7.
If any rows contain all zeros, place them at the bottom.

---
### 📐 **Example 3**:
Solving a 2 × 2 System by Gaussian Elimination

Solve the given system by Gaussian elimination.

2x + 3y = 6

x - y = 1/2

**Solution**

First, we write this as an augmented matrix.

[ 2 3

1 -1 ∣ 6 1/2 ] We want a 1 in row 1, column 1.
This can be accomplished by interchanging row 1 and row 2.

R¹ ↔ R² → [ 1 -1

2 3 ∣ 1/2 6 ] We now have a 1 as the first entry in row 1, column 1.
Now let’s obtain a 0 in row 2, column 1.
This can be accomplished by multiplying row 1 by -2, and then adding the result to row 2.

-2R¹ + R² = R² → [ 1 -1

0 5 ∣ 1/2 5 ] We only have one more step, to multiply row 2 by 1/5 .

 1/5 R² = R² → [ 1 -1

0 1 ∣ 1/2 1 ] Use back-substitution.
The second row of the matrix represents y = 1.
Back-substitute y = 1 into the first equation.

x - (1) = 1/2 

x = 3/2 The solution is the point ( 3 __

---
### ✏️ **Try It #3**
Solve the given system by Gaussian elimination.

4x + 3y = 11

x - 3y = -1

---
### 📐 **Example 4**
Using Gaussian Elimination to Solve a System of Equations Use Gaussian elimination to solve the given 2 × 2 system of equations.

2x + y = 1

4x + 2y = 6

**Solution**

Write the system as an augmented matrix.

[ 2 1

4 2 ∣ 1 6 ] Obtain a 1 in row 1, column 1.
This can be accomplished by multiplying the first row by 1/2 .

 1/2 R¹ = R¹ → [ 1 1/2 

4 2 ∣ 1/2 6 ] Next, we want a 0 in row 2, column 1.
Multiply row 1 by -4 and add row 1 to row 2.

-4R¹ + R² = R² → [ 1 1/2 

0 0 ∣ 1/2 4 ] The second row represents the equation 0 = 4.
Therefore, the system is inconsistent and has no solution.

---
### 📐 **Example 5**:
Solving a Dependent System

Solve the system of equations.

3x + 4y = 12

6x + 8y = 24

**Solution**

Perform row operations on the augmented matrix to try and achieve row-echelon form.

A = [ 3 4

6 8 ∣ 12 24 ] 

- 1/2 R² + R¹ = R¹ → [ 0 0

6 8 ∣ 0 24 ] 

R¹ ↔ R² → [ 6 8

0 0 ∣ 24 0 ] The matrix ends up with all zeros in the last row: 0y = 0.
Thus, there are an infinite number of solutions and the system is classified as dependent.
To find the generic solution, return to one of the original equations and solve for y.

3x + 4y = 12

4y = 12 - 3x

y = 3 - 3/4 x So the solution to this system is ( x, 3 - 3/4 x ) .

---
### 📐 **Example 6**
Performing Row Operations on a 3 × 3 Augmented Matrix to Obtain Row-Echelon Form Perform row operations on the given matrix to obtain row-echelon form. [ 

-3 3 4 ∣ 

 ]

**Solution**

The first row already has a 1 in row 1, column 1.
The next step is to multiply row 1 by -2 and add it to row 2.

Then replace row 2 with the result. -2R¹ + R² = R² → [ 1 -3 4

0 1 -2

-3 3 4 ∣ 

 ] Next, obtain a zero in row 3, column 1.

3R¹ + R³ = R³ → [ 1 -3 4

0 1 -2

 ∣ 

 ] Next, obtain a zero in row 3, column 2.

6R² + R³ = R³ → [ 1 -3 4

0 1 -2

0 0 4 ∣ 

 ] The last step is to obtain a 1 in row 3, column 3.

 1/2 R³ = R³ → [ 1 -3 4

0 1 -2

0 0 1 ∣ 

-6

 21/2 ] 

---
### ✏️ **Try It #4**
Write the system of equations in row-echelon form.

x - 2y + 3z = 9

-x + 3y = - 4

2x - 5y + 5z = 17 Solving a System of Linear Equations Using Matrices We have seen how to write a system of equations with an augmented matrix, and then how to use row operations and back-substitution to obtain row-echelon form.
Now, we will take row-echelon form a step farther to solve a 3 by 3 system of linear equations.
The general idea is to eliminate all but one variable using row operations and then back- substitute to solve for the other variables.

---
### 📐 **Example 7**:
Solving a System of Linear Equations Using Matrices

Solve the system of linear equations using matrices.

x - y + z = 8

2x + 3y - z = -2

3x - 2y - 9z = 9

**Solution**

First, we write the augmented matrix. [ 1 -1 1

2 3 -1

3 -2 -9 ∣ 

-2

 ] Next, we perform row operations to obtain row-echelon form. -2R¹ + R² = R² → [ 1 -1 1

0 5 -3

3 -2 -9 ∣ 

-18

 ] -3R¹ + R³ = R³ → [ 1 -1 1

0 5 -3

0 1 -12 ∣ 

-18

-15 ] The easiest way to obtain a 1 in row 2 of column 1 is to interchange R² and R³.

Interchange R² and R³ → [ 1 -1 1 8

0 1 -12 -15

0 5 -3 -18 ] 

Then -5R² + R³ = R³ → [ 1 -1 1

0 1 -12

0 0 57 ∣ 

-15

 ] - 1 57 R³ = R³ → [ 1 -1 1

0 1 -12

0 0 1 ∣ 

-15

 ] The last matrix represents the equivalent system.

x - y + z = 8

y - 12z = -15

z = 1 Using back-substitution, we obtain the solution as (4, -3, 1).

---
### 📐 **Example 8**:
Solving a Dependent System of Linear Equations Using Matrices

Solve the following system of linear equations using matrices.

-x - 2y + z = -1

2x + 3y = 2

y - 2z = 0

**Solution**

Write the augmented matrix. [ -1 -2 1

0 1 -2 ∣ -1

 ] First, multiply row 1 by -1 to get a 1 in row 1, column 1.
Then, perform row operations to obtain row-echelon form.

-R¹ → [ -1 -2 1

0 1 -2 ∣ -1

 ] 

R² ↔ R³ → [ 

 ∣ 

 ] 

-2R¹ + R³ = R³ → [ 1 2 -1

0 1 -2

0 -1 2 ∣ 

 ] 

R² + R³ = R³ → [ 

 ∣ 

 ] The last matrix represents the following system.

x + 2y - z = 1

y - 2z = 0

0 = 0 We see by the identity 0 = 0 that this is a dependent system with an infinite number of solutions.
We then find the generic solution.
By solving the second equation for y and substituting it into the first equation we can solve for z in terms of x.

x + 2y - z = 1

y = 2z

x + 2(2z) - z = 1

x + 3z = 1

z = 1 - x 

Now we substitute the expression for z into the second equation to solve for y in terms of x.

y - 2z = 0

z = 1 - x 

y - 2( 1 - x ) = 0

y = 2 - 2x The generic solution is ( x, 2 - 2x , 1 - x ) .

---
### ✏️ **Try It #5**
Solve the system using matrices.

x + 4y - z = 4

2x + 5y + 8z = 15

x + 3y - 3z = 1 Can any system of linear equations be solved by Gaussian elimination?
Yes, a system of linear equations of any size can be solved by Gaussian elimination.

---
### 💡 **How To…**
Given a system of equations, solve with matrices using a calculator. 1.
Save the augmented matrix as a matrix variable [A], [B], [C], ... . 2.
Use the ref( function in the calculator, calling up each matrix variable as needed.

---
### 📐 **Example 9**:
Solving Systems of Equations with Matrices Using a Calculator

Solve the system of equations.

5x + 3y + 9z = -1

-2x + 3y - z = -2

-x - 4y + 5z = 1

**Solution**

Write the augmented matrix for the system of equations.

[ 

-2 3 -1

-1 -4 5 ∣ -1

-2

-1 ] On the matrix page of the calculator, enter the augmented matrix above as the matrix variable [A]. [A] = [ 5 3 9 -1

-2 3 -1 -2

-1 -4 5 1 ] Use the ref( function in the calculator, calling up the matrix variable [A].

ref([A]) Evaluate. [ 3/5 9/5 1/5 

0 1 13/21 - 4/7 

 - 24 187 ] → x + 3/5 y + 9/5 z = - 1/5 

y + 13/21 z = - 4/7 z = - 24 187 Using back-substitution, the solution is ( 61 

---
### 📐 **Example 10**:
Applying 2 × 2 Matrices to Finance

Carolyn invests a total of $12,000 in two municipal bonds, one paying 10.5% interest and the other paying 12% interest.
The annual interest earned on the two investments last year was $1,335.
How much was invested at each rate?

**Solution**

We have a system of two equations in two variables.
Let x = the amount invested at 10.5% interest, and y = the amount invested at 12% interest.

As a matrix, we have [ 

Multiply row 1 by -0.105 and add the result to row 2. [ 1 1

75 ] Then,

Thus, $5,000 was invested at 12% interest and $7,000 at 10.5% interest.

---
### 📐 **Example 11**:
Applying 3 × 3 Matrices to Finance

Ava invests a total of $10,000 in three accounts, one paying 5% interest, another paying 8% interest, and the third paying 9% interest.
The annual interest earned on the three investments last year was $770.
The amount invested at 9% was twice the amount invested at 5%.
How much was invested at each rate?

**Solution**

We have a system of three equations in three variables.
Let x be the amount invested at 5% interest, let y be the amount invested at 8% interest, and let z be the amount invested at 9% interest.
Thus,

x + y + z = 10,000

2x - z = 0 As a matrix, we have [ 1 1 1

2 0 -1 ∣ 

 ] Now, we perform Gaussian elimination to achieve row-echelon form.

-0.05R¹ + R² = R² → [ 1 1 1

2 0 -1 ∣ 

 ] 

-2R¹ + R³ = R³ → [ 1 1 1

0 -2 -3 ∣ 

 ] 

 1 0.03 R² = R² → [ 0 1 1

0 1 4/3 

0 -2 -3 ∣ 

 ] 

2R² + R³ = R³ → [ 

0 1 4/3 

0 0 - 1/3 ∣ 

 ] The third row tells us - 1/The second row tells us y + 4/3 z = 9,000.
Substituting z = 6,000, we get

y + 4/The first row tells us x + y + z = 10, 000.
Substituting y = 1,000 and z = 6,000, we get

The answer is $3,000 invested at 5% interest, $1,000 invested at 8%, and $6,000 invested at 9% interest.

---
### ✏️ **Try It #6**
A small shoe company took out a loan of $1,500,000 to expand their inventory.
Part of the money was borrowed at 7%, part was borrowed at 8%, and part was borrowed at 10%.
The amount borrowed at 10% was four times the amount borrowed at 7%, and the annual interest on all three loans was $130,500.
Use matrices to find the amount borrowed at each rate.
Access these online resources for additional instruction and practice with solving systems of linear equations using Gaussian elimination.
• Solve a System of Two Equations Using an Augmented Matrix (http://openstaxcollege.org/l/system²augmat) • Solve a System of Three Equations Using an Augmented Matrix (http://openstaxcollege.org/l/system³augmat) • Augmented Matrices on the Calculator (http://openstaxcollege.org/l/augmatcalc)

### 9.6 Section Exercises

Verbal 1.
Can any system of linear equations be written as an augmented matrix?
Explain why or why not.
Explain how to write that augmented matrix. 2.
Can any matrix be written as a system of linear equations?
Explain why or why not.
Explain how to write that system of equations. 3.
Is there only one correct method of using row operations on a matrix?
Try to explain two different row operations possible to solve the augmented matrix [ 9 3

1 -2 ∣ 0 6 ] . 4.
Can a matrix whose entry is 0 on the diagonal be solved?
Explain why or why not.
What would you do to remedy the situation? 5.
Can a matrix that has 0 entries for an entire row have one solution?
Explain why or why not.
Algebraic For the following exercises, write the augmented matrix for the linear system. 2x + 12y = 3 9x - y = 2 8. 3x + 2y + 10z = 3 -6x + 2y + 5z = 13 4x + z = 18 9. x + 5y + 8z = 19 12x + 3y = 4 3x + 4y + 9z = -7 19x - 5y + 3z = -9 x + 2y = -8 For the following exercises, write the linear system from the augmented matrix. 11. [ -2 5

6 -18 ∣ 5 26 ] 12. [ 3 4

10 17 ∣ 10

13. [ 

-1 -9 4

 ∣ 

-1

 ] 14. [ 

-1 7 5

 ∣ 

 ] 15. [ 

 ∣ 

-5 ] For the following exercises, solve the system by Gaussian elimination.

0 0 ∣ 3 0 ] 

1 0 ∣ 1 2 ] 

4 5 ∣ 3 6 ] 19. [ -1 2

4 -5 ∣ -3 6 ] 

0 2 ∣ 1

-1 ] 5x + 4y = 58 3x + 4y = -17 4x + y = 14 24. -4x - 3y = -2 3x - 5y = -13 10x + 6y = 5 26. 3x + 4y = 12 -6x - 8y = -24 29. 2x - y = 2 3x + 2y = 17/4 x - 3/5 y = 4 1/4 x + 2/3 y = 1/4 x - 2/3 y = -1 1/2 x + 1/3 y = 3 [ 

 ∣ 

 ] [ 

 ∣ 

-90 ] [ 

 ∣ 

 ] 

## 9.6 Section Exercises

---
[ 

 ∣ 0.2

0.8

-0.8 ] 37. -2x + 3y - 2z = 3 4x + 2y - z = 9 4x - 8y + 2z = -6 38. x + y - 4z = -4 5x - 3y - 2z = 0 2x + 6y + 7z = 30 39. 2x + 3y + 2z = 1 -4x - 6y - 4z = -2 40. x + 2y - z = 1 -x - 2y + 2z = -2 3x + 6y - 3z = 5 41. x + 2y - z = 1 -x - 2y + 2z = -2 3x + 6y - 3z = 3 42. x + y = 2 x + z = 1 -y - z = -3 43. x + y + z = 100 x + 2z = 125 -y + 2z = 25/4 x - 2/3 z = - 1/2 1/5 x + 1/3 y = 4/7 1/5 y - 1/3 z = 2/9/2 x + 1/2 y + 1/7 z = - 53 14 1/2 x - 1/2 y + 1/4 z = 3 1/4 x + 1/5 y + 1/3 z = 23 15/2 x - 1/3 y + 1/4 z = - 29 6 1/5 x + 1/6 y - 1/7 z = 431 210 - 1/8 x + 1/9 y + 1 10 z = - 49 45 Extensions For the following exercises, use Gaussian elimination to solve the system. + y - 2 + z - 3 = 0 x + y + z = 6 x + 2 + 2y + z-3 3 = 5 - y + 1 + 3z = -1 x + 5 + y + 7 - z = 4 x + y - z-2 2 = 1 49. x - 3 - y - 1 + 2z = -1 x + 5 + y + 5 + z + 5 = 8 x + y + z = 1 50. x - 3 10 + y + 3 -2z = 3 x + 5 - y - 1 + z = 3/2 x - 1 + y + 4 + 3z = 3/2 51. x - 3 - y - 1 + 2z = -1 x + 5 + y + 5 + z + 5 = 7 x + y + z = 1 Real-World Applications For the following exercises, set up the augmented matrix that describes the situation, and solve for the desired solution. 52.
Every day, a cupcake store sells 5,000 cupcakes in chocolate and vanilla flavors.
If the chocolate flavor is 3 times as popular as the vanilla flavor, how many of each cupcake sell per day? 53.
At a competing cupcake store, $4,520 worth of cupcakes are sold daily.
The chocolate cupcakes cost $2.25 and the red velvet cupcakes cost $1.75.
If the total number of cupcakes sold per day is 2,200, how many of each flavor are sold each day? 54.
You invested $10,000 into two accounts: one that has simple 3% interest, the other with 2.5% interest.
If your total interest payment after one year was $283.50, how much was in each account after the year passed? 55.
You invested $2,300 into account 1, and $2,700 into account 2.
If the total amount of interest after one year is $254, and account 2 has 1.5 times the interest rate of account 1, what are the interest rates?
Assume simple interest rates.

56.
Bikes’R’Us manufactures bikes, which sell for $250.
It costs the manufacturer $180 per bike, plus a startup fee of $3,500.
After how many bikes sold will the manufacturer break even? 57.
A major appliance store is considering purchasing vacuums from a small manufacturer.
The store would be able to purchase the vacuums for $86 each, with a delivery fee of $9,200, regardless of how many vacuums are sold.
If the store needs to start seeing a profit after 230 units are sold, how much should they charge for the vacuums? 58.
The three most popular ice cream flavors are chocolate, strawberry, and vanilla, comprising 83% of the flavors sold at an ice cream shop.
If vanilla sells 1% more than twice strawberry, and chocolate sells 11% more than vanilla, how much of the total ice cream consumption are the vanilla, chocolate, and strawberry flavors? 59.
At an ice cream shop, three flavors are increasing in demand.
Last year, banana, pumpkin, and rocky road ice cream made up 12% of total ice cream sales.
This year, the same three ice creams made up 16.9% of ice cream sales.
The rocky road sales doubled, the banana sales increased by 50%, and the pumpkin sales increased by 20%.
If the rocky road ice cream had one less percent of sales than the banana ice cream, find out the percentage of ice cream sales each individual ice cream made last year. 60.
A bag of mixed nuts contains cashews, pistachios, and almonds.
There are 1,000 total nuts in the bag, and there are 100 less almonds than pistachios.
The cashews weigh 3 g, pistachios weigh 4 g, and almonds weigh 5 g.
If the bag weighs 3.7 kg, find out how many of each type of nut is in the bag. 61.
A bag of mixed nuts contains cashews, pistachios, and almonds.
Originally there were 900 nuts in the bag. 30% of the almonds, 20% of the cashews, and 10% of the pistachios were eaten, and now there are 770 nuts left in the bag.
Originally, there were 100 more cashews than almonds.
Figure out how many of each type of nut was in the bag to begin with.

