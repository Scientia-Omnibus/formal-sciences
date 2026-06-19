# Introduction to Calculus

## Introduction

---
The eight-time world champion and winner of six Olympic gold medals in sprinting, Usain Bolt has truly earned his nickname as the “fastest man on Earth.” Also known as the “lightning bolt,” he set the track on fire by running at a top speed of 27.79 mph—the fastest time ever recorded by a human runner.
Like the fastest land animal, a cheetah, Bolt does not run at his top speed at every instant.
How then, do we approximate his speed at any given instant?
We will find the answer to this and many related questions in this chapter.

Learning Objectives
In this section, you will:
• Understand limit notation.
• Find a limit using a graph.
• Find a limit using a table.

## 12.1 Finding Limits:
Numerical and Graphical Approaches

---
Intuitively, we know what a limit is.
A car can go only so fast and no faster.
A trash can might hold 33 gallons and no more.
It is natural for measured amounts to have limits.
What, for instance, is the limit to the height of a woman?
The tallest woman on record was Jinlian Zeng from China, who was 8 ft 1 in.[36]
Is this the limit of the height to which women can grow?
Perhaps not, but there is likely a limit that we might describe in inches if we were able to determine what it was.
To put it mathematically, the function whose input is a woman and whose output is a measured height in inches has a limit.
In this section, we will examine numerical and graphical approaches to identifying limits.
Understanding Limit Notation We have seen how a sequence can have a limit, a value that the sequence of terms moves toward as the number of terms increases.
For example, the terms of the sequence _ _ _ gets closer and closer to 0.
A sequence is one type of function, but functions that are not sequences can also have limits.
We can describe the behavior of the function as the input values get close to a specific value.
If the limit of a function f (x) = L, then as the input x gets closer and closer to a, the output y-coordinate gets closer and closer to L.
We say that the output “approaches” L. output value f (x) approaches L.
We write the equation of a limit as lim

x → a f(x) = L. This notation indicates that as x approaches a both from the left of x = a and the right of x = a, the output value approaches L. Consider the function

f (x) = x 2 - 6x - 7 x - 7 . We can factor the function as shown.

f (x) = (x - 7)(x + 1)

 x - 7 Cancel like factors in numerator and denominator.

f (x) = x + 1, x ≠ 7 Simplify. Output Y approaches L Input x approaches a x f(x) a L 36 https://en.wikipedia.org/wiki/Human_height and http://en.wikipedia.org/wiki/List_of_tallest_people

Notice that x cannot be 7, or we would be dividing by 0, so 7 is not in the domain of the original function.
In order to avoid changing the function when we simplify, we set the same condition, x ≠ 7, for the simplified function.
We can represent the function graphically as shown in Figure 2.
What happens at x = 7 is completely different from what happens at points close to x = 7 on either side.
The notation

 lim

x → 7 f (x) = 8 indicates that as the input x approaches 7 from either the left or the right, the output approaches 8.
The output can get as close to 8 as we like if the input is sufficiently near 7.
What happens at x = 7?
When x = 7, there is no corresponding output.
We write this as f (7) does not exist.
This notation indicates that 7 is not in the domain of the function.
We had already indicated this when we wrote the function as f (x) = x + 1, x ≠ 7.
Notice that the limit of a function can exist even when f (x) is not defined at x = a.
Much of our subsequent work will be determining limits of functions as x nears a, even though the output at x = a does not exist. the limit of a function A quantity L is the limit of a function f (x) as x approaches a if, as the input values of x approach a (but do not equal a), the corresponding output values of f (x) get closer to L.
Note that the value of the limit is not affected by the output value of f (x) at a.
Both a and L must be real numbers.
We write it as

 lim

x → a f (x) = L

---
### 📐 **Example 1**
Understanding the Limit of a Function For the following limit, define a, f (x), and L.

 lim

x → 2 (3x + 5) = 11

**Solution**

First, we recognize the notation of a limit.
If the limit exists, as x approaches a, we write

 lim

x → a f (x) = L. We are given

 lim

x → 2 (3x + 5) = 11 This means that a = 2, f (x) = 3x + 5, and L = 11.
Analysis Recall that y = 3x + 5 is a line with no breaks.
As the input values approach 2, the output values will get close to 11.
This may be phrased with the equation lim

x → 2 (3x + 5) = 11, which means that as x nears 2 (but is not exactly 2), the output of the function f (x) = 3x + 5 gets as close as we want to 3(2) + 5, or 11, which is the limit L, as we take values of x sufficiently near 2 but not at x = 2. x y -1 -1 -2 -2 f(x) = x²-6x-7 x-7

---
### ✏️ **Try It #1**
For the following limit, define a, f (x), and L. lim

x → 5 (2x² - 4) = 46 Understanding Left-Hand Limits and Right-Hand Limits We can approach the input of a function from either side of a value—from the left or the right.
Figure 3 shows the values of f (x) = x + 1, x ≠ 7 as described earlier and depicted in Figure 2.
Values of x approach 7 from the left (x < 7) x = 7 Values of x approach 7 from the right (x > 7) x 6.9 6.99 6.999 7.001 7.01 7.1 f (x) 7.9 7.99 7.999 Undefined 8.001 8.01 8.1

