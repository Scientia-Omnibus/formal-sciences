# Analytic Geometry

## 10.4 Rotation of Axis

---
Learning Objectives
In this section, you will:
• Identify nondegenerate conic sections given their general form equations.
• Use rotation of axes formulas.
• Write equations of rotated conics in standard form.
• Identify conics without rotating axes.
10.4 Rotation of Axis As we have seen, conic sections are formed when a plane intersects two right circular cones aligned tip to tip and extending infinitely far in opposite directions, which we also call a cone. The way in which we slice the cone will determine the type of conic section formed at the intersection. A circle is formed by slicing a cone with a plane perpendicular to the axis of symmetry of the cone. An ellipse is formed by slicing a single cone with a slanted plane not perpendicular to the axis of symmetry. A parabola is formed by slicing the plane through the top or bottom of the double-cone, whereas a hyperbola is formed when the plane slices both the top and bottom of the cone. See Figure 1. Ellipses, circles, hyperbolas, and parabolas are sometimes called the nondegenerate conic sections, in contrast to the degenerate conic sections, which are shown in Figure 2. A degenerate conic results when a plane intersects the double cone and passes through the apex. Depending on the angle of the plane, three types of degenerate conic sections are possible: a point, a line, or two intersecting lines. Circle Hyperbola Parabola Ellipse Diagonal Slice Horizontal Slice Deep Vertical Slice Vertical Slice Intersecting Lines Single Line Single Point

### Identifying Nondegenerate Conics in General Form

In previous sections of this chapter, we have focused on the standard form equations for nondegenerate conic sections. In this section, we will shift our focus to the general form equation, which can be used for any conic. The general form is set equal to zero, and the terms and coefficients are given in a particular order, as shown below.

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 where A, B, and C are not all zero. We can use the values of the coefficients to identify which type conic is represented by a given equation. You may notice that the general form equation has an xy term that we have not seen in any of the standard form equations. As we will discuss later, the xy term rotates the conic whenever B is not equal to zero. Conic Sections Example ellipse 4x 2 + 9y 2 = 1 circle 4x 2 + 4y 2 = 1 hyperbola 4x 2 - 9y 2 = 1 parabola 4x 2 = 9y or 4y 2 = 9x one line 4x + 9y = 1 intersecting lines (x - 4) (y + 4)= 0 parallel lines (x - 4)(x - 9) = 0 a point 4x 2 + 4y 2 = 0 no graph 4x 2 + 4y 2 = - 1 general form of conic sections A conic section has the general form Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 where A, B, and C are not all zero. indicates that the conic has not been rotated. Conic Sections Example ellipse Ax 2 + Cy 2 + Dx + Ey + F = 0, A ≠  C and AC > 0 circle Ax 2 + Cy 2 + Dx + Ey + F = 0, A = C hyperbola Ax 2 - Cy 2 + Dx + Ey + F = 0 or - Ax 2 + Cy 2 + Dx + Ey + F = 0, where A and C are positive parabola Ax 2 + Dx + Ey + F = 0 or Cy 2 + Dx + Ey + F = 0

---
### 💡 **How To…**
Given the equation of a conic, identify the type of conic. 1. Rewrite the equation in the general form, Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0. 2. Identify the values of A and C from the general form. a. If A and C are nonzero, have the same sign, and are not equal to each other, then the graph may be an ellipse. b. If A and C are equal and nonzero and have the same sign, then the graph may be a circle.

c. If A and C are nonzero and have opposite signs, then the graph may be a hyperbola. d. If either A or C is zero, then the graph may be a parabola. If B = 0, the conic section will have a vertical and/or horizontal axes. If B does not equal 0, as shown below, the conic section is rotated. Notice the phrase “may be” in the definitions. That is because the equation may not represent a conic section at all, depending on the values of A, B, C, D, E, and F. For example, the degenerate case of a circle or an ellipse is a point: Ax 2 +By 2=0, when A and B have the same sign. The degenerate case of a hyperbola is two intersecting straight lines: Ax 2 +By 2=0, when A and B have opposite signs. On the other hand, the equation Ax 2 +By 2+1=0, when A and B are positive does not represent a graph at all, since there are no real ordered pairs which satisfy it.

---
### 📐 **Example  1**: Identifying a Conic from Its General Form

Identify the graph of each of the following nondegenerate conic sections. b. 9y 2 + 16x + 36y - 10 = 0 c. 3x 2 + 3y 2 - 2x - 6y - 4 = 0

**Solution**

a. Rewriting the general form, we have

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0

4x 2 + 0xy + (-9)y 2 + 36x + 36y + (-125) = 0 A = 4 and C = -9, so we observe that A and C have opposite signs. The graph of this equation is a hyperbola. b. Rewriting the general form, we have

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0

0x 2 + 0xy + 9y 2 + 16x + 36y + (-10) = 0 A = 0 and C = 9. We can determine that the equation is a parabola, since A is zero. c. Rewriting the general form, we have

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0

3x 2 + 0xy + 3y 2 + (-2)x + (-6)y + (-4) = 0 A = 3 and C = 3. Because A = C, the graph of this equation is a circle. d. Rewriting the general form, we have

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0

(-25)x 2 + 0xy + (-4)y 2 + 100x + 16y + 20 = 0 A = -25 and C = -4. Because AC > 0 and A ≠  C, the graph of this equation is an ellipse.

---
### ✏️ **Try It #1**
Identify the graph of each of the following nondegenerate conic sections. a. 16y 2 - x 2 + x - 4y - 9 = 0

Finding a New Representation of the Given Equation after Rotating through a Given Angle Until now, we have looked at equations of conic sections without an xy term, which aligns the graphs with the x- and y- axes. When we add an xy term, we are rotating the conic about the origin. If the x- and y-axes are rotated through an angle, say \theta , then every point on the plane may be thought of as having two representations: (x, y) on the Cartesian plane with the original x-axis and y-axis, and (x′, y′) on the new plane defined by the new, rotated axes, called the x′-axis and y′-axis. See Figure 3.

x 2 + y 2 - xy - 15 = 0 We will find the relationships between x and y on the Cartesian plane with x′ and y′ on the new rotated plane. See Figure 4. The original coordinate x- and y-axes have unit vectors i and j. The rotated coordinate axes have unit vectors i′ and j′. The angle \theta  is known as the angle of rotation. See Figure 5. We may write the new unit vectors in terms of the original ones.

i′ = cos \theta i + sin \theta  j

j′ = -sin \theta i + cos \theta  j x \theta  y x’ y’ \theta  cos \theta  cos \theta  sin \theta  -sin \theta  \theta  x' x y y' x y \theta  x' y' j' i' i j sin \theta  -sin \theta  cos \theta  cos \theta 

Consider a vector u in the new coordinate plane. It may be represented in terms of its coordinate axes.

u = x′ i′ + y′ j′

u = x′(i cos \theta  + j sin \theta ) + y′( - i sin \theta  + j cos \theta ) Substitute.

u = ix ' cos \theta  + jx ' sin \theta  - iy' sin \theta  + jy' cos \theta  Distribute.

