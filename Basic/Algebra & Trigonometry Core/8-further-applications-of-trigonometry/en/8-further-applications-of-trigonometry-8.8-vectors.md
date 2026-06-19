# Further Applications of Trigonometry

## 8.8 Vectors

---
Learning Objectives
In this section, you will:
• View vectors geometrically.
• Find magnitude and direction.
• Perform vector addition and scalar multiplication.
• Find the component form of a vector.
• Find the unit vector in the direction of v.
• Perform operations with vectors in terms of i and j.
• Find the dot product of two vectors.
An airplane is flying at an airspeed of 200 miles per hour headed on a SE bearing of 140°.
A north wind (from north to south) is blowing at 16.2 miles per hour, as shown in Figure 1.
What are the ground speed and actual bearing of the plane?
N A O B X C 140 ̊ 16.2 α Ground speed refers to the speed of a plane relative to the ground.
Airspeed refers to the speed a plane can travel relative to its surrounding air mass.
These two quantities are not the same because of the effect of wind.
In an earlier section, we used triangles to solve a similar problem involving the movement of boats.
Later in this section, we will find the airplane’s groundspeed and bearing, while investigating another approach to problems of this type.
First, however, let’s examine the basics of vectors.
A Geometric View of Vectors A vector is a specific quantity drawn as a line segment with an arrowhead at one end.
It has an initial point, where it begins, and a terminal point, where it ends.
A vector is defined by its magnitude, or the length of the line, and its direction, indicated by an arrowhead at the terminal point.
Thus, a vector is a directed line segment.
There are various symbols that distinguish vectors from other quantities: • Lower case, boldfaced type, with or without an arrow on top such as v, u, w, v, u, w.
• Given initial point P and terminal point Q, a vector can be represented as PQ.
The arrowhead on top is what indicates that it is not just a line, but a directed line segment. • Given an initial point of (0, 0) and terminal point (a, b), a vector may be represented as 〈a, b〉.
This last symbol 〈a, b〉 has special significance.
It is called the standard position.
The position vector has an initial point (0, 0) and a terminal point 〈a, b〉.
To change any vector into the position vector, we think about the change in the x-coordinates and the change in the y-coordinates.
Thus, if the initial point of a vector CD is C(x¹, y¹) and the terminal point is D(x², y²), then the position vector is found by calculating AB = 〈x² - x¹, y² - y¹〉

= 〈a, b〉 →→→ → → →

In Figure 2, we see the original vector CD and the position vector AB. x D A C y B (a, b) properties of vectors A vector is a directed line segment with an initial point and a terminal point.
Vectors are identified by magnitude, or the length of the line, and direction, represented by the arrowhead pointing toward the terminal point.
The position vector has an initial point at (0, 0) and is identified by its terminal point 〈a, b〉.

---
### 📐 **Example 1**
Find the Position Vector Consider the vector whose initial point is P(2, 3) and terminal point is Q(6, 4). Find the position vector.

**Solution**

The position vector is found by subtracting one x-coordinate from the other x-coordinate, and one y-coordinate from the other y-coordinate.
Thus

v = 〈6 -2, 4 -3〉

The position vector begins at (0, 0) and terminates at (4, 1). The graphs of both vectors are shown in Figure 3. x y We see that the position vector is 〈4, 1〉.

---
### 📐 **Example 2**:
Drawing a Vector with the Given Criteria and Its Equivalent Position Vector

Find the position vector given that vector v has an initial point at (-3, 2) and a terminal point at (4, 5), then graph both vectors in the same plane.

**Solution**

The position vector is found using the following calculation:

v = 〈4 - ( - 3), 5 - 2〉

Thus, the position vector begins at (0, 0) and terminates at (7, 3). See Figure 4. → →

x y Position vector

---
### ✏️ **Try It #1**
Draw a vector v that connects from the origin to the point (3, 5).
Finding Magnitude and Direction To work with a vector, we need to be able to find its magnitude and its direction.
We find its magnitude using the Pythagorean Theorem or the distance formula, and we find its direction using the inverse tangent function. magnitude and direction of a vector Given a position vector v = 〈a, b〉, the magnitude is found by | v | = √a² + b² .
The direction is equal to the angle formed with the x-axis, or with the y-axis, depending on the application.
For a position vector, the direction is found by tan θ = ( (b)/(a) ) ⇒ θ = tan-1( (b)/(a) ) , as illustrated in Figure 5. x y |v| θ 〈a, b〉 Two vectors v and u are considered equal if they have the same magnitude and the same direction.
Additionally, if both vectors have the same position vector, they are equal.

---
### 📐 **Example 3**
Finding the Magnitude and Direction of a Vector Find the magnitude and direction of the vector with initial point P(-8, 1) and terminal point Q(-2, -5). Draw the vector.

**Solution**

First, find the position vector.

u = 〈-2, - (-8), -5-1〉

= 〈6, - 6〉 We use the Pythagorean Theorem to find the magnitude.

| u | =√(6)² + (-6)² 

= √72 

= 6√2 

The direction is given as


> **tan θ = -6 6 = -1 ⇒ θ = tan -1(-1)**


= -45° However, the angle terminates in the fourth quadrant, so we add 360° to obtain a positive angle.
Thus, -45° + 360° = 315°.
See Figure 6. 315° x y

---
### 📐 **Example 4**
Showing That Two Vectors Are Equal Show that vector v with initial point at (5, -3) and terminal point at (-1, 2) is equal to vector u with initial point at (-1, -3) and terminal point at (-7, 2).
Draw the position vector on the same grid as v and u.
Next, find the magnitude and direction of each vector.

**Solution**

As shown in Figure 7, draw the vector v starting at initial (5, -3) and terminal point (-1, 2).
Draw the vector u with initial point (-1, -3) and terminal point (-7, 2).
Find the standard position for each.
Next, find and sketch the position vector for v and u.
We have

v = 〈-1 - 5, 2 - ( - 3)〉

= 〈-6, 5〉

u = 〈-7 - (-1), 2 - (-3)〉

= 〈-6, 5〉 Since the position vectors are the same, v and u are the same.
An alternative way to check for vector equality is to show that the magnitude and direction are the same for both vectors.
To show that the magnitudes are equal, use the Pythagorean Theorem.

| v | = √—

(-1 - 5)² + (2 - (-3))² 

= √(-6)² + (5)² 

= √—

= √61 

| u | = √—

(-7 - (-1))² + (2 - (-3))² 

= √(-6)² + (5)² 

= √—

