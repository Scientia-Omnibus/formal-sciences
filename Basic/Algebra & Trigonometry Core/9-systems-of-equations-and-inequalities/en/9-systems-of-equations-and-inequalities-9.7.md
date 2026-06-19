# Systems of Equations and Inequalities

## 9.7 Solving Systems with Inverses

---
Nancy plans to invest $10,500 into two different bonds to spread out her risk. The first bond has an annual return of 10%, and the second bond has an annual return of 6%. In order to receive an 8.5% return from the two bonds, how much should Nancy invest in each bond? What is the best method to solve this problem? There are several ways we can solve this problem. As we have seen in previous sections, systems of equations and matrices are useful in solving real-world problems involving finance. After studying this section, we will have the tools to solve the bond problem using the inverse of a matrix. Finding the Inverse of a Matrix We know that the multiplicative inverse of a real number a is a-1, and aa-1 = a-1 a = (  1/a  ) a = 1. For example, 2-1 =  1/2  and (  1/2  ) 2 = 1. The multiplicative inverse of a matrix is similar in concept, except that the product of matrix A and its inverse A-1 equals the identity matrix. The identity matrix is a square matrix containing ones down the main diagonal and zeros everywhere else. We identify identity matrices by In where n represents the dimension of the matrix. The following equations are the identity matrices for a 2 ×  2 matrix and a 3 ×  3 matrix, respectively.

I² = [ 1 0

0 1 ] 

I³ = [ 

 ]  The identity matrix acts as a 1 in matrix algebra. For example, AI = IA = A. A matrix that has a multiplicative inverse has the properties

AA-1 = I

A-1 A = I A matrix that has a multiplicative inverse is called an invertible matrix. Only a square matrix may have a multiplicative inverse, as the reversibility, AA-1 = A-1 A = I, is a requirement. Not all square matrices have an inverse, but if A is invertible, then A-1 is unique. We will look at two methods for finding the inverse of a 2 ×  2 matrix and a third method that can be used on both 2 ×  2 and 3 ×  3 matrices. the identity matrix and multiplicative inverse The identity matrix, In, is a square matrix containing ones down the main diagonal and zeros everywhere else. I² = [ 1 0

0 1 ]  I³ = [ 

 ] 

2 ×  2 3 ×  3 If A is an n ×  n matrix and B is an n ×  n matrix such that AB = BA = In, then B = A-1, the multiplicative inverse of a matrix A. Learning Objectives
In this section, you will:
• Find the inverse of a matrix.
• Solve a system of linear equations using an inverse matrix.

---
### 📐 **Example  1**
Showing That the Identity Matrix Acts as a 1 Given matrix A, show that AI = IA = A.

A = [  3 4

-2 5 ]

**Solution**

Use matrix multiplication to show that the product of A and the identity is equal to the product of the identity and A. AI = [  3 4

-2 5 ]  [ 1 0

0 1 ]  = [  3 ⋅ 1 + 4 ⋅ 0 3 ⋅ 0 + 4 ⋅ 1

-2 ⋅ 1 + 5 ⋅ 0 -2 ⋅ 0 + 5 ⋅ 1 ]  = [  3 4

-2 5 ] 

AI = [ 1 0

0 1 ]  [  3 4

-2 5 ]  = [ 1 ⋅ 3 + 0 ⋅ (-2) 1 ⋅ 4 + 0 ⋅ 5

0 ⋅ 3 + 1 ⋅ (-2) 0 ⋅ 4 + 1 ⋅ 5 ]  = [  3 4

-2 5 ] 

---
### 💡 **How To…**
Given two matrices, show that one is the multiplicative inverse of the other. 1. Given matrix A of order n ×  n and matrix B of order n ×  n multiply AB. 2. If AB = I, then find the product BA. If BA = I, then B = A-1 and A = B-1.

---
### 📐 **Example  2**
Showing That Matrix A Is the Multiplicative Inverse of Matrix B Show that the given matrices are multiplicative inverses of each other.