u = ix ' cos \theta  - iy' sin \theta  + jx ' sin \theta  + jy' cos \theta  Apply commutative property.

u = (x ' cos \theta  - y' sin \theta )i + (x' sin \theta  + y' cos \theta ) j Factor by grouping. Because u = x′ i′ + y′ j′, we have representations of x and y in terms of the new coordinate system. x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta  equations of rotation If a point (x, y) on the Cartesian plane is represented on a new coordinate plane where the axes of rotation are formed by rotating an angle \theta  from the positive x-axis, then the coordinates of the point with respect to the new axes are (x′, y′). We can use the following equations of rotation to define the relationship between (x, y) and (x′, y′): x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta 

---
### 💡 **How To…**
Given the equation of a conic, find a new representation after rotating through an angle. 1. Find x and y where x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta . 2. Substitute the expression for x and y into in the given equation, then simplify. 3. Write the equations with x′ and y′ in standard form.

---
### 📐 **Example  2**
Finding a New Representation of an Equation after Rotating through a Given Angle Find a new representation of the equation 2x 2 - xy + 2y 2 - 30 = 0 after rotating through an angle of \theta  = 45°.

**Solution**

Find x and y, where x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta . Because \theta  = 45°,

x = x′ cos(45°) - y′ sin(45°)

x = x′ (  1 _ √2   )  - y′ (  1 _ √2   ) 

x =  x′ - y′ _ √2   and

y = x′ sin(45°) + y′ cos(45°)

y = x′ (  1 _ √2   )  + y′ (  1 _ √2   ) 

y =  x′ + y′ _ √2   Substitute x = x′ cos\theta  - y′ sin\theta  and y = x′ sin \theta  + y′ cos \theta  into 2x 2 - xy + 2y 2 - 30 = 0.

2 (  x′ - y′ _ √2   )   - (  x′ - y′ _ √2   )  (  x′ + y′ _ √2   )  + 2 (  x′ + y′ _ √2   )   - 30 = 0

Simplify.

/ / 2  (x′ - y′)(x′ - y′)

__ / 2

 -  (x′ - y′)(x′ + y′)

__  + / 2  (x′ + y′)(x′ + y′)

__ / 2

 - 30 = 0 FOIL method

x′ 2 -2x′ y′ + y′ 2 -  (x′ 2 - y′ 2) _  + x′ 2 + 2x′ y′ + y′ 2 - 30 = 0 Combine like terms.

2x′ 2 + 2y′ 2 -  (x′ 2 - y′ 2) _  = 30 Combine like terms.

2( 2x′ 2 + 2y′ 2 -  (x′ 2 - y′ 2) _  )  = 2(30) Multiply both sides by 2.

4x′ 2 + 4y′ 2 - (x′ 2 - y′ 2) = 60 Simplify.

4x′ 2 + 4y′ 2 - x′ 2 + y′ 2 = 60 Distribute.

 3x′ 2/60  +  5y′ 2/60  =  60/60  Set equal to 1. Write the equations with x′ and y′ in the standard form.

 x′ 2/20  +  y′ 2/This equation is an ellipse. Figure 6 shows the graph. Writing Equations of Rotated Conics in Standard Form Now that we can find the standard form of a conic when we are given an angle of rotation, we will learn how to transform the equation of a conic given in the form Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0. into standard form by rotating the axes. To do so, we will rewrite the general form as an equation in the x′ and y′ coordinate system without the x′y′ term, by rotating the axes by a measure of \theta  that satisfies cot(2\theta ) =  A - C ______ B  We have learned already that any conic may be represented by the second degree equation

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0. where A, B, and C are not all zero. However, if B ≠  0, then we have an xy term that prevents us from rewriting the equation in standard form. To eliminate it, we can rotate the axes by an acute angle \theta  where cot(2\theta ) =  A - C ______ B . • If cot(2\theta ) > 0, then 2\theta  is in the first quadrant, and \theta  is between (0°, 45°). • If cot(2\theta ) < 0, then 2\theta  is in the second quadrant, and \theta  is between (45°, 90°). • If A = C, then \theta  = 45°.

---
### 💡 **How To…**
Given an equation for a conic in the x′ y′ system, rewrite the equation without the x′ y′ term in terms of x′ and y′, where the x′ and y′ axes are rotations of the standard axes by \theta  degrees. \theta  = 45° x x’ y’

1. Find cot(2\theta ). 2. Find sin \theta  and cos \theta . 3. Substitute sin \theta  and cos \theta  into x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta . 4. Substitute the expression for x and y into in the given equation, and then simplify. 5. Write the equations with x′ and y′ in the standard form with respect to the rotated axes.

---
### 📐 **Example  3**
Rewriting an Equation with respect to the x ́ and y ́ axes without the x ́y ́ Term Rewrite the equation 8x 2 - 12xy + 17y 2 = 20 in the x′ y′ system without an x′ y′ term.

**Solution**

First, we find cot(2\theta ). See Figure 7.

8x 2 - 12xy + 17y 2 = 20 ⇒ A = 8, B = - 12 and C = 17

cot(2\theta ) =  A - C ______ B  =  8 - 17 ______ -12 

cot(2\theta ) =  -9 ____ -12  =  3/4 

cot(2\theta ) =  3/4  =  adjacen(t)/(o)pposite  So the hypotenuse is

h = 5 Next, we find sin \theta  and cos \theta .

sin \theta  = √___________  1 - cos(2\theta ) __________   = √1 -  3/5  _   = √5 __ 5  -  3/5  _  = √_________  5 - 3 _____  ⋅ 1/2   = √___

 2/10   = √__

 1/5  

sin \theta  =  1 _ √5  

cos \theta  = √___________  1 + cos(2\theta ) __________   = √1 +  3/5  _   = √5 __ 5  +  3/5  _  = √_________  5 + 3 _____  ⋅ 1/2   = √___

 8/10   = √__

 4/5  

cos \theta  =  2 _ √5   Substitute the values of sin \theta  and cos \theta  into x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta .

x = x′ cos \theta  - y′ sin \theta 

x = x′ (  2 _ √5   )  - y′ (  1 _ √5   ) 

x =  2x′ - y′ _ √5   and

y = x′ sin \theta  + y′ cos \theta  2\theta  h x y

y = x′ (  1 _ √5   )  + y′ (  2 _ √5   ) 

y =  x′ + 2y′ _ √5   Substitute the expressions for x and y into in the given equation, and then simplify.

8(  2x′ - y′ _ √5   )   - 12 (  2x′ - y′ _ √5   )  (  x′ + 2y′ _ √5   )  + 17(  x′ + 2y′ _ √5   )   = 20

8(  (2x′ - y′)(2x′ - y′)

__  )  - 12(  (2x′ - y′)(x′ + 2y′)

__  )  + 17(  (x′ + 2y′)(x′ + 2y′)

__  )  = 20

8 (4x′ 2 - 4x′ y′ + y′ 2) - 12(2x′ 2 + 3x′ y′ - 2y′ 2) + 17(x′ 2 + 4x′ y′ + 4y′ 2) = 100