= √61 As the magnitudes are equal, we now need to verify the direction.
Using the tangent function with the position vector gives


> **tan θ = - 5/6 ⇒ θ = tan-1( - 5/6 )**


However, we can see that the position vector terminates in the second quadrant, so we add 180°.
Thus, the direction

x v u Position vector y Performing Vector Addition and Scalar Multiplication Now that we understand the properties of vectors, we can perform operations involving them.
While it is convenient to think of the vector u = 〈x, y〉 as an arrow or directed line segment from the origin to the point (x, y), vectors can be situated anywhere in the plane.
The sum of two vectors u and v, or vector addition, produces a third vector u+ v, the resultant vector.
To find u + v, we first draw the vector u, and from the terminal end of u, we drawn the vector v.
In other words, we have the initial point of v meet the terminal end of u.
This position corresponds to the notion that we move along the first vector and then, from its terminal point, we move along the second vector.
The sum u + v is the resultant vector because it results from addition or subtraction of two vectors.
The resultant vector travels directly from the beginning of u to the end of v in a straight path, as shown in Figure 8. -v v u u u - v u + v Vector subtraction is similar to vector addition.
To find u - v, view it as u + (-v).
Adding -v is reversing direction of v and adding it to the end of u.
The new vector begins at the start of u and stops at the end point of -v.
See Figure 9 for a visual that compares vector addition and vector subtraction using parallelograms. u v u + v –v u u u – v

---
### 📐 **Example 5**:
Adding and Subtracting Vectors

Given u = 〈3, - 2〉 and v = 〈-1, 4〉, find two new vectors u + v, and u - v.

**Solution**

To find the sum of two vectors, we add the components.
Thus,

u + v = 〈3, - 2〉 + 〈-1, 4〉

= 〈3 + ( - 1), - 2 + 4〉

See Figure 10(a). To find the difference of two vectors, add the negative components of v to u. Thus,

u + (-v) = 〈3, - 2〉 + 〈1, -4〉

= 〈3 + 1, - 2 + (-4)〉

= 〈4, - 6〉

See Figure 10(b). x u v u + v y (a) - v (b) x u u - v y Multiplying By a Scalar While adding and subtracting vectors gives us a new vector with a different magnitude and direction, the process of multiplying a vector by a scalar, a constant, changes only the magnitude of the vector or the length of the line.
Scalar multiplication has no effect on the direction unless the scalar is negative, in which case the direction of the resulting vector is opposite the direction of the original vector. scalar multiplication Scalar multiplication involves the product of a vector and a scalar.
Each component of the vector is multiplied by the scalar.
Thus, to multiply v = 〈a, b〉 by k, we have

kv = 〈ka, kb〉 Only the magnitude changes, unless k is negative, and then the vector reverses direction.

---
### 📐 **Example 6**:
Performing Scalar Multiplication

Given vector v = 〈3, 1〉 , find 3v, 1/2 v, and -v.

**Solution**

See Figure 11 for a geometric interpretation.
If v = 〈3, 1〉, then

3v = 〈3 ⋅ 3, 3 ⋅ 1〉

 1/2 v = 〈 1/2 ⋅ 3, 1/2 ⋅ 1〉

= 〈 3 _ _ 2 〉

-v = 〈-3, -1〉 3v v –v v

**Analysis**
Notice that the vector 3v is three times the length of v, 1/2 v is half the length of v, and -v is the same length of v, but in the opposite direction.

---
### ✏️ **Try It #2**
Find the scalar multiple 3u given u = 〈5, 4〉 .

---
### 📐 **Example 7**
Using Vector Addition and Scalar Multiplication to Find a New Vector Given u = 〈3, - 2〉 and v = 〈-1, 4〉, find a new vector w = 3u + 2v.

**Solution**

First, we must multiply each vector by the scalar.

3u = 3 〈3, - 2〉

= 〈9, - 6〉

= 〈-2, 8〉 Then, add the two together.

w = 3u + 2v

= 〈9, - 6〉 + 〈-2, 8〉

= 〈9 - 2, - 6 + 8〉

So, w = 〈7, 2〉.
Finding Component Form In some applications involving vectors, it is helpful for us to be able to break a vector down into its components.
Vectors are comprised of two components: the horizontal component is the x direction, and the vertical component is the y direction.
For example, we can see in the graph in Figure 12 that the position vector 〈2, 3〉 comes from adding the vectors v¹ and v².
We have v¹ with initial point (0, 0) and terminal point (2, 0).

v¹ = 〈2 - 0, 0 - 0〉

We also have v² with initial point (0, 0) and terminal point (0, 3).

v² = 〈0 - 0, 3 - 0〉

Therefore, the position vector is

v = 〈2 + 0, 3 + 0〉

Using the Pythagorean Theorem, the magnitude of v¹ is 2, and the magnitude of v² is 3.
To find the magnitude of v, use the formula with the position vector.

| v | = √ ∣ v¹ ∣2 + ∣ v² ∣2

= √—

= √13 The magnitude of v is √13 . To find the direction, we use the tangent function tan θ = (y)/(x) .


> **tan θ = v² _ v¹**


> **tan θ = 3/2**