A = [  1 5

-2 -9 ] , B = [ -9 -5

2 1 ]

**Solution**

Multiply AB and BA. If both products equal the identity, then the two matrices are inverses of each other.

AB = [  1 5

-2 -9 ] [ -9 -5

2 1 ] 

= [  1(-9) + 5(2) 1(-5) + 5(1)

-2(-9) - 9(2) -2(-5) - 9(1) ] 

= [ 1 0

0 1 ] 

BA = [ -9 -5

2 1 ] [  1 5

-2 -9 ] 

= [ -9(1) - 5(-2) -9(5) - 5(-9)

2(1) + 1(-2) 2(-5) + 1(-9) ] 

= [ 1 0

0 1 ]  A and B are inverses of each other.

---
### ✏️ **Try It #1**
Show that the following two matrices are inverses of each other. A = [  1 4

-1 -3 ] , B = [ -3 -4

1 1 ]  Finding the Multiplicative Inverse Using Matrix Multiplication We can now determine whether two matrices are inverses, but how would we find the inverse of a given matrix? Since we know that the product of a matrix and its inverse is the identity matrix, we can find the inverse of a matrix by setting up an equation using matrix multiplication.

---
### 📐 **Example  3**
Finding the Multiplicative Inverse Using Matrix Multiplication Use matrix multiplication to find the inverse of the given matrix.

A = [ 1 -2

2 -3 ]

**Solution**

For this method, we multiply A by a matrix containing unknown constants and set it equal to the identity.

[ 1 -2

2 -3 ]  [ a b

c d ]  = [ 1 0

0 1 ]  Find the product of the two matrices on the left side of the equal sign.

[ 1 -2

2 -3 ]  [ a b

c d ]  = [ 1a - 2c 1b - 2d

2a - 3c 2b - 3d ]  Next, set up a system of equations with the entry in row 1, column 1 of the new matrix equal to the first entry of the identity, 1. Set the entry in row 2, column 1 of the new matrix equal to the corresponding entry of the identity, which is 0.

1a - 2c = 1 R¹

2a - 3c = 0 R² Using row operations, multiply and add as follows: (-2)R¹ + R² → R². Add the equations, and solve for c.

1a - 2c = 1

0 + 1c = -2

c = -2 Back-substitute to solve for a.

a - 2(-2) = 1

a + 4 = 1

a = -3 Write another system of equations setting the entry in row 1, column 2 of the new matrix equal to the corresponding entry of the identity, 0. Set the entry in row 2, column 2 equal to the corresponding entry of the identity.

1b - 2d = 0 R¹

2b - 3d = 1 R² Using row operations, multiply and add as follows: (-2)R¹ + R² = R². Add the two equations and solve for d.

1b - 2d = 0

0 + 1d = 1

d = 1 Once more, back-substitute and solve for b.

b - 2(1) = 0

b - 2 = 0

b = 2

A-1 = [ -3 2

-2 1 ]  Finding the Multiplicative Inverse by Augmenting with the Identity Another way to find the multiplicative inverse is by augmenting with the identity. When matrix A is transformed into I, the augmented matrix I transforms into A-1. For example, given

A = [ 2 1

5 3 ]  augment A with the identity

[ 2 1

5 3 ∣  1 0

0 1 ]  Perform row operations with the goal of turning A into the identity. 1. Switch row 1 and row 2. [ 5 3

2 1 ∣  0 1

1 0 ]  2. Multiply row 2 by -2 and add to row 1. [ 1 1

2 1 ∣  -2 1

1 0 ]  3. Multiply row 1 by -2 and add to row 2. [ 1 1

0 -1 ∣  -2 1

5 -2 ]  4. Add row 2 to row 1. [ 1 0

0 -1 ∣  3 -1

5 -2 ]  5. Multiply row 2 by -1. [ 1 0

0 1 ∣   3 -1

-5 2 ]  The matrix we have found is A-1.

