# Trigonometric Identities and Equations

## 7.3 Double-Angle, Half-Angle, and Reduction Formulas

Bicycle ramps made for competition (see Figure 1) must vary in height depending on the skill level of the competitors. For advanced competitors, the angle formed by the ramp and the ground should be \theta  such that tan \theta  =  \frac{5}{3} . The angle is divided in half for novices. What is the steepness of the ramp for novices ? In this section, we will investigate three additional categories of identities that we can use to answer questions such as this one. Using Double-Angle Formulas to Find Exact Values In the previous section, we used addition and subtraction formulas for trigonometric functions. Now, we take another look at those same formulas. The double-angle formulas are a special case of the sum formulas, where \alpha  = \beta . Deriving the double-angle formula for sine begins with the sum formula,

sin(\alpha  + \beta ) = sin \alpha  cos \beta  + cos \alpha  sin \beta  If we let \alpha  = \beta  = \theta , then we have

sin(\theta  + \theta ) = sin \theta  cos \theta  + cos \theta  sin \theta 

sin(2\theta ) = 2sin \theta  cos \theta  Deriving the double-angle for cosine gives us three options. First, starting from the sum formula, cos(\alpha  + \beta ) = cos \alpha  cos \beta  - sin \alpha  sin \beta , and letting \alpha  = \beta  = \theta , we have

cos(\theta  + \theta ) = cos \theta  cos \theta  - sin \theta  sin \theta 

cos(2\theta ) = cos^{2} \theta  - sin^{2} \theta  Using the Pythagorean properties, we can expand this double-angle formula for cosine and get two more interpretations. The first one is:

cos(2\theta ) = cos^{2} \theta  - sin^{2} \theta 

= (1 - sin^{2} \theta ) - sin^{2} \theta 

= 1 - 2sin^{2} \theta  The second interpretation is:

cos(2\theta ) = cos^{2} \theta  - sin^{2} \theta 

= cos^{2} \theta  - (1 - cos^{2} \theta )

= 2 cos^{2} \theta  - 1

Similarly, to derive the double-angle formula for tangent, replacing \alpha  = \beta  = \theta  in the sum formula gives tan(\alpha  + \beta ) =  tan \alpha  + tan \beta 

____________

1 - tan \alpha  tan \beta  

tan(\theta  + \theta ) =  tan \theta  + tan \theta 

___________

1 - tan \theta  tan \theta   tan(2\theta ) =  2tan \theta  ________ 1 - tan^{2} \theta   double-angle formulas The double-angle formulas are summarized as follows:

sin(2\theta ) = 2 sin \theta  cos \theta 

cos(2\theta ) = cos^{2} \theta  - sin^{2} \theta 

= 1 - 2 sin^{2} \theta 

= 2 cos^{2} \theta  - 1

tan(2\theta ) =  2 tan \theta  ________ 1 - tan^{2} \theta  

**How To…**

Given the tangent of an angle and the quadrant in which it is located, use the double-angle formulas to find the exact value. 1. Draw a triangle to reflect the given information. 2. Determine the correct double-angle formula. 3. Substitute values into the formula based on the triangle. 4. Simplify.

**Example  1**

Using a Double-Angle Formula to Find the Exact Value Involving Tangent Given that tan \theta  = - \frac{3}{4}  and \theta  is in quadrant II, find the following: a. sin(2\theta ) b. cos(2\theta ) c. tan(2\theta )

**Solution**

If we draw a triangle to reflect the information given, we can find the values needed to solve the problems on the image. We are given tan \theta  = - \frac{3}{4} , such that \theta  is in quadrant II. The tangent of an angle is equal to the opposite side over the adjacent side, and because \theta  is in the second quadrant, the adjacent side is on the x-axis and is negative. Use the Pythagorean Theorem to find the length of the hypotenuse:

(-4)^{2} + (3)^{2} = c^{2}

c = 5 Now we can draw a triangle similar to the one shown in Figure 2. x y \theta 

a. Let’s begin by writing the double-angle formula for sine.

sin(2\theta ) = 2 sin \theta  cos \theta  We see that we to need to find sin \theta  and cos \theta . Based on Figure 2, we see that the hypotenuse equals 5, so sin \theta  =  \frac{3}{5} , and cos \theta  = - \frac{4}{5} . Substitute these values into the equation, and simplify. Thus,

sin(2\theta ) = 2 (  \frac{3}{5}  )( - \frac{4}{5}  )

= - \frac{24}{b}. Write the double-angle formula for cosine.

cos(2\theta ) = cos^{2} \theta  - sin^{2} \theta  Again, substitute the values of the sine and cosine into the equation, and simplify.

cos(2\theta ) = ( - \frac{4}{5}  ) - (  \frac{3}{5}  )

=  \frac{16}{25}  -  \frac{9}{25} 

=  \frac{7}{25}  c. Write the double-angle formula for tangent.

tan(2\theta ) =  2 tan \theta  ________ 1 - tan^{2} \theta  

In this formula, we need the tangent, which we were given as tan \theta  = - \frac{3}{4} . Substitute this value into the equation, and simplify.

tan(2\theta ) =  2 ( - \frac{3}{4}  ) __

1 -( - \frac{3}{4}  ) 2  

=  - \frac{3}{2}  _ 1 -  \frac{9}{16}  

= - \frac{3}{2} (  \frac{16}{7}  )

= - \frac{24}{7} 

**Try It #1**

Given sin \alpha  =  \frac{5}{8} , with \theta  in quadrant I, find cos(2\alpha ).

**Example  2**

Using the Double-Angle Formula for Cosine without Exact Values Use the double-angle formula for cosine to write cos(6x) in terms of cos(3x).

**Solution**

cos(6x) = cos(2(3x))

= cos^{2} 3x - sin^{2} 3x

= 2cos^{2} 3x - 1

**Analysis**
This example illustrates that we can use the double-angle formula without having exact values. It emphasizes that the pattern is what we need to remember and that identities are true for all values in the domain of the trigonometric function. Using Double-Angle Formulas to Verify Identities Establishing identities using the double-angle formulas is performed using the same steps we used to derive the sum and difference formulas. Choose the more complicated side of the equation and rewrite it until it matches the other side.

**Example  3**

Using the Double-Angle Formulas to Establish an Identity Establish the following identity using double-angle formulas: 1 + sin(2\theta ) = (sin \theta  + cos \theta )^{2}


**Solution**

We will work on the right side of the equal sign and rewrite the expression until it matches the left side.

(sin \theta  + cos \theta )^{2} = sin^{2} \theta  + 2 sin \theta  cos \theta  + cos^{2} \theta 

= (sin^{2} \theta  + cos^{2} \theta ) + 2 sin \theta  cos \theta 

= 1 + 2 sin \theta  cos \theta 

= 1 + sin(2\theta )

**Analysis**
This process is not complicated, as long as we recall the perfect square formula from algebra:

(a \pm  b)^{2} = a^{2} \pm  2ab + b^{2} where a = sin \theta  and b = cos \theta . Part of being successful in mathematics is the ability to recognize patterns. While the terms or symbols may change, the algebra remains consistent.

**Try It #2**

Establish the identity: cos^{4} \theta  - sin^{4} \theta  = cos(2\theta ).

**Example  4**

### Verifying a Double-Angle Identity for Tangent

Verify the identity: tan(2\theta ) =  __________

cot \theta  - tan \theta

**Solution**

In this case, we will work with the left side of the equation and simplify or rewrite until it equals the right side of the equation.

tan(2\theta ) =  2 tan \theta  ________ 1 - tan^{2} \theta   Double-angle formula

=  2 tan \theta  (  1 ____ tan \theta   )

__

(1 - tan^{2} \theta )(  1 ____ tan \theta   )  Multiply by a term that results in desired numerator.

=  __

 1 ____ tan \theta   -  tan^{2} \theta  _____ tan \theta   

=  __________

cot \theta  - tan \theta   Use reciprocal identity for  1 ____ tan \theta  . Analysis Here is a case where the more complicated side of the initial equation appeared on the right, but we chose to work the left side. However, if we had chosen the left side to rewrite, we would have been working backwards to arrive at the equivalency. For example, suppose that we wanted to show

 2tan \theta  ________ 1 - tan^{2} \theta   =  __________

cot \theta  - tan \theta   Let’s work on the right side.

 __________

cot \theta  - tan \theta   =  __

 1 ____ tan \theta   - tan \theta   (  tan \theta  ____ tan \theta   )

=  2 tan \theta 

___

 \frac{1}{t}an \theta   (tan \theta ) - tan \theta (tan \theta ) 

=  2 tan \thet\frac{a}{1} - tan^{2} \theta   When using the identities to simplify a trigonometric expression or solve a trigonometric equation, there are usually several paths to a desired result. There is no set rule as to what side should be manipulated. However, we should begin with the guidelines set forth earlier.

**Try It #3**

Verify the identity: cos(2\theta )cos \theta  = cos^{3} \theta  - cos \theta  sin^{2} \theta .

Use Reduction Formulas to Simplify an Expression The double-angle formulas can be used to derive the reduction formulas, which are formulas we can use to reduce the power of a given expression involving even powers of sine or cosine. They allow us to rewrite the even powers of sine or cosine in terms of the first power of cosine. These formulas are especially important in higher-level math courses, calculus in particular. Also called the power-reducing formulas, three identities are included and are easily derived from the double-angle formulas. We can use two of the three double-angle formulas for cosine to derive the reduction formulas for sine and cosine. Let’s begin with cos(2\theta ) = 1 - 2 sin^{2} \theta . Solve for sin^{2} \theta :

cos(2\theta ) = 1 - 2 sin^{2} \theta 

2 sin^{2} \theta  = 1 - cos(2\theta )

sin^{2} \theta  =  1 - cos(2\theta ) _________  Next, we use the formula cos(2\theta ) = 2 cos^{2} \theta  - 1. Solve for cos^{2} \theta :

cos(2\theta ) = 2 cos^{2} \theta  - 1

1 + cos(2\theta ) = 2 cos^{2} \theta 

 1 + cos(2\theta ) _________  = cos^{2} \theta  The last reduction formula is derived by writing tangent in terms of sine and cosine:

tan^{2} \theta  =  sin^{2} \theta  _____ cos^{2} \theta  

=   1 - cos(2\theta ) _________  __

 1 + cos(2\theta ) _________   Substitute the reduction formulas.

= (  1 - cos(2\theta ) _________  )(  _________ 1 + cos(2\theta )  )

=  1 - cos(2\theta ) _________ 1 + cos(2\theta )  reduction formulas The reduction formulas are summarized as follows:

sin^{2} \theta  =  1 - cos(2\theta ) _________  cos^{2} \theta  =  1 + cos(2\theta ) _________  tan^{2} \theta  =  1 - cos(2\theta ) _________ 1 + cos(2\theta ) 

**Example  5**

### Writing an Equivalent Expression Not Containing Powers Greater Than 1

Write an equivalent expression for cos^{4} x that does not involve any powers of sine or cosine greater than 1.

**Solution**

We will apply the reduction formula for cosine twice.

cos^{4} x = (cos^{2} x)^{2}

= (  1 + cos(2x) _________  )  Substitute reduction formula for cos^{2} x.

=  \frac{1}{4} (1 + 2cos(2x) + cos^{2}(2x))

=  \frac{1}{4}  +  \frac{1}{2}  cos(2x) +  \frac{1}{4} (  1 + cos^{2}(2x) __________  ) Substitute reduction formula for cos^{2} x.

=  \frac{1}{4}  +  \frac{1}{2}  cos(2x) +  \frac{1}{8}  +  \frac{1}{8}  cos(4x)

=  \frac{3}{8}  +  \frac{1}{2}  cos(2x) +  \frac{1}{8}  cos(4x) Analysis The solution is found by using the reduction formula twice, as noted, and the perfect square formula from algebra.

**Example  6**

Using the Power-Reducing Formulas to Prove an Identity Use the power-reducing formulas to prove

sin^{3} (2x) = [  \frac{1}{2}  sin(2x) ] [1 - cos(4x)]

**Solution**

We will work on simplifying the left side of the equation:

sin^{3}(2x) = [sin(2x)][sin^{2}(2x)]

= sin(2x) [  1 - cos(4x) _________  ]  Substitute the power-reduction formula.

= sin(2x)(  \frac{1}{2}  )[1 - cos(4x)]

=  \frac{1}{2} [sin(2x)][1 - cos(4x)] Analysis Note that in this example, we substituted

 1 - cos(4x) _________  for sin^{2}(2x). The formula states

sin^{2} \theta  =  1 - cos(2\theta ) _________  We let \theta  = 2x, so 2\theta  = 4x.

**Try It #4**

Use the power-reducing formulas to prove that 10 cos^{4} x =  \frac{15}{4}  + 5 cos(2x) +  \frac{5}{4}  cos(4x). Using Half-Angle Formulas to Find Exact Values The next set of identities is the set of half-angle formulas, which can be derived from the reduction formulas and we can use when we have an angle that is half the size of a special angle. If we replace \theta  with  \alph\frac{a}{2} , the half-angle formula for sine is found by simplifying the equation and solving for sin (  \alph\frac{a}{2}  ). Note that the half-angle formulas are preceded by a \pm  sign. This does not mean that both the positive and negative expressions are valid. Rather, it depends on the quadrant in which  \alph\frac{a}{2}  terminates. The half-angle formula for sine is derived as follows:

sin^{2} \theta  =  1 - cos(2\theta ) _________ 

sin^{2} (  \alph\frac{a}{2}  ) =  1 - cos ( 2 ⋅  \alph\frac{a}{2}  )

__ 

=  1 - cos \alpha  ________ 

sin (  \alph\frac{a}{2}  ) = \pm \sqrt{_________}  1 - cos \alpha  ________   To derive the half-angle formula for cosine, we have

cos^{2} \theta  =  1 + cos(2\theta ) _________ 

cos^{2}(  \alph\frac{a}{2}  ) =  1 + cos ( 2 ⋅  \alph\frac{a}{2}  )

__ 

=  1 + cos \alpha  ________ 

cos (  \alph\frac{a}{2}  ) = \pm \sqrt{_________}  1 + cos \alpha  ________  

For the tangent identity, we have

tan^{2} \theta  =  1 - cos(2\theta ) _________ 1 + cos(2\theta ) 

tan^{2} (  \alph\frac{a}{2}  ) =  1 - cos( 2 ⋅  \alph\frac{a}{2}  )

__

1 + cos( 2 ⋅  \alph\frac{a}{2}  ) 

=  1 - cos \alpha  ________ 1 + cos \alpha  

tan (  \alph\frac{a}{2}  ) = \pm \sqrt{_________}  1 - cos \alph\frac{a}{1} + cos \alpha    half-angle formulas The half-angle formulas are as follows:

sin (  \alph\frac{a}{2}  ) = \pm \sqrt{_________}  1 - cos \alpha  ________  

cos (  \alph\frac{a}{2}  ) = \pm \sqrt{_________}  1 + cos \alpha  ________  

tan (  \alph\frac{a}{2}  ) = \pm \sqrt{_________}  1 - cos \alpha  ________ 1 + cos \alpha   

=  sin \alpha  ________ 1 + cos \alpha  

=  1 - cos \alpha  ________ sin \alpha  

**Example  7**

Using a Half-Angle Formula to Find the Exact Value of a Sine Function Find sin(15°) using a half-angle formula.

**Solution**

Since 15° =  30° ___ 2  , we use the half-angle formula for sine:

sin  30° ___ 2  = \sqrt{__________}  1 - cos^{3}0° _________  

= \sqrt{1} -  \sqrt{3}  _ 2  _  

= \sqrt{2} - \sqrt{3}  _______  _  

= \sqrt{________}  2 - \sqrt{3}  _______  

=  \sqrt{_______} 2 - \sqrt{3}   _  Analysis Notice that we used only the positive root because sin(15°) is positive.

**How To…**

Given the tangent of an angle and the quadrant in which the angle lies, find the exact values of trigonometric functions of half of the angle. 1. Draw a triangle to represent the given information. 2. Determine the correct half-angle formula. 3. Substitute values into the formula based on the triangle. 4. Simplify.

**Example  8**

Finding Exact Values Using Half-Angle Identities Given that tan \alpha  =  \frac{8}{15}  and \alpha  lies in quadrant III, find the exact value of the following: a. sin (  \alph\frac{a}{2}  ) b. cos (  \alph\frac{a}{2}  ) c. tan (  \alph\frac{a}{2}  )

**Solution**

