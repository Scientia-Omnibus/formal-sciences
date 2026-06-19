# Trigonometric Identities and Equations

## Introduction

Math is everywhere, even in places we might not immediately recognize. For example, mathematical relationships describe the transmission of images, light, and sound. The sinusoidal graph in Figure 1 models music playing on a phone, radio, or computer. Such graphs are described using trigonometric equations and functions. In this chapter, we discuss how to manipulate trigonometric equations algebraically by applying various formulas and trigonometric identities. We will also investigate some of the ways that trigonometric equations are used to model real-life phenomena.

Learning Objectives
In this section, you will:
• Verify the fundamental trigonometric identities.
• Simplify trigonometric expressions using algebra and the identities.

## 7.1 Solving Trigonometric Equations with Identities

In espionage movies, we see international spies with multiple passports, each claiming a different identity. However, we know that each of those passports represents the same person. The trigonometric identities act in a similar manner to multiple passports—there are many ways to represent the same trigonometric expression. Just as a spy will choose an Italian passport when traveling to Italy, we choose the identity that applies to the given scenario when solving a trigonometric equation. In this section, we will begin an examination of the fundamental trigonometric identities, including how we can verify them and how we can use them to simplify trigonometric expressions. Verifying the Fundamental Trigonometric Identities Identities enable us to simplify complicated expressions. They are the basic tools of trigonometry used in solving trigonometric equations, just as factoring, finding common denominators, and using special formulas are the basic tools of solving algebraic equations. In fact, we use algebraic techniques constantly to simplify trigonometric expressions. Basic properties and formulas of algebra, such as the difference of squares formula and the perfect squares formula, will simplify the work involved with trigonometric expressions and equations. We already know that all of the trigonometric functions are related because they all are defined in terms of the unit circle. Consequently, any trigonometric identity can be written in many ways. To verify the trigonometric identities, we usually start with the more complicated side of the equation and essentially rewrite the expression until it has been transformed into the same expression as the other side of the equation. Sometimes we have to factor expressions, expand expressions, find common denominators, or use other algebraic strategies to obtain the desired result. In this first section, we will work with the fundamental identities: the Pythagorean identities, the even-odd identities, the reciprocal identities, and the quotient identities. We will begin with the Pythagorean identities (see Table 1), which are equations involving trigonometric functions based on the properties of a right triangle. We have already seen and used the first of these identifies, but now we will also use additional identities. Pythagorean Identities sin^{2} \theta  + cos^{2} \theta  = 1 1 + cot^{2} \theta  = csc^{2} \theta  1 + tan^{2} \theta  = sec^{2} \theta 

The second and third identities can be obtained by manipulating the first. The identity 1 + cot^{2} \theta  = csc^{2} \theta  is found by rewriting the left side of the equation in terms of sine and cosine. Prove: 1 + cot^{2} \theta  = csc^{2} \theta 

1 + cot^{2} \theta  = ( 1 +  cos^{2} \theta  _____ sin^{2} \theta   ) Rewrite the left side.

= (  sin^{2} \theta  _____ sin^{2} \theta   ) + (  cos^{2} \theta  _____ sin^{2} \theta   ) Write both terms with the common denominator.

=  sin^{2} \theta  + cos^{2} \theta  ___________ sin^{2} \theta  

=  1 ____ sin^{2} \theta  

= csc^{2} \theta  Similarly, 1 + tan^{2} \theta  = sec^{2} \theta  can be obtained by rewriting the left side of this identity in terms of sine and cosine. This gives

1 + tan^{2} \theta  = 1 + (  sin \theta  ____ cos \theta   )

Rewrite left side.

= (  cos \theta  ____ cos \theta   ) + (  sin \theta  ____ cos \theta   )

Write both terms with the common denominator.

=  cos^{2} \theta  + sin^{2} \theta  ___________ cos^{2} \theta  

=  1 _____ cos^{2} \theta  

= sec^{2} \theta  The next set of fundamental identities is the set of even-odd identities. The even-odd identities relate the value of a trigonometric function at a given angle to the value of the function at the opposite angle and determine whether the identity is odd or even. (See Table 2). Even-Odd Identities tan(-\theta ) = -tan \theta  sin(-\theta ) = -sin \theta  cos(-\theta ) = cos \theta  cot(-\theta ) = -cot \theta  csc(-\theta ) = -csc \theta  sec(-\theta ) = sec \theta  Recall that an odd function is one in which f (-x) = -f (x) for all x in the domain of f. The sine function is an odd function because sin(-\theta ) = -sin \theta . The graph of an odd function is symmetric about the origin. For example, consider corresponding inputs of  \p\frac{i}{2}  and - \p\frac{i}{2} . The output of sin (  \p\frac{i}{2}  ) is opposite the output of sin ( - \p\frac{i}{2}  ). Thus,

sin (  \p\frac{i}{2}  ) = 1 and

sin ( - \p\frac{i}{2}  ) = -sin (  \p\frac{i}{2}  )

= -1 This is shown in Figure 2. x y \pi  2\pi  –2\pi  –\pi  \pi , \pi , f(x) = sin x Recall that an even function is one in which f (-x) = f (x) for all x in the domain of f

The graph of an even function is symmetric about the y-axis. The cosine function is an even function because cos(-\theta ) = cos \theta . For example, consider corresponding inputs  \p\frac{i}{4}  and - \p\frac{i}{4} . The output of cos (  \p\frac{i}{4}  ) is the same as the output of cos ( - \p\frac{i}{4}  ). Thus, cos ( - \p\frac{i}{4}  ) = cos (  \p\frac{i}{4}  )

See Figure 3. x y \pi  2\pi  –2\pi  –\pi  0.707 \pi  , 0.707 \pi  , f(x) = cos x For all \theta  in the domain of the sine and cosine functions, respectively, we can state the following: • Since sin(-\theta ) = -sin \theta , sine is an odd function. • Since, cos(-\theta ) = cos \theta , cosine is an even function. The other even-odd identities follow from the even and odd nature of the sine and cosine functions. For example, consider the tangent identity, tan(-\theta ) = -tan \theta . We can interpret the tangent of a negative angle as tan(-\theta ) =  sin(-\theta ) ______ cos(-\theta )  =  -sin \theta  ______ cos \theta   = -tan \theta . Tangent is therefore an odd function, which means that tan(-\theta ) = -tan(\theta ) for all \theta  in the domain of the tangent function. The cotangent identity, cot(-\theta ) = -cot \theta , also follows from the sine and cosine identities. We can interpret the cotangent of a negative angle as cot(-\theta ) =  cos(-\theta ) _______ sin(-\theta )  =  cos \theta  _____ -sin \theta   = -cot \theta . Cotangent is therefore an odd function, which means that cot(-\theta ) = -cot(\theta ) for all \theta  in the domain of the cotangent function. The cosecant function is the reciprocal of the sine function, which means that the cosecant of a negative angle will be interpreted as csc(-\theta ) =  ______ sin(-\theta )  =  _____ -sin \theta   = -csc \theta . The cosecant function is therefore odd. Finally, the secant function is the reciprocal of the cosine function, and the secant of a negative angle is interpreted as sec(-\theta ) =  ______ cos(-\theta )  =  1 ____ cos \theta   = sec \theta . The secant function is therefore even. To sum up, only two of the trigonometric functions, cosine and secant, are even. The other four functions are odd, verifying the even-odd identities. The next set of fundamental identities is the set of reciprocal identities, which, as their name implies, relate trigonometric functions that are reciprocals of each other. See Table 3. Reciprocal Identities sin \theta  =  1 ____ csc \theta   csc \theta  =  1 ____ sin \theta   cos \theta  =  1 ____ sec \theta   sec \theta  =  1 ____ cos \theta   tan \theta  =  1 ____ cot \theta   cot \theta  =  1 ____ tan \theta   The final set of identities is the set of quotient identities, which define relationships among certain trigonometric functions and can be very helpful in verifying other identities. See Table 4. Quotient Identities tan \theta  =  sin \theta  ____ cos \theta   cot \theta  =  cos \theta  ____ sin \theta  