A-1 = [  3 -1

-5 2 ]  Finding the Multiplicative Inverse of 2 ×  2 Matrices Using a Formula When we need to find the multiplicative inverse of a 2 ×  2 matrix, we can use a special formula instead of using matrix multiplication or augmenting with the identity. If A is a 2 ×  2 matrix, such as

A = [ a b

c d ]  the multiplicative inverse of A is given by the formula

A-1 =  _______ ad - bc [ d -b

-c a ]  where ad - bc ≠  0. If ad - bc = 0, then A has no inverse.

---
### 📐 **Example  4**
Using the Formula to Find the Multiplicative Inverse of Matrix A Use the formula to find the multiplicative inverse of

A = [ 1 -2

2 -3 ]

**Solution**

Using the formula, we have

A-1 =  ________________

(1)(-3) - (-2)(2) [ -3 2

-2 1 ] 

=  _______ -3 + 4 [ -3 2

-2 1 ] 

= [ -3 2

-2 1 ]  Analysis We can check that our formula works by using one of the other methods to calculate the inverse. Let’s augment A with the identity. [ 1 -2

2 -3 ∣  1 0

0 1 ]  Perform row operations with the goal of turning A into the identity.

1. Multiply row 1 by -2 and add to row 2. [  1 -2

0 1 ∣   1 0

-2 1 ]  2. Multiply row 1 by 2 and add to row 1. [ 1 0

0 1 ∣  -3 2

-2 1 ]  So, we have verified our original solution.

A-1 = [ -3 2

-2 1 ] 

---
### ✏️ **Try It #2**
Use the formula to find the inverse of matrix A. Verify your answer by augmenting with the identity matrix.

A-1 = [  1 -1

2 3 ] 

---
### 📐 **Example  5**
Finding the Inverse of the Matrix, If It Exists Find the inverse, if it exists, of the given matrix.

A = [ 3 6

1 2 ]

**Solution**

We will use the method of augmenting with the identity. [ 3 6

1 3 ∣  1 0

0 1 ]  1. Switch row 1 and row 2. [ 1 3

3 6 ∣  0 1

1 0 ]  2. Multiply row 1 by -3 and add it to row 2. [ 1 2

0 0 ∣   1 0

-3 1 ]  3. There is nothing further we can do. The zeros in row 2 indicate that this matrix has no inverse. Finding the Multiplicative Inverse of 3 ×  3 Matrices Unfortunately, we do not have a formula similar to the one for a 2 ×  2 matrix to find the inverse of a 3 ×  3 matrix. Instead, we will augment the original matrix with the identity matrix and use row operations to obtain the inverse. Given a 3 ×  3 matrix

A = [ 

 ]  augment A with the identity matrix

 A

A A  I = [ 

 ∣    

 ]  To begin, we write the augmented matrix with the identity on the right and A on the left. Performing elementary row operations so that the identity matrix appears on the left, we will obtain the inverse matrix on the right. We will find the inverse of this matrix in the next example.

---
### 💡 **How To…**
Given a 3 ×  3 matrix, find the inverse 1. Write the original matrix augmented with the identity matrix on the right. 2. Use elementary row operations so that the identity appears on the left. 3. What is obtained on the right is the inverse of the original matrix. 4. Use matrix multiplication to show that AA-1 = I and A-1 A = I.

---
### 📐 **Example  6**
Finding the Inverse of a 3 ×  3 Matrix Given the 3 ×  3 matrix A, find the inverse.

A = [ 

 ]

**Solution**

Augment A with the identity matrix, and then begin row operations until the identity matrix replaces A. The matrix on the right will be the inverse of A. [ 

 ∣    

 ]  [ 

 ∣    

 ] 

-R² + R¹ = R¹ → [ 

 ∣    

 ] 

-R² + R³ = R³ → [ 

 ∣    

 ] 

R³ ↔ R² → [ 

 ∣    

 ] 

-2R¹ + R³ = R³ → [ 

 ∣     -1 1 0

-1 0 1

 ] 

-3R² + R³ = R³ → [ 

 ∣     -1 1 0

-1 0 1

6 -2 -3  ]  Thus,