Values of output approach the limit, 8 Values of output approach the limit, 8 Values described as “from the left” are less than the input value 7 and would therefore appear to the left of the value on a number line.
The input values that approach 7 from the left in Figure 3 are 6.9, 6.99, and 6.999.
The corresponding outputs are 7.9, 7.99, and 7.999.
These values are getting closer to 8.
The limit of values of f (x) as x approaches from the left is known as the left-hand limit.
For this function, 8 is the left-hand limit of the function f (x) = x + 1, x ≠ 7 as x approaches 7.
Values described as “from the right” are greater than the input value 7 and would therefore appear to the right of the value on a number line.
The input values that approach 7 from the right in Figure 3 are 7.1, 7.01, and 7.001.
The corresponding outputs are 8.1, 8.01, and 8.001.
These values are getting closer to 8.
The limit of values of f (x) as x approaches from the right is known as the right-hand limit.
For this function, 8 is also the right-hand limit of the function f (x) = x + 1, x ≠ 7 as x approaches 7. distance of 0.1 from 7.
In other words, we need an input x within the interval 6.9 < x < 7.1 to produce an output value of f (x) within the interval 7.9 < f (x) < 8.1.
We also see that we can get output values of f (x) successively closer to 8 by selecting input values closer to 7.
In fact, we can obtain output values within any specified interval if we choose appropriate input values. observe the output can get infinitesimally close to L = 8 as x approaches 7 from the left and as x approaches 7 from the right.
To indicate the left-hand limit, we write

 lim

x → 7- f (x) = 8. To indicate the right-hand limit, we write

 lim

x → 7+ f (x) = 8. x y -1 -1 -2 -2 f(x) approaches 8 L = 8 y = f(x) a = 7 x approaches 7 from the right x approaches 7 from the lef f(x) approaches 8

left- and right-hand limits The left-hand limit of a function f (x) as x approaches a from the left is equal to L, denoted by lim

x → a- f(x) = L.
The values of f (x) can get as close to the limit L as we like by taking values of x sufficiently close to a such that x < a and x ≠ a.
The right-hand limit of a function f (x), as x approaches a from the right, is equal to L, denoted by lim

x → a+ f(x) = L.
The values of f (x) can get as close to the limit L as we like by taking values of x sufficiently close to a but greater than a.
Both a and L are real numbers.
Understanding Two-Sided Limits In the previous example, the left-hand limit and right-hand limit as x approaches a are equal.
If the left- and right-hand limits are equal, we say that the function f (x) has a two-sided limit as x approaches a.
More commonly, we simply refer to a two-sided limit as a limit.
If the left-hand limit does not equal the right-hand limit, or if one of them does not exist, we say the limit does not exist. the two-sided limit of function as x approaches a The limit of a function f (x), as x approaches a, is equal to L, that is, lim

x → a f(x) = L. if and only if lim

x → a- f(x) = lim

x → a+ f(x) In other words, the left-hand limit of a function f (x) as x approaches a is equal to the right-hand limit of the same function as x approaches a.
If such a limit exists, we refer to the limit as a two-sided limit.
Otherwise we say the limit does not exist.
Finding a Limit Using a Graph To visually determine if a limit exists as x approaches a, we observe the graph of the function when x is very near to x = a.
In Figure 5 we observe the behavior of the graph on both sides of a. x y y = f(x) x < a x > a a f (x) = L lim x a- f (x) = L lim x a+ L To determine if a left-hand limit exists, we observe the branch of the graph to the left of x = a, but near x = a.
This is where x < a.
We see that the outputs are getting close to some real number L so there is a left-hand limit.
To determine if a right-hand limit exists, observe the branch of the graph to the right of x = a, but near x = a.
This is where x > a.
We see that the outputs are getting close to some real number L, so there is a right-hand limit.
If the left-hand limit and the right-hand limit are the same, as they are in Figure 5, then we know that the function has a two-sided limit.
Normally, when we refer to a “limit,” we mean a two-sided limit, unless we call it a one-sided limit.
Finally, we can look for an output value for the function f (x) when the input value x is equal to a.
The coordinate pair of the point would be (a, f (a)).
If such a point exists, then f (a) has a value.
If the point does not exist, as in Figure 5, then we say that f (a) does not exist.

---
### 💡 **How To…**
Given a function f (x), use a graph to find the limits and a function value as x approaches a. 1.
Examine the graph to determine whether a left-hand limit exists. 2.
Examine the graph to determine whether a right-hand limit exists. 3.
If the two one-sided limits exist and are equal, then there is a two-sided limit—what we normally call a “limit.” 4.
If there is a point at x = a, then f (a) is the corresponding function value.

---
### 📐 **Example 2**
Finding a Limit Using a Graph a.
Determine the following limits and function value for the function f shown in Figure 6. i. lim

x → 2- f (x) ii. lim

x → 2+ f (x) iii. lim

x → 2 f (x) iv. f (2) b. Determine the following limits and function value for the function f shown in Figure 7. i. lim

x → 2- f (x) ii. lim

x → 2+ f (x) iii. lim

