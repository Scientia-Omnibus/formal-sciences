# Introduction to Calculus

## 12.3 Continuity

---
Learning Objectives
In this section, you will:
• Determine whether a function is continuous at a number.
• Determine the numbers for which a function is discontinuous.
• Determine whether a function is continuous.
Arizona is known for its dry heat.
On a particular day, the temperature might rise as high as 118° F and drop down only to a brisk 95° F.
Figure 1 shows the function T, where the output of T(x) is the temperature in Fahrenheit degrees and the input x is the time of day, using a 24-hour clock on a particular summer day.
When we analyze this graph, we notice a specific characteristic.
There are no breaks in the graph.
We could trace the graph without picking up our pencil.
This single observation tells us a great deal about the function.
In this section, we will investigate functions with and without breaks.
Determining Whether a Function Is Continuous at a Number Let’s consider a specific example of temperature in terms of date and location, such as June 27, 2013, in Phoenix, AZ.
The graph in Figure 1 indicates that, at 2 a.m., the temperature was 96° F.
By 2 p.m. the temperature had risen to 116° F, and by 4 p.m. it was 118° F.
Sometime between 2 a.m. and 4 p.m., the temperature outside must have been exactly 110.5° F.
In fact, any temperature between 96° F and 118° F occurred at some point that day.
This means all real numbers in the output between 96° F and 118° F are generated at some point by the function according to the intermediate value theorem, Look again at Figure 1.
There are no breaks in the function’s graph for this 24-hour period.
At no point did the temperature cease to exist, nor was there a point at which the temperature jumped instantaneously by several degrees.
A function that has no holes or breaks in its graph is known as a continuous function.
Temperature as a function of time is an example of a continuous function.
If temperature represents a continuous function, what kind of function would not be continuous?
Consider an example of dollars expressed as a function of hours of parking.
Let’s create the function D, where D(x) is the output representing cost in dollars for parking x number of hours.
See Figure 2.
Suppose a parking garage charges $4.00 per hour or fraction of an hour, with a $25 per day maximum charge.
Park for two hours and five minutes and the charge is $12.
Park an additional hour and the charge is $16.
We can never be charged $13, $14, or $15.
There are real numbers between 12 and 16 that the function never outputs.
There are breaks in the function’s graph for this 24-hour period, points at which the price of parking jumps instantaneously by several dollars.
Temperature Time, Hours Since Midnight

A function that remains level for an interval and then jumps instantaneously to a higher value is called a stepwise function.
This function is an example.
A function that has any hole or break in its graph is known as a discontinuous function.
A stepwise function, such as parking-garage charges as a function of hours parked, is an example of a discontinuous function.
So how can we decide if a function is continuous at a particular number?
We can check three different conditions.
Let’s use the function y = f (x) represented in Figure 3 as an example.
Condition 1 According to Condition 1, the function f (a) defined at x = a must exist.
In other words, there is a y-coordinate at x = a as in Figure 4.
Condition 2 According to Condition 2, at x = a the limit, written lim

x → a f (x), must exist.
This means that at x = a the left-hand limit must equal the right-hand limit.
Notice as the graph of f in Figure 3 approaches x = a from the left and right, the same y-coordinate is approached.
Therefore, Condition 2 is satisfied.
However, there could still be a hole in the graph at x = a.
Condition 3 According to Condition 3, the corresponding y coordinate at x = a fills in the hole in the graph of f.
This is written lim

x → a f (x) = f (a).
Satisfying all three conditions means that the function is continuous.
All three conditions are satisfied for the function represented in Figure 5 so the function is continuous as x = a.
Dollars Hours Parked a x y f f(a) a x y f

condition or conditions that fail. f(a) a x y f a x y f f(a) a x y f f(a) a x y f

definition of continuity A function f (x) is continuous at x = a provided all three of the following conditions hold true: • Condition 1: f (a) exists. • Condition 2: lim

x → a f (x) exists at x = a. • Condition 3: lim

x → a f (x) = f (a).
If a function f (x) is not continuous at x = a, the function is discontinuous at x = a.
Identifying a Jump Discontinuity Discontinuity can occur in different ways.
We saw in the previous section that a function could have a left-hand limit and a right-hand limit even if they are not equal.
If the left- and right-hand limits exist but are different, the graph “jumps” at x = a.
The function is said to have a jump discontinuity.
As an example, look at the graph of the function y = f (x) in Figure 10.
Notice as x approaches a how the output approaches different values from the left and from the right. jump discontinuity A function f (x) has a jump discontinuity at x = a if the left- and right-hand limits both exist but are not equal: lim

x → a- f (x) ≠ lim

x → a+ f (x).
Identifying Removable Discontinuity Some functions have a discontinuity, but it is possible to redefine the function at that point to make it continuous.
This type of function is said to have a removable discontinuity.
Let’s look at the function y = f (x) represented by the graph in Figure 11.
The function has a limit.
However, there is a hole at x = a.
The hole can be filled by extending the domain to include the input x = a and defining the corresponding output of the function at that value as the limit of the function at x = a. f(a) a x y f f(a) a x y f

removable discontinuity A function f (x) has a removable discontinuity at x = a if the limit, lim

x → a f (x), exists, but either 1. f (a) does not exist or 2. f (a), the value of the function at x = a does not equal the limit, f (a) ≠ lim

x → a f (x).

---
### 📐 **Example 1**:
Identifying Discontinuities

