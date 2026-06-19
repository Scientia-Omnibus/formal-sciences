# Systems of Equations and Inequalities

## Introduction
By 1943, it was obvious to the Nazi regime that defeat was imminent unless it could build a weapon with unlimited destructive power, one that had never been seen before in the history of the world. In September, Adolf Hitler ordered German scientists to begin building an atomic bomb. Rumors and whispers began to spread from across the ocean. Refugees and diplomats told of the experiments happening in Norway. However, Franklin D. Roosevelt wasn’t sold, and even doubted British Prime Minister Winston Churchill’s warning. Roosevelt wanted undeniable proof. Fortunately, he soon received the proof he wanted when a group of mathematicians cracked the “Enigma” code, proving beyond a doubt that Hitler was building an atomic bomb. The next day, Roosevelt gave the order that the United States begin work on the same. The Enigma is perhaps the most famous cryptographic device ever known. It stands as an example of the pivotal role cryptography has played in society. Now, technology has moved cryptanalysis to the digital world. Many ciphers are designed using invertible matrices as the method of message transference, as finding the inverse of a matrix is generally part of the process of decoding. In addition to knowing the matrix and its inverse, the receiver must also know the key that, when used with the matrix inverse, will allow the message to be read. In this chapter, we will investigate matrices and their inverses, and various ways to use matrices to solve systems of equations. First, however, we will study systems of equations on their own: linear and nonlinear, and then partial fractions. We will not be breaking any secret codes here, but we will lay the foundation for future courses. 9.1 Systems of Linear Equations: Two Variables 9.2 Systems of Linear Equations: Three Variables 9.3 Systems of Nonlinear Equations and Inequalities: Two Variables 9.4 Partial Fractions 9.5 Matrices and Matrix Operations 9.6 Solving Systems with Gaussian Elimination 9.7 Solving Systems with Inverses 9.8 Solving Systems with Cramer's Rule


## 9.1 Systems of Linear Equations: Two variables
A skateboard manufacturer introduces a new line of boards. The manufacturer tracks its costs, which is the amount it spends to produce the boards, and its revenue, which is the amount it earns through sales of its boards. How can the company determine if it is making a profit with its new line? How many skateboards must be produced and sold before a profit is possible? In this section, we will consider linear equations with two variables to answer these and similar questions. Introduction to Systems of Equations In order to investigate situations such as that of the skateboard manufacturer, we need to recognize that we are dealing with more than one variable and likely more than one equation. A system of linear equations consists of two or more linear equations made up of two or more variables such that all equations in the system are considered simultaneously. To find the unique solution to a system of linear equations, we must find a numerical value for each variable in the system that will satisfy all equations in the system at the same time. Some linear systems may not have a solution and others may have an infinite number of solutions. In order for a linear system to have a unique solution, there must be at least as many equations as there are variables. Even so, this does not guarantee a unique solution. In this section, we will look at systems of linear equations in two variables, which consist of two equations that contain two different variables. For example, consider the following system of linear equations in two variables.

2x + y = 15

3x - y = 5 The solution to a system of linear equations in two variables is any ordered pair that satisfies each equation independently. In this example, the ordered pair (4, 7) is the solution to the system of linear equations. We can verify the solution by substituting the values into each equation to see if the ordered pair satisfies both equations. Shortly we will investigate methods of finding such a solution if it exists.

2(4) + (7) = 15 True

3(4) - (7) = 5 True In addition to considering the number of equations and variables, we can categorize systems of linear equations by the number of solutions. A consistent system of equations has at least one solution. A consistent system is considered to be an independent system if it has a single solution, such as the example we just explored. The two lines have Learning Objectives
In this section, you will:
• Solve systems of equations by graphing.
• Solve systems of equations by substitution.
• Solve systems of equations by addition.
• Identify inconsistent systems of equations containing two variables.
• Express the solution of a system of dependent equations containing two variables.
different slopes and intersect at one point in the plane. A consistent system is considered to be a dependent system if the equations have the same slope and the same y-intercepts. In other words, the lines coincide so the equations represent the same line. Every point on the line represents a coordinate pair that satisfies the system. Thus, there are an infinite number of solutions. Another type of system of linear equations is an inconsistent system, which is one in which the equations represent two parallel lines. The lines have the same slope and different y-intercepts. There are no points common to both lines; hence, there is no solution to the system. types of linear systems There are three types of systems of linear equations in two variables, and three types of solutions. • An independent system has exactly one solution pair (x, y). The point where the two lines intersect is the only solution. • An inconsistent system has no solution. Notice that the two lines are parallel and will never intersect. • A dependent system has infinitely many solutions. The lines are coincident. They are the same line, so every coordinate pair on the line is a solution to both equations.   y x y x y x

**How To…**
Given a system of linear equations and an ordered pair, determine whether the ordered pair is a solution. 1. Substitute the ordered pair into each equation in the system. 2. Determine whether true statements result from the substitution in both equations; if so, the ordered pair is a solution.

**Example  1**

### Determining Whether an Ordered Pair Is a Solution to a System of Equations
Determine whether the ordered pair (5, 1) is a solution to the given system of equations.

x + 3y = 8

2x - 9 = y Solution Substitute the ordered pair (5, 1) into both equations.

(5) + 3(1) = 8

8 = 8 True

2(5) - 9 = (1)

1 = 1 True The ordered pair (5, 1) satisfies both equations, so it is the solution to the system. Analysis We can see the solution clearly by plotting the graph of each equation. Since the solution is an ordered pair that satisfies both equations, it is a point on both of the lines and thus the point of intersection of the two lines. See Figure 3.

x y 2x - 9 = y x +3y = 8

**Try It #1**
Determine whether the ordered pair (8, 5) is a solution to the following system.

5x - 4y = 20

2x + 1 = 3y Solving Systems of Equations by Graphing There are multiple methods of solving systems of linear equations. For a system of linear equations in two variables, we can determine both the type of system and the solution by graphing the system of equations on the same set of axes.

**Example  2**

### Solving a System of Equations in Two Variables by Graphing
Solve the following system of equations by graphing. Identify the type of system.

2x + y = -8

x - y = -1 Solution Solve the first equation for y.

2x + y = -8

y = - 2x -8 Solve the second equation for y.

x - y = -1

y = x + 1 Graph both equations on the same set of axes as in Figure 4. x y y = -2x -8 y = x + 1

The lines appear to intersect at the point (-3, -2). We can check to make sure that this is the solution to the system by substituting the ordered pair into both equations.

2(-3) + (-2) = -8

-8 = -8 True

(-3) - (-2) = -1

-1 = -1 True The solution to the system is the ordered pair (-3, -2), so the system is independent.

**Try It #2**
Solve the following system of equations by graphing.

2x - 5y = -25

-4x + 5y = 35 Can graphing be used if the system is inconsistent or dependent? Yes, in both cases we can still graph the system to determine the type of system and solution. If the two lines are parallel, the system has no solution and is inconsistent. If the two lines are identical, the system has infinite solutions and is a dependent system. Solving Systems of Equations by Substitution Solving a linear system in two variables by graphing works well when the solution consists of integer values, but if our solution contains decimals or fractions, it is not the most precise method. We will consider two more methods of solving a system of linear equations that are more precise than graphing. One such method is solving a system of equations by the substitution method, in which we solve one of the equations for one variable and then substitute the result into the second equation to solve for the second variable. Recall that we can solve for only one variable at a time, which is the reason the substitution method is both valuable and practical.

**How To…**
Given a system of two equations in two variables, solve using the substitution method. 1. Solve one of the two equations for one of the variables in terms of the other. 2. Substitute the expression for this variable into the second equation, then solve for the remaining variable. 3. Substitute that solution into either of the original equations to find the value of the first variable. If possible, write the solution as an ordered pair. 4. Check the solution in both equations.

**Example  3**

### Solving a System of Equations in Two Variables by Substitution
Solve the following system of equations by substitution.

-x + y = -5

2x - 5y = 1 Solution First, we will solve the first equation for y.

-x + y = -5

y = x - 5

Now we can substitute the expression x - 5 for y in the second equation.

2x - 5y = 1

2x - 5(x - 5) = 1

2x - 5x + 25 = 1

-3x = -24

x = 8 Now, we substitute x = 8 into the first equation and solve for y.

-(8) + y = -5

y = 3 Our solution is (8, 3). Check the solution by substituting (8, 3) into both equations.

-x + y = - 5

-(8) + (3) = - 5 True

2x - 5y = 1

2(8) - 5(3) = 1 True

**Try It #3**
Solve the following system of equations by substitution.

x = y + 3

4 = 3x - 2y Can the substitution method be used to solve any linear system in two variables? Yes, but the method works best if one of the equations contains a coefficient of 1 or -1 so that we do not have to deal with fractions. Solving Systems of Equations in Two Variables by the Addition Method A third method of solving systems of linear equations is the addition method. In this method, we add two terms with the same variable, but opposite coefficients, so that the sum is zero. Of course, not all systems are set up with the two terms of one variable having opposite coefficients. Often we must adjust one or both of the equations by multiplication so that one variable will be eliminated by addition.

**How To…**
Given a system of equations, solve using the addition method. 1. Write both equations with x- and y-variables on the left side of the equal sign and constants on the right. 2. Write one equation above the other, lining up corresponding variables. If one of the variables in the top equation has the opposite coefficient of the same variable in the bottom equation, add the equations together, eliminating one variable. If not, use multiplication by a nonzero number so that one of the variables in the top equation has the opposite coefficient of the same variable in the bottom equation, then add the equations to eliminate the variable. 3. Solve the resulting equation for the remaining variable. 4. Substitute that value into one of the original equations and solve for the second variable. 5. Check the solution by substituting the values into the other equation.


**Example  4**

### Solving a System by the Addition Method
Solve the given system of equations by addition.

x + 2y = -1

-x + y = 3 Solution Both equations are already set equal to a constant. Notice that the coefficient of x in the second equation, -1, is the opposite of the coefficient of x in the first equation, 1. We can add the two equations to eliminate x without needing to multiply by a constant.

x + 2y = - 1

-x + y = 3

3y = 2 Now that we have eliminated x, we can solve the resulting equation for y.

3y = 2

y =  2 _ 3  Then, we substitute this value for y into one of the original equations and solve for x.

-x + y = 3

-x +  2 __ 3  = 3

-x = 3 -  2 _ 3 

-x =  7 _ 3 

x = - 7 _ 3  The solution to this system is  - 7 __ 3 ,  2 __ 3    Check the solution in the first equation.

x + 2y = -1

 - 7 __ 3   + 2  2 __ 3   = -1

- 7 __ 3  +  4 __ 3  = -1

- 3 __ 3  = -1

-1 = -1 True Analysis We gain an important perspective on systems of equations by looking at the graphical representation. See because observing the graph confirms that the system has exactly one solution. x + 2y = -1 x y -x + y = 3


**Example  5**
Using the Addition Method When Multiplication of One Equation Is Required Solve the given system of equations by the addition method.

3x + 5y = -11

x - 2y = 11 Solution Adding these equations as presented will not eliminate a variable. However, we see that the first equation has 3x in it and the second equation has x. So if we multiply the second equation by -3, the x-terms will add to zero.

x - 2y = 11

-3(x - 2y) = -3(11) Multiply both sides by -3.

-3x + 6y = -33

Use the distributive property. Now, let’s add them.

3x + 5y = -11

-3x + 6y = -33

y = -4 For the last step, we substitute y = -4 into one of the original equations and solve for x.

3x + 5y = - 11

3x + 5( - 4) = - 11

3x = 9

x = 3 Our solution is the ordered pair (3, -4). See Figure 6. Check the solution in the original second equation.

x - 2y = 11

(3) - 2( - 4) = 3 + 8

True x y x - 2y = 11 3x + 5y = -11

**Try It #4**
Solve the system of equations by addition.

2x - 7y = 2

3x + y = -20

**Example  6**
Using the Addition Method When Multiplication of Both Equations Is Required Solve the given system of equations in two variables by addition.

2x + 3y = -16

Solution One equation has 2x and the other has 5x. The least common multiple is 10x so we will have to multiply both equations by a constant in order to eliminate one variable. Let’s eliminate x by multiplying the first equation by -5 and the second equation by 2.

- 5(2x + 3y) = -5(-16)

Then, we add the two equations together.

y = -4 Substitute y = -4 into the original first equation.

2x + 3(-4) = -16

2x = -4

x = -2 The solution is (-2, -4). Check it in the other equation.

See Figure 7. x y 2x + 3y = -16

**Example  7**
Using the Addition Method in Systems of Equations Containing Fractions Solve the given system of equations in two variables by addition.

 x __ 3  +  y __ 6  = 3

 x __ 2  -  y __ 4  = 1 Solution First clear each equation of fractions by multiplying both sides of the equation by the least common denominator.

6  x __ 3  +  y __ 6    = 6(3)

2x + y = 18

4  x __ 2  -  y __ 4    = 4(1)

2x - y = 4

Now multiply the second equation by -1 so that we can eliminate the x-variable.

-1(2x - y) = -1(4)

-2x + y = -4 Add the two equations to eliminate the x-variable and solve the resulting equation.

2x + y = 18

-2x + y = -4

y = 7 Substitute y = 7 into the first equation.

2x + (7) = 18

x =  11 ___ 2 

= 5.5 The solution is   11 ___ 2 , 7  . Check it in the other equation.

 x __ 2  -  y __ 4  = 1

  11 _ 2  ____ 2  -  7 __ 4  = 1

 11 ___ 4  -  7 __ 4  = 1

 4 __ 4  = 1

**Try It #5**
Solve the system of equations by addition.

2x + 3y = 8

3x + 5y = 10 Identifying Inconsistent Systems of Equations Containing Two Variables Now that we have several methods for solving systems of equations, we can use the methods to identify inconsistent systems. Recall that an inconsistent system consists of parallel lines that have the same slope but different y-intercepts. They will never intersect. When searching for a solution to an inconsistent system, we will come up with a false statement, such as 12 = 0.

**Example  8**

### Solving an Inconsistent System of Equations
Solve the following system of equations.

x = 9 - 2y

x + 2y = 13 Solution We can approach this problem in two ways. Because one equation is already solved for x, the most obvious step is to use substitution.

x + 2y = 13

(9 - 2y) + 2y = 13

Clearly, this statement is a contradiction because 9 \neq  13. Therefore, the system has no solution.

The second approach would be to first manipulate the equations so that they are both in slope-intercept form. We manipulate the first equation as follows.

x = 9 - 2y

2y = - x + 9

y = -  1 __ 2 x +  9 __ 2  We then convert the second equation expressed to slope-intercept form.

x + 2y = 13

2y = - x + 13

y = - 1 __ 2 x +  13 ___ 2  Comparing the equations, we see that they have the same slope but different y-intercepts. Therefore, the lines are parallel and do not intersect.

y = - 1 __ 2 x +  9 __ 2 

y = - 1 __ 2 x +  13 ___ 2  Analysis Writing the equations in slope-intercept form confirms that the system is inconsistent because all lines will intersect eventually unless they are parallel. Parallel lines will never intersect; thus, the two lines have no points in common. The graphs of the equations in this example are shown in Figure 8. x y y = -x + y = -x +

**Try It #6**
Solve the following system of equations in two variables.

2y - 2x = 2

2y - 2x = 6 Expressing the Solution of a System of Dependent Equations Containing Two Variables Recall that a dependent system of equations in two variables is a system in which the two equations represent the same line. Dependent systems have an infinite number of solutions because all of the points on one line are also on the other line. After using substitution or addition, the resulting equation will be an identity, such as 0 = 0.

**Example  9**
Finding a Solution to a Dependent System of Linear Equations Find a solution to the system of equations using the addition method.

x + 3y = 2

3x + 9y = 6 Solution With the addition method, we want to eliminate one of the variables by adding the equations. In this case, let’s focus on eliminating x. If we multiply both sides of the first equation by -3, then we will be able to eliminate the x-variable.

x + 3y = 2

(-3)(x + 3y) = (-3)(2)

-3x - 9y = - 6 Now add the equations.

-3x - 9y = -6

+ 3x + 9y = 6

0 = 0 We can see that there will be an infinite number of solutions that satisfy both equations. Analysis If we rewrote both equations in the slope-intercept form, we might know what the solution would look like before adding. Let’s look at what happens when we convert the system to slope-intercept form.

x + 3y = 2

3y = - x + 2

y = - 1 __ 3 x +  2 __ 3 

3x + 9y = 6

9y = -3x + 6

y = - 3 __ 9 x +  6 __ 9 

y = - 1 __ 3 x +  2 __ 3  See Figure 9. Notice the results are the same. The general solution to the system is  x, - 1 _ 3 x +  2 _ 3   . x y x + 3y = 2 3x + 9y = 6

**Try It #7**
Solve the following system of equations in two variables.

y - 2x = 5

-3y + 6x = -15 Using Systems of Equations to Investigate Profits Using what we have learned about systems of equations, we can return to the skateboard manufacturing problem at the beginning of the section. The skateboard manufacturer’s revenue function is the function used to calculate the amount of money that comes into the business. It can be represented by the equation R = xp, where x = quantity and p = price. The revenue function is shown in orange in Figure 10. The cost function is the function used to calculate the costs of doing business. It includes fixed costs, such as rent and salaries, and variable costs, such as utilities. The cost function is shown in blue in Figure 10. The x-axis represents quantity in hundreds of units. The y-axis represents either cost or revenue in hundreds of dollars.

Money (in hundreds of dollars) Revenue Break-even Cost Quantity (in hundreds of units) Profit The point at which the two lines intersect is called the break-even point. We can see from the graph that if 700 units are produced, the cost is $3,300 and the revenue is also $3,300. In other words, the company breaks even if they produce and sell 700 units. They neither make money nor lose money. The shaded region to the right of the break-even point represents quantities for which the company makes a profit. The shaded region to the left represents quantities for which the company suffers a loss. The profit function is the revenue function minus the cost function, written as P(x) = R(x) - C(x). Clearly, knowing the quantity for which the cost equals the revenue is of great importance to businesses.

**Example  10**
Finding the Break-Even Point and the Profit Function Using Substitution Given the cost function C(x) = 0.85x + 35,000 and the revenue function R(x) = 1.55x, find the break-even point and the profit function. Solution Write the system of equations using y to replace function notation.

Substitute the expression 0.85x + 35,000 from the first equation into the second equation and solve for x.

Then, we substitute x = 50,000 into either the cost function or the revenue function.

The break-even point is (50,000, 77,500). The profit function is found using the formula P(x) = R(x) - C(x).

The profit function is P(x) = 0.7x - 35,000. Analysis The cost to produce 50,000 units is $77,500, and the revenue from the sales of 50,000 units is also $77,500. To make a profit, the business must produce and sell more than 50,000 units. See Figure 11. We see from the graph in Figure 12 that the profit function has a negative value until x = 50,000, when the graph crosses the x-axis. Then, the graph emerges into positive y-values and continues on this path as the profit function is a straight line. This illustrates that the break-even point for businesses occurs when the profit function is 0. The area to the left of the break-even point represents operating at a loss.

Dollars Quantity Break-even point Profit Cost Revenue R(x) = 1.55x Dollars profit Quantity Profit Break-even point Profit

**Example  11**

### Writing and Solving a System of Equations in Two Variables
The cost of a ticket to the circus is $25.00 for children and $50.00 for adults. On a certain day, attendance at the circus is 2,000 and the total gate revenue is $70,000. How many children and how many adults bought tickets? Solution Let c = the number of children and a = the number of adults in attendance. The total number of people is 2,000. We can use this to write an equation for the number of people at the circus that day.

The revenue from all children can be found by multiplying $25.00 by the number of children, 25c. The revenue from all adults can be found by multiplying $50.00 by the number of adults, 50a. The total revenue is $70,000. We can use this to write an equation for the revenue.

We now have a system of linear equations in two variables.

In the first equation, the coefficient of both variables is 1. We can quickly solve the first equation for either c or a. We will solve for a.

Substitute the expression 2,000 - c in the second equation for a and solve for c.

Substitute c = 1,200 into the first equation to solve for a.

We find that 1,200 children and 800 adults bought tickets to the circus that day.