32x′ 2 - 32x′ y′ + 8y′ 2 - 24x′ 2 - 36x′ y′ + 24y′ 2 + 17x′ 2 + 68x′ y′ + 68y′ 2 = 100

 25 ____ ___ ___ 100  Write the equations with x′ and y′ in the standard form with respect to the new coordinate system.  x′ 2/4  +  y′ 2/1  = 1

---
### ✏️ **Try It #2**
Rewrite the 13x 2 - 6√3 xy + 7y 2 = 16 in the x′ y′ system without the x′ y′ term.

---
### 📐 **Example  4**: Graphing an Equation That Has No x ́y ́ Terms

Graph the following equation relative to the x′ y′ system:

x 2 + 12xy - 4y 2 = 30

**Solution**

First, we find cot(2\theta ).

x 2 + 12xy - 4y 2 = 20 ⇒ A = 1, B = 12, and C = -4

cot(2\theta ) =  A - C ______ B 

cot(2\theta ) =  1 - (-4) ________ 

cot(2\theta ) =  5 ___ 12  x y

Because cot(2\theta ) =  5/12 , we can draw a reference triangle as in Figure 9.

cot(2\theta ) =  5 ___ 12  =  adjacen(t)/(o)pposite  Thus, the hypotenuse is

h = 13 Next, we find sin \theta  and cos \theta . We will use half-angle identities.

sin \theta  = √___________  1 - cos(2\theta ) __________   = √1 -  5/13  _   = √13 _ 13  -  5/13  _   = √______

 8 _____ 13  ⋅ 1/2   =  2 _ √13  

cos \theta  = √___________  1 + cos(2\theta ) __________   = √1 +  5/13  _   = √13 _ 13  +  5/13  _   = √______

 18 ___ 13  ⋅ 1/2   =  3 _ √13   Now we find x and y.

x = x′ cos \theta  - y′ sin \theta 

x = x′ (  3 _ √13   )  - y′ (  2 _ √13   ) 

x =  3x′ - 2y′ _ √13   and

y = x′ sin \theta  + y′ cos \theta 

y = x′ (  2 _ √13   )  + y′ (  3 _ √13   ) 

y =  2x′ + 3y′ _ √13   Now we substitute x =  3x′ - 2y′ _ √13   and y =  2x′ + 3y′ _ √13   into x 2 + 12xy - 4y 2 = 30.

(  3x′ - 2y′ _ √13   )   + 12 (  3x′ - 2y′ _ √13   )(  2x′ + 3y′ _ √13   ) - 4(  2x′ + 3y′ _ √13   )   = 30 cot(2\theta ) = 12 x y 2\theta 

(  1 ___ 13  ) [(3x′ - 2y′ )² + 12(3x′ - 2y′ )(2x′ + 3y′ ) - 4 (2x′ + 3y′ )²] = 30 Factor.

(  1 ___ 13  ) [9x′ 2 - 12x′ y′ + 4y′ 2 + 12 (6x′ 2 + 5x′ y′ - 6y′ 2) - 4 (4x′ 2 + 12x′ y′ + 9y′ 2)] = 30 Multiply.

(  1 ___ 13  ) [9x′ 2 - 12x′ y′ + 4y′ 2 + 72x′ 2 + 60x′ y′ - 72y′ 2 - 16x′ 2 - 48x′ y′ - 36y′ 2] = 30 Distribute.