Identify all discontinuities for the following functions as either a jump or a removable discontinuity. a. f (x) = x² - 2x - 15 x - 5 b. g(x) = { x + 1, x < 2

-x, x ≥ 2 

**Solution**

a. Notice that the function is defined everywhere except at x = 5. Thus, f (5) does not exist, Condition 2 is not satisfied. Since Condition 1 is satisfied, the limit as x approaches 5 is 8, and Condition 2 is not satisfied. This means there is a removable discontinuity at x = 5. b. Condition 2 is satisfied because g(2) = - 2. Notice that the function is a piecewise function, and for each piece, the function is defined everywhere on its domain. Let’s examine Condition 1 by determining the left- and right-hand limits as x approaches 2. Left-hand limit: lim

x → 2- (x + 1) = 2 + 1 = 3. The left-hand limit exists. Right-hand limit: lim

x → 2+ (-x) = - 2. The right-hand limit exists. But lim

x → 2- f (x) ≠ lim

x → 2+ f (x). So, lim

x → 2 f (x) does not exist, and Condition 2 fails: There is no removable discontinuity.
However, since both left- and right-hand limits exist but are not equal, the conditions are satisfied for a jump discontinuity at x = 2.

---
### ✏️ **Try It #1**
Identify all discontinuities for the following functions as either a jump or a removable discontinuity. a. f (x) = x² - 6x x - 6 b. g(x) = { √x , 0 ≤ x < 4

2x, x ≥ 4

 a x y f

### Recognizing Continuous and Discontinuous Real-Number Functions

Many of the functions we have encountered in earlier chapters are continuous everywhere.
They never have a hole in them, and they never jump from one value to the next.
For all of these functions, the limit of f (x) as x approaches a is the same as the value of f (x) when x = a.
So lim

x → a f (x) = f (a).
There are some functions that are continuous everywhere and some that are only continuous where they are defined on their domain because they are not defined for all real numbers. examples of continuous functions The following functions are continuous everywhere: Polynomial functions Ex: f (x) = x 4 - 9x 2 Exponential functions Ex: f (x) = 4x + 2 - 5 Sine functions Ex: f (x) = sin(2x) - 4 Cosine functions Ex: f (x) = - cos ( x + π/3 ) The following functions are continuous everywhere they are defined on their domain: Logarithmic functions Ex: f (x) = 2ln(x) , x > 0 Tangent functions Ex: f (x) = tan(x) + 2, x ≠ π/2 + kπ , k is an integer Rational functions Ex: f (x) = x 2 - 25 x - 7 , x ≠ 7

---
### 💡 **How To…**
Given a function f (x), determine if the function is continuous at x = a. 1. Check Condition 1: f (a) exists. 2. Check Condition 2: lim

x → a f (x) exists at x = a. 3. Check Condition 3: lim

x → a f (x) = f (a). 4. If all three conditions are satisfied, the function is continuous at x = a. If any one of the conditions is not satisfied, the function is not continuous at x = a.

---
### 📐 **Example 2**:
Determining Whether a Piecewise Function is Continuous at a Given Number

Determine whether the function f (x) = { 4x, x ≤ 3

8 + x, x > 3 is continuous at a. x = 3 b. x = 8/3

**Solution**

To determine if the function f is continuous at x = a, we will determine if the three conditions of continuity are satisfied at x = a. a.
Condition 1: Does f (a) exist? f (3) = 4(3) = 12 ⇒ Condition 1 is satisfied.

Condition 2:
Does lim

x → 3 f (x) exist? To the left of x = 3, f (x) = 4x; to the right of x = 3, f (x) = 8 + x. We need to evaluate the left- and right-hand limits as x approaches 1. • Left-hand limit: lim

x → 3- f (x) = lim

x → 3- 4(3) = 12 • Right-hand limit: lim

x → 3+ f (x) = lim

x → 3+ (8 + x) = 8 + 3 = 11 Because lim

x → 1- f (x) ≠ lim

x → 1+ f (x), lim

x → 1 f (x) does not exist. ⇒ Condition 2 fails.
There is no need to proceed further.
Condition 2 fails at x = 3.
If any of the conditions of continuity are not satisfied at x = 3, the function f (x) is not continuous at x = 3. b. x = 8/3 Condition 1: Does f ( 8/3 ) exist? f ( 8/3 ) = 4 ( 8/3 ) = 32/3 ⇒ Condition 1 is satisfied.
Condition 2: Does lim

x → 8/3 f (x) exist? To the left of x = 8/3 f (x) = 4x; to the right of x = 8/3 f (x) = 8 + x. We need to evaluate the left- and right-hand limits as x approaches 8/3 . • Left-hand limit: lim

x → 8/3 - f (x) = lim

x → 8/3 - 4( 8/3 ) = 32/3 • Right-hand limit: lim

x → 8/3 + f (x) = lim

x → 8/3 + (8 + x) = 8 + 8/3 = 32/3 Because lim

x → 8/3 f (x) exists, ⇒ Condition 2 is satisfied. Condition 3: Is f ( 8/3 ) = lim

x → 8/3 f (x)? f ( 32/3 ) = 32/3 lim

x → 8/3 f (x) ⇒ Condition 3 is satisfied. Because all three conditions of continuity are satisfied at x = 8/3 , the function f (x) is continuous at x = 8/3 .

---
### ✏️ **Try It #2**
Determine whether the function f (x) = { 1/x , x ≤ 2

9x - 11.5, x > 2 is continuous at x = 2.

---
### 📐 **Example 3**:
Determining Whether a Rational Function is Continuous at a Given Number

Determine whether the function f (x) = x² - 25/x - 5 is continuous at x = 5.

**Solution**

To determine if the function f is continuous at x = 5, we will determine if the three conditions of continuity are satisfied at x = 5.

Condition 1:

f (5) does not exist.

⇒ Condition 1 fails.
There is no need to proceed further.
Condition 2 fails at x = 5.
If any of the conditions of continuity are not satisfied at x = 5, the function f is not continuous at x = 5.
Analysis See Figure 12.
Notice that for Condition 2 we have

 lim

x → 5 x² - 25 x - 5 = lim

x → 3 (x - 5)(x + 5)

 x - 5 

= lim

x → 5(x + 5)

= 5 + 5 = 10 ⇒ Condition 2 is satisfied.
At x = 5, there exists a removable discontinuity.
See Figure 12.

---
### ✏️ **Try It #3**
Determine whether the function f (x) = 9 - x² x² - 3x is continuous at x = 3.
If not, state the type of discontinuity.
Determining the Input Values for Which a Function Is Discontinuous Now that we can identify continuous functions, jump discontinuities, and removable discontinuities, we will look at more complex functions to find discontinuities.
Here, we will analyze a piecewise function to determine if any real numbers exist where the function is not continuous.
A piecewise function may have discontinuities at the boundary points of the function as well as within the functions that make it up.
To determine the real numbers for which a piecewise function composed of polynomial functions is not continuous, recall that polynomial functions themselves are continuous on the set of real numbers.
Any discontinuity would be at the boundary points.
So we need to explore the three conditions of continuity at the boundary points of the piecewise function.

---
### 💡 **How To…**
Given a piecewise function, determine whether it is continuous at the boundary points. 1.
For each boundary point a of the piecewise function, determine the left- and right-hand limits as x approaches a, as well as the function value at a. x y f

2. Check each condition for each value to determine if all three conditions are satisfied. 3. Determine whether each value satisfies condition 1: f (a) exists. 4. Determine whether each value satisfies condition 2: lim

x → a f (x) exists. 5. Determine whether each value satisfies condition 3: lim

x → a f (x) = f (a). 6. If all three conditions are satisfied, the function is continuous at x = a. If any one of the conditions fails, the function is not continuous at x = a.

---
### 📐 **Example 4**
Determining the Input Values for Which a Piecewise Function Is Discontinuous Determine whether the function f is discontinuous for any real numbers.

f (x) = { x + 1, x < 2

3, 2 ≤ x < 4

x² - 11, x ≥ 4

**Solution**

The piecewise function is defined by three functions, which are all polynomial functions, f (x) = x + 1 on x < 2, f (x) = 3 on 2 ≤ x < 4, and f (x) = x² - 5 on x ≥ 4.
Polynomial functions are continuous everywhere.
Any discontinuities would be at the boundary points, x = 2 and x = 4.
At x = 2, let us check the three conditions of continuity.
Condition 1:

f (2) = 3 ⇒ Condition 1 is satisfied. Condition 2: Because a different function defines the output left and right of x = 2, does

 lim

x → 2- f (x) = lim

x → 2+ f (x)? • Left-hand limit: lim

x → 2- f (x) = lim

x → 2- (x + 1) = 2 + 1 = 3 • Right-hand limit: lim

x → 2+ f (x) = lim

x → 2+ 3 = 3 Because 3 = 3, lim

x → 2- f (x) = lim

x → 2+ f (x) ⇒ Condition 2 is satisfied. Condition 3:

 lim

x → 2 f (x) = 3 = f (2) ⇒ Condition 3 is satisfied.
Because all three conditions are satisfied at x = 2, the function f (x) is continuous at x = 2.
At x = 4, let us check the three conditions of continuity.
Condition 2: Because a different function defines the output left and right of x = 4, does lim

x → 4- f (x) = lim

x → 4+ f (x)? • Left-hand limit: lim

x → 4- f (x) = lim

x → 4- 3 = 3 • Right-hand limit: lim

x → 4+ f (x) = lim

x → 4+(x² - 11) = 42 - 11 = 5 Because 3 ≠ 5, lim

x → 4- f (x) ≠ lim

x → 4+ f (x), so lim

x → 4 f (x) does not exist. ⇒ Condition 2 fails. Because one of the three conditions does not hold at x = 4, the function f (x) is discontinuous at x = 4.

Analysis See Figure 13.
At x = 4, there exists a jump discontinuity.
Notice that the function is continuous at x = 2. x y f -1-1 -2 -2 -3 -4 -5

---
### ✏️ **Try It #4**
Determine where the function f (x) = π x/4 , x < 2 \p(i)/(x) , 2 ≤ x ≤ 6 2π x, x > 6 is discontinuous.
Determining Whether a Function Is Continuous To determine whether a piecewise function is continuous or discontinuous, in addition to checking the boundary points, we must also check whether each of the functions that make up the piecewise function is continuous.

---
### 💡 **How To…**
Given a piecewise function, determine whether it is continuous. 1.
Determine whether each component function of the piecewise function is continuous.
If there are discontinuities, do they occur within the domain where that component function is applied? 2.
For each boundary point x = a of the piecewise function, determine if each of the three conditions hold.

---
### 📐 **Example 5**:
Determining Whether a Piecewise Function Is Continuous

Determine whether the function below is continuous. If it is not, state the location and type of each discontinuity. f (x) = { sin(x), x < 0

x 3, x > 0

**Solution**

The two functions composing this piecewise function are f (x) = sin(x) on x < 0 and f (x) = x 3 on x > 0.
The sine function and all polynomial functions are continuous everywhere.
Any discontinuities would be at the boundary point, At x = 0, let us check the three conditions of continuity.
Condition 1: f (0) does not exist. ⇒ Condition 1 fails.
Because all three conditions are not satisfied at x = 0, the function f (x) is discontinuous at x = 0.

Analysis See Figure 14.
There exists a removable discontinuity at x = 0; lim

x → 0 f (x) = 0, thus the limit exists and is finite, but f (a) does not exist. Access these online resources for additional instruction and practice with continuity. • Continuity at a Point (http://openstaxcollege.org/l/continuitypoint) • Continuity at a Point: Concept Check (http://openstaxcollege.org/l/contconcept) x y f(x) = x³ f(x) = sin(x) -1-1 -2 -2 -3 -3 -4 -4 -5 -6 -5 -6

### 12.3 Section Exercises

Verbal 1.
State in your own words what it means for a function f to be continuous at x = c. 2.
State in your own words what it means for a function to be continuous on the interval (a, b).
Algebraic For the following exercises, determine why the function f is discontinuous at a given point a on the graph.
State which condition fails. 3. f (x) = ln | x + 3 |, a = - 3 4. f (x) = ln | 5x - 2 |, a = 2/5 5. f (x) = x² - 16/x + 4 , a = -4 6. f (x) = x² - 16(x)/(x) , a = 0 7. f (x) = { x, x ≠ 3

2x, x = 3 a = 3 8. f (x) = { 5, x ≠ 0

3, x = 0 a = 0 9. f (x) = { 1 2 - x , x ≠ 2

3, x = 2 a = 2 10. f (x) = { 1 x + 6 , x = - 6

x², x ≠ -6 a = -6 11. f (x) = { 3 + x, x < 1

x, x = 1

x², x > 1 a = 1 12. f (x) = { 3 - x, x < 1

x, x = 1

2x², x > 1 a = 1 13. f (x) = { 3 + 2x, x < 1

x, x = 1

-x², x > 1 a = 1 14. f (x) = { x², x < - 2

2x + 1, x = - 2

x³, x > - 2 a = -2 15. f (x) = { x² - 9 x + 3 , x < -3

x - 9, x = -3

 1/x , x > -3 a = -3 16. f (x) = { x² - 9 x + 3 , x < -3

x - 9, x = -3

-6, x > -3 a = 3 17. f (x) = x² - 4/x - 2 , a = 2 18. f (x) = __

x² - 10x + 25 , a = 5 19. f (x) = x³ - 9(x)/(x)² + 11x + 24 , a = -3 20. f (x) = x³ - 27/x² - 3x , a = 3 21. f (x) = x _ | x | , a = 0 22. f (x) = 2| x + 2 | _ x + 2 , a = -2 For the following exercises, determine whether or not the given function f is continuous everywhere.
If it is continuous everywhere it is defined, state for what range it is continuous.
If it is discontinuous, state where it is discontinuous.
23. f (x) = x³ - 2x - 15 24. f (x) = x² - 2x - 15 x - 5 25. f (x) = 2 ⋅ 3x + 4 26. f (x) = -sin(3x) 27. f (x) = | x - 2 | x² - 2x 28. f (x) = tan(x) + 2 29. f (x) = 2x + 5/x 30. f (x) = log² (x)

## 12.3 Section Exercises

---
31. f (x) = ln x² 32. f (x) = e 2x 33. f (x) = √x - 4 34. f (x) = sec(x) - 3.
35. f (x) = x² + sin(x) 36. Determine the values of b and c such that the following function is continuous on the entire real number line. f (x) = { x + 1, 1 < x < 3

x² + bx + c, | x - 2 | ≥ 1 Graphical For the following exercises, refer to Figure 15.
Each square represents one square unit.
For each value of a, determine which of the three conditions of continuity are satisfied at x = a and which are not. x y For the following exercises, use a graphing utility to graph the function f (x) = sin ( 12\p(i)/(x) ) as in Figure 16.
Set the x-axis a short distance before and after 0 to illustrate the point of discontinuity. x y -5 -5 -10 -10 40.
Which conditions for continuity fail at the point of discontinuity? 41.
Evaluate f (0). 42.
Solve for x if f (x) = 0. 43.
What is the domain of f (x)?
For the following exercises, consider the function shown in Figure 17. x y -2 -2 -1 -1 -3 -3 -4 -4 -5 -6 -5 44.
At what x-coordinates is the function discontinuous? 45.
What condition of continuity is violated at these points?

46. Consider the function shown in Figure 18. At what x-coordinates is the function discontinuous? What condition(s) of continuity were violated? 47. Construct a function that passes through the origin with a constant slope of 1, with removable discontinuities at x = -7 and x = 1. 48. The function f (x) = x 3 - 1/x - 1 is graphed in Figure 19. It appears to be continuous on the interval [-3, 3], but there is an x-value on that interval at which the function is discontinuous. Determine the value of x at which the function is discontinuous, and explain the pitfall of utilizing technology when considering continuity of a function by examining its graph. 49. Find the limit lim

x → 1 f (x) and determine if the following function is continuous at x = 1: f (x) = { x 2 + 4 x ≠ 1

2 x = 1 50. The graph of f (x) = sin(2x) _ x is shown in at x = 0? Why or why not? -0.5 -0.5 0.5 0.5 1.0 1.5 2.0 2.5 1.5 2.5 3.5 4.5 -2.5 -3.5 -4.5 -3 -4 -1.0 -2 y x x y x y

## 12.4 Derivatives

---
Learning Objectives
In this section, you will:
• Find the derivative of a function.
• Find instantaneous rates of change.
• Find an equation of the tangent line to the graph of a function at a point.
• Find the instantaneous velocity of a particle.
The average teen in the United States opens a refrigerator door an estimated 25 times per day.
Supposedly, this average is up from 10 years ago when the average teenager opened a refrigerator door 20 times per day.[37]
It is estimated that a television is on in a home 6.75 hours per day, whereas parents spend an estimated 5.5 minutes per day having a meaningful conversation with their children.
These averages, too, are not the same as they were 10 years ago, when the television was on an estimated 6 hours per day in the typical household, and parents spent 12 minutes per day in meaningful conversation with their kids.
What do these scenarios have in common?
The functions representing them have changed over time.
In this section, we will consider methods of computing such changes over time.
Finding the Average Rate of Change of a Function The functions describing the examples above involve a change over time.
Change divided by time is one example of a rate.
The rates of change in the previous examples are each different.
In other words, some changed faster than others.
If we were to graph the functions, we could compare the rates by determining the slopes of the graphs.
A tangent line to a curve is a line that intersects the curve at only a single point but does not cross it there.
(The tangent line may intersect the curve at another point away from the point of interest.) If we zoom in on a curve at that point, the curve appears linear, and the slope of the curve at that point is close to the slope of the tangent line at that point.
• slope at x = -2 is 8 • slope at x = -1 is –1 • slope at x = 2 is 8 Let’s imagine a point on the curve of function f at x = a as shown in Figure 2.
The coordinates of the point are (a, f (a)).
Connect this point with a second point on the curve a little to the right of x = a, with an x-value increased by some small real number h.
The coordinates of this second point are (a + h, f (a + h)) for some positive-value h. 37 http://www.csun.edu/science/health/docs/tv&health.html Source provided. x y -1-1 -2 -2 -3 -3 -4 -4 -5 -5 m = -1 f(x) = x³ - 4x m = 8 m = 8

We can calculate the slope of the line connecting the two points (a, f (a)) and (a + h, f (a + h)), called a secant line, by applying the slope formula, slope = change in y change in x .
We use the notation msec to represent the slope of the secant line connecting two points.

msec = f (a + h) - f (a)


(a + h) - (a) 

= f (a + h) - f (a)

__

a + h - a The slope msec equals the average rate of change between two points (a, f (a)) and (a + h, f (a + h)).

msec = f (a + h) - f (a)

 h the average rate of change between two points on a curve The average rate of change (AROC) between two points (a, f (a)) and (a + h, f (a + h)) on the curve of f is the slope of the line connecting the two points and is given by

AROC = f (a + h) - f (a)

 h 

---
### 📐 **Example 1**:
Finding the Average Rate of Change

Find the average rate of change connecting the points (2, -6) and (-1, 5).

**Solution**

We know the average rate of change connecting two points may be given by

AROC = f (a + h) - f (a)

 h .
If one point is (2, - 6), or (2, f (2)), then f (2) = -6.
The value h is the displacement from 2 to -1, which equals -1 - 2 = -3.
For the other point, f (a + h) is the y-coordinate at a + h, which is 2 + (-3) or -1, so f (a + h) = f (-1) = 5.

AROC = f (a + h) - f (a)

 h 

= 5 - (-6) -3 

= 11 -3 

= - 11 3 f(a) y x a a + h f(a + h) (a, f(a + h)) h f(a + h) (a, f(a)) f

---
### ✏️ **Try It #1**
Find the average rate of change connecting the points (-5, 1.5) and ( - 2.5, 9).
Understanding the Instantaneous Rate of Change Now that we can find the average rate of change, suppose we make h in Figure 2 smaller and smaller.
Then a + h will approach a as h gets smaller, getting closer and closer to 0.
Likewise, the second point (a + h, f (a + h)) will approach the first point, (a, f (a)).
As a consequence, the connecting line between the two points, called the secant line, will get closer and closer to being a tangent to the function at x = a, and the slope of the secant line will get closer and closer to the slope of the tangent at x = a.
See Figure 3.
Because we are looking for the slope of the tangent at x = a, we can think of the measure of the slope of the curve of a function f at a given point as the rate of change at a particular instant.
We call this slope the instantaneous rate of change, or the derivative of the function at x = a.
Both can be found by finding the limit of the slope of a line connecting the point at x = a with a second point infinitesimally close along the curve.
For a function f both the instantaneous rate of change of the function and the derivative of the function at x = a are written as f ′(a), and we can define them as a two-sided limit that has the same value whether approached from the left or the right. f ′(a) = lim

h → 0 f (a + h) - f (a)

 h The expression by which the limit is found is known as the difference quotient. definition of instantaneous rate of change and derivative The derivative, or instantaneous rate of change, of a function f at x = a, is given by f ′(a) = lim

h → 0 f (a + h) - f (a)

 h The expression f (a + h) - f (a)

 h is called the difference quotient.
We use the difference quotient to evaluate the limit of the rate of change of the function as h approaches 0.
Derivatives: Interpretations and Notation The derivative of a function can be interpreted in different ways.
It can be observed as the behavior of a graph of the function or calculated as a numerical rate of change of the function.
• The derivative of a function f (x) at a point x = a is the slope of the tangent line to the curve f (x) at x = a.
The derivative of f (x) at x = a is written f ′(a).
• The derivative f ′(a) measures how the curve changes at the point (a, f (a)).
• The derivative f ′(a) may be thought of as the instantaneous rate of change of the function f (x) at x = a.
• If a function measures distance as a function of time, then the derivative measures the instantaneous velocity at time t = a. x y a f(a) P = (a, f(a)) f Q¹ Q² Secant Line P to Q¹ Tangent Line at x = a Secant Line P to Q²

notations for the derivative The equation of the derivative of a function f (x) is written as y′ = f ′(x), where y = f (x).
The notation f ′(x) is read as “f prime of x.” Alternate notations for the derivative include the following:

f ′(x) = y′ = dy dx = df dx = d dx f (x) = Df (x) The expression f ′(x) is now a function of x ; this function gives the slope of the curve y = f (x) at any value of x.
The derivative of a function f (x) at a point x = a is denoted f ′(a).

---
### 💡 **How To…**
Given a function f, find the derivative by applying the definition of the derivative. 1. Calculate f (a + h). 2. Calculate f (a). 3. Substitute and simplify f (a + h) - f (a)

 h . 4. Evaluate the limit if it exists: f ′(a) = lim

h → 0 f (a + h) - f (a)

 h .

---
### 📐 **Example 2**
Finding the Derivative of a Polynomial Function Find the derivative of the function f (x) = x 2 - 3x + 5 at x = a.

**Solution**

We have:

f ′(a) = lim

h → 0 f (a + h) - f (a)

 h Definition of a derivative Substitute f (a + h) = (a + h)² - 3(a + h) + 5 and f (a) = a² - 3a + 5.

f ′(a) = lim

h → 0 (a + h)(a + h) - 3(a + h) + 5 - (a² - 3a + 5)


h 

= lim

h → 0 a² + 2ah + h² - 3a - 3h + 5 - a² + 3a - 5


h Evaluate to remove parentheses.

= lim

h → 0 a² + 2ah + h² -3a - 3h + 5 -a² + 3a -5


h Simplify.

= lim

h → 0 2ah + h² - 3h

 h 

= lim

h → 0 h(2a + h - 3)

 h Factor out an h.

= 2a + 0 - 3 Evaluate the limit.

= 2a - 3

---
### ✏️ **Try It #2**
Find the derivative of the function f (x) = 3x² + 7x at x = a.
Finding Derivatives of Rational Functions To find the derivative of a rational function, we will sometimes simplify the expression using algebraic techniques we have already learned.

---
### 📐 **Example 3**
Finding the Derivative of a Rational Function Find the derivative of the function f (x) = 3 + x 2 - x at x = a.

**Solution**

f ′(a) = lim

h → 0 f (a + h) - f (a)

 h 

= lim

h → 0 3 + (a + h) 2 - (a + h) - ( 3 + a 2 - a ) 

 h Substitute f (a + h) and f (a).

= lim

h → 0 (2 - (a + h))(2 - a)[ 3 + (a + h) 2 - (a + h) - ( 3 + a 2 - a ) ] 


(2 - (a + h))(2 - a)(h) Multiply numerator and denominator by (2 - (a + h))(2 - a).

= lim

h → 0 (2 - (a + h))(2 - a)( 3 + (a + h) (2 - (a + h)) ) - (2 - (a + h))(2 - a)( 3 + a 2 - a ) 


(2 - (a + h))(2 - a)(h)

 Distribute.

= lim

h → 0 6 - 3a + 2a - a² + 2h - ah - 6 + 3a + 3h - 2a + a² + ah


(2 - (a + h))(2 - a)(h) Multiply.

= lim

h → 0 5h 

(2 - (a + h))(2 - a)(h) Combine like terms.

= lim

h → 0 

(2 - (a + h))(2 - a) Cancel like factors.

= 

(2 - (a + 0))(2 - a) = 

(2 - a)(2 - a) = (2 - a)² Evaluate the limit.

---
### ✏️ **Try It #3**
Find the derivative of the function f (x) = 10x + 11 5x + 4 at x = a.
Finding Derivatives of Functions with Roots To find derivatives of functions with roots, we use the methods we have learned to find limits of functions with roots, including multiplying by a conjugate.

---
### 📐 **Example 4**
Finding the Derivative of a Function with a Root Find the derivative of the function f (x) = 4√x at x = 36.

**Solution**

We have

f ′(a) = lim

h → 0 f (a + h) - f (a)

 h 

= lim

h → 0 4√a + h - 4√a 

 h Substitute f (a + h) and f (a) Multiply the numerator and denominator by the conjugate: 4√a + h + 4√a/4√a + h + 4√a .

f ′(a) = lim

h → 0 ( 4√a + h - 4√a 

 h ) ⋅ ( 4√a + h + 4√a/4√a + h + 4√a ) 

= lim

h → 0 ( 16(a + h) - 16(a)/(h)⁴( √a + h + 4√a ) ) Multiply.

= lim

h → 0 ( 16a + 16h - 16(a)/(h)⁴( √a + h + 4√a ) ) Distribute and combine like terms.

= lim

h → 0 ( 16(h)/(h)( 4√a + h + 4√a ) ) Simplify.

= lim

h →0/4√a + h + 4√a Evaluate the limit by letting h = 0.

= 16/8√a = 2 _ √a 

f ′(36) = 2 _ √36 Evaluate the derivative at x = 36.

= 2/6 

= 1/3 

---
### ✏️ **Try It #4**
Find the derivative of the function f (x) = 9√x at x = 9.
Finding Instantaneous Rates of Change Many applications of the derivative involve determining the rate of change at a given instant of a function with the independent variable time—which is why the term instantaneous is used.
Consider the height of a ball tossed upward with an initial velocity of 64 feet per second, given by s(t) = -16t 2 + 64t + 6, where t is measured in seconds and s(t) is measured in feet.
We know the path is that of a parabola.
The derivative will tell us how the height is changing at any given point in time.
The height of the ball is shown in Figure 4 as a function of time.
In physics, we call this the “s-t graph.” t s s(t) -5 -1 -2 -3 -4 -5

---
### 📐 **Example 5**
Finding the Instantaneous Rate of Change Using the function above, s(t) = -16t² + 64t + 6, what is the instantaneous velocity of the ball at 1 second and 3 seconds into its flight?

**Solution**

The velocity at t = 1 and t = 3 is the instantaneous rate of change of distance per time, or velocity.
Notice that the initial height is 6 feet.
To find the instantaneous velocity, we find the derivative and evaluate it at t = 1 and t = 3:

f ′(a) = lim

h → 0 f (a + h) - f (a)

 h 

= lim

h → 0 -16(t + h)² + 64(t + h) + 6 - (-16t 2 + 64t + 6)


h Substitute s(t + h) and s(t).

= lim

h → 0 -16t 2 - 32ht - h 2 + 64t + 64h + 6 + 16t 2 - 64t - 6


h Distribute.

= lim

h → 0 -32ht - h 2 + 64h

 h Simplify.

= lim

h → 0 h( - 32t - h + 64)

 h Factor the numerator.

= lim

h → 0 -32t - h + 64 Cancel out the common factor h.

s′(t) = - 32t + 64 Evaluate the limit by letting h = 0. For any value of t, s′(t) tells us the velocity at that value of t. Evaluate t = 1 and t = 3.

s′(1) = -32(1) + 64 = 32

s′(3) = -32(3) + 64 = -32 The velocity of the ball after 1 second is 32 feet per second, as it is on the way up.
The velocity of the ball after 3 seconds is -32 feet per second, as it is on the way down.

---
### ✏️ **Try It #5**
The position of the ball is given by s(t) = -16t 2 + 64t + 6.
What is its velocity 2 seconds into flight?
Using Graphs to Find Instantaneous Rates of Change We can estimate an instantaneous rate of change at x = a by observing the slope of the curve of the function f (x) at x = a.
We do this by drawing a line tangent to the function at x = a and finding its slope.

---
### 💡 **How To…**
Given a graph of a function f (x), find the instantaneous rate of change of the function at x = a. 1.
Locate x = a on the graph of the function f (x). 2.
Draw a tangent line, a line that goes through x = a at a and at no other point in that section of the curve.
Extend the line far enough to calculate its slope as change in y change in x .

---
### 📐 **Example 6**
Estimating the Derivative at a Point on the Graph of a Function From the graph of the function y = f (x) presented in Figure 5, estimate each of the following: f (0); f (2); f ′(0); f ′(2)

**Solution**

To find the functional value, f (a), find the y-coordinate at x = a.
To find the derivative at x = a, f ′(a), draw a tangent line at x = a, and estimate the slope of that tangent line.
See Figure 6. a. f (0) is the y-coordinate at x = 0.
The point has coordinates (0, 1), thus f (0) = 1. b. f (2) is the y-coordinate at x = 2.
The point has coordinates (2, 1), thus f (2) = 1. c. f ′(0) is found by estimating the slope of the tangent line to the curve at x = 0.
The tangent line to the curve at x = 0 appears horizontal.
Horizontal lines have a slope of 0, thus f ′(0) = 0. d. f ′(2) is found by estimating the slope of the tangent line to the curve at x = 2.
Observe the path of the tangent line to the curve at x = 2.
As the x value moves one unit to the right, the y value moves up four units to another point on the line.
Thus, the slope is 4, so f ′(2) = 4.

---
### ✏️ **Try It #6**
Using the graph of the function f (x) = x³ - 3x shown in Figure 7, estimate: f (1), f ′(1), f (0), and f ′(0). x y f -1-1 -2 -2 -3 -3 -4 -4 -5 -5 x y f m = 0 m = 4 -1-1 -2 -2 -3 -3 -4 -4 -5 -5 x y -1-1 -2 -2 -3 -3 -4 -4 -5 -5

Using Instantaneous Rates of Change to Solve Real-World Problems Another way to interpret an instantaneous rate of change at x = a is to observe the function in a real-world context.
The unit for the derivative of a function f (x) is output unit(s)/(i)nput unit Such a unit shows by how many units the output changes for each one-unit change of input.
The instantaneous rate of change at a given instant shows the same thing: the units of change of output per one-unit change of input.
One example of an instantaneous rate of change is a marginal cost.
For example, suppose the production cost for a company to produce x items is given by C(x), in thousands of dollars.
The derivative function tells us how the cost is changing for any value of x in the domain of the function.
In other words, C′ (x) is interpreted as a marginal cost, the additional cost in thousands of dollars of producing one more item when x items have been produced.
For example, C′ (11) is the approximate additional cost in thousands of dollars of producing the 12th item after 11 items have been produced.
C′ (11) = 2.50 means that when 11 items have been produced, producing the 12th item would increase the total cost by approximately $2,500.00.

---
### 📐 **Example 7**
Finding a Marginal Cost The cost in dollars of producing x laptop computers is f (x) = x² - 100x.
At the point where 200 computers have been produced, what is the approximate cost of producing the 201st unit?

**Solution**

If f (x) = x 2 - 100x describes the cost of producing x computers, f ′(x) will describe the marginal cost.
We need to find the derivative.
For purposes of calculating the derivative, we can use the following functions:

f (a + b) = (x + h)² - 100(x + h)

f (a) = a² - 100a

f ′(x) = f (a + h) - f (a)

 h Formula for a derivative

= (x + h)² - 100(x + h) - (x² - 100x)


h Substitute f (a + h) and f (a).

= x² + 2xh + h² - 100x - 100h - x² + 100x


h Multiply polynomials, distribute.

= 2xh + h² - 100h

 h Collect like terms.

= h(2x + h - 100)

 h Factor and cancel like terms.

= 2x + h - 100 Simplify.

Evaluate when h = 0.

f ′(x) = 2x - 100 Formula for marginal cost

Evaluate for 200 units.
The marginal cost of producing the 201st unit will be approximately $300.

---
### 📐 **Example 8**:
Interpreting a Derivative in Context

A car leaves an intersection.
The distance it travels in miles is given by the function f (t), where t represents hours.
Explain the following notations: f (0) = 0 ; f ′(1) = 60; f (1) = 70; f (2.5) = 150

**Solution**

First we need to evaluate the function f (t) and the derivative of the function f ′(t), and distinguish between the two.
When we evaluate the function f (t), we are finding the distance the car has traveled in t hours.
When we evaluate the derivative f ′(t), we are finding the speed of the car after t hours.

a. f (0) = 0 means that in zero hours, the car has traveled zero miles. b. f ′(1) = 60 means that one hour into the trip, the car is traveling 60 miles per hour. c. f (1) = 70 means that one hour into the trip, the car has traveled 70 miles. At some point during the first hour, then, the car must have been traveling faster than it was at the 1-hour mark. d. f (2.5) = 150 means that two hours and thirty minutes into the trip, the car has traveled 150 miles.

---
### ✏️ **Try It #7**
A runner runs along a straight east-west road.
The function f (t) gives how many feet eastward of her starting point she is after t seconds.
Interpret each of the following as it relates to the runner. f (0) = 0; f (10) = 150; f ′(10) = 15; f ′(20) = -10; f (40) = -100 Finding Points Where a Function’s Derivative Does Not Exist To understand where a function’s derivative does not exist, we need to recall what normally happens when a function f (x) has a derivative at x = a.
Suppose we use a graphing utility to zoom in on x = a .
If the function f (x) is differentiable, that is, if it is a function that can be differentiated, then the closer one zooms in, the more closely the graph approaches a straight line.
This characteristic is called linearity.
Look at the graph in Figure 8.
The closer we zoom in on the point, the more linear the curve appears.
We might presume the same thing would happen with any continuous function, but that is not so.
The function f (x) = | x |, for example, is continuous at x = 0, but not differentiable at x = 0.
As we zoom in close to 0 in Figure 9, the graph does not approach a straight line.
No matter how close we zoom in, the graph maintains its sharp corner.
We zoom in closer by narrowing the range to produce Figure 10 and continue to observe the same shape.
This graph does not appear linear at x = 0.
Graph appears linear y x x y -0.1 -0.1 0.1 0.1

What are the characteristics of a graph that is not differentiable at a point?
Here are some examples in which function f (x) is not differentiable at x = a.
In Figure 11, we see the graph of f (x) = { x 2, x ≤ 2

8 - x, x > 2 .
Notice that, as x approaches 2 from the left, the left-hand limit may be observed to be 4, while as x approaches 2 from the right, the right-hand limit may be observed to be 6.
We see that it has a discontinuity at x = 2.
In Figure 12, we see the graph of f (x) = | x |.
We see that the graph has a corner point at x = 0.
In Figure 13, we see that the graph of f (x) = x 2/3 has a cusp at x = 0.
A cusp has a unique feature.
Moving away from the cusp, both the left-hand and right-hand limits approach either infinity or negative infinity.
Notice the tangent lines as x approaches 0 from both the left and the right appear to get increasingly steeper, but one has a negative slope, the other has a positive slope. 3 has a cusp at x = 0. x y 0.001 0.001 x y -2 -1 -2 -3 -4 -5 x y -1-1 -2 -2 -3 -4 -5 x y

In Figure 14, we see that the graph of f (x) = x 1/3 has a vertical tangent at x = 0.
Recall that vertical tangents are vertical lines, so where a vertical tangent exists, the slope of the line is undefined.
This is why the derivative, which measures the slope, does not exist there. 3 has a vertical tangent at x = 0. differentiability A function f (x) is differentiable at x = a if the derivative exists at x = a, which means that f ′(a) exists.
There are four cases for which a function f (x) is not differentiable at a point x = a. 1.
When there is a discontinuity at x = a. 2.
When there is a corner point at x = a. 3.
When there is a cusp at x = a. 4.
Any other time when there is a vertical tangent at x = a.

---
### 📐 **Example 9**
Determining Where a Function Is Continuous and Differentiable from a Graph Using Figure 15, determine where the function is a. continuous b. discontinuous c. differentiable d. not differentiable At the points where the graph is discontinuous or not differentiable, state why.

**Solution**

The graph of f (x) is continuous on (-∞ , -2) ∪ (-2, 1) ∪ (1, ∞ ).
The graph of f (x) has a removable discontinuity at x = -2 and a jump discontinuity at x = 1.
See Figure 16. -1-1 -2 -2 -3 -3 -4 -4 -5 x y f x y f -1-1 -2 -2 -3 -3 -4 -4 -5 -5 -1-1 -2 -2 -3 -3 -4 -4 -5 -6 -5 -6 x y (-∞ , -2) (-2, 1) (1, ∞ )

The graph of f (x) is differentiable on (-∞ , -2) ∪ (-2, -1) ∪ (-1, 1) ∪ (1, 2) ∪ (2, ∞ ).
The graph of f (x) is not differentiable at x = -2 because it is a point of discontinuity, at x = -1 because of a sharp corner, at x = 1 because it is a point of discontinuity, and at x = 2 because of a sharp corner.
See Figure 17.

---
### ✏️ **Try It #8**
Determine where the function y = f (x) shown in Figure 18 is continuous and differentiable from the graph.
Finding an Equation of a Line Tangent to the Graph of a Function The equation of a tangent line to a curve of the function f (x) at x = a is derived from the point-slope form of a line, y = m(x - x¹) + y¹.
The slope of the line is the slope of the curve at x = a and is therefore equal to f ′(a), the derivative of f (x) at x = a.
The coordinate pair of the point on the line at x = a is (a, f (a)).
If we substitute into the point-slope form, we have m = f ′(a) x¹ = a y¹ = f (a) y = m(x - x¹) + y¹

↑ ↑ ↑

f ′(a) a f (a) The equation of the tangent line is

y = f ′(a)(x - a) + f (a) the equation of a line tangent to a curve of the function f The equation of a line tangent to the curve of a function f at a point x = a is

y = f ′(a)(x - a) + f (a) -1-1 -2 -2 -3 -3 -4 -4 -5 -5 Discontinuity Sharp corner Sharp corner Discontinuity (2, ∞ ) x y f x y y = f(x) -1-1 -2 -2 -3 -3 -4 -4 -5

---
### 💡 **How To…**
Given a function f, find the equation of a line tangent to the function at x = a. 1. Find the derivative of f (x) at x = a using f ′(a) = lim

h → 0 f (a + h) - f (a)

 h . 2. Evaluate the function at x = a. This is f (a). 3. Substitute (a, f (a))and f ′(a) into y = f ′(a)(x - a) + f (a). 4. Write the equation of the tangent line in the form y = mx + b.

---
### 📐 **Example 10**
Finding the Equation of a Line Tangent to a Function at a Point Find the equation of a line tangent to the curve f (x) = x 2 - 4x at x = 3.

**Solution**

Using:

f ′(a) = lim

h → 0 f (a + h) - f (a)

 h Substitute f (a + h) = (a + h)² - 4(a + h) and f (a) = a² - 4a.

f ′(a) = lim

h → 0 (a + h)(a + h) - 4(a + h) - (a² - 4a)


h 

= lim

h → 0 a² + 2ah + h² - 4a - 4h - a² + 4a


h Remove parentheses.

= lim

h → 0 a² + 2ah + h² -4a - 4h - a² + 4a


h Combine like terms.

= lim

h → 0 2ah + h² - 4h

 h 

= lim

h → 0 h(2a + h - 4)

 h Factor out h.

= 2a + 0 - 4

f ′(a) = 2a - 4 Evaluate the limit.

f ′(3) = 2(3) - 4 = 2 Equation of tangent line at x = 3:

y = f ′(a)(x - a) + f (a)

y = f ′(3)(x - 3) + f (3)

y = 2(x - 3) + (-3)

y = 2x - 9 Analysis We can use a graphing utility to graph the function and the tangent line.
In so doing, we can observe the point of tangency at x = 3 as shown in Figure 19. x y y = 2x - 9 f (x) = x 2 - 4x -1-1 -2 -2 -3 -3 -4 -4 -5 -5

---
### ✏️ **Try It #9**
Find the equation of a tangent line to the curve of the function f (x) = 5x² - x + 4 at x = 2.
Finding the Instantaneous Speed of a Particle If a function measures position versus time, the derivative measures displacement versus time, or the speed of the object.
A change in speed or direction relative to a change in time is known as velocity.
The velocity at a given instant is known as instantaneous velocity.
In trying to find the speed or velocity of an object at a given instant, we seem to encounter a contradiction.
We normally define speed as the distance traveled divided by the elapsed time.
But in an instant, no distance is traveled, and no time elapses.
How will we divide zero by zero?
The use of a derivative solves this problem.
A derivative allows us to say that even while the object’s velocity is constantly changing, it has a certain velocity at a given instant.
That means that if the object traveled at that exact velocity for a unit of time, it would travel the specified distance. instantaneous velocity Let the function s(t) represent the position of an object at time t.
The instantaneous velocity or velocity of the object at time t = a is given by s′(a) = lim

h → 0 s(a + h) - s(a)

 h 

---
### 📐 **Example 11**
Finding the Instantaneous Velocity A ball is tossed upward from a height of 200 feet with an initial velocity of 36 ft/sec.
If the height of the ball in feet after t seconds is given by s(t) = -16t 2 + 36t + 200, find the instantaneous velocity of the ball at t = 2.

**Solution**

First, we must find the derivative s′ (t) . Then we evaluate the derivative at t = 2, using

s(a + h) = - 16(a + h)² + 36(a + h) + 200 and s(a) = - 16a² + 36a + 200.

s′(a) = lim

h → 0 s(a + h) - s(a)

 h 

= lim

h → 0 -16(a + h)² + 36(a + h) + 200 - (-16a² + 36a + 200)


h 

= lim

h → 0 -16(a² + 2ah + h²) + 36(a + h) + 200 - (-16a² + 36a + 200)


h 

= lim


h 

= lim

h → 0 -16a² - 32ah - 16h² +36a + 36h + 200 + 16a² - 36a 

h 

= lim

h → 0 -32ah - 16h² + 36h

 h 

= lim

h → 0 h(-32a - 16h + 36)

 h 

= lim

h → 0( -32a - 16h + 36)

= -32a - 16 ⋅ 0 + 36

s′(a) = -32a + 36

s′(2) = -32(2) + 36

= -28 Analysis This result means that at time t = 2 seconds, the ball is dropping at a rate of 28 ft/sec.

---
### ✏️ **Try It #10**
A fireworks rocket is shot upward out of a pit 12 ft below the ground at a velocity of 60 ft/sec.
Its height in feet after t seconds is given by s = -16t² + 60t - 12.
What is its instantaneous velocity after 4 seconds?
Access these online resources for additional instruction and practice with derivatives.
• Estimate the Derivative (http://openstaxcollege.org/l/estimatederiv) • Estimate the Derivative Ex. 4 (http://openstaxcollege.org/l/estimatederiv⁴)

## 12.4 Section Exercises

---
### 12.4 Section Exercises

Verbal 1.
How is the slope of a linear function similar to the derivative? 2.
What is the difference between the average rate of change of a function on the interval [x, x + h] and the derivative of the function at x? 3.
A car traveled 110 miles during the time period from 2:00 P.M. to 4:00 P.M.
What was the car's average velocity?
At exactly 2:30 P.M., the speed of the car registered exactly 62 miles per hour.
What is another name for the speed of the car at 2:30 P.M.?
Why does this speed differ from the average velocity? 4.
Explain the concept of the slope of a curve at point x. 5.
Suppose water is flowing into a tank at an average rate of 45 gallons per minute.
Translate this statement into the language of mathematics.
Algebraic For the following exercises, use the definition of derivative lim

h → 0 f (x + h) - f (x)

 h to calculate the derivative of each function. 6. f (x) = 3x - 4 7. f (x) = -2x + 1 8. f (x) = x² - 2x + 1 9. f (x) = 2x² + x - 3 10. f (x) = 2x² + 5 11. f (x) = -1 x - 2 12. f (x) = 2 + x 1 - x 13. f (x) = 5 - 2x 3 + 2x 14. f (x) = √1 + 3x 15. f (x) = 3x³ - x² + 2x + 5 16. f (x) = 5 17. f (x) = 5π For the following exercises, find the average rate of change between the two points.
For the following polynomial functions, find the derivatives.
22. f (x) = x³ + 1 23. f (x) = -3x² - 7x + 6 24. f (x) = 7x² 25. f (x) = 3x³ + 2x² + x - 26 For the following functions, find the equation of the tangent line to the curve at the given point x on the curve.
26. f (x) = 2x² - 3x x = 3 27. f (x) = x³ + 1 x = 2 28. f (x) = √x x = 9 For the following exercise, find k such that the given line is tangent to the graph of the function.
29. f (x) = x² - kx, y = 4x - 9 Graphical For the following exercises, consider the graph of the function f and determine where the function is continuous/ discontinuous and differentiable/not differentiable. x y f(x) -1-1 -2 -2 -3 -3 -4 -4 -5 -5 x y f(x) -1-1 -2 -2 -3 -3 -4 -4 -5 -5

x y f(x) -1-1 -2 -2 -3 -3 -4 -4 -5 -5 -6 x y f(x) -2 -1 -1 -2 -3 -4 -3 -4 -5 -6 -5 -6 For the following exercises, use Figure 20 to estimate either the function at a given value of x or the derivative at a given value of x, as indicated. 39. f ′(-1) 44.
Sketch the function based on the information below: f ′(x) = 2x, f (2) = 4 Technology 45.
Numerically evaluate the derivative.
Explore the behavior of the graph of f (x) = x 2 around x = 1 by graphing use the feature on our calculator that automatically sets Ymin and Ymax to the Xmin and Xmax values we preset.
(On some of the commonly used graphing calculators, this feature may be called ZOOM FIT or ZOOM AUTO).
By examining the corresponding range values for this viewing window, approximate how the curve changes at x = 1, that is, approximate the derivative at x = 1.
Real-World Applications For the following exercises, explain the notation in words.
The volume f (t) of a tank of gasoline, in gallons, t minutes after noon. x y f(x) -2 -1 -1 -2 -3 -4 -3 -4 -5 -6 -7 -8 -9 -10 -5 -6

For the following exercises, explain the functions in words.
The height, s, of a projectile after t seconds is given by s(t) = -16t 2 + 80t.
For the following exercises, the volume V of a sphere with respect to its radius r is given by V = 4/3 π r 3. 56.
Find the average rate of change of V as r changes from 1 cm to 2 cm. 57.
Find the instantaneous rate of change of V when r = 3 cm.
For the following exercises, the revenue generated by selling x items is given by R(x) = 2x 2 + 10x. 58.
Find the average change of the revenue function as x changes from x = 10 to x = 20. 59.
Find R′(10) and interpret. 60.
Find R′(15) and interpret.
Compare R′(15) to R′(10), and explain the difference.
For the following exercises, the cost of producing x cellphones is described by the function C(x) = x 2 - 4x + 1000. 61.
Find the average rate of change in the total cost as x changes from x = 10 to x = 15. 62.
Find the approximate marginal cost, when 15 cellphones have been produced, of producing the 16th cellphone. 63.
Find the approximate marginal cost, when 20 cellphones have been produced, of producing the 21st cellphone.
Extension For the following exercises, use the definition for the derivative at a point x = a, lim

x → a f (x) - f (a) x - a , to find the derivative of the functions. 64. f (x) = 1/x² 65. f (x) = 5x 2 - x + 4 66. f (x) = -x 2 + 4x + 7 67. f (x) = -4 3 - x² 

### Key Terms

average rate of change the slope of the line connecting the two points (a, f (a)) and (a + h, f (a + h)) on the curve of f (x); it is given by AROC = f (a + h) - f (a)

 h . continuous function a function that has no holes or breaks in its graph derivative the slope of a function at a given point; denoted f ′(a), at a point x = a it is f ′(a) = lim

h → 0 f (a + h) - f (a)

 h , providing the limit exists. differentiable a function f (x) for which the derivative exists at x = a.
In other words, if f ′(a) exists. discontinuous function a function that is not continuous at x = a instantaneous rate of change the slope of a function at a given point; at x = a it is given by f ′(a) = lim

h → 0 f (a + h) - f (a)

 h instantaneous velocity the change in speed or direction at a given instant; a function s(t) represents the position of an object at time t, and the instantaneous velocity or velocity of the object at time t = a is given by s′(a) = lim

h → 0 s(a + h) - s(a)

 h . jump discontinuity a point of discontinuity in a function f (x) at x = a where both the left and right-hand limits exist, but lim

x → a- f (x) ≠ lim

x → a+ f (x) left-hand limit the limit of values of f (x) as x approaches a from the left, denoted lim

x → a- f (x) = L.
The values of f (x) can get as close to the limit L as we like by taking values of x sufficiently close to a such that x < a and x ≠ a.
Both a and L are real numbers. limit when it exists, the value, L, that the output of a function f (x) approaches as the input x gets closer and closer to a but does not equal a.
The value of the output, f (x), can get as close to L as we choose to make it by using input values of x sufficiently near to x = a, but not necessarily at x = a.
Both a and L are real numbers, and L is denoted lim

x → a f (x) = L. properties of limits a collection of theorems for finding limits of functions by performing mathematical operations on the limits removable discontinuity a point of discontinuity in a function f (x) where the function is discontinuous, but can be redefined to make it continuous right-hand limit the limit of values of f (x) as x approaches a from the right, denoted lim

x → a+ f (x) = L.
The values of f (x) can get as close to the limit L as we like by taking values of x sufficiently close to a where x > a, and x ≠ a.
Both a and L are real numbers. secant line a line that intersects two points on a curve tangent line a line that intersects a curve at a single point two-sided limit the limit of a function f (x), as x approaches a, is equal to L, that is, lim

x → a f (x) = L if and only if lim

x → a- f (x) = lim

x → a+ f (x). Key Equations average rate of change AROC = f (a + h) - f (a)

 h derivative of a function f ′(a) = lim

h → 0 f (a + h) - f (a)

 h 

### Key Concepts

• A function has a limit if the output values approach some value L as the input values approach some quantity a.
See

**Example 1** — .
• A shorthand notation is used to describe the limit of a function according to the form lim

x → a f (x) = L, which indicates that as x approaches a, both from the left of x = a and the right of x = a, the output value gets close to L. • A function has a left-hand limit if f (x) approaches L as x approaches a where x < a.
A function has a right-hand limit if f (x) approaches L as x approaches a where x > a. • A two-sided limit exists if the left-hand limit and the right-hand limit of a function are the same.
A function is said to have a limit if it has a two-sided limit.
• A graph provides a visual method of determining the limit of a function.
• If the function has a limit as x approaches a, the branches of the graph will approach the same y- coordinate near x = a from the left and the right.
See Example 2. • A table can be used to determine if a function has a limit.
The table should show input values that approach a from both directions so that the resulting output values can be evaluated.
If the output values approach some number, the function has a limit.
See Example 3. • A graphing utility can also be used to find a limit.
See Example 4. 12.2 Finding Limits: Properties of Limits • The properties of limits can be used to perform operations on the limits of functions rather than the functions themselves.
See Example 1. • The limit of a polynomial function can be found by finding the sum of the limits of the individual terms.
See

**Example 2** — and Example 3.
• The limit of a function that has been raised to a power equals the same power of the limit of the function.
Another method is direct substitution.
See Example 4.
• The limit of the root of a function equals the corresponding root of the limit of the function.
• One way to find the limit of a function expressed as a quotient is to write the quotient in factored form and simplify.
See Example 5.
• Another method of finding the limit of a complex fraction is to find the LCD.
See Example 6.
• A limit containing a function containing a root may be evaluated using a conjugate.
See Example 7.
• The limits of some functions expressed as quotients can be found by factoring.
See Example 8.
• One way to evaluate the limit of a quotient containing absolute values is by using numeric evidence.
Setting it up piecewise can also be useful.
See Example 9. 12.3 Continuity • A continuous function can be represented by a graph without holes or breaks.
• A function whose graph has holes is a discontinuous function.
• A function is continuous at a particular number if three conditions are met: • Condition 1: f (a) exists.
• Condition 2: lim

x → a f (x) exists at x = a. • Condition 3: lim

x → a f (x) = f (a). • A function has a jump discontinuity if the left- and right-hand limits are different, causing the graph to “jump.” • A function has a removable discontinuity if it can be redefined at its discontinuous point to make it continuous.
See

**Example 1** — .

• Some functions, such as polynomial functions, are continuous everywhere.
Other functions, such as logarithmic functions, are continuous on their domain.
See Example 2 and Example 3.
• For a piecewise function to be continuous each piece must be continuous on its part of the domain and the function as a whole must be continuous at the boundaries.
See Example 4 and Example 5. 12.4 Derivatives • The slope of the secant line connecting two points is the average rate of change of the function between those points.
See Example 1.
• The derivative, or instantaneous rate of change, is a measure of the slope of the curve of a function at a given point, or the slope of the line tangent to the curve at that point.
See Example 2, Example 3, and Example 4.
• The difference quotient is the quotient in the formula for the instantaneous rate of change: f (a + h) - f (a)

__ h • Instantaneous rates of change can be used to find solutions to many real-world problems.
See Example 5. • The instantaneous rate of change can be found by observing the slope of a function at a point on a graph by drawing a line tangent to the function at that point.
See Example 6. • Instantaneous rates of change can be interpreted to describe real-world situations.
See Example 7 and Example 8. • Some functions are not differentiable at a point or points.
See Example 9. • The point-slope form of a line can be used to find the equation of a line tangent to the curve of a function.
See

**Example 10** — .
• Velocity is a change in position relative to time.
Instantaneous velocity describes the velocity of an object at a given instant.
Average velocity describes the velocity maintained over an interval of time. • Using the derivative makes it possible to calculate instantaneous velocity even though there is no elapsed time.
See

**Example 11** — .

Finding Limits:
A Numerical and Graphical Approach For the following exercises, use Figure 1. x y -2 -4 -6 -8 -10 -2 -4 -6 -8 -10 1. lim

x → -1+ f (x) 2. lim

x → -1- f (x) 3. lim

x → -1 f (x) 4. lim

x → 3 f (x) 5. At what values of x is the function discontinuous? What condition of continuity is violated? 6. Using Table 1, estimate lim

x → 0 f (x). x f (x) -0.1 2.875 -0.01 2.92 2.998 Undefined 0.001 0.01 2.865 0.1 0.15 2.678 For the following exercises, with the use of a graphing utility, use numerical or graphical evidence to determine the left- and right-hand limits of the function given as x approaches a.
If the function has limit as x approaches a, state it.
If not, discuss why there is no limit. 7. f (x) ={ | x | - 1, if x ≠ 1

x³, if x = 1 a = 1 8. f (x) = { 1 x + 1 , if x = -2

(x + 1)², if x ≠ -2 a = -2 9. f (x) = { √x + 3 , if x < 1

-

√x , if x > 1 a = 1 Finding Limits:
Properties of Limits For the following exercises, find the limits if lim

x → c f (x) = -3 and lim

x → c g(x) = 5. 10. lim

x → c ( f (x) + g(x)) 11. lim

x → c f (x) g(x) 12. lim

x → c ( f (x) ⋅ g(x)) 13. lim

x → 0+ f (x), f (x) = { 3x² + 2x + 1 x > 0

5x + 3 x < 0 14. lim

x → 0- f (x), f (x) = { 3x² + 2x + 1 x > 0

5x + 3 x < 0 15. lim

x → 3+(3x - 〚x〛)

For the following exercises, evaluate the limits using algebraic techniques. 16. lim

h → 0 ( (h + 6)² - 36

 h ) 17. lim

x → 25 ( x 2 - 625 _ √x - 5 ) 18. lim

x → 1 ( -x 2 - 9x x ) 19. lim

x → 4 ( 7 - √12x + 1 

 x - 4 ) 20. lim

x → -3 ( 1/3 + 1/x 3 + x ) Continuity For the following exercises, use numerical evidence to determine whether the limit exists at x = a.
If not, describe the behavior of the graph of the function at x = a. 21. f (x) = -2 x - 4 ; a = 4 22. f (x) = -2 (x - 4)² ; a = 4 23. f (x) = -x x 2 - x - 6 ; a = 3 24. f (x) = 6x 2 + 23x + 20

 ; a = - 5 2 25. f (x) = √x - 3 9 - x ; a = 9 For the following exercises, determine where the given function f (x) is continuous.
Where it is not continuous, state which conditions fail, and classify any discontinuities. 26. f (x) = x 2 - 2x - 15 27. f (x) = x 2 - 2x - 15 x - 5 28. f (x) = x 2 - 2x x 2 - 4x + 4 29. f (x) = 

30. f (x) = x 2 - 1/x 2 - x 31. f (x) = x + 2 x 2 - 3x - 10 32. f (x) = x + 2 x 3 + 8 Derivatives For the following exercises, find the average rate of change f (x + h) - f (x)

 h .
33. f (x) = 3x + 2 34. f (x) = 5 35. f (x) = 1 x + 1 36. f (x) = ln(x) 37. f (x) = e²x For the following exercises, find the derivative of the function.
38. f (x) = 4x - 6 39. f (x) = 5x 2 - 3x 40.
Find the equation of the tangent line to the graph of f (x) at the indicated x value. f (x) = -x 3 + 4x; x = 2.
For the following exercises, with the aid of a graphing utility, explain why the function is not differentiable everywhere on its domain.
Specify the points where the function is not differentiable. 41. f (x) = x _ | x | 42.
Given that the volume of a right circular cone is V = 1/3 π r 2h and that a given cone has a fixed height of 9 cm and variable radius length, find the instantaneous rate of change of volume with respect to radius length when the radius is 2 cm.
Give an exact answer in terms of π .

For the following exercises, use the graph of f in Figure 1. x y -1 -2 -3 -4 -5 -1 -2 -3 -4 -5 1. f (1) 2. lim

x → -1+ f (x) 3. lim

x → -1- f (x) 4. lim

x → -1 f (x) 5. lim

x → -2 f (x) 6.
At what values of x is f discontinuous?
What property of continuity is violated?
For the following exercises, with the use of a graphing utility, use numerical or graphical evidence to determine the left- and right-hand limits of the function given as x approaches a.
If the function has a limit as x approaches a, state it.
If not, discuss why there is no limit. 7. f (x) = { 1/x - 3, if x ≤ 2

x³ + 1, if x > 2 a = 2 8. f (x) = { x³ + 1, if x < 1

3x² - 1, if x = 1

-√x + 3 + 4, if x > 1 a = 1 For the following exercises, evaluate each limit using algebraic techniques. 10. lim

h → 0 ( √h² + 25 - 5

 h² ) 11. lim

h → 0 ( 1/h - h² + h ) For the following exercises, determine whether or not the given function f is continuous.
If it is continuous, show why.
If it is not continuous, state which conditions fail. 12. f (x) = √x 2 - 4 13. f (x) = x³ - 4x 2 - 9x + 36


x 3 - 3x 2 + 2x - 6 For the following exercises, use the definition of a derivative to find the derivative of the given function at x = a.
14. f (x) = 5 + 2x 15. f (x) = 3 _ √x 16. f (x) = 2x 2 + 9x 17.
For the graph in Figure 2, determine where the function is continuous/discontinuous and differentiable/not differentiable. x f(x) y -1 -2 -3 -4 -5 lim

x → -5 ( 1/5 + 1/x 10 + 2x ) 

For the following exercises, with the aid of a graphing utility, explain why the function is not differentiable everywhere on its domain.
Specify the points where the function is not differentiable.
18. f (x) = |x - 2| - |x + 2| 19. f (x) = 1 + e 2/x For the following exercises, explain the notation in words when the height of a projectile in feet, s, is a function of time t in seconds after launch and is given by the function s(t). 23. s(2) - s(1) 2 - 1 24. s(t) = 0 For the following exercises, use technology to evaluate the limit. 25. lim

x → 0 sin(x) 3x 26. lim

x → 0 tan²(x) 2x 27. lim

x → 0 sin(x)(1 - cos(x))

 2x 2 28.
Evaluate the limit by hand. lim

x → 1 f (x), where f (x) = { 4x - 7 x ≠ 1

x 2 - 4 x = 1 At what value(s) of x is the function discontinuous?
For the following exercises, consider the function whose graph appears in Figure 3. x y -1 -2 -3 -4 -5 -1 -2 -3 -4 -5 29.
Find the average rate of change of the function from x = 1 to x = 3. 30.
Find all values of x at which f ′(x) = 0. 31.
Find all values of x at which f ′(x) does not exist. 32.
Find an equation of the tangent line to the graph of f the indicated point: f (x) = 3x² - 2x - 6, x = - 2 For the following exercises, use the function f (x) = x(1 - x) 2/5 . 33.
Graph the function f (x) = x(1 - x) 2/5 by entering f (x) = x((1 - x)²) 1/5 and then by entering f (x) = x( (1 - x) 1/5 ) 2. 34.
Explore the behavior of the graph of f (x) around x = 1 by graphing the function on the following [0.9999, 1.0001].
Use this information to determine whether the function appears to be differentiable at x = 1.
For the following exercises, find the derivative of each of the functions using the definition: lim

h → 0 f (x + h) - f (x)

 h 35. f (x) = 2x - 8 36. f (x) = 4x² - 7 37. f (x) = x - 1/2 x² 38. f (x) = 1/x + 2 39. f (x) = 3/x - 1 40. f (x) = -x³ + 1 41. f (x) = x² + x³ 42. f (x) = √x - 1 