x → 2 f (x) iv. f (2) x y -2 -2 -1 -1 -3 -4 f x y f -2 -2 -1 -1 -3 -4 -5 -6

**Solution**

a.
Looking at Figure 6:

i. lim

x → 2- f (x) = 8; when x < 2, but infinitesimally close to 2, the output values get close to y = 8.

ii. lim

x → 2+ f (x) = 3; when x > 2, but infinitesimally close to 2, the output values approach y = 3.

iii. lim

x → 2 f (x) does not exist because lim

x → 2- f (x) ≠ lim

x → 2+ f (x); the left- and right-hand limits are not equal.

iv. f (2) = 3 because the graph of the function f passes through the point (2, f (2)) or (2, 3). b. Looking at Figure 7:

i. lim

x → 2- f (x) = 8; when x < 2 but infinitesimally close to 2, the output values approach y = 8.

ii. lim

x → 2- f (x) = 8; when x > 2 but infinitesimally close to 2, the output values approach y = 8.

iii. lim

x → 2 f (x) = 8 because lim

x → 2- f (x) = lim

x → 2+ f (x) = 8; the left and right-hand limits are equal.

iv. f (2) = 4 because the graph of the function f passes through the point (2, f (2)) or (2, 4).

---
### ✏️ **Try It #2**
Using the graph of the function y = f (x) shown in Figure 8, estimate the following limits. a. lim

x → 0- f (x) b. lim

x → 0+ f (x) c. lim

x → 0 f (x) x y f -2 -2 -1 -1 -3 -3 -4 -5 -6 d. lim

x → 2- f (x) e. lim

x → 2+ f (x) f. lim

x → 2 f (x) g. lim

x → 4- f (x) h. lim

x → 4+ f (x) i. lim

x → 4 f (x)

Finding a Limit Using a Table Creating a table is a way to determine limits using numeric information.
We create a table of values in which the input values of x approach a from both sides.
Then we determine if the output values get closer and closer to some real value, the limit L.
Let’s consider an example using the following function:

 lim

x → 5 ( x³ - 125/x - 5 ) To create the table, we evaluate the function at values close to x = 5.
We use some input values less than 5 and some values greater than 5 as in Figure 9.
The table values show that when x > 5 but nearing 5, the corresponding output gets close to 75.
When x > 5 but nearing 5, the corresponding output also gets close to 75. x 4.9 4.99 4.999 5.001 5.01 5.1 f (x) 73.51 Undefined 76.51

 lim

x → 5- f (x) = 75 lim

x → 5+ f (x) = 75 Because

 lim

x → 5- f (x) = 75 = lim

x → 5+ f (x), then

 lim

x → 5 f (x) = 75. Remember that f (5) does not exist.

---
### 💡 **How To…**
Given a function f, use a table to find the limit as x approaches a and the value of f (a), if it exists. 1.
Choose several input values that approach a from both the left and right.
Record them in a table. 2.
Evaluate the function at each input value.
Record them in the table. 3.
Determine if the table values indicate a left-hand limit and a right-hand limit. 4.
If the left-hand and right-hand limits exist and are equal, there is a two-sided limit. 5.
Replace x with a to find the value of f (a).

---
### 📐 **Example 3**
Finding a Limit Using a Table Numerically estimate the limit of the following expression by setting up a table of values on both sides of the limit.

 lim

x → 0 ( 5sin(x) _ 3x )

**Solution**

We can estimate the value of a limit, if it exists, by evaluating the function at values near x = 0.
We cannot find a function value for x = 0 directly because the result would have a denominator equal to 0, and thus would be undefined.

f (x) = 5sin(x) _ 3x We create Figure 10 by choosing several input values close to x = 0, with half of them less than x = 0 and half of them greater than x = 0.
Note that we need to be sure we are using radian mode.
We evaluate the function at each input value to complete the table.
The table values indicate that when x < 0 but approaching 0, the corresponding output nears 5/3 .
When x > 0 but approaching 0, the corresponding output also nears 5/3 .

x -0.1 -0.01 0.001 0.01 0.1 f (x) Undefined

 lim

x → 0- f (x) = 5/3 lim

x → 0+ f (x) = 5/3 Because

 lim

x → 0- f (x) = 5/3 = lim

x → 0+ f (x), then

 lim

x → 0- f (x) = 5/3 .
Is it possible to check our answer using a graphing utility?
Yes.
We previously used a table to find a limit of 75 for the function f (x) = x³ - 125/x - 5 as x approaches 5.
To check, we graph the function on a viewing window as shown in Figure 11.
A graphical check shows both branches of the graph of the function get close to the output 75 as x nears 5.
Furthermore, we can use the ‘trace’ feature of a graphing calculator.
By approaching x = 5 we may numerically observe the corresponding outputs getting close to 75.

---
### ✏️ **Try It #3**
Numerically estimate the limit of the following function by making a table: lim

x → 0 ( 20sin(x) _ 4x ) Is one method for determining a limit better than the other?
No.
Both methods have advantages.
Graphing allows for quick inspection.
Tables can be used when graphical utilities aren’t available, and they can be calculated to a higher precision than could be seen with an unaided eye inspecting a graph.