A-1 = B = [  -1 1 0

-1 0 1

6 -2 -3  ]  Analysis To prove that B = A-1, let’s multiply the two matrices together to see if the product equals the identity, if AA-1 = I and A-1 A = I.

AA-1 = [ 

 ]  [  -1 1 0

-1 0 1

6 -2 -3  ]  = [  2(-1) + 3(-1) + 1(6) 2(1) + 3(0) + 1(-2) 2(0) + 3(1) + 1(-3)

3(-1) + 3(-1) + 1(6) 3(1) + 3(0) + 1(-2) 3(0) + 3(1) + 1(-3)

2(-1) + 4(-1) + 1(6) 2(1) + 4(0) + 1(-2) 2(0) + 4(1) + 1(-3)  ] 

= [ 

 ] 

A-1A = [  -1 1 0

-1 0 1

6 -2 -3  ]  [ 

 ] 

= [  -1(2) + 1(3) + 0(2) -1(3) + 1(3) + 0(4) -1(1) + 1(1) + 0(1)

-1(2) + 0(3) + 1(2) -1(3) + 0(3) + 1(4) -1(1) + 0(1) + 1(1)

6(2) + -2(3) + -3(2) 6(3) + -2(3) + -3(4) 6(1) + -2(1) + -3(1)  ] 

= [ 

 ]  Interchange R² and R¹

---
### ✏️ **Try It #3**
Find the inverse of the 3 ×  3 matrix.

A = [ 

-1 11 -7

0 3 -2  ]  Solving a System of Linear Equations Using the Inverse of a Matrix Solving a system of linear equations using the inverse of a matrix requires the definition of two new matrices: X is the matrix representing the variables of the system, and B is the matrix representing the constants. Using matrix multiplication, we may define a system of equations with the same number of equations as variables as

AX = B To solve a system of linear equations using an inverse matrix, let A be the coefficient matrix, let X be the variable matrix, and let B be the constant matrix. Thus, we want to solve a system AX = B. For example, look at the following system of equations.

a¹x + b¹y = c¹

a²x + b²y = c² From this system, the coefficient matrix is

A = [ a¹ b¹

a² b² ]  The variable matrix is

X = [ x y ]  And the constant matrix is

B = [ c¹ c² ]  Then AX = B looks like

[ a¹ b¹

a² b² ]  [ x y ]  = [ c¹ c² ]  Recall the discussion earlier in this section regarding multiplying a real number by its inverse, (2-1) 2 = (  1/2  ) 2 = 1. To solve a single linear equation ax = b for x, we would simply multiply both sides of the equation by the multiplicative inverse (reciprocal) of a. Thus,

ax = b

(  1/a  ) ax = (  1/a  ) b

(a-1)ax = (a-1)b

[(a-1)a]x = (a-1)b

1x = (a-1)b

x = (a-1)b The only difference between a solving a linear equation and a system of equations written in matrix form is that finding the inverse of a matrix is more complicated, and matrix multiplication is a longer process. However, the goal is the same—to isolate the variable. We will investigate this idea in detail, but it is helpful to begin with a 2 ×  2 system and then move on to a 3 ×  3 system.

solving a system of equations using the inverse of a matrix Given a system of equations, write the coefficient matrix A, the variable matrix X, and the constant matrix B. Then

AX = B Multiply both sides by the inverse of A to obtain the solution.

(A-1)AX = (A-1)B

[(A-1)A]X = (A-1)B

IX = (A-1)B

X = (A-1)B If the coefficient matrix does not have an inverse, does that mean the system has no solution? No, if the coefficient matrix is not invertible, the system could be inconsistent and have no solution, or be dependent and have infinitely many solutions.

---
### 📐 **Example  7**: Solving a 2 ×  2 System Using the Inverse of a Matrix

Solve the given system of equations using the inverse of a matrix.

3x + 8y = 5

4x + 11y = 7

**Solution**