Using the given information, we can draw the triangle shown in Figure 3. Using the Pythagorean Theorem, we find the hypotenuse to be 17. Therefore, we can calculate sin \alpha  = - \frac{8}{17}  and cos \alpha  = - \frac{15}{17} . x y \alpha  a. Before we start, we must remember that, if \alpha  is in quadrant III, then 180° < \alpha  < 270°, so  180° ____ 2  <  \alph\frac{a}{2}  <  270° ____ 2 . This means that the terminal side of  \alph\frac{a}{2}  is in quadrant II, since 90° <  \alph\frac{a}{2}  < 135°. To find sin  \alph\frac{a}{2} , we begin by writing the half-angle formula for sine. Then we substitute the value of the cosine we found from the triangle in Figure 3 and simplify.

sin  \alph\frac{a}{2}  = \pm  \sqrt{_________}  1 - cos \alpha  _  

= \pm  \sqrt{1} -( - \frac{15}{17}  ) __  

= \pm  \sqrt{32} _ \frac{17}{2}  

= \pm  \sqrt{______}

 \frac{32}{17}  \cdot   \frac{1}{2}  

= \pm  \sqrt{___}

 \frac{16}{17}  

= \pm   4 _ \sqrt{17}  

=  4\sqrt{17}  _  We choose the positive value of sin  \alph\frac{a}{2}  because the angle terminates in quadrant II and sine is positive in quadrant II. b. To find cos  \alph\frac{a}{2} , we will write the half-angle formula for cosine, substitute the value of the cosine we found from the triangle in Figure 3, and simplify.

cos (  \alph\frac{a}{2}  ) = \pm  \sqrt{__________}  1 + cos \alpha  ________  

= \pm  \sqrt{1} + ( - 15 ___ 17  ) __  

= \pm  \sqrt{2} _ \frac{17}{2}  

= \pm  \sqrt{______}  \frac{2}{17}  \cdot  \frac{1}{2}  

= \pm  \sqrt{___}

 \frac{1}{17}  

= -  \sqrt{17}  _ 17  We choose the negative value of cos  \alph\frac{a}{2}  because the angle is in quadrant II because cosine is negative in quadrant II. c. To find tan  \alph\frac{a}{2} , we write the half-angle formula for tangent. Again, we substitute the value of the cosine we found from the triangle in Figure 3 and simplify.

tan  \alph\frac{a}{2}  = \pm  \sqrt{_________}  1 - cos \alph\frac{a}{1} + cos \alpha   

= \pm  \sqrt{1} - ( - \frac{15}{17}  )

__

1 + ( - \frac{15}{17}  )  

= \pm  \sqrt{32} _ \frac{17}{2} _    = \pm \sqrt{___}

 \frac{32}{2}  

= -\sqrt{16} 

= -4 We choose the negative value of tan  \alph\frac{a}{2}  because  \alph\frac{a}{2}  lies in quadrant II, and tangent is negative in quadrant II.

**Try It #5**

Given that sin \alpha  = - \frac{4}{5}  and \alpha  lies in quadrant IV, find the exact value of cos (  \alph\frac{a}{2}  ).

**Example  9**

Finding the Measurement of a Half Angle Now, we will return to the problem posed at the beginning of the section. A bicycle ramp is constructed for high-level competition with an angle of \theta  formed by the ramp and the ground. Another ramp is to be constructed half as steep for novice competition. If tan \theta  =  \frac{5}{3}  for higher-level competition, what is the measurement of the angle for novice competition?

**Solution**

Since the angle for novice competition measures half the steepness of the angle for the high-level competition, and tan \theta  =  \frac{5}{3}  for high-level competition, we can find cos \theta  from the right triangle and the Pythagorean theorem so that we can use the half-angle identities. See Figure 4.

c = \sqrt{34}  \theta  We see that cos \theta  =  3 _ \sqrt{34}   =  3\sqrt{34}  _ 34 . We can use the half-angle formula for tangent: tan  \thet\frac{a}{2}  = \sqrt{_________}  1 - cos \thet\frac{a}{1} + cos \theta   . Since tan \theta  is in the first quadrant, so is tan  \thet\frac{a}{2} . Thus,

tan  \thet\frac{a}{2}  =  \sqrt{1} -  3\sqrt{34}  _ \frac{34}{1} +  3\sqrt{34}  _ 34   

=  \sqrt{34} - 3\sqrt{34}  __  __  34 + 3\sqrt{34}  __

   = \sqrt{___________}  34 - 3\sqrt{34}  __________ 34   

We can take the inverse tangent to find the angle: tan-1 (0.57) ≈ 29.7°. So the angle of the ramp for novice competition Access these online resources for additional instruction and practice with double-angle, half-angle, and reduction formulas. • Double-Angle Identities (http://openstaxcollege.org/l/doubleangiden) • Half-Angle Identities (http://openstaxcollege.org/l/halfangleident)

### 7.3 section EXERCISES

Verbal 1. Explain how to determine the reduction identities from the double-angle identity cos(2x) = cos^{2} x - sin^{2} x. 2. Explain how to determine the double-angle formula for tan(2x) using the double-angle formulas for cos(2x) and sin(2x). 3. We can determine the half-angle formula for tan  (  \frac{x}{2}  ) = \pm   \sqrt{1} - cos x  __

\sqrt{1} + cos x   by dividing the formula for sin (  \frac{x}{2}  ) by cos (  \frac{x}{2}  ). Explain how to determine two formulas for tan (  \frac{x}{2}  ) that do not involve any square roots. 4. For the half-angle formula given in the previous exercise for tan (  \frac{x}{2}  ), explain why dividing by 0 is not a concern. (Hint: examine the values of cos x necessary for the denominator to be 0.) Algebraic For the following exercises, find the exact values of a) sin(2x), b) cos(2x), and c) tan(2x) without solving for x. 5. If sin x =  \frac{1}{8} , and x is in quadrant I. 6. If cos x =  \frac{2}{3} , and x is in quadrant I. 7. If cos x = - \frac{1}{2} , and x is in quadrant III. 8. If tan x = -8, and x is in quadrant IV. For the following exercises, find the values of the six trigonometric functions if the conditions provided hold. 9. cos(2\theta ) = \frac{3}{5}  and 90° \le  \theta  \le  180° 10. cos(2\theta ) =  1 _ \sqrt{2}  and 180° \le  \theta  \le  270° For the following exercises, simplify to one trigonometric expression. 11. 2 sin (  \p\frac{i}{4}  ) 2 cos (  \p\frac{i}{4}  ) 12. 4 sin (  \p\frac{i}{8}  ) cos (  \p\frac{i}{8}  ) For the following exercises, find the exact value using half-angle formulas. 13. sin (  \p\frac{i}{8}  ) 14. cos ( - 11\pi  ___ 12  ) 15. sin (  11\pi  ___ 12  ) 16. cos (  7\pi  ___ 8  ) 17. tan (  5\pi  ___ 12  ) 18. tan ( - 3\pi  ___ 12  ) 19. tan ( - 3\pi  ___ 8  ) For the following exercises, find the exact values of a) sin (  \frac{x}{2}  ), b) cos (  \frac{x}{2}  ), and c) tan (  \frac{x}{2}  ) without solving for x, when 20. If tan x = - \frac{4}{3} , and x is in quadrant IV. 21. If sin x = - \frac{12}{13} , and x is in quadrant III. 22. If csc x = 7, and x is in quadrant II. 23. If sec x = -4, and x is in quadrant II.

## 7.3 Section Exercises

For the following exercises, use Figure 5 to find the requested half and double angles. \theta  \alpha  24. Find sin(2\theta ), cos(2\theta ), and tan(2\theta ). 25. Find sin(2\alpha ), cos(2\alpha ), and tan(2\alpha ). 26. Find sin (  \thet\frac{a}{2}  ), cos (  \thet\frac{a}{2}  ), and tan (  \thet\frac{a}{2}  ). 27. Find sin (  \alph\frac{a}{2}  ), cos (  \alph\frac{a}{2}  ), and tan (  \alph\frac{a}{2}  ). For the following exercises, simplify each expression. Do not evaluate. 28. cos^{2}(28°) - sin^{2}(28°) 31. cos^{2}(9x) - sin^{2}(9x) 32. 4 sin(8x) cos(8x) 33. 6 sin(5x) cos(5x) For the following exercises, prove the identity given. 34. (sin t - cos t)^{2} = 1 - sin(2t) 35. sin(2x) = -2 sin(-x) cos(-x) 36. cot x - tan x = 2 cot(2x) 37.  sin(2\theta ) _________ 1 + cos(2\theta ) tan^{2} \theta  = tan^{3} \theta  For the following exercises, rewrite the expression with an exponent no higher than 1. 42. cos^{2} x sin^{4} x 43. cos^{4} x sin^{2} x 44. tan^{2} x sin^{2} x Technology For the following exercises, reduce the equations to powers of one, and then check the answer graphically. 47. sin^{2} x cos^{2} x 48. tan^{2} x sin x 49. tan^{4} x cos^{2} x 50. cos^{2} x sin(2x) 51. cos^{2} (2x)sin x 52. tan^{2} (  \frac{x}{2}  ) sin x For the following exercises, algebraically find an equivalent function, only in terms of sin x and/or cos x, and then check the answer by graphing both equations. 53. sin(4x) 54. cos(4x) Extensions For the following exercises, prove the identities. 55. sin(2x) =  2 tan x ________ 1 + tan^{2} x  56. cos(2\alpha ) =  1 - tan^{2} \alpha  ________ 1 + tan^{2} \alpha   57. tan(2x) =  2 sin x cos x _________ 2 cos^{2} x - 1  58. (sin^{2} x - 1)^{2} = cos(2x) + sin^{4} x 59. sin(3x) = 3 sin x cos^{2} x - sin^{3} x 60. cos(3x) = cos^{3} x - 3 sin^{2} x cos x 61.  1 + cos(2t) ___________

sin(2t) - cos t  =  2 cos t ________ 2 sin t - 1  62. sin(16x) = 16 sin x cos x cos(2x)cos(4x)cos(8x) 63. cos(16x) = (cos^{2} (4x) - sin^{2} (4x) - sin(8x))(cos^{2} (4x) - sin^{2} (4x) + sin(8x))

Learning Objectives
In this section, you will:
• Express products as sums.
• Express sums as products.

## 7.4 Sum-to-Product and Product-to-Sum Formulas

A band marches down the field creating an amazing sound that bolsters the crowd. That sound travels as a wave that can be interpreted using trigonometric functions. For example, Figure 2 represents a sound wave for the musical note A. In this section, we will investigate trigonometric identities that are the foundation of everyday phenomena such as sound waves. 0.002 0.004 0.006 0.008 0.01 x y Expressing Products as Sums We have already learned a number of formulas useful for expanding or simplifying trigonometric expressions, but sometimes we may need to express the product of cosine and sine as a sum. We can use the product-to-sum formulas, which express products of trigonometric functions as sums. Let’s investigate the cosine identity first and then the sine identity. Expressing Products as Sums for Cosine We can derive the product-to-sum formula from the sum and difference identities for cosine. If we add the two equations, we get:

cos \alpha  cos \beta  + sin \alpha  sin \beta  = cos(\alpha  - \beta )

+ cos \alpha  cos \beta  - sin \alpha  sin \beta  = cos(\alpha  + \beta )

2 cos \alpha  cos \beta  = cos(\alpha  - \beta ) + cos(\alpha  + \beta ) Then, we divide by 2 to isolate the product of cosines:

cos \alpha  cos \beta  =  \frac{1}{2} [cos(\alpha  - \beta ) + cos(\alpha  + \beta )]

**How To…**

Given a product of cosines, express as a sum. 1. Write the formula for the product of cosines. 2. Substitute the given angles into the formula. 3. Simplify.

**Example  1**

### Writing the Product as a Sum Using the Product-to-Sum Formula for Cosine

Write the following product of cosines as a sum: 2 cos (  7\frac{x}{2}  ) cos  3\frac{x}{2} .

**Solution**

We begin by writing the formula for the product of cosines:

cos \alpha  cos \beta  =  \frac{1}{2} [cos(\alpha  - \beta ) + cos(\alpha  + \beta )] We can then substitute the given angles into the formula and simplify.

2 cos (  7\frac{x}{2}  ) cos (  3\frac{x}{2}  ) = (2)(  \frac{1}{2}  )[ cos (  7\frac{x}{2}  -  3\frac{x}{2}  ) + cos (  7\frac{x}{2}  +  3\frac{x}{2}  ) ] 

= [ cos (  4\frac{x}{2}  ) + cos (  10x ___ 2  ) ] 

= cos 2x + cos 5x

**Try It #1**

Use the product-to-sum formula to write the product as a sum or difference: cos(2\theta )cos(4\theta ). Expressing the Product of Sine and Cosine as a Sum Next, we will derive the product-to-sum formula for sine and cosine from the sum and difference formulas for sine. If we add the sum and difference identities, we get: sin(\alpha  + \beta ) = sin \alpha  cos \beta  + cos \alpha  sin \beta  + sin(\alpha  - \beta ) = sin \alpha  cos \beta  - cos \alpha  sin \beta 

sin(\alpha  + \beta ) + sin(\alpha  - \beta ) = 2 sin \alpha  cos \beta  Then, we divide by 2 to isolate the product of cosine and sine:

sin \alpha  cos \beta  =  \frac{1}{2} [sin(\alpha  +\beta ) + sin(\alpha  - \beta )]

**Example  2**

### Writing the Product as a Sum Containing only Sine or Cosine

Express the following product as a sum containing only sine or cosine and no products: sin(4\theta )cos(2\theta ).

**Solution**

Write the formula for the product of sine and cosine. Then substitute the given values into the formula and simplify.

sin \alpha  cos \beta  =  \frac{1}{2} [sin(\alpha  + \beta ) + sin(\alpha  - \beta )]

sin(4\theta )cos(2\theta ) =  \frac{1}{2} [sin(4\theta  + 2\theta ) + sin(4\theta  - 2\theta )]

=  \frac{1}{2} [sin(6\theta ) + sin(2\theta )]

**Try It #2**

Use the product-to-sum formula to write the product as a sum: sin(x + y)cos(x - y).

### Expressing Products of Sines in Terms of Cosine

Expressing the product of sines in terms of cosine is also derived from the sum and difference identities for cosine. In this case, we will first subtract the two cosine formulas: cos(\alpha  - \beta ) = cos \alpha  cos \beta  + sin \alpha  sin \beta  - cos(\alpha  + \beta ) = - (cos \alpha  cos \beta  - sin \alpha  sin \beta )

cos(\alpha  - \beta ) - cos(\alpha  + \beta ) = 2 sin \alpha  sin \beta  Then, we divide by 2 to isolate the product of sines:

sin \alpha  sin \beta  =  \frac{1}{2} [cos(\alpha  - \beta ) - cos(\alpha  + \beta )] Similarly we could express the product of cosines in terms of sine or derive other product-to-sum formulas. the product-to-sum formulas The product-to-sum formulas are as follows: cos \alpha  cos \beta  =  \frac{1}{2} [cos(\alpha  - \beta ) + cos(\alpha  + \beta )] sin \alpha  cos \beta  =  \frac{1}{2} [sin(\alpha  + \beta ) + sin(\alpha  - \beta )] sin \alpha  sin \beta  =  \frac{1}{2} [cos(\alpha  - \beta ) - cos(\alpha  + \beta )] cos \alpha  sin \beta  =  \frac{1}{2} [sin(\alpha  + \beta ) - sin(\alpha  - \beta )]

**Example  3**

Express the Product as a Sum or Difference Write cos(3\theta ) cos(5\theta ) as a sum or difference.

**Solution**

We have the product of cosines, so we begin by writing the related formula. Then we substitute the given angles and simplify.

cos \alpha  cos \beta  =  \frac{1}{2} [cos(\alpha  - \beta ) + cos(\alpha  + \beta )]

cos(3\theta )cos(5\theta ) =  \frac{1}{2} [cos(3\theta  - 5\theta ) + cos(3\theta  + 5\theta )]

=  \frac{1}{2} [cos(2\theta ) + cos(8\theta )] Use even-odd identity.

**Try It #3**

Use the product-to-sum formula to evaluate cos  11\pi  ___ 12  cos  \p\frac{i}{12} . Expressing Sums as Products Some problems require the reverse of the process we just used. The sum-to-product formulas allow us to express sums of sine or cosine as products. These formulas can be derived from the product-to-sum identities. For example, with a few substitutions, we can derive the sum-to-product identity for sine. Let  u + v _____  = \alpha  and  u - v _____ 2 = \beta . Then,