---
### 📐 **Example 4**
Using a Graphing Utility to Determine a Limit With the use of a graphing utility, if possible, determine the left- and right-hand limits of the following function as x approaches 0.
If the function has a limit as x approaches 0, state it.
If not, discuss why there is no limit. f (x) = 3sin ( \p(i)/(x) ) x y f -2 -1 -3 -4 -5 L = 75 a = 5

**Solution**

We can use a graphing utility to investigate the behavior of the graph close to x = 0.
Centering around x = 0, we choose two viewing windows such that the second one is zoomed in closer to x = 0 than the first one.
The result would resemble Figure 12 for [ - 2, 2] by [ - 3, 3]. x y f -2 -4 The result would resemble Figure 13 for [-0.1, 0.1] by [-3, 3]. x y -0.1 0.1 -4 The closer we get to 0, the greater the swings in the output values are.
That is not the behavior of a function with either a left-hand limit or a right-hand limit.
And if there is no left-hand limit or right-hand limit, there certainly is no limit to the function f (x) as x approaches 0.
We write lim

x → 0- ( 3sin ( \p(i)/(x) ) ) does not exist. lim

x → 0+ ( 3sin ( \p(i)/(x) ) ) does not exist. lim

x → 0 ( 3sin ( \p(i)/(x) ) ) does not exist.

---
### ✏️ **Try It #4**
Numerically estimate the following limit: lim