Write the system in terms of a coefficient matrix, a variable matrix, and a constant matrix. A = [  3 8

4 11 ] , X = [ x y ] , B = [ 5 7 ]  Then

[  3 8

4 11 ]  [ x y ]  = [ 5 7 ]  First, we need to calculate A-1. Using the formula to calculate the inverse of a 2 by 2 matrix, we have:

A-1 =  _______ ad - bc [  d -b

-c a ] 

=  ___________ 3(11) - 8(4) [  11 -8

-4 3 ] 

=  1/1 [  11 -8

-4 3 ]  So,

A-1 = [  11 -8

-4 3 ]  Now we are ready to solve. Multiply both sides of the equation by A-1.

(A-1)AX = (A-1)B

[  11 -8

-4 3 ]  [  3 8

4 11 ]  [ x y ]  = [  11 -8

-4 3 ]  [ 5 7 ] 

[ 1 0

0 1 ]  [ x y ]  = [  11(5) + (-8)⁷

-4(5) + 3(7) ] 

[ x y ]  = [ -1 1 ]  The solution is (-1, 1).

Can we solve for X by finding the product BA-1? No, recall that matrix multiplication is not commutative, so A-1 B ≠  BA-1. Consider our steps for solving the matrix equation.

(A-1)AX = (A-1)B

[(A-1)A]X = (A-1)B

IX = (A-1)B

X = (A-1)B Notice in the first step we multiplied both sides of the equation by A-1, but the A-1 was to the left of A on the left side and to the left of B on the right side. Because matrix multiplication is not commutative, order matters.

---
### 📐 **Example  8**: Solving a 3 ×  3 System Using the Inverse of a Matrix

Solve the following system using the inverse of a matrix.

-4x - 11y - 41z = -26

-x - 3y - 11z = -7

**Solution**

Write the equation AX = B. [  5 15 56

-1 -3 -11  ]  [  x

y z  ]  = [ 

-26

-7  ]  First, we will find the inverse of A by augmenting with the identity. [    

-4 -11 -41

-1  -3  -11  ∣        0 1 0    ]  Multiply row 1 by  1/5 . [     56/5  

-4 -11 -41

-1  -3  -11  ∣      1/5     0 1 0    ]  Multiply row 1 by 4 and add to row 2. [     56/5   0 1  19/5 

-1  -3  -11  ∣      1/5      4/5  1 0    ]  Add row 1 to row 3. [       56/5   0 1  19/5     1/5   ∣    1/5      4/5  1 0  1/5     ]  Multiply row 2 by -3 and add to row 1. [      - 1/5   0 1  19/5     1/5   ∣   - 11/5   -3    4/5  1 0  1/5     ]  Multiply row 3 by 5. [      - 1/5   0 1  19/5     ∣   - 11/5   -3    4/5  1 0    ] 

Multiply row 3 by  1/5  and add to row 1. [       0 1  19/5     ∣   -2  -3    4/5  1 0    ]  Multiply row 3 by - 19 ___ 5  and add to row 2. [       0 1 0    ∣   -2  -3  

-3    ]  So, A-1 = [  -2 -3 1

-3 1 -19

1 0 5  ]  Multiply both sides of the equation by A-1. We want A-1AX = A-1B:

[  -2 -3 1

-3 1 -19

1 0 5  ]  [  5 15 56

-1 -3 -11  ]  [  x

y z  ]  = [  -2 -3 1

-3 1 -19

1 0 5  ]  [ 

-26

-7  ]  Thus,

A-1B = [ 

 ]  = [ 

 ]  The solution is (1, 2, 0).

---
### ✏️ **Try It #4**
Solve the system using the inverse of the coefficient matrix.

2x - 17y + 11z = 0

-x + 11y - 7z = 8

3y - 2z = -2

---
### 💡 **How To…**
Given a system of equations, solve with matrix inverses using a calculator. 1. Save the coefficient matrix and the constant matrix as matrix variables [A] and [B]. 2. Enter the multiplication into the calculator, calling up each matrix variable as needed. 3. If the coefficient matrix is invertible, the calculator will present the solution matrix; if the coefficient matrix is not invertible, the calculator will present an error message.