\alpha  + \beta  =  u + v _____  +  u - v _____ 

=  2\frac{u}{2} 

= u

\alpha  - \beta  =  u + v _____  -  u - v _____ 

=  2\frac{v}{2} 

= v

Thus, replacing \alpha  and \beta  in the product-to-sum formula with the substitute expressions, we have

sin \alpha  cos \beta  =  \frac{1}{2} [sin(\alpha  + \beta ) + sin(\alpha  - \beta )]

sin (  u + v _____  ) cos (  u - v _____  ) =  \frac{1}{2} [sin u + sin v] Substitute for (\alpha  + \beta ) and (\alpha  - \beta )

2 sin (  u + v _____  ) cos (  u - v _____  ) = sin u + sin v The other sum-to-product identities are derived similarly. sum-to-product formulas The sum-to-product formulas are as follows: sin \alpha  + sin \beta  = 2 sin (  \alpha  + \beta  _____  ) cos (  \alpha  - \beta  _____  ) sin \alpha  - sin \beta  = 2 sin (  \alpha  - \beta  _____  ) cos (  \alpha  + \beta  _____  ) cos \alpha  - cos \beta  = -2 sin (  \alpha  + \beta  _____  ) sin (  \alpha  - \beta  _____  ) cos \alpha  + cos \beta  = 2 cos (  \alpha  + \beta  _____  ) cos (  \alpha  - \beta  _____  )

**Example  4**

### Writing the Difference of Sines as a Product

Write the following difference of sines expression as a product: sin(4\theta ) - sin(2\theta ).

**Solution**

We begin by writing the formula for the difference of sines.

sin \alpha  - sin \beta  = 2 sin (  \alpha  - \beta  _____  ) cos (  \alpha  + \beta  _____  ) Substitute the values into the formula, and simplify.

sin(4\theta ) - sin(2\theta ) = 2 sin (  4\theta  - 2\theta  ______  ) cos (  4\theta  + 2\theta  ______  )

= 2 sin (  2\thet\frac{a}{2}  ) cos (  6\thet\frac{a}{2}  )

= 2 sin \theta  cos(3\theta )

**Try It #4**

Use the sum-to-product formula to write the sum as a product: sin(3\theta ) + sin(\theta ).

**Example  5**

### Evaluating Using the Sum-to-Product Formula

Evaluate cos(15°) - cos(75°).

**Solution**

We begin by writing the formula for the difference of cosines.

cos \alpha  - cos \beta  = -2 sin (  \alpha  + \beta  _____  ) sin (  \alpha  - \beta  _____  ) Then we substitute the given angles and simplify.

cos(15°) - cos(75°) = -2 sin (  15° + 75° ________  ) sin (  15° - 75° ________  )

= -2 sin(45°)sin(-30°)

= -2(  \sqrt{2}  ___ 2  )( - \frac{1}{2}  )

=  \sqrt{2}  ___ 2 

**Example  6**

Proving an Identity Prove the identity:

 cos(4t) - cos(2t)

_____________

sin(4t) + sin(2t)  = -tan t

**Solution**

We will start with the left side, the more complicated side of the equation, and rewrite the expression until it matches the right side.

 cos(4t) - cos(2t)

_____________

sin(4t) + sin(2t)  =  -2 sin(  4t + 2t ______  )sin (  4t - 2t ______  )

____

2 sin (  4t + 2t ______  ) cos (  4t - 2t ______  ) 

=  -2 sin(3t)sin t

___________

2 sin(3t)cos t 

=  -2 sin(3t)sin t

___________

2 sin(3t)cos t 

= - sin t ____ cos t 

= -tan t

**Analysis**
Recall that verifying trigonometric identities has its own set of rules. The procedures for solving an equation are not the same as the procedures for verifying an identity. When we prove an identity, we pick one side to work on and make substitutions until that side is transformed into the other side.

**Example  7**

Verifying the Identity Using Double-Angle Formulas and Reciprocal Identities Verify the identity csc^{2} \theta  - 2 =  cos(2\theta ) ______ sin^{2} \theta  .

**Solution**

For verifying this equation, we are bringing together several of the identities. We will use the double-angle formula and the reciprocal identities. We will work with the right side of the equation and rewrite it until it matches the left side.

 cos(2\theta ) ______ sin^{2} \theta   =  1 - 2 sin^{2} \theta  _________ sin^{2} \theta  

=  1 ____ sin^{2} \theta   -  2 sin^{2} \theta  ______ sin^{2} \theta  

= csc^{2} \theta  - 2

**Try It #5**

