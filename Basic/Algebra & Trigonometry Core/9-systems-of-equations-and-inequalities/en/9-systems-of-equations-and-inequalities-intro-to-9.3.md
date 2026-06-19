# Systems of Equations and Inequalities

## Introduction

---
By 1943, it was obvious to the Nazi regime that defeat was imminent unless it could build a weapon with unlimited destructive power, one that had never been seen before in the history of the world.
In September, Adolf Hitler ordered German scientists to begin building an atomic bomb.
Rumors and whispers began to spread from across the ocean.
Refugees and diplomats told of the experiments happening in Norway.
However, Franklin D.
Roosevelt wasn’t sold, and even doubted British Prime Minister Winston Churchill’s warning.
Roosevelt wanted undeniable proof.
Fortunately, he soon received the proof he wanted when a group of mathematicians cracked the “Enigma” code, proving beyond a doubt that Hitler was building an atomic bomb.
The next day, Roosevelt gave the order that the United States begin work on the same.
The Enigma is perhaps the most famous cryptographic device ever known.
It stands as an example of the pivotal role cryptography has played in society.
Now, technology has moved cryptanalysis to the digital world.
Many ciphers are designed using invertible matrices as the method of message transference, as finding the inverse of a matrix is generally part of the process of decoding.
In addition to knowing the matrix and its inverse, the receiver must also know the key that, when used with the matrix inverse, will allow the message to be read.
In this chapter, we will investigate matrices and their inverses, and various ways to use matrices to solve systems of equations.
First, however, we will study systems of equations on their own: linear and nonlinear, and then partial fractions.
We will not be breaking any secret codes here, but we will lay the foundation for future courses. 9.1 Systems of Linear Equations:
Two Variables 9.2 Systems of Linear Equations:
Three Variables 9.3 Systems of Nonlinear Equations and Inequalities:
Two Variables 9.4 Partial Fractions 9.5 Matrices and Matrix Operations 9.6 Solving Systems with Gaussian Elimination 9.7 Solving Systems with Inverses 9.8 Solving Systems with Cramer's Rule

## 9.1 Systems of Linear Equations:
Two variables

---
A skateboard manufacturer introduces a new line of boards.
The manufacturer tracks its costs, which is the amount it spends to produce the boards, and its revenue, which is the amount it earns through sales of its boards.
How can the company determine if it is making a profit with its new line?
How many skateboards must be produced and sold before a profit is possible?
In this section, we will consider linear equations with two variables to answer these and similar questions.
Introduction to Systems of Equations In order to investigate situations such as that of the skateboard manufacturer, we need to recognize that we are dealing with more than one variable and likely more than one equation.
A system of linear equations consists of two or more linear equations made up of two or more variables such that all equations in the system are considered simultaneously.
To find the unique solution to a system of linear equations, we must find a numerical value for each variable in the system that will satisfy all equations in the system at the same time.
Some linear systems may not have a solution and others may have an infinite number of solutions.
In order for a linear system to have a unique solution, there must be at least as many equations as there are variables.
Even so, this does not guarantee a unique solution.
In this section, we will look at systems of linear equations in two variables, which consist of two equations that contain two different variables.
For example, consider the following system of linear equations in two variables.

2x + y = 15

3x - y = 5 The solution to a system of linear equations in two variables is any ordered pair that satisfies each equation independently.
In this example, the ordered pair (4, 7) is the solution to the system of linear equations.
We can verify the solution by substituting the values into each equation to see if the ordered pair satisfies both equations.
Shortly we will investigate methods of finding such a solution if it exists.

2(4) + (7) = 15 True