---
### 📐 **Example  9**
Using a Calculator to Solve a System of Equations with Matrix Inverses Solve the system of equations with matrix inverses using a calculator

2x + 3y + z = 32

3x + 3y + z = -27

2x + 4y + z = -2

**Solution**

On the matrix page of the calculator, enter the coefficient matrix as the matrix variable [A], and enter the constant matrix as the matrix variable [B]. [A] = [ 

 ] , [B] = [ 

-27

-2  ] 

On the home screen of the calculator, type in the multiplication to solve for X, calling up each matrix variable as needed.

[A]-1 ×  [B] Evaluate the expression.

[  -59

-34

 ]  Access these online resources for additional instruction and practice with solving systems with inverses. • The Identity Matrix (http://openstaxcollege.org/l/identmatrix) • Determining Inverse Matrices (http://openstaxcollege.org/l/inversematrix) • Using a Matrix Equation to Solve a System of Equations (http://openstaxcollege.org/l/matrixsystem)

### 9.7 Section Exercises

Verbal 1. In a previous section, we showed that matrix multiplication is not commutative, that is, AB ≠  BA in most cases. Can you explain why matrix multiplication is commutative for matrix inverses, that is, A-1 A = AA-1 ? 2. Does every 2 ×  2 matrix have an inverse? Explain why or why not. Explain what condition is necessary for an inverse to exist. 3. Can you explain whether a 2 ×  2 matrix with an entire row of zeros can have an inverse? 4. Can a matrix with an entire column of zeros have an inverse? Explain why or why not. 5. Can a matrix with zeros on the diagonal have an inverse? If so, find an example. If not, prove why not. For simplicity, assume a 2 ×  2 matrix. Algebraic In the following exercises, show that matrix A is the inverse of matrix B. 6. A = [  1 0

-1 1 ] , B = [ 1 0

1 1 ]  7. A = [ 1 2

3 4 ] , B = [ -2 1

 3/2  - 1/2  ]  8. A = [ 4 5

7 0 ] , B = [ 0  1/7 

 1/5  - 4/35  ]  9. A = [ -2  1/2 

3 -1 ] , B = [ -2 -1

-6 -4 ]  10. A = [ 

 ] , B =  1/2 [  2 1 -1

0 1 1

0 -1 1  ]  11. A = [ 

 ] , B = 1/4 [  6 0 -2

-12 2 4  ]  12. A = [ 

 ] , B =  1 ___ 36 [  -6 84 -6

7 -26 1

-1 -22 5  ]  For the following exercises, find the multiplicative inverse of each matrix, if it exists. 13. [  3 -2

1 9 ] 

3 1 ] 

9 2 ]  16. [ -4 -3

-5 8 ] 

2 2 ] 

1 0 ] 

1 -0.5 ]  20. [ 

 ]  21. [ 

 ]  22. [  1 2 -1

-3 4 1

-2 -4 -5  ]  23. [  1 9 -3

2 5 6

4 -2 7  ]  24. [  1 -2 3

-4 8 -12

1 4 2  ]  25. [   1/2    1/2    1/2    1/3   1/4   1/5   1/6    1/7    1/8   ]  26. [ 

 ] 

## 9.7 Section Exercises