The reciprocal and quotient identities are derived from the definitions of the basic trigonometric functions. summarizing trigonometric identities The Pythagorean identities are based on the properties of a right triangle.

cos^{2} \theta  + sin^{2} \theta  = 1

1 + cot^{2} \theta  = csc^{2} \theta 

1 + tan^{2} \theta  = sec^{2} \theta  The even-odd identities relate the value of a trigonometric function at a given angle to the value of the function at the opposite angle.

tan(-\theta ) = -tan \theta 

cot(-\theta ) = -cot \theta 

sin(-\theta ) = -sin \theta 

csc(-\theta ) = -csc \theta 

cos(-\theta ) = cos \theta 

sec(-\theta ) = sec \theta  The reciprocal identities define reciprocals of the trigonometric functions. sin \theta  =  1 ____ csc \theta   cos \theta  =  1 ____ sec \theta   tan \theta  =  1 ____ cot \theta   csc \theta  =  1 ____ sin \theta   sec \theta  =  1 ____ cos \theta   cot \theta  =  1 ____ tan \theta   The quotient identities define the relationship among the trigonometric functions. tan \theta  =  sin \theta  ____ cos \theta   cot \theta  =  cos \theta  ____ sin \theta  

**Example  1**

### Graphing the Equations of an Identity

Graph both sides of the identity cot \theta  =  1 ____ tan \theta  . In other words, on the graphing calculator, graph y = cot \theta  and y =  1 ____ tan \theta  .

**Solution**

See Figure 4. \theta  y \pi  \pi  3\pi  5\pi  = tan \theta  y = cot \theta  3\pi  – 5\pi 

Analysis We see only one graph because both expressions generate the same image. One is on top of the other. This is a good way to prove any identity. If both expressions give the same graph, then they must be identities.

**How To…**

Given a trigonometric identity, verify that it is true. 1. Work on one side of the equation. It is usually better to start with the more complex side, as it is easier to simplify than to build. 2. Look for opportunities to factor expressions, square a binomial, or add fractions. 3. Noting which functions are in the final expression, look for opportunities to use the identities and make the proper substitutions. 4. If these steps do not yield the desired result, try converting all terms to sines and cosines.

**Example  2**

### Verifying a Trigonometric Identity

Verify tan \theta  cos \theta  = sin \theta .

**Solution**

We will start on the left side, as it is the more complicated side: tan \theta cos \theta  = (  sin \theta  ____ cos \theta   ) cos \theta 

= (  sin \theta  ____ cos \theta   ) cos \theta 

= sin \theta  Analysis This identity was fairly simple to verify, as it only required writing tan \theta  in terms of sin \theta  and cos \theta .

**Try It #1**

Verify the identity csc \theta  cos \theta  tan \theta  = 1.

**Example  3**

### Verifying the Equivalency Using the Even-Odd Identities

Verify the following equivalency using the even-odd identities: (1 + sin x)[1 + sin(-x)] = cos^{2} x

**Solution**

Working on the left side of the equation, we have

(1 + sin x)[1 + sin(-x)] = (1 + sin x)(1 - sin x) Since sin(-x) = -sin x

= 1 - sin^{2} x Difference of squares

= cos^{2} x cos^{2} x = 1 - sin^{2} x

**Example  4**

### Verifying a Trigonometric Identity Involving sec^{2} \theta 

Verify the identity  sec^{2} \theta  - 1 ________ sec^{2} \theta   = sin^{2} \theta

**Solution**

As the left side is more complicated, let’s begin there.

 sec^{2} \theta  - 1 ________ sec^{2} \theta   =  (tan^{2} \theta  + 1) - 1

_____________ sec^{2} \theta   sec^{2} \theta  = tan^{2} \theta  + 1

=  tan^{2} \theta  _____ sec^{2} \theta  

= tan^{2} \theta  (  1 ____ sec^{2} \theta   )

= tan^{2} \theta (cos^{2} \theta ) cos^{2} \theta  =  1 ____ sec^{2} \theta  

= (  sin^{2} \theta  _____ cos^{2} \theta   )(cos^{2} \theta ) tan^{2} \theta  =  sin^{2} \theta  _____ cos^{2} \theta  

= (  sin^{2} \theta  _____ cos^{2} \theta   )(cos^{2} \theta )

= sin^{2} \theta 

There is more than one way to verify an identity. Here is another possibility. Again, we can start with the left side.

 sec^{2} \theta  - 1 ________ sec^{2} \theta   =  sec^{2} \theta  _____ sec^{2} \theta   -  1 ____ sec^{2} \theta  

= 1 - cos^{2} \theta 

= sin^{2} \theta  Analysis In the first method, we used the identity sec^{2} \theta  = tan^{2} \theta  + 1 and continued to simplify. In the second method, we split the fraction, putting both terms in the numerator over the common denominator. This problem illustrates that there are multiple ways we can verify an identity. Employing some creativity can sometimes simplify a procedure. As long as the substitutions are correct, the answer will be the same.

**Try It #2**

Show that  cot \theta  ____ csc \theta   = cos \theta .

**Example  5**

### Creating and Verifying an Identity

Create an identity for the expression 2tan \theta  sec \theta  by rewriting strictly in terms of sine.

**Solution**

There are a number of ways to begin, but here we will use the quotient and reciprocal identities to rewrite the expression:

2 tan \theta  sec \theta  = 2(  sin \theta  ____ cos \theta   )(  1 ____ cos \theta   )

=  2 sin \theta  _____ cos^{2} \theta  

=  2 sin \theta  ________ 1 - sin^{2} \theta   Substitute 1 - sin^{2} \theta  for cos^{2} \theta  Thus,

2tan \theta  sec \theta  =  2 sin \theta  ________ 1 - sin^{2} \theta  

**Example  6**

### Verifying an Identity Using Algebra and Even/Odd Identities

Verify the identity:

 sin^{2}(-\theta ) - cos^{2}(-\theta )

_________________

sin(-\theta ) - cos(-\theta )  = cos \theta  - sin \theta

**Solution**

Let’s start with the left side and simplify:

 sin^{2}(-\theta ) - cos^{2}(-\theta )