θ = tan-1 ( 3/x y 56.3° v¹ v² |v| Thus, the magnitude of v is √13 and the direction is 56.3° off the horizontal.

---
### 📐 **Example 8**
Finding the Components of the Vector Find the components of the vector v with initial point (3, 2) and terminal point (7, 4).

**Solution**

First find the standard position.

v = 〈7 - 3, 4 - 2〉

See the illustration in Figure 13. x y The horizontal component is v¹ = 〈4, 0〉 and the vertical component is v² = 〈0, 2〉.
Finding the Unit Vector in the Direction of v In addition to finding a vector’s components, it is also useful in solving problems to find a vector in the same direction as the given vector, but of magnitude 1.
We call a vector with a magnitude of 1 a unit vector.
We can then preserve the direction of the original vector while simplifying calculations.
Unit vectors are defined in terms of components.
The horizontal unit vector is written as i = 〈1, 0〉 and is directed along the positive horizontal axis.
The vertical unit vector is written as j = 〈0, 1〉 and is directed along the positive vertical axis.
See Figure 14. x y j = 〈0, 1〉 i = 〈1, 0〉

the unit vectors If v is a nonzero vector, then v _ ∣ v ∣ is a unit vector in the direction of v.
Any vector divided by its magnitude is a unit vector.
Notice that magnitude is always a scalar, and dividing by a scalar is the same as multiplying by the reciprocal of the scalar.

---
### 📐 **Example 9**
Finding the Unit Vector in the Direction of v Find a unit vector in the same direction as v = 〈-5, 12〉.

**Solution**

First, we will find the magnitude.

| v | = √(-5)² + (12)² 

= √—

= √169 

= 13 Then we divide each component by | v |, which gives a unit vector in the same direction as v:

 v _ | v | = - 5/13 i + 12/13 j or, in component form

 v _ | v | = 〈- 5 _ _ 13 〉 See Figure 15. x y - Verify that the magnitude of the unit vector equals 1.
The magnitude of - 5/13 i + 12/13 j is given as

√

( - 5 13 ) 2 + ( 12 13 ) 2 = √

 25 

= √

 169/169 

= 1 The vector u = 5 13 i + 12 13 j is the unit vector in the same direction as v = 〈-5, 12〉.
Performing Operations with Vectors in Terms of i and j So far, we have investigated the basics of vectors: magnitude and direction, vector addition and subtraction, scalar multiplication, the components of vectors, and the representation of vectors geometrically.
Now that we are familiar with the general strategies used in working with vectors, we will represent vectors in rectangular coordinates in terms of i and j.

vectors in the rectangular plane Given a vector v with initial point P = (x¹, y¹) and terminal point Q = (x², y²), v is written as v = (x² - x¹)i + (y¹ - y²) j The position vector from (0, 0) to (a, b), where (x² - x¹) = a and (y² - y¹) = b, is written as v = ai + bj.
This vector sum is called a linear combination of the vectors i and j.
The magnitude of v = ai + bj is given as | v | = √a² + b² .
See Figure 16. v = ai + bj bj ai

---
### 📐 **Example 10**:
Writing a Vector in Terms of i and j

Given a vector v with initial point P = (2, -6) and terminal point Q = (-6, 6), write the vector in terms of i and j.

**Solution**

Begin by writing the general form of the vector.
Then replace the coordinates with the given values.

v = (x² - x¹)i + (y² - y¹) j

= ( -6 - 2)i + (6 - ( - 6)) j

= - 8i + 12 j

---
### 📐 **Example 11**:
Writing a Vector in Terms of i and j Using Initial and Terminal Points

Given initial point P¹ = (-1, 3) and terminal point P² = (2, 7), write the vector v in terms of i and j.

**Solution**

Begin by writing the general form of the vector.
Then replace the coordinates with the given values.

v = (x² - x¹)i + (y² - y¹) j

v = (2 - ( - 1))i + (7 - 3) j

= 3i + 4 j

---
### ✏️ **Try It #3**
Write the vector u with initial point P = (-1, 6) and terminal point Q = (7, - 5) in terms of i and j.
Performing Operations on Vectors in Terms of i and j When vectors are written in terms of i and j, we can carry out addition, subtraction, and scalar multiplication by performing operations on corresponding components. adding and subtracting vectors in rectangular coordinates Given v = ai + bj and u = ci + dj, then

v + u = (a + c)i + (b + d)j

v - u = (a - c)i + (b - d)j

---
### 📐 **Example 12**
Finding the Sum of the Vectors Find the sum of v¹ = 2i - 3j and v² = 4i + 5j.

**Solution**

According to the formula, we have

v¹ + v² = (2 + 4)i + ( - 3 + 5) j

= 6i + 2 j Calculating the Component Form of a Vector:
Direction We have seen how to draw vectors according to their initial and terminal points and how to find the position vector.
We have also examined notation for vectors drawn specifically in the Cartesian coordinate plane using i and j.
For any of these vectors, we can calculate the magnitude.
Now, we want to combine the key points, and look further at the ideas of magnitude and direction.
Calculating direction follows the same straightforward process we used for polar coordinates.
We find the direction of the vector by finding the angle to the horizontal.
We do this by using the basic trigonometric identities, but with |v| replacing r. vector components in terms of magnitude and direction Given a position vector v = 〈x, y〉 and a direction angle θ ,


> **cos θ = x _ | v | and sin θ = y _ | v |**


x = | v | cos θ y = | v | sin θ Thus, v = xi + yj = |v|cos θ i + |v|sin θ j, and magnitude is expressed as |v| = √x² + y² .

---
### 📐 **Example 13**:
Writing a Vector in Terms of Magnitude and Direction

Write a vector with length 7 at an angle of 135° to the positive x-axis in terms of magnitude and direction.

**Solution**


Using the conversion formulas x = |v| cos θ i and y =|v| sin θ j, we find that


x = 7cos(135°)i

= - 7√2/2 

y = 7sin(135°) j

= 7√2/2 This vector can be written as v = 7cos(135°)i + 7sin(135°) j or simplified as

v = - 7√2/2 i + 7√2/2 j

---
### ✏️ **Try It #4**
A vector travels from the origin to the point (3, 5).
Write the vector in terms of magnitude and direction.
Finding the Dot Product of Two Vectors As we discussed earlier in the section, scalar multiplication involves multiplying a vector by a scalar, and the result is a vector.
As we have seen, multiplying a vector by a number is called scalar multiplication.
If we multiply a vector by a vector, there are two possibilities: the dot product and the cross product.
We will only examine the dot product here; you may encounter the cross product in more advanced mathematics courses.
The dot product of two vectors involves multiplying two vectors together, and the result is a scalar.

dot product The dot product of two vectors v = 〈a, b〉 and u = 〈c, d〉 is the sum of the product of the horizontal components and the product of the vertical components.

v ⋅ u = ac + bd To find the angle between the two vectors, use the formula below.


> **cos θ = v | v | ⋅ u | u |**


---
### 📐 **Example 14**
Finding the Dot Product of Two Vectors Find the dot product of v = 〈5, 12〉 and u = 〈-3, 4〉.

**Solution**

Using the formula, we have

v ⋅ u = 〈5, 12〉 ⋅ 〈-3, 4〉

= 5 ⋅ ( -3) + 12 ⋅ 4

= 33

---
### 📐 **Example 15**
Finding the Dot Product of Two Vectors and the Angle between Them Find the dot product of v¹ = 5i + 2j and v² = 3i + 7j.
Then, find the angle between the two vectors.

**Solution**

Finding the dot product, we multiply corresponding components.

v¹ ⋅ v² = 〈5, 2〉 ⋅ 〈3, 7〉

= 5 ⋅ 3 + 2 ⋅ 7

= 29 To find the angle between them, we use the formula cos θ = v _ | v | ⋅ u _ | u | 

 v _ | v | ⋅ u _ | u | = 〈 √29 + √29 〉 ⋅ 〈 √58 + √58 〉

= √29 ⋅ √58 + √29 ⋅ √58 

= √— + √— = √See Figure 17. x y 45°

---
### 📐 **Example 16**
Finding the Angle between Two Vectors Find the angle between u = 〈-3, 4〉 and v = 〈5, 12〉.

**Solution**

Using the formula, we have


> **θ = cos-1 ( u _ | u | ⋅ v _ | v | )**


( u _ ∣ u ∣ ⋅ v _ ∣ v ∣ ) = -3i + 4j _ ⋅ 5i + 12j _ 

= ( - 3/5 ⋅ 5/13 ) + ( 4/5 ⋅ 12/13 ) 

= - 15 _ _ 65 

= 33/65 


> **θ = cos-1( 33/65 )**


See Figure 18. x y 59.5°

---
### 📐 **Example 17**
Finding Ground Speed and Bearing Using Vectors We now have the tools to solve the problem we introduced in the opening of the section.
An airplane is flying at an airspeed of 200 miles per hour headed on a SE bearing of 140°.
A north wind (from north to south) is blowing at 16.2 miles per hour.
What are the ground speed and actual bearing of the plane?
See Figure 19.
N A O B X C 140 ̊ 16.2 α

**Solution**

The ground speed is represented by x in the diagram, and we need to find the angle α in order to calculate the adjusted bearing, which will be 140° + α .

Notice in Figure 19, that angle BCO must be equal to angle AOC by the rule of alternating interior angles, so angle BCO is 140°.
We can find x by the Law of Cosines:

x = √The ground speed is approximately 213 miles per hour.
Now we can calculate the bearing using the Law of Sines.


> **sin α/16.2 = sin(140°) _**


> **sin α = 16.2sin(140°) __ 212.7**


Therefore, the plane has a SE bearing of 140° + 2.8° = 142.8°.
The ground speed is 212.7 miles per hour.
Access these online resources for additional instruction and practice with vectors.
• Introduction to Vectors (http://openstaxcollege.org/l/introvectors) • Vector Operations (http://openstaxcollege.org/l/vectoroperation) • The Unit Vector (http://openstaxcollege.org/l/unitvector)

## 8.8 Section Exercises

---
### 8.8 Section Exercises

Verbal 1.
What are the characteristics of the letters that are commonly used to represent vectors? 2.
How is a vector more specific than a line segment? 3.
What are i and j, and what do they represent? 4.
What is component form? 5.
When a unit vector is expressed as 〈a, b〉, which letter is the coefficient of the i and which the j?
Algebraic 6.
Given a vector with initial point (5, 2) and terminal point (-1, - 3), find an equivalent vector whose initial point is (0, 0).
Write the vector in component form 〈a, b〉. 7.
Given a vector with initial point (-4, 2) and terminal point (3, - 3), find an equivalent vector whose initial point is (0, 0).
Write the vector in component form 〈a, b〉. 8.
Given a vector with initial point (7, - 1) and terminal point (-1, - 7), find an equivalent vector whose initial point is (0, 0).
Write the vector in component form 〈a, b〉.
For the following exercises, determine whether the two vectors u and v are equal, where u has an initial point P¹ and a terminal point P² and v has an initial point P³ and a terminal point P⁴.
P⁴ = (9, - 4) P⁴ = (-1, - 4) 14.
Given initial point P¹ = (-3, 1) and terminal point P² = (5, 2), write the vector v in terms of i and j. 15.
Given initial point P¹ = (6, 0) and terminal point P² = (-1, - 3), write the vector v in terms of i and j.
For the following exercises, use the vectors u = i + 5j, v = -2i - 3j, and w = 4i - j. 16.
Find u + (v - w) 17.
Find 4v + 2u For the following exercises, use the given vectors to compute u + v, u - v, and 2u - 3v. 18. u = 〈2, - 3〉 , v = 〈1, 5〉 19. u = 〈-3, 4〉 , v = 〈-2, 1〉 20.
Let v = -4i + 3j.
Find a vector that is half the length and points in the same direction as v. 21.
Let v = 5i + 2j.
Find a vector that is twice the length and points in the opposite direction as v.
For the following exercises, find a unit vector in the same direction as the given vector. 22. a = 3i + 4j 23. b = -2i + 5j 24. c = 10i - j 25. d = - 1/3 i + 5/2 j 27. u = -14i + 2j For the following exercises, find the magnitude and direction of the vector, 0 ≤ θ < 2π . 32.
Given u = 3i - 4j and v = -2i + 3j, calculate u ⋅ v. 33.
Given u = -i - j and v = i + 5j, calculate u ⋅ v. 34.
Given u = 〈-2, 4〉 and v = 〈-3, 1〉, calculate u ⋅ v. 35.
Given u = 〈-1, 6〉 and v = 〈6, - 1〉, calculate u ⋅ v.

Graphical For the following exercises, given v, draw v, 3v and 1/2 v.
For the following exercises, use the vectors shown to sketch u + v, u - v, and 2u. v u v u v u For the following exercises, use the vectors shown to sketch 2u + v. u v u v For the following exercises, use the vectors shown to sketch u - 3v. u v u v For the following exercises, write the vector shown in component form.

48. Given initial point P¹ = (2, 1) and terminal point P² = (-1, 2), write the vector v in terms of i and j, then draw the vector on the graph. 49. Given initial point P¹ = (4, - 1) and terminal point P² = (-3, 2), write the vector v in terms of i and j. Draw the points and the vector on the graph. 50. Given initial point P¹ = (3, 3) and terminal point P² = (-3, 3), write the vector v in terms of i and j. Draw the points and the vector on the graph. Extensions For the following exercises, use the given magnitude and direction in standard position, write the vector in component form. 51. | v | = 6, θ = 45 ° 52. | v | = 8, θ = 220° 53. | v | = 2, θ = 300° 54. | v | = 5, θ = 135° 55. A 60-pound box is resting on a ramp that is inclined 12°. Rounding to the nearest tenth, a. Find the magnitude of the normal (perpendicular) component of the force. b. Find the magnitude of the component of the force that is parallel to the ramp. 56. A 25-pound box is resting on a ramp that is inclined 8°. Rounding to the nearest tenth, a. Find the magnitude of the normal (perpendicular) component of the force. b. Find the magnitude of the component of the force that is parallel to the ramp. 57. Find the magnitude of the horizontal and vertical components of a vector with magnitude 8 pounds pointed in a direction of 27° above the horizontal. Round to the nearest hundredth. 58. Find the magnitude of the horizontal and vertical components of the vector with magnitude 4 pounds pointed in a direction of 127° above the horizontal. Round to the nearest hundredth. 59. Find the magnitude of the horizontal and vertical components of a vector with magnitude 5 pounds pointed in a direction of 55° above the horizontal. Round to the nearest hundredth. 60. Find the magnitude of the horizontal and vertical components of the vector with magnitude 1 pound pointed in a direction of 8° above the horizontal. Round to the nearest hundredth. Real-World Applications 61. A woman leaves home and walks 3 miles west, then 2 miles southwest. How far from home is she, and in what direction must she walk to head directly home? 62. A boat leaves the marina and sails 6 miles north, then 2 miles northeast. How far from the marina is the boat, and in what direction must it sail to head directly back to the marina? 63. A man starts walking from home and walks 4 miles east, 2 miles southeast, 5 miles south, 4 miles southwest, and 2 miles east. How far has he walked? If he walked straight home, how far would he have to walk? 64. A woman starts walking from home and walks 4 miles east, 7 miles southeast, 6 miles south, 5 miles southwest, and 3 miles east. How far has she walked? If she walked straight home, how far would she have to walk? 65. A man starts walking from home and walks 3 miles at 20° north of west, then 5 miles at 10° west of south, then 4 miles at 15° north of east. If he walked straight home, how far would he have to the walk, and in what direction? 66. A woman starts walking from home and walks 6 miles at 40° north of east, then 2 miles at 15° east of south, then 5 miles at 30° south of west. If she walked straight home, how far would she have to walk, and in what direction?

67. An airplane is heading north at an airspeed of 600 km/hr, but there is a wind blowing from the southwest at 80 km/hr. How many degrees off course will the plane end up flying, and what is the plane’s speed relative to the ground? 68. An airplane is heading north at an airspeed of 500 km/hr, but there is a wind blowing from the northwest at 50 km/hr. How many degrees off course will the plane end up flying, and what is the plane’s speed relative to the ground? 69. An airplane needs to head due north, but there is a wind blowing from the southwest at 60 km/hr. The plane flies with an airspeed of 550 km/hr. To end up flying due north, how many degrees west of north will the pilot need to fly the plane? 70. An airplane needs to head due north, but there is a wind blowing from the northwest at 80 km/hr. The plane flies with an airspeed of 500 km/hr. To end up flying due north, how many degrees west of north will the pilot need to fly the plane? 71. As part of a video game, the point (5, 7) is rotated counterclockwise about the origin through an angle of 35°. Find the new coordinates of this point. 72. As part of a video game, the point (7, 3) is rotated counterclockwise about the origin through an angle of 40°. Find the new coordinates of this point. 73. Two children are throwing a ball back and forth straight across the back seat of a car. The ball is being thrown 10 mph relative to the car, and the car is traveling 25 mph down the road. If one child doesn't catch the ball, and it flies out the window, in what direction does the ball fly (ignoring wind resistance)? 74. Two children are throwing a ball back and forth straight across the back seat of a car. The ball is being thrown 8 mph relative to the car, and the car is traveling 45 mph down the road. If one child doesn't catch the ball, and it flies out the window, in what direction does the ball fly (ignoring wind resistance)? 75. A 50-pound object rests on a ramp that is inclined 19°. Find the magnitude of the components of the force parallel to and perpendicular to (normal) the ramp to the nearest tenth of a pound. 76. Suppose a body has a force of 10 pounds acting on it to the right, 25 pounds acting on it upward, and 5 pounds acting on it 45° from the horizontal. What single force is the resultant force acting on the body? 77. Suppose a body has a force of 10 pounds acting on it to the right, 25 pounds acting on it -135° from the horizontal, and 5 pounds acting on it directed 150° from the horizontal. What single force is the resultant force acting on the body? 78. The condition of equilibrium is when the sum of the forces acting on a body is the zero vector. Suppose a body has a force of 2 pounds acting on it to the right, 5 pounds acting on it upward, and 3 pounds acting on it 45° from the horizontal. What single force is needed to produce a state of equilibrium on the body? 79. Suppose a body has a force of 3 pounds acting on it to the left, 4 pounds acting on it upward, and 2 pounds acting on it 30° from the horizontal. What single force is needed to produce a state of equilibrium on the body? Draw the vector.

### Key Terms

altitude a perpendicular line from one vertex of a triangle to the opposite side, or in the case of an obtuse triangle, to the line containing the opposite side, forming two right triangles ambiguous case a scenario in which more than one triangle is a valid solution for a given oblique SSA triangle Archimedes’ spiral a polar curve given by r = θ .
When multiplied by a constant, the equation appears as r = aθ .
As r = θ , the curve continues to widen in a spiral path over the domain. argument the angle associated with a complex number; the angle between the line from the origin to the point and the positive real axis cardioid a member of the limaçon family of curves, named for its resemblance to a heart; its equation is given as r = a ± bcos θ and r = a ± bsin θ , where (a)/(b) = 1 convex limaçon a type of one-loop limaçon represented by r = a ± bcos θ and r = a ± bsin θ such that (a)/(b) ≥ 2 De Moivre’s Theorem formula used to find the nth power or nth roots of a complex number; states that, for a positive integer n, z n is found by raising the modulus to the nth power and multiplying the angles by n dimpled limaçon a type of one-loop limaçon represented by r = a ± bcos θ and r = a ± bsin θ such that 1 < (a)/(b) < 2 dot product given two vectors, the sum of the product of the horizontal components and the product of the vertical components Generalized Pythagorean Theorem an extension of the Law of Cosines; relates the sides of an oblique triangle and is used for SAS and SSS triangles initial point the origin of a vector inner-loop limaçon a polar curve similar to the cardioid, but with an inner loop; passes through the pole twice; represented by r = a ± bcos θ and r = a ± bsin θ where a < b Law of Cosines states that the square of any side of a triangle is equal to the sum of the squares of the other two sides minus twice the product of the other two sides and the cosine of the included angle Law of Sines states that the ratio of the measurement of one angle of a triangle to the length of its opposite side is equal to the remaining two ratios of angle measure to opposite side; any pair of proportions may be used to solve for a missing angle or side lemniscate a polar curve resembling a figure 8 and given by the equation r 2 = a² cos 2θ and r 2 = a² sin 2θ , a ≠ 0 magnitude the length of a vector; may represent a quantity such as speed, and is calculated using the Pythagorean Theorem modulus the absolute value of a complex number, or the distance from the origin to the point (x, y); also called the amplitude oblique triangle any triangle that is not a right triangle one-loop limaçon a polar curve represented by r = a ± bcos θ and r = a ± bsin θ such that a > 0, b > 0, and (a)/(b) > 1; may be dimpled or convex; does not pass through the pole parameter a variable, often representing time, upon which x and y are both dependent polar axis on the polar grid, the equivalent of the positive x-axis on the rectangular grid polar coordinates on the polar grid, the coordinates of a point labeled (r, θ ), where θ indicates the angle of rotation from the polar axis and r represents the radius, or the distance of the point from the pole in the direction of θ polar equation an equation describing a curve on the polar grid polar form of a complex number a complex number expressed in terms of an angle θ and its distance from the origin r; can be found by using conversion formulas x = rcos θ , y = rsin θ , and r = √x² + y² pole the origin of the polar grid

resultant a vector that results from addition or subtraction of two vectors, or from scalar multiplication rose curve a polar equation resembling a flower, given by the equations r = acos nθ and r = asin nθ ; when n is even there are 2n petals, and the curve is highly symmetrical; when n is odd there are n petals. scalar a quantity associated with magnitude but not direction; a constant scalar multiplication the product of a constant and each component of a vector standard position the placement of a vector with the initial point at (0, 0) and the terminal point (a, b), represented by the change in the x-coordinates and the change in the y-coordinates of the original vector terminal point the end point of a vector, usually represented by an arrow indicating its direction unit vector a vector that begins at the origin and has magnitude of 1; the horizontal unit vector runs along the x-axis and is defined as v¹ = 〈1, 0〉 the vertical unit vector runs along the y-axis and is defined as v² = 〈0, 1〉. vector a quantity associated with both magnitude and direction, represented as a directed line segment with a starting point (initial point) and an end point (terminal point) vector addition the sum of two vectors, found by adding corresponding components Key Equations Law of Sines sin α a = sin β b = sin γ c (a)/(s)in α = (b)/(s)in β = (c)/(s)in γ Area for oblique triangles


Area = 1/2 bcsin α


> **= 1/2 acsin β**


= 1/2 absin γ Law of Cosines a² = b² + c² - 2bccos α b² = a² + c² - 2accos β c² = a² + b² - 2abcos γ Heron’s formula Area = √—

s(s - a)(s - b)(s - c) where s = (a + b + c) _ Conversion formulas cos θ = (x)/(r) → x = rcos θ sin θ = (y)/(r) → y = rsin θ r² = x² + y² tan θ = (y)/(x) 

### Key Concepts

• The Law of Sines can be used to solve oblique triangles, which are non-right triangles.
• According to the Law of Sines, the ratio of the measurement of one of the angles to the length of its opposite side equals the other two ratios of angle measure to opposite side.

• There are three possible cases:
ASA, AAS, SSA.
Depending on the information given, we can choose the appropriate equation to find the requested solution.
See Example 1.
• The ambiguous case arises when an oblique triangle can have different outcomes.
• There are three possible cases that arise from SSA arrangement—a single solution, two possible solutions, and no solution.
See Example 2 and Example 3. • The Law of Sines can be used to solve triangles with given criteria.
See Example 4. • The general area formula for triangles translates to oblique triangles by first finding the appropriate height value.
See

**Example 5** — .
• There are many trigonometric applications.
They can often be solved by first drawing a diagram of the given information and then using the appropriate equation.
See Example 6. 8.2 Non-right Triangles: Law of Cosines • The Law of Cosines defines the relationship among angle measurements and lengths of sides in oblique triangles.
• The Generalized Pythagorean Theorem is the Law of Cosines for two cases of oblique triangles: SAS and SSS.
Dropping an imaginary perpendicular splits the oblique triangle into two right triangles or forms one right triangle, which allows sides to be related and measurements to be calculated.
See Example 1 and Example 2.
• The Law of Cosines is useful for many types of applied problems.
The first step in solving such problems is generally to draw a sketch of the problem presented.
If the information given fits one of the three models (the three equations), then apply the Law of Cosines to find a solution.
See Example 3 and Example 4.
• Heron’s formula allows the calculation of area in oblique triangles.
All three sides must be known to apply Heron’s formula.
See Example 5 and See Example 6. 8.3 Polar Coordinates • The polar grid is represented as a series of concentric circles radiating out from the pole, or origin.
• To plot a point in the form (r, θ ), θ > 0, move in a counterclockwise direction from the polar axis by an angle of θ , and then extend a directed line segment from the pole the length of r in the direction of θ .
If θ is negative, move in a clockwise direction, and extend a directed line segment the length of r in the direction of θ .
See Example 1.
• If r is negative, extend the directed line segment in the opposite direction of θ .
See Example 2.
• To convert from polar coordinates to rectangular coordinates, use the formulas x = rcos θ and y = rsin θ .
See Example 3 and Example 4.
• To convert from rectangular coordinates to polar coordinates, use one or more of the formulas: cos θ = (x)/(r) , sin θ = (y)/(r) , tan θ = (y)/(x) , and r = √x² + y² .
See Example 5.
• Transforming equations between polar and rectangular forms means making the appropriate substitutions based on the available formulas, together with algebraic manipulations.
See Example 6, Example 7, and Example 8.
• Using the appropriate substitutions makes it possible to rewrite a polar equation as a rectangular equation, and then graph it in the rectangular plane.
See Example 9, Example 10, and Example 11. 8.4 Polar Coordinates: Graphs • It is easier to graph polar equations if we can test the equations for symmetry with respect to the line θ = π/2 , the polar axis, or the pole.
• There are three symmetry tests that indicate whether the graph of a polar equation will exhibit symmetry.
If an equation fails a symmetry test, the graph may or may not exhibit symmetry.
See Example 1.
• Polar equations may be graphed by making a table of values for θ and r.
• The maximum value of a polar equation is found by substituting the value θ that leads to the maximum value of the trigonometric expression.
• The zeros of a polar equation are found by setting r = 0 and solving for θ .
See Example 2.
• Some formulas that produce the graph of a circle in polar coordinates are given by r = acos θ and r = asin θ .
See

**Example 3** — .
• The formulas that produce the graphs of a cardioid are given by r = a ± bcos θ and r = a ± bsin θ , for a > 0, b > 0, and (a)/(b) = 1. See Example 4.

• The formulas that produce the graphs of a one-loop limaçon are given by r = a ± bcos θ and r = a ± bsin θ for 1 < (a)/(b) < 2. See Example 5. • The formulas that produce the graphs of an inner-loop limaçon are given by r = a ± bcos θ and r = a ± bsin θ for a > 0, b > 0, and a < b. See Example 6. • The formulas that produce the graphs of a lemniscates are given by r² = a² cos 2θ and r² = a² sin 2θ , where a ≠ 0. See Example 7. • The formulas that produce the graphs of rose curves are given by r = acos nθ and r = asin nθ , where a ≠ 0; if n is even, there are 2n petals, and if n is odd, there are n petals. See Example 8 and Example 9. • The formula that produces the graph of an Archimedes’ spiral is given by r = θ , θ ≥ 0. See Example 10. 8.5 Polar Form of Complex Numbers • Complex numbers in the form a + bi are plotted in the complex plane similar to the way rectangular coordinates are plotted in the rectangular plane. Label the x-axis as the real axis and the y-axis as the imaginary axis. See Example 1. • The absolute value of a complex number is the same as its magnitude. It is the distance from the origin to the point: ∣ z ∣ = √a² + b² . See Example 2 and Example 3. • To write complex numbers in polar form, we use the formulas x = rcos θ , y = rsin θ , and r = √x² + y² . Then, z = r(cos θ + isin θ ). See Example 4 and Example 5. • To convert from polar form to rectangular form, first evaluate the trigonometric functions. Then, multiply through by r. See Example 6 and Example 7. • To find the product of two complex numbers, multiply the two moduli and add the two angles. Evaluate the trigonometric functions, and multiply using the distributive property. See Example 8. • To find the quotient of two complex numbers in polar form, find the quotient of the two moduli and the difference of the two angles. See Example 9. • To find the power of a complex number zn, raise r to the power n, and multiply θ by n. See Example 10. • Finding the roots of a complex number is the same as raising a complex number to a power, but using a rational exponent. See Example 11. 8.6 Parametric Equations • Parameterizing a curve involves translating a rectangular equation in two variables, x and y, into two equations in three variables, x, y, and t. Often, more information is obtained from a set of parametric equations. See Example 1,

**Example 2** — , and Example 3.
• Sometimes equations are simpler to graph when written in rectangular form.
By eliminating t, an equation in x and y is the result. • To eliminate t, solve one of the equations for t, and substitute the expression into the second equation.
See

**Example 4** — , Example 5, Example 6, and Example 7.
• Finding the rectangular equation for a curve defined parametrically is basically the same as eliminating the parameter.
Solve for t in one of the equations, and substitute the expression into the second equation.
See Example 8.
• There are an infinite number of ways to choose a set of parametric equations for a curve defined as a rectangular equation.
• Find an expression for x such that the domain of the set of parametric equations remains the same as the original rectangular equation.
See Example 9.

• When there is a third variable, a third parameter on which x and y depend, parametric equations can be used.
• To graph parametric equations by plotting points, make a table with three columns labeled t, x(t), and y(t).
Choose values for t in increasing order.
Plot the last two columns for x and y.
See Example 1 and Example 2.
• When graphing a parametric curve by plotting points, note the associated t-values and show arrows on the graph indicating the orientation of the curve.
See Example 3 and Example 4.
• Parametric equations allow the direction or the orientation of the curve to be shown on the graph.
Equations that are not functions can be graphed and used in many applications involving motion.
See Example 5.
• Projectile motion depends on two parametric equations: x = (v⁰ cos θ )t and y = - 16t² + (v⁰ sin θ )t + h.
Initial velocity is symbolized as v⁰.
θ represents the initial angle of the object when thrown, and h represents the height at which the object is propelled. 8.8 Vectors • The position vector has its initial point at the origin.
See Example 1.
• If the position vector is the same for two vectors, they are equal.
See Example 2.
Vectors are defined by their magnitude and direction.
See Example 3.
• If two vectors have the same magnitude and direction, they are equal.
See Example 4.
• Vector addition and subtraction result in a new vector found by adding or subtracting corresponding elements.
See

**Example 5** — .
• Scalar multiplication is multiplying a vector by a constant.
Only the magnitude changes; the direction stays the same.
See Example 6 and Example 7. • Vectors are comprised of two components: the horizontal component along the positive x-axis, and the vertical component along the positive y-axis.
See Example 8.
• The unit vector in the same direction of any nonzero vector is found by dividing the vector by its magnitude.
• The magnitude of a vector in the rectangular coordinate system is ∣ v ∣ = √a² + b² .
See Example 9. • In the rectangular coordinate system, unit vectors may be represented in terms of i and j where i represents the horizontal component and j represents the vertical component.
Then, v = ai + bj is a scalar multiple of v by real numbers a and b.
See Example 10 and Example 11. • Adding and subtracting vectors in terms of i and j consists of adding or subtracting corresponding coefficients of i and corresponding coefficients of j.
See Example 12. • A vector v = ai + bj is written in terms of magnitude and direction as v = ∣ v ∣cos θ i + ∣ v ∣sin θ j.
See Example 13. • The dot product of two vectors is the product of the i terms plus the product of the j terms.
See Example 14. • We can use the dot product to find the angle between two vectors.
Example 15 and Example 16. • Dot products are useful for many types of physics applications.
See Example 17.

Non-right Triangles:
Law of Sines For the following exercises, assume α is opposite side a, β is opposite side b, and γ is opposite side c.
Solve each triangle, if possible.
Round each answer to the nearest tenth. 3.
Solve the triangle.

a c C 24° 36° 4.
Find the area of the triangle.

75° 5.
A pilot is flying over a straight highway.
He determines the angles of depression to two mileposts, 2.1 km apart, to be 25° and 49°, as shown in Figure 1.
Find the distance of the plane from point A and the elevation of the plane.

Non-right Triangles:
Law of Cosines 6.
Solve the triangle, rounding to the nearest tenth, assuming α is opposite side a, β is opposite side b, and γ is opposite side c: a = 4, b = 6, c = 8. 7.
Solve the triangle in Figure 2, rounding to the nearest tenth.

54° B C a 8.
Find the area of a triangle with sides of length 8.3, 6.6, and 9.1. 9.
To find the distance between two cities, a satellite calculates the distances and angle shown in Figure 3 (not to scale).
Find the distance between the cities.
Round answers to the nearest tenth.

1.8° A B

Polar Coordinates 10.
Plot the point with polar coordinates ( 3, π/6 ) . 11.
Plot the point with polar coordinates ( 5, - 2π 3 ) 12.
Convert ( 6, - 3π 4 ) to rectangular coordinates. 13.
Convert ( -2, 3π 2 ) to rectangular coordinates. 14.
Convert (7, -2) to polar coordinates. 15.
Convert (-9, -4) to polar coordinates.
For the following exercises, convert the given Cartesian equation to a polar equation. 18. x² + y² = - 2y For the following exercises, convert the given polar equation to a Cartesian equation. 19. r = 7cos θ 20. r = -2 

4cos θ + sin θ For the following exercises, convert to rectangular form and graph. 21.
θ = 3π 4 22. r = 5sec θ Polar Coordinates: Graphs For the following exercises, test each equation for symmetry. 23. r = 4 + 4sin θ 25.
Sketch a graph of the polar equation r = 1 - 5sin θ .
Label the axis intercepts. 26.
Sketch a graph of the polar equation r = 5sin(7θ ). 27.
Sketch a graph of the polar equation r = 3 - 3cos θ Polar Form of Complex Numbers For the following exercises, find the absolute value of each complex number.
Write the complex number in polar form. __ 2 - √3 2 i For the following exercises, convert the complex number from polar to rectangular form. 32. z = 5cis ( 5π 6 ) 33. z = 3cis(40°) For the following exercises, find the product z¹z² in polar form. 34. z¹ = 2cis(89°), z² = 5cis(23°) 35. z¹ = 10cis ( π/6 ) , z² = 6cis ( π/3 ) For the following exercises, find the quotient z¹ _ z² in polar form. 37. z¹ = 27cis ( 5π 3 ) , z² = 9cis ( π/3 ) For the following exercises, find the powers of each complex number in polar form. 38.
Find z⁴ when z = 2cis(70°) 39.
Find z² when z = 5cis ( 3π 4 ) For the following exercises, evaluate each root. 40.
Evaluate the cube root of z when z = 64cis(210°). 41.
Evaluate the square root of z when z = 25cis ( 3π 2 ) .
For the following exercises, plot the complex number in the complex plane.
Parametric Equations For the following exercises, eliminate the parameter t to rewrite the parametric equation as a Cartesian equation. 44. { x(t) = 3t - 1

y(t) = √— t 

 45. { x(t) = - cos t

y(t) = 2sin² t 

46. Parameterize (write a parametric equation for) each Cartesian equation by using x(t) = acos t and y(t) = bsin t for x²

 25 + y²

 47. Parameterize the line from (-2, 3) to (4, 7) so that the line is at (-2, 3) at t = 0 and (4, 7) at t = 1. Parametric Equations: Graphs For the following exercises, make a table of values for each set of parametric equations, graph the equations, and include an orientation; then write the Cartesian equation. 48. { x(t) = 3t²

y(t) = 2t - 1 49. { x(t) = e t

y(t) = -2e 5t 50. { x(t) = 3cos t

y(t) = 2sin t 51.
A ball is launched with an initial velocity of 80 feet per second at an angle of 40° to the horizontal.
The ball is released at a height of 4 feet above the ground. a.
Find the parametric equations to model the path of the ball. b.
Where is the ball after 3 seconds? c.
How long is the ball in the air?
Vectors For the following exercises, determine whether the two vectors, u and v, are equal, where u has an initial point P¹ and a terminal point P², and v has an initial point P³ and a terminal point P⁴.
P⁴ = (-8, 2) For the following exercises, use the vectors u = 2i - j, v = 4i - 3j, and w = -2i + 5j to evaluate the expression. 54. u - v 55. 2v - u + w For the following exercises, find a unit vector in the same direction as the given vector. 56. a = 8i - 6j 57. b = -3i - j For the following exercises, find the magnitude and direction of the vector.
For the following exercises, calculate u ⋅ v. 60. u = -2i + j and v = 3i + 7j 61. u = i + 4j and v = 4i + 3j 62.
Given v = 〈-3, 4〉 draw v, 2v, and 1/2 v. 63.
Given the vectors shown in Figure 4, sketch u + v, u - v and 3v. u v 64.
Given initial point P¹ = (3, 2) and terminal point P² = (-5, -1), write the vector v in terms of i and j.
Draw the points and the vector on the graph.

1. Assume α is opposite side a, β is opposite side b, and γ is opposite side c. Solve the triangle, if possible, and round each answer to the nearest tenth, given β = 68°, 2. Find the area of the triangle in Figure 1. Round each answer to the nearest tenth. 6.25 60° 3. A pilot flies in a straight path for 2 hours. He then makes a course correction, heading 15° to the right of his original course, and flies 1 hour in the new direction. If he maintains a constant speed of 575 miles per hour, how far is he from his starting position? 4. Convert (2, 2) to polar coordinates, and then plot the point. 5. Convert ( 2, π/3 ) to rectangular coordinates. 6. Convert the polar equation to a Cartesian equation: x² + y² = 5y. 7. Convert to rectangular form and graph: r = - 3csc θ . 8. Test the equation for symmetry: r = - 4sin (2θ ). 9. Graph r = 3 + 3cos θ . 10. Graph r = 3 - 5sin θ . 11. Find the absolute value of the complex number 12. Write the complex number in polar form: 4 + i. 13. Convert the complex number from polar to rectangular form: z = 5cis( 2π 3 ) . Given z¹ = 8cis(36°) and z² = 2cis(15°), evaluate each expression. 15. z¹ _ z² 

z¹ 18. Plot the complex number -5 - i in the complex plane. 19. Eliminate the parameter t to rewrite the following parametric equations as a Cartesian equation: { x(t) = t + 1

y(t) = 2t² 20. Parameterize (write a parametric equation for) the following Cartesian equation by using x(t) = acos t and y(t) = bsin t: x² 36 + y²

 21. Graph the set of parametric equations and find the Cartesian equation: { x(t) = -2sin t

y(t) = 5cos t 22.
A ball is launched with an initial velocity of 95 feet per second at an angle of 52° to the horizontal.
The ball is released at a height of 3.5 feet above the ground. a.
Find the parametric equations to model the path of the ball. b.
Where is the ball after 2 seconds? c.
How long is the ball in the air?
For the following exercises, use the vectors u = i -3j and v = 2i + 3j. 24.
Calculate u ∙ v. 25.
Find a unit vector in the same direction as v. 26.
Given vector v has an initial point P¹ = (2, 2) and terminal point P² = (-1, 0), write the vector v in terms of i and j.
On the graph, draw v, and - v.