---
For the following exercises, solve the system using the inverse of a 2 ×  2 matrix. 4x + 3y = -2 3x - 4y = 1 29. 3x - 2y = 6 -x + 5y = -2 4x + y = 2.3 12x + 4y = -6 32. -2x + 3y =  3 ___ 10  - x + 5y = 1/2  __ 5 x -  4/5 y =  2/5  - 8/5 x +  1/5 y =  7 ___ 10/2 x +  1/5  y = - 1/4   1/2 x -  3/5 y = - 9/4  For the following exercises, solve a system using the inverse of a 3 ×  3 matrix. 5x + 4y = 37 x - 2y - 5z = 5 36. 4x + 4y + 4z = 40 2x - 3y + 4z = -12 -x + 3y + 4z = 9 37. 6x - 5y - z = 31 -x + 2y + z = -6 3x + 3y + 2z = 13 38. 6x - 5y + 2z = -4 2x + 5y - z = 12 2x + 5y + z = 12 2x + 2y - 9z = 33 6y - 4z = 1 ___ 10 x -  1/5 y + 4z = - 41 ___ 2   1/5 x - 20y +  2/3 ___ 10 x + 4y -  3 ___ __ 2 x -  1/5 y +  1/5 z =  31 ___ 100  - 3/4 x -  1/4 y +  1/2 z =  7 ___ 40  - 4/5 x -  1/2 y +  3/2 z = 14 Technology For the following exercises, use a calculator to solve the system of equations with matrix inverses. 43. 2x - y = -3 -x + 2y = 2.3/2 x -  3/2 y = - 43 ___ 20   5/2 x +  11 ___ 5 y =  31 ___ 4  8y - 5z = -10 0.5x + 4y + 5z = 0 Extensions For the following exercises, find the inverse of the given matrix. 47. [  

 ]  49. [   1 -2 3 0

0 1 0 2

1 4 -2 3 

-5 0 1 1  ]  [   

 ]  [    

 ]  [  -1    

0 0 0 2

0 2 -1 0

 -3    ] 

Real-World Applications For the following exercises, write a system of equations that represents the situation. Then, solve the system using the inverse of a matrix. 52. 2,400 tickets were sold for a basketball game. If the prices for floor 1 and floor 2 were different, and the total amount of money brought in is $64,000, how much was the price of each ticket? 53. In the previous exercise, if you were told there were 400 more tickets sold for floor 2 than floor 1, how much was the price of each ticket? 54. A food drive collected two different types of canned goods, green beans and kidney beans. The total number of collected cans was 350 and the total weight of all donated food was 348 lb, 12 oz. If the green bean cans weigh 2 oz less than the kidney bean cans, how many of each can was donated? 55. Students were asked to bring their favorite fruit to class. 95% of the fruits consisted of banana, apple, and oranges. If oranges were twice as popular as bananas, and apples were 5% less popular than bananas, what are the percentages of each individual fruit? 56. A sorority held a bake sale to raise money and sold brownies and chocolate chip cookies. They priced the brownies at $1 and the chocolate chip cookies at $0.75. They raised $700 and sold 850 items. How many brownies and how many cookies were sold? 57. A clothing store needs to order new inventory. It has three different types of hats for sale: straw hats, beanies, and cowboy hats. The straw hat is priced at $13.99, the beanie at $7.99, and the cowboy hat at $14.49. If 100 hats were sold this past quarter, $1,119 was taken in by sales, and the amount of beanies sold was 10 more than cowboy hats, how many of each should the clothing store order to replace those already sold? 58. Anna, Ashley, and Andrea weigh a combined 370 lb. If Andrea weighs 20 lb more than Ashley, and Anna weighs 1.5 times as much as Ashley, how much does each girl weigh? 59. Three roommates shared a package of 12 ice cream bars, but no one remembers who ate how many. If Tom ate twice as many ice cream bars as Joe, and Albert ate three less than Tom, how many ice cream bars did each roommate eat? 60. A farmer constructed a chicken coop out of chicken wire, wood, and plywood. The chicken wire cost $2 per square foot, the wood $10 per square foot, and the plywood $5 per square foot. The farmer spent a total of $51, and the total amount of materials used was 14 ft². He used 3 ft² more chicken wire than plywood. How much of each material in did the farmer use? 61. Jay has lemon, orange, and pomegranate trees in his backyard. An orange weighs 8 oz, a lemon 5 oz, and a pomegranate 11 oz. Jay picked 142 pieces of fruit weighing a total of 70 lb, 10 oz. He picked 15.5 times more oranges than pomegranates. How many of each fruit did Jay pick?