(  1 ___ Combine like terms.

Multiply.

 x′ 2/6  -  4y′ 2/15  = 1 Divide by 390. _ 6  -  4y′ 2/Identifying Conics without Rotating Axes Now we have come full circle. How do we identify the type of conic described by an equation? What happens when the axes are rotated? Recall, the general form of a conic is

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 If we apply the rotation formulas to this equation we get the form

A′ x′ 2 + B′x′y′ + C′y′ 2 + D′x′ + E′y′ + F′ = 0 It may be shown that B² - 4AC = B′ 2 - 4A′ C′. The expression does not vary after rotation, so we call the expression invariant. The discriminant, B² - 4AC, is invariant and remains unchanged after rotation. Because the discriminant remains unchanged, observing the discriminant enables us to identify the conic section. using the discriminant to identify a conic If the equation Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 is transformed by rotating axes into the equation A′x′ 2 + B′x′y′ + C′y′ 2 + D′x′ + E′y′ + F′ = 0, then B² - 4AC = B′ 2 - 4A′C′. The equation Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 is an ellipse, a parabola, or a hyperbola, or a degenerate case of one of these. If the discriminant, B² - 4AC, is • < 0, the conic section is an ellipse • = 0, the conic section is a parabola • > 0, the conic section is a hyperbola y’ x’ y x

---
### 📐 **Example  5**: Identifying the Conic without Rotating Axes

Identify the conic for each of the following without rotating axes. a. 5x 2 + 2√3 xy + 2y 2 - 5 = 0 b. 5x 2 + 2√3 xy + 12y 2 - 5 = 0

**Solution**

a. Let’s begin by determining A, B, and C.

 5 A x 2 +  2√3 

B xy +  2 C y 2 - 5 = 0 Now, we find the discriminant.

B² - 4AC = ( 2√3  ) 2 - 4(5)(2)

= - 28 < 0 Therefore, 5x 2 + 2√3 xy + 2y 2 - 5 = 0 represents an ellipse. b. Again, let’s begin by determining A, B, and .

 5 A x 2 +  2√3 

B xy +  12 C y 2 - 5 = 0 Now, we find the discriminant.

B² - 4AC = ( 2√3  )

Therefore, 5x 2 + 2√3 xy + 12y 2 - 5 = 0 represents an ellipse.

---
### ✏️ **Try It #3**
Identify the conic for each of the following without rotating axes. a. x 2 - 9xy + 3y 2 - 12 = 0 b. 10x 2 - 9xy + 4y 2 - 4 = 0 > Access this online resource for additional instruction and practice with conic sections and rotation of axes. • Introduction to Conic Sections (http://openstaxcollege.org/l/introconic) { { { {

### 10.4 Section Exercises

Verbal 1. What effect does the xy term have on the graph of a conic section? 2. If the equation of a conic section is written in the form Ax 2 + By 2 + Cx + Dy + E = 0 and AB = 0, what can we conclude? 3. If the equation of a conic section is written in the form Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0, and B² - 4AC > 0, what can we conclude? 4. Given the equation ax 2 + 4x + 3y 2 - 12 = 0, what can we conclude if a > 0? 5. For the equation Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0, the value of \theta  that satisfies cot(2\theta ) =  A - C ______ B  gives us what information? Algebraic For the following exercises, determine which conic section is represented based on the given equation. 7. x 2 - 10x + 4y - 10 = 0 8. 2x 2 - 2y 2 + 4x - 6y - 2 = 0 9. 4x 2 - y 2 + 8x - 1 = 0 10. 4y 2 - 5x + 9y + 1 = 0 3 xy - 4y 2 + 9 = 0 3 xy + 6y 2 - 6x - 3 = 0 16. -x 2 + 4√2 xy + 2y 2 - 2y + 1 = 0 2 xy + 4y 2 - 10x + 1 = 0 For the following exercises, find a new representation of the given equation after rotating through the given angle. 18. 3x 2 + xy + 3y 2 - 5 = 0, \theta  = 45° 19. 4x 2 - xy + 4y 2 - 2 = 0, \theta  = 45° 21. -2x 2 + 8xy + 1 = 0, \theta  = 45° 2 xy + 4y 2 + y + 2 = 0, \theta  = 45° For the following exercises, determine the angle \theta  that will eliminate the xy term and write the corresponding equation without the xy term. 3 xy + 4y 2 + y - 2 = 0 3 xy + 6y 2 + y - 2 = 0 3 xy + 6y 2 + 4y - 3 = 0 26. -3x 2 - √3 xy - 2y 2 - x = 0 27. 16x 2 + 24xy + 9y 2 + 6x - 6y + 2 = 0 28. x 2 + 4xy + 4y 2 + 3x - 2 = 0 29. x 2 + 4xy + y 2 - 2x + 1 = 0 3 xy + 6y 2 - 1 = 0 Graphical For the following exercises, rotate through the given angle based on the given equation. Give the new equation and graph the original and rotated equation. 31. y = - x 2, \theta  = - 45° 32. x = y 2, \theta  = 45°

_ 4  +  y 2/1  = 1, \theta  = 45°

_ 16  +  x 2/9  = 1, \theta  = 45° 35. y 2 - x 2 = 1, \theta  = 45° 36. y =  x 2/2  , \theta  = 30° 37. x = (y - 1)², \theta  = 30°

_ 9  +  y 2/4  = 1, \theta  = 30°

## 10.4 Section Exercises

---
For the following exercises, graph the equation relative to the x′ y′ system in which the equation has no x′ y′ term. 40. x 2 + 10xy + y 2 - 6 = 0 41. x 2 - 10xy + y 2 - 24 = 0 3 xy + y 2 - 22 = 0 3 xy + 4y 2 - 21 = 0 3 xy + y 2 - 64 = 0 3 xy + 19y 2 - 18 = 0 3 xy + 7y 2 - 16 = 0 49. 4x 2 - 4xy + y 2 - 8√5 x - 16√5 y = 0 For the following exercises, determine the angle of rotation in order to eliminate the xy term. Then graph the new set of axes. 3 xy + y 2 + 10x - 12y = 0 51. 6x 2 - 5xy + 6y 2 + 20x - y = 0 3 xy + 14y 2 + 10x - 3y = 0 3 xy + 10y 2 + 20x - 40y = 0 54. 8x 2 + 3xy + 4y 2 + 2x - 4 = 0 For the following exercises, determine the value of k based on the given equation. 56. Given 4x 2 + kxy + 16y 2 + 8x + 24y - 48 = 0, find k for the graph to be a parabola. 57. Given 2x 2 + kxy + 12y 2 + 10x - 16y + 28 = 0, find k for the graph to be an ellipse. 58. Given 3x 2 + kxy + 4y 2 - 6x + 20y + 128 = 0, find k for the graph to be a hyperbola. 59. Given kx 2 + 8xy + 8y 2 - 12x + 16y + 18 = 0, find k for the graph to be a parabola. 60. Given 6x 2 + 12xy + ky 2 + 16x + 10y + 4 = 0, find k for the graph to be an ellipse.

Learning Objectives
In this section, you will:
• Identify a conic in polar form.
• Graph the polar equations of conics.
• Define conics in terms of a focus and a directrix.
Conic Sections in Polar Coordinates Most of us are familiar with orbital motion, such as the motion of a planet around the sun or an electron around an atomic nucleus. Within the planetary system, orbits of planets, asteroids, and comets around a larger celestial body are often elliptical. Comets, however, may take on a parabolic or hyperbolic orbit instead. And, in reality, the characteristics of the planets’ orbits may vary over time. Each orbit is tied to the location of the celestial body being orbited and the distance and direction of the planet or other object from that body. As a result, we tend to use polar coordinates to represent these orbits. In an elliptical orbit, the periapsis is the point at which the two objects are closest, and the apoapsis is the point at which they are farthest apart. Generally, the velocity of the orbiting body tends to increase as it approaches the periapsis and decrease as it approaches the apoapsis. Some objects reach an escape velocity, which results in an infinite orbit. These bodies exhibit either a parabolic or a hyperbolic orbit about a body; the orbiting body breaks free of the celestial body’s gravitational pull and fires off into space. Each of these orbits can be modeled by a conic section in the polar coordinate system. Identifying a Conic in Polar Form Any conic may be determined by three characteristics: a single focus, a fixed line called the directrix, and the ratio of the distances of each to a point on the graph. Consider the parabola x = 2 + y 2 shown in Figure 2. Polar axis x = 2 + y² F, Focus @ pole r D P(r, \theta ) Directrix \theta 

## 10.5 Conic Sections in Polar Coordinates

---
In The Parabola, we learned how a parabola is defined by the focus (a fixed point) and the directrix (a fixed line). In this section, we will learn how to define any conic in the polar coordinate system in terms of a fixed point, the focus P(r, \theta ) at the pole, and a line, the directrix, which is perpendicular to the polar axis. If F is a fixed point, the focus, and D is a fixed line, the directrix, then we can let e be a fixed positive number, called the eccentricity, which we can define as the ratio of the distances from a point on the graph to the focus and the point on the graph to the directrix. Then the set of all points P such that e =  PF ___ PD  is a conic. In other words, we can define a conic as the set of all points P with the property that the ratio of the distance from P to F to the distance from P to D is equal to the constant e. For a conic with eccentricity e, • if 0 ≤  e < 1, the conic is an ellipse • if e = 1, the conic is a parabola • if e > 1, the conic is an hyperbola With this definition, we may now define a conic in terms of the directrix, x = ±  p, the eccentricity e, and the angle \theta . Thus, each conic may be written as a polar equation, an equation written in terms of r and \theta . the polar equation for a conic For a conic with a focus at the origin, if the directrix is x = ±  p, where p is a positive real number, and the eccentricity is a positive real number e, the conic has a polar equation

r =  ep/1 ±  e cos \theta   For a conic with a focus at the origin, if the directrix is y = ±  p, where p is a positive real number, and the eccentricity is a positive real number e, the conic has a polar equation

r =  ep/1 ±  e sin \theta  

---
### 💡 **How To…**
Given the polar equation for a conic, identify the type of conic, the directrix, and the eccentricity. 1. Multiply the numerator and denominator by the reciprocal of the constant in the denominator to rewrite the equation in standard form. 2. Identify the eccentricity e as the coefficient of the trigonometric function in the denominator. 3. Compare e with 1 to determine the shape of the conic. 4. Determine the directrix as x = p if cosine is in the denominator and y = p if sine is in the denominator. Set ep equal to the numerator in standard form to solve for x or y.

---
### 📐 **Example  1**: Identifying a Conic Given the Polar Form

For each of the following equations, identify the conic with focus at the origin, the directrix, and the eccentricity. a. r =  _________ 3 + 2 sin \theta   b. r =  _________ 4 + 5 cos \theta   c. r =  _________ 2 - 2 sin \theta

**Solution**

For each of the three conics, we will rewrite the equation in standard form. Standard form has a 1 as the constant in the denominator. Therefore, in all three parts, the first step will be to multiply the numerator and denominator by the reciprocal of the constant of the original equation,  1/c , where c is that constant. a. Multiply the numerator and denominator by  1/3 . r =  _________ 3 + 2sin \theta   ⋅  (  1/3  ) _ (  1/3  )  =  6(  1/3  )

__

3(  1/3  ) + 2(  1/3  ) sin \theta   =  __

1 +  2/3  sin \theta  

Because sin \theta  is in the denominator, the directrix is y = p. Comparing to standard form, note that e =  2/3 . Therefore, from the numerator,

2 = ep

2 = 2/3 p

(  3/2  ) 2 = (  3/2  )  2/3  p

3 = p Since e < 1, the conic is an ellipse. The eccentricity is e =  2/3  and the directrix is y = 3. b. Multiply the numerator and denominator by  1/4 .

r =  _ 4 + 5 cos \theta   ⋅  (  1/4  )  _ (  1/4  )  

r =  _ 4  ) 

__

4(  1/4  )  + 5(  1/4  )  cos \theta  

r =  _ 1 +  5/4  cos \theta   Because cos \theta  is in the denominator, the directrix is x = p. Comparing to standard form, e =  5/4 . Therefore, from the numerator,

3 = ep

3 =  5/4  p

(  4/5  ) 3 = (  4/5  )  5/4  p

 12 ___ 5  = p Since e > 1, the conic is a hyperbola. The eccentricity is e =  5/4  and the directrix is x =  12 ___ c. Multiply the numerator and denominator by  1/2 .

r =  _ 2 - 2 sin \theta   ⋅  (  1/2  )  _ (  1/2  )  

r =  7(  1/2  ) 

__

2(  1/2  )  - 2(  1/2  )  sin \theta  

r =   7/2  _ 1 - sin \theta   Because sine is in the denominator, the directrix is y = -p. Comparing to standard form, e = 1. Therefore, from the numerator,

 7/2  = ep

 7/2  = (1)p

 7/2  = p Because e = 1, the conic is a parabola. The eccentricity is e = 1 and the directrix is y = - 7

---
### ✏️ **Try It #1**
Identify the conic with focus at the origin, the directrix, and the eccentricity for r =  ________ 3 - cos \theta  . Graphing the Polar Equations of Conics When graphing in Cartesian coordinates, each conic section has a unique equation. This is not the case when graphing in polar coordinates. We must use the eccentricity of a conic section to determine which type of curve to graph, and then determine its specific characteristics. The first step is to rewrite the conic in standard form as we have done in the previous example. In other words, we need to rewrite the equation so that the denominator begins with 1. This enables us to determine e and, therefore, the shape of the curve. The next step is to substitute values for \theta  and solve for r to plot a few key points. Setting \theta  equal to 0,  π/2 , π , and  3π  ___ 2  provides the vertices so we can create a rough sketch of the graph.

---
### 📐 **Example  2**: Graphing a Parabola in Polar Form

Graph r =  _________ 3 + 3 cos \theta  .

**Solution**

First, we rewrite the conic in standard form by multiplying the numerator and denominator by the reciprocal of 3, which is  1/3 .

r =  _ 3 + 3 cos \theta   =  5(  1/3  ) 

__

3(  1/3  )  + 3(  1/3  )  cos \theta  

r =   5/3  _ 1 + cos \theta   Because e = 1, we will graph a parabola with a focus at the origin. The function has a cos \theta , and there is an addition sign in the denominator, so the directrix is x = p.

 5/3  = ep

 5/3  = (1)p

 5/3  = p The directrix is x =  5/3 . Plotting a few key points as in Table 1 will enable us to see the vertices. See Figure 3. A B C D \theta   π/2  π   3π  ___ 2  r =  _________ 3 + 3 cos \theta    5  5 undefined  5 A Directrix B F D r x = 5

Analysis We can check our result with a graphing utility. See Figure 4.

---
### 📐 **Example  3**: Graphing a Hyperbola in Polar Form

Graph r =  _________ 2 - 3 sin \theta  .

**Solution**

First, we rewrite the conic in standard form by multiplying the numerator and denominator by the reciprocal of 2, which is  1/2 .

r =  _ 2 - 3 sin \theta   =  8(  1/2  ) 

__

2(  1/2  )  - 3(  1/2  )  sin \theta  

r =  _ 1 -  3/2  cos \theta   Because e =  3/2 , e > 1, so we will graph a hyperbola with a focus at the origin. The function has a sin \theta  term and there is a subtraction sign in the denominator, so the directrix is y = -p.

4 = ep

4 = (  3/2  ) p

4(  2/3  )  = p

 8/3  = p The directrix is y = - 8/3 . Plotting a few key points as in Table 2 will enable us to see the vertices. See Figure 5. A B C D \theta   π/2  π   3π  ___ 2  r =  _________ 2 - 3 sin \theta   -8  8/A C D B r

---
### 📐 **Example  4**: Graphing an Ellipse in Polar Form

Graph r =  __________ 5 - 4 cos \theta .

**Solution**

First, we rewrite the conic in standard form by multiplying the numerator and denominator by the reciprocal of 5, which is  1/5 .

r =  _________ 5 - 4 cos \theta   =  _ 5  ) 