_________________

sin(-\theta ) - cos(-\theta )  =  [sin(-\theta )]2 - [cos(-\theta )]2

__________________

sin(-\theta ) - cos(-\theta ) 

=  (-sin \theta )^{2} - (cos \theta )^{2}

________________

-sin \theta  - cos \theta   sin(-x) = -sin x and cos(-x) = cos x

=  (sin \theta )^{2} - (cos \theta )^{2}

______________

-sin \theta  - cos \theta   Difference of squares

=  (sin \theta  - cos \theta )(sin \theta  + cos \theta )

______________________

-(sin \theta  + cos \theta ) 

=  (sin \theta  - cos \theta )(sin \theta  + cos \theta )

______________________

-(sin \theta  + cos \theta ) 

= cos \theta  - sin \theta 

**Try It #3**

Verify the identity  sin^{2} \theta  - 1

_____________

tan \theta  sin \theta  - tan \theta   =  sin \theta  + 1 _______ tan \theta  .

**Example  7**

### Verifying an Identity Involving Cosines and Cotangents

Verify the identity: (1 - cos^{2} x)(1 + cot^{2} x) = 1.

**Solution**

We will work on the left side of the equation

(1 - cos^{2} x)(1 + cot^{2} x) = (1 - cos^{2} x)( 1 +  cos^{2} x _____ sin^{2} x  )

= (1 - cos^{2} x)(  sin^{2} x _____ sin^{2} x  +  cos^{2} x _____ sin^{2} x  ) Find the common denominator.

= (1 - cos^{2} x)(  sin^{2} x + cos^{2} x

___________ sin^{2} x  )

= (sin^{2} x)(  1 ____ sin^{2} x  )

= 1 Using Algebra to Simplify Trigonometric Expressions We have seen that algebra is very important in verifying trigonometric identities, but it is just as critical in simplifying trigonometric expressions before solving. Being familiar with the basic properties and formulas of algebra, such as the difference of squares formula, the perfect square formula, or substitution, will simplify the work involved with trigonometric expressions and equations. For example, the equation (sin x + 1)(sin x - 1) = 0 resembles the equation (x + 1)(x - 1) = 0, which uses the factored form of the difference of squares. Using algebra makes finding a solution straightforward and familiar. We can set each factor equal to zero and solve. This is one example of recognizing algebraic patterns in trigonometric expressions or equations. Another example is the difference of squares formula, a^{2} - b^{2} = (a - b)(a + b), which is widely used in many areas other than mathematics, such as engineering, architecture, and physics. We can also create our own identities by continually expanding an expression and making the appropriate substitutions. Using algebraic properties and formulas makes many trigonometric equations easier to understand and solve.

**Example  8**

### Writing the Trigonometric Expression as an Algebraic Expression

Write the following trigonometric expression as an algebraic expression: 2cos^{2} \theta  + cos \theta  - 1.

**Solution**

Notice that the pattern displayed has the same form as a standard quadratic expression, ax^{2} + bx + c. Letting cos \theta  = x, we can rewrite the expression as follows: 2x^{2} + x - 1 This expression can be factored as (2x - 1)(x + 1). If it were set equal to zero and we wanted to solve the equation, we would use the zero factor property and solve each factor for x. At this point, we would replace x with cos \theta  and solve for \theta .

**Example  9**

Rewriting a Trigonometric Expression Using the Difference of Squares Rewrite the trigonometric expression: 4 cos^{2} \theta  - 1.

**Solution**

Notice that both the coefficient and the trigonometric expression in the first term are squared, and the square of the number 1 is 1. This is the difference of squares. Thus,

4 cos^{2} \theta  - 1 = (2 cos \theta )^{2} - 1

= (2 cos \theta  - 1)(2 cos \theta  + 1) Analysis If this expression were written in the form of an equation set equal to zero, we could solve each factor using the zero factor property. We could also use substitution like we did in the previous problem and let cos \theta  = x, rewrite the expression as 4x^{2} - 1, and factor (2x - 1)(2x + 1). Then replace x with cos \theta  and solve for the angle.

**Try It #4**

Rewrite the trigonometric expression: 25 - 9 sin^{2} \theta .

**Example  10**

Simplify by Rewriting and Using Substitution Simplify the expression by rewriting and using identities: csc^{2} \theta  - cot^{2} \theta

**Solution**

We can start with the Pythagorean Identity.

1 + cot^{2} \theta  = csc^{2} \theta  Now we can simplify by substituting 1 + cot^{2} \theta  for csc^{2} \theta . We have

csc^{2} \theta  - cot^{2} \theta  = 1 + cot^{2} \theta  - cot^{2} \theta 

= 1

**Try It #5**

Use algebraic techniques to verify the identity:  cos \theta  _______ 1 + sin \theta   =  1 - sin \theta  _______ cos \theta  . (Hint: Multiply the numerator and denominator on the left side by 1 - sin \theta .)

