# Trigonometric Identities and Equations

## Introduction

---
Math is everywhere, even in places we might not immediately recognize.
For example, mathematical relationships describe the transmission of images, light, and sound.
The sinusoidal graph in Figure 1 models music playing on a phone, radio, or computer.
Such graphs are described using trigonometric equations and functions.
In this chapter, we discuss how to manipulate trigonometric equations algebraically by applying various formulas and trigonometric identities.
We will also investigate some of the ways that trigonometric equations are used to model real-life phenomena.

Learning Objectives
In this section, you will:
• Verify the fundamental trigonometric identities.
• Simplify trigonometric expressions using algebra and the identities.

## 7.1 Solving Trigonometric Equations with Identities

---
In espionage movies, we see international spies with multiple passports, each claiming a different identity.
However, we know that each of those passports represents the same person.
The trigonometric identities act in a similar manner to multiple passports—there are many ways to represent the same trigonometric expression.
Just as a spy will choose an Italian passport when traveling to Italy, we choose the identity that applies to the given scenario when solving a trigonometric equation.
In this section, we will begin an examination of the fundamental trigonometric identities, including how we can verify them and how we can use them to simplify trigonometric expressions.
Verifying the Fundamental Trigonometric Identities Identities enable us to simplify complicated expressions.
They are the basic tools of trigonometry used in solving trigonometric equations, just as factoring, finding common denominators, and using special formulas are the basic tools of solving algebraic equations.
In fact, we use algebraic techniques constantly to simplify trigonometric expressions.
Basic properties and formulas of algebra, such as the difference of squares formula and the perfect squares formula, will simplify the work involved with trigonometric expressions and equations.
We already know that all of the trigonometric functions are related because they all are defined in terms of the unit circle.
Consequently, any trigonometric identity can be written in many ways.
To verify the trigonometric identities, we usually start with the more complicated side of the equation and essentially rewrite the expression until it has been transformed into the same expression as the other side of the equation.
Sometimes we have to factor expressions, expand expressions, find common denominators, or use other algebraic strategies to obtain the desired result.
In this first section, we will work with the fundamental identities: the Pythagorean identities, the even-odd identities, the reciprocal identities, and the quotient identities.
We will begin with the Pythagorean identities (see Table 1), which are equations involving trigonometric functions based on the properties of a right triangle.
We have already seen and used the first of these identifies, but now we will also use additional identities.
Pythagorean Identities sin² θ + cos² θ = 1 1 + cot² θ = csc² θ 1 + tan² θ = sec² θ 

The second and third identities can be obtained by manipulating the first.
The identity 1 + cot² θ = csc² θ is found by rewriting the left side of the equation in terms of sine and cosine.
Prove: 1 + cot² θ = csc² θ 


1 + cot² θ = ( 1 + cos² θ sin² θ ) Rewrite the left side.


= ( sin² θ sin² θ ) + ( cos² θ sin² θ ) Write both terms with the common denominator.


= sin² θ + cos² θ sin² θ


> **= 1 sin² θ**


= csc² θ Similarly, 1 + tan² θ = sec² θ can be obtained by rewriting the left side of this identity in terms of sine and cosine.
This gives


> **1 + tan² θ = 1 + ( sin θ cos θ )**


Rewrite left side.


> **= ( cos θ cos θ ) + ( sin θ cos θ )**


Write both terms with the common denominator.


= cos² θ + sin² θ cos² θ


> **= 1 cos² θ**


= sec² θ The next set of fundamental identities is the set of even-odd identities.
The even-odd identities relate the value of a trigonometric function at a given angle to the value of the function at the opposite angle and determine whether the identity is odd or even.
(See Table 2).
Even-Odd Identities tan(-θ ) = -tan θ sin(-θ ) = -sin θ cos(-θ ) = cos θ cot(-θ ) = -cot θ csc(-θ ) = -csc θ sec(-θ ) = sec θ Recall that an odd function is one in which f (-x) = -f (x) for all x in the domain of f.
The sine function is an odd function because sin(-θ ) = -sin θ .
The graph of an odd function is symmetric about the origin.
For example, consider corresponding inputs of π/2 and - π/2 .
The output of sin ( π/2 ) is opposite the output of sin ( - π/2 ).
Thus,


> **sin ( π/2 ) = 1 and**


> **sin ( - π/2 ) = -sin ( π/2 )**


= -1 This is shown in Figure 2. x y π 2π –2π –π π , π , f(x) = sin x Recall that an even function is one in which f (-x) = f (x) for all x in the domain of f

The graph of an even function is symmetric about the y-axis.
The cosine function is an even function because cos(-θ ) = cos θ .
For example, consider corresponding inputs π/4 and - π/4 .
The output of cos ( π/4 ) is the same as the output of cos ( - π/4 ).
Thus, cos ( - π/4 ) = cos ( π/4 )