Verify the identity tan \theta  cot \theta  - cos^{2}\theta  = sin^{2}\theta . Access these online resources for additional instruction and practice with the product-to-sum and sum-to-product identities. • Sum to Product Identities (http://openstaxcollege.org/l/sumtoprod) • Sum to Product and Product to Sum Identities (http://openstaxcollege.org/l/sumtpptsum)

## 7.4 Section Exercises

### 7.4 Section Exercises

Verbal 1. Starting with the product to sum formula sin \alpha  cos \beta  =  \frac{1}{2} [sin(\alpha  + \beta ) + sin(\alpha  - \beta )], explain how to determine the formula for cos \alpha  sin \beta . 2. Explain two different methods of calculating cos(195°)cos(105°), one of which uses the product to sum. Which method is easier? 3. Explain a situation where we would convert an equation from a sum to a product and give an example. 4. Explain a situation where we would convert an equation from a product to a sum, and give an example. Algebraic For the following exercises, rewrite the product as a sum or difference. 6. 20cos(36t)cos(6t) 7. 2sin(5x)cos(3x) 8. 10cos(5x)sin(10x) 9. sin(-x)sin(5x) 10. sin(3x)cos(5x) For the following exercises, rewrite the sum or difference as a product. 11. cos(6t) + cos(4t) 12. sin(3x) + sin(7x) 13. cos(7x) + cos(-7x) 14. sin(3x) - sin(-3x) 15. cos(3x) + cos(9x) 16. sin h - sin(3h) For the following exercises, evaluate the product using a sum or difference of two functions. Evaluate exactly. 17. cos(45°)cos(15°) 18. cos(45°)sin(15°) 19. sin(-345°)sin(-15°) 21. sin(-45°)sin(-15°) For the following exercises, evaluate the product using a sum or difference of two functions. Leave in terms of sine and cosine. 22. cos(23°)sin(17°) 25. sin(213°)cos(8°) For the following exercises, rewrite the sum as a product of two functions. Leave in terms of sine and cosine. 27. sin(76°) + sin(14°) 28. cos(58°) - cos(12°) 29. sin(101°) - sin(32°) 30. cos(100°) + cos(200°) 31. sin(-1°) + sin(-2°) For the following exercises, prove the identity. 32.  cos(a + b) ________ cos(a - b)  =  1 - tan a tan b

___________

1 + tan a tan b  33. 4sin(3x)cos(4x) = 2 sin(7x) - 2 sinx 34.  6cos(8x)sin(2x)

____________

sin(-6x)  = -3 sin(10x)csc(6x) + 3 35. sin x + sin(3x) = 4sin x cos^{2} x 36. 2(cos^{3} x - cos x sin^{2} x)= cos(3x) + cos x 37. 2 tan x cos(3x) = sec x(sin(4x) - sin(2x)) 38. cos(a + b) + cos(a - b) = 2cos a cos b

Numeric For the following exercises, rewrite the sum as a product of two functions or the product as a sum of two functions. Give your answer in terms of sines and cosines. Then evaluate the final answer numerically, rounded to four decimal places. 39. cos(58°) + cos(12°) 40. sin(2°) - sin(3°) 41. cos(44°) - cos(22°) 42. cos(176°)sin(9°) 43. sin(-14°)sin(85°) Technology For the following exercises, algebraically determine whether each of the given expressions is a true identity. If it is not an identity, replace the right-hand side with an expression equivalent to the left side. Verify the results by graphing both expressions on a calculator. 44. 2sin(2x)sin(3x) = cos x - cos(5x) 45.  cos(10\theta ) + cos(6\theta )

_______________

cos(6\theta ) - cos(10\theta )  = cot(2\theta )cot(8\theta ) 46.  sin(3x) - sin(5x)

_____________

cos(3x) + cos(5x)  = tan x 47. 2cos(2x)cos x + sin(2x)sin x = 2 sin x 48.  sin(2x) + sin(4x)

_____________

sin(2x) - sin(4x)  = -tan(3x)cot x For the following exercises, simplify the expression to one term, then graph the original function and your simplified version to verify they are identical. 49.  sin(9t) - sin(3t)

_____________

cos(9t) + cos(3t)  50. 2sin(8x)cos(6x) - sin(2x) 51.  sin(3x) - sin x

____________ sin x  52.  cos(5x) + cos(3x)

______________

sin(5x) + sin(3x)  53. sin x cos(15x) - cos x sin(15x) Extensions For the following exercises, prove the following sum-to-product formulas. 54. sin x - sin y = 2 sin (  x - \frac{y}{2}  )cos (  x + \frac{y}{2}  ) 55. cos x + cos y = 2cos (  x + \frac{y}{2}  ) cos (  x - \frac{y}{2}  ) For the following exercises, prove the identity. 56.  sin(6x) + sin(4x)

_____________

sin(6x) - sin(4x)  = tan (5x)cot x 57.  cos(3x) + cos x

____________

cos(3x) - cos x  = -cot (2x)cot x 58.  cos(6y) + cos(8y)

______________

sin(6y) - sin(4y)  = cot y cos(7y) sec(5y) 59.  cos(2y) - cos(4y)

______________

sin(2y) + sin(4y)  = tan y 60.  sin(10x) - sin(2x)

______________

cos(10x) + cos(2x)  = tan(4x) 61. cos x - cos(3x) = 4 sin^{2} x cos x 62. (cos(2x) - cos(4x))^{2} + (sin(4x) + sin(2x))^{2} = 4 sin^{2}(3x) 63. tan(  \p\frac{i}{4}  - t ) =  1 - tan \frac{t}{1} + tan t 

## 7.5 Solving Trigonometric Equations

Learning Objectives
In this section, you will:
• Solve linear trigonometric equations in sine and cosine.
• Solve equations involving a single trigonometric function.
• Solve trigonometric equations using a calculator.
• Solve trigonometric equations that are quadratic in form.
• Solve trigonometric equations using fundamental identities.
• Solve trigonometric equations with multiple angles.
• Solve right triangle problems.

### Solving Trigonometric Equations

Thales of Miletus (circa 625–547 BC) is known as the founder of geometry. The legend is that he calculated the height of the Great Pyramid of Giza in Egypt using the theory of similar triangles, which he developed by measuring the shadow of his staff. Based on proportions, this theory has applications in a number of areas, including fractal geometry, engineering, and architecture. Often, the angle of elevation and the angle of depression are found using similar triangles. In earlier sections of this chapter, we looked at trigonometric identities. Identities are true for all values in the domain of the variable. In this section, we begin our study of trigonometric equations to study real-world scenarios such as the finding the dimensions of the pyramids. Solving Linear Trigonometric Equations in Sine and Cosine Trigonometric equations are, as the name implies, equations that involve trigonometric functions. Similar in many ways to solving polynomial equations or rational equations, only specific values of the variable will be solutions, if there are solutions at all. Often we will solve a trigonometric equation over a specified interval. However, just as often, we will be asked to find all possible solutions, and as trigonometric functions are periodic, solutions are repeated within each period. In other words, trigonometric equations may have an infinite number of solutions. Additionally, like rational equations, the domain of the function must be considered before we assume that any solution is valid. The period of both the sine function and the cosine function is 2\pi . In other words, every 2\pi  units, the y-values repeat. If we need to find all possible solutions, then we must add 2\pi k, where k is an integer, to the initial solution. Recall the rule that gives the format for stating all possible solutions for a function where the period is 2\pi : sin \theta  = sin(\theta  \pm  2k\pi ) There are similar rules for indicating all possible solutions for the other trigonometric functions. Solving trigonometric equations requires the same techniques as solving algebraic equations. We read the equation from left to right, horizontally, like a sentence. We look for known patterns, factor, find common denominators, and substitute certain expressions with a variable to make solving a more straightforward process. However, with trigonometric equations, we also have the advantage of using the identities we developed in the previous sections.

**Example  1**

### Solving a Linear Trigonometric Equation Involving the Cosine Function

Find all possible exact solutions for the equation cos \theta  =  \frac{1}{2} .

**Solution**

From the unit circle, we know that

cos \theta  =  \frac{1}{2} 

\theta  =  \p\frac{i}{3} ,  5\pi  ___ 3  These are the solutions in the interval [0, 2\pi ]. All possible solutions are given by

\theta  =  \p\frac{i}{3}  \pm  2k\pi  and \theta  =  5\pi  ___ 3  \pm  2k\pi  where k is an integer.

**Example  2**

### Solving a Linear Equation Involving the Sine Function

Find all possible exact solutions for the equation sin t =  \frac{1}{2} .

**Solution**

Solving for all possible values of t means that solutions include angles beyond the period of 2\pi . From Section 7.2 Figure 2, we can see that the solutions are t =  \p\frac{i}{6}  and t =  5\pi  ___ 6 . But the problem is asking for all possible values that solve the equation. Therefore, the answer is t =  \p\frac{i}{6}  \pm  2\pi k and t =  5\pi  ___ 6  \pm  2\pi k where k is an integer.

**How To…**

Given a trigonometric equation, solve using algebra. 1. Look for a pattern that suggests an algebraic property, such as the difference of squares or a factoring opportunity. 2. Substitute the trigonometric expression with a single variable, such as x or u. 3. Solve the equation the same way an algebraic equation would be solved. 4. Substitute the trigonometric expression back in for the variable in the resulting expressions. 5. Solve for the angle.

**Example  3**

Solve the Trigonometric Equation in Linear Form Solve the equation exactly: 2cos \theta  - 3 = - 5, 0 \le  \theta  < 2\pi .

**Solution**

Use algebraic techniques to solve the equation.

2cos \theta  - 3 = -5

2cos \theta  = -2

cos \theta  = -1

\theta  = \pi 

**Try It #1**

Solve exactly the following linear equation on the interval [0, 2\pi ): 2sin x + 1 = 0. Solving Equations Involving a Single Trigonometric Function When we are given equations that involve only one of the six trigonometric functions, their solutions involve using algebraic techniques and the unit circle (see Section 7.2 Figure 2). We need to make several considerations when the equation involves trigonometric functions other than sine and cosine. Problems involving the reciprocals of the primary trigonometric functions need to be viewed from an algebraic perspective. In other words, we will write the reciprocal function, and solve for the angles using the function. Also, an equation involving the tangent function is slightly different from one containing a sine or cosine function. First, as we know, the period of tangent is \pi , not 2\pi . Further, the domain of tangent is all real numbers with the exception of odd integer multiples of  \p\frac{i}{2} , unless, of course, a problem places its own restrictions on the domain.

**Example  4**

### Solving a Problem Involving a Single Trigonometric Function

Solve the problem exactly: 2sin^{2} \theta  - 1 = 0, 0 \le  \theta  < 2\pi .

**Solution**

As this problem is not easily factored, we will solve using the square root property. First, we use algebra to isolate sin \theta . Then we will find the angles.

2sin^{2} \theta  - 1 = 0

2sin^{2} \theta  = 1

sin^{2} \theta  =  \frac{1}{2} 

\sqrt{sin^{2}} \theta   = \pm \sqrt{__}

 \frac{1}{2}  

sin \theta  = \pm  1 _ \sqrt{2}   = \pm  \sqrt{2}  ____ 2 

\theta  =  \p\frac{i}{4} ,  3\pi  ___ 4 ,  5\pi  ___ 4 ,  7\pi  ___ 4 

**Example  5**

### Solving a Trigonometric Equation Involving Cosecant

Solve the following equation exactly: csc \theta  = -2, 0 \le  \theta  < 4\pi .

**Solution**

We want all values of \theta  for which csc \theta  = -2 over the interval 0 \le  \theta  < 4\pi .

csc \theta  = -2

 1 ____ sin \theta   = -2

sin \theta  = - \frac{1}{2} 

\theta  =  7\pi  ___ ___ ___ ___ 6  Analysis As sin \theta  = -  \frac{1}{2} , notice that all four solutions are in the third and fourth quadrants.

**Example  6**

### Solving an Equation Involving Tangent

Solve the equation exactly: tan ( \theta  -  \p\frac{i}{2}  ) = 1, 0 \le  \theta  < 2\pi .

**Solution**

Recall that the tangent function has a period of \pi . On the interval [0, \pi ), and at the angle of  \p\frac{i}{4} , the tangent has a value of 1. However, the angle we want is ( \theta  -  \p\frac{i}{2}  ). Thus, if tan (  \p\frac{i}{4}  ) = 1, then

\theta  -  \p\frac{i}{2}  =  \p\frac{i}{4} 

\theta  =  3\pi  ___ 4  \pm  k\pi  Over the interval [0, 2\pi ), we have two solutions:

\theta  =  3\pi  ___ 4  and \theta  =  3\pi  ___ 4  + \pi  =  7\pi  ___ 4 

**Try It #2**

Find all solutions for tan x = \sqrt{3} .

**Example  7**

Identify all Solutions to the Equation Involving Tangent Identify all exact solutions to the equation 2(tan x + 3) = 5 + tan x, 0 \le  x < 2\pi .

**Solution**

We can solve this equation using only algebra. Isolate the expression tan x on the left side of the equals sign.

2(tan x) + 2(3) = 5 + tan x

2tan x + 6 = 5 + tan x

2tan x - tan x = 5 - 6

tan x = -1 There are two angles on the unit circle that have a tangent value of -1: \theta  =  3\p\frac{i}{4}  and \theta  =  7\p\frac{i}{4} . Solve Trigonometric Equations Using a Calculator Not all functions can be solved exactly using only the unit circle. When we must solve an equation involving an angle other than one of the special angles, we will need to use a calculator. Make sure it is set to the proper mode, either degrees or radians, depending on the criteria of the given problem.

**Example  8**

Using a Calculator to Solve a Trigonometric Equation Involving Sine Use a calculator to solve the equation sin \theta  = 0.8, where \theta  is in radians.

**Solution**

Make sure mode is set to radians. To find \theta , use the inverse sine function. On most calculators, you will need to push the 2ND button and then the SIN button to bring up the sin-1 function. What is shown on the screen is sin-1( . The calculator is ready for the input within the parentheses. For this problem, we enter sin-1 (0.8), and press ENTER. Thus, to four decimals places,

The solution is

The angle measurement in degrees is

Analysis Note that a calculator will only return an angle in quadrants I or IV for the sine function, since that is the range of the inverse sine. The other angle is obtained by using \pi  - \theta .

**Example  9**

Using a Calculator to Solve a Trigonometric Equation Involving Secant Use a calculator to solve the equation sec \theta  = -4, giving your answer in radians.

**Solution**

We can begin with some algebra.

sec \theta  = -4

 1 ____ cos \theta   = -4

cos \theta  = -  \frac{1}{4}  Check that the MODE is in radians. Now use the inverse cosine function.

cos-1( - \frac{1}{S}ince  \p\frac{i}{2}  ≈ 1.57 and \pi  ≈ 3.14, 1.8235 is between these two numbers, thus \theta  ≈ 1.8235 is in quadrant II. Cosine is also negative in quadrant III. Note that a calculator will only return an angle in quadrants I or II for the cosine function, since that is the range of the inverse cosine. See Figure 2.

x y So, we also need to find the measure of the angle in quadrant III. In quadrant III, the reference angle is \theta  ́≈ \pi  - 1.8235 ≈ 1.3181. The other solution in quadrant III is \theta  ́ ≈ \pi  + 1.3181 ≈ 4.4597. The solutions are \theta  ≈ 1.8235 \pm  2\pi k and \theta  ≈ 4.4597 \pm  2\pi k.

**Try It #3**

Solve cos \theta  = -0.2. Solving Trigonometric Equations in Quadratic Form Solving a quadratic equation may be more complicated, but once again, we can use algebra as we would for any quadratic equation. Look at the pattern of the equation. Is there more than one trigonometric function in the equation, or is there only one? Which trigonometric function is squared? If there is only one function represented and one of the terms is squared, think about the standard form of a quadratic. Replace the trigonometric function with a variable such as x or u. If substitution makes the equation look like a quadratic equation, then we can use the same methods for solving quadratics to solve the trigonometric equations.

**Example  10**

### Solving a Trigonometric Equation in Quadratic Form

Solve the equation exactly: cos^{2} \theta  + 3 cos \theta  - 1 = 0, 0 \le  \theta  < 2\pi .

**Solution**

We begin by using substitution and replacing cos \theta  with x. It is not necessary to use substitution, but it may make the problem easier to solve visually. Let cos \theta  = x. We have

x^{2} + 3x - 1 = 0 The equation cannot be factored, so we will use the quadratic formula x =  -b \pm  \sqrt{b^{2}} - 4ac 

_____________ 2a .

x =  -3 \pm  \sqrt{—}

(-3)^{2} - 4(1)(-1) 

______________________

=  -3 \pm  \sqrt{13}  _________  Replace x with cos \theta , and solve. Thus,

cos \theta  =  -3 \pm  \sqrt{13}  _________ 

\theta  = cos-1(  -3 + \sqrt{13}  _________  ) Note that only the + sign is used. This is because we get an error when we solve \theta  = cos-1(  -3 - \sqrt{13}  _________  ) on a calculator, since the domain of the inverse cosine function is [-1, 1]. However, there is a second solution:

\theta  = cos-1(  -3 + \sqrt{13}  _________  )

This terminal side of the angle lies in quadrant I. Since cosine is also positive in quadrant IV, the second solution is

\theta  = 2\pi  - cos-1(  -3 + \sqrt{13}  _________  )

**Try It #4**

Solve sin^{2} \theta  = 2 cos \theta  + 2, 0 \le  \theta  \le  2\pi . [Hint: Make a substitution to express the equation only in terms of cosine.]

**Example  11**

### Solving a Trigonometric Equation in Quadratic Form by Factoring

Solve the equation exactly: 2 sin^{2} \theta  - 5 sin \theta  + 3 = 0, 0 \le  \theta  \le  2\pi .

**Solution**

Using grouping, this quadratic can be factored. Either make the real substitution, sin \theta  = u, or imagine it, as we factor:

2sin^{2} \theta  - 5sin \theta  + 3 = 0

(2sin \theta  - 3)(sin \theta  - 1) = 0 Now set each factor equal to zero.

2sin \theta  - 3 = 0

2sin \theta  = 3

sin \theta  =  \frac{3}{2} 

sin \theta  - 1 = 0

sin \theta  = 1 Next solve for \theta : sin \theta  \neq   \frac{3}{2} , as the range of the sine function is [-1, 1]. However, sin \theta  = 1, giving the solution \theta  =  \p\frac{i}{2} .

**Analysis**
Make sure to check all solutions on the given domain as some factors have no solution.

**Try It #5**

Solve sin^{2} \theta  = 2cos \theta  + 2, 0 \le  \theta  \le  2\pi . [Hint: Make a substitution to express the equation only in terms of cosine.]

**Example  12**

### Solving a Trigonometric Equation Using Algebra

Solve exactly: 2sin^{2} \theta  + sin \theta  = 0; 0 \le  \theta  < 2\pi

**Solution**

This problem should appear familiar as it is similar to a quadratic. Let sin \theta  = x. The equation becomes 2x^{2} + x = 0. We begin by factoring:

2x^{2} + x = 0

x(2x + 1) = 0 Set each factor equal to zero.

x = 0

(2x + 1) = 0

x = - \frac{1}{2}  Then, substitute back into the equation the original expression sin \theta  for x. Thus,

sin \theta  = 0

\theta  = 0, \pi 

sin \theta  = - \frac{1}{2} 

\theta  =  7\pi  ___ ___ 6  The solutions within the domain 0 \le  \theta  < 2\pi  are \theta  = 0, \pi ,  7\pi  ___ ___ 6 . If we prefer not to substitute, we can solve the equation by following the same pattern of factoring and setting each factor equal to zero.

2sin^{2} \theta  + sin \theta  = 0

sin \theta (2sin \theta  + 1) = 0

sin \theta  = 0

\theta  = 0, \pi 

2sin \theta  + 1 = 0

2sin \theta  = -1

sin \theta  = - \frac{1}{2} 

\theta  =  7\pi  ___ ___ 6  Analysis We can see the solutions on the graph in Figure 3. On the interval 0 \le  \theta  < 2\pi , the graph crosses the x-axis four times, at the solutions noted. Notice that trigonometric equations that are in quadratic form can yield up to four solutions instead of the expected two that are found with quadratic equations. In this example, each solution (angle) corresponding to a positive sine value will yield two angles that would result in that value. \pi  2\pi  \theta  y – \pi  \pi  \pi  \pi  13\pi  11\pi  7\pi  4\pi  3\pi  5\pi  5\pi  2\pi  f(\theta ) = 2 sin^{2} \theta  + sin \theta  We can verify the solutions on the unit circle in Section 7.2 Figure 2 as well.

**Example  13**

### Solving a Trigonometric Equation Quadratic in Form

Solve the equation quadratic in form exactly: 2sin^{2} \theta  - 3sin \theta  + 1 = 0, 0 \le  \theta  < 2\pi .

**Solution**

We can factor using grouping.

**Solution**

values of \theta  can be found on the unit circle:

(2sin \theta  - 1)(sin \theta  - 1) = 0

2sin \theta  - 1 = 0

sin \theta  =  \frac{1}{2} 

\theta  =  \p\frac{i}{6} ,  5\pi  ___ 6 

sin \theta  = 1

\theta  =  \p\frac{i}{2} 

**Try It #6**

Solve the quadratic equation 2cos^{2} \theta  + cos \theta  = 0. Solving Trigonometric Equations Using Fundamental Identities While algebra can be used to solve a number of trigonometric equations, we can also use the fundamental identities because they make solving equations simpler. Remember that the techniques we use for solving are not the same as those for verifying identities. The basic rules of algebra apply here, as opposed to rewriting one side of the identity to match the other side. In the next example, we use two identities to simplify the equation.

**Example  14**

Use Identities to Solve an Equation Use identities to solve exactly the trigonometric equation over the interval 0 \le  x < 2\pi .

cos x cos(2x) + sin x sin(2x) =  \sqrt{3}  ____ 2

**Solution**

Notice that the left side of the equation is the difference formula for cosine.

cos x cos(2x) + sin x sin(2x) =  \sqrt{3}  ____ 2 

cos(x - 2x) =  \sqrt{3}  ____ 2  Difference formula for cosine

cos(-x) =  \sqrt{3}  ____ 2  Use the negative angle identity.

cos x =  \sqrt{3}  ____ 2  From the unit circle in Figure 2, we see that cos x =  \sqrt{3}  ____ 2  when x =  \pi  __ ___ 6 .

**Example  15**

### Solving the Equation Using a Double-Angle Formula

Solve the equation exactly using a double-angle formula: cos(2\theta ) = cos \theta .

**Solution**

We have three choices of expressions to substitute for the double-angle of cosine. As it is simpler to solve for one trigonometric function at a time, we will choose the double-angle identity involving only cosine:

cos(2\theta ) = cos \theta 

2cos^{2} \theta  - 1 = cos \theta 

2cos^{2} \theta  - cos \theta  - 1 = 0

(2cos \theta  + 1)(cos \theta  - 1) = 0

2cos \theta  + 1 = 0

cos \theta  = - \frac{1}{2} 

cos \theta  - 1 = 0

cos \theta  = 1 So, if cos \theta  = - \frac{1}{2} , then \theta  =  2\p\frac{i}{3}  \pm  2\pi k and \theta  =  4\p\frac{i}{3}  \pm  2\pi k; if cos \theta  = 1, then \theta  = 0 \pm  2\pi k.

**Example  16** — Solving an Equation Using an Identity
Solve the equation exactly using an identity: 3cos \theta  + 3 = 2sin^{2} \theta , 0 \le  \theta  < 2\pi .

**Solution**

If we rewrite the right side, we can write the equation in terms of cosine:

3cos \theta  + 3 = 2sin^{2} \theta 

3cos \theta  + 3 = 2(1 - cos^{2} \theta )

3cos \theta  + 3 = 2 - 2cos^{2} \theta 

2cos^{2} \theta  + 3cos \theta  + 1 = 0

(2cos \theta  + 1)(cos \theta  + 1) = 0

2cos \theta  + 1 = 0

cos \theta  = - \frac{1}{2} 

\theta  =  2\pi  ___ 3 ,  4\pi  ___ 3 

cos \theta  + 1 = 0

cos \theta  = -1

\theta  = \pi  Our solutions are \theta  =  2\pi  ___ 3 ,  4\pi  ___ 3 , \pi 

### Solving Trigonometric Equations with Multiple Angles

Sometimes it is not possible to solve a trigonometric equation with identities that have a multiple angle, such as sin(2x) or cos(3x). When confronted with these equations, recall that y = sin(2x) is a horizontal compression by a factor of 2 of the function y = sin x. On an interval of 2\pi , we can graph two periods of y = sin(2x), as opposed to one cycle of y = sin x. This compression of the graph leads us to believe there may be twice as many x-intercepts or solutions to sin(2x) = 0 compared to sin x = 0. This information will help us solve the equation.

**Example  17**

### Solving a Multiple Angle Trigonometric Equation

Solve exactly: cos(2x) =  \frac{1}{2}  on [0, 2\pi ).

**Solution**

We can see that this equation is the standard equation with a multiple of an angle. If cos(\alpha ) =  \frac{1}{2} , we know \alpha  is in quadrants I and IV. While \theta  = cos-1 \frac{1}{2}  will only yield solutions in quadrants I and II, we recognize that the solutions to the equation cos \theta  =  \frac{1}{2}  will be in quadrants I and IV. Therefore, the possible angles are \theta  =  \p\frac{i}{3}  and \theta  =  5\p\frac{i}{3} . So, 2x =  \p\frac{i}{3}  or 2x =  5\p\frac{i}{3} , which means that x =  \p\frac{i}{6}  or x =  5\p\frac{i}{6} . Does this make sense? Yes, because cos ( 2 (  \p\frac{i}{6}  ) ) = cos (  \p\frac{i}{3}  ) =  \frac{1}{2} . Are there any other possible answers? Let us return to our first step. In quadrant I, 2x =  \p\frac{i}{3} , so x =  \p\frac{i}{6}  as noted. Let us revolve around the circle again:

2x =  \p\frac{i}{3}  + 2\pi 

=  \p\frac{i}{3}  +  6\pi  ___ 3 

=  7\pi  ___ 3  so x =  7\pi  ___ 6 . One more rotation yields

2x =  \p\frac{i}{3}  + 4\pi 

=  \p\frac{i}{3}  +  12\pi  ___ 3 

=  13\pi  ___ 3  x =  13\pi  ___ 6  > 2\pi , so this value for x is larger than 2\pi , so it is not a solution on [0, 2\pi ). In quadrant IV, 2x =  5\p\frac{i}{3} , so x =  5\p\frac{i}{6}  as noted. Let us revolve around the circle again:

2x =  5\pi  ___ 3  + 2\pi 

=  5\pi  ___ 3  +  6\pi  ___ 3 

=  11\pi  ___ 3  so x =  11\pi  ___ 6 .

One more rotation yields

2x =  5\pi  ___ 3  + 4\pi 

=  5\pi  ___ 3  +  12\pi  ___ 3 

=  17\pi  ___ 3  x =  17\pi  ___ 6  > 2\pi , so this value for x is larger than 2\pi , so it is not a solution on [0, 2\pi ). Our solutions are x =  \p\frac{i}{6} ,  5\p\frac{i}{6} ,  7\p\frac{i}{6} , and  11\pi  ___ 6 . Note that whenever we solve a problem in the form of sin(nx) = c, we must go around the unit circle n times. Solving Right Triangle Problems We can now use all of the methods we have learned to solve problems that involve applying the properties of right triangles and the Pythagorean Theorem. We begin with the familiar Pythagorean Theorem, a^{2} + b^{2} = c^{2}, and model an equation to fit a situation.

**Example  18**

Using the Pythagorean Theorem to Model an Equation Use the Pythagorean Theorem, and the properties of right triangles to model an equation that fits the problem. One of the cables that anchors the center of the London Eye Ferris wheel to the ground must be replaced. The center of the Ferris wheel is 69.5 meters above the ground, and the second anchor on the ground is 23 meters from the base of the Ferris wheel. Approximately how long is the cable, and what is the angle of elevation (from ground up to the center of the Ferris wheel)? See Figure 4. 69.5 \theta

**Solution**

Using the information given, we can draw a right triangle. We can find the length of the cable with the Pythagorean Theorem.

a^{2} + b^{2} = c^{2}

\sqrt{The} angle of elevation is \theta , formed by the second anchor on the ground and the cable reaching to the center of the wheel. We can use the tangent function to find its measure. Round to two decimal places.

tan \theta  =  69.5 ____ 23 

____

The angle of elevation is approximately 71.7°, and the length of the cable is 73.2 meters.

**Example  19**

Using the Pythagorean Theorem to Model an Abstract Problem OSHA safety regulations require that the base of a ladder be placed 1 foot from the wall for every 4 feet of ladder length. Find the angle that a ladder of any length forms with the ground and the height at which the ladder touches the wall.

**Solution**

For any length of ladder, the base needs to be a distance from the wall equal to one fourth of the ladder’s length. Equivalently, if the base of the ladder is “a” feet from the wall, the length of the ladder will be 4a feet. See 4a \theta  a b The side adjacent to \theta  is a and the hypotenuse is 4a. Thus,

cos \theta  =  \frac{a}{4}a  =  \frac{1}{4} 

cos-1(  \frac{1}{T}he elevation of the ladder forms an angle of 75.5° with the ground. The height at which the ladder touches the wall can be found using the Pythagorean Theorem:

a^{2} + b^{2} = (4a)^{2}

b^{2} = (4a)^{2} - a^{2}

b = a\sqrt{15}  Thus, the ladder touches the wall at a\sqrt{15}  feet from the ground. Access these online resources for additional instruction and practice with solving trigonometric equations. • Solving Trigonometric Equations I (http://openstaxcollege.org/l/solvetrigeqI) • Solving Trigonometric Equations II (http://openstaxcollege.org/l/solvetrigeqII) • Solving Trigonometric Equations III (http://openstaxcollege.org/l/solvetrigeqIII) • Solving Trigonometric Equations IV (http://openstaxcollege.org/l/solvetrigeqIV) • Solving Trigonometric Equations V (http://openstaxcollege.org/l/solvetrigeqV) • Solving Trigonometric Equations VI (http://openstaxcollege.org/l/solvetrigeqVI)

7.5 SECTION EXERCISES Verbal 1. Will there always be solutions to trigonometric function equations? If not, describe an equation that would not have a solution. Explain why or why not. 2. When solving a trigonometric equation involving more than one trig function, do we always want to try to rewrite the equation so it is expressed in terms of one trigonometric function? Why or why not? 3. When solving linear trig equations in terms of only sine or cosine, how do we know whether there will be solutions? Algebraic For the following exercises, find all solutions exactly on the interval 0 \le  \theta  < 2\pi . 4. 2sin \theta  = -\sqrt{2}  5. 2sin \theta  = \sqrt{3}  6. 2cos \theta  = 1 7. 2cos \theta  = -\sqrt{2}  8. tan \theta  = -1 9. tan x = 1 10. cot x + 1 = 0 12. csc^{2} x - 4 = 0 For the following exercises, solve exactly on [0, 2\pi ). 13. 2cos \theta  = \sqrt{2}  14. 2cos \theta  = -1 15. 2sin \theta  = -1 16. 2sin \theta  = -\sqrt{3}  18. 2sin(2\theta ) = \sqrt{3}  19. 2cos(3\theta ) = -\sqrt{2}  20. cos(2\theta ) = - \sqrt{3}  ____ 2  21. 2sin(\pi \theta ) = 1 22. 2cos(  \p\frac{i}{5} \theta  ) = \sqrt{3}  For the following exercises, find all exact solutions on [0, 2\pi ). 23. sec(x)sin(x) - 2sin(x) = 0 24. tan(x) - 2sin(x)tan(x) = 0 25. 2cos^{2} t + cos(t) = 1 26. 2tan^{2}(t) = 3sec(t) 27. 2sin(x)cos(x) - sin(x) + 2cos(x) - 1 = 0 28. cos^{2} \theta  =  \frac{1}{2}  29. sec^{2} x = 1 30. tan^{2} (x) = -1 + 2tan(-x) 31. 8sin^{2}(x) + 6sin(x) + 1 = 0 32. tan^{5}(x) = tan(x) For the following exercises, solve with the methods shown in this section exactly on the interval [0, 2\pi ). 33. sin(3x)cos(6x) - cos(3x)sin(6x) = -0.9 34. sin(6x)cos(11x) - cos(6x)sin(11x) = -0.1 35. cos(2x)cos x + sin(2x)sin x = 1 36. 6sin(2t) + 9sin t = 0 37. 9cos(2\theta ) = 9cos^{2} \theta  - 4 38. sin(2t) = cos t 39. cos(2t) = sin t 40. cos(6x) - cos(3x) = 0 For the following exercises, solve exactly on the interval [0, 2\pi ). Use the quadratic formula if the equations do not factor. 41. tan^{2} x - \sqrt{3} tan x = 0 42. sin^{2} x + sin x - 2 = 0 43. sin^{2} x - 2sin x - 4 = 0 44. 5cos^{2} x + 3cos x - 1 = 0 45. 3cos^{2} x - 2cos x - 2 = 0 46. 5sin^{2} x + 2sin x - 1 = 0 47. tan^{2} x + 5tan x - 1 = 0 48. cot^{2} x = -cot x 49. -tan^{2} x - tan x - 2 = 0

## 7.5 Section Exercises

For the following exercises, find exact solutions on the interval [0, 2\pi ). Look for opportunities to use trigonometric identities. 50. sin^{2} x - cos^{2} x - sin x = 0 51. sin^{2} x + cos^{2} x = 0 52. sin(2x) - sin x = 0 53. cos(2x) - cos x = 0 54.  2 tan x ________ 2 - sec^{2} x  - sin^{2} x = cos^{2} x 55. 1 - cos(2x) = 1 + cos(2x) 56. sec^{2} x = 7 57. 10sin x cos x = 6cos x 58. -3sin t = 15cos t sin t 59. 4cos^{2} x - 4 = 15cos x 60. 8sin^{2} x + 6sin x + 1 = 0 61. 8cos^{2} \theta  = 3 - 2cos \theta  62. 6cos^{2} x + 7sin x - 8 = 0 63. 12sin^{2} t + cos t - 6 = 0 64. tan x = 3sin x 65. cos^{3} t = cos t Graphical For the following exercises, algebraically determine all solutions of the trigonometric equation exactly, then verify the results by graphing the equation and finding the zeros. 66. 6sin^{2} x - 5sin x + 1 = 0 67. 8cos^{2} x - 2cos x - 1 = 0 69. 2cos^{2} x - cos x + 15 = 0 70. 20sin^{2} x - 27sin x + 7 = 0 71. 2tan^{2} x + 7tan x + 6 = 0 Technology For the following exercises, use a calculator to find all solutions to four decimal places. For the following exercises, solve the equations algebraically, and then use a calculator to find the values on the interval [0, 2\pi ). Round to four decimal places. 77. tan^{2} x + 3tan x - 3 = 0 78. 6tan^{2} x + 13tan x = -6 79. tan^{2} x - sec x = 1 80. sin^{2} x - 2cos^{2} x = 0 81. 2tan^{2} x + 9tan x - 6 = 0 82. 4sin^{2} x + sin(2x)sec x - 3 = 0 Extensions For the following exercises, find all solutions exactly to the equations on the interval [0, 2\pi ). 83. csc^{2} x - 3csc x - 4 = 0 84. sin^{2} x - cos^{2} x - 1 = 0 85. sin^{2} x( 1 - sin^{2} x) + cos^{2} x( 1 - sin^{2} x) = 0 86. 3sec^{2} x + 2 + sin^{2} x - tan^{2} x + cos^{2} x = 0 87. sin^{2} x - 1 + 2 cos(2x) - cos^{2} x = 1 88. tan^{2} x - 1 - sec^{3} x cos x = 0 89.  sin(2x) ______ sec^{2} x  = 0 90.  sin(2x) ______ 2 csc^{2} x  = 0 91. 2cos^{2} x - sin^{2} x - cos x - 5 = 0 ____ sec^{2} x  + 2 + sin^{2} x + 4cos^{2} x = 4

Real-World Applications 93. An airplane has only enough gas to fly to a city 200 miles northeast of its current location. If the pilot knows that the city is 25 miles north, how many degrees north of east should the airplane fly? 94. If a loading ramp is placed next to a truck, at a height of 4 feet, and the ramp is 15 feet long, what angle does the ramp make with the ground? 95. If a loading ramp is placed next to a truck, at a height of 2 feet, and the ramp is 20 feet long, what angle does the ramp make with the ground? 96. A woman is watching a launched rocket currently 11 miles in altitude. If she is standing 4 miles from the launch pad, at what angle is she looking up from horizontal? 97. An astronaut is in a launched rocket currently 15 miles in altitude. If a man is standing 2 miles from the launch pad, at what angle is she looking down at him from horizontal? (Hint: this is called the angle of depression.) 98. A woman is standing 8 meters away from a 10-meter tall building. At what angle is she looking to the top of the building? 99. A man is standing 10 meters away from a 6-meter tall building. Someone at the top of the building is looking down at him. At what angle is the person looking at him? 100. A 20-foot tall building has a shadow that is 55 feet long. What is the angle of elevation of the sun? 101. A 90-foot tall building has a shadow that is 2 feet long. What is the angle of elevation of the sun? 102. A spotlight on the ground 3 meters from a 2-meter tall man casts a 6 meter shadow on a wall 6 meters from the man. At what angle is the light? 103. A spotlight on the ground 3 feet from a 5-foot tall woman casts a 15-foot tall shadow on a wall 6 feet from the woman. At what angle is the light? For the following exercises, find a solution to the word problem algebraically. Then use a calculator to verify the result. Round the answer to the nearest tenth of a degree. 104. A person does a handstand with his feet touching a wall and his hands 1.5 feet away from the wall. If the person is 6 feet tall, what angle do his feet make with the wall? 105. A person does a handstand with her feet touching a wall and her hands 3 feet away from the wall. If the person is 5 feet tall, what angle do her feet make with the wall? 106. A 23-foot ladder is positioned next to a house. If the ladder slips at 7 feet from the house when there is not enough traction, what angle should the ladder make with the ground to avoid slipping?

## 7.6 Modeling with Trigonometric Equations

Learning Objectives
In this section, you will:
• Determine the amplitude and period of sinusoidal functions.
• Model equations and graph sinusoidal functions.
• Model periodic behavior.
• Model harmonic motion functions.

### Modeling with Trigonometric Equations

Suppose we charted the average daily temperatures in New York City over the course of one year. We would expect to find the lowest temperatures in January and February and highest in July and August. This familiar cycle repeats year after year, and if we were to extend the graph over multiple years, it would resemble a periodic function. Many other natural phenomena are also periodic. For example, the phases of the moon have a period of approximately 28 days, and birds know to fly south at about the same time each year. So how can we model an equation to reflect periodic behavior? First, we must collect and record data. We then find a function that resembles an observed pattern. Finally, we make the necessary alterations to the function to get a model that is dependable. In this section, we will take a deeper look at specific types of periodic behavior and model equations to fit data. Determining the Amplitude and Period of a Sinusoidal Function Any motion that repeats itself in a fixed time period is considered periodic motion and can be modeled by a sinusoidal function. The amplitude of a sinusoidal function is the distance from the midline to the maximum value, or from the midline to the minimum value. The midline is the average value. Sinusoidal functions oscillate above and below the midline, are periodic, and repeat values in set cycles. Recall from Graphs of the Sine and Cosine Functions that the period of the sine function and the cosine function is 2\pi . In other words, for any value of x, sin(x \pm  2\pi k) = sin x and cos(x \pm  2\pi k) = cos x where k is an integer standard form of sinusoidal equations The general forms of a sinusoidal equation are given as y = Asin(Bt - C) + D or y = Acos(Bt - C) + D where amplitude = ∣ A ∣, B is related to period such that the period =  2\p\frac{i}{B} , C is the phase shift such that  \frac{C}{B}  denotes the horizontal shift, and D represents the vertical shift from the graph’s parent graph. Note that the models are sometimes written as y = a sin(ω t \pm  C) + D or y = a cos(ω t \pm  C) + D, and period is given as  2\pi  _ ω . The difference between the sine and the cosine graphs is that the sine graph begins with the average value of the function and the cosine graph begins with the maximum or minimum value of the function.

**Example  1**

Showing How the Properties of a Trigonometric Function Can Transform a Graph Show the transformation of the graph of y = sin x into the graph of y = 2sin( 4x -  \p\frac{i}{2}  ) + 2.

**Solution**

Consider the series of graphs in Figure 2 and the way each change to the equation changes the image. y = sin x x y \pi  \pi  2\pi  2\pi  \pi  \pi  3\pi  5\pi  5\pi  3\pi  y = 2sin x x y \pi  \pi  2\pi  2\pi  \pi  \pi  3\pi  5\pi  5\pi  3\pi  y = 2sin (4x) x y \pi  \pi  2\pi  2\pi  \pi  \pi  3\pi  5\pi  5\pi  3\pi  x y \pi  \pi  2\pi  2\pi  \pi  \pi  3\pi  5\pi  5\pi  3\pi  y = 2sin \pi  4x x y \pi  \pi  2\pi  2\pi  \pi  \pi  3\pi  5\pi  5\pi  3\pi  +2 y = 2sin \pi  4x (a) (b) (c) (e) (d) with the value of B, such that period =  2\pi  ___ B . Here we have B = 4, which translates to a period of  \p\frac{i}{2} . The graph completes one full cycle in  \p\frac{i}{2}  units. (d) The graph displays a horizontal shift equal to  \frac{C}{B} , or   \pi  __ \frac{2}{4}  =  \p\frac{i}{8} . (e) Finally, the graph is shifted vertically by the value of D. In this case, the graph is shifted up by 2 units.

**Example  2**

Finding the Amplitude and Period of a Function Find the amplitude and period of the following functions and graph one cycle. a. y = 2sin (  \frac{1}{4} x ) b. y = -3sin ( 2x +  \p\frac{i}{2}  ) c. y = cos x + 3

**Solution**

We will solve these problems according to the models. a. y = 2sin(  \frac{1}{4} x ) involves sine, so we use the form

y = Asin(Bt - C) + D We know that ∣ A ∣ is the amplitude, so the amplitude is 2. Period is  2\p\frac{i}{B}  , so the period is

 2\p\frac{i}{B}  =  2\pi  _  \frac{1}{4}  

= 8\pi  See the graph in Figure 3. 2\pi  4\pi  6\pi  8\pi  x y Amplitude = 2 Period = 8\pi  y = 2 sin 1 x

b. y = -3sin( 2x +  \p\frac{i}{2}  ) involves sine, so we use the form

y = Asin(Bt - C) + D Amplitude is ∣ A ∣, so the amplitude is ∣ -3 ∣ = 3. Since A is negative, the graph is reflected over the x-axis. Period is  2\p\frac{i}{B} , so the period is

 2\p\frac{i}{B}  =  2\p\frac{i}{2}  = \pi  The graph is shifted to the left by  \frac{C}{B}  =   \pi  _ \frac{2}{2}  =  \p\frac{i}{4}  units. See Figure 4. \pi  \pi  3\pi  – \pi  x y y = –3 sin + \pi  2x c. y = cos x + 3 involves cosine, so we use the form

y = Acos(Bt - C) + D Amplitude is ∣ A ∣, so the amplitude is 1. The period is 2\pi . See Figure 5. This is the standard cosine function shifted up three units. \pi  2\pi  \pi  3\pi  x y Midline: y = 3 y = cos x + 3

**Try It #1**

What are the amplitude and period of the function y = 3cos(3\pi x)? Finding Equations and Graphing Sinusoidal Functions One method of graphing sinusoidal functions is to find five key points. These points will correspond to intervals of equal length representing  \frac{1}{4}  of the period. The key points will indicate the location of maximum and minimum values. If there is no vertical shift, they will also indicate x-intercepts. For example, suppose we want to graph the function y = cos \theta . We know that the period is 2\pi , so we find the interval between key points as follows.  2\p\frac{i}{4}  =  \p\frac{i}{2}  Starting with \theta  = 0, we calculate the first y-value, add the length of the interval  \p\frac{i}{2}  to 0, and calculate the second y-value. We then add  \p\frac{i}{2}  repeatedly until the five key points are determined. The last value should equal the first value, as the calculations cover one full period. Making a table similar to Table 1, we can see these key points clearly on the graph shown in Figure 6.

\theta   \p\frac{i}{2}  \pi   3\p\frac{i}{2}  2\pi  y = cos \theta  -1 \pi  2\pi  \pi  3\pi  \theta  y y = cos \theta 

**Example  3**

### Graphing Sinusoidal Functions Using Key Points

Graph the function y = -4cos(\pi x) using amplitude, period, and key points.

**Solution**

The amplitude is ∣ -4 ∣ = 4. The period is  2\pi  _ ω  =  2\pi  _ \pi   = 2. (Recall that we sometimes refer to B as ω.) One cycle of the graph can be drawn over the interval [0, 2]. To find the key points, we divide the period by 4. Make a table similar to Table 2, starting with x = 0 and then adding  \frac{1}{2}  successively to x and calculate y. See the graph in Figure 7. x  \frac{1}{2}   \frac{3}{2}  y = -4 cos(\pi x) -4 -4 x y y = –4 cos (\pi x)

**Try It #2**

Graph the function y = 3sin(3x) using the amplitude, period, and five key points. Modeling Periodic Behavior We will now apply these ideas to problems involving periodic behavior.

**Example  4**

### Modeling an Equation and Sketching a Sinusoidal Graph to Fit Criteria

The average monthly temperatures for a small town in Oregon are given in Table 3. Find a sinusoidal function of the form y = Asin(Bt - C) + D that fits the data (round to the nearest tenth) and sketch the graph.

Month Temperature, ° F January 42.5 February 44.5 March 48.5 April 52.5 May June July 68.5 August September 64.5 October 55.5 November 46.5 December 43.5

**Solution**

Recall that amplitude is found using the formula

A =  largest value - smallest value

______________________

 Thus, the amplitude is

∣ A ∣ =  69 - 42.5 ________ 

The data covers a period of 12 months, so  2\p\frac{i}{B}  = 12 which gives B =  2\p\frac{i}{12}  =  \p\frac{i}{6} . The vertical shift is found using the following equation.

D =  highest value + lowest value

_____________________

 Thus, the vertical shift is

________ 

So far, we have the equation y = 13.3sin (  \p\frac{i}{6} x - C ) + 55.8. To find the horizontal shift, we input the x and y values for the first month and solve for C.

_ 6 (1) - C ) + 55.\frac{8}{6}  - C )

-1 = sin(  \p\frac{i}{6}  - C ) sin \theta  = -1 → \theta  = - \p\frac{i}{2} 

 \p\frac{i}{6}  - C = - \p\frac{i}{2} 

 \p\frac{i}{6}  +  \p\frac{i}{2}  = C

=  2\p\frac{i}{3} 

We have the equation y = 13.3sin (  \p\frac{i}{6} x -  2\p\frac{i}{3}  ) + 55.8. See the graph in Figure 8. Temperatures Months Average Amplitude = 13.3

**Example  5**

### Describing Periodic Motion

The hour hand of the large clock on the wall in Union Station measures 24 inches in length. At noon, the tip of the hour hand is 30 inches from the ceiling. At 3 PM, the tip is 54 inches from the ceiling, and at 6 PM, 78 inches. At 9 PM, it is again 54 inches from the ceiling, and at midnight, the tip of the hour hand returns to its original position 30 inches from the ceiling. Let y equal the distance from the tip of the hour hand to the ceiling x hours after noon. Find the equation that models the motion of the clock and sketch the graph.

**Solution**

Begin by making a table of values as shown in Table 4. x y Points to plot Noon 30 in 3 PM 54 in 6 PM 78 in 9 PM 54 in Midnight 30 in To model an equation, we first need to find the amplitude.

∣ A ∣ =   78 - 30 ______  

= 24 The clock’s cycle repeats every 12 hours. Thus,

B =  2\p\frac{i}{12} 

=  \p\frac{i}{6}  The vertical shift is

D =  78 + 30 ______ 

= 54 There is no horizontal shift, so C = 0. Since the function begins with the minimum value of y when x = 0 (as opposed to the maximum value), we will use the cosine function with the negative value for A. In the form y = A cos(Bx \pm  C) + D, the equation is

y = -24cos (  \p\frac{i}{6} x ) + 54 See Figure 9. x y

**Example  6**

Determining a Model for Tides The height of the tide in a small beach town is measured along a seawall. Water levels oscillate between 7 feet at low tide and 15 feet at high tide. On a particular day, low tide occurred at 6 AM and high tide occurred at noon. Approximately every 12 hours, the cycle repeats. Find an equation to model the water levels.

**Solution**

As the water level varies from 7 ft to 15 ft, we can calculate the amplitude as

∣ A ∣ =   (15 - 7) _______  

= 4 The cycle repeats every 12 hours; therefore, B is

 2\p\frac{i}{12}  =  \p\frac{i}{6}  There is a vertical translation of  (15 + 7) _______  = 11. Since the value of the function is at a maximum at t = 0, we will use the cosine function, with the positive value for A. y = 4cos (  \p\frac{i}{6}  )t + 11 See Figure 10. Water Level (feet) Time Midline: y = 11

**Try It #3**

The daily temperature in the month of March in a certain city varies from a low of 24°F to a high of 40°F. Find a sinusoidal function to model daily temperature and sketch the graph. Approximate the time when the temperature reaches the freezing point 32°F. Let t = 0 correspond to noon.

**Example  7**

### Interpreting the Periodic Behavior Equation

The average person’s blood pressure is modeled by the function f(t) = 20 sin(160\pi t) + 100, where f(t) represents the blood pressure at time t, measured in minutes. Interpret the function in terms of period and frequency. Sketch the graph and find the blood pressure reading.

**Solution**

The period is given by

 2\pi  ___ ω  =  2\pi  ____

=  \frac{1}{80}  In a blood pressure function, frequency represents the number of heart beats per minute. Frequency is the reciprocal of period and is given by

 ω __ 2\pi   =  160\pi  ____ 2\pi  

= 80 See the graph in Figure 11. t f(t) f(t) = 20sin(160\pi t) + 100 ____ 80 (  maximum _________ minimum  ).

Analysis Blood pressure of  \frac{120}{80}  is considered to be normal. The top number is the maximum or systolic reading, which measures the pressure in the arteries when the heart contracts. The bottom number is the minimum or diastolic reading, which measures the pressure in the arteries as the heart relaxes between beats, refilling with blood. Thus, normal blood pressure can be modeled by a periodic function with a maximum of 120 and a minimum of 80. Modeling Harmonic Motion Functions Harmonic motion is a form of periodic motion, but there are factors to consider that differentiate the two types. While general periodic motion applications cycle through their periods with no outside interference, harmonic motion requires a restoring force. Examples of harmonic motion include springs, gravitational force, and magnetic force. Simple Harmonic Motion A type of motion described as simple harmonic motion involves a restoring force but assumes that the motion will continue forever. Imagine a weighted object hanging on a spring, When that object is not disturbed, we say that the object is at rest, or in equilibrium. If the object is pulled down and then released, the force of the spring pulls the object back toward equilibrium and harmonic motion begins. The restoring force is directly proportional to the displacement of the object from its equilibrium point. When t = 0, d = 0. simple harmonic motion We see that simple harmonic motion equations are given in terms of displacement: d = acos(ωt) or d = asin(ωt) where |a| is the amplitude,  2\pi  _ ω  is the period, and  ω _ 2\pi   is the frequency, or the number of cycles per unit of time.

**Example  8**

Finding the Displacement, Period, and Frequency, and Graphing a Function For the given functions, 1. Find the maximum displacement of an object. 2. Find the period or the time required for one vibration. 3. Find the frequency. 4. Sketch the graph. a. y = 5sin(3t) b. y = 6cos(\pi t) c. y = 5cos (  \p\frac{i}{2} t )

**Solution**

a. y = 5sin(3t) 1. The maximum displacement is equal to the amplitude, ∣ a ∣, which is 5. 2. The period is  2\pi  _ ω  =  2\p\frac{i}{3} . 3. The frequency is given as  ω _ 2\pi   =  \frac{3}{2}\pi  . 4. See Figure 12. The graph indicates the five key points. \pi  \pi  \pi  2\pi  t y y = 5sin(3t) b. y = 6cos(\pi t) 1. The maximum displacement is 6. 2. The period is  2\pi  _ ω  =  2\pi  _ \pi   = 2. 3. The frequency is  ω _ 2\pi   =  \p\frac{i}{2}\pi   =  \frac{1}{2} . 4. See Figure 13. t y y = 6cos(\pi t)

c. y = 5cos (  \p\frac{i}{2}  )t 1. The maximum displacement is 5. 2. The period is  2\pi  _ ω  =  2\pi  _  \p\frac{i}{2}   = 4. 3. The frequency is  \frac{1}{4} . 4. See Figure 14. t y y = 5cos 2 \pi  t Damped Harmonic Motion In reality, a pendulum does not swing back and forth forever, nor does an object on a spring bounce up and down forever. Eventually, the pendulum stops swinging and the object stops bouncing and both return to equilibrium. Periodic motion in which an energy-dissipating force, or damping factor, acts is known as damped harmonic motion. Friction is typically the damping factor. In physics, various formulas are used to account for the damping factor on the moving object. Some of these are calculus-based formulas that involve derivatives. For our purposes, we will use formulas for basic damped harmonic motion models. damped harmonic motion In damped harmonic motion, the displacement of an oscillating object from its rest position at time t is given as f(t) = ae-ctsin(ωt) or f(t) = ae-ctcos(ωt) where c is a damping factor, ∣ a ∣ is the initial displacement and  2\pi  _ ω  is the period.

**Example  9**

### Modeling Damped Harmonic Motion

Model the equations that fit the two scenarios and use a graphing utility to graph the functions: Two mass-spring systems exhibit damped harmonic motion at a frequency of 0.5 cycles per second. Both have an initial displacement of 10 cm. The first has a damping factor of 0.5 and the second has a damping factor of 0.1.

**Solution**

At time t = 0, the displacement is the maximum of 10 cm, which calls for the cosine function. The cosine function will apply to both models. We are given the frequency f =  ω _ 2\pi   of 0.5 cycles per second. Thus,

 ω _

= \pi  The first spring system has a damping factor of c = 0.5. Following the general model for damped harmonic motion, we have

f(t) = 10e-0.5t cos(\pi t) t f(t) f(t) = 10e–0.5tcos(\pi t)

The second spring system has a damping factor of c = 0.1 and can be modeled as

f (t) = 10e-0.1tcos(\pi t) t f(t) f(t) = 10e–0.1tcos (\pi t) Analysis Notice the differing effects of the damping constant. The local maximum and minimum values of the function with the damping factor c = 0.5 decreases much more rapidly than that of the function with c = 0.1.

**Example  10**

Finding a Cosine Function that Models Damped Harmonic Motion Find and graph a function of the form y = ae-ctcos(ωt) that models the information given. b. a = 2, c = 1.5, f = 3

**Solution**

Substitute the given values into the model. Recall that period is  2\pi  _ ω  and frequency is  ω _ 2\pi  . a. y = 20e-0.05tcos (  \p\frac{i}{2} t ). See Figure 17. t y \pi  t b. y = 2e-1.5tcos(6\pi t). See Figure 18. t y y = 2e–1.5t cos(6\pi t)

**Try It #4**

The following equation represents a damped harmonic motion model: f(t) = 5e-6tcos(4t) Find the initial displacement, the damping constant, and the frequency.

**Example  11**

Finding a Sine Function that Models Damped Harmonic Motion Find and graph a function of the form y = ae-ct sin(ωt) that models the information given. a. a = 7, c = 10, p =  \p\frac{i}{6}  b. a = 0.3, c = 0.2, f = 20

**Solution**

Calculate the value of ω and substitute the known values into the model. a. As period is  2\pi  _ ω , we have

 \p\frac{i}{6}  =  2\pi  _ ω 

ω\pi  = 6(2\pi )

ω = 12 The damping factor is given as 10 and the amplitude is 7. Thus, the model is y = 7e-10tsin(12t). See Figure 19. t y y = 7e–10t sin(12t) b. As frequency is  ω _ 2\pi  , we have

20 =  ω _ 2\pi  

40\pi  = ω The damping factor is given as 0.2 and the amplitude is 0.3. The model is y = 0.3e-0.2tsin(40\pi t). See Figure 20. t y Analysis A comparison of the last two examples illustrates how we choose between the sine or cosine functions to model sinusoidal criteria. We see that the cosine function is at the maximum displacement when t = 0, and the sine function is at the equilibrium point when t = 0. For example, consider the equation y = 20e-0.05tcos (  \p\frac{i}{2} t ) from Example 10. We can see from the graph that when t = 0, y = 20, which is the initial amplitude. Check this by setting t = 0 in the cosine equation:

y = 20e-0.05(0)cos (  \p\frac{i}{2}  )(0)

= 20 Using the sine function yields

y = 20e-0.05(0)sin (  \p\frac{i}{2}  )(0)

= 0 Thus, cosine is the correct function.

**Try It #5**

Write the equation for damped harmonic motion given a = 10, c = 0.5, and p = 2.

**Example  12**

### Modeling the Oscillation of a Spring

A spring measuring 10 inches in natural length is compressed by 5 inches and released. It oscillates once every 3 seconds, and its amplitude decreases by 30% every second. Find an equation that models the position of the spring t seconds after being released.

**Solution**

The amplitude begins at 5 in. and deceases 30% each second. Because the spring is initially compressed, we will write A as a negative value. We can write the amplitude portion of the function as

A(t) = 5(1 - 0.30)t We put (1 - 0.30)t in the form ect as follows:

c = ln 0.7

Now let’s address the period. The spring cycles through its positions every 3 seconds, this is the period, and we can use the formula to find omega.

3 =  2\pi  _ ω 

ω =  2\p\frac{i}{3}  The natural length of 10 inches is the midline. We will use the cosine function, since the spring starts out at its maximum displacement. This portion of the equation is represented as

y = cos (  2\p\frac{i}{3} t ) + 10 Finally, we put both functions together. Our the model for the position of the spring at t seconds is given as

y = -5e-0.357t cos (  2\p\frac{i}{3} t ) + 10 See the graph in Figure 21. t y y = –5e–0.357t cos 3

**Try It #6**

A mass suspended from a spring is raised a distance of 5 cm above its resting position. The mass is released at time t = 0 and allowed to oscillate. After  \frac{1}{3}  second, it is observed that the mass returns to its highest position. Find a function to model this motion relative to its initial resting position.

**Example  13**

### Finding the Value of the Damping Constant c According to the Given Criteria

A guitar string is plucked and vibrates in damped harmonic motion. The string is pulled and displaced 2 cm from its resting position. After 3 seconds, the displacement of the string measures 1 cm. Find the damping constant.

**Solution**

The displacement factor represents the amplitude and is determined by the coefficient ae-ct in the model for damped harmonic motion. The damping constant is included in the term e-ct. It is known that after 3 seconds, the local maximum measures one-half of its original value. Therefore, we have the equation ae-c(t + 3) =  \frac{1}{2} ae-ct

Use algebra and the laws of exponents to solve for c.

ae-c(t + 3) =  \frac{1}{2} ae-ct

e-ct \cdot  e-3c =  \frac{1}{2} e-ct Divide out a.

e-3c =  \frac{1}{2}  Divide out e-ct.

e^{3}c = 2 Take reciprocals. Then use the laws of logarithms.

e^{3}c = 2

3c = ln(2)

c =  ln(2) _ 3  The damping constant is  ln(2) ___ 3 . Bounding Curves in Harmonic Motion Harmonic motion graphs may be enclosed by bounding curves. When a function has a varying amplitude, such that the amplitude rises and falls multiple times within a period, we can determine the bounding curves from part of the function.

**Example  14**

### Graphing an Oscillating Cosine Curve

Graph the function f(x) = cos(2\pi x) cos(16\pi x).

**Solution**

The graph produced by this function will be shown in two parts. The first graph will be the exact function f(x) (see Figure 22), and the second graph is the exact function f(x) plus a bounding function (see Figure 23). The graphs look quite different. f(x) x f(x) = cos (2\pi x) cos (16\pi x) y x f(x) = cos (2\pi x) cos (16\pi x) y = cos (2\pi x) y = –cos (2\pi x) Analysis The curves y = cos(2\pi x) and y = -cos(2\pi x) are bounding curves: they bound the function from above and below, tracing out the high and low points. The harmonic motion graph sits inside the bounding curves. This is an example of a function whose amplitude not only decreases with time, but actually increases and decreases multiple times within a period. Access these online resources for additional instruction and practice with trigonometric applications. • Solving Problems Using Trigonometry (http://openstaxcollege.org/l/solvetrigprob) • Ferris Wheel Trigonometry (http://openstaxcollege.org/l/ferriswheel) • Daily Temperatures and Trigonometry (http://openstaxcollege.org/l/dailytemp) • Simple Harmonic Motion (http://openstaxcollege.org/l/simpleharm)

7.6 SECTION EXERCISES Verbal 1. Explain what types of physical phenomena are best modeled by sinusoidal functions. What are the characteristics necessary? 2. What information is necessary to construct a trigonometric model of daily temperature? Give examples of two different sets of information that would enable modeling with an equation. 3. If we want to model cumulative rainfall over the course of a year, would a sinusoidal function be a good model? Why or why not? 4. Explain the effect of a damping factor on the graphs of harmonic motion functions. Algebraic For the following exercises, find a possible formula for the trigonometric function represented by the given table of values. 5. x y -4 -1 -1 -4 -1 6. x y -3 -3 x  \p\frac{i}{4}   \p\frac{i}{2}   3\p\frac{i}{4}  \pi   5\p\frac{i}{4}   3\p\frac{i}{2}  y -3 8. x y -3 -7 -3 -3 -7 9. x y -2 -2 y -3 -3 x -3 -2 -1 y -1 -\sqrt{2}  -1 1 - \sqrt{2}  \sqrt{2}  - 1 \sqrt{2}  + 1 x -1 y \sqrt{3}  - 2 2 - \sqrt{3}   \sqrt{3}  ____ 3  \sqrt{3}  2 + \sqrt{3}  Graphical For the following exercises, graph the given function, and then find a possible physical process that the equation could model. 13. f (x) = -30cos (  x\p\frac{i}{6}  ) - 20cos^{2} (  x\p\frac{i}{6}  ) + 80 [0, 12] 14. f (x) = -18cos (  x\p\frac{i}{12}  ) - 5sin (  x\p\frac{i}{12}  ) + 100 on the interval [0, 24] 15. f (x) = 10 - sin (  x\p\frac{i}{6}  ) + 24tan (  x\p\frac{i}{240}  ) on the interval [0, 80] Technology For the following exercise, construct a function modeling behavior and use a calculator to find desired results. 16. A city’s average yearly rainfall is currently 20 inches and varies seasonally by 5 inches. Due to unforeseen circumstances, rainfall appears to be decreasing by 15% each year. How many years from now would we expect rainfall to initially reach 0 inches? Note, the model is invalid once it predicts negative rainfall, so choose the first point at which it goes below 0.

## 7.6 Section Exercises

Real-World Applications For the following exercises, construct a sinusoidal function with the provided information, and then solve the equation for the requested values. 17. Outside temperatures over the course of a day can be modeled as a sinusoidal function. Suppose the high temperature of 105°F occurs at 5PM and the average temperature for the day is 85°F. Find the temperature, to the nearest degree, at 9AM. 18. Outside temperatures over the course of a day can be modeled as a sinusoidal function. Suppose the high temperature of 84°F occurs at 6PM and the average temperature for the day is 70°F. Find the temperature, to the nearest degree, at 7AM. 19. Outside temperatures over the course of a day can be modeled as a sinusoidal function. Suppose the temperature varies between 47°F and 63°F during the day and the average daily temperature first occurs at 10 AM. How many hours after midnight does the temperature first reach 51°F? 20. Outside temperatures over the course of a day can be modeled as a sinusoidal function. Suppose the temperature varies between 64°F and 86°F during the day and the average daily temperature first occurs at 12 AM. How many hours after midnight does the temperature first reach 70°F? 21. A Ferris wheel is 20 meters in diameter and boarded from a platform that is 2 meters above the ground. The six o’clock position on the Ferris wheel is level with the loading platform. The wheel completes 1 full revolution in 6 minutes. How much of the ride, in minutes and seconds, is spent higher than 13 meters above the ground? 22. A Ferris wheel is 45 meters in diameter and boarded from a platform that is 1 meter above the ground. The six o’clock position on the Ferris wheel is level with the loading platform. The wheel completes 1 full revolution in 10 minutes. How many minutes of the ride are spent higher than 27 meters above the ground? Round to the nearest second 23. The sea ice area around the North Pole fluctuates between about 6 million square kilometers on September 1 to 14 million square kilometers on March 1. Assuming a sinusoidal fluctuation, when are there less than 9 million square kilometers of sea ice? Give your answer as a range of dates, to the nearest day. 24. The sea ice area around the South Pole fluctuates between about 18 million square kilometers in September to 3 million square kilometers in March. Assuming a sinusoidal fluctuation, when are there more than 15 million square kilometers of sea ice? Give your answer as a range of dates, to the nearest day. 25. During a 90-day monsoon season, daily rainfall can be modeled by sinusoidal functions. If the rainfall fluctuates between a low of 2 inches on day 10 and 12 inches on day 55, during what period is daily rainfall more than 10 inches? 26. During a 90-day monsoon season, daily rainfall can be modeled by sinusoidal functions. A low of 4 inches of rainfall was recorded on day 30, and overall the average daily rainfall was 8 inches. During what period was daily rainfall less than 5 inches? 27. In a certain region, monthly precipitation peaks at 8 inches on June 1 and falls to a low of 1 inch on December 1. Identify the periods when the region is under flood conditions (greater than 7 inches) and drought conditions (less than 2 inches). Give your answer in terms of the nearest day. 28. In a certain region, monthly precipitation peaks at 24 inches in September and falls to a low of 4 inches in March. Identify the periods when the region is under flood conditions (greater than 22 inches) and drought conditions (less than 5 inches). Give your answer in terms of the nearest day. For the following exercises, find the amplitude, period, and frequency of the given function. 29. The displacement h(t) in centimeters of a mass suspended by a spring is modeled by the function h(t) = 8sin(6\pi t),where t is measured in seconds. Find the amplitude, period, and frequency of this displacement. 30. The displacement h(t) in centimeters of a mass suspended by a spring is modeled by the function h(t) = 11sin(12\pi t), where t is measured in seconds. Find the amplitude, period, and frequency of this displacement.

31. The displacement h(t) in centimeters of a mass suspended by a spring is modeled by the function h(t) = 4cos (  \p\frac{i}{2} t ), where t is measured in seconds. Find the amplitude, period, and frequency of this displacement. For the following exercises, construct an equation that models the described behavior. 32. The displacement h(t), in centimeters, of a mass suspended by a spring is modeled by the function h(t) = -5 cos(60\pi t), where t is measured in seconds. Find the amplitude, period, and frequency of this displacement. For the following exercises, construct an equation that models the described behavior. 33. A deer population oscillates 19 above and below average during the year, reaching the lowest value in January. The average population starts at 800 deer and increases by 160 each year. Find a function that models the population, P, in terms of months since January, t. 34. A rabbit population oscillates 15 above and below average during the year, reaching the lowest value in January. The average population starts at 650 rabbits and increases by 110 each year. Find a function that models the population, P, in terms of months since January, t. 35. A muskrat population oscillates 33 above and below average during the year, reaching the lowest value in January. The average population starts at 900 muskrats and increases by 7% each month. Find a function that models the population, P, in terms of months since January, t. 36. A fish population oscillates 40 above and below average during the year, reaching the lowest value in January. The average population starts at 800 fish and increases by 4% each month. Find a function that models the population, P, in terms of months since January, t. 37. A spring attached to the ceiling is pulled 10 cm down from equilibrium and released. The amplitude decreases by 15% each second. The spring oscillates 18 times each second. Find a function that models the distance, D, the end of the spring is from equilibrium in terms of seconds, t, since the spring was released. 38. A spring attached to the ceiling is pulled 7 cm down from equilibrium and released. The amplitude decreases by 11% each second. The spring oscillates 20 times each second. Find a function that models the distance, D, the end of the spring is from equilibrium in terms of seconds, t, since the spring was released. 39. A spring attached to the ceiling is pulled 17 cm down from equilibrium and released. After 3 seconds, the amplitude has decreased to 13 cm. The spring oscillates 14 times each second. Find a function that models the distance, D, the end of the spring is from equilibrium in terms of seconds, t, since the spring was released. 40. A spring attached to the ceiling is pulled 19 cm down from equilibrium and released. After 4 seconds, the amplitude has decreased to 14 cm. The spring oscillates 13 times each second. Find a function that models the distance, D, the end of the spring is from equilibrium in terms of seconds, t, since the spring was released. For the following exercises, create a function modeling the described behavior. Then, calculate the desired result using a calculator. 41. A certain lake currently has an average trout population of 20,000. The population naturally oscillates above and below average by 2,000 every year. This year, the lake was opened to fishermen. If fishermen catch 3,000 fish every year, how long will it take for the lake to have no more trout? 42. Whitefish populations are currently at 500 in a lake. The population naturally oscillates above and below by 25 each year. If humans overfish, taking 4% of the population every year, in how many years will the lake first have fewer than 200 whitefish? 43. A spring attached to a ceiling is pulled down 11 cm from equilibrium and released. After 2 seconds, the amplitude has decreased to 6 cm. The spring oscillates 8 times each second. Find when the spring first comes between -0.1 and 0.1 cm, effectively at rest. 44. A spring attached to a ceiling is pulled down 21 cm from equilibrium and released. After 6 seconds, the amplitude has decreased to 4 cm. The spring oscillates 20 times each second. Find when the spring first comes between -0.1 and 0.1 cm, effectively at rest.

45. Two springs are pulled down from the ceiling and released at the same time. The first spring, which oscillates 8 times per second, was initially pulled down 32 cm from equilibrium, and the amplitude decreases by 50% each second. The second spring, oscillating 18 times per second, was initially pulled down 15 cm from equilibrium and after 4 seconds has an amplitude of 2 cm. Which spring comes to rest first, and at what time? Consider “rest” as an amplitude less than 0.1 cm. 46. Two springs are pulled down from the ceiling and released at the same time. The first spring, which oscillates 14 times per second, was initially pulled down 2 cm from equilibrium, and the amplitude decreases by 8% each second. The second spring, oscillating 22 times per second, was initially pulled down 10 cm from equilibrium and after 3 seconds has an amplitude of 2 cm. Which spring comes to rest first, and at what time? Consider “rest” as an amplitude less than 0.1 cm. Extensions 47. A plane flies 1 hour at 150 mph at 22° east of north, then continues to fly for 1.5 hours at 120 mph, this time at a bearing of 112° east of north. Find the total distance from the starting point and the direct angle flown north of east. 48. A plane flies 2 hours at 200 mph at a bearing of 60°, then continues to fly for 1.5 hours at the same speed, this time at a bearing of 150°. Find the distance from the starting point and the bearing from the starting point. Hint: bearing is measured counterclockwise from north. For the following exercises, find a function of the form y = abx + csin (  \p\frac{i}{2} x ) that fits the given data. x y y y -40 For the following exercises, find a function of the form y = abx cos(  \p\frac{i}{2} x ) + c that fits the given data. y y -11

### Key Terms

damped harmonic motion oscillating motion that resembles periodic motion and simple harmonic motion, except that the graph is affected by a damping factor, an energy dissipating influence on the motion, such as friction double-angle formulas identities derived from the sum formulas for sine, cosine, and tangent in which the angles are equal even-odd identities set of equations involving trigonometric functions such that if f (-x) = -f (x), the identity is odd, and if f (-x) = f (x), the identity is even half-angle formulas identities derived from the reduction formulas and used to determine half-angle values of trigonometric functions product-to-sum formula a trigonometric identity that allows the writing of a product of trigonometric functions as a sum or difference of trigonometric functions Pythagorean identities set of equations involving trigonometric functions based on the right triangle properties quotient identities pair of identities based on the fact that tangent is the ratio of sine and cosine, and cotangent is the ratio of cosine and sine reciprocal identities set of equations involving the reciprocals of basic trigonometric definitions reduction formulas identities derived from the double-angle formulas and used to reduce the power of a trigonometric function simple harmonic motion a repetitive motion that can be modeled by periodic sinusoidal oscillation sum-to-product formula a trigonometric identity that allows, by using substitution, the writing of a sum of trigonometric functions as a product of trigonometric functions Key Equations Pythagorean identities sin^{2} \theta  + cos^{2} \theta  = 1 1 + cot^{2} \theta  = csc^{2} \theta  1 + tan^{2} \theta  = sec^{2} \theta  Even-odd identities tan(-\theta ) = -tan \theta  cot(-\theta ) = -cot \theta  sin(-\theta ) = -sin \theta  csc(-\theta ) = -csc \theta  cos(-\theta ) = cos \theta  sec(-\theta ) = sec \theta  Reciprocal identities sin \theta  =  \frac{1}{c}sc \theta   cos \theta  =  \frac{1}{s}ec \theta   tan \theta  =  \frac{1}{c}ot \theta   csc \theta  =  \frac{1}{s}in \theta   sec \theta  =  \frac{1}{c}os \theta   cot \theta  =  \frac{1}{t}an \theta  

Quotient identities tan \theta  =  sin \thet\frac{a}{c}os \theta   cot \theta  =  cos \thet\frac{a}{s}in \theta   Sum Formula for Cosine cos(\alpha  + \beta ) = cos \alpha  cos \beta  - sin \alpha  sin \beta  Difference Formula for Cosine cos(\alpha  - \beta ) = cos \alpha  cos \beta  + sin \alpha  sin \beta  Sum Formula for Sine sin(\alpha  + \beta )= sin \alpha  cos \beta  + cos \alpha  sin \beta  Difference Formula for Sine sin(\alpha  - \beta ) = sin \alpha  cos \beta  - cos \alpha  sin \beta  Sum Formula for Tangent tan(\alpha  + \beta ) =  tan \alpha  + tan \beta 

___________

1 - tan \alpha  tan \beta   Difference Formula for Tangent tan(\alpha  - \beta ) =  tan \alpha  - tan \beta 

___________

1 + tan \alpha  tan \beta   Cofunction identities sin \theta  = cos(  \p\frac{i}{2}  - \theta  ) cos \theta  = sin(  \p\frac{i}{2}  - \theta  ) tan \theta  = cot(  \p\frac{i}{2}  - \theta  ) cot \theta  = tan(  \p\frac{i}{2}  - \theta  ) sec \theta  = csc(  \p\frac{i}{2}  - \theta  ) csc \theta  = sec(  \p\frac{i}{2}  - \theta  ) Double-angle formulas sin(2\theta ) = 2sin \theta  cos \theta  cos(2\theta ) = cos^{2} \theta  - sin^{2} \theta  = 1 - 2sin^{2} \theta  = 2cos^{2} \theta  - 1 tan(2\theta ) =  2tan \theta  ________ 1 - tan^{2} \theta   Reduction formulas sin^{2}\theta  =  1 - cos(2\theta ) _________  cos^{2}\theta  =  1 + cos(2\theta ) _________  tan^{2}\theta  =  1 - cos(2\theta ) _________ 1 + cos(2\theta ) 

Half-angle formulas sin  \alph\frac{a}{2}  = \pm \sqrt{_________}  1 - cos \alpha  _______   cos  \alph\frac{a}{2}  = \pm \sqrt{_________}  1 + cos \alpha  _______   tan  \alph\frac{a}{2}  = \pm \sqrt{_________}  1 - cos \alpha  _______ 1 + cos \alpha   

=  sin \alpha  _______ 1 + cos \alpha  

=  1 - cos \alpha  _______ sin \alpha   Product-to-sum Formulas cos \alpha  cos \beta  =  \frac{1}{2} [cos(\alpha  - \beta ) + cos(\alpha  + \beta )] sin \alpha  cos \beta  =  \frac{1}{2} [sin(\alpha  + \beta ) + sin(\alpha  - \beta )] sin \alpha  sin \beta  =  \frac{1}{2} [cos(\alpha  - \beta ) - cos(\alpha  + \beta )] cos \alpha  sin \beta  =  \frac{1}{2} [sin(\alpha  + \beta ) - sin(\alpha  - \beta )] Sum-to-product Formulas sin \alpha  + sin \beta  = 2 sin(  \alpha  + \beta  _____  )cos(  \alpha  - \beta  _____  ) sin \alpha  - sin \beta  = 2 sin(  \alpha  - \beta  _____  )cos(  \alpha  + \beta  _____  ) cos \alpha  - cos \beta  = -2 sin(  \alpha  + \beta  _____  )sin(  \alpha  - \beta  _____  ) cos \alpha  + cos \beta  = 2cos(  \alpha  + \beta  _____  )cos(  \alpha  - \beta  _____  ) Standard form of sinusoidal equation y = A sin(Bt - C) + D or y = A cos(Bt - C) + D Simple harmonic motion d = a cos(ωt) or d = a sin(ωt) Damped harmonic motion f (t) = ae-ct sin(ωt) or f (t) = ae-ct cos(ωt)

### Key Concepts

• There are multiple ways to represent a trigonometric expression. Verifying the identities illustrates how expressions can be rewritten to simplify a problem. • Graphing both sides of an identity will verify it. See Example 1. • Simplifying one side of the equation to equal the other side is another method for verifying an identity. See

**Example 2** — and Example 3.
• The approach to verifying an identity depends on the nature of the identity. It is often useful to begin on the more complex side of the equation. See Example 4. • We can create an identity by simplifying an expression and then verifying it. See Example 5. • Verifying an identity may involve algebra with the fundamental identities. See Example 6 and Example 7.

• Algebraic techniques can be used to simplify trigonometric expressions. We use algebraic techniques throughout this text, as they consist of the fundamental rules of mathematics. See Example 8, Example 9, and Example 10. 7.2 Sum and Difference Identities • The sum formula for cosines states that the cosine of the sum of two angles equals the product of the cosines of the angles minus the product of the sines of the angles. The difference formula for cosines states that the cosine of the difference of two angles equals the product of the cosines of the angles plus the product of the sines of the angles. • The sum and difference formulas can be used to find the exact values of the sine, cosine, or tangent of an angle. See Example 1 and Example 2. • The sum formula for sines states that the sine of the sum of two angles equals the product of the sine of the first angle and cosine of the second angle plus the product of the cosine of the first angle and the sine of the second angle. The difference formula for sines states that the sine of the difference of two angles equals the product of the sine of the first angle and cosine of the second angle minus the product of the cosine of the first angle and the sine of the second angle. See Example 3. • The sum and difference formulas for sine and cosine can also be used for inverse trigonometric functions. See

**Example 4** — .
• The sum formula for tangent states that the tangent of the sum of two angles equals the sum of the tangents of the angles divided by 1 minus the product of the tangents of the angles. The difference formula for tangent states that the tangent of the difference of two angles equals the difference of the tangents of the angles divided by 1 plus the product of the tangents of the angles. See Example 5. • The Pythagorean Theorem along with the sum and difference formulas can be used to find multiple sums and differences of angles. See Example 6. • The cofunction identities apply to complementary angles and pairs of reciprocal functions. See Example 7. • Sum and difference formulas are useful in verifying identities. See Example 8 and Example 9. • Application problems are often easier to solve by using sum and difference formulas. See Example 10 and Example 11. 7.3 Double-Angle, Half-Angle, and Reduction Formulas • Double-angle identities are derived from the sum formulas of the fundamental trigonometric functions: sine, cosine, and tangent. See Example 1, Example 2, Example 3, and Example 4. • Reduction formulas are especially useful in calculus, as they allow us to reduce the power of the trigonometric term. See Example 5 and Example 6. • Half-angle formulas allow us to find the value of trigonometric functions involving half-angles, whether the original angle is known or not. See Example 7, Example 8, and Example 9. 7.4 Sum-to-Product and Product-to-Sum Formulas • From the sum and difference identities, we can derive the product-to-sum formulas and the sum-to-product formulas for sine and cosine. • We can use the product-to-sum formulas to rewrite products of sines, products of cosines, and products of sine and cosine as sums or differences of sines and cosines. See Example 1, Example 2, and Example 3. • We can also derive the sum-to-product identities from the product-to-sum identities using substitution. • We can use the sum-to-product formulas to rewrite sum or difference of sines, cosines, or products sine and cosine as products of sines and cosines. See Example 4.

• Trigonometric expressions are often simpler to evaluate using the formulas. See Example 5. • The identities can be verified using other formulas or by converting the expressions to sines and cosines. To verify an identity, we choose the more complicated side of the equals sign and rewrite it until it is transformed into the other side. See Example 6 and Example 7. 7.5 Solving Trigonometric Equations • When solving linear trigonometric equations, we can use algebraic techniques just as we do solving algebraic equations. Look for patterns, like the difference of squares, quadratic form, or an expression that lends itself well to substitution. See Example 1, Example 2, and Example 3. • Equations involving a single trigonometric function can be solved or verified using the unit circle. See Example 4,

**Example 5** — , and Example 6, and Example 7.
• We can also solve trigonometric equations using a graphing calculator. See Example 8 and Example 9. • Many equations appear quadratic in form. We can use substitution to make the equation appear simpler, and then use the same techniques we use solving an algebraic quadratic: factoring, the quadratic formula, etc. See Example 10, Example 11, Example 12, and Example 13. • We can also use the identities to solve trigonometric equation. See Example 14, Example 15, and Example 16. • We can use substitution to solve a multiple-angle trigonometric equation, which is a compression of a standard trigonometric function. We will need to take the compression into account and verify that we have found all solutions on the given interval. See Example 17. • Real-world scenarios can be modeled and solved using the Pythagorean Theorem and trigonometric functions. See Example 18. 7.6 Modeling with Trigonometric Equations • Sinusoidal functions are represented by the sine and cosine graphs. In standard form, we can find the amplitude, period, and horizontal and vertical shifts. See Example 1 and Example 2. • Use key points to graph a sinusoidal function. The five key points include the minimum and maximum values and the midline values. See Example 3. • Periodic functions can model events that reoccur in set cycles, like the phases of the moon, the hands on a clock, and the seasons in a year. See Example 4, Example 5, Example 6 and Example 7. • Harmonic motion functions are modeled from given data. Similar to periodic motion applications, harmonic motion requires a restoring force. Examples include gravitational force and spring motion activated by weight. See Example 8. • Damped harmonic motion is a form of periodic behavior affected by a damping factor. Energy dissipating factors, like friction, cause the displacement of the object to shrink. See Example 9, Example 10, Example 11, Example 12, and Example 13. • Bounding curves delineate the graph of harmonic motion with variable maximum and minimum values. See

**Example 14** — .

### Solving Trigonometric Equations with Identities

For the following exercises, find all solutions exactly that exist on the interval [0, 2\pi ). 1. csc^{2} t = 3 2. cos^{2} x =  \frac{1}{4}  3. 2sin \theta  = -1 4. tan x sin x + sin(-x) = 0 5. 9sin ω - 2 = 4 sin^{2} ω 6. 1 - 2tan(ω) = tan^{2}(ω) For the following exercises, use basic identities to simplify the expression. 7. sec x cos x + cos x -  1 ____ sec x  8. sin^{3} x + cos^{2} x sin x For the following exercises, determine if the given identities are equivalent. 9. sin^{2} x + sec^{2} x - 1 =  (1 - cos^{2} x)(1 + cos^{2} x)

__

cos^{2} x  10. tan^{3} x csc^{2} x cot^{2} x cos x sin x = 1 Sum and Difference Identities For the following exercises, find the exact value. 11. tan (  7\pi  ___ 12  ) 12. cos (  25\pi  ___ 12  ) 13. sin(70°)cos(25°) - cos(70°)sin(25°) 14. cos(83°)cos(23°) + sin(83°)sin(23°) For the following exercises, prove the identity. 15. cos(4x) - cos(3x)cosx = sin^{2} x - 4cos^{2} x sin^{2} x 16. cos(3x) - cos^{3} x = - cos x sin^{2} x - sin x sin(2x) For the following exercise, simplify the expression. 17.  tan(  \frac{1}{2} x ) + tan(  \frac{1}{8} x )

___

1 - tan(  \frac{1}{8} x ) tan(  \frac{1}{2} x )  For the following exercises, find the exact value. 18. cos ( sin-1 (0) - cos-1 (  \frac{1}{2}  ) ) 19. tan ( sin-1 (0) + sin-1 (  \frac{1}{2}  ) ) Double-Angle, Half-Angle, and Reduction Formulas For the following exercises, find the exact value. 20. Find sin(2\theta ), cos(2\theta ), and tan(2\theta ) given cos \theta  = - \frac{1}{3}  and \theta  is in the interval [  \p\frac{i}{2} , \pi  ]  21. Find sin(2\theta ), cos(2\theta ), and tan(2\theta ) given sec \theta  = - \frac{5}{3}  and \theta  is in the interval [  \p\frac{i}{2} , \pi  ]  22. sin (  7\pi  ___ 8  ) 23. sec (  3\pi  ___ 8  )

For the following exercises, use Figure 1 to find the desired quantities. \alpha  \beta  24. sin(2\beta ), cos(2\beta ), tan(2\beta ), sin(2\alpha ), cos(2\alpha ), and tan(2\alpha ) 25. sin (  \bet\frac{a}{2}  ), cos (  \bet\frac{a}{2}  ), tan (  \bet\frac{a}{2}  ), sin (  \alph\frac{a}{2}  ), cos (  \alph\frac{a}{2}  ), and tan (  \alph\frac{a}{2}  ) For the following exercises, prove the identity. _______ sin(2x)  = cot x - tan x 27. cot x cos(2x) = - sin(2x) + cot x For the following exercises, rewrite the expression with no powers. 28. cos^{2} x sin^{4}(2x) 29. tan^{2} x sin^{3} x Sum-to-Product and Product-to-Sum Formulas For the following exercises, evaluate the product for the given expression using a sum or difference of two functions. Write the exact answer. 30. cos (  \p\frac{i}{3}  ) sin (  \p\frac{i}{4}  ) 31. 2sin (  2\p\frac{i}{3}  ) sin (  5\p\frac{i}{6}  ) 32. 2cos (  \p\frac{i}{5}  ) cos (  \p\frac{i}{3}  ) For the following exercises, evaluate the sum by using a product formula. Write the exact answer. 33. sin (  \p\frac{i}{12}  ) - sin (  7\p\frac{i}{12}  ) 34. cos (  5\p\frac{i}{12}  ) + cos (  7\p\frac{i}{12}  ) For the following exercises, change the functions from a product to a sum or a sum to a product. 35. sin(9x)cos(3x) 36. cos(7x)cos(12x) 37. sin(11x) + sin(2x) 38. cos(6x) + cos(5x) Solving Trigonometric Equations For the following exercises, find all exact solutions on the interval [0, 2\pi ). 39. tan x + 1 = 0 40. 2sin(2x) + \sqrt{2}  = 0 For the following exercises, find all exact solutions on the interval [0, 2\pi ). 41. 2sin^{2} x - sin x = 0 42. cos^{2} x - cos x - 1 = 0 43. 2sin^{2} x + 5 sin x + 3 = 0 44. cos x - 5sin(2x) = 0 ____ sec^{2} x  + 2 + sin^{2} x + 4cos^{2} x = 0

For the following exercises, simplify the equation algebraically as much as possible. Then use a calculator to find the solutions on the interval [0, 2\pi ). Round to four decimal places. 3  cot^{2} x + cot x = 1 47. csc^{2} x - 3csc x - 4 = 0 For the following exercises, graph each side of the equation to find the zeroes on the interval [0, 2\pi ). 48. 20cos^{2} x + 21cos x + 1 = 0 49. sec^{2} x - 2sec x = 15 Modeling with Trigonometric Equations For the following exercises, graph the points and find a possible formula for the trigonometric values in the given table. x y x y -2 -2 -5 -2 x -3 -2 -1 y 3 + 2\sqrt{2}  2\sqrt{2}  - 1 3 - 2\sqrt{2}  -1 -1 - 2\sqrt{2}  53. A man with his eye level 6 feet above the ground is standing 3 feet away from the base of a 15-foot vertical ladder. If he looks to the top of the ladder, at what angle above horizontal is he looking? 54. Using the ladder from the previous exercise, if a 6-foot-tall construction worker standing at the top of the ladder looks down at the feet of the man standing at the bottom, what angle from the horizontal is he looking? For the following exercises, construct functions that model the described behavior. 55. A population of lemmings varies with a yearly low of 500 in March. If the average yearly population of lemmings is 950, write a function that models the population with respect to t, the month. 56. Daily temperatures in the desert can be very extreme. If the temperature varies from 90°F to 30°F and the average daily temperature first occurs at 10 AM, write a function modeling this behavior. For the following exercises, find the amplitude, frequency, and period of the given equations. 57. y = 3cos(x\pi ) 58. y = -2sin(16x\pi ) For the following exercises, model the described behavior and find requested values. 59. An invasive species of carp is introduced to Lake Freshwater. Initially there are 100 carp in the lake and the population varies by 20 fish seasonally. If by year 5, there are 625 carp, find a function modeling the population of carp with respect to t, the number of years from now. 60. The native fish population of Lake Freshwater averages 2500 fish, varying by 100 fish seasonally. Due to competition for resources from the invasive carp, the native fish population is expected to decrease by 5% each year. Find a function modeling the population of native fish with respect to t, the number of years from now. Also determine how many years it will take for the carp to overtake the native fish population.

For the following exercises, simplify the given expression. 1. cos(-x)sin x cot x + sin^{2} x 2. sin(-x)cos(-2x)-sin(-x)cos(-2x) For the following exercises, find the exact value. 3. cos (  7\p\frac{i}{12}  ) 4. tan (  3\pi  ___ 8  ) 5. tan ( sin-1 (  \sqrt{2}  ____ 2  ) + tan-1 \sqrt{3}  ) 6. 2sin (  \p\frac{i}{4}  ) sin (  \p\frac{i}{6}  ) For the following exercises, find all exact solutions to the equation on [0, 2\pi ). 7. cos^{2} x - sin^{2} x - 1 = 0 8. cos^{2} x = cos x 4sin^{2} x + 2sin x - 3 = 0 9. cos(2x) + sin^{2} x = 0 10. 2sin^{2} x - sin x = 0 11. Rewrite the expression as a product instead of a sum: cos(2x) + cos(-8x). 12. Find all solutions of tan(x) - \sqrt{13.} Find the solutions of sec^{2} x - 2sec x = 15 on the interval [0, 2\pi ) algebraically; then graph both sides of the equation to determine the answer. 14. Find sin(2\theta ), cos(2\theta ), and tan(2\theta ) given cot \theta  = - \frac{3}{4}  and \theta  is on the interval [  \p\frac{i}{2} , \pi  ] . 15. Find sin(  \thet\frac{a}{2}  ), cos(  \thet\frac{a}{2}  ), and tan(  \thet\frac{a}{2}  ) given cos \theta  =  \frac{7}{25}  and \theta  is in quadrant IV. 16. Rewrite the expression sin^{4} x with no powers greater than 1. For the following exercises, prove the identity. 17. tan^{3} x - tan x sec^{2} x = tan(-x) 18. sin(3x) - cos x sin(2x) = cos^{2} x sin x - sin^{3} x 19.  sin(2x) ______ sin x  -  cos(2x) ______ cos x  = sec x 20. Plot the points and find a function of the form y = Acos(Bx + C) + D that fits the given data. x y -2 -2 -2 21. The displacement h(t) in centimeters of a mass suspended by a spring is modeled by the function h(t) =  \frac{1}{4}  sin(120\pi t), where t is measured in seconds. Find the amplitude, period, and frequency of this displacement. 22. A woman is standing 300 feet away from a 2,000- foot building. If she looks to the top of the building, at what angle above horizontal is she looking? A bored worker looks down at her from the 15th floor (1500 feet above her). At what angle is he looking down at her? Round to the nearest tenth of a degree. 23. Two frequencies of sound are played on an instrument governed by the equation n(t) = 8 cos(20\pi t)cos(1,000\pi t). What are the period and frequency of the “fast” and “slow” oscillations? What is the amplitude? 24. The average monthly snowfall in a small village in the Himalayas is 6 inches, with the low of 1 inch occurring in July. Construct a function that models this behavior. During what period is there more than 10 inches of snowfall? 25. A spring attached to a ceiling is pulled down 20 cm. After 3 seconds, wherein it completes 6 full periods, the amplitude is only 15 cm. Find the function modeling the position of the spring t seconds after being released. At what time will the spring come to rest? In this case, use 1 cm amplitude as rest. 26. Water levels near a glacier currently average 9 feet, varying seasonally by 2 inches above and below the average and reaching their highest point in January. Due to global warming, the glacier has begun melting faster than normal. Every year, the water levels rise by a steady 3 inches. Find a function modeling the depth of the water t months from now. If the docks are 2 feet above current water levels, at what point will the water first rise above the docks?