__

5(  1/5  )  - 4(  1/5  )  cos \theta  

r =  _ 1 -  4/5  sin \theta   Because e =  4/5 , e < 1, so we will graph an ellipse with a focus at the origin. The function has a cos \theta , and there is a subtraction sign in the denominator, so the directrix is x = -p.

2 = ep

2 = (  4/5  ) p

2(  5/4  )  = p

 5/2  = p The directrix is x = - 5/2 . Plotting a few key points as in Table 3 will enable us to see the vertices. See Figure 6. A B C D \theta   π/2  π   3π  ___ 2  r =  _________ 5 - 4 cos \theta    10 ___ D C B A r x = -5 Directrix

**Analysis**
We can check our result with a graphing utility. See Figure 7. _ 5 - 4 cos \theta   graphed on a viewing window of [-3, 12, 1] by [ -4, 4, 1], \theta  min = 0 and \theta  max = 2π .

---
### ✏️ **Try It #2**
Graph r =  _________ 4 - cos \theta .  Defining Conics in Terms of a Focus and a Directrix So far we have been using polar equations of conics to describe and graph the curve. Now we will work in reverse; we will use information about the origin, eccentricity, and directrix to determine the polar equation.

---
### 💡 **How To…**
Given the focus, eccentricity, and directrix of a conic, determine the polar equation. 1. Determine whether the directrix is horizontal or vertical. If the directrix is given in terms of y, we use the general polar form in terms of sine. If the directrix is given in terms of x, we use the general polar form in terms of cosine. 2. Determine the sign in the denominator. If p < 0, use subtraction. If p > 0, use addition. 3. Write the coefficient of the trigonometric function as the given eccentricity. 4. Write the absolute value of p in the numerator, and simplify the equation.