See Figure 3. x y π 2π –2π –π 0.707 π , 0.707 π , f(x) = cos x For all θ in the domain of the sine and cosine functions, respectively, we can state the following: • Since sin(-θ ) = -sin θ , sine is an odd function.
• Since, cos(-θ ) = cos θ , cosine is an even function.
The other even-odd identities follow from the even and odd nature of the sine and cosine functions.
For example, consider the tangent identity, tan(-θ ) = -tan θ .
We can interpret the tangent of a negative angle as tan(-θ ) = sin(-θ ) cos(-θ ) = -sin θ cos θ = -tan θ .
Tangent is therefore an odd function, which means that tan(-θ ) = -tan(θ ) for all θ in the domain of the tangent function.
The cotangent identity, cot(-θ ) = -cot θ , also follows from the sine and cosine identities.
We can interpret the cotangent of a negative angle as cot(-θ ) = cos(-θ ) sin(-θ ) = cos θ -sin θ = -cot θ .
Cotangent is therefore an odd function, which means that cot(-θ ) = -cot(θ ) for all θ in the domain of the cotangent function.
The cosecant function is the reciprocal of the sine function, which means that the cosecant of a negative angle will be interpreted as csc(-θ ) = sin(-θ ) = -sin θ = -csc θ .
The cosecant function is therefore odd.
Finally, the secant function is the reciprocal of the cosine function, and the secant of a negative angle is interpreted as sec(-θ ) = cos(-θ ) = 1 cos θ = sec θ .
The secant function is therefore even.
To sum up, only two of the trigonometric functions, cosine and secant, are even.
The other four functions are odd, verifying the even-odd identities.
The next set of fundamental identities is the set of reciprocal identities, which, as their name implies, relate trigonometric functions that are reciprocals of each other.
See Table 3.
Reciprocal Identities sin θ = 1 csc θ csc θ = 1 sin θ cos θ = 1 sec θ sec θ = 1 cos θ tan θ = 1 cot θ cot θ = 1 tan θ The final set of identities is the set of quotient identities, which define relationships among certain trigonometric functions and can be very helpful in verifying other identities.
See Table 4.
Quotient Identities tan θ = sin θ cos θ cot θ = cos θ sin θ 

The reciprocal and quotient identities are derived from the definitions of the basic trigonometric functions. summarizing trigonometric identities The Pythagorean identities are based on the properties of a right triangle.


cos² θ + sin² θ = 1


1 + cot² θ = csc² θ


1 + tan² θ = sec² θ The even-odd identities relate the value of a trigonometric function at a given angle to the value of the function at the opposite angle.


> **tan(-θ ) = -tan θ**


> **cot(-θ ) = -cot θ**


> **sin(-θ ) = -sin θ**


> **csc(-θ ) = -csc θ**


> **cos(-θ ) = cos θ**


sec(-θ ) = sec θ The reciprocal identities define reciprocals of the trigonometric functions. sin θ = 1 csc θ cos θ = 1 sec θ tan θ = 1 cot θ csc θ = 1 sin θ sec θ = 1 cos θ cot θ = 1 tan θ The quotient identities define the relationship among the trigonometric functions. tan θ = sin θ cos θ cot θ = cos θ sin θ 

---
### 📐 **Example 1**:
Graphing the Equations of an Identity

Graph both sides of the identity cot θ = 1 tan θ .
In other words, on the graphing calculator, graph y = cot θ and y = 1 tan θ .

**Solution**


> **See Figure 4.
θ y π π 3π 5π = tan θ y = cot θ 3π – 5π**


Analysis We see only one graph because both expressions generate the same image.
One is on top of the other.
This is a good way to prove any identity.
If both expressions give the same graph, then they must be identities.

---
### 💡 **How To…**
Given a trigonometric identity, verify that it is true. 1.
Work on one side of the equation.
It is usually better to start with the more complex side, as it is easier to simplify than to build. 2.
Look for opportunities to factor expressions, square a binomial, or add fractions. 3.
Noting which functions are in the final expression, look for opportunities to use the identities and make the proper substitutions. 4.
If these steps do not yield the desired result, try converting all terms to sines and cosines.

---
### 📐 **Example 2**:
Verifying a Trigonometric Identity


> **Verify tan θ cos θ = sin θ .**


**Solution**

We will start on the left side, as it is the more complicated side: tan θ cos θ = ( sin θ cos θ ) cos θ 


> **= ( sin θ cos θ ) cos θ**


= sin θ Analysis This identity was fairly simple to verify, as it only required writing tan θ in terms of sin θ and cos θ .

---
### ✏️ **Try It #1**
Verify the identity csc θ cos θ tan θ = 1.

---
### 📐 **Example 3**:
Verifying the Equivalency Using the Even-Odd Identities

Verify the following equivalency using the even-odd identities: (1 + sin x)[1 + sin(-x)] = cos² x

**Solution**

Working on the left side of the equation, we have

(1 + sin x)[1 + sin(-x)] = (1 + sin x)(1 - sin x) Since sin(-x) = -sin x

= 1 - sin² x Difference of squares

= cos² x cos² x = 1 - sin² x

---
### 📐 **Example 4**:
Verifying a Trigonometric Identity Involving sec² θ 


Verify the identity sec² θ - 1 sec² θ = sin² θ


**Solution**

As the left side is more complicated, let’s begin there.


sec² θ - 1 sec² θ = (tan² θ + 1) - 1


sec² θ sec² θ = tan² θ + 1


= tan² θ sec² θ


= tan² θ ( 1 sec² θ )


= tan² θ (cos² θ ) cos² θ = 1 sec² θ


= ( sin² θ cos² θ )(cos² θ ) tan² θ = sin² θ cos² θ


= ( sin² θ cos² θ )(cos² θ )


> **= sin² θ**


There is more than one way to verify an identity.
Here is another possibility.
Again, we can start with the left side.


sec² θ - 1 sec² θ = sec² θ sec² θ - 1 sec² θ


> **= 1 - cos² θ**


= sin² θ Analysis In the first method, we used the identity sec² θ = tan² θ + 1 and continued to simplify.
In the second method, we split the fraction, putting both terms in the numerator over the common denominator.
This problem illustrates that there are multiple ways we can verify an identity.
Employing some creativity can sometimes simplify a procedure.
As long as the substitutions are correct, the answer will be the same.

---
### ✏️ **Try It #2**
Show that cot θ csc θ = cos θ .

---
### 📐 **Example 5**:
Creating and Verifying an Identity

Create an identity for the expression 2tan θ sec θ by rewriting strictly in terms of sine.

**Solution**