x → 0 ( sin ( 2/x ) ) . Access these online resources for additional instruction and practice with finding limits. • Introduction to Limits (http://openstaxcollege.org/l/introtolimits) • Formal Definition of a Limit (http://openstaxcollege.org/l/formaldeflimit)

### 12.1 Section Exercises

Verbal 1.
Explain the difference between a value at x = a and the limit as x approaches a. 2.
Explain why we say a function does not have a limit as x approaches a if, as x approaches a, the left-hand limit is not equal to the right-hand limit.
Graphical For the following exercises, estimate the functional values and the limits from the graph of the function f provided in Figure 14. x y f(x) -2 -2 -1 -1 -3 -3 -4 -4 -5 -6 -5 3. lim

x → -2- f (x) 4. lim

x → -2+ f (x) 5. lim

x → -2 f (x) 6. f (-2) 7. lim

x → -1- f (x) 8. lim

x → 1+ f (x) 9. lim

x → 1 f (x) 11. lim

x → 4- f (x) 12. lim

x → 4+ f (x) 13. lim

x → 4 f (x) For the following exercises, draw the graph of a function from the functional values and limits provided. 15. lim

x → 0- f (x) = 2, lim

x → 0+ f (x) = -3, lim

x → 2 f (x) = 2, f (0) = 4, f (2) = -1, f (-3) does not exist. 16. lim

x → 2- f (x) = 0, lim

x → 2+ = -2, lim

x → 0 f (x) = 3, f (2) = 5, f (0) 17. lim

x → 2- f (x) = 2, lim

x → 2+ = -3, lim

x → 0 f (x) = 5, f (0) = 1, f (1) = 0 18. lim

x → 3- f (x) = 0, lim

x → 3+ f (x) = 5, lim

x → 5 f (x) = 0, f (5) = 4, f (3) does not exist. 19. lim

x → 4 f (x)= 6, lim

x → 6+ f (x) = -1, lim

x → 0 f (x) = 5, f (4) = 6, f (2) = 6 20. lim

x → -3 f (x) = 2, lim

x → 1+ f (x) = -2, lim

x → 3 f (x) = - 4, f (-3) = 0, f (0) = 0 21. lim


> **x → π f (x) = π 2, lim**


> **x → -π f (x) = π/2 , lim**


x → 1- f (x) = 0, f (π ) = √2 , f (0) does not exist.
For the following exercises, use a graphing calculator to determine the limit to 5 decimal places as x approaches 0.
22. f (x) = (1 + x) 1/x 23. g (x) = (1 + x) 2/x 24. h (x) = (1 + x) 3/x 25. i(x) = (1 + x) 4/x 26. j(x) = (1 + x) 5/x 27.
Based on the pattern you observed in the exercises above, make a conjecture as to the limit of f (x) = (1 + x) 6/x , g (x) = (1 + x) 7/x , and h(x) = (1 + x) (n)/(x) .
For the following exercises, use a graphing utility to find graphical evidence to determine the left- and right-hand limits of the function given as x approaches a.
If the function has a limit as x approaches a, state it.
If not, discuss why there is no limit. 28.
(x) = { | x | - 1, if x ≠ 1

x 3, if x = 1 a = 1 29. (x) = { 1 x + 1 , if x = -2

(x + 1)², if x ≠ -2 a = -2

## 12.1 Section Exercises

---
Numeric For the following exercises, use numerical evidence to determine whether the limit exists at x = a.
If not, describe the behavior of the graph of the function near x = a.
Round answers to two decimal places.
30. f (x) = x² - 4x/16 - x 2 ; a = 4 31. f (x) = x 2 - x - 6/x 2 - 9 ; a = 3 32. f (x) = x 2 - 6x - 7/x 2 - 7x ; a = 7 33. f (x) = x 2 - 1/x 2 - 3x + 2 ; a = 1 34. f (x) = 1 - x 2/x 2 - 3x + 2 ; a = 1 35. f (x) = 10 - 10x² _ x 2 - 3x + 2 ; a = 1 36. f (x) = x/6x 2 - 5x - 6 ; a = 3/2 37. f (x) = x/4x 2 + 4x + 1 ; a = - 1/2 38. f (x) = 2/x - 4 ; a = 4 For the following exercises, use a calculator to estimate the limit by preparing a table of values.
If there is no limit, describe the behavior of the function as x approaches the given value. 39. lim

x → 0 7tanx/3x 40. lim

x → 4 x² _ x - 4 41. lim

x → 0 2sinx/4tanx For the following exercises, use a graphing utility to find numerical or graphical evidence to determine the left and right-hand limits of the function given as x approaches a.
If the function has a limit as x approaches a, state it.
If not, discuss why there is no limit. 42. lim

x → 0 ee 1/x 43. lim

x → 0 ee- 1/x 2 44. lim

x → 0 | x | _ x 45. lim

x → -1 | x + 1 | _ x + 1 46. lim

x → 5 | x - 5 | _ 5 - x 47. lim

x → -1 _ (x + 1)² 48. lim

x → 1 _ (x - 1)³ 49. lim

x → 0/1 - e 2/x 50.
Use numerical and graphical evidence to compare and contrast the limits of two functions whose formulas appear similar: f (x) = 1 - (x)/(x) and g(x) = 1 + (x)/(x) as x approaches 0.
Use a graphing utility, if possible, to determine the left- and right-hand limits of the functions f (x) and g(x) as x approaches 0.
If the functions have a limit as x approaches 0, state it.
If not, discuss why there is no limit.
Extensions 51.
According to the Theory of Relativity, the mass m of a particle depends on its velocity v.
That is m = mo where mo is the mass when the particle is at rest and c is the speed of light.
Find the limit of the mass, m, as v approaches c -. 52.
Allow the speed of light, c, to be equal to 1.0.
If the mass, m, is 1, what occurs to m as v → c?
Using the values listed in Table 1, make a conjecture as to what the mass is as v approaches 1.00. v m 0.5 1.15 0.9 2.29 0.95 3.20 0.99 7.09 0.999 22.36 √

1 - v 2/c 2 

Learning Objectives
In this section, you will:
• Find the limit of a sum, a difference, and a product.
• Find the limit of a polynomial.
• Find the limit of a power or a root.
• Find the limit of a quotient.

## 12.2 Finding Limits:
Properties of Limits

---
Consider the rational function

f (x) = x² - 6x - 7 x - 7 The function can be factored as follows:

f (x) = (x - 7)(x + 1)

 x - 7 , which gives us f (x) = x + 1, x ≠ 7.
Does this mean the function f is the same as the function g(x) = x + 1?
The answer is no.
Function f does not have x = 7 in its domain, but g does.
Graphically, we observe there is a hole in the graph of f (x) at x = 7, as shown in Figure 1 and no such hole in the graph of g(x), as shown in Figure 2. x 2 - 6x - 7 f (x) = x - 7 y x and is therefore not continuous at x = 7. y x g(x) = x + 1 So, do these two different functions also have different limits as x approaches 7?
Not necessarily.
Remember, in determining a limit of a function as x approaches a, what matters is whether the output approaches a real number as we get close to x = a.
The existence of a limit does not depend on what happens when x equals a.
Look again at Figure 1 and Figure 2.
Notice that in both graphs, as x approaches 7, the output values approach 8.
This means lim

x → 7 f (x) = lim

x → 7 g(x).
Remember that when determining a limit, the concern is what occurs near x = a, not at x = a.
In this section, we will use a variety of methods, such as rewriting functions by factoring, to evaluate the limit.
These methods will give us formal verification for what we formerly accomplished by intuition.

Finding the Limit of a Sum, a Difference, and a Product Graphing a function or exploring a table of values to determine a limit can be cumbersome and time-consuming.
When possible, it is more efficient to use the properties of limits, which is a collection of theorems for finding limits.
Knowing the properties of limits allows us to compute limits directly.
We can add, subtract, multiply, and divide the limits of functions as if we were performing the operations on the functions themselves to find the limit of the result.
Similarly, we can find the limit of a function raised to a power by raising the limit to that power.
We can also find the limit of the root of a function by taking the root of the limit.
Using these operations on limits, we can find the limits of more complex functions by finding the limits of their simpler component functions. properties of limits Let a, k, A, and B represent real numbers, and f and g be functions, such that lim

x → a f (x) = A and lim

x → a g(x) = B. For limits that exist and are finite, the properties of limits are summarized in Table 1. Constant, k lim

x → a k = k Constant times a function lim

x → a [k ⋅ f (x)] = k lim

x → a f (x) = kA Sum of functions lim

x → a [f (x) + g(x)] = lim

x → a f (x) + lim

x → a g(x) = A + B Difference of functions lim

x → a [f (x) - g(x)] = lim

x → a f (x) - lim

x → a g(x) = A - B Product of functions lim

x → a [f (x) ⋅ g(x)] = lim

x → a f (x) ⋅ lim

x → a g(x) = A ⋅ B Quotient of functions lim

x → a f (x) g(x) = lim

x → a f (x) lim

x → a g(x) = (A)/(B) , B ≠ 0 Function raised to an exponent lim

x → a[ f (x)]n = [ lim

x → ∞ f (x) ] n = An, where n is a positive integer nth root of a function, where n is a positive integer lim

x → a n √f (x) = n √lim

x → a [ f (x)] = n √A Polynomial function lim

x → a p(x) = p(a)

---
### 📐 **Example 1**:
Evaluating the Limit of a Function Algebraically

Evaluate lim

x → 3 (2x + 5).

**Solution**

 lim

x → 3(2x + 5) = lim

x → 3(2x) + lim

x → 3 (5) Sum of functions property

= 2 lim

x → 3(x) + lim

x → 3 (5) Constant times a function property

= 2(3) + 5

Evaluate

= 11

---
### ✏️ **Try It #1**
Evaluate the following limit: lim

x → -12(-2x + 2).

Finding the Limit of a Polynomial Not all functions or their limits involve simple addition, subtraction, or multiplication.
Some may include polynomials.
Recall that a polynomial is an expression consisting of the sum of two or more terms, each of which consists of a constant and a variable raised to a nonnegative integral power.
To find the limit of a polynomial function, we can find the limits of the individual terms of the function, and then add them together.
Also, the limit of a polynomial function as x approaches a is equivalent to simply evaluating the function for a.

---
### 💡 **How To…**
Given a function containing a polynomial, find its limit. 1.
Use the properties of limits to break up the polynomial into individual terms. 2.
Find the limits of the individual terms. 3.
Add the limits together. 4.
Alternatively, evaluate the function for a.

---
### 📐 **Example 2**:
Evaluating the Limit of a Function Algebraically

Evaluate lim

x → 3(5x²).

**Solution**

 lim

x → 3(5x²) = 5 lim

x → 3(x²) Constant times a function property

Function raised to an exponent property

= 45

---
### ✏️ **Try It #2**
Evaluate lim

x → 4(x³ - 5).

---
### 📐 **Example 3**:
Evaluating the Limit of a Polynomial Algebraically

Evaluate lim

x → 5(2x³ - 3x + 1).

**Solution**

 lim

x → 5(2x³ - 3x + 1) = lim

x → 5(2x³) - lim

x → 5(3x) + lim

x → 5(1) Sum of functions

= 2 lim

x → 5(x³) - 3 lim

x → 5(x) + lim

x → 5(1) Constant times a function

= 2(53) - 3(5) + 1 Function raised to an exponent

= 236 Evaluate

---
### ✏️ **Try It #3**
Evaluate the following limit: lim

x → -1(x⁴ - 4x³ + 5).
Finding the Limit of a Power or a Root When a limit includes a power or a root, we need another property to help us evaluate it.
The square of the limit of a function equals the limit of the square of the function; the same goes for higher powers.
Likewise, the square root of the limit of a function equals the limit of the square root of the function; the same holds true for higher roots.

---
### 📐 **Example 4**:
Evaluating a Limit of a Power

Evaluate lim

x → 2(3x + 1)⁵.

**Solution**

We will take the limit of the function as x approaches 2 and raise the result to the 5th power.

 lim

x → 2(3x + 1)⁵ = ( lim

x → 2(3x + 1) ) 5

= (3(2) + 1)⁵

= 75

---
### ✏️ **Try It #4**
Evaluate the following limit: lim

If we can’t directly apply the properties of a limit, for example in lim

x → 2( x² + 6x + 8 x - 2 ) , can we still determine the limit of the function as x approaches a?
Yes.
Some functions may be algebraically rearranged so that one can evaluate the limit of a simplified equivalent form of the function.
Finding the Limit of a Quotient Finding the limit of a function expressed as a quotient can be more complicated.
We often need to rewrite the function algebraically before applying the properties of a limit.
If the denominator evaluates to 0 when we apply the properties of a limit directly, we must rewrite the quotient in a different form.
One approach is to write the quotient in factored form and simplify.

---
### 💡 **How To…**
Given the limit of a function in quotient form, use factoring to evaluate it. 1.
Factor the numerator and denominator completely. 2.
Simplify by dividing any factors common to the numerator and denominator. 3.
Evaluate the resulting limit, remembering to use the correct domain.

---
### 📐 **Example 5**:
Evaluating the Limit of a Quotient by Factoring

Evaluate lim

x → 2( x² - 6x + 8 x - 2 ) .

**Solution**

Factor where possible, and simplify.

 lim

x → 2( x² - 6x + 8 x - 2 ) = lim

x → 2 ( (x - 2)(x - 4)

 x - 2 ) Factor the numerator.

= lim

x → 2( (x - 2)(x - 4)

 x - 2 ) Cancel the common factors.

= lim

x → 2(x - 4) Evaluate.

= 2 - 4 = -2 Analysis When the limit of a rational function cannot be evaluated directly, factored forms of the numerator and denominator may simplify to a result that can be evaluated.
Notice, the function

f (x) = x² - 6x + 8 x - 2 is equivalent to the function

f (x) = x - 4, x ≠ 2. Notice that the limit exists even though the function is not defined at x = 2.

---
### ✏️ **Try It #5**
Evaluate the following limit: lim

x → 7( x² - 11x + 28 7 - x ) .

---
### 📐 **Example 6**:
Evaluating the Limit of a Quotient by Finding the LCD

Evaluate lim

x → 5( 1/x - 1/5 x - 5 ) .

**Solution**

Find the LCD for the denominators of the two terms in the numerator, and convert both fractions to have the LCD as their denominator.

 lim

x → 5( 1/x - 1/5 x - 5 ) = lim

x → 5( 5x ( 1/x - 1/5 ) 5x(x - 5) ) Multiply numerator and denominator by LCD.

= lim

x → 5( 5x( 1/x ) - 5x ( 1/5 )


5x(x - 5) ) Apply distributive property.

= lim

x → 5( 5 - x 5x(x - 5) ) Simplify.

= lim

x → 5( -1(x - 5) 5x(x - 5) ) Factor the numerator

= lim

x → 5- 1/5x Cancel out like fractions

= - 1 5(5) Evaluate for x = 5

= - 1 25 

**Analysis**
When determining the limit of a rational function that has terms added or subtracted in either the numerator or denominator, the first step is to find the common denominator of the added or subtracted terms; then, convert both terms to have that denominator, or simplify the rational function by multiplying numerator and denominator by the least common denominator.
Then check to see if the resulting numerator and denominator have any common factors.

---
### ✏️ **Try It #6**
Evaluate lim

x → -5( 1/5 + 1/x 10 + 2x ) .

---
### 💡 **How To…**
Given a limit of a function containing a root, use a conjugate to evaluate. 1.
If the quotient as given is not in indeterminate ( 0/0 ) form, evaluate directly. 2.
Otherwise, rewrite the sum (or difference) of two quotients as a single quotient, using the least common denominator (LCD). 3.
If the numerator includes a root, rationalize the numerator; multiply the numerator and denominator by the conjugate of the numerator.
Recall that a ± √b are conjugates. 4.
Simplify. 5.
Evaluate the resulting limit.

---
### 📐 **Example 7**:
Evaluating a Limit Containing a Root Using a Conjugate

Evaluate lim

x → 0( √25 - x - 5/x ) .

**Solution**

 lim

x → 0( √25 - x - 5/x ) = lim

x → 0( √25 - x - 5/x ⋅ √25 - x + 5

__

√25 - x + 5 ) Multiply numerator and denominator by the conjugate.

= lim

x → 0 ( (25 - x) - 25/x( √25 - x + 5 ) ) Multiply: ( √25 - x - 5 ) ⋅ ( √25 - x + 5 ) 

= (25 - x) - 25.

= lim

x → 0 ( -(x)/(x)( √25 - x + 5 ) ) Combine like terms.

= lim

x → 0 ( -(x)/(x)( √25 - x + 5 ) ) Simplify -x x = -1.

= -1 __

√25 - 0 + 5 

Evaluate.

= -1 5 + 5 = - 1 10 Analysis When determining a limit of a function with a root as one of two terms where we cannot evaluate directly, think about multiplying the numerator and denominator by the conjugate of the terms.

---
### ✏️ **Try It #7**
Evaluate the following limit: lim

h → 0 ( √16 - h - 4 h ) .

---
### 📐 **Example 8**:
Evaluating the Limit of a Quotient of a Function by Factoring

Evaluate lim

x → 4 ( 4 - x √x - 2 ) .

**Solution**

 lim

x → 4 ( 4 - x _ √x - 2 ) = lim

x → 4 ( ( 2 + √x )( 2 - √x )

__

√x - 2

 ) Factor.

= lim

x → 4 ( ( 2 + √x )( 2 - √x )


-( 2 - √x )

 ) Factor -1 out of the denominator. Simplify.

= lim

x → 4 -( 2 + √x ) Evaluate.

= -( 2 + √4 )

= -4 Analysis Multiplying by a conjugate would expand the numerator; look instead for factors in the numerator.
Four is a perfect square so that the numerator is in the form a² - b² and may be factored as (a + b)(a -b).

---
### ✏️ **Try It #8**
Evaluate the following limit: lim

x → 3 ( x - 3 _ √x - √3 ) .

---
### 💡 **How To…**
Given a quotient with absolute values, evaluate its limit. 1.
Try factoring or finding the LCD. 2.
If the limit cannot be found, choose several values close to and on either side of the input where the function is undefined. 3.
Use the numeric evidence to estimate the limits on both sides.

---
### 📐 **Example 9**:
Evaluating the Limit of a Quotient with Absolute Values

Evaluate lim

x → 7 | x - 7 | _ x - 7 .

**Solution**

The function is undefined at x = 7, so we will try values close to 7 from the left and the right.
Left-hand limit: | 6.9 - 7 | _ 6.9 - 7 = _ 6.99 - 7 = _ Right-hand limit: | 7.1 - 7 | _ 7.1 - 7 = _ 7.01 - 7 = _ Since the left- and right-hand limits are not equal, there is no limit.

---
### ✏️ **Try It #9**
Evaluate lim

x → 6+ 6 - x _ | x - 6 | . Access the following online resource for additional instruction and practice with properties of limits. • Determine a Limit Analytically (http://openstaxcollege.org/l/limitanalytic)

## 12.2 Section Exercises

---
### 12.2 Section Exercises

Verbal 1.
Give an example of a type of function f whose limit, as x approaches a, is f (a). 2.
When direct substitution is used to evaluate the limit of a rational function as x approaches a and the result is f (a) = 0/0 , does this mean that the limit of f does not exist? 3.
What does it mean to say the limit of f (x), as x approaches c, is undefined?
Algebraic For the following exercises, evaluate the limits algebraically. 4. lim

x → 0(3) 5. lim

x → 2 ( -5(x)/(x)² - 1 ) 6. lim

x → 2( x² - 5x + 6/x + 2 ) 7. lim

x → 3( x² - 9/x - 3 ) 8. lim

x → -1( x² - 2x - 3/x + 1 ) 9. lim

x → 3/2 ( 6x² - 17x + 12/2x - 3 ) 10. lim

x → - 7/2 ( 8x² + 18x - 35/2x + 7 ) 11. lim

x → 3( x² - 9/x 2 - 5x + 6 ) 12. lim

x → -3( -7x⁴ - 21x³

__

-12x⁴ + 108x² ) 13. lim

x → 3( x² + 2x - 3/x - 3 ) 14. lim

h → 0( (3 + h)³ - 27/h ) 15. lim

h → 0( (2 - h)³ - 8/h ) 16. lim

h → 0( (h + 3)² - 9/h ) 17. lim

h → 0( √5 - h - √5/h ) 18. lim

x → 0( √3 - x - √3/x ) 19. lim

x → 9( x² - 81/3 - √x ) 20. lim

x → 1( √x - x² _ 1 - √x ) 21. lim

x → 0( x __

√1 + 2x - 1 ) 22. lim

x → 1/2 23. lim

x → 4( x³ - 64/x² - 16 ) 24. lim

x → 2-( | x - 2 | _ x - 2 ) 25. lim

x → 2+( | x - 2 | _ x - 2 ) 26. lim

x → 2( | x - 2 | _ x - 2 ) 27. lim

x → 4-( | x - 4 | _ 4 - x ) 28. lim

x → 4+( | x - 4 | _ 4 - x ) 29. lim

x → 4( | x - 4 | _ 4 - x ) 30. lim

x → 2( -8 + 6x - x²

__ x - 2 ) For the following exercise, use the given information to evaluate the limits: lim

x → c f (x) = 3, lim

x → c g(x) = 5 31. lim

x → c [ 2 f (x) + √g(x) ] 32. lim

x → c [ 3 f (x) + √g(x) ] 33. lim

x → c f (x) _ g(x) For the following exercises, evaluate the following limits. 34. lim


> **x → 2cos(π x) 35. lim**


> **x → 2sin(π x) 36. lim**


x → 2sin( \p(i)/(x) ) 37. f (x) = { 2x² + 2x + 1, x ≤ 0

x - 3, x > 0 ; lim

x → 0+ f (x) 38. f (x) = { 2x² + 2x + 1, x ≤ 0

x - 3, x > 0 ; lim

x → 0- f (x) 39. f (x) = { 2x² + 2x + 1, x ≤ 0

x - 3, x > 0 ; lim

x → 0 f (x) 40. lim

x → 4 √x + 5 - 3 x - 4 41. lim

x → 2+ ( 2x - 〚x〛 ) 42. lim

x → 2 √x + 7 - 3 x² - x - 2 43. lim

x → 3+ x 2 x 2 - 9 ( x² - 1/4/2x - 1 ) 

For the following exercises, find the average rate of change f (x + h) - f (x)

 h .
44. f (x) = x + 1 45. f (x) = 2x 2 - 1 46. f (x) = x 2 + 3x + 4 47. f (x) = x 2 + 4x - 100 48. f (x) = 3x 2 + 1 49. f (x) = cos(x) 50. f (x) = 2x 3 - 4x 51. f (x) = 1/x 52. f (x) = 1/x² 53. f (x) = √x Graphical 54.
Find an equation that could be represented by 55.
Find an equation that could be represented by 56.
What is the right-hand limit of the function as x approaches 0? 57.
What is the left-hand limit of the function as x approaches 0?
Real-World Applications 58.
The position function s(t) = -16t 2 + 144t gives the position of a projectile as a function of time.
Find the average velocity (average rate of change) on the interval [1, 2] . 59.
The height of a projectile is given by s(t) = -64t 2 + 192t Find the average rate of change of the height from t = 1 second to t = 1.5 seconds. 60.
The amount of money in an account after t years compounded continuously at 4.25% interest is given by the formula A = A⁰ e 0.0425t, where A⁰ is the initial amount invested.
Find the average rate of change of the balance of the account from t = 1 year to t = 2 years if the initial amount invested is $1,000.00. --1-1 -2 -3 -3 -4 -4 -5 -5 x y --1-1 -2 -3 -3 -4 -4 -5 -5 x y x y -1-1 -2 -2 -3 -3 -4 -4 -5 -5 x y -1-1 -2 -2 -3 -3 -4 -4 -5 -5