**Try It #8**
Meal tickets at the circus cost $4.00 for children and $12.00 for adults. If 1,650 meal tickets were bought for a total of $14,200, how many children and how many adults bought meal tickets? Access these online resources for additional instruction and practice with systems of linear equations. • Solving Systems of Equations Using Substitution (http://openstaxcollege.org/l/syssubst) • Solving Systems of Equations Using Elimination (http://openstaxcollege.org/l/syselim) • Applications of Systems of Equations (http://openstaxcollege.org/l/sysapp)


## 9.1 Section Exercises

### 9.1 Section Exercises
Verbal 1. Can a system of linear equations have exactly two solutions? Explain why or why not. 2. If you are performing a break-even analysis for a business and their cost and revenue equations are dependent, explain what this means for the company’s profit margins. 3. If you are solving a break-even analysis and get a negative break-even point, explain what this signifies for the company? 4. If you are solving a break-even analysis and there is no break-even point, explain what this means for the company. How should they ensure there is a break-even point? 5. Given a system of equations, explain at least two different methods of solving that system. Algebraic For the following exercises, determine whether the given ordered pair is a solution to the system of equations. 6. 5x - y = 4 x + 6y = 2 and (4, 0) - x + 4y = 10 and (-6, 1) 2x + 4y = 0 and (2, 3) 9. -2x + 5y = 7 2x + 9y = 7 and (-1, 1) 3x - 2y = -1 and (3, 5) For the following exercises, solve each system by substitution. 11. x + 3y = 5 2x + 3y = 4 3x + 9y = 0 16. x - 0.2y = 1 -10x + 2y = 5 17. 3 x + 5y = 9 18. -3x + y = 2 12x - 4y = -8 __ 2  x +  1 __ 3 y = 16  1 __ 6 x +  1 __ 4 y = 9 __ 4 x +  3 __ 2 y = 11 - 1 __ 8 x +  1 __ 3 y = 3 For the following exercises, solve each system by addition. 7x + 2y = 30 2x + 6y = 4 23. 5x - y = -2.6 25. -x + 2y = -1 5x - 10y = 6 26. 7x + 6y = 2 -28x - 24y = -8 __ 6 x +  1 __ 4 y = 0  1 __ 8 x -  1 __ 2 y = - 43 ___ 120  __ 3 x +  1 __ 9 y =  2 __ 9  - 1 __ 2 x +  4 __ 5 y = - 1 __ 3  x - 2y = -3 5x - 10y = 1 For the following exercises, solve each system by any method. x + 2y = 4 7x - 4y = 3 34. x -  5 ___ 12 y = - 55 ___ 12  -6x +  5 __ 2 y =  55 ___ 2 

35. 7x - 4y =  7 __ 6  2x + 4y =  1 __ 3  2x + 4y = 9 __ 3 x -  1 __ 6 y = 2 - 21 ___ 6 x +  3 ___ 12 y = -3 __ 2 x +  1 __ 3 y =  1 __ 3   3 __ 2 x +  1 __ 4 y = - 1 __ 8  Graphical For the following exercises, graph the system of equations and state whether the system is consistent, inconsistent, or dependent and whether the system has one solution, no solution, or infinite solutions. x - 2y = 1.3 42. -x + 2y = 4 2x - 4y = 1 43. x + 2y = 7 2x + 6y = 12 x - 2y = 3 45. 3x - 2y = 5 -9x + 6y = -15 Technology For the following exercises, use the intersect function on a graphing device to solve each system. Round all answers to the nearest hundredth. Extensions For the following exercises, solve each system in terms of A, B, C, D, E, and F where A – F are nonzero numbers. Note that A \neq  B and AE \neq  BD. 51. x + y = A x - y = B 52. x + Ay = 1 x + By = 1 53. Ax + y = 0 Bx + y = 1 54. Ax + By = C x + y = 1 55. Ax + By = C Dx + Ey = F Real-World Applications For the following exercises, solve for the desired quantity. 56. A stuffed animal business has a total cost of production C = 12x + 30 and a revenue function R = 20x. Find the break-even point. 57. A fast-food restaurant has a cost of production C(x) = 11x + 120 and a revenue function R(x) = 5x. When does the company start to turn a profit? 58. A cell phone factory has a cost of production C(x) = 150x + 10,000 and a revenue function R(x) = 200x. What is the break-even point? 59. A musician charges C(x) = 64x + 20,000, where x is the total number of attendees at the concert. The venue charges $80 per ticket. After how many people buy tickets does the venue break even, and what is the value of the total tickets sold at that point? 60. A guitar factory has a cost of production C(x) = 75x + 50,000. If the company needs to break even after 150 units sold, at what price should they sell each guitar? Round up to the nearest dollar, and write the revenue function.

For the following exercises, use a system of linear equations with two variables and two equations to solve. 61. Find two numbers whose sum is 28 and difference 62. A number is 9 more than another number. Twice the sum of the two numbers is 10. Find the two numbers. 63. The startup cost for a restaurant is $120,000, and each meal costs $10 for the restaurant to make. If each meal is then sold for $15, after how many meals does the restaurant break even? 64. A moving company charges a flat rate of $150, and an additional $5 for each box. If a taxi service would charge $20 for each box, how many boxes would you need for it to be cheaper to use the moving company, and what would be the total cost? 65. A total of 1,595 first- and second-year college students gathered at a pep rally. The number of freshmen exceeded the number of sophomores by 15. How many freshmen and sophomores were in attendance? 66. 276 students enrolled in a freshman-level chemistry class. By the end of the semester, 5 times the number of students passed as failed. Find the number of students who passed, and the number of students who failed. 67. There were 130 faculty at a conference. If there were 18 more women than men attending, how many of each gender attended the conference? 68. A jeep and BMW enter a highway running east- west at the same exit heading in opposite directions. The jeep entered the highway 30 minutes before the BMW did, and traveled 7 mph slower than the BMW. After 2 hours from the time the BMW entered the highway, the cars were 306.5 miles apart. Find the speed of each car, assuming they were driven on cruise control. 69. If a scientist mixed 10% saline solution with 60% saline solution to get 25 gallons of 40% saline solution, how many gallons of 10% and 60% solutions were mixed? 70. An investor earned triple the profits of what she earned last year. If she made $500,000.48 total for both years, how much did she earn in profits each year? 71. An investor who dabbles in real estate invested 1.1 million dollars into two land investments. On the first investment, Swan Peak, her return was a 110% increase on the money she invested. On the second investment, Riverside Community, she earned 50% over what she invested. If she earned $1 million in profits, how much did she invest in each of the land deals? 72. If an investor invests a total of $25,000 into two bonds, one that pays 3% simple interest, and the other that pays 2 7 __ 8  % interest, and the investor earns $737.50 annual interest, how much was invested in each account? 73. If an investor invests $23,000 into two bonds, one that pays 4% in simple interest, and the other paying 2% simple interest, and the investor earns $710.00 annual interest, how much was invested in each account? 74. CDs cost $5.96 more than DVDs at All Bets Are Off Electronics. How much would 6 CDs and 2 DVDs cost if 5 CDs and 2 DVDs cost $127.73? 75. A store clerk sold 60 pairs of sneakers. The high-tops sold for $98.99 and the low-tops sold for $129.99. If the receipts for the two types of sales totaled $6,404.40, how many of each type of sneaker were sold? 76. A concert manager counted 350 ticket receipts the day after a concert. The price for a student ticket was $12.50, and the price for an adult ticket was $16.00. The register confirms that $5,075 was taken in. How many student tickets and adult tickets were sold? 77. Admission into an amusement park for 4 children and 2 adults is $116.90. For 6 children and 3 adults, the admission is $175.35. Assuming a different price for children and adults, what is the price of the child’s ticket and the price of the adult ticket?


## 9.2 Systems of Linear Equations: Three variables
John received an inheritance of $12,000 that he divided into three parts and invested in three ways: in a money-market fund paying 3% annual interest; in municipal bonds paying 4% annual interest; and in mutual funds paying 7% annual interest. John invested $4,000 more in municipal funds than in municipal bonds. He earned $670 in interest the first year. How much did John invest in each type of fund? Understanding the correct approach to setting up problems such as this one makes finding a solution a matter of following a pattern. We will solve this and similar problems involving three equations and three variables in this section. Doing so uses similar techniques as those used to solve systems of two equations in two variables. However, finding solutions to systems of three equations requires a bit more organization and a touch of visual gymnastics. Solving Systems of Three Equations in Three Variables In order to solve systems of equations in three variables, known as three-by-three systems, the primary tool we will be using is called Gaussian elimination, named after the prolific German mathematician Karl Friedrich Gauss. While there is no definitive order in which operations are to be performed, there are specific guidelines as to what type of moves can be made. We may number the equations to keep track of the steps we apply. The goal is to eliminate one variable at a time to achieve upper triangular form, the ideal form for a three-by-three system because it allows for straightforward back-substitution to find a solution (x, y, z), which we call an ordered triple. A system in upper triangular form looks like the following:

Ax + By + Cz = D

Ey + Fz = G

Hz = K The third equation can be solved for z, and then we back-substitute to find y and x. To write the system in upper triangular form, we can perform the following operations: 1. Interchange the order of any two equations. 2. Multiply both sides of an equation by a nonzero constant. 3. Add a nonzero multiple of one equation to another equation. Learning Objectives
In this section, you will:
• Solve systems of three equations in three variables.
• Identify inconsistent systems of equations containing three variables.
• Express the solution of a system of dependent equations containing three variables.
The solution set to a three-by-three system is an ordered triple {(x, y, z)}. Graphically, the ordered triple defines the point that is the intersection of three planes in space. You can visualize such an intersection by imagining any corner in a rectangular room. A corner is defined by three planes: two adjoining walls and the floor (or ceiling). Any point where two walls and the floor meet represents the intersection of three planes. number of possible solutions • Systems that have a single solution are those which, after elimination, result in a solution set consisting of an ordered triple {(x, y, z)}. Graphically, the ordered triple defines a point that is the intersection of three planes in space. • Systems that have an infinite number of solutions are those which, after elimination, result in an expression that is always true, such as 0 = 0. Graphically, an infinite number of solutions represents a line or coincident plane that serves as the intersection of three planes in space. • Systems that have no solution are those that, after elimination, result in a statement that is a contradiction, such as 3 = 0. Graphically, a system with no solution is represented by three planes with no point in common. (a) (b) ( b) Three planes intersect in a line, representing a three-by-three system with infinite solutions. (a) (b) (c) (b) Two of the planes are parallel and intersect with the third plane, but not with each other. ( c) All three planes are parallel, so there is no point of intersection.

**Example  1**

### Determining Whether an Ordered Triple Is a Solution to a System
Determine whether the ordered triple (3, -2, 1) is a solution to the system.

x + y + z = 2

6x - 4y + 5z = 31

5x + 2y + 2z = 13 Solution We will check each equation by substituting in the values of the ordered triple for x, y, and z.

x + y + z = 2

(3) + (-2) + (1) = 2

True

6x - 4y + 5z = 31

6(3) - 4(-2) + 5(1) = 31

True

5x + 2y + 2z = 13

5(3) + 2(-2) + 2(1) = 13

True The ordered triple (3, -2, 1) is indeed a solution to the system.

**How To…**
Given a linear system of three equations, solve for three unknowns. 1. Pick any pair of equations and solve for one variable. 2. Pick another pair of equations and solve for the same variable. 3. You have created a system of two equations in two unknowns. Solve the resulting two-by-two system. 4. Back-substitute known variables into any one of the original equations and solve for the missing variable.

**Example  2**

### Solving a System of Three Equations in Three Variables by Elimination
Find a solution to the following system:

x - 2y + 3z = 9 (1)

-x + 3y - z = -6 (2)

2x - 5y + 5z = 17 (3) Solution There will always be several choices as to where to begin, but the most obvious first step here is to eliminate x by adding equations (1) and (2).

x - 2y + 3z = 9 (1)

-x + 3y - z = -6 (2)

y + 2z = 3 (3) The second step is multiplying equation (1) by -2 and adding the result to equation (3). These two steps will eliminate the variable x.

-2x + 4y - 6z = -18 (1) multiplied by - 2

2x - 5y + 5z = 17 (3)

- y - z = -1 (5) In equations (4) and (5), we have created a new two-by-two system. We can solve for z by adding the two equations.

y + 2z = 3 (4)

-y - z = - 1 (5)

z = 2 (6) Choosing one equation from each new system, we obtain the upper triangular form:

x - 2y + 3z = 9 (1)

y + 2z = 3 (4)

z = 2 (6) Next, we back-substitute z = 2 into equation (4) and solve for y.

y + 2(2) = 3

y + 4 = 3

y = -1 Finally, we can back-substitute z = 2 and y = -1 into equation (1). This will yield the solution for x.

x - 2(-1) + 3(2) = 9

x + 2 + 6 = 9

x = 1

The solution is the ordered triple (1, -1, 2). See Figure 4. x = 1 z = 2 y = -2

**Example  3**
Solving a Real-World Problem Using a System of Three Equations in Three Variables In the problem posed at the beginning of the section, John invested his inheritance of $12,000 in three different funds: part in a money-market fund paying 3% interest annually; part in municipal bonds paying 4% annually; and the rest in mutual funds paying 7% annually. John invested $4,000 more in mutual funds than he invested in municipal bonds. The total interest earned in one year was $670. How much did he invest in each type of fund? Solution To solve this problem, we use all of the information given and set up three equations. First, we assign a variable to each of the three investment amounts:

x = amount invested in money-market fund

y = amount invested in municipal bonds

z = amount invested in mutual funds The first equation indicates that the sum of the three principal amounts is $12,000.

x + y + z = 12,000 We form the second equation according to the information that John invested $4,000 more in mutual funds than he invested in municipal bonds.

The third equation shows that the total amount of interest earned from each fund equals $670.

Then, we write the three equations as a system.

x + y + z = 12,000

- y + z = 4,000

To make the calculations simpler, we can multiply the third equation by 100. Thus,

x + y + z = 12,000 (1)

- y + z = 4,000 (2)

(3) Step 1. Interchange equation (2) and equation (3) so that the two equations with three variables will line up.

x + y + z = 12,000

- y + z = 4,000 Step 2. Multiply equation (1) by -3 and add to equation (2). Write the result as row 2.

x + y + z = 12,000

- y + z = 4,000

Step 3. Add equation (2) to equation (3) and write the result as equation (3).

x + y + z = 12,000

Step 4. Solve for z in equation (3). Back-substitute that value in equation (2) and solve for y. Then, back-substitute the values for z and y into equation (1) and solve for x.

John invested $2,000 in a money-market fund, $3,000 in municipal bonds, and $7,000 in mutual funds.

**Try It #1**
Solve the system of equations in three variables.

2x + y - 2z = -1

3x - 3y - z = 5

x - 2y + 3z = 6 Identifying Inconsistent Systems of Equations Containing Three Variables Just as with systems of equations in two variables, we may come across an inconsistent system of equations in three variables, which means that it does not have a solution that satisfies all three equations. The equations could represent three parallel planes, two parallel planes and one intersecting plane, or three planes that intersect the other two but not at the same location. The process of elimination will result in a false statement, such as 3 = 7 or some other contradiction.

**Example  4**

### Solving an Inconsistent System of Three Equations in Three Variables
Solve the following system.

x - 3y + z = 4 (1)

-x + 2y - 5z = 3 (2)

5x - 13y + 13z = 8 (3) Solution Looking at the coefficients of x, we can see that we can eliminate x by adding equation (1) to equation (2).

x - 3y + z = 4 (1)

-x + 2y - 5z = 3 (2)

-y - 4z = 7 (4) Next, we multiply equation (1) by -5 and add it to equation (3).

-5x + 15y - 5z = -20 (1) multiplied by -5

5x - 13y + 13z = 8 (3)

2y + 8z = -12 (5) Then, we multiply equation (4) by 2 and add it to equation (5).

-2y - 8z = 14 (4) multiplied by 2

2y + 8z = -12 (5)

0 = 2

The final equation 0 = 2 is a contradiction, so we conclude that the system of equations in inconsistent and, therefore, has no solution. Analysis In this system, each plane intersects the other two, but not at the same location. Therefore, the system is inconsistent.

**Try It #2**
Solve the system of three equations in three variables.

x + y + z = 2

y - 3z = 1

2x + y + 5z = 0 Expressing the Solution of a System of Dependent Equations Containing Three Variables We know from working with systems of equations in two variables that a dependent system of equations has an infinite number of solutions. The same is true for dependent systems of equations in three variables. An infinite number of solutions can result from several situations. The three planes could be the same, so that a solution to one equation will be the solution to the other two equations. All three equations could be different but they intersect on a line, which has infinite solutions. Or two of the equations could be the same and intersect the third on a line.

**Example  5**
Finding the Solution to a Dependent System of Equations Find the solution to the given system of three equations in three variables.

2x + y - 3z = 0

(1)

4x + 2y - 6z = 0

(2)

x - y + z = 0

(3) Solution First, we can multiply equation (1) by -2 and add it to equation (2).

-4x - 2y + 6z = 0 equation (1) multiplied by -2

4x + 2y - 6z = 0

(2)

0 = 0 We do not need to proceed any further. The result we get is an identity, 0 = 0, which tells us that this system has an infinite number of solutions. There are other ways to begin to solve this system, such as multiplying equation (3) by -2, and adding it to equation (1). We then perform the same steps as above and find the same result, 0 = 0. When a system is dependent, we can find general expressions for the solutions. Adding equations (1) and (3), we have

2x + y - 3z = 0

x - y + z = 0

3x - 2z = 0 We then solve the resulting equation for z.

3x - 2z = 0

z =  3 __ 2 x We back-substitute the expression for z into one of the equations and solve for y.

2x + y - 3  3 __ 2 x  = 0

2x + y -  9 __ 2 x = 0

y =  9 __ 2 x - 2x

y =  5 __ 2 x So the general solution is  x,  5 __ 2 x,  3 __ 2 x  . In this solution, x can be any real number. The values of y and z are dependent on the value selected for x. Analysis As shown in Figure 5, two of the planes are the same and they intersect the third plane on a line. The solution set is infinite, as all points along the intersection line will satisfy all three equations. x - y + z = 0 -4x - 2y + 6z = 0 4x + 2y - 6z = 0 Does the generic solution to a dependent system always have to be written in terms of x? No, you can write the generic solution in terms of any of the variables, but it is common to write it in terms of x and if needed x and y.

**Try It #3**
Solve the following system.

x + y + z = 7

3x - 2y - z = 4

x + 6y + 5z = 24 Access these online resources for additional instruction and practice with systems of equations in three variables. • Ex 1: System of Three Equations with Three Unknowns Using Elimination (http://openstaxcollege.org/l/systhree) • Ex. 2: System of Three Equations with Three Unknowns Using Elimination (http://openstaxcollege.org/l/systhelim)


## 9.2 Section Exercises

### 9.2 Section Exercises
Verbal 1. Can a linear system of three equations have exactly two solutions? Explain why or why not 2. If a given ordered triple solves the system of equations, is that solution unique? If so, explain why. If not, give an example where it is not unique. 3. If a given ordered triple does not solve the system of equations, is there no solution? If so, explain why. If not, give an example. 4. Using the method of addition, is there only one way to solve the system? 5. Can you explain whether there can be only one method to solve a linear system of equations? If yes, give an example of such a system of equations. If not, explain why not. Algebraic For the following exercises, determine whether the ordered triple given is the solution to the system of equations. 6. 2x - 6y + 6z = -12 x + 4y + 5z = -1 and (0, 1, -1) -x + 2y + 3z = -1 7. 6x - y + 3z = 6 3x + 5y + 2z = 0 and (3, -3, -5) x + y = 0 8. 6x - 7y + z = 2 -x - y + 3z = 4 and (4, 2, -6) 2x + y - z = 1 9. x - y = 0 x - z = 5 and (4, 4, -1) x - y + z = -1 10. -x - y + 2z = 3 5x + 8y - 3z = 4 and (4, 1, -7) -x + 3y - 5z = -5 For the following exercises, solve each system by substitution. 2x + 4y + z = 16 2x + 3y + 5z = 20 2x - 4y - 3z = -9 x + 6y - 8z = 21 13. 5x + 2y + 4z = 9 -3x + 2y + z = 10 4x - 3y + 5z = -3 14. 4x - 3y + 5z = 31 -x + 2y + 4z = 20 x + 5y - 2z = -29 15. 5x - 2y + 3z = 4 -4x + 6y - 7z = -1 3x + 2y - z = 4 16. 4x + 6y + 9z = 0 -5x + 2y - 6z = 3 7x - 4y + 3z = -3 For the following exercises, solve each system by Gaussian elimination. 17. 2x - y + 3z = 17 -5x + 4y - 2z = -46 2y + 5z = -7 - x + 4y = 10 2x - z = 10 19. 2x + 3y - 6z = 1 -4x - 6y + 12z = -2 x + 2y + 5z = 10 20. 4x + 6y - 2z = 8 6x + 9y - 3z = 12 -2x - 3y + z = -4 21. 2x + 3y - 4z = 5 -3x + 2y + z = 11 -x + 5y + 3z = 4 -x - 2y - 4z = -1 -12x - 6y + 6z = -12 23. x + y + z = 14 2y + 3z = -14 24. 5x - 3y + 4z = -1 -4x + 2y - 3z = 0 -x + 5y + 7z = -11 25. x + y + z = 0 2x - y + 3z = 0 x - z = 0

26. 3x + 2y - 5z = 6 5x - 4y + 3z = -12 4x + 5y-2z = 15 27. x + y + z = 0 2x - y + 3z = 0 x - z = 1 __ 2 y - z = - 1 __ 2  4x + z = 3 -x +  3 __ 2 y =  5 __ 2  29. 6x - 5y + 6z = 38  1 __ 5 x -  1 __ 2 y +  3 __ 5 z = 1 -4x -  3 __ 2 y - z = -74 30.  1 __ 2 x -  1 __ 5 y +  2 __ 5 z = - 13 ___ 10   1 __ 4 x -  2 __ 5 y -  1 __ 5 z = - 7 ___ 20  - 1 __ 2 x -  3 __ 4 y -  1 __ 2 z = - 5 __ 4  __ 3 x -  1 __ 2 y -  1 __ 4 z =  3 __ 4  - 1 __ 2 x -  1 __ 4 y -  1 __ 2 z = 2 - 1 __ 4 x -  3 __ 4 y -  1 __ 2 z = - 1 __ 2  __ 2 x -  1 __ 4 y +  3 __ 4 z = 0  1 __ 4 x -  1 ___ 10 y +  2 __ 5 z = -2  1 __ 8 x +  1 __ 5 y -  1 __ 8 z = 2 __ 5 x -  7 __ 8 y +  1 __ 2 z = 1 - 4 __ 5 x -  3 __ 4 y +  1 __ 3 z = -8 - 2 __ 5 x -  7 __ 8 y +  1 __ 2 z = -5 __ 3 x -  1 __ 8 y +  1 __ 6 z = - 4 __ 3  - 2 __ 3 x -  7 __ 8 y +  1 __ 3 z = - 23 ___ 3  - 1 __ 3 x -  5 __ 8 y +  5 __ 6 z = 0 __ 4 x -  5 __ 4 y +  5 __ 2 z = -5 - 1 __ 2 x -  5 __ 3 y +  5 __ 4 z =  55 ___ 12  - 1 __ 3 x -  1 __ 3 y +  1 __ 3 z =  5 __ 3  ___ 40 x +  1 ___ 60 y +  1 ___ 80 z =  1 ___ 100  - 1 __ 2 x -  1 __ 3 y -  1 __ 4 z = - 1 __ 5   3 __ 8 x +  3 ___ 12 y +  3 ___ 16 z =  3 ___ 20  Extensions For the following exercises, solve the system for x, y, and z. 46. x + y + z = 3  x - 1 _____  +  y - 3 _____  +  z + 1 _____  = 0  x - 2 _____  +  y + 4 _____  +  z - 3 _____  =  2 __ 3  47. 5x - 3y -  z + 1 _____  =  1 __ 2  6x +  y - 9 _____  + 2z = -3  x + 8 _____  - 4y + z = 4 _____  -  y - 1 _____  +  z + 2 _____  = 1  x - 2 _____  +  y + 1 _____  -  z + 8 _____ 12  = 0  x + 6 _____  -  y + 2 _____  +  z + 4 _____  = 3 _____  +  y + 2 _____  -  z - 3 _____  = 2  x + 2 _____  +  y - 5 _____  +  z + 4 _____  = 1  x + 6 _____  -  y - 3 _____  + z + 1 = 9 ____ 3  +  y + 3 _____  +  z + 2 _____  = 1 4x + 3y - 2z = 11

Real-World Applications 51. Three even numbers sum up to 108. The smaller is half the larger and the middle number is  3 _ 4  the larger. What are the three numbers? 52. Three numbers sum up to 147. The smallest number is half the middle number, which is half the largest number. What are the three numbers? 53. At a family reunion, there were only blood relatives, consisting of children, parents, and grandparents, in attendance. There were 400 people total. There were twice as many parents as grandparents, and 50 more children than parents. How many children, parents, and grandparents were in attendance? 54. An animal shelter has a total of 350 animals comprised of cats, dogs, and rabbits. If the number of rabbits is 5 less than one-half the number of cats, and there are 20 more cats than dogs, how many of each animal are at the shelter? 55. Your roommate, Sarah, offered to buy groceries for you and your other roommate. The total bill was $82. She forgot to save the individual receipts but remembered that your groceries were $0.05 cheaper than half of her groceries, and that your other roommate’s groceries were $2.10 more than your groceries. How much was each of your share of the groceries? 56. Your roommate, John, offered to buy household supplies for you and your other roommate. You live near the border of three states, each of which has a different sales tax. The total amount of money spent was $100.75. Your supplies were bought with 5% tax, John’s with 8% tax, and your third roommate’s with 9% sales tax. The total amount of money spent without taxes is $93.50. If your supplies before tax were $1 more than half of what your third roommate’s supplies were before tax, how much did each of you spend? Give your answer both with and without taxes. 57. Three coworkers work for the same employer. Their jobs are warehouse manager, office manager, and truck driver. The sum of the annual salaries of the warehouse manager and office manager is $82,000. The office manager makes $4,000 more than the truck driver annually. The annual salaries of the warehouse manager and the truck driver total $78,000. What is the annual salary of each of the co-workers? 58. At a carnival, $2,914.25 in receipts were taken at the end of the day. The cost of a child’s ticket was $20.50, an adult ticket was $29.75, and a senior citizen ticket was $15.25. There were twice as many senior citizens as adults in attendance, and 20 more children than senior citizens. How many children, adult, and senior citizen tickets were sold? 59. A local band sells out for their concert. They sell all 1,175 tickets for a total purse of $28,112.50. The tickets were priced at $20 for student tickets, $22.50 for children, and $29 for adult tickets. If the band sold twice as many adult as children tickets, how many of each type was sold? 60. In a bag, a child has 325 coins worth $19.50. There were three types of coins: pennies, nickels, and dimes. If the bag contained the same number of nickels as dimes, how many of each type of coin was in the bag? 61. Last year, at Haven’s Pond Car Dealership, for a particular model of BMW, Jeep, and Toyota, one could purchase all three cars for a total of $140,000. This year, due to inflation, the same cars would cost $151,830. The cost of the BMW increased by 8%, the Jeep by 5%, and the Toyota by 12%. If the price of last year’s Jeep was $7,000 less than the price of last year’s BMW, what was the price of each of the three cars last year? 62. A recent college graduate took advantage of his business education and invested in three investments immediately after graduating. He invested $80,500 into three accounts, one that paid 4% simple interest, one that paid 4% simple interest, one that paid 3 1 __ 8 % simple interest, and one that paid 2 1 __ 2 % simple interest. He earned $2,670 interest at the end of one year. If the amount of the money invested in the second account was four times the amount invested in the third account, how much was invested in each account?

63. You inherit one million dollars. You invest it all in three accounts for one year. The first account pays 3% compounded annually, the second account pays 4% compounded annually, and the third account pays 2% compounded annually. After one year, you earn $34,000 in interest. If you invest four times the money into the account that pays 3% compared to 2%, how much did you invest in each account? 64. You inherit one hundred thousand dollars. You invest it all in three accounts for one year. The first account pays 4% compounded annually, the second account pays 3% compounded annually, and the third account pays 2% compounded annually. After one year, you earn $3,650 in interest. If you invest five times the money in the account that pays 4% compared to 3%, how much did you invest in each account? 65. The top three countries in oil consumption in a certain year are as follows: the United States, Japan, and China. In millions of barrels per day, the three top countries consumed 39.8% of the world’s consumed oil. The United States consumed 0.7% more than four times China’s consumption. The United States consumed 5% more than triple Japan’s consumption. What percent of the world oil consumption did the United States, Japan, and China consume?[28] 66. The top three countries in oil production in the same year are Saudi Arabia, the United States, and Russia. In millions of barrels per day, the top three countries produced 31.4% of the world’s produced oil. Saudi Arabia and the United States combined for 22.1% of the world’s production, and Saudi Arabia produced 2% more oil than Russia. What percent of the world oil production did Saudi Arabia, the United States, and Russia produce?[29] 67. The top three sources of oil imports for the United States in the same year were Saudi Arabia, Mexico, and Canada. The three top countries accounted for 47% of oil imports. The United States imported 1.8% more from Saudi Arabia than they did from Mexico, and 1.7% more from Saudi Arabia than they did from Canada. What percent of the United States oil imports were from these three countries?[30] 68. The top three oil producers in the United States in a certain year are the Gulf of Mexico, Texas, and Alaska. The three regions were responsible for 64% of the United States oil production. The Gulf of Mexico and Texas combined for 47% of oil production. Texas produced 3% more than Alaska. What percent of United States oil production came from these regions?[31] 69. At one time, in the United States, 398 species of animals were on the endangered species list. The top groups were mammals, birds, and fish, which comprised 55% of the endangered species. Birds accounted for 0.7% more than fish, and fish accounted for 1.5% more than mammals. What percent of the endangered species came from mammals, birds, and fish? 70. Meat consumption in the United States can be broken into three categories: red meat, poultry, and fish. If fish makes up 4% less than one-quarter of poultry consumption, and red meat consumption is 18.2% higher than poultry consumption, what are the percentages of meat consumption?[32] 28 “Oil reserves, production and consumption in 2001,” accessed April 6, 2014, http://scaruffi.com/politics/oil.html. 29 “Oil reserves, production and consumption in 2001,” accessed April 6, 2014, http://scaruffi.com/politics/oil.html. 30 “Oil reserves, production and consumption in 2001,” accessed April 6, 2014, http://scaruffi.com/politics/oil.html. 31 “USA: The coming global oil crisis,” accessed April 6, 2014, http://www.oilcrisis.com/us/. 32 “The United States Meat Industry at a Glance,” accessed April 6, 2014, http://www.meatami.com/ht/d/sp/i/47465/pid/47465.


## 9.3 Systems of Nonlinear Equations and Inequalities: Two Variables
Halley’s Comet (Figure 1) orbits the sun about once every 75 years. Its path can be considered to be a very elongated ellipse. Other comets follow similar paths in space. These orbital paths can be studied using systems of equations. These systems, however, are different from the ones we considered in the previous section because the equations are not linear. In this section, we will consider the intersection of a parabola and a line, a circle and a line, and a circle and an ellipse. The methods for solving systems of nonlinear equations are similar to those for linear equations. Solving a System of Nonlinear Equations Using Substitution A system of nonlinear equations is a system of two or more equations in two or more variables containing at least one equation that is not linear. Recall that a linear equation can take the form Ax + By + C = 0. Any equation that cannot be written in this form in nonlinear. The substitution method we used for linear systems is the same method we will use for nonlinear systems. We solve one equation for one variable and then substitute the result into the second equation to solve for another variable, and so on. There is, however, a variation in the possible outcomes. Intersection of a Parabola and a Line There are three possible types of solutions for a system of nonlinear equations involving a parabola and a line. possible types of solutions for points of intersection of a parabola and a line • No solution. The line will never intersect the parabola. • One solution. The line is tangent to the parabola and intersects the parabola at exactly one point. • Two solutions. The line crosses on the inside of the parabola and intersects the parabola at two points. (a) No solutions One solutions Two solutions (b) (c) x y x y x y Learning Objectives
In this section, you will:
• Solve a system of nonlinear equations using substitution.
• Solve a system of nonlinear equations using elimination.
• Graph a nonlinear inequality.
• Graph a system of nonlinear inequalities.

**How To…**
Given a system of equations containing a line and a parabola, find the solution. 1. Solve the linear equation for one of the variables. 2. Substitute the expression obtained in step one into the parabola equation. 3. Solve for the remaining variable. 4. Check your solutions in both equations.

**Example  1**

### Solving a System of Nonlinear Equations Representing a Parabola and a Line
Solve the system of equations.

x - y = -1

y = x^{2} + 1 Solution Solve the first equation for x and then substitute the resulting expression into the second equation.

x - y = -1

x = y - 1 Solve for x.

y = x^{2} + 1

y = (y - 1)^{2} + 1 Substitute expression for x. Expand the equation and set it equal to zero.

y = (y - 1)^{2}

= (y^{2} - 2y + 1) + 1

= y^{2} - 2y + 2

0 = y^{2} -3y + 2

= (y - 2)(y - 1) Solving for y gives y = 2 and y = 1. Next, substitute each value for y into the first equation to solve for x. Always substitute the value into the linear equation to check for extraneous solutions.

x - y = -1

x - (2) = -1

x = 1

x - (1) = -1

x = 0 The solutions are (1, 2) and (0, 1), which can be verified by substituting these (x, y) values into both of the original equations. See Figure 3. x y x - y = -1 y = x 2 + 1

Could we have substituted values for y into the second equation to solve for x in Example 1? Yes, but because x is squared in the second equation this could give us extraneous solutions for x. For y = 1

y = x^{2} + 1

1 = x^{2} + 1

x^{2} = 0

x = \pm  \sqrt{0}  = 0 This gives us the same value as in the solution. For y = 2

y = x^{2} + 1

2 = x^{2} + 1

x^{2} = 1

x = \pm  \sqrt{1}  = \pm  1 Notice that -1 is an extraneous solution.

**Try It #1**
Solve the given system of equations by substitution.

3x - y = -2

2x^{2} - y = 0 Intersection of a Circle and a Line Just as with a parabola and a line, there are three possible outcomes when solving a system of equations representing a circle and a line. possible types of solutions for the points of intersection of a circle and a line • No solution. The line does not intersect the circle. • One solution. The line is tangent to the circle and intersects the circle at exactly one point. • Two solutions. The line crosses the circle and intersects it at two points. No solutions One solution Two solutions

**How To…**
Given a system of equations containing a line and a circle, find the solution. 1. Solve the linear equation for one of the variables. 2. Substitute the expression obtained in step one into the equation for the circle. 3. Solve for the remaining variable. 4. Check your solutions in both equations.


**Example  2**
Finding the Intersection of a Circle and a Line by Substitution Find the intersection of the given circle and the given line by substitution.

x^{2} + y^{2} = 5

y = 3x - 5 Solution One of the equations has already been solved for y. We will substitute y = 3x - 5 into the equation for the circle.

x^{2} + (3x - 5)^{2} = 5

x^{2} + 9x^{2} -30x + 25 = 5

Now, we factor and solve for x.

10(x^{2} - 3x + 2) = 0

10(x - 2)(x - 1) = 0

x = 2

x = 1 Substitute the two x-values into the original linear equation to solve for y.

y = 3(2)-5

= 1

y = 3(1)-5

= -2 The line intersects the circle at (2, 1) and (1, -2), which can be verified by substituting these (x, y) values into both of the original equations. See Figure 5. x y y = 3x - 5 x^{2} + y^{2} = 5

**Try It #2**
Solve the system of nonlinear equations.

x^{2} + y^{2} = 10

x - 3y = -10 Solving a System of Nonlinear Equations Using Elimination We have seen that substitution is often the preferred method when a system of equations includes a linear equation and a nonlinear equation. However, when both equations in the system have like variables of the second degree, solving them using elimination by addition is often easier than substitution. Generally, elimination is a far simpler method when the system involves only two equations in two variables (a two-by-two system), rather than a three-by-three system, as there are fewer steps. As an example, we will investigate the possible types of solutions when solving a system of equations representing a circle and an ellipse.

possible types of solutions for the points of intersection of a circle and an ellipse • No solution. The circle and ellipse do not intersect. One shape is inside the other or the circle and the ellipse are a distance away from the other. • One solution. The circle and ellipse are tangent to each other, and intersect at exactly one point. • Two solutions. The circle and the ellipse intersect at two points. • Three solutions. The circle and the ellipse intersect at three points. • Four solutions. The circle and the ellipse intersect at four points. No solution One solution Two solutions Tree solutions Four solutions

**Example  3**
Solving a System of Nonlinear Equations Representing a Circle and an Ellipse Solve the system of nonlinear equations.

x^{2} + y^{2} = 26 (1)

(2) Solution Let’s begin by multiplying equation (1) by -3, and adding it to equation (2).

(-3)(x^{2} + y^{2}) = (-3)(26)

-3x^{2} - 3y^{2} = - 78

After we add the two equations together, we solve for y.

y^{2} = 1

y = \pm  \sqrt{1}  = \pm  1 Substitute y = \pm  1 into one of the equations and solve for x.

x^{2} + (1)^{2} = 26

x^{2} + (-1)^{2} = 26

x^{2} + 1 = 26

x^{2} = 25 = \pm  5

x^{2} + 1 = 26

x^{2} = 25

x = \pm  \sqrt{25}  = \pm  5 There are four solutions: (5, 1), (-5, 1), (5, -1), and (-5, -1). See Figure 7. x y


**Try It #3**
Find the solution set for the given system of nonlinear equations.

4x^{2} + y^{2} = 13

x^{2} + y^{2} = 10 Graphing a Nonlinear Inequality All of the equations in the systems that we have encountered so far have involved equalities, but we may also encounter systems that involve inequalities. We have already learned to graph linear inequalities by graphing the corresponding equation, and then shading the region represented by the inequality symbol. Now, we will follow similar steps to graph a nonlinear inequality so that we can learn to solve systems of nonlinear inequalities. A nonlinear inequality is an inequality containing a nonlinear expression. Graphing a nonlinear inequality is much like graphing a linear inequality. Recall that when the inequality is greater than, y > a, or less than, y < a, the graph is drawn with a dashed line. When the inequality is greater than or equal to, y \ge  a, or less than or equal to, y \le  a, the graph is drawn with a solid line. The graphs will create regions in the plane, and we will test each region for a solution. If one point in the region works, the whole region works. That is the region we shade. See Figure 8. x y y > x^{2} - 4 y \ge  x^{2} - 4 y < x^{2} - 4 y \le  x^{2} - 4 x y x y x y (a) (b) (c) (d)

**How To…**
Given an inequality bounded by a parabola, sketch a graph. 1. Graph the parabola as if it were an equation. This is the boundary for the region that is the solution set. 2. If the boundary is included in the region (the operator is \le  or \ge ), the parabola is graphed as a solid line. 3. If the boundary is not included in the region (the operator is < or >), the parabola is graphed as a dashed line. 4. Test a point in one of the regions to determine whether it satisfies the inequality statement. If the statement is true, the solution set is the region including the point. If the statement is false, the solution set is the region on the other side of the boundary line. 5. Shade the region representing the solution set.

**Example  4**

### Graphing an Inequality for a Parabola
Graph the inequality y > x^{2} + 1. Solution First, graph the corresponding equation y = x^{2} + 1. Since y > x^{2} + 1 has a greater than symbol, we draw the graph with a dashed line. Then we choose points to test both inside and outside the parabola. Let’s test the points (0, 2) and (2, 0). One point is clearly inside the parabola and the other point is clearly outside.

y > x^{2} + 1

2 > (0)^{2} + 1

2 > 1 True

0 > (2)^{2} + 1

0 > 5 False

The graph is shown in Figure 9. We can see that the solution set consists of all points inside the parabola, but not on the graph itself. x y Graphing a System of Nonlinear Inequalities Now that we have learned to graph nonlinear inequalities, we can learn how to graph systems of nonlinear inequalities. A system of nonlinear inequalities is a system of two or more inequalities in two or more variables containing at least one inequality that is not linear. Graphing a system of nonlinear inequalities is similar to graphing a system of linear inequalities. The difference is that our graph may result in more shaded regions that represent a solution than we find in a system of linear inequalities. The solution to a nonlinear system of inequalities is the region of the graph where the shaded regions of the graph of each inequality overlap, or where the regions intersect, called the feasible region.

**How To…**
Given a system of nonlinear inequalities, sketch a graph. 1. Find the intersection points by solving the corresponding system of nonlinear equations. 2. Graph the nonlinear equations. 3. Find the shaded regions of each inequality. 4. Identify the feasible region as the intersection of the shaded regions of each inequality or the set of points common to each inequality.

**Example  5**

### Graphing a System of Inequalities
Graph the given system of inequalities.

x^{2} - y \le  0

2x^{2} + y \le  12 Solution These two equations are clearly parabolas. We can find the points of intersection by the elimination process: Add both equations and the variable y will be eliminated. Then we solve for x.

x^{2} - y = 0

2x^{2} + y = 12

x^{2} = 4

x = \pm  2 Substitute the x-values into one of the equations and solve for y.

x^{2} - y = 0

(2)^{2} - y = 0

4 - y = 0

y = 4

(-2)^{2} - y = 0

4 - y = 0

y = 4

The two points of intersection are (2, 4) and (-2, 4). Notice that the equations can be rewritten as follows.

x^{2} - y \le  0

x^{2} \le  y

y \ge  x^{2}

2x^{2} + y \le  12

y \le  - 2x^{2} + 12 Graph each inequality. See Figure 10. The feasible region is the region between the two equations bounded by 2 x^{2} + y \le  12 on the top and x^{2} - y \le  0 on the bottom. x y

**Try It #4**
Graph the given system of inequalities.

y \ge  x^{2} - 1

x - y \ge  - 1 Access these online resources for additional instruction and practice with nonlinear equations. • Solve a System of Nonlinear Equations Using Substitution (http://openstaxcollege.org/l/nonlinsub) • Solve a System of Nonlinear Equations Using Elimination (http://openstaxcollege.org/l/nonlinelim)


## 9.3 Section Exercises

### 9.3 Section Exercises
Verbal 1. Explain whether a system of two nonlinear equations can have exactly two solutions. What about exactly three? If not, explain why not. If so, give an example of such a system, in graph form, and explain why your choice gives two or three answers. 2. When graphing an inequality, explain why we only need to test one point to determine whether an entire region is the solution? 3. When you graph a system of inequalities, will there always be a feasible region? If so, explain why. If not, give an example of a graph of inequalities that does not have a feasible region. Why does it not have a feasible region? 4. If you graph a revenue and cost function, explain how to determine in what regions there is profit. 5. If you perform your break-even analysis and there is more than one solution, explain how you would determine which x-values are profit and which are not. Algebraic For the following exercises, solve the system of nonlinear equations using substitution. 6. x + y = 4 x^{2} + y^{2} = 9 7. y = x - 3 x^{2} + y^{2} = 9 8. y = x x^{2} + y^{2} = 9 9. y = - x x^{2} + y^{2} = 9 10. x = 2 x^{2} - y^{2} = 9 For the following exercises, solve the system of nonlinear equations using elimination. 4x^{2} + 9y^{2} = 36 12. x^{2} + y^{2} = 25 x^{2} - y^{2} = 1 13. 2x^{2} + 4y^{2} = 4 2x^{2} -4y^{2} = 25x - 10 14. y^{2} - x^{2} = 9 3x^{2} + 2y^{2} = 8 15. x^{2} + y^{2} +  1 _ y = 2x^{2} For the following exercises, use any method to solve the system of nonlinear equations. 16. -2x^{2} + y = -5 6x - y = 9 17. -x^{2} + y = 2 -x + y = 2 18. x^{2} + y^{2} = 1 y = 20x^{2} -1 19. x^{2} + y^{2} = 1 y = -x^{2} 20. 2x^{3} - x^{2} = y y =  1 _ 2  - x (x - 6)^{2} + y^{2} = 1 22. x^{4} - x^{2} = y x^{2} + y = 0 23. 2x^{3} - x^{2} = y x^{2} + y = 0 For the following exercises, use any method to solve the nonlinear system. 24. x^{2} + y^{2} = 9 y = 3 - x^{2} 25. x^{2} - y^{2} = 9 x = 3 26. x^{2} - y^{2} = 9 y = 3 27. x^{2} - y^{2} = 9 x - y = 0 28. -x^{2} + y = 2 -4x + y = -1 29. -x^{2} + y = 2 2y = - x 30. x^{2} + y^{2} = 25 x^{2} - y^{2} = 36 31. x^{2} + y^{2} = 1 y^{2} = x^{2} y^{2} + x^{2} = 16

33. 3x^{2} - y^{2} = 12 (x - 1)^{2} + y^{2} = 1 34. 3x^{2} - y^{2} = 12 (x - 1)^{2} + y^{2} = 4 35. 3x^{2} - y^{2} = 12 x^{2} + y^{2} = 16 36. x^{2} - y^{2} - 6x - 4y - 11 = 0 -x^{2} + y^{2} = 5 37. x^{2} + y^{2} - 6y = 7 x^{2} + y = 1 38. x^{2} + y^{2} = 6 xy = 1 Graphical For the following exercises, graph the inequality. 39. x^{2} + y < 9 40. x^{2} + y^{2} < 4 For the following exercises, graph the system of inequalities. Label all points of intersection. 41. x^{2} + y < 1 y > 2x 42. x^{2} + y < -5 y > 5x + 10 43. x^{2} + y^{2} < 25 3x^{2} - y^{2} > 12 44. x^{2} - y^{2} > -4 x^{2} + y^{2} < 12 45. x^{2} + 3y^{2} > 16 3x^{2} - y^{2} < 1 Extensions For the following exercises, graph the inequality. 46. y \ge  ex y \le  ln(x) + 5 47. y \le  -log(x) y \le  ex For the following exercises, find the solutions to the nonlinear equations with two variables. 48.  4 __ x^{2}  +  1 __ y^{2}  = 24  5 __ x^{2}  -  2 __ y^{2}  + 4 = 0 __ x^{2}  -  1 __ y^{2}  = 8  1 __ x^{2}  -  6 __ y^{2}  =  1 __ 8  50. x^{2} - xy + y^{2} -2 = 0 x + 3y = 4 51. x^{2} - xy - 2y^{2} -6 = 0 x^{2} + y^{2} = 1 52. x^{2} + 4xy - 2y^{2} - 6 = 0 x = y + 2 Technology For the following exercises, solve the system of inequalities. Use a calculator to graph the system to confirm the answer. y > \sqrt{x}  54. x^{2} + y < 3 y > 2x Real-World Applications For the following exercises, construct a system of nonlinear equations to describe the given behavior, then solve for the requested solutions. 55. Two numbers add up to 300. One number is twice the square of the other number. What are the numbers? 56. The squares of two numbers add to 360. The second number is half the value of the first number squared. What are the numbers? 57. A laptop company has discovered their cost and revenue functions for each day: C(x) = 3x^{2} - 10x + 200 and R(x) = -2x^{2} + 100x + 50. If they want to make a profit, what is the range of laptops per day that they should produce? Round to the nearest number which would generate profit. 58. A cell phone company has the following cost and revenue functions: C(x) = 8x^{2} - 600x + 21,500 and R(x) = -3x^{2} + 480x. What is the range of cell phones they should produce each day so there is profit? round to the nearest number that generates profit.


## 9.4 Partial Fractions
Earlier in this chapter, we studied systems of two equations in two variables, systems of three equations in three variables, and nonlinear systems. Here we introduce another way that systems of equations can be utilized—the decomposition of rational expressions. Fractions can be complicated; adding a variable in the denominator makes them even more so. The methods studied in this section will help simplify the concept of a rational expression. Decomposing  P(x ) ____ Q(x )  Where Q(x ) Has Only Nonrepeated Linear Factors Recall the algebra regarding adding and subtracting rational expressions. These operations depend on finding a common denominator so that we can write the sum or difference as a single, simplified rational expression. In this section, we will look at partial fraction decomposition, which is the undoing of the procedure to add or subtract rational expressions. In other words, it is a return from the single simplified rational expression to the original expressions, called the partial fractions. For example, suppose we add the following fractions:  _____ x - 3  +  -1 _____ x + 2  We would first need to find a common denominator, (x + 2)(x - 3). Next, we would write each expression with this common denominator and find the sum of the terms.

 _____ x - 3   x + 2 _____ x + 2   +  -1 _____ x + 2   x - 3 _____ x - 3    =  2x + 4 - x + 3

____________

(x + 2)(x - 3)  =  x + 7 ________ x^{2} - x - 6  Partial fraction decomposition is the reverse of this procedure. We would start with the solution and rewrite (decompose) it as the sum of two fractions.   x + 7 _______ x^{2} - x - 6 

Simplified sum  =   ____ x - 3  +  -1 _____ x + 2 

Partial fraction decomposition  We will investigate rational expressions with linear factors and quadratic factors in the denominator where the degree of the numerator is less than the degree of the denominator. Regardless of the type of expression we are decomposing, the first and most important thing to do is factor the denominator. When the denominator of the simplified expression contains distinct linear factors, it is likely that each of the original rational expressions, which were added or subtracted, had one of the linear factors as the denominator. In other words, using the example above, the factors of x^{2} - x - 6 are (x - 3)(x + 2), the denominators of the decomposed rational expression. So we will rewrite the simplified form as the sum of individual fractions and use a variable for each numerator. Then, we will solve for each numerator using one of several methods available for partial fraction decomposition. Learning Objectives
In this section, you will:
• Decompose P (x )Q (x ), where Q (x ) has only nonrepeated linear factors.
• Decompose P (x )Q (x ), where Q (x ) has repeated linear factors.
• Decompose P (x )Q (x ), where Q (x ) has a nonrepeated irreducible quadratic factor.
• Decompose P (x )Q (x ), where Q (x ) has a repeated irreducible quadratic factor.
partial fraction decomposition of  P(x) ____ Q(x)  : Q(x) has nonrepeated linear factors The partial fraction decomposition of  P(x) ____ Q(x)  when Q(x) has nonrepeated linear factors and the degree of P(x) is less than the degree of Q(x) is  P(x) ____ Q(x)  =  A^{1} __  a^{1}x + b^{1}   +  A^{2} __  a^{2} x + b^{2}   +  A^{3} __  a^{3}x + b^{3}   + ... +  An __  anx + bn   .

**How To…**
Given a rational expression with distinct linear factors in the denominator, decompose it. 1. Use a variable for the original numerators, usually A, B, or C, depending on the number of factors, placing each variable over a single factor. For the purpose of this definition, we use An for each numerator  P(x) ____ Q(x)  =  A^{1} __  a^{1}x + b^{1}   +  A^{2} __  a^{2} x + b^{2}   + ... +  An __  anx + bn   . 2. Multiply both sides of the equation by the common denominator to eliminate fractions. 3. Expand the right side of the equation and collect like terms. 4. Set coefficients of like terms from the left side of the equation equal to those on the right side to create a system of equations to solve for the numerators.

**Example  1**

### Decomposing a Rational Function with Distinct Linear Factors
Decompose the given rational expression with distinct linear factors.

 3x ___________

(x + 2)(x - 1)  Solution We will separate the denominator factors and give each numerator a symbolic label, like A, B, or C.

 3x ___________

(x + 2)(x - 1)  =  A ______ (x + 2)  +  B _____ (x - 1)  Multiply both sides of the equation by the common denominator to eliminate the fractions:

(x + 2)(x - 1)  3x __________

(x + 2)(x - 1)    =  (x + 2)(x - 1)  A ______  (x + 2)    + (x + 2) (x - 1)  B _____  (x - 1)    The resulting equation is

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

 3x __________

(x + 2)(x - 1)  =  ______ (x + 2)  +  _____ (x - 1) 

Another method to use to solve for A or B is by considering the equation that resulted from eliminating the fractions and substituting a value for x that will make either the A- or B-term equal 0. If we let x = 1, the A-term becomes 0 and we can simply solve for B.

3x = A(x - 1) + B(x + 2)

3(1) = A[(1) - 1] + B[(1) + 2]

3 = 0 + 3B

1 = B Next, either substitute B = 1 into the equation and solve for A, or make the B-term 0 by substituting x = -2 into the equation.

3x = A(x - 1) + B(x + 2)

3(-2) = A[(-2) - 1] + B[(-2) + 2]

-6 = -3A + 0

 -6 ___ -3  = A

2 = A We obtain the same values for A and B using either method, so the decompositions are the same using either method.

 3x ___________

(x + 2)(x - 1)  =  ______ (x + 2)  +  _____ (x - 1)  Although this method is not seen very often in textbooks, we present it here as an alternative that may make some partial fraction decompositions easier. It is known as the Heaviside method, named after Charles Heaviside, a pioneer in the study of electronics.

**Try It #1**
Find the partial fraction decomposition of the following expression.  x ____________

(x - 3)(x - 2)  Decomposing  P(x ) ____ Q(x )  Where Q(x ) Has Repeated Linear Factors Some fractions we may come across are special cases that we can decompose into partial fractions with repeated linear factors. We must remember that we account for repeated factors by writing each factor in increasing powers. partial fraction decomposition of  P(x) ____ Q(x)  : Q(x) has repeated linear factors The partial fraction decomposition of  P(x) ____ Q(x)  when Q(x) has repeated linear factor occurring n times and the degree of P(x) is less than the degree of Q(x), is  P(x) ____ Q(x)  =  A^{1} _______ (ax + b)  +  A^{2} ________ (ax + b)^{2}  +  A^{3} ________ (ax + b)^{3}  + ... +  An ________ (ax + b)n  Write the denominator powers in increasing order.

**How To…**
Given a rational expression with repeated linear factors, decompose it. 1. Use a variable like A, B, or C for the numerators and account for increasing powers of the denominators.  P(x) ____ Q(x)  =  A^{1} _______ (ax + b)  +  A^{2} ________ (ax + b)^{2}  + ... +  An ________ (ax + b)n  2. Multiply both sides of the equation by the common denominator to eliminate fractions. 3. Expand the right side of the equation and collect like terms. 4. Set coefficients of like terms from the left side of the equation equal to those on the right side to create a system of equations to solve for the numerators.


**Example  2**

### Decomposing with Repeated Linear Factors
Decompose the given rational expression with repeated linear factors.

 -x^{2} + 2x + 4

___________

x^{3} - 4x^{2} + 4x  Solution The denominator factors are x(x - 2)^{2}. To allow for the repeated factor of (x - 2), the decomposition will include three denominators: x, (x - 2), and (x - 2)^{2}. Thus,

 -x^{2} + 2x + 4

__________

x^{3} - 4x^{2} + 4x  =  A __ x  +  B ______ (x - 2)  +  C _______ (x - 2)^{2}  Next, we multiply both sides by the common denominator.

x(x - 2)^{2}  -x^{2} + 2x + 4

__________ x(x - 2)^{2}

   =   A __ x  +  B ______ (x - 2)  +  C _______ (x - 2)^{2}   x(x - 2)^{2}

-x^{2} + 2x + 4 = A(x - 2)^{2} + Bx(x-2) + Cx On the right side of the equation, we expand and collect like terms.

-x^{2} + 2x + 4 = A(x^{2} - 4x + 4) + B(x^{2} - 2x) + Cx

= Ax^{2} - 4Ax + 4A + Bx^{2} - 2Bx + Cx

= (A + B)x^{2} + ( -4A - 2B + C)x + 4A Next, we compare the coefficients of both sides. This will give the system of equations in three variables:

-x^{2} + 2x + 4 = (A + B)x^{2} + (-4A - 2B + C)x + 4A

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

 -x^{2} + 2x + 4

__________

x^{3} - 4x^{2} + 4x  =  1 __ x  -  ______ (x - 2)  +  _______ (x - 2)^{2} 

**Try It #2**
Find the partial fraction decomposition of the expression with repeated linear factors.

 6x - 11 _______ (x - 1)^{2} 


### Decomposing  P(x )
____ Q(x )  Where Q(x ) Has a Nonrepeated Irreducible Quadratic Factor So far, we have performed partial fraction decomposition with expressions that have had linear factors in the denominator, and we applied numerators A, B, or C representing constants. Now we will look at an example where one of the factors in the denominator is a quadratic expression that does not factor. This is referred to as an irreducible quadratic factor. In cases like this, we use a linear numerator such as Ax + B, Bx + C, etc. decomposition of  P(x) _____ Q(x):  Q(x) has a nonrepeated irreducible quadratic factor The partial fraction decomposition of  P(x) ____ Q(x)  such that Q(x) has a nonrepeated irreducible quadratic factor and the degree of P(x) is less than the degree of Q(x), is written as  P(x) ____ Q(x)  =  A^{1} x + B^{1} ______________

(a^{1}

x 2 + b^{1} x + c^{1})  +  A^{2} x + B^{2} ______________

(a^{2} x^{2} + b^{2} x + c^{2})  + ... +  An x + Bn ______________

(an x^{2} + bn x + cn)  The decomposition may contain more rational expressions if there are linear factors. Each linear factor will have a different constant numerator: A, B, C, and so on.

**How To…**
Given a rational expression where the factors of the denominator are distinct, irreducible quadratic factors, decompose it. 1. Use variables such as A, B, or C for the constant numerators over linear factors, and linear expressions such as A^{1} x + B^{1}, A^{2}x + B^{2}, etc., for the numerators of each quadratic factor in the denominator.  P(x) ____ Q(x)  =  A ______ ax + b  +  A^{1} x + B^{1} _____________

(a^{1} x^{2} + b^{1} x + c^{1})  +  A^{2} x + B^{2} _____________

(a^{2} x^{2} + b^{2} x + c^{2})  + ... +  An x + Bn _____________

(an x 2 + bn x + cn)  2. Multiply both sides of the equation by the common denominator to eliminate fractions. 3. Expand the right side of the equation and collect like terms. 4. Set coefficients of like terms from the left side of the equation equal to those on the right side to create a system of equations to solve for the numerators.

**Example  3**

### Decomposing  P(x)
____ Q(x)  When Q(x) Contains a Nonrepeated Irreducible Quadratic Factor Find a partial fraction decomposition of the given expression.

 8x^{2} + 12x - 20

________________

(x + 3)(x^{2} + x + 2)  Solution We have one linear factor and one irreducible quadratic factor in the denominator, so one numerator will be a constant and the other numerator will be a linear expression. Thus,



________________

(x + 3)(x^{2} + x + 2)  =  A ______ (x + 3)  +  Bx + C __________ (x^{2} + x + 2)  We follow the same steps as in previous problems. First, clear the fractions by multiplying both sides of the equation by the common denominator.

(x + 3)(x^{2} + x + 2)  8x^{2} + 12x - 20

________________

(x + 3)(x^{2} + x + 2)    =   A ______ (x + 3)  +  Bx + C __________ (x^{2} + x + 2)   (x + 3)(x^{2} + x + 2)

8x^{2} + 12x - 20 = A(x^{2} + x + 2) + (Bx + C)(x + 3)

Notice we could easily solve for A by choosing a value for x that will make the Bx + C term equal 0. Let x = -3 and substitute it into the equation.

8x^{2} + 12x - 20 = A(x^{2} + x + 2) + (Bx + C)(x + 3)

8(-3)^{2} + 12(-3) - 20 = A((-3)^{2} + (-3) + 2) + (B(-3) + C)((-3) + 3)

A = 2 Now that we know the value of A, substitute it back into the equation. Then expand the right side and collect like terms.

8x^{2} + 12x - 20 = 2(x^{2} + x + 2) + (Bx + C)(x + 3)

8x^{2} + 12x - 20 = 2x^{2} + 2x + 4 + Bx^{2} + 3B + Cx + 3C

8x^{2} + 12x - 20 = (2 + B)x^{2} + (2 + 3B + C)x + (4 + 3C) Setting the coefficients of terms on the right side equal to the coefficients of terms on the left side gives the system of equations.

2 + B = 8 (1)

2 + 3B + C = 12 (2)

4 + 3C = -20 (3) Solve for B using equation (1) and solve for C using equation (3).

2 + B = 8 (1)

B = 6

4 + 3C = -20 (3)

C = -8 Thus, the partial fraction decomposition of the expression is

 8x^{2} + 12x - 20

_______________

(x + 3)(x^{2} + x + 2)  =  ______ (x + 3)  +  6x - 8 __________ (x^{2} + x + 2)  Could we have just set up a system of equations to solve Example 3? Yes, we could have solved it by setting up a system of equations without solving for A first. The expansion on the right would be:

8x^{2} + 12x - 20 = Ax^{2} + Ax + 2A + Bx^{2} + 3B + Cx + 3C

8x^{2} + 12x - 20 = (A + B)x^{2} + (A + 3B + C)x + (2A + 3C) So the system of equations would be:

A + B = 8

A + 3B + C = 12

2A + 3C = -20

**Try It #3**
Find the partial fraction decomposition of the expression with a nonrepeating irreducible quadratic factor.  5x^{2} - 6x + 7

____________

(x - 1)(x^{2} + 1) 


### Decomposing  P(x )
____ Q(x )  Where Q(x ) Has a Repeated Irreducible Quadratic Factor Now that we can decompose a simplified rational expression with an irreducible quadratic factor, we will learn how to do partial fraction decomposition when the simplified rational expression has repeated irreducible quadratic factors. The decomposition will consist of partial fractions with linear numerators over each irreducible quadratic factor represented in increasing powers. decomposition of  P(x) ____ Q(x)  : when Q(x) has a repeated irreducible quadratic factor The partial fraction decomposition of  P(x) ____ Q(x) , when Q(x) has a repeated irreducible quadratic factor and the degree of P(x) is less than the degree of Q(x), is  P(x) _____________

(ax 2 + bx + c) n  =  A^{1} x + B^{1} ____________

(ax 2 + bx + c)  +  A^{2} x + B^{2} _____________

(ax 2 + bx + c)^{2}  +  A^{3} x + B^{3} _____________

(ax 2 + bx + c)^{3}  + ... +  An x + Bn _____________

(ax 2 + bx + c) n  Write the denominators in increasing powers.

**How To…**
Given a rational expression that has a repeated irreducible factor, decompose it. 1. Use variables like A, B, or C for the constant numerators over linear factors, and linear expressions such as A^{1}x + B^{1}, A^{2}x + B^{2}, etc., for the numerators of each quadratic factor in the denominator written in increasing powers, such as  P(x) ____ Q(x)  =  A ______ ax + b  +  A^{1} x + B^{1} ____________

(ax^{2} + bx + c)  +  A^{2} x + B^{2} ____________

(ax^{2} + bx + c)^{2}  + ... +  An x + Bn ____________

(ax 2 + bx + c) n  2. Multiply both sides of the equation by the common denominator to eliminate fractions. 3. Expand the right side of the equation and collect like terms. 4. Set coefficients of like terms from the left side of the equation equal to those on the right side to create a system of equations to solve for the numerators.

**Example  4**
Decomposing a Rational Function with a Repeated Irreducible Quadratic Factor in the Denominator Decompose the given expression that has a repeated irreducible factor in the denominator.  x^{4} + x^{3} + x^{2} - x + 1

________________

x(x^{2} + 1)^{2}

 Solution The factors of the denominator are x, (x^{2} + 1), and (x^{2} + 1)^{2}. Recall that, when a factor in the denominator is a quadratic that includes at least two terms, the numerator must be of the linear form Ax + B. So, let’s begin the decomposition.

 x^{4} + x^{3} + x^{2} - x + 1

________________

x(x^{2} + 1)^{2}

 =  A __ x  +  Bx + C _______ (x^{2} + 1)  +  Dx + E _______ (x^{2} + 1)^{2}  We eliminate the denominators by multiplying each term by x(x^{2} + 1)^{2}. Thus,

x^{4} + x^{3} + x^{2} - x + 1 = A(x^{2} + 1)^{2} + (Bx + C)(x)(x^{2} + 1) + (Dx + E)(x) Expand the right side. x^{4} + x^{3} + x^{2} - x + 1 = A(x^{4} + 2x^{2} + 1) + Bx^{4} + Bx^{2} + Cx^{3} + Cx + Dx^{2} + Ex

= Ax^{4} + 2Ax^{2} + A + Bx^{4} + Bx^{2} + Cx^{3} + Cx + Dx^{2} + Ex Now we will collect like terms. x^{4} + x^{3} + x^{2} - x + 1 = (A + B)x^{4} + (C)x^{3} + (2A + B + D)x^{2} + (C + E)x + A

Set up the system of equations matching corresponding coefficients on each side of the equal sign.

A + B = 1

C = 1

2A + B + D = 1

C + E = -1

A = 1 We can use substitution from this point. Substitute A = 1 into the first equation.

1 + B = 1

B = 0 Substitute A = 1 and B = 0 into the third equation.

2(1) + 0 + D = 1

D = -1 Substitute C = 1 into the fourth equation.

1 + E = -1

E = -2 Now we have solved for all of the unknowns on the right side of the equal sign. We have A = 1, B = 0, C = 1, D = -1, and E = -2. We can write the decomposition as follows:  x^{4} + x^{3} + x^{2} - x + 1

________________

x(x^{2} + 1)^{2}

 =  1 __ x  +  _______ (x^{2} + 1)  -  x + 2 _______ (x^{2} + 1)^{2} 

**Try It #4**
Find the partial fraction decomposition of the expression with a repeated irreducible quadratic factor.

 x^{3} - 4x^{2} + 9x-5

______________

(x^{2} -2x + 3)^{2}  Access these online resources for additional instruction and practice with partial fractions. • Partial Fraction Decomposition (http://openstaxcollege.org/l/partdecomp) • Partial Fraction Decomposition With Repeated Linear Factors (http://openstaxcollege.org/l/partdecomprlf) • Partial Fraction Decomposition With Linear and Quadratic Factors (http://openstaxcollege.org/l/partdecomlqu)


## 9.4 Section Exercises

### 9.4 Section Exercises
Verbal 1. Can any quotient of polynomials be decomposed into at least two partial fractions? If so, explain why, and if not, give an example of such a fraction 2. Can you explain why a partial fraction decomposition is unique? (Hint: Think about it as a system of equations.) 3. Can you explain how to verify a partial fraction decomposition graphically? 4. You are unsure if you correctly decomposed the partial fraction correctly. Explain how you could double check your answer. 5. Once you have a system of equations generated by the partial fraction decomposition, can you explain another method to solve it? For example if you had  ___________

3x^{2} + 8x + 15  =  A _____ x + 1  +  B ______ 3x + 5 , we eventually simplify to 7x + 13 = A(3x + 5) + B(x + 1). Explain how you could intelligently choose an x-value that will eliminate either A or B and solve for A and B. Algebraic For the following exercises, find the decomposition of the partial fraction for the nonrepeating linear factors. 6.  ___________

x^{2} + 10x + 24  7.  __________ x^{2} - 5x - 24  8.  -x - 24 __________ x^{2} - 2x - 24  __________ x^{2} + 7x + 10  10.  x ____________

 11.  ____________

 12.  x + 1 __________ x^{2} + 7x + 10  _ x^{2} - 9  ______ x^{2} - 25  _____ x^{2} - 4  16.  2x - 3 _________ x^{2} - 6x + 5  _ x^{2} - x - 6  18.  4x + 3 __________ x^{2} + 8x + 15  19.  3x - 1 _________ x^{2} -5x + 6  For the following exercises, find the decomposition of the partial fraction for the repeating linear factors. ________ (x + 4)^{2}  21.  x _______ (x - 2)^{2}  _______ (x + 3)^{2}  _________ (4x + 5)^{2}  _________ (6x - 7)^{2}  25.  5 - x _______ (x - 7)^{2}  26.  ____________



___________ 2x(x + 1)^{2} 

____________

5x(3x + 5)^{2} 

____________________

2x^{2} (3x + 2)^{2}

 30.  x^{3} - 5x^{2} + 12x + 144

_________________

x^{2}(x^{2} + 12x + 36) 

For the following exercises, find the decomposition of the partial fraction for the irreducible non repeating quadratic factor. 31.  4x^{2} + 6x + 11

_______________

(x + 2)(x^{2} + x + 3)  32.  4x^{2} + 9x + 23

_________________

(x - 1)(x^{2} + 6x + 11)  33.  -2x^{2} + 10x + 4

________________

(x - 1)(x^{2} + 3x + 8)  34.  x^{2} + 3x + 1

________________

(x + 1)(x^{2} + 5x - 2)  35.  4x^{2} + 17x - 1

________________

(x + 3)(x^{2} + 6x + 1)  36.  4x^{2} ________________

(x + 5)(x^{2} + 7x - 5)  37.  4x^{2} + 5x + 3 __________ x^{3} - 1

 38.  -5x^{2} + 18x - 4

____________ x^{3} + 8



___________ x^{3} + 27

 40.  x^{2} + 2x + 40 __________



___________

 42.  -50x^{2} + 5x - 3

____________



____________________

x^{4} + 216x

 For the following exercises, find the decomposition of the partial fraction for the irreducible repeating quadratic factor. 44.  3x^{3} + 2x^{2} + 14x + 15

_________________

(x^{2} + 4)^{2}

 45.  x^{3} + 6x^{2} + 5x + 9

______________

(x^{2} + 1)^{2}

 46.  x^{3} - x^{2} + x - 1

___________ (x^{2} - 3)^{2}

 47.  x^{2} + 5x + 5 _________ (x + 2)^{2}  48.  x^{3} + 2x^{2} + 4x

___________

(x^{2} + 2x + 9)^{2}  49.  x^{2} + 25 ____________

(x^{2} + 3x + 25)^{2} 

________________

(2x^{2} + x + 14)^{2}

 ________ x(x^{2} + 4)^{2}  52.  x^{4} + x^{3} + 8x^{2} + 6x + 36

___________________

x(x^{2} + 6)^{2}

 _______ (x^{2} - x)^{2}  54.  5x^{3} - 2x + 1 __________ (x^{2} + 2x)^{2}  Extensions For the following exercises, find the partial fraction expansion. 55.  x^{2} + 4 _______ (x + 1)^{3}  56.  x^{3} - 4x^{2} + 5x + 4

______________ (x - 2)^{3}

 For the following exercises, perform the operation and then find the partial fraction decomposition. 57.  _____ x + 8  +  _____ x - 2  -  x - 1 __________ x^{2} -6x - 16  58.  _____ x - 4  -  _____ x + 6  -  2x + 7 __________ x^{2} + 2x - 24  59.  2x ______ x^{2} - 16  -  1-2x _________ x^{2} + 6x + 8  -  x - 5 ______ x^{2} - 4x 


## 9.5 Matrices and Matrix Operations
Two club soccer teams, the Wildcats and the Mud Cats, are hoping to obtain new equipment for an upcoming season. Wildcats Mud Cats Goals Balls Jerseys A goal costs $300; a ball costs $10; and a jersey costs $30. How can we find the total cost for the equipment needed for each team? In this section, we discover a method in which the data in the soccer equipment table can be displayed and used for calculating other information. Then, we will be able to calculate the cost of the equipment. Finding the Sum and Difference of Two Matrices To solve a problem like the one described for the soccer teams, we can use a matrix, which is a rectangular array of numbers. A row in a matrix is a set of numbers that are aligned horizontally. A column in a matrix is a set of numbers that are aligned vertically. Each number is an entry, sometimes called an element, of the matrix. Matrices (plural) are enclosed in [ ] or ( ), and are usually named with capital letters. For example, three matrices named A, B, and C are shown below. A =  1 2

  , B =  

  , C =   -1 3

   Learning Objectives
In this section, you will:
• Find the sum and difference of two matrices.
• Find scalar multiples of a matrix.
• Find the product of two matrices.

### Describing Matrices
A matrix is often referred to by its size or dimensions: m \times  n indicating m rows and n columns. Matrix entries are defined first by row and then by column. For example, to locate the entry in matrix A identified as aij, we look for the entry in row i, column j. In matrix A, shown below, the entry in row 2, column 3 is a^{2}3. A =   a^{1}1 a^{1}2 a^{1}3

a^{2}1 a^{2}2 a^{2}3

a^{3}1 a^{3}2 a^{3}3    A square matrix is a matrix with dimensions n \times  n, meaning that it has the same number of rows as columns. The 3 \times  3 matrix above is an example of a square matrix. A row matrix is a matrix consisting of one row with dimensions 1 \times  n. [a^{1}1 a^{1}2 a^{1}3] A column matrix is a matrix consisting of one column with dimensions m \times  1.   a^{1}1

a^{1}2 a^{1}3    A matrix may be used to represent a system of equations. In these cases, the numbers represent the coefficients of the variables in the system. Matrices often make solving systems of equations easier because they are not encumbered with variables. We will investigate this idea further in the next section, but first we will look at basic matrix operations. matrices A matrix is a rectangular array of numbers that is usually named by a capital letter: A, B, C, and so on. Each entry in a matrix is referred to as aij, such that i represents the row and j represents the column. Matrices are often referred to by their dimensions: m \times  n indicating m rows and n columns.

**Example  1**
Finding the Dimensions of the Given Matrix and Locating Entries Given matrix A: a. What are the dimensions of matrix A? b. What are the entries at a^{3}1 and a^{2}2 ?

A =  

  

**Solution**
a. The dimensions are 3 \times  3 because there are three rows and three columns. b. Entry a^{3}1 is the number at row 3, column 1, which is 3. The entry a^{2}2 is the number at row 2, column 2, which is 4. Remember, the row comes first, then the column. Adding and Subtracting Matrices We use matrices to list data or to represent systems. Because the entries are numbers, we can perform operations on matrices. We add or subtract matrices by adding or subtracting corresponding entries. In order to do this, the entries must correspond. Therefore, addition and subtraction of matrices is only possible when the matrices have the same dimensions. We can add or subtract a 3 \times  3 matrix and another 3 \times  3 matrix, but we cannot add or subtract a 2 \times  3 matrix and a 3 \times  3 matrix because some entries in one matrix will not have a corresponding entry in the other matrix.

adding and subtracting matrices Given matrices A and B of like dimensions, addition and subtraction of A and B will produce matrix C or matrix D of the same dimension. A + B = C such that aij + bij = cij A - B = D such that aij - bij = dij Matrix addition is commutative.

A + B = B + A It is also associative.

(A + B) + C = A + (B + C)

**Example  2**
Finding the Sum of Matrices Find the sum of A and B, given

A =  a b

c d    and B =  e f

g h    Solution Add corresponding entries.

A + B =  a b

c d    +  e f

g h   

=  a + e b + f

c + g d + h   

**Example  3**

### Adding Matrix A and Matrix B
Find the sum of A and B.

A =  4 1

   and B =  5 9

   Solution Add corresponding entries. Add the entry in row 1, column 1, a^{1}1, of matrix A to the entry in row 1, column 1, b^{1}1, of B. Continue the pattern until all entries have been added.

A + B =  4 1

   +  5 9

  

=  4 + 5 1 + 9

3 + 0 2 + 7   

=  9 10

  

**Example  4**

### Finding the Difference of Two Matrices
Find the difference of A and B.

A =  -2 3

   and B =  8 1

   Solution We subtract the corresponding entries of each matrix.

A - B =  -2 3

   -  8 1

  

=  -2 - 8 3 - 1

0 - 5 1 - 4   

=  -10 2

-5 -3  


**Example  5**
Finding the Sum and Difference of Two 3 x 3 Matrices Given A and B : a. Find the sum. b. Find the difference. A =  

4 -2 2    and B =   6 10 -2

-5 2 -2   

**Solution**
a. Add the corresponding entries.

A + B =  

4 -2 2    +   6 10 -2

-5 2 -2   

=   2 + 6 -10 + 10 -2 - 2

4 - 5 -2 + 2 2 - 2   

=  

-1 0 -0    b. Subtract the corresponding entries.

A - B =  

4 -2 2    -   6 10 -2

-5 2 -2   

=   2 - 6 -10 - 10 -2 + 2

14 - 0 12 + 12 10 + 4

4 + 5 -2 - 2 2 + 2   

=   -4 -20 0

9 -4 4   

**Try It #1**
Add matrix A and matrix B. A =     1 0  -3    and B =    -2  1 5 -4     Finding Scalar Multiples of a Matrix Besides adding and subtracting whole matrices, there are many situations in which we need to multiply a matrix by a constant called a scalar. Recall that a scalar is a real number quantity that has magnitude, but not direction. For example, time, temperature, and distance are scalar quantities. The process of scalar multiplication involves multiplying each entry in a matrix by a scalar. A scalar multiple is any entry of a matrix that results from scalar multiplication. Consider a real-world scenario in which a university needs to add to its inventory of computers, computer tables, and chairs in two of the campus labs due to increased enrollment. They estimate that 15% more equipment is needed in both labs. The school’s current inventory is displayed in Table 2. Lab A Lab B Computers Computer Tables Chairs

Converting the data to a matrix, we have

C^{2}013 =  

   To calculate how much computer equipment will be needed, we multiply all entries in matrix C by 0.15.

   =  

   We must round up to the next integer, so the amount of new equipment needed is

 

   Adding the two matrices as shown below, we see the new inventory amounts.

 

   +  

   =  

   This means

C^{2}014 =  

   Thus, Lab A will have 18 computers, 19 computer tables, and 19 chairs; Lab B will have 32 computers, 40 computer tables, and 40 chairs. scalar multiplication Scalar multiplication involves finding the product of a constant by each entry in the matrix. Given

A =  a^{1}1 a^{1}2

a^{2}1 a^{2}2    the scalar multiple cA is

cA = c a^{1}1 a^{1}2

a^{2}1 a^{2}2   

=  ca^{1}1 ca^{1}2

ca^{2}1 ca^{2}2    Scalar multiplication is distributive. For the matrices A, B, and C with scalars a and b,

a(A + B) = aA + aB

(a + b)A = aA + bA

**Example  6**

### Multiplying the Matrix by a Scalar
Multiply matrix A by the scalar 3.

A =  8 1

   Solution Multiply each entry in A by the scalar 3.

3A = 3 8 1

  

=  3 ⋅ 8 3 ⋅ 1

3 ⋅ 5 3 ⋅ 4   

=   24 3


**Try It #2**
Given matrix B, find -2B where A =  4 1

  

**Example  7**
Finding the Sum of Scalar Multiples Find the sum 3A + 2B. A =   1 -2 0

0 -1 2

4 3 -6    and B =   -1 2 1

0 -3 2

0 1 -4    Solution First, find 3A, then 2B.

3A =   3 ⋅ 1 3(-2) 3 ⋅ 0

3 ⋅ 0 3(-1) 3 ⋅ 2

3 ⋅ 4 3 ⋅ 3 3(-6)   

=   3 -6 0

0 -3 6

  

2B =   2(-1) 2 ⋅ 2 2 ⋅ 1

2 ⋅ 0 2(-3) 2 ⋅ 2

2 ⋅ 0 2 ⋅ 1 2(-4)   

=   -2 4 2

0 -6 4

0 2 -8    Now, add 3A + 2B.

3A + 2B =   3 -6 0

0 -3 6

   +   -2 4 2

0 -6 4

0 2 -8   

=   3 - 2 -6 + 4 0 + 2

0 + 0 -3 - 6 6 + 4

12 + 0 9 + 2 -18 - 8   

=   1 -2 2

0 -9 10

   Finding the Product of Two Matrices In addition to multiplying a matrix by a scalar, we can multiply two matrices. Finding the product of two matrices is only possible when the inner dimensions are the same, meaning that the number of columns of the first matrix is equal to the number of rows of the second matrix. If A is an m \times  r matrix and B is an r \times  n matrix, then the product matrix AB is an m \times  n matrix. For example, the product AB is possible because the number of columns in A is the same as the number of rows in B. If the inner dimensions do not match, the product is not defined. A ⋅ B 2 \times  3 3 \times  3 same We multiply entries of A with entries of B according to a specific pattern as outlined below. The process of matrix multiplication becomes clearer when working a problem with real numbers. To obtain the entries in row i of AB, we multiply the entries in row i of A by column j in B and add. For example, given matrices A and B, where the dimensions of A are 2 \times  3 and the dimensions of B are 3 \times  3, the product of AB will be a 2 \times  3 matrix.

A =  a^{1}1 a^{1}2 a^{1}3

a^{2}1 a^{2}2 a^{2}3    and B =   b^{1}1 b^{1}2 b^{1}3

b^{2}1 b^{2}2 b^{2}3

b^{3}1 b^{3}2 b^{3}3   

Multiply and add as follows to obtain the first entry of the product matrix AB. 1. To obtain the entry in row 1, column 1 of AB, multiply the first row in A by the first column in B, and add.

[a^{1}1 a^{1}2 a^{1}3]  b^{1}1

b^{2}1 b^{3}1    = a^{1}1 ⋅ b^{1}1 + a^{1}2 ⋅ b^{2}1 + a^{1}3 ⋅ b^{3}1 2. To obtain the entry in row 1, column 2 of AB, multiply the first row of A by the second column in B, and add.

[a^{1}1 a^{1}2 a^{1}3]  b^{1}2

b^{2}2 b^{3}2    = a^{1}1 ⋅ b^{1}2 + a^{1}2 ⋅ b^{2}2 + a^{1}3 ⋅ b^{3}2 3. To obtain the entry in row 1, column 3 of AB, multiply the first row of A by the third column in B, and add.

[a^{1}1 a^{1}2 a^{1}3]  b^{1}3

b^{2}3 b^{3}3    = a^{1}1 ⋅ b^{1}3 + a^{1}2 ⋅ b^{2}3 + a^{1}3 ⋅ b^{3}3 We proceed the same way to obtain the second row of AB. In other words, row 2 of A times column 1 of B; row 2 of A times column 2 of B; row 2 of A times column 3 of B. When complete, the product matrix will be AB =  a^{1}1 ⋅ b^{1}1 + a^{1}2 ⋅ b^{2}1 + a^{1}3 ⋅ b^{3}1 a^{1}1 ⋅ b^{1}2 + a^{1}2 ⋅ b^{2}2 + a^{1}3 ⋅ b^{3}2 a^{1}1 ⋅ b^{1}3 + a^{1}2 ⋅ b^{2}3 + a^{1}3 ⋅ b^{3}3

a^{2}1 ⋅ b^{1}1 + a^{2}2 ⋅ b^{2}1 + a^{2}3 ⋅ b^{3}1 a^{2}1 ⋅ b^{1}2 + a^{2}2 ⋅ b^{2}2 + a^{2}3 ⋅ b^{3}2 a^{2}1 ⋅ b^{1}3 + a^{2}2 ⋅ b^{2}3 + a^{2}3 ⋅ b^{3}3    properties of matrix multiplication For the matrices A, B, and C the following properties hold. • Matrix multiplication is associative: (AB)C = A(BC).

C(A + B) = CA + CB, • Matrix multiplication is distributive:

(A + B)C = AC + BC. Note that matrix multiplication is not commutative.

**Example  8**

### Multiplying Two Matrices
Multiply matrix A and matrix B. A =  1 2

   and B =  5 6

   Solution First, we check the dimensions of the matrices. Matrix A has dimensions 2 \times  2 and matrix B has dimensions 2 \times  2. The inner dimensions are the same so we can perform the multiplication. The product will have the dimensions 2 \times  2. We perform the operations outlined previously.

AB =  1 2

   5 6

  

=  1(5) + 2(7) 1(6) + 2(8)

3(5) + 4(7) 3(6) + 4(8)   

=  19 22

  

**Example  9**

### Multiplying Two Matrices
Given A and B : a. Find AB. b. Find BA.

A =  -1 2 3

4 0 5   and B =   5 -1

-4 0

  


**Solution**
a. As the dimensions of A are 2 \times  3 and the dimensions of B are 3 \times  2, these matrices can be multiplied together because the number of columns in A matches the number of rows in B. The resulting product will be a 2 \times  2 matrix, the number of rows in A by the number of columns in B.

AB =  -1 2 3

4 0 5    5 -1

-4 0

  

=  -1(5) + 2(-4) + 3(2) -1(-1) + 2(0) + 3(3)

4(5) + 0(-4) + 5(2) 4(-1) + 0(0) + 5(3)  

=  -7 10

b. The dimensions of B are 3 \times  2 and the dimensions of A are 2 \times  3. The inner dimensions match so the product is defined and will be a 3 \times  3 matrix.

BA =   5 -1

-4 0

   -1 2 3

4 0 5  

=   5(-1) + -1(4) 5(2) + -1(0) 5(3) + -1(5)

-4(-1) + 0(4) -4(2) + 0(0) -4(3) + 0(5)

2(-1) + 3(4) 2(2) + 3(0) 2(3) + 3(5)   

=   -9 10 10

10 4 21    Analysis Notice that the products AB and BA are not equal. AB =  -7 10

30 11   \neq    -9 10 10

10 4 21    = BA This illustrates the fact that matrix multiplication is not commutative. Is it possible for AB to be defined but not BA? Yes, consider a matrix A with dimension 3 \times  4 and matrix B with dimension 4 \times  2. For the product AB the inner dimensions are 4 and the product is defined, but for the product BA the inner dimensions are 2 and 3 so the product is undefined.

**Example  10**
Using Matrices in Real-World Problems Let’s return to the problem presented at the opening of this section. We have Table 3, representing the equipment needs of two soccer teams. Wildcats Mud Cats Goals Balls Jerseys We are also given the prices of the equipment, as shown in Table 4. Goals $300 Balls $10 Jerseys $30

We will convert the data to matrices. Thus, the equipment need matrix is written as

E =  

   The cost matrix is written as

We perform matrix multiplication to obtain costs for the equipment.

CE = [300 10 30] 

  

The total cost for equipment for the Wildcats is $2,520, and the total cost for equipment for the Mud Cats is $3,840.

**How To…**
Given a matrix operation, evaluate using a calculator. 1. Save each matrix as a matrix variable [A], [B], [C], ... 2. Enter the operation into the calculator, calling up each matrix variable as needed. 3. If the operation is defined, the calculator will present the solution matrix; if the operation is undefined, it will display an error message.

**Example  11**
Using a Calculator to Perform Matrix Operations Find AB - C given A =  

  , B =  

-24 52 19

  , and C =  

  . Solution On the matrix page of the calculator, we enter matrix A above as the matrix variable [A], matrix B above as the matrix variable [B], and matrix C above as the matrix variable [C]. On the home screen of the calculator, we type in the problem and call up each matrix variable as needed. [A]\times [B] - [C] The calculator gives us the following matrix.  

   Access these online resources for additional instruction and practice with matrices and matrix operations. • Dimensions of a Matrix (http://openstaxcollege.org/l/matrixdimen) • Matrix Addition and Subtraction (http://openstaxcollege.org/l/matrixaddsub) • Matrix Operations (http://openstaxcollege.org/l/matrixoper) • Matrix Multiplication (http://openstaxcollege.org/l/matrixmult)


### 9.5 Section Exercises
Verbal 1. Can we add any two matrices together? If so, explain why; if not, explain why not and give an example of two matrices that cannot be added together. 2. Can we multiply any column matrix by any row matrix? Explain why or why not. 3. Can both the products AB and BA be defined? If so, explain how; if not, explain why. 4. Can any two matrices of the same size be multiplied? If so, explain why, and if not, explain why not and give an example of two matrices of the same size that cannot be multiplied together. 5. Does matrix multiplication commute? That is, does AB = BA? If so, prove why it does. If not, explain why it does not. Algebraic For the following exercises, use the matrices below and perform the matrix addition or subtraction. Indicate if the operation is undefined. A =  1 3

0 7  , B =   2 14

22 6  , C =  

  , D =  

  , E =   6 12

14 5  , F =  

   6. A + B 7. C + D 8. A + C 9. B - E 10. C + F 11. D - B For the following exercises, use the matrices below to perform scalar multiplication. A =   4 6

13 12  , B =  

  , C =  16 3 7 18

90 5 3 29  , D =  

   __ 2 C For the following exercises, use the matrices below to perform matrix multiplication. A =  -1 5

3 2  , B =   3 6 4

-8 0 12  , C =  

-2 6

  , D =   2 -3 12

9 3 1

0 8 -10    For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed. A =  2 -5

6 7  , B =  -9 6

-4 2   , C =  0 9

7 1  , D =   -8 7 -5

  , E =   4 5 3

7 -6 -5

1 0 9    24. A + B - C


## 9.5 Section Exercises
For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed. (Hint: A^{2} = A ⋅ A) A =  -10 20

5 25  , B =   40 10

-20 30  , C =   -1 0

0 -1

   38. A^{2} B^{2} 39. (AB)^{2} 40. (BA)^{2} For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed. (Hint: A^{2} = A ⋅ A) A =  1 0

2 3  , B =  -2 3 4

-1 1 -5  , C =  

  , D =  

-6 7 5

   48. (AB)C 49. A(BC) Technology For the following exercises, use the matrices below to perform the indicated operation if possible. If not possible, explain why the operation cannot be performed. Use a calculator to verify your solution. A =   -2 0 9

  , B =  

  , C =  

   Extensions For the following exercises, use the matrix below to perform the indicated operation on the given matrix. B =      0 0 1      59. Using the above questions, find a formula for Bn. Test the formula for B^{2}01 and B^{2}02, using a calculator.


## 9.6 Solving Systems with Gaussian EliMination
Carl Friedrich Gauss lived during the late 18th century and early 19th century, but he is still considered one of the most prolific mathematicians in history. His contributions to the science of mathematics and physics span fields such as algebra, number theory, analysis, differential geometry, astronomy, and optics, among others. His discoveries regarding matrix theory changed the way mathematicians have worked for the last two centuries. We first encountered Gaussian elimination in Systems of Linear Equations: Two Variables. In this section, we will revisit this technique for solving systems, this time using matrices. Writing the Augmented Matrix of a System of Equations A matrix can serve as a device for representing and solving a system of equations. To express a system in matrix form, we extract the coefficients of the variables and the constants, and these become the entries of the matrix. We use a vertical line to separate the coefficient entries from the constants, essentially replacing the equal signs. When a system is written in this form, we call it an augmented matrix. For example, consider the following 2 \times  2 system of equations.

3x + 4y = 7

4x - 2y = 5 We can write this system as an augmented matrix:   3 4

4 -2 ∣  7 5   We can also write a matrix containing just the coefficients. This is called the coefficient matrix.   3 4

4 -2   Learning Objectives
In this section, you will:
• Write the augmented matrix of a system of equations.
• Write the system of equations from an augmented matrix.
• Perform row operations on a matrix.
• Solve a system of linear equations using matrices.
A three-by-three system of equations such as

3x - y - z = 0

x + y = 5

2x - 3z = 2 has a coefficient matrix   3 -1 -1

1 1 0

2 0 -3    and is represented by the augmented matrix   3 -1 -1

1 1 0

2 0 -3  ∣    

   Notice that the matrix is written so that the variables line up in their own columns: x-terms go in the first column, y-terms in the second column, and z-terms in the third column. It is very important that each equation is written in standard form ax + by + cz = d so that the variables line up. When there is a missing variable term in an equation, the coefficient is 0.

**How To…**
Given a system of equations, write an augmented matrix. 1. Write the coefficients of the x-terms as the numbers down the first column. 2. Write the coefficients of the y-terms as the numbers down the second column. 3. If there are z-terms, write the coefficients as the numbers down the third column. 4. Draw a vertical line and write the constants to the right of the line.

**Example  1**

### Writing the Augmented Matrix for a System of Equations
Write the augmented matrix for the given system of equations.

x + 2y - z = 3

2x - y + 2z = 6

x - 3y + 3z = 4 Solution The augmented matrix displays the coefficients of the variables, and an additional column for the constants.   1 2 -1

2 -1 2

1 -3 3  ∣    

  

**Try It #1**
Write the augmented matrix of the given system of equations.

4x - 3y = 11

3x + 2y = 4 Writing a System of Equations from an Augmented Matrix We can use augmented matrices to help us solve systems of equations because they simplify operations when the systems are not encumbered by the variables. However, it is important to understand how to move back and forth between formats in order to make finding solutions smoother and more intuitive. Here, we will use the information in an augmented matrix to write the system of equations in standard form.


**Example  2**

### Writing a System of Equations from an Augmented Matrix Form
Find the system of equations from the augmented matrix.   1 -3 -5

2 -5 -4

-3 5 4  ∣     -2

   Solution When the columns represent the variables x, y, and z,   1 -3 -5

2 -5 -4

-3 5 4  ∣     -2

   →  x - 3y - 5z = - 2

2x - 5y - 4z = 5

-3x + 5y + 4z = 6 

**Try It #2**
Write the system of equations from the augmented matrix.  

 ∣    

-9    Performing Row Operations on a Matrix Now that we can write systems of equations in augmented matrix form, we will examine the various row operations that can be performed on a matrix, such as addition, multiplication by a constant, and interchanging rows. Performing row operations on a matrix is the method we use for solving a system of equations. In order to solve the system of equations, we want to convert the matrix to row-echelon form, in which there are ones down the main diagonal from the upper left corner to the lower right corner, and zeros in every position below the main diagonal as shown. Row-echelon form   1 a b

0 1 d

   We use row operations corresponding to equation operations to obtain a new matrix that is row-equivalent in a simpler form. Here are the guidelines to obtaining row-echelon form. 1. In any nonzero row, the first nonzero number is a 1. It is called a leading 1. 2. Any all-zero rows are placed at the bottom on the matrix. 3. Any leading 1 is below and to the right of a previous leading 1. 4. Any column containing a leading 1 has zeros in all other positions in the column. To solve a system of equations we can perform the following row operations to convert the coefficient matrix to row- echelon form and do back-substitution to find the solution. 1. Interchange rows. (Notation: Ri ↔ Rj ) 2. Multiply a row by a constant. (Notation: cRi ) 3. Add the product of a row multiplied by a constant to another row. (Notation: Ri + cRj) Each of the row operations corresponds to the operations we have already learned to solve systems of equations in three variables. With these operations, there are some key moves that will quickly achieve the goal of writing a matrix in row-echelon form. To obtain a matrix in row-echelon form for finding solutions, we use Gaussian elimination, a method that uses row operations to obtain a 1 as the first entry so that row 1 can be used to convert the remaining rows.

Gaussian elimination The Gaussian elimination method refers to a strategy used to obtain the row-echelon form of a matrix. The goal is to write matrix A with the number 1 as the entry down the main diagonal and have all zeros below. A =   a^{1}1 a^{1}2 a^{1}3

a^{2}1 a^{2}2 a^{2}3

a^{3}1 a^{3}2 a^{3}3    After Gaussian elimination A =   1 b^{1}2 b^{1}3

0 1 b^{2}3

   The first step of the Gaussian strategy includes obtaining a 1 as the first entry, so that row 1 may be used to alter the rows below.

**How To…**
Given an augmented matrix, perform row operations to achieve row-echelon form. 1. The first equation should have a leading coefficient of 1. Interchange rows or multiply by a constant, if necessary. 2. Use row operations to obtain zeros down the first column below the first entry of 1. 3. Use row operations to obtain a 1 in row 2, column 2. 4. Use row operations to obtain zeros down column 2, below the entry of 1. 5. Use row operations to obtain a 1 in row 3, column 3. 6. Continue this process for all rows until there is a 1 in every entry down the main diagonal and there are only zeros below. 7. If any rows contain all zeros, place them at the bottom.

**Example  3**

### Solving a 2 \times  2 System by Gaussian Elimination
Solve the given system by Gaussian elimination.

2x + 3y = 6

x - y =  1 __ 2  Solution First, we write this as an augmented matrix.

  2 3

1 -1  ∣    6  1 _ 2    We want a 1 in row 1, column 1. This can be accomplished by interchanging row 1 and row 2.

R^{1} ↔ R^{2} →   1 -1

2 3 ∣   1 _ 2  6   We now have a 1 as the first entry in row 1, column 1. Now let’s obtain a 0 in row 2, column 1. This can be accomplished by multiplying row 1 by -2, and then adding the result to row 2.

-2R^{1} + R^{2} = R^{2} →   1 -1

0 5 ∣   1 _ 2  5   We only have one more step, to multiply row 2 by  1 __ 5 .

 1 __ 5  R^{2} = R^{2} →   1 -1

0 1 ∣   1 _ 2  1   Use back-substitution. The second row of the matrix represents y = 1. Back-substitute y = 1 into the first equation.

x - (1) =  1 __ 2 

x =  3 __ 2  The solution is the point   3 __


**Try It #3**
Solve the given system by Gaussian elimination.

4x + 3y = 11

x - 3y = -1

**Example  4**
Using Gaussian Elimination to Solve a System of Equations Use Gaussian elimination to solve the given 2 \times  2 system of equations.

2x + y = 1

4x + 2y = 6 Solution Write the system as an augmented matrix.

 2 1

4 2 ∣  1 6   Obtain a 1 in row 1, column 1. This can be accomplished by multiplying the first row by  1 __ 2 .

 1 __ 2 R^{1} = R^{1} →  1  1 _ 2 

4 2 ∣   1 _ 2  6   Next, we want a 0 in row 2, column 1. Multiply row 1 by -4 and add row 1 to row 2.

-4R^{1} + R^{2} = R^{2} →  1  1 _ 2 

0 0 ∣   1 _ 2  4   The second row represents the equation 0 = 4. Therefore, the system is inconsistent and has no solution.

**Example  5**

### Solving a Dependent System
Solve the system of equations.

3x + 4y = 12

6x + 8y = 24 Solution Perform row operations on the augmented matrix to try and achieve row-echelon form.

A =  3 4

6 8 ∣  12 24  

- 1 __ 2 R^{2} + R^{1} = R^{1} →  0 0

6 8 ∣   0 24  

R^{1} ↔ R^{2} →  6 8

0 0 ∣  24 0   The matrix ends up with all zeros in the last row: 0y = 0. Thus, there are an infinite number of solutions and the system is classified as dependent. To find the generic solution, return to one of the original equations and solve for y.

3x + 4y = 12

4y = 12 - 3x

y = 3 -  3 __ 4 x So the solution to this system is  x, 3 -  3 __ 4 x  .

**Example  6**
Performing Row Operations on a 3 \times  3 Augmented Matrix to Obtain Row-Echelon Form Perform row operations on the given matrix to obtain row-echelon form.  

-3 3 4  ∣    

   Solution The first row already has a 1 in row 1, column 1. The next step is to multiply row 1 by -2 and add it to row 2.

Then replace row 2 with the result. -2R^{1} + R^{2} = R^{2} →   1 -3 4

0 1 -2

-3 3 4  ∣    

   Next, obtain a zero in row 3, column 1.

3R^{1} + R^{3} = R^{3} →   1 -3 4

0 1 -2

 ∣    

   Next, obtain a zero in row 3, column 2.

6R^{2} + R^{3} = R^{3} →   1 -3 4

0 1 -2

0 0 4  ∣    

   The last step is to obtain a 1 in row 3, column 3.

 1 __ 2 R^{3} = R^{3} →   1 -3 4

0 1 -2

0 0 1  ∣    

-6

 21 __ 2    

**Try It #4**
Write the system of equations in row-echelon form.

x - 2y + 3z = 9

-x + 3y = - 4

2x - 5y + 5z = 17 Solving a System of Linear Equations Using Matrices We have seen how to write a system of equations with an augmented matrix, and then how to use row operations and back-substitution to obtain row-echelon form. Now, we will take row-echelon form a step farther to solve a 3 by 3 system of linear equations. The general idea is to eliminate all but one variable using row operations and then back- substitute to solve for the other variables.

**Example  7**

### Solving a System of Linear Equations Using Matrices
Solve the system of linear equations using matrices.

x - y + z = 8

2x + 3y - z = -2

3x - 2y - 9z = 9 Solution First, we write the augmented matrix.   1 -1 1

2 3 -1

3 -2 -9  ∣    

-2

   Next, we perform row operations to obtain row-echelon form. -2R^{1} + R^{2} = R^{2} →   1 -1 1

0 5 -3

3 -2 -9  ∣    

-18

   -3R^{1} + R^{3} = R^{3} →   1 -1 1

0 5 -3

0 1 -12  ∣    

-18

-15    The easiest way to obtain a 1 in row 2 of column 1 is to interchange R^{2} and R^{3}.

Interchange R^{2} and R^{3} →   1 -1 1 8

0 1 -12 -15

0 5 -3 -18   

Then -5R^{2} + R^{3} = R^{3} →   1 -1 1

0 1 -12

0 0 57  ∣    

-15

   -  1 ___ 57  R^{3} = R^{3} →   1 -1 1

0 1 -12

0 0 1  ∣    

-15

   The last matrix represents the equivalent system.

x - y + z = 8

y - 12z = -15

z = 1 Using back-substitution, we obtain the solution as (4, -3, 1).

**Example  8**

### Solving a Dependent System of Linear Equations Using Matrices
Solve the following system of linear equations using matrices.

-x - 2y + z = -1

2x + 3y = 2

y - 2z = 0 Solution Write the augmented matrix.   -1 -2 1

0 1 -2  ∣     -1

   First, multiply row 1 by -1 to get a 1 in row 1, column 1. Then, perform row operations to obtain row-echelon form.

-R^{1} →   -1 -2 1

0 1 -2  ∣     -1

  

R^{2} ↔ R^{3} →  

 ∣    

  

-2R^{1} + R^{3} = R^{3} →   1 2 -1

0 1 -2

0 -1 2  ∣    

  

R^{2} + R^{3} = R^{3} →  

 ∣    

   The last matrix represents the following system.

x + 2y - z = 1

y - 2z = 0

0 = 0 We see by the identity 0 = 0 that this is a dependent system with an infinite number of solutions. We then find the generic solution. By solving the second equation for y and substituting it into the first equation we can solve for z in terms of x.

x + 2y - z = 1

y = 2z

x + 2(2z) - z = 1

x + 3z = 1

z =  1 - x _____ 

Now we substitute the expression for z into the second equation to solve for y in terms of x.

y - 2z = 0

z =  1 - x _____ 

y - 2  1 - x _____    = 0

y =  2 - 2x ______  The generic solution is  x,  2 - 2x ______ ,  1 - x _____   .

**Try It #5**
Solve the system using matrices.

x + 4y - z = 4

2x + 5y + 8z = 15

x + 3y - 3z = 1 Can any system of linear equations be solved by Gaussian elimination? Yes, a system of linear equations of any size can be solved by Gaussian elimination.

**How To…**
Given a system of equations, solve with matrices using a calculator. 1. Save the augmented matrix as a matrix variable [A], [B], [C], ... . 2. Use the ref( function in the calculator, calling up each matrix variable as needed.

**Example  9**

### Solving Systems of Equations with Matrices Using a Calculator
Solve the system of equations.

5x + 3y + 9z = -1

-2x + 3y - z = -2

-x - 4y + 5z = 1 Solution Write the augmented matrix for the system of equations.

 

-2 3 -1

-1 -4 5  ∣     -1

-2

-1    On the matrix page of the calculator, enter the augmented matrix above as the matrix variable [A]. [A] =   5 3 9 -1

-2 3 -1 -2

-1 -4 5 1    Use the ref( function in the calculator, calling up the matrix variable [A].

ref([A]) Evaluate.     3 _ 5    9 _ 5    1 _ 5  

0 1  13 __ 21  - 4 _ 7  

   - 24 ___ 187     →  x +  3 _ 5 y +  9 _ 5 z = - 1 _ 5  

y +  13 __ 21 z = - 4 _ 7   z = - 24 ___ 187   Using back-substitution, the solution is   61 ___ ___ ___


**Example  10**

### Applying 2 \times  2 Matrices to Finance
Carolyn invests a total of $12,000 in two municipal bonds, one paying 10.5% interest and the other paying 12% interest. The annual interest earned on the two investments last year was $1,335. How much was invested at each rate? Solution We have a system of two equations in two variables. Let x = the amount invested at 10.5% interest, and y = the amount invested at 12% interest.

As a matrix, we have  

Multiply row 1 by -0.105 and add the result to row 2.   1 1

75   Then,

Thus, $5,000 was invested at 12% interest and $7,000 at 10.5% interest.

**Example  11**

### Applying 3 \times  3 Matrices to Finance
Ava invests a total of $10,000 in three accounts, one paying 5% interest, another paying 8% interest, and the third paying 9% interest. The annual interest earned on the three investments last year was $770. The amount invested at 9% was twice the amount invested at 5%. How much was invested at each rate? Solution We have a system of three equations in three variables. Let x be the amount invested at 5% interest, let y be the amount invested at 8% interest, and let z be the amount invested at 9% interest. Thus,

x + y + z = 10,000

2x - z = 0 As a matrix, we have   1 1 1

2 0 -1  ∣    

   Now, we perform Gaussian elimination to achieve row-echelon form.

-0.05R^{1} + R^{2} = R^{2} →   1 1 1

2 0 -1  ∣    

  

-2R^{1} + R^{3} = R^{3} →   1 1 1

0 -2 -3  ∣    

  

 1 ____ 0.03 R^{2} = R^{2} →   0 1 1

0 1  4 _ 3 

0 -2 -3  ∣    

  

2R^{2} + R^{3} = R^{3} →  

0 1  4 _ 3 

0 0 - 1 _ 3   ∣    

   The third row tells us - 1 __

The second row tells us y +  4 __ 3 z = 9,000. Substituting z = 6,000, we get

y +  4 __

The first row tells us x + y + z = 10, 000. Substituting y = 1,000 and z = 6,000, we get

The answer is $3,000 invested at 5% interest, $1,000 invested at 8%, and $6,000 invested at 9% interest.

**Try It #6**
A small shoe company took out a loan of $1,500,000 to expand their inventory. Part of the money was borrowed at 7%, part was borrowed at 8%, and part was borrowed at 10%. The amount borrowed at 10% was four times the amount borrowed at 7%, and the annual interest on all three loans was $130,500. Use matrices to find the amount borrowed at each rate. Access these online resources for additional instruction and practice with solving systems of linear equations using Gaussian elimination. • Solve a System of Two Equations Using an Augmented Matrix (http://openstaxcollege.org/l/system^{2}augmat) • Solve a System of Three Equations Using an Augmented Matrix (http://openstaxcollege.org/l/system^{3}augmat) • Augmented Matrices on the Calculator (http://openstaxcollege.org/l/augmatcalc)


### 9.6 Section Exercises
Verbal 1. Can any system of linear equations be written as an augmented matrix? Explain why or why not. Explain how to write that augmented matrix. 2. Can any matrix be written as a system of linear equations? Explain why or why not. Explain how to write that system of equations. 3. Is there only one correct method of using row operations on a matrix? Try to explain two different row operations possible to solve the augmented matrix  9 3

1 -2 ∣  0 6  . 4. Can a matrix whose entry is 0 on the diagonal be solved? Explain why or why not. What would you do to remedy the situation? 5. Can a matrix that has 0 entries for an entire row have one solution? Explain why or why not. Algebraic For the following exercises, write the augmented matrix for the linear system. 2x + 12y = 3 9x - y = 2 8. 3x + 2y + 10z = 3 -6x + 2y + 5z = 13 4x + z = 18 9. x + 5y + 8z = 19 12x + 3y = 4 3x + 4y + 9z = -7 19x - 5y + 3z = -9 x + 2y = -8 For the following exercises, write the linear system from the augmented matrix. 11.  -2 5

6 -18 ∣   5 26   12.   3 4

10 17 ∣   10

13.  

-1 -9 4

 ∣    

-1

   14.  

-1 7 5

 ∣    

   15.  

 ∣    

-5    For the following exercises, solve the system by Gaussian elimination.

0 0 ∣  3 0  

1 0 ∣  1 2  

4 5 ∣  3 6   19.  -1 2

4 -5 ∣  -3 6  

0 2 ∣   1

-1   5x + 4y = 58 3x + 4y = -17 4x + y = 14 24. -4x - 3y = -2 3x - 5y = -13 10x + 6y = 5 26. 3x + 4y = 12 -6x - 8y = -24 29. 2x - y = 2 3x + 2y = 17 __ 4 x -  3 __ 5 y = 4  1 __ 4 x +  2 __ 3 y = 1 __ 4 x -  2 __ 3 y = -1  1 __ 2 x +  1 __ 3 y = 3  

 ∣    

    

 ∣    

-90     

 ∣    

  


## 9.6 Section Exercises
 

 ∣     0.2

0.8

-0.8    37. -2x + 3y - 2z = 3 4x + 2y - z = 9 4x - 8y + 2z = -6 38. x + y - 4z = -4 5x - 3y - 2z = 0 2x + 6y + 7z = 30 39. 2x + 3y + 2z = 1 -4x - 6y - 4z = -2 40. x + 2y - z = 1 -x - 2y + 2z = -2 3x + 6y - 3z = 5 41. x + 2y - z = 1 -x - 2y + 2z = -2 3x + 6y - 3z = 3 42. x + y = 2 x + z = 1 -y - z = -3 43. x + y + z = 100 x + 2z = 125 -y + 2z = 25 __ 4 x -  2 __ 3 z = - 1 __ 2   1 __ 5 x +  1 __ 3 y =  4 __ 7   1 __ 5 y - 1 __ 3 z =  2 __ 9  __ 2 x +  1 __ 2 y +  1 __ 7 z = - 53 ___ 14   1 __ 2 x -  1 __ 2 y +  1 __ 4 z = 3  1 __ 4 x +  1 __ 5 y +  1 __ 3 z =  23 ___ 15  __ 2 x -  1 __ 3 y +  1 __ 4 z = - 29 ___ 6   1 __ 5 x +  1 __ 6 y -  1 __ 7 z =  431 ___ 210  - 1 __ 8 x +  1 __ 9 y +  1 ___ 10 z = - 49 ___ 45  Extensions For the following exercises, use Gaussian elimination to solve the system. _____  +  y - 2 _____  +  z - 3 _____  = 0 x + y + z = 6  x + 2 _____  + 2y +  z-3 ____ 3  = 5 _____  -  y + 1 _____  + 3z = -1  x + 5 _____  +  y + 7 _____  - z = 4 x + y -  z-2 ____ 2  = 1 49.  x - 3 _____  -  y - 1 _____  + 2z = -1  x + 5 _____  +  y + 5 _____  +  z + 5 _____  = 8 x + y + z = 1 50.  x - 3 _____ 10  +  y + 3 _____  -2z = 3  x + 5 _____  -  y - 1 _____  + z =  3 __ 2   x - 1 _____  +  y + 4 _____  + 3z =  3 __ 2  51.  x - 3 _____  -  y - 1 _____  + 2z = -1  x + 5 _____  +  y + 5 _____  +  z + 5 _____  = 7 x + y + z = 1 Real-World Applications For the following exercises, set up the augmented matrix that describes the situation, and solve for the desired solution. 52. Every day, a cupcake store sells 5,000 cupcakes in chocolate and vanilla flavors. If the chocolate flavor is 3 times as popular as the vanilla flavor, how many of each cupcake sell per day? 53. At a competing cupcake store, $4,520 worth of cupcakes are sold daily. The chocolate cupcakes cost $2.25 and the red velvet cupcakes cost $1.75. If the total number of cupcakes sold per day is 2,200, how many of each flavor are sold each day? 54. You invested $10,000 into two accounts: one that has simple 3% interest, the other with 2.5% interest. If your total interest payment after one year was $283.50, how much was in each account after the year passed? 55. You invested $2,300 into account 1, and $2,700 into account 2. If the total amount of interest after one year is $254, and account 2 has 1.5 times the interest rate of account 1, what are the interest rates? Assume simple interest rates.

56. Bikes’R’Us manufactures bikes, which sell for $250. It costs the manufacturer $180 per bike, plus a startup fee of $3,500. After how many bikes sold will the manufacturer break even? 57. A major appliance store is considering purchasing vacuums from a small manufacturer. The store would be able to purchase the vacuums for $86 each, with a delivery fee of $9,200, regardless of how many vacuums are sold. If the store needs to start seeing a profit after 230 units are sold, how much should they charge for the vacuums? 58. The three most popular ice cream flavors are chocolate, strawberry, and vanilla, comprising 83% of the flavors sold at an ice cream shop. If vanilla sells 1% more than twice strawberry, and chocolate sells 11% more than vanilla, how much of the total ice cream consumption are the vanilla, chocolate, and strawberry flavors? 59. At an ice cream shop, three flavors are increasing in demand. Last year, banana, pumpkin, and rocky road ice cream made up 12% of total ice cream sales. This year, the same three ice creams made up 16.9% of ice cream sales. The rocky road sales doubled, the banana sales increased by 50%, and the pumpkin sales increased by 20%. If the rocky road ice cream had one less percent of sales than the banana ice cream, find out the percentage of ice cream sales each individual ice cream made last year. 60. A bag of mixed nuts contains cashews, pistachios, and almonds. There are 1,000 total nuts in the bag, and there are 100 less almonds than pistachios. The cashews weigh 3 g, pistachios weigh 4 g, and almonds weigh 5 g. If the bag weighs 3.7 kg, find out how many of each type of nut is in the bag. 61. A bag of mixed nuts contains cashews, pistachios, and almonds. Originally there were 900 nuts in the bag. 30% of the almonds, 20% of the cashews, and 10% of the pistachios were eaten, and now there are 770 nuts left in the bag. Originally, there were 100 more cashews than almonds. Figure out how many of each type of nut was in the bag to begin with.


## 9.7 Solving Systems with Inverses
Nancy plans to invest $10,500 into two different bonds to spread out her risk. The first bond has an annual return of 10%, and the second bond has an annual return of 6%. In order to receive an 8.5% return from the two bonds, how much should Nancy invest in each bond? What is the best method to solve this problem? There are several ways we can solve this problem. As we have seen in previous sections, systems of equations and matrices are useful in solving real-world problems involving finance. After studying this section, we will have the tools to solve the bond problem using the inverse of a matrix. Finding the Inverse of a Matrix We know that the multiplicative inverse of a real number a is a-1, and aa-1 = a-1 a =   1 __ a   a = 1. For example, 2-1 =  1 __ 2  and   1 __ 2   2 = 1. The multiplicative inverse of a matrix is similar in concept, except that the product of matrix A and its inverse A-1 equals the identity matrix. The identity matrix is a square matrix containing ones down the main diagonal and zeros everywhere else. We identify identity matrices by In where n represents the dimension of the matrix. The following equations are the identity matrices for a 2 \times  2 matrix and a 3 \times  3 matrix, respectively.

I^{2} =  1 0

0 1  

I^{3} =  

   The identity matrix acts as a 1 in matrix algebra. For example, AI = IA = A. A matrix that has a multiplicative inverse has the properties

AA-1 = I

A-1 A = I A matrix that has a multiplicative inverse is called an invertible matrix. Only a square matrix may have a multiplicative inverse, as the reversibility, AA-1 = A-1 A = I, is a requirement. Not all square matrices have an inverse, but if A is invertible, then A-1 is unique. We will look at two methods for finding the inverse of a 2 \times  2 matrix and a third method that can be used on both 2 \times  2 and 3 \times  3 matrices. the identity matrix and multiplicative inverse The identity matrix, In, is a square matrix containing ones down the main diagonal and zeros everywhere else. I^{2} =  1 0

0 1   I^{3} =  

  

2 \times  2 3 \times  3 If A is an n \times  n matrix and B is an n \times  n matrix such that AB = BA = In, then B = A-1, the multiplicative inverse of a matrix A. Learning Objectives
In this section, you will:
• Find the inverse of a matrix.
• Solve a system of linear equations using an inverse matrix.

**Example  1**
Showing That the Identity Matrix Acts as a 1 Given matrix A, show that AI = IA = A.

A =   3 4

-2 5   Solution Use matrix multiplication to show that the product of A and the identity is equal to the product of the identity and A. AI =   3 4

-2 5    1 0

0 1   =   3 ⋅ 1 + 4 ⋅ 0 3 ⋅ 0 + 4 ⋅ 1

-2 ⋅ 1 + 5 ⋅ 0 -2 ⋅ 0 + 5 ⋅ 1   =   3 4

-2 5  

AI =  1 0

0 1     3 4

-2 5   =  1 ⋅ 3 + 0 ⋅ (-2) 1 ⋅ 4 + 0 ⋅ 5

0 ⋅ 3 + 1 ⋅ (-2) 0 ⋅ 4 + 1 ⋅ 5   =   3 4

-2 5  

**How To…**
Given two matrices, show that one is the multiplicative inverse of the other. 1. Given matrix A of order n \times  n and matrix B of order n \times  n multiply AB. 2. If AB = I, then find the product BA. If BA = I, then B = A-1 and A = B-1.

**Example  2**
Showing That Matrix A Is the Multiplicative Inverse of Matrix B Show that the given matrices are multiplicative inverses of each other.

A =   1 5

-2 -9  , B =  -9 -5

2 1   Solution Multiply AB and BA. If both products equal the identity, then the two matrices are inverses of each other.

AB =   1 5

-2 -9   -9 -5

2 1  

=   1(-9) + 5(2) 1(-5) + 5(1)

-2(-9) - 9(2) -2(-5) - 9(1)  

=  1 0

0 1  

BA =  -9 -5

2 1    1 5

-2 -9  

=  -9(1) - 5(-2) -9(5) - 5(-9)

2(1) + 1(-2) 2(-5) + 1(-9)  

=  1 0

0 1   A and B are inverses of each other.

**Try It #1**
Show that the following two matrices are inverses of each other. A =   1 4

-1 -3  , B =  -3 -4

1 1   Finding the Multiplicative Inverse Using Matrix Multiplication We can now determine whether two matrices are inverses, but how would we find the inverse of a given matrix? Since we know that the product of a matrix and its inverse is the identity matrix, we can find the inverse of a matrix by setting up an equation using matrix multiplication.


**Example  3**
Finding the Multiplicative Inverse Using Matrix Multiplication Use matrix multiplication to find the inverse of the given matrix.

A =  1 -2

2 -3   Solution For this method, we multiply A by a matrix containing unknown constants and set it equal to the identity.

 1 -2

2 -3    a b

c d   =  1 0

0 1   Find the product of the two matrices on the left side of the equal sign.

 1 -2

2 -3    a b

c d   =  1a - 2c 1b - 2d

2a - 3c 2b - 3d   Next, set up a system of equations with the entry in row 1, column 1 of the new matrix equal to the first entry of the identity, 1. Set the entry in row 2, column 1 of the new matrix equal to the corresponding entry of the identity, which is 0.

1a - 2c = 1 R^{1}

2a - 3c = 0 R^{2} Using row operations, multiply and add as follows: (-2)R^{1} + R^{2} → R^{2}. Add the equations, and solve for c.

1a - 2c = 1

0 + 1c = -2

c = -2 Back-substitute to solve for a.

a - 2(-2) = 1

a + 4 = 1

a = -3 Write another system of equations setting the entry in row 1, column 2 of the new matrix equal to the corresponding entry of the identity, 0. Set the entry in row 2, column 2 equal to the corresponding entry of the identity.

1b - 2d = 0 R^{1}

2b - 3d = 1 R^{2} Using row operations, multiply and add as follows: (-2)R^{1} + R^{2} = R^{2}. Add the two equations and solve for d.

1b - 2d = 0

0 + 1d = 1

d = 1 Once more, back-substitute and solve for b.

b - 2(1) = 0

b - 2 = 0

b = 2

A-1 =  -3 2

-2 1   Finding the Multiplicative Inverse by Augmenting with the Identity Another way to find the multiplicative inverse is by augmenting with the identity. When matrix A is transformed into I, the augmented matrix I transforms into A-1. For example, given

A =  2 1

5 3   augment A with the identity

 2 1

5 3 ∣  1 0

0 1   Perform row operations with the goal of turning A into the identity. 1. Switch row 1 and row 2.  5 3

2 1 ∣  0 1

1 0   2. Multiply row 2 by -2 and add to row 1.  1 1

2 1 ∣  -2 1

1 0   3. Multiply row 1 by -2 and add to row 2.  1 1

0 -1 ∣  -2 1

5 -2   4. Add row 2 to row 1.  1 0

0 -1 ∣  3 -1

5 -2   5. Multiply row 2 by -1.  1 0

0 1 ∣   3 -1

-5 2   The matrix we have found is A-1.

A-1 =   3 -1

-5 2   Finding the Multiplicative Inverse of 2 \times  2 Matrices Using a Formula When we need to find the multiplicative inverse of a 2 \times  2 matrix, we can use a special formula instead of using matrix multiplication or augmenting with the identity. If A is a 2 \times  2 matrix, such as

A =  a b

c d   the multiplicative inverse of A is given by the formula

A-1 =  _______ ad - bc  d -b

-c a   where ad - bc \neq  0. If ad - bc = 0, then A has no inverse.

**Example  4**
Using the Formula to Find the Multiplicative Inverse of Matrix A Use the formula to find the multiplicative inverse of

A =  1 -2

2 -3   Solution Using the formula, we have

A-1 =  ________________

(1)(-3) - (-2)(2)  -3 2

-2 1  

=  _______ -3 + 4  -3 2

-2 1  

=  -3 2

-2 1   Analysis We can check that our formula works by using one of the other methods to calculate the inverse. Let’s augment A with the identity.  1 -2

2 -3 ∣  1 0

0 1   Perform row operations with the goal of turning A into the identity.

1. Multiply row 1 by -2 and add to row 2.   1 -2

0 1 ∣   1 0

-2 1   2. Multiply row 1 by 2 and add to row 1.  1 0

0 1 ∣  -3 2

-2 1   So, we have verified our original solution.

A-1 =  -3 2

-2 1  

**Try It #2**
Use the formula to find the inverse of matrix A. Verify your answer by augmenting with the identity matrix.

A-1 =   1 -1

2 3  

**Example  5**
Finding the Inverse of the Matrix, If It Exists Find the inverse, if it exists, of the given matrix.

A =  3 6

1 2   Solution We will use the method of augmenting with the identity.  3 6

1 3 ∣  1 0

0 1   1. Switch row 1 and row 2.  1 3

3 6 ∣  0 1

1 0   2. Multiply row 1 by -3 and add it to row 2.  1 2

0 0 ∣   1 0

-3 1   3. There is nothing further we can do. The zeros in row 2 indicate that this matrix has no inverse. Finding the Multiplicative Inverse of 3 \times  3 Matrices Unfortunately, we do not have a formula similar to the one for a 2 \times  2 matrix to find the inverse of a 3 \times  3 matrix. Instead, we will augment the original matrix with the identity matrix and use row operations to obtain the inverse. Given a 3 \times  3 matrix

A =  

   augment A with the identity matrix

 A

A A  I =  

 ∣    

   To begin, we write the augmented matrix with the identity on the right and A on the left. Performing elementary row operations so that the identity matrix appears on the left, we will obtain the inverse matrix on the right. We will find the inverse of this matrix in the next example.

**How To…**
Given a 3 \times  3 matrix, find the inverse 1. Write the original matrix augmented with the identity matrix on the right. 2. Use elementary row operations so that the identity appears on the left. 3. What is obtained on the right is the inverse of the original matrix. 4. Use matrix multiplication to show that AA-1 = I and A-1 A = I.


**Example  6**
Finding the Inverse of a 3 \times  3 Matrix Given the 3 \times  3 matrix A, find the inverse.

A =  

   Solution Augment A with the identity matrix, and then begin row operations until the identity matrix replaces A. The matrix on the right will be the inverse of A.  

 ∣    

    

 ∣    

  

-R^{2} + R^{1} = R^{1} →  

 ∣    

  

-R^{2} + R^{3} = R^{3} →  

 ∣    

  

R^{3} ↔ R^{2} →  

 ∣    

  

-2R^{1} + R^{3} = R^{3} →  

 ∣     -1 1 0

-1 0 1

  

-3R^{2} + R^{3} = R^{3} →  

 ∣     -1 1 0

-1 0 1

6 -2 -3    Thus,

A-1 = B =   -1 1 0

-1 0 1

6 -2 -3    Analysis To prove that B = A-1, let’s multiply the two matrices together to see if the product equals the identity, if AA-1 = I and A-1 A = I.

AA-1 =  

     -1 1 0

-1 0 1

6 -2 -3    =   2(-1) + 3(-1) + 1(6) 2(1) + 3(0) + 1(-2) 2(0) + 3(1) + 1(-3)

3(-1) + 3(-1) + 1(6) 3(1) + 3(0) + 1(-2) 3(0) + 3(1) + 1(-3)

2(-1) + 4(-1) + 1(6) 2(1) + 4(0) + 1(-2) 2(0) + 4(1) + 1(-3)   

=  

  

A-1A =   -1 1 0

-1 0 1

6 -2 -3     

  

=   -1(2) + 1(3) + 0(2) -1(3) + 1(3) + 0(4) -1(1) + 1(1) + 0(1)

-1(2) + 0(3) + 1(2) -1(3) + 0(3) + 1(4) -1(1) + 0(1) + 1(1)

6(2) + -2(3) + -3(2) 6(3) + -2(3) + -3(4) 6(1) + -2(1) + -3(1)   

=  

   Interchange R^{2} and R^{1}


**Try It #3**
Find the inverse of the 3 \times  3 matrix.

A =  

-1 11 -7

0 3 -2    Solving a System of Linear Equations Using the Inverse of a Matrix Solving a system of linear equations using the inverse of a matrix requires the definition of two new matrices: X is the matrix representing the variables of the system, and B is the matrix representing the constants. Using matrix multiplication, we may define a system of equations with the same number of equations as variables as

AX = B To solve a system of linear equations using an inverse matrix, let A be the coefficient matrix, let X be the variable matrix, and let B be the constant matrix. Thus, we want to solve a system AX = B. For example, look at the following system of equations.

a^{1}x + b^{1}y = c^{1}

a^{2}x + b^{2}y = c^{2} From this system, the coefficient matrix is

A =  a^{1} b^{1}

a^{2} b^{2}   The variable matrix is

X =  x y   And the constant matrix is

B =  c^{1} c^{2}   Then AX = B looks like

 a^{1} b^{1}

a^{2} b^{2}    x y   =  c^{1} c^{2}   Recall the discussion earlier in this section regarding multiplying a real number by its inverse, (2-1) 2 =   1 __ 2   2 = 1. To solve a single linear equation ax = b for x, we would simply multiply both sides of the equation by the multiplicative inverse (reciprocal) of a. Thus,

ax = b

  1 __ a   ax =   1 __ a   b

(a-1)ax = (a-1)b

[(a-1)a]x = (a-1)b

1x = (a-1)b

x = (a-1)b The only difference between a solving a linear equation and a system of equations written in matrix form is that finding the inverse of a matrix is more complicated, and matrix multiplication is a longer process. However, the goal is the same—to isolate the variable. We will investigate this idea in detail, but it is helpful to begin with a 2 \times  2 system and then move on to a 3 \times  3 system.

solving a system of equations using the inverse of a matrix Given a system of equations, write the coefficient matrix A, the variable matrix X, and the constant matrix B. Then

AX = B Multiply both sides by the inverse of A to obtain the solution.

(A-1)AX = (A-1)B

[(A-1)A]X = (A-1)B

IX = (A-1)B

X = (A-1)B If the coefficient matrix does not have an inverse, does that mean the system has no solution? No, if the coefficient matrix is not invertible, the system could be inconsistent and have no solution, or be dependent and have infinitely many solutions.

**Example  7**

### Solving a 2 \times  2 System Using the Inverse of a Matrix
Solve the given system of equations using the inverse of a matrix.

3x + 8y = 5

4x + 11y = 7 Solution Write the system in terms of a coefficient matrix, a variable matrix, and a constant matrix. A =   3 8

4 11  , X =  x y  , B =  5 7   Then

  3 8

4 11    x y   =  5 7   First, we need to calculate A-1. Using the formula to calculate the inverse of a 2 by 2 matrix, we have:

A-1 =  _______ ad - bc   d -b

-c a  

=  ___________ 3(11) - 8(4)   11 -8

-4 3  

=  1 __ 1   11 -8

-4 3   So,

A-1 =   11 -8

-4 3   Now we are ready to solve. Multiply both sides of the equation by A-1.

(A-1)AX = (A-1)B

  11 -8

-4 3     3 8

4 11    x y   =   11 -8

-4 3    5 7  

 1 0

0 1    x y   =   11(5) + (-8)^{7}

-4(5) + 3(7)  

 x y   =  -1 1   The solution is (-1, 1).

Can we solve for X by finding the product BA-1? No, recall that matrix multiplication is not commutative, so A-1 B \neq  BA-1. Consider our steps for solving the matrix equation.

(A-1)AX = (A-1)B

[(A-1)A]X = (A-1)B

IX = (A-1)B

X = (A-1)B Notice in the first step we multiplied both sides of the equation by A-1, but the A-1 was to the left of A on the left side and to the left of B on the right side. Because matrix multiplication is not commutative, order matters.

**Example  8**

### Solving a 3 \times  3 System Using the Inverse of a Matrix
Solve the following system using the inverse of a matrix.

-4x - 11y - 41z = -26

-x - 3y - 11z = -7 Solution Write the equation AX = B.   5 15 56

-1 -3 -11      x

y z    =  

-26

-7    First, we will find the inverse of A by augmenting with the identity.     

-4 -11 -41

-1  -3  -11  ∣        0 1 0      Multiply row 1 by  1 __ 5 .      56 __ 5  

-4 -11 -41

-1  -3  -11  ∣      1 _ 5     0 1 0      Multiply row 1 by 4 and add to row 2.      56 __ 5   0 1  19 __ 5 

-1  -3  -11  ∣      1 _ 5      4 _ 5  1 0      Add row 1 to row 3.        56 __ 5   0 1  19 __ 5     1 _ 5   ∣    1 _ 5      4 _ 5  1 0  1 _ 5       Multiply row 2 by -3 and add to row 1.       - 1 __ 5   0 1  19 __ 5     1 _ 5   ∣   - 11 _ 5   -3    4 _ 5  1 0  1 _ 5       Multiply row 3 by 5.       - 1 __ 5   0 1  19 __ 5     ∣   - 11 _ 5   -3    4 _ 5  1 0     

Multiply row 3 by  1 __ 5  and add to row 1.        0 1  19 __ 5     ∣   -2  -3    4 _ 5  1 0      Multiply row 3 by - 19 ___ 5  and add to row 2.        0 1 0    ∣   -2  -3  

-3      So, A-1 =   -2 -3 1

-3 1 -19

1 0 5    Multiply both sides of the equation by A-1. We want A-1AX = A-1B:

  -2 -3 1

-3 1 -19

1 0 5      5 15 56

-1 -3 -11      x

y z    =   -2 -3 1

-3 1 -19

1 0 5     

-26

-7    Thus,

A-1B =  

   =  

   The solution is (1, 2, 0).

**Try It #4**
Solve the system using the inverse of the coefficient matrix.

2x - 17y + 11z = 0

-x + 11y - 7z = 8

3y - 2z = -2

**How To…**
Given a system of equations, solve with matrix inverses using a calculator. 1. Save the coefficient matrix and the constant matrix as matrix variables [A] and [B]. 2. Enter the multiplication into the calculator, calling up each matrix variable as needed. 3. If the coefficient matrix is invertible, the calculator will present the solution matrix; if the coefficient matrix is not invertible, the calculator will present an error message.

**Example  9**
Using a Calculator to Solve a System of Equations with Matrix Inverses Solve the system of equations with matrix inverses using a calculator

2x + 3y + z = 32

3x + 3y + z = -27

2x + 4y + z = -2 Solution On the matrix page of the calculator, enter the coefficient matrix as the matrix variable [A], and enter the constant matrix as the matrix variable [B]. [A] =  

  , [B] =  

-27

-2   

On the home screen of the calculator, type in the multiplication to solve for X, calling up each matrix variable as needed.

[A]-1 \times  [B] Evaluate the expression.

  -59

-34

   Access these online resources for additional instruction and practice with solving systems with inverses. • The Identity Matrix (http://openstaxcollege.org/l/identmatrix) • Determining Inverse Matrices (http://openstaxcollege.org/l/inversematrix) • Using a Matrix Equation to Solve a System of Equations (http://openstaxcollege.org/l/matrixsystem)


### 9.7 Section Exercises
Verbal 1. In a previous section, we showed that matrix multiplication is not commutative, that is, AB \neq  BA in most cases. Can you explain why matrix multiplication is commutative for matrix inverses, that is, A-1 A = AA-1 ? 2. Does every 2 \times  2 matrix have an inverse? Explain why or why not. Explain what condition is necessary for an inverse to exist. 3. Can you explain whether a 2 \times  2 matrix with an entire row of zeros can have an inverse? 4. Can a matrix with an entire column of zeros have an inverse? Explain why or why not. 5. Can a matrix with zeros on the diagonal have an inverse? If so, find an example. If not, prove why not. For simplicity, assume a 2 \times  2 matrix. Algebraic In the following exercises, show that matrix A is the inverse of matrix B. 6. A =   1 0

-1 1  , B =  1 0

1 1   7. A =  1 2

3 4  , B =  -2 1

 3 _ 2  - 1 _ 2    8. A =  4 5

7 0  , B =  0  1 _ 7 

 1 _ 5  - 4 __ 35    9. A =  -2  1 _ 2 

3 -1  , B =  -2 -1

-6 -4   10. A =  

  , B =  1 __ 2   2 1 -1

0 1 1

0 -1 1    11. A =  

  , B = 1 __ 4   6 0 -2

-12 2 4    12. A =  

  , B =  1 ___ 36   -6 84 -6

7 -26 1

-1 -22 5    For the following exercises, find the multiplicative inverse of each matrix, if it exists. 13.   3 -2

1 9  

3 1  

9 2   16.  -4 -3

-5 8  

2 2  

1 0  

1 -0.5   20.  

   21.  

   22.   1 2 -1

-3 4 1

-2 -4 -5    23.   1 9 -3

2 5 6

4 -2 7    24.   1 -2 3

-4 8 -12

1 4 2    25.    1 _ 2    1 _ 2    1 _ 2    1 _ 3   1 _ 4   1 _ 5   1 _ 6    1 _ 7    1 _ 8     26.  

  


## 9.7 Section Exercises
For the following exercises, solve the system using the inverse of a 2 \times  2 matrix. 4x + 3y = -2 3x - 4y = 1 29. 3x - 2y = 6 -x + 5y = -2 4x + y = 2.3 12x + 4y = -6 32. -2x + 3y =  3 ___ 10  - x + 5y = 1 __ 2  __ 5 x -  4 __ 5 y =  2 __ 5  - 8 __ 5 x +  1 __ 5 y =  7 ___ 10  __ 2 x +  1 __ 5  y = - 1 __ 4   1 __ 2 x -  3 __ 5 y = - 9 __ 4  For the following exercises, solve a system using the inverse of a 3 \times  3 matrix. 5x + 4y = 37 x - 2y - 5z = 5 36. 4x + 4y + 4z = 40 2x - 3y + 4z = -12 -x + 3y + 4z = 9 37. 6x - 5y - z = 31 -x + 2y + z = -6 3x + 3y + 2z = 13 38. 6x - 5y + 2z = -4 2x + 5y - z = 12 2x + 5y + z = 12 2x + 2y - 9z = 33 6y - 4z = 1 ___ 10 x -  1 __ 5 y + 4z = - 41 ___ 2   1 __ 5 x - 20y +  2 __  3 ___ 10 x + 4y -  3 ___ __ 2 x -  1 __ 5 y +  1 __ 5 z =  31 ___ 100  - 3 __ 4 x -  1 __ 4 y +  1 __ 2 z =  7 ___ 40  - 4 __ 5 x -  1 __ 2 y +  3 __ 2 z = 14 Technology For the following exercises, use a calculator to solve the system of equations with matrix inverses. 43. 2x - y = -3 -x + 2y = 2.3 __ 2 x -  3 __ 2 y = - 43 ___ 20   5 __ 2 x +  11 ___ 5 y =  31 ___ 4  8y - 5z = -10 0.5x + 4y + 5z = 0 Extensions For the following exercises, find the inverse of the given matrix. 47.   



   49.    1 -2 3 0

0 1 0 2

1 4 -2 3 

-5 0 1 1       





       







     -1    

0 0 0 2

0 2 -1 0

 -3     

Real-World Applications For the following exercises, write a system of equations that represents the situation. Then, solve the system using the inverse of a matrix. 52. 2,400 tickets were sold for a basketball game. If the prices for floor 1 and floor 2 were different, and the total amount of money brought in is $64,000, how much was the price of each ticket? 53. In the previous exercise, if you were told there were 400 more tickets sold for floor 2 than floor 1, how much was the price of each ticket? 54. A food drive collected two different types of canned goods, green beans and kidney beans. The total number of collected cans was 350 and the total weight of all donated food was 348 lb, 12 oz. If the green bean cans weigh 2 oz less than the kidney bean cans, how many of each can was donated? 55. Students were asked to bring their favorite fruit to class. 95% of the fruits consisted of banana, apple, and oranges. If oranges were twice as popular as bananas, and apples were 5% less popular than bananas, what are the percentages of each individual fruit? 56. A sorority held a bake sale to raise money and sold brownies and chocolate chip cookies. They priced the brownies at $1 and the chocolate chip cookies at $0.75. They raised $700 and sold 850 items. How many brownies and how many cookies were sold? 57. A clothing store needs to order new inventory. It has three different types of hats for sale: straw hats, beanies, and cowboy hats. The straw hat is priced at $13.99, the beanie at $7.99, and the cowboy hat at $14.49. If 100 hats were sold this past quarter, $1,119 was taken in by sales, and the amount of beanies sold was 10 more than cowboy hats, how many of each should the clothing store order to replace those already sold? 58. Anna, Ashley, and Andrea weigh a combined 370 lb. If Andrea weighs 20 lb more than Ashley, and Anna weighs 1.5 times as much as Ashley, how much does each girl weigh? 59. Three roommates shared a package of 12 ice cream bars, but no one remembers who ate how many. If Tom ate twice as many ice cream bars as Joe, and Albert ate three less than Tom, how many ice cream bars did each roommate eat? 60. A farmer constructed a chicken coop out of chicken wire, wood, and plywood. The chicken wire cost $2 per square foot, the wood $10 per square foot, and the plywood $5 per square foot. The farmer spent a total of $51, and the total amount of materials used was 14 ft^{2}. He used 3 ft^{2} more chicken wire than plywood. How much of each material in did the farmer use? 61. Jay has lemon, orange, and pomegranate trees in his backyard. An orange weighs 8 oz, a lemon 5 oz, and a pomegranate 11 oz. Jay picked 142 pieces of fruit weighing a total of 70 lb, 10 oz. He picked 15.5 times more oranges than pomegranates. How many of each fruit did Jay pick?


## 9.8 Solving Systems with Cramer's Rule
We have learned how to solve systems of equations in two variables and three variables, and by multiple methods: substitution, addition, Gaussian elimination, using the inverse of a matrix, and graphing. Some of these methods are easier to apply than others and are more appropriate in certain situations. In this section, we will study two more strategies for solving systems of equations. Evaluating the Determinant of a 2 \times  2 Matrix A determinant is a real number that can be very useful in mathematics because it has multiple applications, such as calculating area, volume, and other quantities. Here, we will use determinants to reveal whether a matrix is invertible by using the entries of a square matrix to determine whether there is a solution to the system of equations. Perhaps one of the more interesting applications, however, is their use in cryptography. Secure signals or messages are sometimes sent encoded in a matrix. The data can only be decrypted with an invertible matrix and the determinant. For our purposes, we focus on the determinant as an indication of the invertibility of the matrix. Calculating the determinant of a matrix involves following the specific patterns that are outlined in this section. find the determinant of a 2 \times  2 matrix The determinant of a 2 \times  2 matrix, given

A =  a b

c d   is defined as

det(A) = ∣ a b

c d ∣ = ad - cb Notice the change in notation. There are several ways to indicate the determinant, including det(A) and replacing the brackets in a matrix with straight lines, ∣ A ∣.

**Example  1**
Finding the Determinant of a 2 \times  2 Matrix Find the determinant of the given matrix. A =   5 2

-6 3  

**Solution**
det(A) = ∣  5 2

-6 3 ∣

= 5(3) - (-6)(2)

= 27 Using Cramer’s Rule to Solve a System of Two Equations in Two Variables We will now introduce a final method for solving systems of equations that uses determinants. Known as Cramer’s Rule, this technique dates back to the middle of the 18th century and is named for its innovator, the Swiss mathematician Gabriel Cramer (1704-1752), who introduced it in 1750 in Introduction à l'Analyse des lignes Courbes algébriques. Cramer’s Rule is a viable and efficient method for finding solutions to systems with an arbitrary number of unknowns, provided that we have the same number of equations as unknowns. Learning Objectives
In this section, you will:
• Evaluate 2 \times  2 determinants.
• Use Cramer’s Rule to solve a system of equations in two variables.
• Evaluate 3 \times  3 determinants.
• Use Cramer’s Rule to solve a system of three equations in three variables.
• Know the properties of determinants.
Cramer’s Rule will give us the unique solution to a system of equations, if it exists. However, if the system has no solution or an infinite number of solutions, this will be indicated by a determinant of zero. To find out if the system is inconsistent or dependent, another method, such as elimination, will have to be used. To understand Cramer’s Rule, let’s look closely at how we solve systems of linear equations using basic row operations. Consider a system of two equations in two variables.

a^{1}x + b^{1} y = c^{1} (1)

a^{2}x + b^{2} y = c^{2} (2) We eliminate one variable using row operations and solve for the other. Say that we wish to solve for x. If equation (2) is multiplied by the opposite of the coefficient of y in equation (1), equation (1) is multiplied by the coefficient of y in equation (2), and we add the two equations, the variable y will be eliminated.

b^{2} a^{1}x + b^{2} b^{1} y = b^{2}c^{1} Multiply R^{1} by b^{2}

-b^{1} a^{2}x - b^{1}b^{2} y = -b^{1}c^{2} Multiply R^{2} by -b^{1}

b^{2} a^{1}x - b^{1} a^{2}x = b^{2}c^{1} - b^{1}c^{2} Now, solve for x.

b^{2} a^{1}x - b^{1} a^{2}x = b^{2}c^{1} - b^{1}c^{2}

x(b^{2} a^{1} - b^{1} a^{2}) = b^{2}c^{1} - b^{1}c^{2}

x =  b^{2}c^{1} - b^{1}c^{2} _ b^{2}a^{1} - b^{1}a^{2}  =   c^{1} b^{1}

c^{2} b^{2}   _  a^{1} b^{1}

a^{2} b^{2}     Similarly, to solve for y, we will eliminate x.

a^{2}a^{1}x + a^{2}b^{1} y = a^{2}c^{1} Multiply R^{1} by a^{2}

-a^{1}a^{2}x -a^{1}b^{2}y = -a^{1}c^{2} Multiply R^{2} by -a^{1}

a^{2}b^{1} y - a^{1}b^{2} y = a^{2}c^{1} - a^{1}c^{2} Solving for y gives

a^{2}b^{1} y - a^{1}b^{2} y = a^{2}c^{1} - a^{1}c^{2}

y(a^{2}b^{1} - a^{1}b^{2}) = a^{2}c^{1} - a^{1}c^{2}

y =  a^{2}c^{1} - a^{1}c^{2} _ a^{2}b^{1} - a^{1}b^{2}  =  a^{1}c^{2} - a^{2}c^{1} _ a^{1}b^{2} - a^{2}b^{1}  =   a^{1} c^{1}

a^{2} c^{2}   _  a^{1} b^{1}

a^{2} b^{2}    Notice that the denominator for both x and y is the determinant of the coefficient matrix. We can use these formulas to solve for x and y, but Cramer’s Rule also introduces new notation: • D : determinant of the coefficient matrix • Dx : determinant of the numerator in the solution of x

x =  Dx _ D  • Dy : determinant of the numerator in the solution of y

y =  Dy

_ D  The key to Cramer’s Rule is replacing the variable column of interest with the constant column and calculating the determinants. We can then express x and y as a quotient of two determinants.

Cramer’s Rule for 2 \times  2 systems Cramer’s Rule is a method that uses determinants to solve systems of equations that have the same number of equations as variables. Consider a system of two linear equations in two variables.

a^{1}x + b^{1} y = c^{1}

a^{2}x + b^{2} y = c^{2} The solution using Cramer’s Rule is given as x =  Dx _ D  =   c^{1} b^{1}

c^{2} b^{2}   _  a^{1} b^{1}

a^{2} b^{2}   , D \neq  0; y =  Dy

_ D  =   a^{1} c^{1}

a^{2} c^{2}   _  a^{1} b^{1}

a^{2} b^{2}   , D \neq  0. If we are solving for x, the x column is replaced with the constant column. If we are solving for y, the y column is replaced with the constant column.

**Example  2**
Using Cramer’s Rule to Solve a 2 \times  2 System Solve the following 2 \times  2 system using Cramer’s Rule.

2x - 3y = 13 Solution Solve for x. x =  Dx _ D  =  ∣ 15 3

13 -3 ∣ _ ∣ 12 3

2 -3 ∣  =  -45 - 39 ________ -36 - 6  =  -84 ____ -42  = 2 Solve for y.

y =  Dy

_ D  = 

2 13 ∣ _ ∣ 12 3

2 -3 ∣ ________ -36 - 6  = - 126 ___ 42  = -3 The solution is (2, -3).

**Try It #1**
Use Cramer’s Rule to solve the 2 \times  2 system of equations.

x + 2y = -11

-2x + y = -13 Evaluating the Determinant of a 3 \times  3 Matrix Finding the determinant of a 2 \times  2 matrix is straightforward, but finding the determinant of a 3 \times  3 matrix is more complicated. One method is to augment the 3 \times  3 matrix with a repetition of the first two columns, giving a 3 \times  5 matrix. Then we calculate the sum of the products of entries down each of the three diagonals (upper left to lower right), and subtract the products of entries up each of the three diagonals (lower left to upper right). This is more easily understood with a visual and an example. Find the determinant of the 3 \times  3 matrix.

A =   a^{1} b^{1} c^{1}

a^{2} b^{2} c^{2}

a^{3} b^{3} c^{3}   

1. Augment A with the first two columns.

det(A) = ∣  a^{1} b^{1} c^{1}

a^{2} b^{2} c^{2}

a^{3} b^{3} c^{3}  ∣     a^{1} b^{1}

a^{2} b^{2}

a^{3} b^{3}  ∣  2. From upper left to lower right: Multiply the entries down the first diagonal. Add the result to the product of entries down the second diagonal. Add this result to the product of the entries down the third diagonal. 3. From lower left to upper right: Subtract the product of entries up the first diagonal. From this result subtract the product of entries up the second diagonal. From this result, subtract the product of entries up the third diagonal.

det(A) = ∣  a^{1} b^{1} c^{1}

a^{2} b^{2} c^{2}

a^{3} b^{3} c^{3}  ∣     a^{1} b^{1}

a^{2} b^{2}

a^{3} b^{3}  ∣  The algebra is as follows:

∣ A ∣ = a^{1} b^{2} c^{3} + b^{1} c^{2} a^{3} + c^{1} a^{2} b^{3} - a^{3} b^{2} c^{1} - b^{3} c^{2} a^{1} - c^{3} a^{2} b^{1}

**Example  3**
Finding the Determinant of a 3 \times  3 Matrix Find the determinant of the 3 \times  3 matrix given

A =  

   Solution Augment the matrix with the first two columns and then follow the formula. Thus,

∣ A ∣ = ∣ 

 ∣    

3 -1

 ∣  = 0(-1)(1) + 2(1)(4) + 1(3)(0) - 4(-1)(1) - 0(1)(0) - 1(3)(2)

= 0 + 8 + 0 + 4 - 0 - 6

= 6

**Try It #2**
Find the determinant of the 3 \times  3 matrix. det(A) = ∣ 

 ∣  Can we use the same method to find the determinant of a larger matrix? No, this method only works for 2 \times  2 and 3 \times  3 matrices. For larger matrices it is best to use a graphing utility or computer software. Using Cramer’s Rule to Solve a System of Three Equations in Three Variables Now that we can find the determinant of a 3 \times  3 matrix, we can apply Cramer’s Rule to solve a system of three equations in three variables. Cramer’s Rule is straightforward, following a pattern consistent with Cramer’s Rule for 2 \times  2 matrices. As the order of the matrix increases to 3 \times  3, however, there are many more calculations required. When we calculate the determinant to be zero, Cramer’s Rule gives no indication as to whether the system has no solution or an infinite number of solutions. To find out, we have to perform elimination on the system.

Consider a 3 \times  3 system of equations.

a^{1}x + b^{1} y + c^{1}z = d^{1}

a^{2}x + b^{2} y + c^{2}z = d^{2}

a^{3}x + b^{3} y + c^{3}z = d^{3} x =  Dx _ D , y =  Dy

_ D , z =  Dz

_ D , D \neq  0 where D = ∣  a^{1} b^{1} c^{1}

a^{2} b^{2} c^{2}

a^{3} b^{3} c^{3}  ∣ , Dx = ∣  d^{1} b^{1} c^{1}

d^{2} b^{2} c^{2}

d^{3} b^{3} c^{3}  ∣ , Dy = ∣  a^{1} d^{1} c^{1}

a^{2} d^{2} c^{2}

a^{3} d^{3} c^{3}  ∣ , Dz = ∣  a^{1} b^{1} d^{1}

a^{2} b^{2} d^{2}

a^{3} b^{3} d^{3}  ∣  If we are writing the determinant Dx, we replace the x column with the constant column. If we are writing the determinant Dy, we replace the y column with the constant column. If we are writing the determinant Dz, we replace the z column with the constant column. Always check the answer.

**Example  4**

### Solving a 3 \times  3 System Using Cramer’s Rule
Find the solution to the given 3 \times  3 system using Cramer’s Rule.

x + y - z = 6

3x - 2y + z = -5

x + 3y - 2z = 14 Solution Use Cramer’s Rule. D = ∣  1 1 -1

3 -2 1

1 3 -2  ∣ , Dx = ∣  6 1 -1

-5 -2 1

14 3 -2  ∣ , Dy = ∣  1 6 -1

3 -5 1

 ∣ , Dz = ∣  1 1 6

3 -2 -5

 ∣  Then, x =  Dx _ D  =  -3 ___ -3  = 1

y =  Dy

_ D  =  -9 ___ -3  = 3

z =  Dz

_ D  =  6 ___ -3  = - 2 The solution is (1, 3, -2).

**Try It #3**
Use Cramer’s Rule to solve the 3 \times  3 matrix.

x - 3y + 7z = 13

x + y + z = 1

x - 2y + 3z = 4

**Example  5**
Using Cramer’s Rule to Solve an Inconsistent System Solve the system of equations using Cramer’s Rule.

3x - 2y = 4 (1)

6x - 4y = 0 (2) Solution We begin by finding the determinants D, Dx, and Dy.

D = ∣ 3 -2

6 -4 ∣ = 3(-4) - 6(-2) = 0

We know that a determinant of zero means that either the system has no solution or it has an infinite number of solutions. To see which one, we use the process of elimination. Our goal is to eliminate one of the variables. 1. Multiply equation (1) by -2. 2. Add the result to equation (2).

-6x + 4y = -8

6x - 4y = 0

0 = -8 We obtain the equation 0 = -8, which is false. Therefore, the system has no solution. Graphing the system reveals two parallel lines. See Figure 1. x y y = 3 2 x - 2 y = 3 2 x

**Example  6**
Use Cramer’s Rule to Solve a Dependent System Solve the system with an infinite number of solutions.

x - 2y + 3z = 0

(1)

3x + y - 2z = 0

(2)

2x - 4y + 6z = 0

(3) Solution Let’s find the determinant first. Set up a matrix augmented by the first two columns. ∣  1 -2 3

3 1 -2

2 -4 6  ∣     1 -2

2 -4  ∣  Then, 1(1)(6) + (-2)(-2)(2) + 3(3)(-4) - 2(1)(3) - (-4)(-2)(1) - 6(3)(-2) = 0 As the determinant equals zero, there is either no solution or an infinite number of solutions. We have to perform elimination to find out. 1. Multiply equation (1) by -2 and add the result to equation (3):

-2x + 4y - 6x = 0

2x - 4y + 6z = 0

0 = 0 2. Obtaining an answer of 0 = 0, a statement that is always true, means that the system has an infinite number of solutions. Graphing the system, we can see that two of the planes are the same and they both intersect the third plane on a line. See Figure 2.

x - 2y + 3z = 0 2x - 4y + 6z = 0 3x + y + 2z = 0 Understanding Properties of Determinants There are many properties of determinants. Listed here are some properties that may be helpful in calculating the determinant of a matrix. properties of determinants 1. If the matrix is in upper triangular form, the determinant equals the product of entries down the main diagonal. 2. When two rows are interchanged, the determinant changes sign. 3. If either two rows or two columns are identical, the determinant equals zero. 4. If a matrix contains either a row of zeros or a column of zeros, the determinant equals zero. 5. The determinant of an inverse matrix A-1 is the reciprocal of the determinant of the matrix A. 6. If any row or column is multiplied by a constant, the determinant is multiplied by the same factor.

**Example  7**
Illustrating Properties of Determinants Illustrate each of the properties of determinants. Solution Property 1 states that if the matrix is in upper triangular form, the determinant is the product of the entries down the main diagonal.

A =  

   Augment A with the first two columns.

A =  

 ∣    

   Then det(A) = 1(2)(-1) + 2(1)(0) + 3(0)(0) - 0(2)(3) - 0(1)(1) + 1(0)(2)

= -2 Property 2 states that interchanging rows changes the sign. Given

A =  -1 5

4 -3  , det(A) = (-1)(-3) - (4)(5) = 3 - 20 = -17

B =   4 -3

-1 5  , det(B) = (4)(5) - (-1)(-3) = 20 - 3 = 17

Property 3 states that if two rows or two columns are identical, the determinant equals zero.

A = ∣ 

 ∣    

-1 2   

det(A) = 1(2)(2) + 2(2)(-1) + 2(2)(2) + 1(2)(2) - 2(2)(1) - 2(2)(2)

= 4 - 4 + 8 + 4 - 4 - 8 = 0 Property 4 states that if a row or column equals zero, the determinant equals zero. Thus,

A =  1 2

0 0  , det(A) = 1(0) - 2(0) = 0 Property 5 states that the determinant of an inverse matrix A-1 is the reciprocal of the determinant A. Thus,

A =  1 2

3 4  , det(A) = 1(4) - 3(2) = -2

A-1 =   -2    3 _ 2  - 1 _ 2   , det(A-1) = -2 - 1 __ 2    -   3 __ 2   (1) = - 1 __ 2  Property 6 states that if any row or column of a matrix is multiplied by a constant, the determinant is multiplied by the same factor. Thus,

A =  1 2

3 4  , det(A) = 1(4) - 2(3) = -2

B =  2(1) 2(2) 3 4  , det(B) = 2(4) - 3(4) = -4

**Example  8**
Using Cramer’s Rule and Determinant Properties to Solve a System Find the solution to the given 3 \times  3 system.

2x + 4y + 4z = 2 (1)

3x + 7y + 7z = -5 (2)

x + 2y + 2z = 4 (3) Solution Using Cramer’s Rule, we have D = ∣ 

 ∣  Notice that the second and third columns are identical. According to Property 3, the determinant will be zero, so there is either no solution or an infinite number of solutions. We have to perform elimination to find out. 1. Multiply equation (3) by -2 and add the result to equation (1).

-2x - 4y - 4x = -8

2x + 4y + 4z = 2

0 = -6 Obtaining a statement that is a contradiction means that the system has no solution. Access these online resources for additional instruction and practice with Cramer’s Rule. • Solve a System of Two Equations Using Cramer's Rule (http://openstaxcollege.org/l/system^{2}cramer) • Solve a Systems of Three Equations using Cramer's Rule (http://openstaxcollege.org/l/system^{3}cramer)


## 9.8 Section Exercises

### 9.8 Section Exercises
Verbal 1. Explain why we can always evaluate the determinant of a square matrix. 2. Examining Cramer’s Rule, explain why there is no unique solution to the system when the determinant of your matrix is 0. For simplicity, use a 2 \times  2 matrix. 3. Explain what it means in terms of an inverse for a matrix to have a 0 determinant. 4. The determinant of 2 \times  2 matrix A is 3. If you switch the rows and multiply the first row by 6 and the second row by 2, explain how to find the determinant and provide the answer. Algebraic For the following exercises, find the determinant.

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

-9.3    ∣  24.  ∣  - 1 _ 2    1 _ 3    1 _ 4    1 _ 5  - 1 _ 6   1 _ 7     1 _ 8   ∣  For the following exercises, solve the system of linear equations using Cramer’s Rule. 4x + 5y = 9 26. 5x - 4y = 2 -4x + 7y = 6 27. 6x - 3y = 2 -8x + 9y = -1 5x - 2y = 13 2x - y = -1 -5x + 8y = -1 2x + 6y = -4 32. 4x - 5y = 7 -3x + 9y = 0 -3x - 5y = -105 34. 8x - 2y = -3 -4x + 6y = 4 For the following exercises, solve the system of linear equations using Cramer’s Rule. 35. x + 2y - 4z = - 1 7x + 3y + 5z = 26 -2x - 6y + 7z = - 6 36. -5x + 2y - 4z = - 47 4x - 3y - z = - 94 3x - 3y + 2z = 94 37. 4x + 5y - z = -7 -2x - 9y + 2z = 8 5y + 7z = 21 5x - 2z = - 2 3x + 2y - 5z = - 9 39. 4x - 2y + 3z = 6 - 6x + y = - 2 2x + 7y + 8z = 24 40. 5x + 2y - z = 1 -7x - 8y + 3z = 1.5 6x - 12y + z = 7 42. -4x - 3y - 8z = - 7 2x - 9y + 5z = 0.5 5x - 6y - 5z = - 2

43. 4x - 6y + 8z = 10 -2x + 3y - 4z = - 5 x + y + z = 1 44. 4x - 6y + 8z = 10 -2x + 3y - 4z = - 5 Technology For the following exercises, use the determinant function on a graphing utility.  



 ∣  ∣    1 _ 2  1 7 4

0  1 _ 2  100 5



0 0 0 2  ∣   



 ∣  Real-World Applications For the following exercises, create a system of linear equations to describe the behavior. Then, calculate the determinant. Will there be a unique solution? If so, find the unique solution. 49. Two numbers add up to 56. One number is 20 less than the other. 50. Two numbers add up to 104. If you add two times the first number plus two times the second number, your total is 208 51. Three numbers add up to 106. The first number is 3 less than the second number. The third number is 4 more than the first number. 52. Three numbers add to 216. The sum of the first two numbers is 112. The third number is 8 less than the first two numbers combined. For the following exercises, create a system of linear equations to describe the behavior. Then, solve the system for all solutions using Cramer’s Rule. 53. You invest $10,000 into two accounts, which receive 8% interest and 5% interest. At the end of a year, you had $10,710 in your combined accounts. How much was invested in each account? 54. You invest $80,000 into two accounts, $22,000 in one account, and $58,000 in the other account. At the end of one year, assuming simple interest, you have earned $2,470 in interest. The second account receives half a percent less than twice the interest on the first account. What are the interest rates for your accounts? 55. A movie theater needs to know how many adult tickets and children tickets were sold out of the 1,200 total tickets. If children’s tickets are $5.95, adult tickets are $11.15, and the total amount of revenue was $12,756, how many children’s tickets and adult tickets were sold? 56. A concert venue sells single tickets for $40 each and couple’s tickets for $65. If the total revenue was $18,090 and the 321 tickets were sold, how many single tickets and how many couple’s tickets were sold? 57. You decide to paint your kitchen green. You create the color of paint by mixing yellow and blue paints. You cannot remember how many gallons of each color went into your mix, but you know there were 10 gal total. Additionally, you kept your receipt, and know the total amount spent was $29.50. If each gallon of yellow costs $2.59, and each gallon of blue costs $3.19, how many gallons of each color go into your green mix? 58. You sold two types of scarves at a farmers’ market and would like to know which one was more popular. The total number of scarves sold was 56, the yellow scarf cost $10, and the purple scarf cost $11. If you had total revenue of $583, how many yellow scarves and how many purple scarves were sold? ∣     

0 -9 1 3 

3 0 -2 -1

   -2  ∣ 

59. Your garden produced two types of tomatoes, one green and one red. The red weigh 10 oz, and the green weigh 4 oz. You have 30 tomatoes, and a total weight of 13 lb, 14 oz. How many of each type of tomato do you have? 60. At a market, the three most popular vegetables make up 53% of vegetable sales. Corn has 4% higher sales than broccoli, which has 5% more sales than onions. What percentage does each vegetable have in the market share? 61. At the same market, the three most popular fruits make up 37% of the total fruit sold. Strawberries sell twice as much as oranges, and kiwis sell one more percentage point than oranges. For each fruit, find the percentage of total fruit sold. 62. Three bands performed at a concert venue. The first band charged $15 per ticket, the second band charged $45 per ticket, and the final band charged $22 per ticket. There were 510 tickets sold, for a total of $12,700. If the first band had 40 more audience members than the second band, how many tickets were sold for each band? 63. A movie theatre sold tickets to three movies. The tickets to the first movie were $5, the tickets to the second movie were $11, and the third movie was $12. 100 tickets were sold to the first movie. The total number of tickets sold was 642, for a total revenue of $6,774. How many tickets for each movie were sold? of the population at a prison last year. This year, the same age groups made up 82.08% of the population. The 20–29 age group increased by 20%, the 30–39 age group increased by 2%, and the 40–49 age group decreased to  3 __ 4  of their previous population. Originally, the 30–39 age group had 2% more prisoners than the 20–29 age group. Determine the prison population percentage for each age group last year. 65. At a women’s prison down the road, the total number of inmates aged 20–49 totaled 5,525. This year, the 20–29 age group increased by 10%, the 30–39 age group decreased by 20%, and the 40–49 age group doubled. There are now 6,040 prisoners. Originally, there were 500 more in the 30–39 age group than the 20–29 age group. Determine the prison population for each age group last year. For the following exercises, use this scenario: A health-conscious company decides to make a trail mix out of almonds, dried cranberries, and chocolate-covered cashews. The nutritional information for these items is shown in Table 1. Fat (g) Protein (g) Carbohydrates (g) Almonds (10) Cranberries (10) 0.02 Cashews (10) 3.5 5.5 66. For the special “low-carb” trail mix, there are 1,000 pieces of mix. The total number of carbohydrates is 425 g, and the total amount of fat is 570.2 g. If there are 200 more pieces of cashews than cranberries, how many of each item is in the trail mix? 67. For the “hiking” mix, there are 1,000 pieces in the mix, containing 390.8 g of fat, and 165 g of protein. If there is the same amount of almonds as cashews, how many of each item is in the trail mix? 68. For the “energy-booster” mix, there are 1,000 pieces in the mix, containing 145 g of protein and 625 g of carbohydrates. If the number of almonds and cashews summed together is equivalent to the amount of cranberries, how many of each item is in the trail mix?


### Key Terms
addition method an algebraic technique used to solve systems of linear equations in which the equations are added in a way that eliminates one variable, allowing the resulting equation to be solved for the remaining variable; substitution is then used to solve for the first variable augmented matrix a coefficient matrix adjoined with the constant column separated by a vertical line within the matrix brackets break-even point the point at which a cost function intersects a revenue function; where profit is zero coefficient matrix a matrix that contains only the coefficients from a system of equations column a set of numbers aligned vertically in a matrix consistent system a system for which there is a single solution to all equations in the system and it is an independent system, or if there are an infinite number of solutions and it is a dependent system cost function the function used to calculate the costs of doing business; it usually has two parts, fixed costs and variable costs Cramer’s Rule a method for solving systems of equations that have the same number of equations as variables using determinants dependent system a system of linear equations in which the two equations represent the same line; there are an infinite number of solutions to a dependent system determinant a number calculated using the entries of a square matrix that determines such information as whether there is a solution to a system of equations entry an element, coefficient, or constant in a matrix feasible region the solution to a system of nonlinear inequalities that is the region of the graph where the shaded regions of each inequality intersect Gaussian elimination using elementary row operations to obtain a matrix in row-echelon form identity matrix a square matrix containing ones down the main diagonal and zeros everywhere else; it acts as a 1 in matrix algebra inconsistent system a system of linear equations with no common solution because they represent parallel lines, which have no point or line in common independent system a system of linear equations with exactly one solution pair (x, y) main diagonal entries from the upper left corner diagonally to the lower right corner of a square matrix matrix a rectangular array of numbers multiplicative inverse of a matrix a matrix that, when multiplied by the original, equals the identity matrix nonlinear inequality an inequality containing a nonlinear expression partial fraction decomposition the process of returning a simplified rational expression to its original form, a sum or difference of simpler rational expressions partial fractions the individual fractions that make up the sum or difference of a rational expression before combining them into a simplified rational expression profit function the profit function is written as P(x) = R(x) - C(x), revenue minus cost revenue function the function that is used to calculate revenue, simply written as R = xp, where x = quantity and p = price row a set of numbers aligned horizontally in a matrix row operations adding one row to another row, multiplying a row by a constant, interchanging rows, and so on, with the goal of achieving row-echelon form row-echelon form after performing row operations, the matrix form that contains ones down the main diagonal and zeros at every space below the diagonal row-equivalent two matrices A and B are row-equivalent if one can be obtained from the other by performing basic row operations scalar multiple an entry of a matrix that has been multiplied by a scalar solution set the set of all ordered pairs or triples that satisfy all equations in a system of equations substitution method an algebraic technique used to solve systems of linear equations in which one of the two equations is solved for one variable and then substituted into the second equation to solve for the second variable

system of linear equations a set of two or more equations in two or more variables that must be considered simultaneously. system of nonlinear equations a system of equations containing at least one equation that is of degree larger than one system of nonlinear inequalities a system of two or more inequalities in two or more variables containing at least one inequality that is not linear Key Equations Identity matrix for a 2 \times  2 matrix I^{2} =  1 0

0 1   Identity matrix for a 3 \times  3 matrix I^{3} =  

   Multiplicative inverse of a 2 \times  2 matrix A-1 =  _______ ad - bc    d -b

-c a  , where ad - bc \neq  0

### Key Concepts
• A system of linear equations consists of two or more equations made up of two or more variables such that all equations in the system are considered simultaneously. • The solution to a system of linear equations in two variables is any ordered pair that satisfies each equation independently. See Example 1. • Systems of equations are classified as independent with one solution, dependent with an infinite number of solutions, or inconsistent with no solution. • One method of solving a system of linear equations in two variables is by graphing. In this method, we graph the equations on the same set of axes. See Example 2. • Another method of solving a system of linear equations is by substitution. In this method, we solve for one variable in one equation and substitute the result into the second equation. See Example 3. • A third method of solving a system of linear equations is by addition, in which we can eliminate a variable by adding opposite coefficients of corresponding variables. See Example 4. • It is often necessary to multiply one or both equations by a constant to facilitate elimination of a variable when adding the two equations together. See Example 5, Example 6, and Example 7. • Either method of solving a system of equations results in a false statement for inconsistent systems because they are made up of parallel lines that never intersect. See Example 8. • The solution to a system of dependent equations will always be true because both equations describe the same line. See Example 9. • Systems of equations can be used to solve real-world problems that involve more than one variable, such as those relating to revenue, cost, and profit. See Example 10 and Example 11. 9.2 Systems of Linear Equations: Three Variables • A solution set is an ordered triple {(x, y, z)} that represents the intersection of three planes in space. See Example 1. • A system of three equations in three variables can be solved by using a series of steps that forces a variable to be eliminated. The steps include interchanging the order of equations, multiplying both sides of an equation by a nonzero constant, and adding a nonzero multiple of one equation to another equation. See Example 2. • Systems of three equations in three variables are useful for solving many different types of real-world problems. See

**Example 3** — .
• A system of equations in three variables is inconsistent if no solution exists. After performing elimination operations, the result is a contradiction. See Example 4. • Systems of equations in three variables that are inconsistent could result from three parallel planes, two parallel planes and one intersecting plane, or three planes that intersect the other two but not at the same location.

• A system of equations in three variables is dependent if it has an infinite number of solutions. After performing elimination operations, the result is an identity. See Example 5. • Systems of equations in three variables that are dependent could result from three identical planes, three planes intersecting at a line, or two identical planes that intersect the third on a line. 9.3 Systems of Nonlinear Equations and Inequalities: Two Variables • There are three possible types of solutions to a system of equations representing a line and a parabola: (1) no solution, the line does not intersect the parabola; (2) one solution, the line is tangent to the parabola; and (3) two solutions, the line intersects the parabola in two points. See Example 1. • There are three possible types of solutions to a system of equations representing a circle and a line: (1) no solution, the line does not intersect the circle; (2) one solution, the line is tangent to the parabola; (3) two solutions, the line intersects the circle in two points. See Example 2. • There are five possible types of solutions to the system of nonlinear equations representing an ellipse and a circle: (1) no solution, the circle and the ellipse do not intersect; (2) one solution, the circle and the ellipse are tangent to each other; (3) two solutions, the circle and the ellipse intersect in two points; (4) three solutions, the circle and ellipse intersect in three places; (5) four solutions, the circle and the ellipse intersect in four points. See Example 3. • An inequality is graphed in much the same way as an equation, except for > or <, we draw a dashed line and shade the region containing the solution set. See Example 4. • Inequalities are solved the same way as equalities, but solutions to systems of inequalities must satisfy both inequalities. See Example 5. 9.4 Partial Fractions • Decompose  P(x) ____ Q(x)  by writing the partial fractions as  A ________ a^{1} x + b^{1}  +  B ________ a^{2} x + b^{2} . Solve by clearing the fractions, expanding the right side, collecting like terms, and setting corresponding coefficients equal to each other, then setting up and solving a system of equations. See Example 1. • The decomposition of  P(x) ____ Q(x)  with repeated linear factors must account for the factors of the denominator in increasing powers. See Example 2. • The decomposition of  P(x) ____ Q(x)  with a nonrepeated irreducible quadratic factor needs a linear numerator over the quadratic factor, as in  A __ x  +  Bx + C ____________

(ax^{2} + bx + c) . See Example 3. • In the decomposition of  P(x) ____ Q(x)  , where Q(x) has a repeated irreducible quadratic factor, when the irreducible quadratic factors are repeated, powers of the denominator factors must be represented in increasing powers as  Ax + B __

(ax^{2} + bx + c)  +  A^{2} x + B^{2} __

(ax^{2} + bx + c)^{2}  + ... +  An x + Bn __

(ax^{2} + bx + c) n . See Example 4. 9.5 Matrices and Matrix Operations • A matrix is a rectangular array of numbers. Entries are arranged in rows and columns. • The dimensions of a matrix refer to the number of rows and the number of columns. A 3 \times  2 matrix has three rows and two columns. See Example 1. • We add and subtract matrices of equal dimensions by adding and subtracting corresponding entries of each matrix. See Example 2, Example 3, Example 4, and Example 5. • Scalar multiplication involves multiplying each entry in a matrix by a constant. See Example 6. • Scalar multiplication is often required before addition or subtraction can occur. See Example 7. • Multiplying matrices is possible when inner dimensions are the same—the number of columns in the first matrix must match the number of rows in the second. • The product of two matrices, A and B, is obtained by multiplying each entry in row 1 of A by each entry in column 1 of B; then multiply each entry of row 1 of A by each entry in columns 2 of B, and so on. See Example 8 and Example 9.

• Many real-world problems can often be solved using matrices. See Example 10. • We can use a calculator to perform matrix operations after saving each matrix as a matrix variable. See Example 11. 9.6 Solving Systems with Gaussian Elimination • An augmented matrix is one that contains the coefficients and constants of a system of equations. See Example 1. • A matrix augmented with the constant column can be represented as the original system of equations. See Example 2. • Row operations include multiplying a row by a constant, adding one row to another row, and interchanging rows. • We can use Gaussian elimination to solve a system of equations. See Example 3, Example 4, and Example 5. • Row operations are performed on matrices to obtain row-echelon form. See Example 6. • To solve a system of equations, write it in augmented matrix form. Perform row operations to obtain row-echelon form. Back-substitute to find the solutions. See Example 7 and Example 8. • A calculator can be used to solve systems of equations using matrices. See Example 9. • Many real-world problems can be solved using augmented matrices. See Example 10 and Example 11. 9.7 Solving Systems with Inverses • An identity matrix has the property AI = IA = A. See Example 1. • An invertible matrix has the property AA-1 = A-1 A = I. See Example 2. • Use matrix multiplication and the identity to find the inverse of a 2 \times  2 matrix. See Example 3. • The multiplicative inverse can be found using a formula. See Example 4. • Another method of finding the inverse is by augmenting with the identity. See Example 5. • We can augment a 3 \times  3 matrix with the identity on the right and use row operations to turn the original matrix into the identity, and the matrix on the right becomes the inverse. See Example 6. • Write the system of equations as AX = B, and multiply both sides by the inverse of A: A-1 AX = A-1 B. See Example 7 and Example 8. • We can also use a calculator to solve a system of equations with matrix inverses. See Example 9. 9.8 Solving Systems with Cramer's Rule • The determinant for  a b

c d   is ad - bc. See Example 1. • Cramer’s Rule replaces a variable column with the constant column. Solutions are x =  Dx _ D , y =  Dy

_ D . See Example 2. • To find the determinant of a 3 \times  3 matrix, augment with the first two columns. Add the three diagonal entries (upper left to lower right) and subtract the three diagonal entries (lower left to upper right). See Example 3. • To solve a system of three equations in three variables using Cramer’s Rule, replace a variable column with the constant column for each desired solution: x =  Dx _ D , y =  Dy

_ D , z =  Dz

_ D . See Example 4. • Cramer’s Rule is also useful for finding the solution of a system of equations with no solution or infinite solutions. See

**Example 5** — and Example 6.
• Certain properties of determinants are useful for solving problems. For example:

○ If the matrix is in upper triangular form, the determinant equals the product of entries down the main diagonal.

○ When two rows are interchanged, the determinant changes sign.

○ If either two rows or two columns are identical, the determinant equals zero.

○ If a matrix contains either a row of zeros or a column of zeros, the determinant equals zero.

○ The determinant of an inverse matrix A-1 is the reciprocal of the determinant of the matrix A.

○ If any row or column is multiplied by a constant, the determinant is multiplied by the same factor. See

**Example 7** — and Example 8.

Systems of Linear Equations: Two Variables For the following exercises, determine whether the ordered pair is a solution to the system of equations. 1. 3x - y = 4 x + 4y = - 3 and ( - 1, 1) -3x + 3y = 18 and (9, 15) For the following exercises, use substitution to solve the system of equations. 3x - 2y = -12 __ 7 x +  1 __ 5 y =  43 ___ 70   5 __ 6 x -  1 __ 3 y = - 2 __ 3  4x + 8y = 8 For the following exercises, use addition to solve the system of equations. 6. 3x + 2y = -7 2x + 4y = 6 7. 3x + 4y = 2 9x + 12y = 3 8. 8x + 4y = 2 For the following exercises, write a system of equations to solve each problem. Solve the system of equations. 9. A factory has a cost of production C(x) = 150x + 15,000 and a revenue function R(x) = 200x. What is the break-even point? 10. A performer charges C(x) = 50x + 10,000, where x is the total number of attendees at a show. The venue charges $75 per ticket. After how many people buy tickets does the venue break even, and what is the value of the total tickets sold at that point? Systems of Linear Equations: Three Variables For the following exercises, solve the system of three equations using substitution or addition. 12. 5x + 3y - z = 5 3x - 2y + 4z = 13 4x + 3y + 5z = 22 13. x + y + z = 1 2x + 2y + 2z = 1 3x + 3y = 2 14. 2x - 3y + z = -1 x + y + z = -4 4x + 2y - 3z = 33 15. 3x + 2y - z = -10 x - y + 2z = 7 -x + 3y + z = -2 x - 2y = 5 4y - z = -10 17. 2x - 3y + z = 0 2x + 4y - 3z = 0 6x - 2y - z = 0 18. 6x - 4y - 2z = 2 3x + 2y - 5z = 4 6y - 7z = 5 For the following exercises, write a system of equations to solve each problem. Solve the system of equations. 19. Three odd numbers sum up to 61. The smaller is one-third the larger and the middle number is 16 less than the larger. What are the three numbers? 20. A local theatre sells out for their show. They sell all 500 tickets for a total purse of $8,070.00. The tickets were priced at $15 for students, $12 for children, and $18 for adults. If the band sold three times as many adult tickets as children’s tickets, how many of each type was sold?

Systems of Nonlinear Equations and Inequalities: Two Variables For the following exercises, solve the system of nonlinear equations. 21. y = x^{2} - 7 y = 5x - 13 22. y = x^{2} - 4 y = 5x + 10 23. x^{2} + y^{2} = 16 y = x - 8 24. x^{2} + y^{2} = 25 y = x^{2} + 5 25. x^{2} + y^{2} = 4 y - x^{2} = 3 For the following exercises, graph the inequality. 26. y > x^{2} - 1 __ 4 x^{2} + y^{2} < 4 For the following exercises, graph the system of inequalities. 28. x^{2} + y^{2} + 2x < 3 y > - x^{2} - 3 29. x^{2} - 2x + y^{2} - 4x < 4 y < - x + 4 30. x^{2} + y^{2} < 1 y^{2} < x Partial Fractions For the following exercises, decompose into partial fractions. __________ x^{2} + 3x + 2  32.  ___________ 4x^{2} + 4x + 1  33.  ____________

x^{2} + 10x + 25  34.  x - 18 ____________

x^{2} - 12x + 36  35.  -x^{2} + 36x + 70

_____________

 36.  -5x^{2} + 6x - 2

____________ x^{3} + 27

 37.  x^{3} - 4x^{2} + 3x + 11

________________

(x^{2} - 2)^{2}

 38.  4x^{4} - 2x^{3} + 22x^{2} - 6x + 48

_______________________

x(x^{2} + 4)^{2}

 Matrices and Matrix Operations For the following exercises, perform the requested operations on the given matrices. A =   4 -2

1 3  , B =   6 7 -3

11 -2 4  , C =  

  , D =   1 -4 9

10 5 -7

2 8 5   , E =  

2 -1 3

   41. B + C Solving Systems with Gaussian Elimination For the following exercises, write the system of linear equations from the augmented matrix. Indicate whether there will be a unique solution. 51.  

 ∣   

-5    52.  

 ∣    -9

   For the following exercises, write the augmented matrix from the system of linear equations. 53. -2x + 2y + z = 7 2x - 8y + 5z = 0 54. 4x + 2y - 3z = 14 -12x + 3y + z = 100 9x - 6y + 2z = 31 55. x + 3z = 12 -x + 4y = 0 y + 2z = - 7

For the following exercises, solve the system of linear equations using Gaussian elimination. 56. 3x - 4y = - 7 -6x + 8y = 14 57. 3x - 4y = 1 -6x + 8y = 6 59. 2x + 3y + 2z = 1 -4x - 6y - 4z = - 2 60. -x + 2y - 4z = 8 3y + 8z = - 4 -7x + y + 2z = 1 Solving Systems with Inverses For the following exercises, find the inverse of the matrix.

  1 __ 2  - 1 __ 2 

- 1 __ 4   3 __ 4     63.   12 9 -6

-1 3 2

-4 -3 2    64.  

   For the following exercises, find the solutions by computing the inverse of the matrix. 5x - 4y - z = -6.1 x + z = -0.7 68. -2x - 3y + 2z = 3 -x + 2y + 4z = -5 -2y + 5z = -3 For the following exercises, write a system of equations to solve each problem. Solve the system of equations. 69. Students were asked to bring their favorite fruit to class. 90% of the fruits consisted of banana, apple, and oranges. If oranges were half as popular as bananas and apples were 5% more popular than bananas, what are the percentages of each individual fruit? 70. A sorority held a bake sale to raise money and sold brownies and chocolate chip cookies. They priced the brownies at $2 and the chocolate chip cookies at $1. They raised $250 and sold 175 items. How many brownies and how many cookies were sold? Solving Systems with Cramer's Rule For the following exercises, find the determinant.

0 0  

73.   -1 4 3

   74.   \sqrt{2}  0 0

0 \sqrt{2}  0

0 0 

\sqrt{2}     For the following exercises, use Cramer’s Rule to solve the linear systems of equations. 75. 4x - 2y = 23 -5x - 10y = -35 78. x + 6y + 3z = 4 2x + y + 2z = 3 3x - 2y + z = 0 79. 4x - 3y + 5z = - 5 __ 2  7x - 9y - 3z =  3 __ 2  x - 5y - 5z =  5 __ 2  ___ 10 x -  1 __ 5 y -  3 ___ 10 z = - 1 ___ 50   1 ___ 10 x -  1 ___ 10 y -  1 __ 2 z = -  9 ___ 50   2 __ 5 x -  1 __ 2 y -  3 __ 5 z = - 1 __ 5 

Is the following ordered pair a solution to the system of equations? 1. -5x - y = 12 x + 4y = 9 with ( - 3, 3) For the following exercises, solve the systems of linear and nonlinear equations using substitution or elimination. Indicate if no solution exists. __ 2 x -  1 __ 3 y = 4  3 __ 2 x - y = 0 __ 2 x - 4y = 4 2x + 16y = 2 4. 5x - y = 1 -10x + 2y = - 2 5. 4x - 6y - 2z =  1 ___ 10  x - 7y + 5z = - 1 __ 4  3x + 6y - 9z =  6 __ 5  6. x + z = 20 x + y + z = 20 x + 2y + z = 10 7. 5x - 4y - 3z = 0 2x + y + 2z = 0 x - 6y - 7z = 0 8. y = x^{2} + 2x - 3 y = x - 1 9. y^{2} + x^{2} = 25 y^{2} - 2x^{2} = 1 For the following exercises, graph the following inequalities. 10. y < x^{2} + 9 11. x 2 + y 2 > 4 y < x^{2} + 1 For the following exercises, write the partial fraction decomposition. 12.  ____________

x^{2} + 10x + 25  ________ (3x + 1)^{2}  14.  x^{4} - x^{3} + 2x - 1

______________

x(x^{2} + 1)^{2}

 For the following exercises, perform the given matrix operations.

-2 3   +  1 __ 2  -6 12

4 -8   16.  

-2 9 5

     3 -4

     1 __ 2   1 __ 3 

 1 __ 4   1 __ 5     -1  18. det∣ 

 19. det  ∣   1 __ 2   - 1 __ 2   

- 1 __ 2  0   1 __ 2    1 __ 2    ∣  20. If det(A) = -6, what would be the determinant if you switched rows 1 and 3, multiplied the second row by 12, and took the inverse? 21. Rewrite the system of linear equations as an augmented matrix. -2x + 3y - 6z = -1 x - 5y + 12z = 11 22. Rewrite the augmented matrix as a system of linear equations.  

 ∣    

-5

  

For the following exercises, use Gaussian elimination to solve the systems of equations. 23. x - 6y = 4 2x - 12y = 0 24. 2x + y + z = -3 x - 2y + 3z = 6 x - y - z = 6 For the following exercises, use the inverse of a matrix to solve the systems of equations. -x + 2y = 80 ___ 100 x -  3 ___ 100 y +  1 ___  3 ___ 100 x -  7 ___ 100 y -  1 ___  9 ___ 100 x -  9 ___ 100 y -  9 ___ For the following exercises, use Cramer’s Rule to solve the systems of equations. For the following exercises, solve using a system of linear equations. 29. A factory producing cell phones has the following cost and revenue functions: C(x) = x 2 + 75x + 2,688 and R(x) = x 2 + 160x. What is the range of cell phones they should produce each day so there is profit? Round to the nearest number that generates profit. 30. A small fair charges $1.50 for students, $1 for children, and $2 for adults. In one day, three times as many children as adults attended. A total of 800 tickets were sold for a total revenue of $1,050. How many of each type of ticket was sold?