Access these online resources for additional instruction and practice with the fundamental trigonometric identities. • Fundamental Trigonometric Identities (http://openstaxcollege.org/l/funtrigiden) • Verifying Trigonometric Identities (http://openstaxcollege.org/l/verifytrigiden)

7.1 SECTION EXERCISES Verbal 1. We know g(x) = cos x is an even function, and f (x) = sin x and h(x) = tan x are odd functions. What about G(x) = cos^{2} x, F (x) = sin^{2} x, and H(x) = tan^{2} x? Are they even, odd, or neither? Why? 2. Examine the graph of f (x) = sec x on the interval [-\pi , \pi ]. How can we tell whether the function is even or odd by only observing the graph of f (x) = sec x? 3. After examining the reciprocal identity for sec t, explain why the function is undefined at certain points. 4. All of the Pythagorean identities are related. Describe how to manipulate the equations to get from sin^{2} t + cos^{2} t = 1 to the other forms. Algebraic For the following exercises, use the fundamental identities to fully simplify the expression. 5. sin x cos x sec x 6. sin(-x)cos(-x)csc(-x) 7. tan x sin x + sec x cos^{2} x 8. csc x + cos x cot(-x) 9.  cot t + tan t __________ sec(-t)  10. 3 sin^{3} t csc t + cos^{2} t + 2 cos(-t)cos t 11. -tan(-x)cot(-x) 12.  -sin(-x)cos x sec x csc x tan x

________________________

cot x  13.  1 + tan^{2} \theta  ________ csc^{2} \theta   + sin^{2} \theta  +  1 ____ sec^{2} \theta   14. (  tan x ____ csc^{2} x  +  tan x ____ sec^{2} x  )(  1 + tan x ________ 1 + cot x  ) -  1 _____ cos^{2} x  15.  1 - cos^{2} x ________ tan^{2} x + 2 sin^{2} x For the following exercises, simplify the first trigonometric expression by writing the simplified form in terms of the second expression. 16.  tan x + cot x __________ csc x ; cos x 17.  sec x + csc x __________ 1 + tan x ; sin x 18.  cos x _______ 1 + sin x  + tan x; cos x 19.  ________ sin x cos x  - cot x; cot x 20.  _______ 1 - cos x  -  cos x _______ 1 + cos x ; csc x 21. (sec x + csc x)(sin x + cos x) - 2 - cot x; tan x 22.  __________

csc x - sin x ; sec x and tan x 23.  1 - sin x _______ 1 + sin x  -  1 + sin x _______ 1 - sin x ; sec x and tan x 24. tan x; sec x 25. sec x; cot x 26. sec x; sin x 27. cot x; sin x 28. cot x; csc x For the following exercises, verify the identity. 29. cos x - cos^{3} x = cos x sin^{2} x 30. cos x(tan x - sec(-x)) = sin x - 1 31.  1 + sin^{2} x ________ cos^{2} x  =  1 _____ cos^{2} x  +  sin^{2} x _____ cos^{2} x  = 1 + 2 tan^{2} x 32. (sin x + cos x)^{2} = 1 + 2 sin x cos x 33. cos^{2} x - tan^{2} x = 2 - sin^{2} x - sec^{2} x

## 7.1 Section Exercises

Extensions For the following exercises, prove or disprove the identity. 34.  _______ 1 + cos x  -  ___________

1 - cos( - x)  = -2 cot x csc x 35. csc^{2} x(1 + sin^{2} x) = cot^{2} x 36. (  sec^{2}(-x) - tan^{2} x

______________ tan x  )(  2 + 2 tan x _________ 2 + 2 cot x  ) - 2 sin^{2} x = cos 2x 37.  tan x ____ sec x  sin(-x) = cos^{2} x 38.  sec(-x) __________

tan x + cot x  = -sin(-x) 39.  1 + sin x _______ cos x  =  cos x _________

1 + sin(-x)  For the following exercises, determine whether the identity is true or false. If false, find an appropriate equivalent expression. 40.  cos^{2} \theta  - sin^{2} \theta 

___________

1 - tan^{2} \theta   = sin^{2} \theta  41. 3 sin^{2} \theta  + 4 cos^{2} \theta  = 3 + cos^{2} \theta  42.  sec \theta  + tan \theta  __________

cot \theta  + cos \theta  = sec^{2} \theta 

Learning Objectives
In this section, you will:
• Use sum and difference formulas for cosine.
• Use sum and difference formulas for sine.
• Use sum and difference formulas for tangent.
• Use sum and difference formulas for cofunctions.
• Use sum and difference formulas to verify identities.

## 7.2 Sum and Difference Identities

How can the height of a mountain be measured? What about the distance from Earth to the sun? Like many seemingly impossible problems, we rely on mathematical formulas to find the answers. The trigonometric identities, commonly used in mathematical proofs, have had real-world applications for centuries, including their use in calculating long distances. The trigonometric identities we will examine in this section can be traced to a Persian astronomer who lived around 950 AD, but the ancient Greeks discovered these same formulas much earlier and stated them in terms of chords. These are special equations or postulates, true for all values input to the equations, and with innumerable applications. In this section, we will learn techniques that will enable us to solve problems such as the ones presented above. The formulas that follow will simplify many trigonometric expressions and equations. Keep in mind that, throughout this section, the term formula is used synonymously with the word identity. Using the Sum and Difference Formulas for Cosine Finding the exact value of the sine, cosine, or tangent of an angle is often easier if we can rewrite the given angle in terms of two angles that have known trigonometric values. We can use the special angles, which we can review in the unit circle shown in Figure 2. \pi  \pi  \pi  \pi  60° 4\pi  5\pi  7\pi  225° 240° 300° 315° 2\pi  \pi  3\pi  5\pi  7\pi  5\pi  150° 3\pi  2\pi  135° 11\pi  30° 45° 330° 210° 120°

We will begin with the sum and difference formulas for cosine, so that we can find the cosine of a given angle if we can break it up into the sum or difference of two of the special angles. See Table 1. Sum formula for cosine cos(\alpha  + \beta ) = cos \alpha  cos \beta  - sin \alpha  sin \beta  Difference formula for cosine cos(\alpha  - \beta ) = cos \alpha  cos \beta  + sin \alpha  sin \beta  First, we will prove the difference formula for cosines. Let’s consider two points on the unit circle. See Figure 3. Point P is at an angle \alpha  from the positive x-axis with coordinates (cos \alpha , sin \alpha ) and point Q is at an angle of \beta  from the positive x-axis with coordinates (cos \beta , sin \beta ). Note the measure of angle POQ is \alpha  - \beta . Label two more points: A at an angle of (\alpha  - \beta ) from the positive x-axis with coordinates (cos(\alpha  - \beta ), sin(\alpha  - \beta )); and point B with coordinates (1, 0). Triangle POQ is a rotation of triangle AOB and thus the distance from P to Q is the same as the distance from A to B. x y \pi  2\pi  –2\pi  –\pi  \pi , \pi , f(x) = sin x We can find the distance from P to Q using the distance formula.

dPQ = \sqrt{—}

(cos \alpha  - cos \beta )^{2} + (sin \alpha  - sin \beta )^{2} 

= \sqrt{———}

cos^{2} \alpha  - 2 cos \alpha  cos \beta  + cos^{2} \beta  + sin^{2} \alpha  - 2 sin \alpha  sin \beta  + sin^{2} \beta   Then we apply the Pythagorean Identity and simplify.

= \sqrt{———}

(cos^{2} \alpha  + sin^{2} \alpha ) + (cos^{2} \beta  + sin^{2} \beta ) - 2 cos \alpha  cos \beta  - 2 sin \alpha  sin \beta  

= \sqrt{—}

1 + 1 - 2 cos \alpha  cos \beta  - 2 sin \alpha  sin \beta  

= \sqrt{—}

2 - 2 cos \alpha  cos \beta  - 2 sin \alpha  sin \beta   Similarly, using the distance formula we can find the distance from A to B.

dAB = \sqrt{—}

(cos(\alpha  - \beta ) - 1)^{2} + (sin(\alpha  - \beta ) - 0)^{2} 

= \sqrt{——}

cos^{2}(\alpha  - \beta ) - 2 cos(\alpha  - \beta ) + 1 + sin^{2}(\alpha  - \beta )  Applying the Pythagorean Identity and simplifying we get:

= \sqrt{——}

(cos^{2}(\alpha  - \beta ) + sin^{2}(\alpha  - \beta )) - 2 cos(\alpha  - \beta ) + 1 

= \sqrt{—}

1 - 2 cos(\alpha  - \beta ) + 1 

= \sqrt{2} - 2 cos(\alpha  - \beta )  Because the two distances are the same, we set them equal to each other and simplify.

\sqrt{—}

2 - 2 cos \alpha  cos \beta  - 2 sin \alpha  sin \beta   = \sqrt{2} - 2 cos(\alpha  - \beta ) 

2 - 2 cos \alpha  cos \beta  - 2 sin \alpha  sin \beta  = 2 - 2 cos(\alpha  - \beta ) Finally we subtract 2 from both sides and divide both sides by -2.

cos \alpha  cos \beta  + sin \alpha  sin \beta  = cos(\alpha  - \beta ) Thus, we have the difference formula for cosine. We can use similar methods to derive the cosine of the sum of two angles.

sum and difference formulas for cosine These formulas can be used to calculate the cosine of sums and differences of angles. cos(\alpha  + \beta ) = cos \alpha  cos \beta  - sin \alpha  sin \beta  cos(\alpha  - \beta ) = cos \alpha  cos \beta  + sin \alpha  sin \beta 

**How To…**

Given two angles, find the cosine of the difference between the angles. 1. Write the difference formula for cosine. 2. Substitute the values of the given angles into the formula. 3. Simplify.

**Example  1**

Finding the Exact Value Using the Formula for the Cosine of the Difference of Two Angles Using the formula for the cosine of the difference of two angles, find the exact value of cos (  5\p\frac{i}{4}  -  \p\frac{i}{6}  ).

**Solution**

Use the formula for the cosine of the difference of two angles. We have

cos(\alpha  - \beta ) = cos \alpha  cos \beta  + sin \alpha  sin \beta 

cos (  5\pi  ___ 4  -  \p\frac{i}{6}  ) = cos (  5\pi  ___ 4  ) cos (  \p\frac{i}{6}  ) + sin (  5\pi  ___ 4  ) sin (  \p\frac{i}{6}  )

= ( -  \sqrt{2}  ____ 2  )(  \sqrt{3}  ____ 2  ) - (  \sqrt{2}  ____ 2  )(  \frac{1}{2}  )

= -  \sqrt{6}  ____ 4  -  \sqrt{2}  ____ 4 

=  -\sqrt{6}  - \sqrt{2}  __________ 

**Try It #1**

Find the exact value of cos (  \p\frac{i}{3}  -  \p\frac{i}{4}  ).

**Example  2**

Finding the Exact Value Using the Formula for the Sum of Two Angles for Cosine Find the exact value of cos(75°).

**Solution**

As 75° = 45° + 30°, we can evaluate cos(75°) as cos(45° + 30°). Thus,

cos(45° + 30°) = cos(45°)cos(30°) - sin(45°)sin(30°)

=  \sqrt{2}  ____ 2 (  \sqrt{3}  ____ 2  ) -  \sqrt{2}  ____ 2 (  \frac{1}{2}  )

=  \sqrt{6}  ____ 4  -  \sqrt{2}  ____ 4 

=  \sqrt{6}  - \sqrt{2}  __________ 

**Try It #2**

Find the exact value of cos(105°). Using the Sum and Difference Formulas for Sine The sum and difference formulas for sine can be derived in the same manner as those for cosine, and they resemble the cosine formulas.

sum and difference formulas for sine These formulas can be used to calculate the sines of sums and differences of angles. sin(\alpha  + \beta ) = sin \alpha  cos \beta  + cos \alpha  sin \beta  sin(\alpha  - \beta ) = sin \alpha  cos \beta  - cos \alpha  sin \beta 

**How To…**

Given two angles, find the sine of the difference between the angles. 1. Write the difference formula for sine. 2. Substitute the given angles into the formula. 3. Simplify.

**Example  3**

Using Sum and Difference Identities to Evaluate the Difference of Angles Use the sum and difference identities to evaluate the difference of the angles and show that part a equals part b. a. sin(45° - 30°) b. sin(135° - 120°)

**Solution**

a. Let’s begin by writing the formula and substitute the given angles.

sin(\alpha  - \beta ) = sin \alpha  cos \beta  - cos \alpha  sin \beta 

sin(45° - 30°) = sin(45°)cos(30°) - cos(45°)sin(30°) Next, we need to find the values of the trigonometric expressions.

sin(45°) =  \sqrt{2}  ____ 2 , cos(30°) =  \sqrt{3}  ____ 2 , cos(45°) =  \sqrt{2}  ____ 2 , sin(30°) =  \frac{1}{2}  Now we can substitute these values into the equation and simplify.

sin(45° - 30°) =  \sqrt{2}  ____ 2 (  \sqrt{3}  ____ 2  ) -  \sqrt{2}  ____ 2 (  \frac{1}{2}  )

=  \sqrt{6}  - \sqrt{2}  _________  b. Again, we write the formula and substitute the given angles.

sin(\alpha  - \beta ) = sin \alpha  cos \beta  - cos \alpha  sin \beta 

sin(135° - 120°) = sin(135°)cos(120°) - cos(135°)sin(120°) Next, we find the values of the trigonometric expressions. sin(135°) =  \sqrt{2}  ____ 2 , cos(120°) = - \frac{1}{2} , cos(135°) = - \sqrt{2}  ____ 2 , sin(120°) =  \sqrt{3}  ____ 2  Now we can substitute these values into the equation and simplify.

sin(135° - 120°) =  \sqrt{2}  ____ 2 ( - \frac{1}{2}  ) - ( -  \sqrt{2}  ____ 2  )(  \sqrt{3}  ____ 2  )

=  -\sqrt{2}  + \sqrt{6}  __________ 

=  \sqrt{6}  - \sqrt{2}  _________ 

sin(135° - 120°) =  \sqrt{2}  ____ 2 ( - \frac{1}{2}  ) - ( -  \sqrt{2}  ____ 2  )(  \sqrt{3}  ____ 2  )

=  -\sqrt{2}  + \sqrt{6}  __________ 

=  \sqrt{6}  - \sqrt{2}  _________ 

**Example  4**

Finding the Exact Value of an Expression Involving an Inverse Trigonometric Function Find the exact value of sin ( cos-1 \frac{1}{2}  + sin-1 \frac{3}{5}  ).

**Solution**

The pattern displayed in this problem is sin(\alpha  + \beta ). Let \alpha  = cos-1 \frac{1}{2}  and \beta  = sin-1 \frac{3}{5} . Then we can write

cos \alpha  =  \frac{1}{2} , 0 \le  \alpha  \le  \pi 

sin \beta  =  \frac{3}{5} , - \p\frac{i}{2}  \le  \beta  \le   \p\frac{i}{2}  We will use the Pythagorean identities to find sin \alpha  and cos \beta .

sin \alpha  = \sqrt{1} - cos^{2} \alpha  

= \sqrt{______}

1 -  \frac{1}{4}  

= \sqrt{__}

 \frac{3}{4}  

=  \sqrt{3}  _ 2  Using the sum formula for sine,

sin ( cos-1  \frac{1}{2}  + sin-1  \frac{3}{5}  ) = sin(\alpha  + \beta )

= sin \alpha  cos \beta  + cos \alpha  sin \beta 

=  \sqrt{3}  ____ 2  \cdot   \frac{4}{5}  +  \frac{1}{2}  \cdot   \frac{3}{5} 

=  4\sqrt{3}  + 3 ________  Using the Sum and Difference Formulas for Tangent Finding exact values for the tangent of the sum or difference of two angles is a little more complicated, but again, it is a matter of recognizing the pattern. Finding the sum of two angles formula for tangent involves taking quotient of the sum formulas for sine and cosine and simplifying. Recall, tan x =  sin x ____ cos x , cos x \neq  0. Let’s derive the sum formula for tangent.

tan(\alpha  + \beta ) =  sin(\alpha  + \beta ) _ cos(\alpha  + \beta )  =  sin \alpha  cos \beta  + cos \alpha  sin \beta 

__________________

cos \alpha  cos \beta  - sin \alpha  sin \beta  

=  sin \alpha  cos \beta  + cos \alpha  sin \beta 

__________________

cos \alpha  cos \beta    cos \alpha  cos \beta  - sin \alpha  sin \beta 

__________________

cos \alpha  cos \beta  

=  sin \alpha  cos \beta  ________ cos \alpha  cos \beta   +  cos \alpha  sin \beta  ________ cos \alpha  cos \beta    cos \alpha  cos \beta  _________ cos \alpha  cos \beta   -  sin \alpha  sin \beta  ________ cos \alpha  cos \beta  

=  sin \alpha  ____ cos \alpha   +  sin \beta  ____ cos \beta   1 -  sin \alpha  sin \beta  ________ cos \alpha  cos \beta  

=  tan \alpha  + tan \beta 

____________

1 - tan \alpha  tan \beta   We can derive the difference formula for tangent in a similar way. cos \beta  = \sqrt{1} - sin^{2} \beta  

= \sqrt{______} 1 -  \frac{9}{25}  

= \sqrt{___}

 \frac{16}{25}  

=  \frac{4}{5}  Divide the numerator and denominator by cos \alpha  cos \beta 

sum and difference formulas for tangent The sum and difference formulas for tangent are: tan(\alpha  + \beta ) =  tan \alpha  + tan \beta 

___________

1 - tan \alpha  tan \beta   tan(\alpha  - \beta ) =  tan \alpha  - tan \beta 

___________

1 + tan \alpha  tan \beta  

**How To…**

Given two angles, find the tangent of the sum of the angles. 1. Write the sum formula for tangent. 2. Substitute the given angles into the formula. 3. Simplify.

**Example  5**

Finding the Exact Value of an Expression Involving Tangent Find the exact value of tan (  \p\frac{i}{6}  +  \p\frac{i}{4}  ).

**Solution**

Let’s first write the sum formula for tangent and substitute the given angles into the formula.

tan(\alpha  + \beta ) =  tan \alpha  + tan \bet\frac{a}{1} - tan \alpha  tan \beta  

tan (  \p\frac{i}{6}  +  \p\frac{i}{4}  ) =  tan (  \p\frac{i}{6}  ) + tan (  \p\frac{i}{4}  )

___

1 - ( tan (  \p\frac{i}{6}  )tan (  \p\frac{i}{4}  ) )  Next, we determine the individual tangents within the formulas:

tan (  \p\frac{i}{6}  ) =  1 _ \sqrt{—} 3   tan (  \p\frac{i}{4}  ) = 1 So we have

tan(  \p\frac{i}{6}  +  \p\frac{i}{4}  ) =   1 _ \sqrt{3}   + \frac{1}{1} - (  1 _ \sqrt{3}   )(1) 

=   1 + \sqrt{3}  _ \sqrt{3} 

 _  \sqrt{3}  - 1 _ \sqrt{3} 

 

=  1 + \sqrt{3}  _ \sqrt{3} 

(  \sqrt{3}  _ \sqrt{3}  - 1  )

=  \sqrt{3}  + 1 _ \sqrt{3}  - 1 

**Try It #3**

Find the exact value of tan (  2\p\frac{i}{3}  +  \p\frac{i}{4}  ).

**Example  6**

Finding Multiple Sums and Differences of Angles Given sin \alpha  =  \frac{3}{5} , 0 < \alpha  <  \p\frac{i}{2} , cos \beta  = - \frac{5}{13} , \pi  < \beta  <  3\p\frac{i}{2} , find a. sin(\alpha  + \beta ) b. cos(\alpha  + \beta ) c. tan(\alpha  + \beta ) d. tan(\alpha  - \beta )


**Solution**

We can use the sum and difference formulas to identify the sum or difference of angles when the ratio of sine, cosine, or tangent is provided for each of the individual angles. To do so, we construct what is called a reference triangle to help find each component of the sum and difference formulas. a. To find sin(\alpha  + \beta ), we begin with sin \alpha  =  \frac{3}{5}  and 0 < \alpha  <  \p\frac{i}{2} . The side opposite \alpha  has length 3, the hypotenuse has length 5, and \alpha  is in the first quadrant. See Figure 4. Using the Pythagorean Theorem,we can find the length of side a:

a = 4 \alpha  y x Since cos \beta  = - \frac{5}{13}  and \pi  < \beta  <  3\p\frac{i}{2} , the side adjacent to \beta  is -5, the hypotenuse is 13, and \beta  is in the third quadrant. See Figure 5. Again, using the Pythagorean Theorem, we have

a = \pm 12 Since \beta  is in the third quadrant, a = –12. \beta  y x The next step is finding the cosine of \alpha  and the sine of \beta . The cosine of \alpha  is the adjacent side over the hypotenuse. We can find it from the triangle in Figure 5: cos \alpha  =  \frac{4}{5} . We can also find the sine of \beta  from the triangle in Figure 5, as opposite side over the hypotenuse: sin \beta  = - \frac{12}{13} . Now we are ready to evaluate sin(\alpha  + \beta ).

sin(\alpha  + \beta ) = sin \alpha cos \beta  + cos \alpha sin \beta 

= (  \frac{3}{5}  )( - \frac{5}{13}  ) + (  \frac{4}{5}  )( - \frac{12}{13}  )

= - 15 __ __ 65 

= - \frac{63}{65} 

b. We can find cos(\alpha  + \beta ) in a similar manner. We substitute the values according to the formula.

cos(\alpha  + \beta ) = cos \alpha  cos \beta  - sin \alpha  sin \beta 

= (  \frac{4}{5}  )( - \frac{5}{13}  ) - (  \frac{3}{5}  )( - \frac{12}{13}  )

= - 20 __ __ 65 

=  \frac{16}{65} 

c. For tan(\alpha  + \beta ), if sin \alpha  =  \frac{3}{5}  and cos \alpha  =  \frac{4}{5} , then

tan \alpha  =   \frac{3}{5} 

_  \frac{4}{5}   =  \frac{3}{4}  If sin \beta  = - \frac{12}{13}  and cos \beta  = - \frac{5}{13} , then

tan \beta  =   -\frac{12}{13}  _  -\frac{5}{13}   =  \frac{12}{5}  Then,

tan(\alpha  + \beta ) =  tan \alpha  + tan \bet\frac{a}{1} - tan \alpha  tan \beta   =   \frac{3}{4}  +  \frac{12}{5}  __

1 -  \frac{3}{4} (  \frac{12}{5}  ) 

=   \frac{63}{20}  _ - \frac{16}{20}  

= - \frac{63}{16} 

d. To find tan(\alpha  - \beta ), we have the values we need. We can substitute them in and evaluate.

tan(\alpha  - \beta ) =  tan \alpha  - tan \bet\frac{a}{1} + tan \alpha  tan \beta   =   \frac{3}{4}  -  \frac{12}{5}  __

1 + \frac{3}{4}  (  \frac{12}{5}  ) 

=  - \frac{33}{20}  _  \frac{56}{20}  

= - \frac{33}{56} 

**Analysis**
A common mistake when addressing problems such as this one is that we may be tempted to think that \alpha  and \beta  are angles in the same triangle, which of course, they are not. Also note that tan(\alpha  + \beta ) =  sin(\alpha  + \beta ) ________ cos(\alpha  + \beta ) 

Using Sum and Difference Formulas for Cofunctions Now that we can find the sine, cosine, and tangent functions for the sums and differences of angles, we can use them to do the same for their cofunctions. You may recall from Right Triangle Trigonometry that, if the sum of two positive angles is  \p\frac{i}{2} , those two angles are complements, and the sum of the two acute angles in a right triangle is  \p\frac{i}{2} , so they are also complements. In Figure 6, notice that if one of the acute angles is labeled as \theta , then the other acute angle must be labeled (  \p\frac{i}{2}  - \theta  ). Notice also that sin \theta  = cos (  \p\frac{i}{2}  - \theta  ): opposite over hypotenuse. Thus, when two angles are complimentary, we can say that the sine of \theta  equals the cofunction of the complement of \theta . Similarly, tangent and cotangent are cofunctions, and secant and cosecant are cofunctions. \theta  \pi  – \theta  From these relationships, the cofunction identities are formed. cofunction identities The cofunction identities are summarized in Table 2. sin \theta  = cos (  \p\frac{i}{2}  - \theta  ) cos \theta  = sin (  \p\frac{i}{2}  - \theta  ) tan \theta  = cot (  \p\frac{i}{2}  - \theta  ) sec \theta  = csc (  \p\frac{i}{2}  - \theta  ) csc \theta  = sec (  \p\frac{i}{2}  - \theta  ) cot \theta  = tan (  \p\frac{i}{2}  - \theta  ) Notice that the formulas in the table may also be justified algebraically using the sum and difference formulas. For example, using

cos(\alpha  - \beta ) = cos \alpha cos \beta  + sin \alpha sin \beta , we can write

cos (  \p\frac{i}{2}  - \theta  ) = cos \p\frac{i}{2}  cos \theta  + sin \p\frac{i}{2}  sin \theta 

= (0)cos \theta  + (1)sin \theta 

= sin \theta 

**Example  7**

Finding a Cofunction with the Same Value as the Given Expression Write tan  \p\frac{i}{9}  in terms of its cofunction.

**Solution**

The cofunction of tan \theta  = cot (  \p\frac{i}{2}  - \theta  ). Thus,

tan (  \p\frac{i}{9}  ) = cot (  \p\frac{i}{2}  -  \p\frac{i}{9}  )

= cot (  9\pi  ___ 18  -  2\pi  ___ 18  )

= cot (  7\pi  ___ 18  )

**Try It #4**

Write sin  \p\frac{i}{7}  in terms of its cofunction. Using the Sum and Difference Formulas to Verify Identities Verifying an identity means demonstrating that the equation holds for all values of the variable. It helps to be very familiar with the identities or to have a list of them accessible while working the problems. Reviewing the general rules from Solving Trigonometric Equations with Identities may help simplify the process of verifying an identity.

**How To…**

Given an identity, verify using sum and difference formulas. 1. Begin with the expression on the side of the equal sign that appears most complex. Rewrite that expression until it matches the other side of the equal sign. Occasionally, we might have to alter both sides, but working on only one side is the most efficient. 2. Look for opportunities to use the sum and difference formulas. 3. Rewrite sums or differences of quotients as single quotients. 4. If the process becomes cumbersome, rewrite the expression in terms of sines and cosines.

**Example  8**

### Verifying an Identity Involving Sine

Verify the identity sin(\alpha  + \beta ) + sin(\alpha  - \beta ) = 2 sin \alpha  cos \beta .

**Solution**

We see that the left side of the equation includes the sines of the sum and the difference of angles. sin(\alpha  + \beta ) = sin \alpha  cos \beta  + cos \alpha  sin \beta  sin(\alpha  - \beta ) = sin \alpha  cos \beta  - cos \alpha  sin \beta  We can rewrite each using the sum and difference formulas. sin(\alpha  + \beta ) + sin(\alpha  - \beta ) = sin \alpha  cos \beta  + cos \alpha  sin \beta  + sin \alpha  cos \beta  - cos \alpha  sin \beta 

= 2 sin \alpha  cos \beta  We see that the identity is verified.

**Example  9**

### Verifying an Identity Involving Tangent

Verify the following identity.

 sin(\alpha  - \beta ) _ cos \alpha  cos \beta   = tan \alpha  - tan \beta

**Solution**

We can begin by rewriting the numerator on the left side of the equation.

 sin(\alpha  - \beta ) _ cos \alpha  cos \beta   =  sin \alpha  cos \beta  - cos \alpha  sin \bet\frac{a}{c}os \alpha  cos \beta  

=  sin \alpha  cos \bet\frac{a}{c}os \alpha  cos \beta   -  cos \alpha  sin \bet\frac{a}{c}os \alpha  cos \beta   Rewrite using a common denominator.

=  sin \alph\frac{a}{c}os \alpha   -  sin \bet\frac{a}{c}os \beta   Cancel.

= tan \alpha  - tan \beta  Rewrite in terms of tangent. We see that the identity is verified. In many cases, verifying tangent identities can successfully be accomplished by writing the tangent in terms of sine and cosine.

**Try It #5**

Verify the identity: tan(\pi  - \theta ) = -tan \theta .

**Example  10**

Using Sum and Difference Formulas to Solve an Application Problem Let L^{1} and L^{2} denote two non-vertical intersecting lines, and let \theta  denote the acute angle between L^{1} and L^{2}. See Figure 7. Show that tan \theta  =  m^{2} - m^{1} _ 1 + m^{1} m^{2}  where m^{1} and m^{2} are the slopes of L^{1} and L^{2} respectively. (Hint: Use the fact that tan \theta 1 = m^{1} and tan \theta 2 = m^{2}.) \theta  \theta 1 \theta 2 y x L^{1} L^{2}

**Solution**

Using the difference formula for tangent, this problem does not seem as daunting as it might.

tan \theta  = tan(\theta 2 - \theta 1)

=  tan \theta 2 - tan \theta \frac{1}{1} + tan \theta 1 tan \theta 2 

=  m^{2} - m^{1} _ 

**Example  11**

### Investigating a Guy-wire Problem

For a climbing wall, a guy-wire R is attached 47 feet high on a vertical pole. Added support is provided by another guy-wire S attached 40 feet above ground on the same pole. If the wires are attached to the ground 50 feet from the pole, find the angle \alpha  between the wires. See Figure 8. \alpha  \beta  R S 47 f 40 f 50 f

**Solution**

Let’s first summarize the information we can gather from the diagram. As only the sides adjacent to the right angle are known, we can use the tangent function. Notice that tan \beta  =  \frac{47}{50} , and tan( \beta  - \alpha ) =  \frac{40}{50}  =  \frac{4}{5} . We can then use difference formula for tangent. tan(\beta  - \alpha ) =  tan \beta  - tan \alph\frac{a}{1} + tan \beta  tan \alpha  

Now, substituting the values we know into the formula, we have

 \frac{4}{5}  =   \frac{47}{50}  - tan \alpha  __

___ 50 tan \alpha  

4 ( 1 +  \frac{47}{50} tan \alpha  ) = 5(  \frac{47}{50}  - tan \alpha  ) Use the distributive property, and then simplify the functions.

4(1) + 4(  \frac{47}{50}  ) tan \alpha  = 5(  \frac{47}{50}  ) - 5tan \alpha 

4 + 3.76tan \alpha  = 4.7 - 5tan \alpha 

5tan \alpha  + 3.76tan \alpha  = 0.7

Now we can calculate the angle in degrees. ___ \pi   ) ≈ 4.57° Analysis Occasionally, when an application appears that includes a right triangle, we may think that solving is a matter of applying the Pythagorean Theorem. That may be partially true, but it depends on what the problem is asking and what information is given. Access these online resources for additional instruction and practice with sum and difference identities. • Sum and Difference Identities for Cosine (http://openstaxcollege.org/l/sumdifcos) • Sum and Difference Identities for Sine (http://openstaxcollege.org/l/sumdifsin) • Sum and Difference Identities for Tangent (http://openstaxcollege.org/l/sumdiftan)

### 7.2 section EXERCISES

Verbal 1. Explain the basis for the cofunction identities and when they apply. 2. Is there only one way to evaluate cos (  5\pi  ___ 4  ) ? Explain how to set up the solution in two different ways, and then compute to make sure they give the same answer. 3. Explain to someone who has forgotten the even-odd properties of sinusoidal functions how the addition and subtraction formulas can determine this characteristic for f(x) = sin(x) and g(x) = cos(x). (Hint: 0 - x = -x) Algebraic For the following exercises, find the exact value. 4. cos (  7\pi  ___ 12  ) 5. cos (  \p\frac{i}{12}  ) 6. sin (  5\pi  ___ 12  ) 7. sin (  11\pi  ___ 12  ) 8. tan ( - \p\frac{i}{12}  ) 9. tan (  19\pi  ___ 12  ) For the following exercises, rewrite in terms of sin x and cos x. 10. sin ( x +  11\pi  ___ 6  ) 11. sin ( x -  3\pi  ___ 4  ) 12. cos ( x -  5\pi  ___ 6  ) 13. cos ( x +  2\pi  ___ 3  ) For the following exercises, simplify the given expression. 14. csc (  \p\frac{i}{2}  - t ) 15. sec (  \p\frac{i}{2}  - \theta  ) 16. cot (  \p\frac{i}{2}  - x ) 17. tan (  \p\frac{i}{2}  - x ) 18. sin(2x) cos(5x) - sin(5x) cos(2x) 19. tan (  \frac{3}{2} x ) - tan (  \frac{7}{5} x ) 1 + tan (  \frac{3}{2} x ) tan (  \frac{7}{5} x ) For the following exercises, find the requested information. 20. Given that sin a =  \frac{2}{3}  and cos b = - \frac{1}{4} , with a and b both in the interval [  \p\frac{i}{2} , \pi  ) , find sin(a + b) and cos(a - b). 21. Given that sin a =  \frac{4}{5} , and cos b =  \frac{1}{3} , with a and b both in the interval [ 0,  \p\frac{i}{2}  ) , find sin(a - b) and cos(a + b). For the following exercises, find the exact value of each expression. 22. sin ( cos-1(0) - cos-1 (  \frac{1}{2}  ) ) 23. cos ( cos-1 (  \sqrt{2}  ____ 2  ) + sin- 1(  \sqrt{3}  ____ 2  ) ) 24. tan ( sin-1(  \frac{1}{2}  ) - cos-1 (  \frac{1}{2}  ) )

## 7.2 Section Exercises

Graphical For the following exercises, simplify the expression, and then graph both expressions as functions to verify the graphs are identical. 25. cos (  \p\frac{i}{2}  - x ) 26. sin(\pi  - x) 27. tan (  \p\frac{i}{3}  + x ) 28. sin (  \p\frac{i}{3}  + x ) 29. tan (  \p\frac{i}{4}  - x ) 30. cos (  7\pi  ___ 6  + x ) 31. sin (  \p\frac{i}{4}  + x ) 32. cos (  5\pi  ___ 4  + x ) For the following exercises, use a graph to determine whether the functions are the same or different. If they are the same, show why. If they are different, replace the second function with one that is identical to the first. (Hint: think 2x = x + x. ) 33. f(x) = sin(4x) - sin(3x)cos x, g(x) = sin x cos(3x) 34. f(x) = cos(4x) + sin x sin(3x), g(x) = -cos x cos(3x) 35. f(x) = sin(3x)cos(6x), g(x) = -sin(3x)cos(6x) 36. f(x) = sin(4x), g(x) = sin(5x)cos x - cos(5x)sin x 37. f(x) = sin(2x), g(x) = 2 sin x cos x 38. f(\theta ) = cos(2\theta ), g(\theta ) = cos^{2} \theta  - sin^{2} \theta  39. f(\theta ) = tan(2\theta ), g(\theta ) =  tan \thet\frac{a}{1} + tan^{2}\theta   40. f(x) = sin(3x)sin x, g(x) = sin^{2}(2x)cos^{2} x - cos^{2}(2x)sin^{2} x 41. f(x) = tan(-x), g(x) =  tan x - tan(2x)

__

1 - tan x tan(2x)  Technology For the following exercises, find the exact value algebraically, and then confirm the answer with a calculator to the fourth decimal point. Extensions For the following exercises, prove the identities provided. 47. tan ( x +  \p\frac{i}{4}  ) =  tan x + 1 ________ 1 - tan x  48.  tan(a + b) ________ tan(a - b)  =  sin a cos a + sin b cos b

__________________

sin a cos a - sin b cos b  49.  cos(a + b) ________ cos a cos b  = 1 - tan a tan b 50. cos(x + y)cos(x - y) = cos^{2} x - sin^{2} y 51.  cos(x + h) - cos x

______________ h  = cos x  cos h - \frac{1}{h}  - sin x sin \frac{h}{h}  For the following exercises, prove or disprove the statements. 52. tan(u + v) =  tan u + tan v

___________

1 - tan u tan v  53. tan(u - v) =  tan u - tan v

___________

1 + tan u tan v  54.  tan(x + y) __

1 + tan x tan x  =  tan x + tan \frac{y}{1} - tan^{2} x tan^{2} y  55. If \alpha , \beta , and \gamma  are angles in the same triangle, then prove or disprove sin(\alpha  + \beta ) = sin \gamma . 56. If \alpha , \beta , and \gamma  are angles in the same triangle, then prove or disprove: tan \alpha  + tan \beta  + tan \gamma  = tan \alpha  tan \beta  tan \gamma .

Learning Objectives
In this section, you will:
• Use double-angle formulas to find exact values.
• Use double-angle formulas to verify identities.
• Use reduction formulas to simplify an expression.
• Use half-angle formulas to find exact values.