There are a number of ways to begin, but here we will use the quotient and reciprocal identities to rewrite the expression:


> **2 tan θ sec θ = 2( sin θ cos θ )( 1 cos θ )**


> **= 2 sin θ cos² θ**


= 2 sin θ 1 - sin² θ Substitute 1 - sin² θ for cos² θ Thus,


2tan θ sec θ = 2 sin θ 1 - sin² θ


---
### 📐 **Example 6**:
Verifying an Identity Using Algebra and Even/Odd Identities

Verify the identity:

 sin²(-θ ) - cos²(-θ )


> **sin(-θ ) - cos(-θ ) = cos θ - sin θ**


**Solution**

Let’s start with the left side and simplify:

 sin²(-θ ) - cos²(-θ )


> **sin(-θ ) - cos(-θ ) = [sin(-θ )]2 - [cos(-θ )]2**


sin(-θ ) - cos(-θ ) 


> **= (-sin θ )² - (cos θ )²**


-sin θ - cos θ sin(-x) = -sin x and cos(-x) = cos x


> **= (sin θ )² - (cos θ )²**


-sin θ - cos θ Difference of squares


> **= (sin θ - cos θ )(sin θ + cos θ )**


-(sin θ + cos θ ) 


> **= (sin θ - cos θ )(sin θ + cos θ )**


-(sin θ + cos θ ) 


> **= cos θ - sin θ**


---
### ✏️ **Try It #3**
Verify the identity sin² θ - 1


> **tan θ sin θ - tan θ = sin θ + 1 tan θ .**


---
### 📐 **Example 7**:
Verifying an Identity Involving Cosines and Cotangents

Verify the identity: (1 - cos² x)(1 + cot² x) = 1.

**Solution**

We will work on the left side of the equation

(1 - cos² x)(1 + cot² x) = (1 - cos² x)( 1 + cos² x sin² x )

= (1 - cos² x)( sin² x sin² x + cos² x sin² x ) Find the common denominator.

= (1 - cos² x)( sin² x + cos² x

 sin² x )

= (sin² x)( 1 sin² x )

= 1 Using Algebra to Simplify Trigonometric Expressions We have seen that algebra is very important in verifying trigonometric identities, but it is just as critical in simplifying trigonometric expressions before solving.
Being familiar with the basic properties and formulas of algebra, such as the difference of squares formula, the perfect square formula, or substitution, will simplify the work involved with trigonometric expressions and equations.
For example, the equation (sin x + 1)(sin x - 1) = 0 resembles the equation (x + 1)(x - 1) = 0, which uses the factored form of the difference of squares.
Using algebra makes finding a solution straightforward and familiar.
We can set each factor equal to zero and solve.
This is one example of recognizing algebraic patterns in trigonometric expressions or equations.
Another example is the difference of squares formula, a² - b² = (a - b)(a + b), which is widely used in many areas other than mathematics, such as engineering, architecture, and physics.
We can also create our own identities by continually expanding an expression and making the appropriate substitutions.
Using algebraic properties and formulas makes many trigonometric equations easier to understand and solve.

---
### 📐 **Example 8**:
Writing the Trigonometric Expression as an Algebraic Expression

Write the following trigonometric expression as an algebraic expression: 2cos² θ + cos θ - 1.

**Solution**

Notice that the pattern displayed has the same form as a standard quadratic expression, ax² + bx + c.
Letting cos θ = x, we can rewrite the expression as follows: 2x² + x - 1 This expression can be factored as (2x - 1)(x + 1).
If it were set equal to zero and we wanted to solve the equation, we would use the zero factor property and solve each factor for x.
At this point, we would replace x with cos θ and solve for θ .

---
### 📐 **Example 9**
Rewriting a Trigonometric Expression Using the Difference of Squares Rewrite the trigonometric expression: 4 cos² θ - 1.

**Solution**

Notice that both the coefficient and the trigonometric expression in the first term are squared, and the square of the number 1 is 1.
This is the difference of squares.
Thus,


> **4 cos² θ - 1 = (2 cos θ )² - 1**


= (2 cos θ - 1)(2 cos θ + 1) Analysis If this expression were written in the form of an equation set equal to zero, we could solve each factor using the zero factor property.
We could also use substitution like we did in the previous problem and let cos θ = x, rewrite the expression as 4x² - 1, and factor (2x - 1)(2x + 1).
Then replace x with cos θ and solve for the angle.

---
### ✏️ **Try It #4**
Rewrite the trigonometric expression: 25 - 9 sin² θ .

---
### 📐 **Example 10**
Simplify by Rewriting and Using Substitution Simplify the expression by rewriting and using identities: csc² θ - cot² θ

**Solution**

We can start with the Pythagorean Identity.

1 + cot² θ = csc² θ Now we can simplify by substituting 1 + cot² θ for csc² θ .
We have


csc² θ - cot² θ = 1 + cot² θ - cot² θ


= 1

---
### ✏️ **Try It #5**
Use algebraic techniques to verify the identity: cos θ 1 + sin θ = 1 - sin θ cos θ . (Hint: Multiply the numerator and denominator on the left side by 1 - sin θ .)