**Example  5** — Finding the Polar Form of a Vertical Conic Given a Focus at the Origin and the Eccentricity and Directrix
Find the polar form of the conic given a focus at the origin, e = 3 and directrix y = - 2.

**Solution**

The directrix is y = -p, so we know the trigonometric function in the denominator is sine. Because y = -2, -2 < 0, so we know there is a subtraction sign in the denominator. We use the standard form of

r =  ep ________ 1 - esin \theta   and e = 3 and | -2 | = 2 = p. Therefore,

r =  (3)(2) _________ 1 - 3 sin \theta  

r =  _________ 1 - 3 sin \theta  

---
### 📐 **Example  6**
Finding the Polar Form of a Horizontal Conic Given a Focus at the Origin and the Eccentricity and Directrix Find the polar form of a conic given a focus at the origin, e =  3/5 , and directrix x = 4.

**Solution**

Because the directrix is x = p, we know the function in the denominator is cosine. Because x = 4, 4 > 0, so we know there is an addition sign in the denominator. We use the standard form of

r =  ep _________ 1 + e cos \theta   and e =  3/5  and |4| = 4 = p.

Therefore,

r =  (  3/5  ) (4) ___________ 1 +  3/5  cos \theta  

r =   12/5  ___________ 1 +  3/5  cos \theta  

r =   12/5  _______________

1 (  5/5  ) +  3/5  cos \theta  

r =   12/5  ____________  5/5  +  3/5  cos \theta  

r =  12/5  ⋅  _________ 5 + 3 cos \theta  

r =  _________ 5 + 3 cos \theta  

---
### ✏️ **Try It #3**
Find the polar form of the conic given a focus at the origin, e = 1, and directrix x = -1.

---
### 📐 **Example  7**
Converting a Conic in Polar Form to Rectangular Form Convert the conic r =  _________ 5 - 5sin \theta   to rectangular form.

**Solution**

We will rearrange the formula to use the identities r = √x 2 + y² , x = r cos \theta , and y = r sin \theta .

r =  _________ 5 - 5sin \theta  

r ⋅ (5 - 5 sin \theta ) =  _________ 5 - 5sin \theta   ⋅ (5 - 5 sin \theta ) Eliminate the fraction.

5r - 5r sin \theta  = 1 Distribute.

5r = 1 + 5r sin \theta  Isolate 5r.

25r 2 = (1 + 5r sin \theta )² Square both sides.

25(x 2 + y 2) = (1 + 5y)² Substitute r = √x 2 + y 2  and y = r sin \theta .

Distribute and use FOIL.

Rearrange terms and set equal to 1.