3(4) - (7) = 5 True In addition to considering the number of equations and variables, we can categorize systems of linear equations by the number of solutions.
A consistent system of equations has at least one solution.
A consistent system is considered to be an independent system if it has a single solution, such as the example we just explored.
The two lines have Learning Objectives
In this section, you will:
• Solve systems of equations by graphing.
• Solve systems of equations by substitution.
• Solve systems of equations by addition.
• Identify inconsistent systems of equations containing two variables.
• Express the solution of a system of dependent equations containing two variables.
different slopes and intersect at one point in the plane.
A consistent system is considered to be a dependent system if the equations have the same slope and the same y-intercepts.
In other words, the lines coincide so the equations represent the same line.
Every point on the line represents a coordinate pair that satisfies the system.
Thus, there are an infinite number of solutions.
Another type of system of linear equations is an inconsistent system, which is one in which the equations represent two parallel lines.
The lines have the same slope and different y-intercepts.
There are no points common to both lines; hence, there is no solution to the system. types of linear systems There are three types of systems of linear equations in two variables, and three types of solutions.
• An independent system has exactly one solution pair (x, y).
The point where the two lines intersect is the only solution. • An inconsistent system has no solution.
Notice that the two lines are parallel and will never intersect. • A dependent system has infinitely many solutions.
The lines are coincident.
They are the same line, so every coordinate pair on the line is a solution to both equations.
( ( y x y x y x

---
### 💡 **How To…**
Given a system of linear equations and an ordered pair, determine whether the ordered pair is a solution. 1.
Substitute the ordered pair into each equation in the system. 2.
Determine whether true statements result from the substitution in both equations; if so, the ordered pair is a solution.

---
### 📐 **Example 1**:
Determining Whether an Ordered Pair Is a

**Solution**

to a System of Equations

Determine whether the ordered pair (5, 1) is a solution to the given system of equations.

x + 3y = 8

2x - 9 = y

**Solution**

Substitute the ordered pair (5, 1) into both equations.

(5) + 3(1) = 8

8 = 8 True

2(5) - 9 = (1)

1 = 1 True The ordered pair (5, 1) satisfies both equations, so it is the solution to the system.
Analysis We can see the solution clearly by plotting the graph of each equation.
Since the solution is an ordered pair that satisfies both equations, it is a point on both of the lines and thus the point of intersection of the two lines.
See Figure 3.

x y 2x - 9 = y x +3y = 8

---
### ✏️ **Try It #1**
Determine whether the ordered pair (8, 5) is a solution to the following system.

5x - 4y = 20

2x + 1 = 3y Solving Systems of Equations by Graphing There are multiple methods of solving systems of linear equations.
For a system of linear equations in two variables, we can determine both the type of system and the solution by graphing the system of equations on the same set of axes.

---
### 📐 **Example 2**:
Solving a System of Equations in Two Variables by Graphing

Solve the following system of equations by graphing.
Identify the type of system.

2x + y = -8

x - y = -1

**Solution**

Solve the first equation for y.

2x + y = -8

y = - 2x -8 Solve the second equation for y.

x - y = -1

y = x + 1 Graph both equations on the same set of axes as in Figure 4. x y y = -2x -8 y = x + 1

The lines appear to intersect at the point (-3, -2). We can check to make sure that this is the solution to the system by substituting the ordered pair into both equations.

2(-3) + (-2) = -8

-8 = -8 True

(-3) - (-2) = -1

-1 = -1 True The solution to the system is the ordered pair (-3, -2), so the system is independent.

---
### ✏️ **Try It #2**
Solve the following system of equations by graphing.

2x - 5y = -25

-4x + 5y = 35 Can graphing be used if the system is inconsistent or dependent?
Yes, in both cases we can still graph the system to determine the type of system and solution.
If the two lines are parallel, the system has no solution and is inconsistent.
If the two lines are identical, the system has infinite solutions and is a dependent system.
Solving Systems of Equations by Substitution Solving a linear system in two variables by graphing works well when the solution consists of integer values, but if our solution contains decimals or fractions, it is not the most precise method.
We will consider two more methods of solving a system of linear equations that are more precise than graphing.
One such method is solving a system of equations by the substitution method, in which we solve one of the equations for one variable and then substitute the result into the second equation to solve for the second variable.
Recall that we can solve for only one variable at a time, which is the reason the substitution method is both valuable and practical.

---
### 💡 **How To…**
Given a system of two equations in two variables, solve using the substitution method. 1.
Solve one of the two equations for one of the variables in terms of the other. 2.
Substitute the expression for this variable into the second equation, then solve for the remaining variable. 3.
Substitute that solution into either of the original equations to find the value of the first variable.
If possible, write the solution as an ordered pair. 4.
Check the solution in both equations.

---
### 📐 **Example 3**:
Solving a System of Equations in Two Variables by Substitution

Solve the following system of equations by substitution.

-x + y = -5

2x - 5y = 1

**Solution**

First, we will solve the first equation for y.

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

---
### ✏️ **Try It #3**
Solve the following system of equations by substitution.

x = y + 3

4 = 3x - 2y Can the substitution method be used to solve any linear system in two variables?
Yes, but the method works best if one of the equations contains a coefficient of 1 or -1 so that we do not have to deal with fractions.
Solving Systems of Equations in Two Variables by the Addition Method A third method of solving systems of linear equations is the addition method.
In this method, we add two terms with the same variable, but opposite coefficients, so that the sum is zero.
Of course, not all systems are set up with the two terms of one variable having opposite coefficients.
Often we must adjust one or both of the equations by multiplication so that one variable will be eliminated by addition.

---
### 💡 **How To…**
Given a system of equations, solve using the addition method. 1.
Write both equations with x- and y-variables on the left side of the equal sign and constants on the right. 2.
Write one equation above the other, lining up corresponding variables.
If one of the variables in the top equation has the opposite coefficient of the same variable in the bottom equation, add the equations together, eliminating one variable.
If not, use multiplication by a nonzero number so that one of the variables in the top equation has the opposite coefficient of the same variable in the bottom equation, then add the equations to eliminate the variable. 3.
Solve the resulting equation for the remaining variable. 4.
Substitute that value into one of the original equations and solve for the second variable. 5.
Check the solution by substituting the values into the other equation.

---
### 📐 **Example 4**:
Solving a System by the Addition Method

Solve the given system of equations by addition.

x + 2y = -1

-x + y = 3

**Solution**

Both equations are already set equal to a constant.
Notice that the coefficient of x in the second equation, -1, is the opposite of the coefficient of x in the first equation, 1.
We can add the two equations to eliminate x without needing to multiply by a constant.

x + 2y = - 1

-x + y = 3

3y = 2 Now that we have eliminated x, we can solve the resulting equation for y.

3y = 2

y = 2/3 Then, we substitute this value for y into one of the original equations and solve for x.

-x + y = 3

-x + 2/3 = 3

-x = 3 - 2/3 

-x = 7/3 

x = - 7/3 The solution to this system is ( - 7/3 , 2/3 ) Check the solution in the first equation.

x + 2y = -1

( - 7/3 ) + 2( 2/3 ) = -1

- 7/3 + 4/3 = -1

- 3/3 = -1

-1 = -1 True Analysis We gain an important perspective on systems of equations by looking at the graphical representation.
See because observing the graph confirms that the system has exactly one solution. x + 2y = -1 x y -x + y = 3

---
### 📐 **Example 5**
Using the Addition Method When Multiplication of One Equation Is Required Solve the given system of equations by the addition method.

3x + 5y = -11

x - 2y = 11

**Solution**

Adding these equations as presented will not eliminate a variable.
However, we see that the first equation has 3x in it and the second equation has x.
So if we multiply the second equation by -3, the x-terms will add to zero.

x - 2y = 11

-3(x - 2y) = -3(11) Multiply both sides by -3.

-3x + 6y = -33

Use the distributive property.
Now, let’s add them.

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

---
### ✏️ **Try It #4**
Solve the system of equations by addition.

2x - 7y = 2

3x + y = -20

---
### 📐 **Example 6**
Using the Addition Method When Multiplication of Both Equations Is Required Solve the given system of equations in two variables by addition.

2x + 3y = -16

**Solution**

One equation has 2x and the other has 5x.
The least common multiple is 10x so we will have to multiply both equations by a constant in order to eliminate one variable.
Let’s eliminate x by multiplying the first equation by -5 and the second equation by 2.

- 5(2x + 3y) = -5(-16)

Then, we add the two equations together.

y = -4 Substitute y = -4 into the original first equation.

2x + 3(-4) = -16

2x = -4

x = -2 The solution is (-2, -4). Check it in the other equation.

See Figure 7. x y 2x + 3y = -16

---
### 📐 **Example 7**
Using the Addition Method in Systems of Equations Containing Fractions Solve the given system of equations in two variables by addition.

 x/3 + y/6 = 3

 x/2 - y/4 = 1

**Solution**

First clear each equation of fractions by multiplying both sides of the equation by the least common denominator.

6( x/3 + y/6 ) = 6(3)

2x + y = 18

4( x/2 - y/4 ) = 4(1)

2x - y = 4

Now multiply the second equation by -1 so that we can eliminate the x-variable.

-1(2x - y) = -1(4)

-2x + y = -4 Add the two equations to eliminate the x-variable and solve the resulting equation.

2x + y = 18

-2x + y = -4

y = 7 Substitute y = 7 into the first equation.

2x + (7) = 18

x = 11 2 

= 5.5 The solution is ( 11 2 , 7 ) . Check it in the other equation.

 x/2 - y/4 = 1

 11/2 2 - 7/4 = 1

 11 4 - 7/4 = 1

 4/4 = 1

---
### ✏️ **Try It #5**
Solve the system of equations by addition.

2x + 3y = 8

3x + 5y = 10 Identifying Inconsistent Systems of Equations Containing Two Variables Now that we have several methods for solving systems of equations, we can use the methods to identify inconsistent systems.
Recall that an inconsistent system consists of parallel lines that have the same slope but different y-intercepts.
They will never intersect.
When searching for a solution to an inconsistent system, we will come up with a false statement, such as 12 = 0.

---
### 📐 **Example 8**:
Solving an Inconsistent System of Equations

Solve the following system of equations.

x = 9 - 2y

x + 2y = 13

**Solution**

We can approach this problem in two ways.
Because one equation is already solved for x, the most obvious step is to use substitution.

x + 2y = 13

(9 - 2y) + 2y = 13

Clearly, this statement is a contradiction because 9 ≠ 13.
Therefore, the system has no solution.

The second approach would be to first manipulate the equations so that they are both in slope-intercept form.
We manipulate the first equation as follows.

x = 9 - 2y

2y = - x + 9

y = - 1/2 x + 9/2 We then convert the second equation expressed to slope-intercept form.

x + 2y = 13

2y = - x + 13

y = - 1/2 x + 13 2 Comparing the equations, we see that they have the same slope but different y-intercepts.
Therefore, the lines are parallel and do not intersect.

y = - 1/2 x + 9/2 

y = - 1/2 x + 13 2 Analysis Writing the equations in slope-intercept form confirms that the system is inconsistent because all lines will intersect eventually unless they are parallel.
Parallel lines will never intersect; thus, the two lines have no points in common.
The graphs of the equations in this example are shown in Figure 8. x y y = -x + y = -x +

---
### ✏️ **Try It #6**
Solve the following system of equations in two variables.

2y - 2x = 2

2y - 2x = 6 Expressing the

**Solution**

of a System of Dependent Equations Containing Two Variables Recall that a dependent system of equations in two variables is a system in which the two equations represent the same line.
Dependent systems have an infinite number of solutions because all of the points on one line are also on the other line.
After using substitution or addition, the resulting equation will be an identity, such as 0 = 0.

---
### 📐 **Example 9**
Finding a

**Solution**

to a Dependent System of Linear Equations Find a solution to the system of equations using the addition method.

x + 3y = 2

3x + 9y = 6

**Solution**

With the addition method, we want to eliminate one of the variables by adding the equations.
In this case, let’s focus on eliminating x.
If we multiply both sides of the first equation by -3, then we will be able to eliminate the x-variable.

x + 3y = 2

(-3)(x + 3y) = (-3)(2)

-3x - 9y = - 6 Now add the equations.

-3x - 9y = -6

+ 3x + 9y = 6

0 = 0 We can see that there will be an infinite number of solutions that satisfy both equations.
Analysis If we rewrote both equations in the slope-intercept form, we might know what the solution would look like before adding.
Let’s look at what happens when we convert the system to slope-intercept form.

x + 3y = 2

3y = - x + 2

y = - 1/3 x + 2/3 

3x + 9y = 6

9y = -3x + 6

y = - 3/9 x + 6/9 

y = - 1/3 x + 2/3 See Figure 9. Notice the results are the same. The general solution to the system is ( x, - 1/3 x + 2/3 ) . x y x + 3y = 2 3x + 9y = 6

---
### ✏️ **Try It #7**
Solve the following system of equations in two variables.

y - 2x = 5

-3y + 6x = -15 Using Systems of Equations to Investigate Profits Using what we have learned about systems of equations, we can return to the skateboard manufacturing problem at the beginning of the section.
The skateboard manufacturer’s revenue function is the function used to calculate the amount of money that comes into the business.
It can be represented by the equation R = xp, where x = quantity and p = price.
The revenue function is shown in orange in Figure 10.
The cost function is the function used to calculate the costs of doing business.
It includes fixed costs, such as rent and salaries, and variable costs, such as utilities.
The cost function is shown in blue in Figure 10.
The x-axis represents quantity in hundreds of units.
The y-axis represents either cost or revenue in hundreds of dollars.

Money (in hundreds of dollars) Revenue Break-even Cost Quantity (in hundreds of units) Profit The point at which the two lines intersect is called the break-even point.
We can see from the graph that if 700 units are produced, the cost is $3,300 and the revenue is also $3,300.
In other words, the company breaks even if they produce and sell 700 units.
They neither make money nor lose money.
The shaded region to the right of the break-even point represents quantities for which the company makes a profit.
The shaded region to the left represents quantities for which the company suffers a loss.
The profit function is the revenue function minus the cost function, written as P(x) = R(x) - C(x).
Clearly, knowing the quantity for which the cost equals the revenue is of great importance to businesses.

---
### 📐 **Example 10**
Finding the Break-Even Point and the Profit Function Using Substitution Given the cost function C(x) = 0.85x + 35,000 and the revenue function R(x) = 1.55x, find the break-even point and the profit function.

**Solution**

Write the system of equations using y to replace function notation.

Substitute the expression 0.85x + 35,000 from the first equation into the second equation and solve for x.

Then, we substitute x = 50,000 into either the cost function or the revenue function.

The break-even point is (50,000, 77,500). The profit function is found using the formula P(x) = R(x) - C(x).

The profit function is P(x) = 0.7x - 35,000.
Analysis The cost to produce 50,000 units is $77,500, and the revenue from the sales of 50,000 units is also $77,500.
To make a profit, the business must produce and sell more than 50,000 units.
See Figure 11.
We see from the graph in Figure 12 that the profit function has a negative value until x = 50,000, when the graph crosses the x-axis.
Then, the graph emerges into positive y-values and continues on this path as the profit function is a straight line.
This illustrates that the break-even point for businesses occurs when the profit function is 0.
The area to the left of the break-even point represents operating at a loss.

Dollars Quantity Break-even point Profit Cost Revenue R(x) = 1.55x Dollars profit Quantity Profit Break-even point Profit

---
### 📐 **Example 11**:
Writing and Solving a System of Equations in Two Variables

The cost of a ticket to the circus is $25.00 for children and $50.00 for adults.
On a certain day, attendance at the circus is 2,000 and the total gate revenue is $70,000.
How many children and how many adults bought tickets?

**Solution**

Let c = the number of children and a = the number of adults in attendance.
The total number of people is 2,000.
We can use this to write an equation for the number of people at the circus that day.

The revenue from all children can be found by multiplying $25.00 by the number of children, 25c.
The revenue from all adults can be found by multiplying $50.00 by the number of adults, 50a.
The total revenue is $70,000.
We can use this to write an equation for the revenue.

We now have a system of linear equations in two variables.

In the first equation, the coefficient of both variables is 1.
We can quickly solve the first equation for either c or a.
We will solve for a.

Substitute the expression 2,000 - c in the second equation for a and solve for c.

Substitute c = 1,200 into the first equation to solve for a.

We find that 1,200 children and 800 adults bought tickets to the circus that day.

---
### ✏️ **Try It #8**
Meal tickets at the circus cost $4.00 for children and $12.00 for adults.
If 1,650 meal tickets were bought for a total of $14,200, how many children and how many adults bought meal tickets?
Access these online resources for additional instruction and practice with systems of linear equations.
• Solving Systems of Equations Using Substitution (http://openstaxcollege.org/l/syssubst) • Solving Systems of Equations Using Elimination (http://openstaxcollege.org/l/syselim) • Applications of Systems of Equations (http://openstaxcollege.org/l/sysapp)

## 9.1 Section Exercises

---
### 9.1 Section Exercises

Verbal 1.
Can a system of linear equations have exactly two solutions?
Explain why or why not. 2.
If you are performing a break-even analysis for a business and their cost and revenue equations are dependent, explain what this means for the company’s profit margins. 3.
If you are solving a break-even analysis and get a negative break-even point, explain what this signifies for the company? 4.
If you are solving a break-even analysis and there is no break-even point, explain what this means for the company.
How should they ensure there is a break-even point? 5.
Given a system of equations, explain at least two different methods of solving that system.
Algebraic For the following exercises, determine whether the given ordered pair is a solution to the system of equations. 6. 5x - y = 4 x + 6y = 2 and (4, 0) - x + 4y = 10 and (-6, 1) 2x + 4y = 0 and (2, 3) 9. -2x + 5y = 7 2x + 9y = 7 and (-1, 1) 3x - 2y = -1 and (3, 5) For the following exercises, solve each system by substitution.
11. x + 3y = 5 2x + 3y = 4 3x + 9y = 0 16. x - 0.2y = 1 -10x + 2y = 5 17. 3 x + 5y = 9 18. -3x + y = 2 12x - 4y = -8/2 x + 1/3 y = 16 1/6 x + 1/4 y = 9/4 x + 3/2 y = 11 - 1/8 x + 1/3 y = 3 For the following exercises, solve each system by addition. 7x + 2y = 30 2x + 6y = 4 23. 5x - y = -2.6 25. -x + 2y = -1 5x - 10y = 6 26. 7x + 6y = 2 -28x - 24y = -8/6 x + 1/4 y = 0 1/8 x - 1/2 y = - 43 120/3 x + 1/9 y = 2/9 - 1/2 x + 4/5 y = - 1/3 x - 2y = -3 5x - 10y = 1 For the following exercises, solve each system by any method. x + 2y = 4 7x - 4y = 3 34. x - 5 12 y = - 55 12 -6x + 5/2 y = 55 2 

35. 7x - 4y = 7/6 2x + 4y = 1/3 2x + 4y = 9/3 x - 1/6 y = 2 - 21 6 x + 3 12 y = -3/2 x + 1/3 y = 1/3 3/2 x + 1/4 y = - 1/8 Graphical For the following exercises, graph the system of equations and state whether the system is consistent, inconsistent, or dependent and whether the system has one solution, no solution, or infinite solutions. x - 2y = 1.3 42. -x + 2y = 4 2x - 4y = 1 43. x + 2y = 7 2x + 6y = 12 x - 2y = 3 45. 3x - 2y = 5 -9x + 6y = -15 Technology For the following exercises, use the intersect function on a graphing device to solve each system. Round all answers to the nearest hundredth. Extensions For the following exercises, solve each system in terms of A, B, C, D, E, and F where A – F are nonzero numbers. Note that A ≠ B and AE ≠ BD.
51. x + y = A x - y = B 52. x + Ay = 1 x + By = 1 53. Ax + y = 0 Bx + y = 1 54. Ax + By = C x + y = 1 55. Ax + By = C Dx + Ey = F Real-World Applications For the following exercises, solve for the desired quantity. 56. A stuffed animal business has a total cost of production C = 12x + 30 and a revenue function R = 20x. Find the break-even point. 57. A fast-food restaurant has a cost of production C(x) = 11x + 120 and a revenue function R(x) = 5x. When does the company start to turn a profit? 58. A cell phone factory has a cost of production C(x) = 150x + 10,000 and a revenue function R(x) = 200x. What is the break-even point? 59. A musician charges C(x) = 64x + 20,000, where x is the total number of attendees at the concert. The venue charges $80 per ticket. After how many people buy tickets does the venue break even, and what is the value of the total tickets sold at that point? 60. A guitar factory has a cost of production C(x) = 75x + 50,000. If the company needs to break even after 150 units sold, at what price should they sell each guitar? Round up to the nearest dollar, and write the revenue function.

For the following exercises, use a system of linear equations with two variables and two equations to solve. 61.
Find two numbers whose sum is 28 and difference 62.
A number is 9 more than another number.
Twice the sum of the two numbers is 10.
Find the two numbers. 63.
The startup cost for a restaurant is $120,000, and each meal costs $10 for the restaurant to make.
If each meal is then sold for $15, after how many meals does the restaurant break even? 64.
A moving company charges a flat rate of $150, and an additional $5 for each box.
If a taxi service would charge $20 for each box, how many boxes would you need for it to be cheaper to use the moving company, and what would be the total cost? 65.
A total of 1,595 first- and second-year college students gathered at a pep rally.
The number of freshmen exceeded the number of sophomores by 15.
How many freshmen and sophomores were in attendance? 66. 276 students enrolled in a freshman-level chemistry class.
By the end of the semester, 5 times the number of students passed as failed.
Find the number of students who passed, and the number of students who failed. 67.
There were 130 faculty at a conference.
If there were 18 more women than men attending, how many of each gender attended the conference? 68.
A jeep and BMW enter a highway running east- west at the same exit heading in opposite directions.
The jeep entered the highway 30 minutes before the BMW did, and traveled 7 mph slower than the BMW.
After 2 hours from the time the BMW entered the highway, the cars were 306.5 miles apart.
Find the speed of each car, assuming they were driven on cruise control. 69.
If a scientist mixed 10% saline solution with 60% saline solution to get 25 gallons of 40% saline solution, how many gallons of 10% and 60% solutions were mixed? 70.
An investor earned triple the profits of what she earned last year.
If she made $500,000.48 total for both years, how much did she earn in profits each year? 71.
An investor who dabbles in real estate invested 1.1 million dollars into two land investments.
On the first investment, Swan Peak, her return was a 110% increase on the money she invested.
On the second investment, Riverside Community, she earned 50% over what she invested.
If she earned $1 million in profits, how much did she invest in each of the land deals? 72.
If an investor invests a total of $25,000 into two bonds, one that pays 3% simple interest, and the other that pays 2 7/8 % interest, and the investor earns $737.50 annual interest, how much was invested in each account? 73.
If an investor invests $23,000 into two bonds, one that pays 4% in simple interest, and the other paying 2% simple interest, and the investor earns $710.00 annual interest, how much was invested in each account? 74.
CDs cost $5.96 more than DVDs at All Bets Are Off Electronics.
How much would 6 CDs and 2 DVDs cost if 5 CDs and 2 DVDs cost $127.73? 75.
A store clerk sold 60 pairs of sneakers.
The high-tops sold for $98.99 and the low-tops sold for $129.99.
If the receipts for the two types of sales totaled $6,404.40, how many of each type of sneaker were sold? 76.
A concert manager counted 350 ticket receipts the day after a concert.
The price for a student ticket was $12.50, and the price for an adult ticket was $16.00.
The register confirms that $5,075 was taken in.
How many student tickets and adult tickets were sold? 77.
Admission into an amusement park for 4 children and 2 adults is $116.90.
For 6 children and 3 adults, the admission is $175.35.
Assuming a different price for children and adults, what is the price of the child’s ticket and the price of the adult ticket?

## 9.2 Systems of Linear Equations:
Three variables

---
John received an inheritance of $12,000 that he divided into three parts and invested in three ways: in a money-market fund paying 3% annual interest; in municipal bonds paying 4% annual interest; and in mutual funds paying 7% annual interest.
John invested $4,000 more in municipal funds than in municipal bonds.
He earned $670 in interest the first year.
How much did John invest in each type of fund?
Understanding the correct approach to setting up problems such as this one makes finding a solution a matter of following a pattern.
We will solve this and similar problems involving three equations and three variables in this section.
Doing so uses similar techniques as those used to solve systems of two equations in two variables.
However, finding solutions to systems of three equations requires a bit more organization and a touch of visual gymnastics.
Solving Systems of Three Equations in Three Variables In order to solve systems of equations in three variables, known as three-by-three systems, the primary tool we will be using is called Gaussian elimination, named after the prolific German mathematician Karl Friedrich Gauss.
While there is no definitive order in which operations are to be performed, there are specific guidelines as to what type of moves can be made.
We may number the equations to keep track of the steps we apply.
The goal is to eliminate one variable at a time to achieve upper triangular form, the ideal form for a three-by-three system because it allows for straightforward back-substitution to find a solution (x, y, z), which we call an ordered triple.
A system in upper triangular form looks like the following:

Ax + By + Cz = D

Ey + Fz = G

Hz = K The third equation can be solved for z, and then we back-substitute to find y and x.
To write the system in upper triangular form, we can perform the following operations: 1.
Interchange the order of any two equations. 2.
Multiply both sides of an equation by a nonzero constant. 3.
Add a nonzero multiple of one equation to another equation.
Learning Objectives
In this section, you will:
• Solve systems of three equations in three variables.
• Identify inconsistent systems of equations containing three variables.
• Express the solution of a system of dependent equations containing three variables.
The solution set to a three-by-three system is an ordered triple {(x, y, z)}.
Graphically, the ordered triple defines the point that is the intersection of three planes in space.
You can visualize such an intersection by imagining any corner in a rectangular room.
A corner is defined by three planes: two adjoining walls and the floor (or ceiling).
Any point where two walls and the floor meet represents the intersection of three planes. number of possible solutions • Systems that have a single solution are those which, after elimination, result in a solution set consisting of an ordered triple {(x, y, z)}.
Graphically, the ordered triple defines a point that is the intersection of three planes in space.
• Systems that have an infinite number of solutions are those which, after elimination, result in an expression that is always true, such as 0 = 0.
Graphically, an infinite number of solutions represents a line or coincident plane that serves as the intersection of three planes in space.
• Systems that have no solution are those that, after elimination, result in a statement that is a contradiction, such as 3 = 0.
Graphically, a system with no solution is represented by three planes with no point in common.
(a) (b) ( b) Three planes intersect in a line, representing a three-by-three system with infinite solutions.
(a) (b) (c) (b) Two of the planes are parallel and intersect with the third plane, but not with each other.
( c) All three planes are parallel, so there is no point of intersection.

---
### 📐 **Example 1**:
Determining Whether an Ordered Triple Is a

**Solution**

to a System

Determine whether the ordered triple (3, -2, 1) is a solution to the system.

x + y + z = 2

6x - 4y + 5z = 31

5x + 2y + 2z = 13

**Solution**

We will check each equation by substituting in the values of the ordered triple for x, y, and z.

x + y + z = 2

(3) + (-2) + (1) = 2

True

6x - 4y + 5z = 31

6(3) - 4(-2) + 5(1) = 31

True

5x + 2y + 2z = 13

5(3) + 2(-2) + 2(1) = 13

True The ordered triple (3, -2, 1) is indeed a solution to the system.

---
### 💡 **How To…**
Given a linear system of three equations, solve for three unknowns. 1.
Pick any pair of equations and solve for one variable. 2.
Pick another pair of equations and solve for the same variable. 3.
You have created a system of two equations in two unknowns.
Solve the resulting two-by-two system. 4.
Back-substitute known variables into any one of the original equations and solve for the missing variable.

---
### 📐 **Example 2**:
Solving a System of Three Equations in Three Variables by Elimination

Find a solution to the following system:

x - 2y + 3z = 9 (1)

-x + 3y - z = -6 (2)

2x - 5y + 5z = 17 (3)

**Solution**

There will always be several choices as to where to begin, but the most obvious first step here is to eliminate x by adding equations (1) and (2).

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

---
### 📐 **Example 3**
Solving a Real-World Problem Using a System of Three Equations in Three Variables In the problem posed at the beginning of the section, John invested his inheritance of $12,000 in three different funds: part in a money-market fund paying 3% interest annually; part in municipal bonds paying 4% annually; and the rest in mutual funds paying 7% annually.
John invested $4,000 more in mutual funds than he invested in municipal bonds.
The total interest earned in one year was $670.
How much did he invest in each type of fund?

**Solution**

To solve this problem, we use all of the information given and set up three equations.
First, we assign a variable to each of the three investment amounts:

x = amount invested in money-market fund

y = amount invested in municipal bonds

z = amount invested in mutual funds The first equation indicates that the sum of the three principal amounts is $12,000.

x + y + z = 12,000 We form the second equation according to the information that John invested $4,000 more in mutual funds than he invested in municipal bonds.

The third equation shows that the total amount of interest earned from each fund equals $670.

Then, we write the three equations as a system.

x + y + z = 12,000

- y + z = 4,000

To make the calculations simpler, we can multiply the third equation by 100.
Thus,

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

---
### ✏️ **Try It #1**
Solve the system of equations in three variables.

2x + y - 2z = -1

3x - 3y - z = 5

x - 2y + 3z = 6 Identifying Inconsistent Systems of Equations Containing Three Variables Just as with systems of equations in two variables, we may come across an inconsistent system of equations in three variables, which means that it does not have a solution that satisfies all three equations.
The equations could represent three parallel planes, two parallel planes and one intersecting plane, or three planes that intersect the other two but not at the same location.
The process of elimination will result in a false statement, such as 3 = 7 or some other contradiction.

---
### 📐 **Example 4**:
Solving an Inconsistent System of Three Equations in Three Variables

Solve the following system.

x - 3y + z = 4 (1)

-x + 2y - 5z = 3 (2)

5x - 13y + 13z = 8 (3)

**Solution**

Looking at the coefficients of x, we can see that we can eliminate x by adding equation (1) to equation (2).

x - 3y + z = 4 (1)

-x + 2y - 5z = 3 (2)

-y - 4z = 7 (4) Next, we multiply equation (1) by -5 and add it to equation (3).

-5x + 15y - 5z = -20 (1) multiplied by -5

5x - 13y + 13z = 8 (3)

2y + 8z = -12 (5) Then, we multiply equation (4) by 2 and add it to equation (5).

-2y - 8z = 14 (4) multiplied by 2

2y + 8z = -12 (5)

0 = 2

The final equation 0 = 2 is a contradiction, so we conclude that the system of equations in inconsistent and, therefore, has no solution.
Analysis In this system, each plane intersects the other two, but not at the same location.
Therefore, the system is inconsistent.

---
### ✏️ **Try It #2**
Solve the system of three equations in three variables.

x + y + z = 2

y - 3z = 1

2x + y + 5z = 0 Expressing the

**Solution**

of a System of Dependent Equations Containing Three Variables We know from working with systems of equations in two variables that a dependent system of equations has an infinite number of solutions.
The same is true for dependent systems of equations in three variables.
An infinite number of solutions can result from several situations.
The three planes could be the same, so that a solution to one equation will be the solution to the other two equations.
All three equations could be different but they intersect on a line, which has infinite solutions.
Or two of the equations could be the same and intersect the third on a line.

---
### 📐 **Example 5**
Finding the

**Solution**

to a Dependent System of Equations Find the solution to the given system of three equations in three variables.

2x + y - 3z = 0

(1)

4x + 2y - 6z = 0

(2)

x - y + z = 0

(3)

**Solution**

First, we can multiply equation (1) by -2 and add it to equation (2).

-4x - 2y + 6z = 0 equation (1) multiplied by -2

4x + 2y - 6z = 0

(2)

0 = 0 We do not need to proceed any further.
The result we get is an identity, 0 = 0, which tells us that this system has an infinite number of solutions.
There are other ways to begin to solve this system, such as multiplying equation (3) by -2, and adding it to equation (1).
We then perform the same steps as above and find the same result, 0 = 0.
When a system is dependent, we can find general expressions for the solutions.
Adding equations (1) and (3), we have

2x + y - 3z = 0

x - y + z = 0

3x - 2z = 0 We then solve the resulting equation for z.

3x - 2z = 0

z = 3/2 x We back-substitute the expression for z into one of the equations and solve for y.

2x + y - 3( 3/2 x ) = 0

2x + y - 9/2 x = 0

y = 9/2 x - 2x

y = 5/2 x So the general solution is ( x, 5/2 x, 3/2 x ) .
In this solution, x can be any real number.
The values of y and z are dependent on the value selected for x.
Analysis As shown in Figure 5, two of the planes are the same and they intersect the third plane on a line.
The solution set is infinite, as all points along the intersection line will satisfy all three equations. x - y + z = 0 -4x - 2y + 6z = 0 4x + 2y - 6z = 0 Does the generic solution to a dependent system always have to be written in terms of x?
No, you can write the generic solution in terms of any of the variables, but it is common to write it in terms of x and if needed x and y.

---
### ✏️ **Try It #3**
Solve the following system.

x + y + z = 7

3x - 2y - z = 4

x + 6y + 5z = 24 Access these online resources for additional instruction and practice with systems of equations in three variables.
• Ex 1: System of Three Equations with Three Unknowns Using Elimination (http://openstaxcollege.org/l/systhree) • Ex. 2: System of Three Equations with Three Unknowns Using Elimination (http://openstaxcollege.org/l/systhelim)

## 9.2 Section Exercises

---
### 9.2 Section Exercises

Verbal 1.
Can a linear system of three equations have exactly two solutions?
Explain why or why not 2.
If a given ordered triple solves the system of equations, is that solution unique?
If so, explain why.
If not, give an example where it is not unique. 3.
If a given ordered triple does not solve the system of equations, is there no solution?
If so, explain why.
If not, give an example. 4.
Using the method of addition, is there only one way to solve the system? 5.
Can you explain whether there can be only one method to solve a linear system of equations?
If yes, give an example of such a system of equations.
If not, explain why not.
Algebraic For the following exercises, determine whether the ordered triple given is the solution to the system of equations. 6. 2x - 6y + 6z = -12 x + 4y + 5z = -1 and (0, 1, -1) -x + 2y + 3z = -1 7. 6x - y + 3z = 6 3x + 5y + 2z = 0 and (3, -3, -5) x + y = 0 8. 6x - 7y + z = 2 -x - y + 3z = 4 and (4, 2, -6) 2x + y - z = 1 9. x - y = 0 x - z = 5 and (4, 4, -1) x - y + z = -1 10. -x - y + 2z = 3 5x + 8y - 3z = 4 and (4, 1, -7) -x + 3y - 5z = -5 For the following exercises, solve each system by substitution. 2x + 4y + z = 16 2x + 3y + 5z = 20 2x - 4y - 3z = -9 x + 6y - 8z = 21 13. 5x + 2y + 4z = 9 -3x + 2y + z = 10 4x - 3y + 5z = -3 14. 4x - 3y + 5z = 31 -x + 2y + 4z = 20 x + 5y - 2z = -29 15. 5x - 2y + 3z = 4 -4x + 6y - 7z = -1 3x + 2y - z = 4 16. 4x + 6y + 9z = 0 -5x + 2y - 6z = 3 7x - 4y + 3z = -3 For the following exercises, solve each system by Gaussian elimination. 17. 2x - y + 3z = 17 -5x + 4y - 2z = -46 2y + 5z = -7 - x + 4y = 10 2x - z = 10 19. 2x + 3y - 6z = 1 -4x - 6y + 12z = -2 x + 2y + 5z = 10 20. 4x + 6y - 2z = 8 6x + 9y - 3z = 12 -2x - 3y + z = -4 21. 2x + 3y - 4z = 5 -3x + 2y + z = 11 -x + 5y + 3z = 4 -x - 2y - 4z = -1 -12x - 6y + 6z = -12 23. x + y + z = 14 2y + 3z = -14 24. 5x - 3y + 4z = -1 -4x + 2y - 3z = 0 -x + 5y + 7z = -11 25. x + y + z = 0 2x - y + 3z = 0 x - z = 0

26. 3x + 2y - 5z = 6 5x - 4y + 3z = -12 4x + 5y-2z = 15 27. x + y + z = 0 2x - y + 3z = 0 x - z = 1/2 y - z = - 1/2 4x + z = 3 -x + 3/2 y = 5/2 29. 6x - 5y + 6z = 38 1/5 x - 1/2 y + 3/5 z = 1 -4x - 3/2 y - z = -74 30. 1/2 x - 1/5 y + 2/5 z = - 13 10 1/4 x - 2/5 y - 1/5 z = - 7 20 - 1/2 x - 3/4 y - 1/2 z = - 5/4/3 x - 1/2 y - 1/4 z = 3/4 - 1/2 x - 1/4 y - 1/2 z = 2 - 1/4 x - 3/4 y - 1/2 z = - 1/2/2 x - 1/4 y + 3/4 z = 0 1/4 x - 1 10 y + 2/5 z = -2 1/8 x + 1/5 y - 1/8 z = 2/5 x - 7/8 y + 1/2 z = 1 - 4/5 x - 3/4 y + 1/3 z = -8 - 2/5 x - 7/8 y + 1/2 z = -5/3 x - 1/8 y + 1/6 z = - 4/3 - 2/3 x - 7/8 y + 1/3 z = - 23 3 - 1/3 x - 5/8 y + 5/6 z = 0/4 x - 5/4 y + 5/2 z = -5 - 1/2 x - 5/3 y + 5/4 z = 55 12 - 1/3 x - 1/3 y + 1/3 z = 5/3 40 x + 1 60 y + 1 80 z = 1 100 - 1/2 x - 1/3 y - 1/4 z = - 1/5 3/8 x + 3 12 y + 3 16 z = 3 20 Extensions For the following exercises, solve the system for x, y, and z.
46. x + y + z = 3 x - 1 + y - 3 + z + 1 = 0 x - 2 + y + 4 + z - 3 = 2/3 47. 5x - 3y - z + 1 = 1/2 6x + y - 9 + 2z = -3 x + 8 - 4y + z = 4 - y - 1 + z + 2 = 1 x - 2 + y + 1 - z + 8 12 = 0 x + 6 - y + 2 + z + 4 = 3 + y + 2 - z - 3 = 2 x + 2 + y - 5 + z + 4 = 1 x + 6 - y - 3 + z + 1 = 9 3 + y + 3 + z + 2 = 1 4x + 3y - 2z = 11

Real-World Applications 51.
Three even numbers sum up to 108.
The smaller is half the larger and the middle number is 3/4 the larger.
What are the three numbers? 52.
Three numbers sum up to 147.
The smallest number is half the middle number, which is half the largest number.
What are the three numbers? 53.
At a family reunion, there were only blood relatives, consisting of children, parents, and grandparents, in attendance.
There were 400 people total.
There were twice as many parents as grandparents, and 50 more children than parents.
How many children, parents, and grandparents were in attendance? 54.
An animal shelter has a total of 350 animals comprised of cats, dogs, and rabbits.
If the number of rabbits is 5 less than one-half the number of cats, and there are 20 more cats than dogs, how many of each animal are at the shelter? 55.
Your roommate, Sarah, offered to buy groceries for you and your other roommate.
The total bill was $82.
She forgot to save the individual receipts but remembered that your groceries were $0.05 cheaper than half of her groceries, and that your other roommate’s groceries were $2.10 more than your groceries.
How much was each of your share of the groceries? 56.
Your roommate, John, offered to buy household supplies for you and your other roommate.
You live near the border of three states, each of which has a different sales tax.
The total amount of money spent was $100.75.
Your supplies were bought with 5% tax, John’s with 8% tax, and your third roommate’s with 9% sales tax.
The total amount of money spent without taxes is $93.50.
If your supplies before tax were $1 more than half of what your third roommate’s supplies were before tax, how much did each of you spend?
Give your answer both with and without taxes. 57.
Three coworkers work for the same employer.
Their jobs are warehouse manager, office manager, and truck driver.
The sum of the annual salaries of the warehouse manager and office manager is $82,000.
The office manager makes $4,000 more than the truck driver annually.
The annual salaries of the warehouse manager and the truck driver total $78,000.
What is the annual salary of each of the co-workers? 58.
At a carnival, $2,914.25 in receipts were taken at the end of the day.
The cost of a child’s ticket was $20.50, an adult ticket was $29.75, and a senior citizen ticket was $15.25.
There were twice as many senior citizens as adults in attendance, and 20 more children than senior citizens.
How many children, adult, and senior citizen tickets were sold? 59.
A local band sells out for their concert.
They sell all 1,175 tickets for a total purse of $28,112.50.
The tickets were priced at $20 for student tickets, $22.50 for children, and $29 for adult tickets.
If the band sold twice as many adult as children tickets, how many of each type was sold? 60.
In a bag, a child has 325 coins worth $19.50.
There were three types of coins: pennies, nickels, and dimes.
If the bag contained the same number of nickels as dimes, how many of each type of coin was in the bag? 61.
Last year, at Haven’s Pond Car Dealership, for a particular model of BMW, Jeep, and Toyota, one could purchase all three cars for a total of $140,000.
This year, due to inflation, the same cars would cost $151,830.
The cost of the BMW increased by 8%, the Jeep by 5%, and the Toyota by 12%.
If the price of last year’s Jeep was $7,000 less than the price of last year’s BMW, what was the price of each of the three cars last year? 62.
A recent college graduate took advantage of his business education and invested in three investments immediately after graduating.
He invested $80,500 into three accounts, one that paid 4% simple interest, one that paid 4% simple interest, one that paid 3 1/8 % simple interest, and one that paid 2 1/2 % simple interest.
He earned $2,670 interest at the end of one year.
If the amount of the money invested in the second account was four times the amount invested in the third account, how much was invested in each account?

63.
You inherit one million dollars.
You invest it all in three accounts for one year.
The first account pays 3% compounded annually, the second account pays 4% compounded annually, and the third account pays 2% compounded annually.
After one year, you earn $34,000 in interest.
If you invest four times the money into the account that pays 3% compared to 2%, how much did you invest in each account? 64.
You inherit one hundred thousand dollars.
You invest it all in three accounts for one year.
The first account pays 4% compounded annually, the second account pays 3% compounded annually, and the third account pays 2% compounded annually.
After one year, you earn $3,650 in interest.
If you invest five times the money in the account that pays 4% compared to 3%, how much did you invest in each account? 65.
The top three countries in oil consumption in a certain year are as follows: the United States, Japan, and China.
In millions of barrels per day, the three top countries consumed 39.8% of the world’s consumed oil.
The United States consumed 0.7% more than four times China’s consumption.
The United States consumed 5% more than triple Japan’s consumption.
What percent of the world oil consumption did the United States, Japan, and China consume?[28] 66.
The top three countries in oil production in the same year are Saudi Arabia, the United States, and Russia.
In millions of barrels per day, the top three countries produced 31.4% of the world’s produced oil.
Saudi Arabia and the United States combined for 22.1% of the world’s production, and Saudi Arabia produced 2% more oil than Russia.
What percent of the world oil production did Saudi Arabia, the United States, and Russia produce?[29] 67.
The top three sources of oil imports for the United States in the same year were Saudi Arabia, Mexico, and Canada.
The three top countries accounted for 47% of oil imports.
The United States imported 1.8% more from Saudi Arabia than they did from Mexico, and 1.7% more from Saudi Arabia than they did from Canada.
What percent of the United States oil imports were from these three countries?[30] 68.
The top three oil producers in the United States in a certain year are the Gulf of Mexico, Texas, and Alaska.
The three regions were responsible for 64% of the United States oil production.
The Gulf of Mexico and Texas combined for 47% of oil production.
Texas produced 3% more than Alaska.
What percent of United States oil production came from these regions?[31] 69.
At one time, in the United States, 398 species of animals were on the endangered species list.
The top groups were mammals, birds, and fish, which comprised 55% of the endangered species.
Birds accounted for 0.7% more than fish, and fish accounted for 1.5% more than mammals.
What percent of the endangered species came from mammals, birds, and fish? 70.
Meat consumption in the United States can be broken into three categories: red meat, poultry, and fish.
If fish makes up 4% less than one-quarter of poultry consumption, and red meat consumption is 18.2% higher than poultry consumption, what are the percentages of meat consumption?[32] 28 “Oil reserves, production and consumption in 2001,” accessed April 6, 2014, http://scaruffi.com/politics/oil.html. 29 “Oil reserves, production and consumption in 2001,” accessed April 6, 2014, http://scaruffi.com/politics/oil.html. 30 “Oil reserves, production and consumption in 2001,” accessed April 6, 2014, http://scaruffi.com/politics/oil.html. 31 “USA:
The coming global oil crisis,” accessed April 6, 2014, http://www.oilcrisis.com/us/. 32 “The United States Meat Industry at a Glance,” accessed April 6, 2014, http://www.meatami.com/ht/d/sp/i/47465/pid/47465.

## 9.3 Systems of Nonlinear Equations and Inequalities:
Two Variables

---
Halley’s Comet (Figure 1) orbits the sun about once every 75 years.
Its path can be considered to be a very elongated ellipse.
Other comets follow similar paths in space.
These orbital paths can be studied using systems of equations.
These systems, however, are different from the ones we considered in the previous section because the equations are not linear.
In this section, we will consider the intersection of a parabola and a line, a circle and a line, and a circle and an ellipse.
The methods for solving systems of nonlinear equations are similar to those for linear equations.
Solving a System of Nonlinear Equations Using Substitution A system of nonlinear equations is a system of two or more equations in two or more variables containing at least one equation that is not linear.
Recall that a linear equation can take the form Ax + By + C = 0.
Any equation that cannot be written in this form in nonlinear.
The substitution method we used for linear systems is the same method we will use for nonlinear systems.
We solve one equation for one variable and then substitute the result into the second equation to solve for another variable, and so on.
There is, however, a variation in the possible outcomes.
Intersection of a Parabola and a Line There are three possible types of solutions for a system of nonlinear equations involving a parabola and a line. possible types of solutions for points of intersection of a parabola and a line • No solution.
The line will never intersect the parabola. • One solution.
The line is tangent to the parabola and intersects the parabola at exactly one point. • Two solutions.
The line crosses on the inside of the parabola and intersects the parabola at two points.
(a) No solutions One solutions Two solutions (b) (c) x y x y x y Learning Objectives
In this section, you will:
• Solve a system of nonlinear equations using substitution.
• Solve a system of nonlinear equations using elimination.
• Graph a nonlinear inequality.
• Graph a system of nonlinear inequalities.

---
### 💡 **How To…**
Given a system of equations containing a line and a parabola, find the solution. 1.
Solve the linear equation for one of the variables. 2.
Substitute the expression obtained in step one into the parabola equation. 3.
Solve for the remaining variable. 4.
Check your solutions in both equations.

---
### 📐 **Example 1**:
Solving a System of Nonlinear Equations Representing a Parabola and a Line

Solve the system of equations.

x - y = -1

y = x² + 1

**Solution**

Solve the first equation for x and then substitute the resulting expression into the second equation.

x - y = -1

x = y - 1 Solve for x.

y = x² + 1

y = (y - 1)² + 1 Substitute expression for x. Expand the equation and set it equal to zero.

y = (y - 1)²

= (y² - 2y + 1) + 1

= y² - 2y + 2

0 = y² -3y + 2

= (y - 2)(y - 1) Solving for y gives y = 2 and y = 1.
Next, substitute each value for y into the first equation to solve for x.
Always substitute the value into the linear equation to check for extraneous solutions.

x - y = -1

x - (2) = -1

x = 1

x - (1) = -1

x = 0 The solutions are (1, 2) and (0, 1), which can be verified by substituting these (x, y) values into both of the original equations. See Figure 3. x y x - y = -1 y = x 2 + 1

Could we have substituted values for y into the second equation to solve for x in Example 1?
Yes, but because x is squared in the second equation this could give us extraneous solutions for x.
For y = 1

y = x² + 1

1 = x² + 1

x² = 0

x = ± √0 = 0 This gives us the same value as in the solution.
For y = 2

y = x² + 1

2 = x² + 1

x² = 1

x = ± √1 = ± 1 Notice that -1 is an extraneous solution.

---
### ✏️ **Try It #1**
Solve the given system of equations by substitution.

3x - y = -2

2x² - y = 0 Intersection of a Circle and a Line Just as with a parabola and a line, there are three possible outcomes when solving a system of equations representing a circle and a line. possible types of solutions for the points of intersection of a circle and a line • No solution.
The line does not intersect the circle. • One solution.
The line is tangent to the circle and intersects the circle at exactly one point. • Two solutions.
The line crosses the circle and intersects it at two points.
No solutions One solution Two solutions

---
### 💡 **How To…**
Given a system of equations containing a line and a circle, find the solution. 1.
Solve the linear equation for one of the variables. 2.
Substitute the expression obtained in step one into the equation for the circle. 3.
Solve for the remaining variable. 4.
Check your solutions in both equations.

---
### 📐 **Example 2**
Finding the Intersection of a Circle and a Line by Substitution Find the intersection of the given circle and the given line by substitution.

x² + y² = 5

y = 3x - 5

**Solution**

One of the equations has already been solved for y.
We will substitute y = 3x - 5 into the equation for the circle.

x² + (3x - 5)² = 5

x² + 9x² -30x + 25 = 5

Now, we factor and solve for x.

10(x² - 3x + 2) = 0

10(x - 2)(x - 1) = 0

x = 2

x = 1 Substitute the two x-values into the original linear equation to solve for y.

y = 3(2)-5

= 1

y = 3(1)-5

= -2 The line intersects the circle at (2, 1) and (1, -2), which can be verified by substituting these (x, y) values into both of the original equations. See Figure 5. x y y = 3x - 5 x² + y² = 5

---
### ✏️ **Try It #2**
Solve the system of nonlinear equations.

x² + y² = 10

x - 3y = -10 Solving a System of Nonlinear Equations Using Elimination We have seen that substitution is often the preferred method when a system of equations includes a linear equation and a nonlinear equation.
However, when both equations in the system have like variables of the second degree, solving them using elimination by addition is often easier than substitution.
Generally, elimination is a far simpler method when the system involves only two equations in two variables (a two-by-two system), rather than a three-by-three system, as there are fewer steps.
As an example, we will investigate the possible types of solutions when solving a system of equations representing a circle and an ellipse.

possible types of solutions for the points of intersection of a circle and an ellipse • No solution.
The circle and ellipse do not intersect.
One shape is inside the other or the circle and the ellipse are a distance away from the other. • One solution.
The circle and ellipse are tangent to each other, and intersect at exactly one point. • Two solutions.
The circle and the ellipse intersect at two points. • Three solutions.
The circle and the ellipse intersect at three points. • Four solutions.
The circle and the ellipse intersect at four points.
No solution One solution Two solutions Tree solutions Four solutions

---
### 📐 **Example 3**
Solving a System of Nonlinear Equations Representing a Circle and an Ellipse Solve the system of nonlinear equations.

x² + y² = 26 (1)

(2)

**Solution**

Let’s begin by multiplying equation (1) by -3, and adding it to equation (2).

(-3)(x² + y²) = (-3)(26)

-3x² - 3y² = - 78

After we add the two equations together, we solve for y.

y² = 1

y = ± √1 = ± 1 Substitute y = ± 1 into one of the equations and solve for x.

x² + (1)² = 26

x² + (-1)² = 26

x² + 1 = 26

x² = 25 = ± 5

x² + 1 = 26

x² = 25

x = ± √25 = ± 5 There are four solutions: (5, 1), (-5, 1), (5, -1), and (-5, -1). See Figure 7. x y

---
### ✏️ **Try It #3**
Find the solution set for the given system of nonlinear equations.

4x² + y² = 13

x² + y² = 10 Graphing a Nonlinear Inequality All of the equations in the systems that we have encountered so far have involved equalities, but we may also encounter systems that involve inequalities.
We have already learned to graph linear inequalities by graphing the corresponding equation, and then shading the region represented by the inequality symbol.
Now, we will follow similar steps to graph a nonlinear inequality so that we can learn to solve systems of nonlinear inequalities.
A nonlinear inequality is an inequality containing a nonlinear expression.
Graphing a nonlinear inequality is much like graphing a linear inequality.
Recall that when the inequality is greater than, y > a, or less than, y < a, the graph is drawn with a dashed line.
When the inequality is greater than or equal to, y ≥ a, or less than or equal to, y ≤ a, the graph is drawn with a solid line.
The graphs will create regions in the plane, and we will test each region for a solution.
If one point in the region works, the whole region works.
That is the region we shade.
See Figure 8. x y y > x² - 4 y ≥ x² - 4 y < x² - 4 y ≤ x² - 4 x y x y x y (a) (b) (c) (d)

---
### 💡 **How To…**
Given an inequality bounded by a parabola, sketch a graph. 1.
Graph the parabola as if it were an equation.
This is the boundary for the region that is the solution set. 2.
If the boundary is included in the region (the operator is ≤ or ≥ ), the parabola is graphed as a solid line. 3.
If the boundary is not included in the region (the operator is < or >), the parabola is graphed as a dashed line. 4.
Test a point in one of the regions to determine whether it satisfies the inequality statement.
If the statement is true, the solution set is the region including the point.
If the statement is false, the solution set is the region on the other side of the boundary line. 5.
Shade the region representing the solution set.

---
### 📐 **Example 4**:
Graphing an Inequality for a Parabola

Graph the inequality y > x² + 1.

**Solution**

First, graph the corresponding equation y = x² + 1.
Since y > x² + 1 has a greater than symbol, we draw the graph with a dashed line.
Then we choose points to test both inside and outside the parabola.
Let’s test the points (0, 2) and (2, 0).
One point is clearly inside the parabola and the other point is clearly outside.

y > x² + 1

2 > (0)² + 1

2 > 1 True

0 > (2)² + 1

0 > 5 False

The graph is shown in Figure 9.
We can see that the solution set consists of all points inside the parabola, but not on the graph itself. x y Graphing a System of Nonlinear Inequalities Now that we have learned to graph nonlinear inequalities, we can learn how to graph systems of nonlinear inequalities.
A system of nonlinear inequalities is a system of two or more inequalities in two or more variables containing at least one inequality that is not linear.
Graphing a system of nonlinear inequalities is similar to graphing a system of linear inequalities.
The difference is that our graph may result in more shaded regions that represent a solution than we find in a system of linear inequalities.
The solution to a nonlinear system of inequalities is the region of the graph where the shaded regions of the graph of each inequality overlap, or where the regions intersect, called the feasible region.

---
### 💡 **How To…**
Given a system of nonlinear inequalities, sketch a graph. 1.
Find the intersection points by solving the corresponding system of nonlinear equations. 2.
Graph the nonlinear equations. 3.
Find the shaded regions of each inequality. 4.
Identify the feasible region as the intersection of the shaded regions of each inequality or the set of points common to each inequality.

---
### 📐 **Example 5**:
Graphing a System of Inequalities

Graph the given system of inequalities.

x² - y ≤ 0

2x² + y ≤ 12

**Solution**

These two equations are clearly parabolas.
We can find the points of intersection by the elimination process:
Add both equations and the variable y will be eliminated.
Then we solve for x.

x² - y = 0

2x² + y = 12

x² = 4

x = ± 2 Substitute the x-values into one of the equations and solve for y.

x² - y = 0

(2)² - y = 0

4 - y = 0

y = 4

(-2)² - y = 0

4 - y = 0

y = 4

The two points of intersection are (2, 4) and (-2, 4). Notice that the equations can be rewritten as follows.

x² - y ≤ 0

x² ≤ y

y ≥ x²

2x² + y ≤ 12

y ≤ - 2x² + 12 Graph each inequality.
See Figure 10.
The feasible region is the region between the two equations bounded by 2 x² + y ≤ 12 on the top and x² - y ≤ 0 on the bottom. x y

---
### ✏️ **Try It #4**
Graph the given system of inequalities.

y ≥ x² - 1

x - y ≥ - 1 Access these online resources for additional instruction and practice with nonlinear equations.
• Solve a System of Nonlinear Equations Using Substitution (http://openstaxcollege.org/l/nonlinsub) • Solve a System of Nonlinear Equations Using Elimination (http://openstaxcollege.org/l/nonlinelim)

## 9.3 Section Exercises

---
### 9.3 Section Exercises

Verbal 1.
Explain whether a system of two nonlinear equations can have exactly two solutions.
What about exactly three?
If not, explain why not.
If so, give an example of such a system, in graph form, and explain why your choice gives two or three answers. 2.
When graphing an inequality, explain why we only need to test one point to determine whether an entire region is the solution? 3.
When you graph a system of inequalities, will there always be a feasible region?
If so, explain why.
If not, give an example of a graph of inequalities that does not have a feasible region.
Why does it not have a feasible region? 4.
If you graph a revenue and cost function, explain how to determine in what regions there is profit. 5.
If you perform your break-even analysis and there is more than one solution, explain how you would determine which x-values are profit and which are not.
Algebraic For the following exercises, solve the system of nonlinear equations using substitution. 6. x + y = 4 x² + y² = 9 7. y = x - 3 x² + y² = 9 8. y = x x² + y² = 9 9. y = - x x² + y² = 9 10. x = 2 x² - y² = 9 For the following exercises, solve the system of nonlinear equations using elimination. 4x² + 9y² = 36 12. x² + y² = 25 x² - y² = 1 13. 2x² + 4y² = 4 2x² -4y² = 25x - 10 14. y² - x² = 9 3x² + 2y² = 8 15. x² + y² + 1/y = 2x² For the following exercises, use any method to solve the system of nonlinear equations. 16. -2x² + y = -5 6x - y = 9 17. -x² + y = 2 -x + y = 2 18. x² + y² = 1 y = 20x² -1 19. x² + y² = 1 y = -x² 20. 2x³ - x² = y y = 1/2 - x (x - 6)² + y² = 1 22. x⁴ - x² = y x² + y = 0 23. 2x³ - x² = y x² + y = 0 For the following exercises, use any method to solve the nonlinear system. 24. x² + y² = 9 y = 3 - x² 25. x² - y² = 9 x = 3 26. x² - y² = 9 y = 3 27. x² - y² = 9 x - y = 0 28. -x² + y = 2 -4x + y = -1 29. -x² + y = 2 2y = - x 30. x² + y² = 25 x² - y² = 36 31. x² + y² = 1 y² = x² y² + x² = 16

33. 3x² - y² = 12 (x - 1)² + y² = 1 34. 3x² - y² = 12 (x - 1)² + y² = 4 35. 3x² - y² = 12 x² + y² = 16 36. x² - y² - 6x - 4y - 11 = 0 -x² + y² = 5 37. x² + y² - 6y = 7 x² + y = 1 38. x² + y² = 6 xy = 1 Graphical For the following exercises, graph the inequality. 39. x² + y < 9 40. x² + y² < 4 For the following exercises, graph the system of inequalities. Label all points of intersection. 41. x² + y < 1 y > 2x 42. x² + y < -5 y > 5x + 10 43. x² + y² < 25 3x² - y² > 12 44. x² - y² > -4 x² + y² < 12 45. x² + 3y² > 16 3x² - y² < 1 Extensions For the following exercises, graph the inequality. 46. y ≥ ex y ≤ ln(x) + 5 47. y ≤ -log(x) y ≤ ex For the following exercises, find the solutions to the nonlinear equations with two variables. 48. 4/x² + 1/y² = 24 5/x² - 2/y² + 4 = 0/x² - 1/y² = 8 1/x² - 6/y² = 1/8 50. x² - xy + y² -2 = 0 x + 3y = 4 51. x² - xy - 2y² -6 = 0 x² + y² = 1 52. x² + 4xy - 2y² - 6 = 0 x = y + 2 Technology For the following exercises, solve the system of inequalities. Use a calculator to graph the system to confirm the answer. y > √x 54. x² + y < 3 y > 2x Real-World Applications For the following exercises, construct a system of nonlinear equations to describe the given behavior, then solve for the requested solutions. 55. Two numbers add up to 300. One number is twice the square of the other number. What are the numbers? 56. The squares of two numbers add to 360. The second number is half the value of the first number squared. What are the numbers? 57. A laptop company has discovered their cost and revenue functions for each day: C(x) = 3x² - 10x + 200 and R(x) = -2x² + 100x + 50. If they want to make a profit, what is the range of laptops per day that they should produce? Round to the nearest number which would generate profit. 58. A cell phone company has the following cost and revenue functions: C(x) = 8x² - 600x + 21,500 and R(x) = -3x² + 480x. What is the range of cell phones they should produce each day so there is profit? round to the nearest number that generates profit.