Access these online resources for additional instruction and practice with the fundamental trigonometric identities.
• Fundamental Trigonometric Identities (http://openstaxcollege.org/l/funtrigiden) • Verifying Trigonometric Identities (http://openstaxcollege.org/l/verifytrigiden)

7.1 SECTION EXERCISES Verbal 1. We know g(x) = cos x is an even function, and f (x) = sin x and h(x) = tan x are odd functions. What about G(x) = cos² x, F (x) = sin² x, and H(x) = tan² x? Are they even, odd, or neither? Why? 2. Examine the graph of f (x) = sec x on the interval [-π , π ]. How can we tell whether the function is even or odd by only observing the graph of f (x) = sec x? 3. After examining the reciprocal identity for sec t, explain why the function is undefined at certain points. 4. All of the Pythagorean identities are related. Describe how to manipulate the equations to get from sin² t + cos² t = 1 to the other forms. Algebraic For the following exercises, use the fundamental identities to fully simplify the expression. 5. sin x cos x sec x 6. sin(-x)cos(-x)csc(-x) 7. tan x sin x + sec x cos² x 8. csc x + cos x cot(-x) 9. cot t + tan t sec(-t) 10. 3 sin³ t csc t + cos² t + 2 cos(-t)cos t 11. -tan(-x)cot(-x) 12. -sin(-x)cos x sec x csc x tan x


cot x 13. 1 + tan² θ csc² θ + sin² θ + 1 sec² θ 14.
( tan x csc² x + tan x sec² x )( 1 + tan x 1 + cot x ) - 1 cos² x 15. 1 - cos² x tan² x + 2 sin² x For the following exercises, simplify the first trigonometric expression by writing the simplified form in terms of the second expression.
16. tan x + cot x csc x ; cos x 17. sec x + csc x 1 + tan x ; sin x 18. cos x 1 + sin x + tan x; cos x 19. sin x cos x - cot x; cot x 20. 1 - cos x - cos x 1 + cos x ; csc x 21.
(sec x + csc x)(sin x + cos x) - 2 - cot x; tan x 22. 

csc x - sin x ; sec x and tan x 23. 1 - sin x 1 + sin x - 1 + sin x 1 - sin x ; sec x and tan x 24. tan x; sec x 25. sec x; cot x 26. sec x; sin x 27. cot x; sin x 28. cot x; csc x For the following exercises, verify the identity.
29. cos x - cos³ x = cos x sin² x 30. cos x(tan x - sec(-x)) = sin x - 1 31. 1 + sin² x cos² x = 1 cos² x + sin² x cos² x = 1 + 2 tan² x 32.
(sin x + cos x)² = 1 + 2 sin x cos x 33. cos² x - tan² x = 2 - sin² x - sec² x

## 7.1 Section Exercises

---
Extensions For the following exercises, prove or disprove the identity. 34. 1 + cos x - 

1 - cos( - x) = -2 cot x csc x 35. csc² x(1 + sin² x) = cot² x 36. ( sec²(-x) - tan² x

 tan x )( 2 + 2 tan x 2 + 2 cot x ) - 2 sin² x = cos 2x 37. tan x sec x sin(-x) = cos² x 38. sec(-x) 

tan x + cot x = -sin(-x) 39. 1 + sin x cos x = cos x 

1 + sin(-x) For the following exercises, determine whether the identity is true or false. If false, find an appropriate equivalent expression. 40. cos² θ - sin² θ 


1 - tan² θ = sin² θ 41. 3 sin² θ + 4 cos² θ = 3 + cos² θ 42. sec θ + tan θ 


> **cot θ + cos θ = sec² θ**


Learning Objectives
In this section, you will:
• Use sum and difference formulas for cosine.
• Use sum and difference formulas for sine.
• Use sum and difference formulas for tangent.
• Use sum and difference formulas for cofunctions.
• Use sum and difference formulas to verify identities.

## 7.2 Sum and Difference Identities

---
How can the height of a mountain be measured?
What about the distance from Earth to the sun?
Like many seemingly impossible problems, we rely on mathematical formulas to find the answers.
The trigonometric identities, commonly used in mathematical proofs, have had real-world applications for centuries, including their use in calculating long distances.
The trigonometric identities we will examine in this section can be traced to a Persian astronomer who lived around 950 AD, but the ancient Greeks discovered these same formulas much earlier and stated them in terms of chords.
These are special equations or postulates, true for all values input to the equations, and with innumerable applications.
In this section, we will learn techniques that will enable us to solve problems such as the ones presented above.
The formulas that follow will simplify many trigonometric expressions and equations.
Keep in mind that, throughout this section, the term formula is used synonymously with the word identity.
Using the Sum and Difference Formulas for Cosine Finding the exact value of the sine, cosine, or tangent of an angle is often easier if we can rewrite the given angle in terms of two angles that have known trigonometric values.
We can use the special angles, which we can review in the unit circle shown in Figure 2.
π π π π 60° 4π 5π 7π 225° 240° 300° 315° 2π π 3π 5π 7π 5π 150° 3π 2π 135° 11π 30° 45° 330° 210° 120°

We will begin with the sum and difference formulas for cosine, so that we can find the cosine of a given angle if we can break it up into the sum or difference of two of the special angles.
See Table 1.
Sum formula for cosine cos(α + β ) = cos α cos β - sin α sin β Difference formula for cosine cos(α - β ) = cos α cos β + sin α sin β First, we will prove the difference formula for cosines.
Let’s consider two points on the unit circle.
See Figure 3.
Point P is at an angle α from the positive x-axis with coordinates (cos α , sin α ) and point Q is at an angle of β from the positive x-axis with coordinates (cos β , sin β ).
Note the measure of angle POQ is α - β .
Label two more points: A at an angle of (α - β ) from the positive x-axis with coordinates (cos(α - β ), sin(α - β )); and point B with coordinates (1, 0).
Triangle POQ is a rotation of triangle AOB and thus the distance from P to Q is the same as the distance from A to B. x y π 2π –2π –π π , π , f(x) = sin x We can find the distance from P to Q using the distance formula.

dPQ = √—

(cos α - cos β )² + (sin α - sin β )² 

= √———

cos² α - 2 cos α cos β + cos² β + sin² α - 2 sin α sin β + sin² β Then we apply the Pythagorean Identity and simplify.

= √———

(cos² α + sin² α ) + (cos² β + sin² β ) - 2 cos α cos β - 2 sin α sin β 

= √—

1 + 1 - 2 cos α cos β - 2 sin α sin β 

= √—

2 - 2 cos α cos β - 2 sin α sin β Similarly, using the distance formula we can find the distance from A to B.

dAB = √—

(cos(α - β ) - 1)² + (sin(α - β ) - 0)² 

= √——

cos²(α - β ) - 2 cos(α - β ) + 1 + sin²(α - β ) Applying the Pythagorean Identity and simplifying we get:

= √——

(cos²(α - β ) + sin²(α - β )) - 2 cos(α - β ) + 1 

= √—

1 - 2 cos(α - β ) + 1 

= √2 - 2 cos(α - β ) Because the two distances are the same, we set them equal to each other and simplify.

√—


> **2 - 2 cos α cos β - 2 sin α sin β = √2 - 2 cos(α - β )**


2 - 2 cos α cos β - 2 sin α sin β = 2 - 2 cos(α - β ) Finally we subtract 2 from both sides and divide both sides by -2.

cos α cos β + sin α sin β = cos(α - β ) Thus, we have the difference formula for cosine. We can use similar methods to derive the cosine of the sum of two angles.

sum and difference formulas for cosine These formulas can be used to calculate the cosine of sums and differences of angles. cos(α + β ) = cos α cos β - sin α sin β cos(α - β ) = cos α cos β + sin α sin β 

---
### 💡 **How To…**
Given two angles, find the cosine of the difference between the angles. 1.
Write the difference formula for cosine. 2.
Substitute the values of the given angles into the formula. 3.
Simplify.

---
### 📐 **Example 1**
Finding the Exact Value Using the Formula for the Cosine of the Difference of Two Angles Using the formula for the cosine of the difference of two angles, find the exact value of cos ( 5π/4 - π/6 ).

**Solution**

Use the formula for the cosine of the difference of two angles.
We have


> **cos(α - β ) = cos α cos β + sin α sin β**


cos ( 5π 4 - π/6 ) = cos ( 5π 4 ) cos ( π/6 ) + sin ( 5π 4 ) sin ( π/6 )

= ( - √2 2 )( √3 2 ) - ( √2 2 )( 1/2 )

= - √6 4 - √2 4 

= -√6 - √2 

---
### ✏️ **Try It #1**
Find the exact value of cos ( π/3 - π/4 ).

---
### 📐 **Example 2**
Finding the Exact Value Using the Formula for the Sum of Two Angles for Cosine Find the exact value of cos(75°).

**Solution**

As 75° = 45° + 30°, we can evaluate cos(75°) as cos(45° + 30°). Thus,

cos(45° + 30°) = cos(45°)cos(30°) - sin(45°)sin(30°)

= √2 2 ( √3 2 ) - √2 2 ( 1/2 )

= √6 4 - √2 4 

= √6 - √2 

---
### ✏️ **Try It #2**
Find the exact value of cos(105°).
Using the Sum and Difference Formulas for Sine The sum and difference formulas for sine can be derived in the same manner as those for cosine, and they resemble the cosine formulas.

sum and difference formulas for sine These formulas can be used to calculate the sines of sums and differences of angles. sin(α + β ) = sin α cos β + cos α sin β sin(α - β ) = sin α cos β - cos α sin β 

---
### 💡 **How To…**
Given two angles, find the sine of the difference between the angles. 1.
Write the difference formula for sine. 2.
Substitute the given angles into the formula. 3.
Simplify.

---
### 📐 **Example 3**
Using Sum and Difference Identities to Evaluate the Difference of Angles Use the sum and difference identities to evaluate the difference of the angles and show that part a equals part b. a. sin(45° - 30°) b. sin(135° - 120°)

**Solution**

a.
Let’s begin by writing the formula and substitute the given angles.


> **sin(α - β ) = sin α cos β - cos α sin β**


sin(45° - 30°) = sin(45°)cos(30°) - cos(45°)sin(30°) Next, we need to find the values of the trigonometric expressions.

sin(45°) = √2 2 , cos(30°) = √3 2 , cos(45°) = √2 2 , sin(30°) = 1/2 Now we can substitute these values into the equation and simplify.

sin(45° - 30°) = √2 2 ( √3 2 ) - √2 2 ( 1/2 )

= √6 - √2 b.
Again, we write the formula and substitute the given angles.


> **sin(α - β ) = sin α cos β - cos α sin β**


sin(135° - 120°) = sin(135°)cos(120°) - cos(135°)sin(120°) Next, we find the values of the trigonometric expressions. sin(135°) = √2 2 , cos(120°) = - 1/2 , cos(135°) = - √2 2 , sin(120°) = √3 2 Now we can substitute these values into the equation and simplify.

sin(135° - 120°) = √2 2 ( - 1/2 ) - ( - √2 2 )( √3 2 )

= -√2 + √6 

= √6 - √2 

sin(135° - 120°) = √2 2 ( - 1/2 ) - ( - √2 2 )( √3 2 )

= -√2 + √6 

= √6 - √2 

---
### 📐 **Example 4**
Finding the Exact Value of an Expression Involving an Inverse Trigonometric Function Find the exact value of sin ( cos-1 1/2 + sin-1 3/5 ).

**Solution**

The pattern displayed in this problem is sin(α + β ). Let α = cos-1 1/2 and β = sin-1 3/5 . Then we can write


> **cos α = 1/2 , 0 ≤ α ≤ π**


sin β = 3/5 , - π/2 ≤ β ≤ π/2 We will use the Pythagorean identities to find sin α and cos β .


> **sin α = √1 - cos² α**


= √

1 - 1/4 

= √__

 3/4 

= √3/2 Using the sum formula for sine,


> **sin ( cos-1 1/2 + sin-1 3/5 ) = sin(α + β )**


> **= sin α cos β + cos α sin β**


= √3 2 · 4/5 + 1/2 · 3/5 

= 4√3 + 3 Using the Sum and Difference Formulas for Tangent Finding exact values for the tangent of the sum or difference of two angles is a little more complicated, but again, it is a matter of recognizing the pattern.
Finding the sum of two angles formula for tangent involves taking quotient of the sum formulas for sine and cosine and simplifying.
Recall, tan x = sin x cos x , cos x ≠ 0.
Let’s derive the sum formula for tangent.


> **tan(α + β ) = sin(α + β ) _ cos(α + β ) = sin α cos β + cos α sin β**


cos α cos β - sin α sin β 


> **= sin α cos β + cos α sin β**


cos α cos β cos α cos β - sin α sin β 


cos α cos β 

= sin α cos β cos α cos β + cos α sin β cos α cos β cos α cos β cos α cos β - sin α sin β cos α cos β 

= sin α cos α + sin β cos β 1 - sin α sin β cos α cos β 


> **= tan α + tan β**


1 - tan α tan β We can derive the difference formula for tangent in a similar way. cos β = √1 - sin² β 

= √ 1 - 9/25 

= √

 16/25 


= 4/5 Divide the numerator and denominator by cos α cos β


sum and difference formulas for tangent The sum and difference formulas for tangent are: tan(α + β ) = tan α + tan β 


> **1 - tan α tan β tan(α - β ) = tan α - tan β**


1 + tan α tan β 

---
### 💡 **How To…**
Given two angles, find the tangent of the sum of the angles. 1.
Write the sum formula for tangent. 2.
Substitute the given angles into the formula. 3.
Simplify.

---
### 📐 **Example 5**
Finding the Exact Value of an Expression Involving Tangent Find the exact value of tan ( π/6 + π/4 ).

**Solution**

Let’s first write the sum formula for tangent and substitute the given angles into the formula.


> **tan(α + β ) = tan α + tan β/1 - tan α tan β**


> **tan ( π/6 + π/4 ) = tan ( π/6 ) + tan ( π/4 )**


1 - ( tan ( π/6 )tan ( π/4 ) ) Next, we determine the individual tangents within the formulas:


> **tan ( π/6 ) = 1 _ √— 3 tan ( π/4 ) = 1 So we have**


> **tan( π/6 + π/4 ) = 1 _ √3 + 1/1 - ( 1 _ √3 )(1)**


= 1 + √3 _ √3 

 _ √3 - 1 _ √3 

 

= 1 + √3 _ √3 

( √3 _ √3 - 1 )

= √3 + 1 _ √3 - 1 

---
### ✏️ **Try It #3**
Find the exact value of tan ( 2π/3 + π/4 ).

---
### 📐 **Example 6**
Finding Multiple Sums and Differences of Angles Given sin α = 3/5 , 0 < α < π/2 , cos β = - 5/13 , π < β < 3π/2 , find a. sin(α + β ) b. cos(α + β ) c. tan(α + β ) d. tan(α - β )

**Solution**

We can use the sum and difference formulas to identify the sum or difference of angles when the ratio of sine, cosine, or tangent is provided for each of the individual angles.
To do so, we construct what is called a reference triangle to help find each component of the sum and difference formulas. a.
To find sin(α + β ), we begin with sin α = 3/5 and 0 < α < π/2 .
The side opposite α has length 3, the hypotenuse has length 5, and α is in the first quadrant.
See Figure 4.
Using the Pythagorean Theorem,we can find the length of side a:

a = 4 α y x Since cos β = - 5/13 and π < β < 3π/2 , the side adjacent to β is -5, the hypotenuse is 13, and β is in the third quadrant.
See Figure 5.
Again, using the Pythagorean Theorem, we have

a = ± 12 Since β is in the third quadrant, a = –12.
β y x The next step is finding the cosine of α and the sine of β .
The cosine of α is the adjacent side over the hypotenuse.
We can find it from the triangle in Figure 5: cos α = 4/5 .
We can also find the sine of β from the triangle in Figure 5, as opposite side over the hypotenuse: sin β = - 12/13 .
Now we are ready to evaluate sin(α + β ).


> **sin(α + β ) = sin α cos β + cos α sin β**


= ( 3/5 )( - 5/13 ) + ( 4/5 )( - 12/13 )

= - 15 __ __ 65 

= - 63/65 

b. We can find cos(α + β ) in a similar manner. We substitute the values according to the formula.


> **cos(α + β ) = cos α cos β - sin α sin β**


= ( 4/5 )( - 5/13 ) - ( 3/5 )( - 12/13 )

= - 20 __ __ 65 

= 16/65 


> **c. For tan(α + β ), if sin α = 3/5 and cos α = 4/5 , then**


> **tan α = 3/5/4/5 = 3/4 If sin β = - 12/13 and cos β = - 5/13 , then**


> **tan β = -12/13 _ -5/13 = 12/5 Then,**


tan(α + β ) = tan α + tan β/1 - tan α tan β = 3/4 + 12/5/1 - 3/4 ( 12/5 ) 

= 63/20 _ - 16/20 

= - 63/16 

d. To find tan(α - β ), we have the values we need. We can substitute them in and evaluate.

tan(α - β ) = tan α - tan β/1 + tan α tan β = 3/4 - 12/5/1 + 3/4 ( 12/5 ) 

= - 33/20/56/20 

= - 33/56 

**Analysis**
A common mistake when addressing problems such as this one is that we may be tempted to think that α and β are angles in the same triangle, which of course, they are not.
Also note that tan(α + β ) = sin(α + β ) cos(α + β ) 

Using Sum and Difference Formulas for Cofunctions Now that we can find the sine, cosine, and tangent functions for the sums and differences of angles, we can use them to do the same for their cofunctions.
You may recall from Right Triangle Trigonometry that, if the sum of two positive angles is π/2 , those two angles are complements, and the sum of the two acute angles in a right triangle is π/2 , so they are also complements.
In Figure 6, notice that if one of the acute angles is labeled as θ , then the other acute angle must be labeled ( π/2 - θ ).
Notice also that sin θ = cos ( π/2 - θ ): opposite over hypotenuse.
Thus, when two angles are complimentary, we can say that the sine of θ equals the cofunction of the complement of θ .
Similarly, tangent and cotangent are cofunctions, and secant and cosecant are cofunctions.
θ π – θ From these relationships, the cofunction identities are formed. cofunction identities The cofunction identities are summarized in Table 2. sin θ = cos ( π/2 - θ ) cos θ = sin ( π/2 - θ ) tan θ = cot ( π/2 - θ ) sec θ = csc ( π/2 - θ ) csc θ = sec ( π/2 - θ ) cot θ = tan ( π/2 - θ ) Notice that the formulas in the table may also be justified algebraically using the sum and difference formulas.
For example, using


> **cos(α - β ) = cos α cos β + sin α sin β , we can write**


> **cos ( π/2 - θ ) = cos π/2 cos θ + sin π/2 sin θ**


> **= (0)cos θ + (1)sin θ**


> **= sin θ**


---
### 📐 **Example 7**
Finding a Cofunction with the Same Value as the Given Expression Write tan π/9 in terms of its cofunction.

**Solution**


The cofunction of tan θ = cot ( π/2 - θ ). Thus,


> **tan ( π/9 ) = cot ( π/2 - π/9 )**


> **= cot ( 9π 18 - 2π 18 )**


> **= cot ( 7π 18 )**


---
### ✏️ **Try It #4**
Write sin π/7 in terms of its cofunction.
Using the Sum and Difference Formulas to Verify Identities Verifying an identity means demonstrating that the equation holds for all values of the variable.
It helps to be very familiar with the identities or to have a list of them accessible while working the problems.
Reviewing the general rules from Solving Trigonometric Equations with Identities may help simplify the process of verifying an identity.

---
### 💡 **How To…**
Given an identity, verify using sum and difference formulas. 1.
Begin with the expression on the side of the equal sign that appears most complex.
Rewrite that expression until it matches the other side of the equal sign.
Occasionally, we might have to alter both sides, but working on only one side is the most efficient. 2.
Look for opportunities to use the sum and difference formulas. 3.
Rewrite sums or differences of quotients as single quotients. 4.
If the process becomes cumbersome, rewrite the expression in terms of sines and cosines.

---
### 📐 **Example 8**:
Verifying an Identity Involving Sine


Verify the identity sin(α + β ) + sin(α - β ) = 2 sin α cos β .


**Solution**

We see that the left side of the equation includes the sines of the sum and the difference of angles. sin(α + β ) = sin α cos β + cos α sin β sin(α - β ) = sin α cos β - cos α sin β We can rewrite each using the sum and difference formulas. sin(α + β ) + sin(α - β ) = sin α cos β + cos α sin β + sin α cos β - cos α sin β 


= 2 sin α cos β We see that the identity is verified.


---
### 📐 **Example 9**:
Verifying an Identity Involving Tangent

Verify the following identity.


> **sin(α - β ) _ cos α cos β = tan α - tan β**


**Solution**

We can begin by rewriting the numerator on the left side of the equation.

 sin(α - β ) _ cos α cos β = sin α cos β - cos α sin β/cos α cos β 

= sin α cos β/cos α cos β - cos α sin β/cos α cos β Rewrite using a common denominator.


> **= sin α/cos α - sin β/cos β Cancel.**


= tan α - tan β Rewrite in terms of tangent.
We see that the identity is verified.
In many cases, verifying tangent identities can successfully be accomplished by writing the tangent in terms of sine and cosine.

---
### ✏️ **Try It #5**
Verify the identity: tan(π - θ ) = -tan θ .

---
### 📐 **Example 10**
Using Sum and Difference Formulas to Solve an Application Problem Let L¹ and L² denote two non-vertical intersecting lines, and let θ denote the acute angle between L¹ and L².
See Figure 7.
Show that tan θ = m² - m¹ _ 1 + m¹ m² where m¹ and m² are the slopes of L¹ and L² respectively.
(Hint: Use the fact that tan θ 1 = m¹ and tan θ 2 = m².) θ θ 1 θ 2 y x L¹ L²

**Solution**

Using the difference formula for tangent, this problem does not seem as daunting as it might.


> **tan θ = tan(θ 2 - θ 1)**


> **= tan θ 2 - tan θ 1/1 + tan θ 1 tan θ 2**


= m² - m¹ _ 

---
### 📐 **Example 11**:
Investigating a Guy-wire Problem

For a climbing wall, a guy-wire R is attached 47 feet high on a vertical pole.
Added support is provided by another guy-wire S attached 40 feet above ground on the same pole.
If the wires are attached to the ground 50 feet from the pole, find the angle α between the wires.
See Figure 8.
α β R S 47 f 40 f 50 f

**Solution**

Let’s first summarize the information we can gather from the diagram.
As only the sides adjacent to the right angle are known, we can use the tangent function.
Notice that tan β = 47/50 , and tan( β - α ) = 40/50 = 4/5 .
We can then use difference formula for tangent. tan(β - α ) = tan β - tan α/1 + tan β tan α 

Now, substituting the values we know into the formula, we have


> **4/5 = 47/50 - tan α __**


 50 tan α 

4 ( 1 + 47/50 tan α ) = 5( 47/50 - tan α ) Use the distributive property, and then simplify the functions.


> **4(1) + 4( 47/50 ) tan α = 5( 47/50 ) - 5tan α**


4 + 3.76tan α = 4.7 - 5tan α


5tan α + 3.76tan α = 0.7


Now we can calculate the angle in degrees.
π ) ≈ 4.57° Analysis Occasionally, when an application appears that includes a right triangle, we may think that solving is a matter of applying the Pythagorean Theorem.
That may be partially true, but it depends on what the problem is asking and what information is given.
Access these online resources for additional instruction and practice with sum and difference identities.
• Sum and Difference Identities for Cosine (http://openstaxcollege.org/l/sumdifcos) • Sum and Difference Identities for Sine (http://openstaxcollege.org/l/sumdifsin) • Sum and Difference Identities for Tangent (http://openstaxcollege.org/l/sumdiftan)

### 7.2 section EXERCISES

Verbal 1.
Explain the basis for the cofunction identities and when they apply. 2.
Is there only one way to evaluate cos ( 5π 4 ) ?
Explain how to set up the solution in two different ways, and then compute to make sure they give the same answer. 3.
Explain to someone who has forgotten the even-odd properties of sinusoidal functions how the addition and subtraction formulas can determine this characteristic for f(x) = sin(x) and g(x) = cos(x).
(Hint: 0 - x = -x) Algebraic For the following exercises, find the exact value. 4. cos ( 7π 12 ) 5. cos ( π/12 ) 6. sin ( 5π 12 ) 7. sin ( 11π 12 ) 8. tan ( - π/12 ) 9. tan ( 19π 12 ) For the following exercises, rewrite in terms of sin x and cos x.
10. sin ( x + 11π 6 ) 11. sin ( x - 3π 4 ) 12. cos ( x - 5π 6 ) 13. cos ( x + 2π 3 ) For the following exercises, simplify the given expression. 14. csc ( π/2 - t ) 15. sec ( π/2 - θ ) 16. cot ( π/2 - x ) 17. tan ( π/2 - x ) 18. sin(2x) cos(5x) - sin(5x) cos(2x) 19. tan ( 3/2 x ) - tan ( 7/5 x ) 1 + tan ( 3/2 x ) tan ( 7/5 x ) For the following exercises, find the requested information. 20.
Given that sin a = 2/3 and cos b = - 1/4 , with a and b both in the interval [ π/2 , π ) , find sin(a + b) and cos(a - b). 21.
Given that sin a = 4/5 , and cos b = 1/3 , with a and b both in the interval [ 0, π/2 ) , find sin(a - b) and cos(a + b).
For the following exercises, find the exact value of each expression. 22. sin ( cos-1(0) - cos-1 ( 1/2 ) ) 23. cos ( cos-1 ( √2 2 ) + sin- 1( √3 2 ) ) 24. tan ( sin-1( 1/2 ) - cos-1 ( 1/2 ) )

## 7.2 Section Exercises

---
Graphical For the following exercises, simplify the expression, and then graph both expressions as functions to verify the graphs are identical.
25. cos ( π/2 - x ) 26. sin(π - x) 27. tan ( π/3 + x ) 28. sin ( π/3 + x ) 29. tan ( π/4 - x ) 30. cos ( 7π 6 + x ) 31. sin ( π/4 + x ) 32. cos ( 5π 4 + x ) For the following exercises, use a graph to determine whether the functions are the same or different.
If they are the same, show why.
If they are different, replace the second function with one that is identical to the first.
(Hint: think 2x = x + x. ) 33. f(x) = sin(4x) - sin(3x)cos x, g(x) = sin x cos(3x) 34. f(x) = cos(4x) + sin x sin(3x), g(x) = -cos x cos(3x) 35. f(x) = sin(3x)cos(6x), g(x) = -sin(3x)cos(6x) 36. f(x) = sin(4x), g(x) = sin(5x)cos x - cos(5x)sin x 37. f(x) = sin(2x), g(x) = 2 sin x cos x 38. f(θ ) = cos(2θ ), g(θ ) = cos² θ - sin² θ 39. f(θ ) = tan(2θ ), g(θ ) = tan θ/1 + tan²θ 40. f(x) = sin(3x)sin x, g(x) = sin²(2x)cos² x - cos²(2x)sin² x 41. f(x) = tan(-x), g(x) = tan x - tan(2x)

__

1 - tan x tan(2x) Technology For the following exercises, find the exact value algebraically, and then confirm the answer with a calculator to the fourth decimal point.
Extensions For the following exercises, prove the identities provided. 47. tan ( x + π/4 ) = tan x + 1 1 - tan x 48. tan(a + b) tan(a - b) = sin a cos a + sin b cos b


sin a cos a - sin b cos b 49. cos(a + b) cos a cos b = 1 - tan a tan b 50. cos(x + y)cos(x - y) = cos² x - sin² y 51. cos(x + h) - cos x

 h = cos x cos h - 1/h - sin x sin (h)/(h) For the following exercises, prove or disprove the statements. 52. tan(u + v) = tan u + tan v


1 - tan u tan v 53. tan(u - v) = tan u - tan v


1 + tan u tan v 54. tan(x + y) __

1 + tan x tan x = tan x + tan y/1 - tan² x tan² y 55.
If α , β , and γ are angles in the same triangle, then prove or disprove sin(α + β ) = sin γ . 56.
If α , β , and γ are angles in the same triangle, then prove or disprove: tan α + tan β + tan γ = tan α tan β tan γ .

Learning Objectives
In this section, you will:
• Use double-angle formulas to find exact values.
• Use double-angle formulas to verify identities.
• Use reduction formulas to simplify an expression.
• Use half-angle formulas to find exact values.