---
### ✏️ **Try It #4**
Convert the conic r =  __________ 1 + 2cos \theta   to rectangular form. Access these online resources for additional instruction and practice with conics in polar coordinates. • Polar Equations of Conic Sections (http://openstaxcollege.org/l/determineconic) • Graphing Polar Equations of Conics – 1 (http://openstaxcollege.org/l/graphconic¹) • Graphing Polar Equations of Conics – 2 (http://openstaxcollege.org/l/graphconic²)

### 10.5 Section Exercises

Verbal 1. Explain how eccentricity determines which conic section is given. 2. If a conic section is written as a polar equation, what must be true of the denominator? 3. If a conic section is written as a polar equation, and the denominator involves sin \theta , what conclusion can be drawn about the directrix? 4. If the directrix of a conic section is perpendicular to the polar axis, what do we know about the equation of the graph? 5. What do we know about the focus/foci of a conic section if it is written as a polar equation? Algebraic For the following exercises, identify the conic with a focus at the origin, and then give the directrix and eccentricity. 6. r =  __________ 1 - 2 cos \theta   7. r =  __________ 4 - 4 sin \theta   8. r =  __________ 4 - 3 cos \theta   9. r =  __________ 1 + 2 sin \theta   10. r =  __________ 4 + 3 cos \theta   11. r =  ____________

10 + 10 cos \theta   12. r =  ________ 1 - cos \theta   13. r =  __________ 7 + 2 cos \theta   14. r(1 - cos \theta ) = 3 15. r(3 + 5sin \theta ) = 11 16. r(4 - 5sin \theta ) = 1 17. r(7 + 8cos \theta ) = 7 For the following exercises, convert the polar equation of a conic section to a rectangular equation. 18. r =  __________ 1 + 3 sin \theta   19. r =  __________ 5 - 3 sin \theta   20. r =  __________ 3 - 2 cos \theta   21. r =  __________ 2 + 5 cos \theta   22. r =  __________ 2 + 2 sin \theta   23. r = __________ 8 - 8 cos \theta   24. r =  __________ 6 + 7 cos \theta   25. r =  ___________ 5 - 11 sin \theta   26. r(5 + 2 cos \theta ) = 6 27. r(2 - cos \theta ) = 1 29. r =  6sec \theta  ___________ -2 + 3 sec \theta   30. r =  6csc \theta  __________ 3 + 2 csc \theta   For the following exercises, graph the given conic section. If it is a parabola, label the vertex, focus, and directrix. If it is an ellipse, label the vertices and foci. If it is a hyperbola, label the vertices and foci. 31. r =  ________ 2 + cos \theta   32. r =  __________ 3 + 3 sin \theta   33. r =  __________ 5 - 4 sin \theta   34. r =  __________ 1 + 2 cos \theta   35. r =  __________ 4 - 5 cos \theta   36. r =  __________ 4 - 4 cos \theta   37. r =  _ 1 - sin \theta   38. r =  __________ 3 + 2 sin \theta   39. r(1 + cos \theta ) = 5 40. r(3 - 4sin \theta ) = 9 41. r(3 - 2sin \theta ) = 6 42. r(6 - 4cos \theta ) = 5 For the following exercises, find the polar equation of the conic with focus at the origin and the given eccentricity and directrix. 43. Directrix: x = 4; e =  1/5  44. Directrix: x = - 4; e = 5 45. Directrix: y = 2; e = 2 46. Directrix: y = - 2; e =  1/2  47. Directrix: x = 1; e = 1 48. Directrix: x = -1; e = 1 49. Directrix: x = - 1/4 ; e =  7/2  50. Directrix: y =  2/5 ; e =  7/2  51. Directrix: y = 4; e =  3/2  52. Directrix: x = -2; e =  8/3  53. Directrix: x = -5; e =  3/4  54. Directrix: y = 2; e = 2.5 55. Directrix: x = -3; e =  1/3  Extensions Recall from Rotation of Axes that equations of conics with an xy term have rotated graphs. For the following exercises, express each equation in polar form with r as a function of \theta . 57. x 2 + xy + y 2 = 4 60. 2xy + y = 1

### Key Terms

angle of rotation an acute angle formed by a set of axes rotated from the Cartesian plane where, if cot(2\theta ) > 0, then \theta  is between (0°, 45°); if cot(2\theta ) < 0, then \theta  is between (45°, 90°); and if cot(2\theta ) = 0, then \theta  = 45° center of a hyperbola the midpoint of both the transverse and conjugate axes of a hyperbola center of an ellipse the midpoint of both the major and minor axes conic section any shape resulting from the intersection of a right circular cone with a plane conjugate axis the axis of a hyperbola that is perpendicular to the transverse axis and has the co-vertices as its endpoints degenerate conic sections any of the possible shapes formed when a plane intersects a double cone through the apex. Types of degenerate conic sections include a point, a line, and intersecting lines. directrix a line perpendicular to the axis of symmetry of a parabola; a line such that the ratio of the distance between the points on the conic and the focus to the distance to the directrix is constant eccentricity the ratio of the distances from a point P on the graph to the focus F and to the directrix D represented by e =  PF ___ PD , where e is a positive real number ellipse the set of all points (x, y) in a plane such that the sum of their distances from two fixed points is a constant foci plural of focus focus (of a parabola) a fixed point in the interior of a parabola that lies on the axis of symmetry focus (of an ellipse) one of the two fixed points on the major axis of an ellipse such that the sum of the distances from these points to any point (x, y) on the ellipse is a constant hyperbola the set of all points (x, y) in a plane such that the difference of the distances between (x, y) and the foci is a positive constant latus rectum the line segment that passes through the focus of a parabola parallel to the directrix, with endpoints on the parabola major axis the longer of the two axes of an ellipse minor axis the shorter of the two axes of an ellipse nondegenerate conic section a shape formed by the intersection of a plane with a double right cone such that the plane does not pass through the apex; nondegenerate conics include circles, ellipses, hyperbolas, and parabolas parabola the set of all points (x, y) in a plane that are the same distance from a fixed line, called the directrix, and a fixed point (the focus) not on the directrix polar equation an equation of a curve in polar coordinates r and \theta  transverse axis the axis of a hyperbola that includes the foci and has the vertices as its endpoints Key Equations Horizontal ellipse, center at origin  x 2/a²  +  y 2/b²  = 1, a > b Vertical ellipse, center at origin  x 2/b²  +  y 2/a²  = 1, a > b Horizontal ellipse, center (h, k)  (x - h)² _______ a²  +  (y - k)² _______ b²  = 1, a > b Vertical ellipse, center (h, k)  (x - h)² _______ b²  +  (y - k)² _______ a²  = 1, a > b Hyperbola, center at origin, transverse axis on x-axis  x 2/a²  -  y 2/b²  = 1 Hyperbola, center at origin, transverse axis on y-axis  y 2/a²  -  x 2/b²  = 1

Hyperbola, center at (h, k), transverse axis parallel to x-axis  (x - h)² _______ a²  -  (y - k)² _______ b²  = 1 Hyperbola, center at (h, k), transverse axis parallel to y-axis  (y - k)² _______ a²  -  (x - h)² _______ b²  = 1 Parabola, vertex at origin, axis of symmetry on x-axis y 2 = 4px Parabola, vertex at origin, axis of symmetry on y-axis x 2 = 4py Parabola, vertex at (h, k), axis of symmetry on x-axis (y - k)² = 4p(x - h) Parabola, vertex at (h, k), axis of symmetry on y-axis (x - h)² = 4p(y - k) General Form equation of a conic section Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 Rotation of a conic section x = x' cos \theta  - y' sin \theta 

y = x' sin \theta  + y' cos \theta  Angle of rotation \theta , where cot(2\theta ) =  A - C ______ B 

### Key Concepts

• An ellipse is the set of all points (x, y) in a plane such that the sum of their distances from two fixed points is a constant. Each fixed point is called a focus (plural: foci). • When given the coordinates of the foci and vertices of an ellipse, we can write the equation of the ellipse in standard form. See Example 1 and Example 2. • When given an equation for an ellipse centered at the origin in standard form, we can identify its vertices, co-vertices, foci, and the lengths and positions of the major and minor axes in order to graph the ellipse. See

**Example 3** — and Example 4.
• When given the equation for an ellipse centered at some point other than the origin, we can identify its key features and graph the ellipse. See Example 5 and Example 6. • Real-world situations can be modeled using the standard equations of ellipses and then evaluated to find key features, such as lengths of axes and distance between foci. See Example 7. 10.2 The Hyperbola • A hyperbola is the set of all points (x, y) in a plane such that the difference of the distances between (x, y) and the foci is a positive constant. • The standard form of a hyperbola can be used to locate its vertices and foci. See Example 1. • When given the coordinates of the foci and vertices of a hyperbola, we can write the equation of the hyperbola in standard form. See Example 2 and Example 3. • When given an equation for a hyperbola, we can identify its vertices, co-vertices, foci, asymptotes, and lengths and positions of the transverse and conjugate axes in order to graph the hyperbola. See Example 4 and Example 5. • Real-world situations can be modeled using the standard equations of hyperbolas. For instance, given the dimensions of a natural draft cooling tower, we can find a hyperbolic equation that models its sides. See Example 6.

• A parabola is the set of all points (x, y) in a plane that are the same distance from a fixed line, called the directrix, and a fixed point (the focus) not on the directrix. • The standard form of a parabola with vertex (0, 0) and the x-axis as its axis of symmetry can be used to graph the parabola. If p > 0, the parabola opens right. If p < 0, the parabola opens left. See Example 1. • The standard form of a parabola with vertex (0, 0) and the y-axis as its axis of symmetry can be used to graph the parabola. If p > 0, the parabola opens up. If p < 0, the parabola opens down. See Example 2. • When given the focus and directrix of a parabola, we can write its equation in standard form. See Example 3. • The standard form of a parabola with vertex (h, k) and axis of symmetry parallel to the x-axis can be used to graph the parabola. If p > 0, the parabola opens right. If p < 0, the parabola opens left. See Example 4. • The standard form of a parabola with vertex (h, k) and axis of symmetry parallel to the y-axis can be used to graph the parabola. If p > 0, the parabola opens up. If p < 0, the parabola opens down. See Example 5. • Real-world situations can be modeled using the standard equations of parabolas. For instance, given the diameter and focus of a cross-section of a parabolic reflector, we can find an equation that models its sides. See Example 6. 10.4 Rotation of Axes • Four basic shapes can result from the intersection of a plane with a pair of right circular cones connected tail to tail. They include an ellipse, a circle, a hyperbola, and a parabola. • A nondegenerate conic section has the general form Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 where A, B and C are not all zero. The values of A, B, and C determine the type of conic. See Example 1. • Equations of conic sections with an xy term have been rotated about the origin. See Example 2. • The general form can be transformed into an equation in the x' and y' coordinate system without the x' y' term. See Example 3 and Example 4. • An expression is described as invariant if it remains unchanged after rotating. Because the discriminant is invariant, observing it enables us to identify the conic section. See Example 5. 10.5 Conic Sections in Polar Coordinates • Any conic may be determined by a single focus, the corresponding eccentricity, and the directrix. We can also define a conic in terms of a fixed point, the focus P(r, \theta ) at the pole, and a line, the directrix, which is perpendicular to the polar axis. • A conic is the set of all points e =  PF ___ PD , where eccentricity e is a positive real number. Each conic may be written in terms of its polar equation. See Example 1. • The polar equations of conics can be graphed. See Example 2, Example 3, and Example 4. • Conics can be defined in terms of a focus, a directrix, and eccentricity. See Example 5 and Example 6. • We can use the identities r = √x 2 + y 2 , x = r cos \theta , and y = r sin \theta  to convert the equation for a conic from polar to rectangular form. See Example 7.

The Ellipse For the following exercises, write the equation of the ellipse in standard form. Then identify the center, vertices, and foci.

___ 25  +  y 2

___ 2.  (x - 2)² _______ 100  +  (y + 3)² _______ 36  = 1 3. 9x 2 + y 2 + 54x - 4y + 76 = 0 For the following exercises, graph the ellipse, noting center, vertices, and foci.

___ 36  +  y 2/9  = 1 6.  (x - 4)² _______  +  (y + 3)² _______  = 1 7. 4x 2 + y 2 + 16x + 4y - 44 = 0 For the following exercises, use the given information to find the equation for the ellipse. 9. Center at (0, 0), focus at (3, 0), vertex at (-5, 0) 10. Center at (2, -2), vertex at (7, -2), focus at (4, -2) 11. A whispering gallery is to be constructed such that the foci are located 35 feet from the center. If the length of the gallery is to be 100 feet, what should the height of the ceiling be? The Hyperbola For the following exercises, write the equation of the hyperbola in standard form. Then give the center, vertices, and foci.

___ 81  -  y 2/9  = 1 _______  -  (x - 4)² _______  = 1 15. 3x 2 - y 2 - 12x - 6y - 9 = 0 For the following exercises, graph the hyperbola, labeling vertices and foci.

__ 9  -  y 2

___ _______  -  (x + 1)² _______  = 1 For the following exercises, find the equation of the hyperbola. 20. Center at (0, 0), vertex at (0, 4), focus at (0, -6) 21. Foci at (3, 7) and (7, 7), vertex at (6, 7) The Parabola For the following exercises, write the equation of the parabola in standard form. Then give the vertex, focus, and directrix. 23. (x + 2)² =  1/2 (y - 1) 24. y 2 - 6y - 6x - 3 = 0 25. x 2 + 10x - y + 23 = 0 For the following exercises, graph the parabola, labeling vertex, focus, and directrix. 27. (y - 1)² =  1/2 (x + 3)

For the following exercises, write the equation of the parabola using the given information. 30. Focus at (-4, 0); directrix is x = 4 31. Focus at ( 2,  9/8  ) ; directrix is y =  7/8  32. A cable TV receiving dish is the shape of a paraboloid of revolution. Find the location of the receiver, which is placed at the focus, if the dish is 5 feet across at its opening and 1.5 feet deep. Rotation of Axes For the following exercises, determine which of the conic sections is represented. 35. 4x 2 + xy + 2y 2 + 8x - 26y + 9 = 0 For the following exercises, determine the angle \theta  that will eliminate the xy term, and write the corresponding equation without the xy term. 36. x 2 + 4xy - 2y 2 - 6 = 0 37. x 2 - xy + y 2 - 6 = 0 For the following exercises, graph the equation relative to the x'y' system in which the equation has no x'y' term. 39. x 2 - xy + y 2 - 2 = 0 Conic Sections in Polar Coordinates For the following exercises, given the polar equation of the conic with focus at the origin, identify the eccentricity and directrix. 41. r =  _________ 1 - 5 cos \theta   42. r =  _________ 3 + 2 cos \theta   43. r =  _________ 4 + 3 sin \theta   44. r =  _________ 5 - 5 sin \theta   For the following exercises, graph the conic given in polar form. If it is a parabola, label the vertex, focus, and directrix. If it is an ellipse or a hyperbola, label the vertices and foci. 45. r =  ________ 1 - sin \theta   46. r =  _________ 4 + 3 sin \theta   47. r =  _________ 4 + 5 cos \theta   48. r =  _________ 3 - 6 cos \theta   For the following exercises, given information about the graph of a conic with focus at the origin, find the equation in polar form. 49. Directrix is x = 3 and eccentricity e = 1 50. Directrix is y = -2 and eccentricity e = 4

For the following exercises, write the equation in standard form and state the center, vertices, and foci.

__ 9  +  y 2/4  = 1 For the following exercises, sketch the graph, identifying the center, vertices, and foci. 3.  (x - 3)² _______  +  (y - 2)² _______  = 1 4. 2x 2 + y 2 + 8x - 6y - 7 = 0 5. Write the standard form equation of an ellipse with a center at (1, 2), vertex at (7, 2), and focus at (4, 2). 6. A whispering gallery is to be constructed with a length of 150 feet. If the foci are to be located 20 feet away from the wall, how high should the ceiling be? For the following exercises, write the equation of the hyperbola in standard form, and give the center, vertices, foci, and asymptotes.

___ 49  -  y 2

___ For the following exercises, graph the hyperbola, noting its center, vertices, and foci. State the equations of the asymptotes. 9.  (x - 3)² _______  -  (y + 3)² _______  = 1 10. y 2 - x 2 + 4y - 4x - 18 = 0 11. Write the standard form equation of a hyperbola with foci at (1, 0) and (1, 6), and a vertex at (1, 2). For the following exercises, write the equation of the parabola in standard form, and give the vertex, focus, and equation of the directrix. For the following exercises, graph the parabola, labeling the vertex, focus, and directrix. 14. (x - 1)² = -4(y + 3) 15. y 2 + 8x - 8y + 40 = 0 16. Write the equation of a parabola with a focus at (2, 3) and directrix y = -1. 17. A searchlight is shaped like a paraboloid of revolution. If the light source is located 1.5 feet from the base along the axis of symmetry, and the depth of the searchlight is 3 feet, what should the width of the opening be? For the following exercises, determine which conic section is represented by the given equation, and then determine the angle \theta  that will eliminate the xy term. 19. x 2 + 4xy + 4y 2 + 6x - 8y = 0 For the following exercises, rewrite in the x'y' system without the x'y' term, and graph the rotated graph.

3 xy + y 2 = 4 For the following exercises, identify the conic with focus at the origin, and then give the directrix and eccentricity. 22. r =  ________ 2 - sin \theta   23. r =  _________ 4 + 6 cos \theta   For the following exercises, graph the given conic section. If it is a parabola, label vertex, focus, and directrix. If it is an ellipse or a hyperbola, label vertices and foci. 24. r =  _________ 4 - 8 sin \theta   25. r =  _________ 4 + 4 sin \theta   26. Find a polar equation of the conic with focus at the origin, eccentricity of e = 2, and directrix: x = 3.
