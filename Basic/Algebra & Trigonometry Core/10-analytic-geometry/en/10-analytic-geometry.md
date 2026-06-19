# Analytic Geometry

## Introduction
The Greek mathematician Menaechmus (c. 380–c. 320 BCE) is generally credited with discovering the shapes formed by the intersection of a plane and a right circular cone. Depending on how he tilted the plane when it intersected the cone, he formed different shapes at the intersection—beautiful shapes with near-perfect symmetry. It was also said that Aristotle may have had an intuitive understanding of these shapes, as he observed the orbit of the planet to be circular. He presumed that the planets moved in circular orbits around Earth, and for nearly 2,000 years this was the commonly held belief. It was not until the Renaissance movement that Johannes Kepler noticed that the orbits of the planet were not circular in nature. His published law of planetary motion in the 1600s changed our view of the solar system forever. He claimed that the sun was at one end of the orbits, and the planets revolved around the sun in an oval-shaped path. In this chapter, we will investigate the two-dimensional figures that are formed when a right circular cone is intersected by a plane. We will begin by studying each of three figures created in this manner. We will develop defining equations for each figure and then learn how to use these equations to solve a variety of problems. a b

Learning Objectives
In this section, you will:
• Write equations of ellipses in standard form.
• Graph ellipses centered at the origin.
• Graph ellipses not centered at the origin.
• Solve applied problems involving ellipses.

## 10.1 The Ellipse
Can you imagine standing at one end of a large room and still being able to hear a whisper from a person standing at the other end? The National Statuary Hall in Washington, D.C., shown in Figure 1, is such a room.[33] It is an oval- shaped room called a whispering chamber because the shape makes it possible for sound to travel along the walls. In this section, we will investigate the shape of this room and its real-world applications, including how far apart two people in Statuary Hall can stand and still hear each other whisper. Writing Equations of Ellipses in Standard Form A conic section, or conic, is a shape resulting from intersecting a right circular cone with a plane. The angle at which the plane intersects the cone determines the shape, as shown in Figure 2. Ellipse Hyperbola Parabola Conic sections can also be described by a set of points in the coordinate plane. Later in this chapter, we will see that the graph of any quadratic equation in two variables is a conic section. The signs of the equations and the coefficients of the variable terms determine the shape. This section focuses on the four variations of the standard form of the 33. Architect of the Capitol. http://www.aoc.gov. Accessed April 15, 2014.

equation for the ellipse. An ellipse is the set of all points (x, y) in a plane such that the sum of their distances from two fixed points is a constant. Each fixed point is called a focus (plural: foci). We can draw an ellipse using a piece of cardboard, two thumbtacks, a pencil, and string. Place the thumbtacks in the cardboard to form the foci of the ellipse. Cut a piece of string longer than the distance between the two thumbtacks (the length of the string represents the constant in the definition). Tack each end of the string to the cardboard, and trace a curve with a pencil held taut against the string. The result is an ellipse. See Figure 3. Foci Every ellipse has two axes of symmetry. The longer axis is called the major axis, and the shorter axis is called the minor axis. Each endpoint of the major axis is the vertex of the ellipse (plural: vertices), and each endpoint of the minor axis is a co-vertex of the ellipse. The center of an ellipse is the midpoint of both the major and minor axes. The axes are perpendicular at the center. The foci always lie on the major axis, and the sum of the distances from the foci to any point on the ellipse (the constant sum) is greater than the distance between the foci. See Figure 4. Co-vertex Vertex Co-vertex Minor Axis Major Axis Center Focus Focus x y Vertex In this section, we restrict ellipses to those that are positioned vertically or horizontally in the coordinate plane. That is, the axes will either lie on or be parallel to the x- and y-axes. Later in the chapter, we will see ellipses that are rotated in the coordinate plane. To work with horizontal and vertical ellipses in the coordinate plane, we consider two cases: those that are centered at the origin and those that are centered at a point other than the origin. First we will learn to derive the equations of ellipses, and then we will learn how to write the equations of ellipses in standard form. Later we will use what we learn to draw the graphs.

Deriving the Equation of an Ellipse Centered at the Origin To derive the equation of an ellipse centered at the origin, we begin with the foci (-c, 0) and (c, 0). The ellipse is the set of all points (x, y) such that the sum of the distances from (x, y) to the foci is constant, as shown in Figure 5. y x (x, y) (a, 0) (c, 0) (–c, 0) (–a, 0) d^{1} d^{2} If (a, 0) is a vertex of the ellipse, the distance from (-c, 0) to (a, 0) is a - ( -c) = a + c. The distance from (c, 0) to (a, 0) is a - c . The sum of the distances from the foci to the vertex is

(a + c) + (a - c) = 2a If (x, y) is a point on the ellipse, then we can define the following variables:

d^{1} = the distance from (-c, 0) to (x, y)

d^{2} = the distance from (c, 0) to (x, y) By the definition of an ellipse, d^{1} + d^{2} is constant for any point (x, y) on the ellipse. We know that the sum of these distances is 2a for the vertex (a, 0). It follows that d^{1} + d^{2} = 2a for any point on the ellipse. We will begin the derivation by applying the distance formula. The rest of the derivation is algebraic.

d^{1} + d^{2} = \sqrt{—}

(x - ( - c))^{2} + (y - 0)^{2}  + \sqrt{(x} - c)^{2} + (y - 0)^{2}  = 2a Distance formula \sqrt{(x} + c)^{2} + y 2  + \sqrt{(x} - c)^{2} + y 2  = 2a Simplify expressions.

\sqrt{(x} + c)^{2} + y 2  = 2a - \sqrt{(x} - c)^{2} + y 2  Move radical to opposite side.

(x + c)^{2} + y 2 = [2a -\sqrt{(x} - c)^{2} + y 2 ]  Square both sides.

x 2 + 2cx + c^{2} + y 2 = 4a^{2} - 4a\sqrt{(x} - c)^{2} + y 2  + (x - c)^{2} + y 2 Expand the squares.

x 2 + 2cx + c^{2} + y 2 = 4a^{2} - 4a\sqrt{(x} - c)^{2} + y 2  + x 2 - 2cx + c^{2} + y 2 Expand remaining squares.

2cx = 4a^{2} - 4a\sqrt{(x} - c)^{2} + y 2  - 2cx Combine like terms.

4cx - 4a^{2} = -4a\sqrt{(x} - c)^{2} + y 2  Isolate the radical.

cx - a^{2} = - a \sqrt{(x} - c)^{2} + y 2  Divide by 4.

 cx - a^{2}   2 = a^{2}  \sqrt{(x} - c)^{2} + y 2     Square both sides.

c^{2} x 2 - 2a^{2} cx + a^{4} = a^{2}  x 2 - 2cx + c^{2} + y 2   Expand the squares.

c^{2} x 2 - 2a^{2} cx + a^{4} = a^{2} x 2 - 2a^{2} cx + a^{2} c^{2} + a^{2} y 2 Distribute a^{2}.

a^{2} x 2 - c^{2} x 2 + a^{2} y 2 = a^{4} - a^{2} c^{2} Rewrite.

x 2(a^{2} - c^{2}) + a^{2} y 2 = a^{2}(a^{2} - c^{2}) Factor common terms.

x 2 b^{2} + a^{2} y 2 = a^{2} b^{2} Set b^{2} = a^{2} - c^{2}.

 x 2b^{2} ____ a^{2}b^{2}  +  a^{2}y 2 ____ a^{2}b^{2}  =  a^{2}b^{2} ____ a^{2}b^{2}  Divide both sides by a^{2}b^{2}.

 x 2

__ a^{2}  +  y 2

__ b^{2}  = 1 Simplify. Thus, the standard equation of an ellipse is  x 2

__ a^{2}  +  y 2

_ b^{2}  = 1. This equation defines an ellipse centered at the origin. If a > b, the ellipse is stretched further in the horizontal direction, and if b > a, the ellipse is stretched further in the vertical direction.


### Writing Equations of Ellipses Centered at the Origin in Standard Form
Standard forms of equations tell us about key features of graphs. Take a moment to recall some of the standard forms of equations we’ve worked with in the past: linear, quadratic, cubic, exponential, logarithmic, and so on. By learning to interpret standard forms of equations, we are bridging the relationship between algebraic and geometric representations of mathematical phenomena. The key features of the ellipse are its center, vertices, co-vertices, foci, and lengths and positions of the major and minor axes. Just as with other equations, we can identify all of these features just by looking at the standard form of the equation. There are four variations of the standard form of the ellipse. These variations are categorized first by the location of the center (the origin or not the origin), and then by the position (horizontal or vertical). Each is presented along with a description of how the parts of the equation relate to the graph. Interpreting these parts allows us to form a mental picture of the ellipse. standard forms of the equation of an ellipse with center (0, 0) The standard form of the equation of an ellipse with center (0, 0) and major axis on the x-axis is  x 2

_ a^{2}  +  y 2

_ b^{2}  = 1 where • a > b • the length of the major axis is 2a • the coordinates of the vertices are (\pm a, 0) • the length of the minor axis is 2b • the coordinates of the co-vertices are (0, \pm b) • the coordinates of the foci are (\pm c, 0) , where c^{2} = a^{2} - b^{2}. See Figure 6a. The standard form of the equation of an ellipse with center (0, 0) and major axis on the y-axis is  x 2

_ b^{2}  +  y 2

_ a^{2}  = 1 where • a > b • the length of the major axis is 2a • the coordinates of the vertices are (0, \pm  a) • the length of the minor axis is 2b • the coordinates of the co-vertices are (\pm b, 0) • the coordinates of the foci are (0, \pm  c) , where c^{2} = a^{2} - b^{2}. See Figure 6b. Note that the vertices, co-vertices, and foci are related by the equation c^{2} = a^{2} - b^{2}. When we are given the coordinates of the foci and vertices of an ellipse, we can use this relationship to find the equation of the ellipse in standard form. (0, b) (c, 0) (-a, 0) (-c, 0) (0, a) (0, -a) (0, -b) (a) (b) (0, -c) (0, c) (-b, 0) (b, 0) (a, 0) Major Axis Minor Axis Minor Axis Major Axis x x y y


**How To…**
Given the vertices and foci of an ellipse centered at the origin, write its equation in standard form. 1. Determine whether the major axis lies on the x- or y-axis.

a. If the given coordinates of the vertices and foci have the form (\pm a, 0) and ( \pm c, 0) respectively, then the major axis is the x-axis. Use the standard form  x 2

_ a^{2}  +  y 2

_ b^{2}  = 1.

b. If the given coordinates of the vertices and foci have the form (0, \pm a) and ( \pm c, 0), respectively, then the major axis is the y-axis. Use the standard form  x 2

_ b^{2}  +  y 2

_ a^{2}  = 1. 2. Use the equation c^{2} = a^{2} - b^{2}, along with the given coordinates of the vertices and foci, to solve for b^{2}. 3. Substitute the values for a^{2} and b^{2} into the standard form of the equation determined in Step 1.

**Example  1**

### Writing the Equation of an Ellipse Centered at the Origin in Standard Form
What is the standard form equation of the ellipse that has vertices (\pm 8, 0) and foci (\pm 5, 0)? Solution The foci are on the x-axis, so the major axis is the x-axis. Thus, the equation will have the form

 x 2

__ a^{2}  +  y 2

_ b^{2}  = 1 The vertices are (\pm 8, 0), so a = 8 and a^{2} = 64. The foci are (\pm 5, 0), so c = 5 and c^{2} = 25. We know that the vertices and foci are related by the equation c 2 = a 2 - b 2. Solving for b 2, we have:

c 2 = a 2 - b^{2}

Substitute for c 2 and a 2.

Solve for b^{2}. Now we need only substitute a^{2} = 64 and b^{2} = 39 into the standard form of the equation. The equation of the ellipse is  x 2

_ 64  +  y 2

_

**Try It #1**
What is the standard form equation of the ellipse that has vertices (0, \pm  4) and foci (0, \pm  \sqrt{15} )? Can we write the equation of an ellipse centered at the origin given coordinates of just one focus and vertex? Yes. Ellipses are symmetrical, so the coordinates of the vertices of an ellipse centered around the origin will always have the form (\pm a, 0) or (0, \pm  a). Similarly, the coordinates of the foci will always have the form (\pm c, 0) or (0, \pm  c). Knowing this, we can use a and c from the given points, along with the equation c^{2} = a^{2} - b^{2}, to find b^{2}. Writing Equations of Ellipses Not Centered at the Origin Like the graphs of other equations, the graph of an ellipse can be translated. If an ellipse is translated h units horizontally and k units vertically, the center of the ellipse will be (h, k). This translation results in the standard form of the equation we saw previously, with x replaced by (x - h) and y replaced by (y - k).

standard forms of the equation of an ellipse with center (h, k) The standard form of the equation of an ellipse with center (h, k) and major axis parallel to the x-axis is  (x - h)^{2} _ a^{2}  +  (y - k)^{2} _ b^{2}  = 1 where • a > b • the length of the major axis is 2a • the coordinates of the vertices are (h \pm  a, k) • the length of the minor axis is 2b • the coordinates of the co-vertices are (h, k \pm  b) • the coordinates of the foci are (h \pm  c, k), where c^{2} = a^{2} - b^{2}. See Figure 7a. The standard form of the equation of an ellipse with center (h, k) and major axis parallel to the y-axis is  (x - h)^{2} _ b^{2}  +  (y - k)^{2} _ a^{2}  = 1 where • a > b • the length of the major axis is 2a • the coordinates of the vertices are (h, k \pm  a) • the length of the minor axis is 2b • the coordinates of the co-vertices are (h \pm  b, k) • the coordinates of the foci are (h, k \pm  c), where c^{2} = a^{2} - b^{2}. See Figure 7b. Just as with ellipses centered at the origin, ellipses that are centered at a point (h, k) have vertices, co-vertices, and foci that are related by the equation c^{2} = a^{2} - b^{2}. We can use this relationship along with the midpoint and distance formulas to find the equation of the ellipse in standard form when the vertices and foci are given. y y x x (h + c^{1}, k) (h, k - a) (h, k - c) (h, k - b) (h, k) (h, k) (h, k + b) (h + a, k) (h + b, k) (h, k + a) (h, k + c) (h - a, k) (h - b, k) (h - c^{1}, k) Major Axis Major Axis Minor Axis Minor Axis (a) (b)

**How To…**
Given the vertices and foci of an ellipse not centered at the origin, write its equation in standard form. 1. Determine whether the major axis is parallel to the x- or y-axis. a. If the y-coordinates of the given vertices and foci are the same, then the major axis is parallel to the x-axis. Use the standard form  (x - h)^{2} _ a^{2}  +  (y - k)^{2} _ b^{2}  = 1. b. If the x-coordinates of the given vertices and foci are the same, then the major axis is parallel to the y-axis. Use the standard form  (x - h)^{2} _ b^{2}  +  (y - k)^{2} _ a^{2}  = 1.

2. Identify the center of the ellipse (h, k) using the midpoint formula and the given coordinates for the vertices. 3. Find a^{2} by solving for the length of the major axis, 2a, which is the distance between the given vertices. 4. Find c^{2} using h and k, found in Step 2, along with the given coordinates for the foci. 5. Solve for b^{2} using the equation c^{2} = a^{2} - b^{2}. 6. Substitute the values for h, k, a^{2}, and b^{2} into the standard form of the equation determined in Step 1.

**Example  2**
Writing the Equation of an Ellipse Centered at a Point Other Than the Origin What is the standard form equation of the ellipse that has vertices (-2, -8) and (-2, 2) and foci (-2, -7) and (-2, 1)? Solution The x-coordinates of the vertices and foci are the same, so the major axis is parallel to the y-axis. Thus, the equation of the ellipse will have the form

 (x - h)^{2} _ b^{2}  +  (y - k)^{2} _ a^{2}  = 1 First, we identify the center, (h, k). The center is halfway between the vertices, (-2, - 8) and (-2, 2). Applying the midpoint formula, we have:

(h, k) =   -2 + (-2) _________  ,  -8 + 2 _______   

= (-2, -3) Next, we find a^{2}. The length of the major axis, 2a, is bounded by the vertices. We solve for a by finding the distance between the y-coordinates of the vertices.

2a = 2 - (-8)

a = 5 Now we find c^{2}. The foci are given by (h, k \pm  c). So, (h, k - c) = (-2, -7) and (h, k + c) = (-2, 1). We substitute k = -3 using either of these points to solve for c.

k + c = 1

-3 + c = 1

c = 4 Next, we solve for b^{2} using the equation c^{2} = a^{2} - b^{2}.

c^{2} = a^{2} - b^{2}

b^{2} = 9 Finally, we substitute the values found for h, k, a^{2}, and b^{2} into the standard form equation for an ellipse:

 (x + 2)^{2} _  +  (y + 3)^{2} _  = 1

**Try It #2**
What is the standard form equation of the ellipse that has vertices (-3, 3) and (5, 3) and foci (1 - 2\sqrt{3} , 3) and (1 + 2\sqrt{Graphing} Ellipses Centered at the Origin Just as we can write the equation for an ellipse given its graph, we can graph an ellipse given its equation. To graph ellipses centered at the origin, we use the standard form  x 2

_ a^{2}  +  y 2

_ b^{2}  = 1, a > b for horizontal ellipses and  x 2

_ b^{2}  +  y 2

_ a^{2}  = 1, a > b for vertical ellipses.


**How To…**
Given the standard form of an equation for an ellipse centered at (0, 0), sketch the graph. 1. Use the standard forms of the equations of an ellipse to determine the major axis, vertices, co-vertices, and foci. a. If the equation is in the form  x 2

_ a^{2}  +  y 2

_ b^{2}  = 1, where a > b, then • the major axis is the x-axis • the coordinates of the vertices are (\pm a, 0) • the coordinates of the co-vertices are (0, \pm  b) • the coordinates of the foci are (\pm c, 0) b. If the equation is in the form  x 2

_ b^{2}  +  y 2

_ a^{2}  = 1, where a > b, then • the major axis is the y-axis • the coordinates of the vertices are (0, \pm  a) • the coordinates of the co-vertices are (\pm b, 0) • the coordinates of the foci are (0, \pm  c) 2. Solve for c using the equation c^{2} = a^{2} - b^{2}. 3. Plot the center, vertices, co-vertices, and foci in the coordinate plane, and draw a smooth curve to form the ellipse.

**Example  3**

### Graphing an Ellipse Centered at the Origin
Graph the ellipse given by the equation,  x 2

_ 9  +  y 2

_ 25  = 1. Identify and label the center, vertices, co-vertices, and foci. Solution First, we determine the position of the major axis. Because 25 > 9, the major axis is on the y-axis. Therefore, the equation is in the form  x 2

_ b 2  +  y 2

_ a 2  = 1, where b 2 = 9 and a^{2} = 25. It follows that: • the center of the ellipse is (0, 0) • the coordinates of the vertices are (0, \pm  a) = (0, \pm  \sqrt{25} ) = (0, \pm  5) • the coordinates of the co-vertices are (\pm b, 0) = (\pm  \sqrt{•} the coordinates of the foci are (0, \pm  c), where c 2 = a 2 - b 2 Solving for c, we have:

c = \pm  \sqrt{a^{2}} - b^{2} 

= \pm  \sqrt{—}

= \pm  \sqrt{16} 

= \pm  4 Therefore, the coordinates of the foci are (0, \pm  4). Next, we plot and label the center, vertices, co-vertices, and foci, and draw a smooth curve to form the ellipse. See y x


**Try It #3**
Graph the ellipse given by the equation  x 2

__ 36  +  y 2

_ 4  = 1. Identify and label the center, vertices, co-vertices, and foci.

**Example  4**
Graphing an Ellipse Centered at the Origin from an Equation Not in Standard Form Graph the ellipse given by the equation 4x 2 + 25y 2 = 100. Rewrite the equation in standard form. Then identify and label the center, vertices, co-vertices, and foci. Solution First, use algebra to rewrite the equation in standard form.

 4x 2 ____ _ ___ 100 

 x 2

_ 25  +  y 2

_ 4  = 1 Next, we determine the position of the major axis. Because 25 > 4, the major axis is on the x-axis. Therefore, the equation is in the form  x 2

_ a^{2}  +  y 2

_ b^{2}  = 1, where a^{2} = 25 and b^{2} = 4. It follows that: • the center of the ellipse is (0, 0) • the coordinates of the vertices are (\pm a, 0) = (\pm \sqrt{•} the coordinates of the co-vertices are (0, \pm  b) = (0, \pm  \sqrt{4} ) = (0, \pm  2) • the coordinates of the foci are (\pm c, 0), where c 2 = a 2 - b 2. Solving for c, we have:

c = \pm  \sqrt{a^{2}} - b^{2} 

= \pm  \sqrt{—}

= \pm  \sqrt{21}  Therefore the coordinates of the foci are (\pm  \sqrt{Next,} we plot and label the center, vertices, co-vertices, and foci, and draw a smooth curve to form the ellipse. See y x

**Try It #4**
Graph the ellipse given by the equation 49x 2 + 16y 2 = 784. Rewrite the equation in standard form. Then identify and label the center, vertices, co-vertices, and foci. Graphing Ellipses Not Centered at the Origin When an ellipse is not centered at the origin, we can still use the standard forms to find the key features of the graph. When the ellipse is centered at some point, (h, k), we use the standard forms  (x - h)^{2} _ a 2  +  (y - k)^{2} _ b 2  = 1, a > b for horizontal ellipses and  (x - h)^{2} _ b 2  +  (y - k)^{2} _ a^{2}  = 1, a > b for vertical ellipses. From these standard equations, we can easily determine the center, vertices, co-vertices, foci, and positions of the major and minor axes.


**How To…**
Given the standard form of an equation for an ellipse centered at (h, k), sketch the graph. 1. Use the standard forms of the equations of an ellipse to determine the center, position of the major axis, vertices, co-vertices, and foci. a. If the equation is in the form  (x - h)^{2} _ a^{2}  +  (y - k)^{2} _ b^{2}  = 1, where a > b, then • the center is (h, k) • the major axis is parallel to the x-axis • the coordinates of the vertices are (h \pm  a, k) • the coordinates of the co-vertices are (h, k \pm  b) • the coordinates of the foci are (h \pm  c, k) b. If the equation is in the form  (x - h)^{2} _ b^{2}  +  (y - k)^{2} _ a^{2}  = 1, where a > b, then • the center is (h, k) • the major axis is parallel to the y-axis • the coordinates of the vertices are (h, k \pm  a) • the coordinates of the co-vertices are (h \pm  b, k) • the coordinates of the foci are (h, k \pm  c) 2. Solve for c using the equation c 2 = a^{2} - b^{2}. 3. Plot the center, vertices, co-vertices, and foci in the coordinate plane, and draw a smooth curve to form the ellipse.

**Example  5**

### Graphing an Ellipse Centered at (h, k)
Graph the ellipse given by the equation,  (x + 2)^{2} _  +  (y - 5)^{2} _  = 1. Identify and label the center, vertices, co-vertices, and foci. Solution First, we determine the position of the major axis. Because 9 > 4, the major axis is parallel to the y-axis. Therefore, the equation is in the form  (x - h)^{2} _ b^{2}  +  (y - k)^{2} _ a^{2}  = 1, where b^{2} = 4 and a^{2} = 9. It follows that: • the center of the ellipse is (h, k) = (-2, 5) • the coordinates of the vertices are (h, k \pm  a) = (-2, 5 \pm  \sqrt{9} ) = (-2, 5 \pm  3), or (-2, 2) and (-2, 8) • the coordinates of the co-vertices are (h \pm  b, k) = (-2 \pm  \sqrt{4} , 5) = (-2 \pm  2, 5), or (-4, 5) and (0, 5) • the coordinates of the foci are (h, k \pm  c), where c 2 = a 2 - b 2. Solving for c, we have:

c = \pm  \sqrt{a^{2}} - b^{2} 

= \pm  \sqrt{9} - 4 

= \pm  \sqrt{5}  Therefore, the coordinates of the foci are (-2, 5 -\sqrt{5} ) and (-2, 5 + \sqrt{5} ). Next, we plot and label the center, vertices, co-vertices, and foci, and draw a smooth curve to form the ellipse. (-2, 5 + \sqrt{5}) y x


**Try It #5**
Graph the ellipse given by the equation  (x - 4)^{2} _  +  (y - 2)^{2} _  = 1. Identify and label the center, vertices, co-vertices, and foci.

**How To…**
Given the general form of an equation for an ellipse centered at (h, k), express the equation in standard form. 1. Recognize that an ellipse described by an equation in the form ax 2 + by 2 + cx + dy + e = 0 is in general form. 2. Rearrange the equation by grouping terms that contain the same variable. Move the constant term to the opposite side of the equation. 3. Factor out the coefficients of the x 2 and y 2 terms in preparation for completing the square. 4. Complete the square for each variable to rewrite the equation in the form of the sum of multiples of two binomials squared set equal to a constant, m^{1} (x - h)^{2} + m^{2}(y - k)^{2} = m^{3}, where m^{1}, m^{2}, and m^{3} are constants. 5. Divide both sides of the equation by the constant term to express the equation in standard form.

**Example  6**
Graphing an Ellipse Centered at ( h, k) by First Writing It in Standard Form Graph the ellipse given by the equation 4x 2 + 9y 2 - 40x + 36y + 100 = 0. Identify and label the center, vertices, co-vertices, and foci. Solution We must begin by rewriting the equation in standard form.

Group terms that contain the same variable, and move the constant to the opposite side of the equation.

(4x 2 - 40x) + (9y 2 + 36y) = -100 Factor out the coefficients of the squared terms.

4(x 2 - 10x)+ 9(y 2 + 4y) = -100 Complete the square twice. Remember to balance the equation by adding the same constants to each side.

4(x 2 - 10x + 25)+ 9(y 2 + 4y + 4) = -100 + 100 + 36 Rewrite as perfect squares.

4(x - 5)^{2} + 9(y + 2)^{2} = 36 Divide both sides by the constant term to place the equation in standard form.

 (x - 5)^{2} _  +  (y + 2)^{2} _  = 1 Now that the equation is in standard form, we can determine the position of the major axis. Because 9 > 4, the major axis is parallel to the x-axis. Therefore, the equation is in the form  (x - h)^{2} _ a^{2}  +  (y - k)^{2} _ b^{2}  = 1, where a^{2} = 9 and b^{2} = 4. It follows that: • the center of the ellipse is (h, k) = (5, -2) • the coordinates of the vertices are (h \pm  a, k) = (5 \pm  \sqrt{—} 9 , -2) = (5 \pm  3, -2), or (2, -2) and (8, -2) • the coordinates of the co-vertices are (h, k \pm  b) = (5, -2 \pm  \sqrt{—} 4 )= (5, -2 \pm  2), or (5, -4) and (5, 0) • the coordinates of the foci are (h \pm  c, k), where c^{2} = a^{2} - b^{2}. Solving for c, we have:

c = \pm  \sqrt{a^{2}} - b^{2} 

= \pm  \sqrt{9} - 4 

= \pm  \sqrt{5}  Therefore, the coordinates of the foci are (5 - \sqrt{5} , -2) and (5 + \sqrt{Next} we plot and label the center, vertices, co-vertices, and foci, and draw a smooth curve to form the ellipse as shown in Figure 11.

9 x

**Try It #6**
Express the equation of the ellipse given in standard form. Identify the center, vertices, co-vertices, and foci of the ellipse. 4x 2 + y 2 - 24x + 2y + 21 = 0 Solving Applied Problems Involving Ellipses Many real-world situations can be represented by ellipses, including orbits of planets, satellites, moons and comets, and shapes of boat keels, rudders, and some airplane wings. A medical device called a lithotripter uses elliptical reflectors to break up kidney stones by generating sound waves. Some buildings, called whispering chambers, are designed with elliptical domes so that a person whispering at one focus can easily be heard by someone standing at the other focus. This occurs because of the acoustic properties of an ellipse. When a sound wave originates at one focus of a whispering chamber, the sound wave will be reflected off the elliptical dome and back to the other focus. See Figure 12. In the whisper chamber at the Museum of Science and Industry in Chicago, two people standing at the foci—about 43 feet apart—can hear each other whisper.

**Example  7**
Locating the Foci of a Whispering Chamber The Statuary Hall in the Capitol Building in Washington, D.C. is a whispering chamber. Its dimensions are 46 feet wide by 96 feet long as shown in Figure 13. a. What is the standard form of the equation of the ellipse representing the outline of the room? Hint: assume a horizontal ellipse, and let the center of the room be the point (0, 0). b. If two senators standing at the foci of this room can hear each other whisper, how far apart are the senators? Round to the nearest foot. 96 feet 46 feet


**Solution**
a. We are assuming a horizontal ellipse with center (0, 0), so we need to find an equation of the form  x 2

_ a^{2}  +  y 2

_ b^{2}  = 1, where a > b. We know that the length of the major axis, 2a, is longer than the length of the minor axis, 2b. So the length of the room, 96, is represented by the major axis, and the width of the room, 46, is represented by the minor axis. • Solving for a, we have 2a = 96, so a = 48, and a^{2} = 2304. • Solving for b, we have 2b = 46, so b = 23, and b^{2} = 529. Therefore, the equation of the ellipse is  x 2 _ 2304  +  y 2

_ b. To find the distance between the senators, we must find the distance between the foci, (\pm c, 0), where c^{2} = a^{2} - b^{2}. Solving for c, we have:

c^{2} = a^{2} - b^{2}

Substitute using the values found in part (a).

c = \pm  \sqrt{Take} the square root of both sides.

c = \pm  \sqrt{Subtract.}

c ≈ \pm  42 Round to the nearest foot. The points (\pm 42, 0) represent the foci. Thus, the distance between the senators is 2(42) = 84 feet.

**Try It #7**
Suppose a whispering chamber is 480 feet long and 320 feet wide. a. What is the standard form of the equation of the ellipse representing the room? Hint: assume a horizontal ellipse, and let the center of the room be the point (0, 0). b. If two people are standing at the foci of this room and can hear each other whisper, how far apart are the people? Round to the nearest foot. Access these online resources for additional instruction and practice with ellipses. • Conic Sections: The Ellipse (http://openstaxcollege.org/l/conicellipse) • Graph an Ellipse with Center at the Origin (http://openstaxcollege.org/l/grphellorigin) • Graph an Ellipse with Center Not at the Origin (http://openstaxcollege.org/l/grphellnot)


## 10.1 Section Exercises

### 10.1 Section Exercises
Verbal 1. Define an ellipse in terms of its foci. 2. Where must the foci of an ellipse lie? 3. What special case of the ellipse do we have when the major and minor axis are of the same length? 4. For the special case mentioned in the previous question, what would be true about the foci of that ellipse? 5. What can be said about the symmetry of the graph of an ellipse with center at the origin and foci along the y-axis? Algebraic For the following exercises, determine whether the given equations represent ellipses. If yes, write in standard form. 6. 2x 2 + y = 4 For the following exercises, write the equation of an ellipse in standard form, and identify the end points of the major and minor axes as well as the foci.

_ 4  +  y 2

_ _ 100  +  y 2

_ _______  +  (y - 4)^{2} _______  = 1 _  +  (y + 1)^{2} _  = 1 _  +  (y - 7)^{2} _  = 1 _______  +  (y - 7)^{2} _______  = 1 For the following exercises, find the foci for the given ellipses. _  +  (y + 1)^{2} _  = 1 _  +  (y - 2)^{2} _  = 1 30. x 2 + 4y 2 + 4x + 8y = 1 Graphical For the following exercises, graph the given ellipses, noting center, vertices, and foci.

_ 25  +  y 2

_

_ 16  +  y 2

_ 9  = 1 _  +  (y - 4)^{2} _  = 1 _  +  (y - 3)^{2} _  = 1

_ 2  +  (y + 1)^{2} _  = 1 For the following exercises, use the given information about the graph of each ellipse to determine its equation. 46. Center at the origin, symmetric with respect to the x- and y-axes, focus at (4, 0), and point on graph (0, 3). 47. Center at the origin, symmetric with respect to the x- and y-axes, focus at (0, -2), and point on graph

48. Center at the origin, symmetric with respect to the x- and y-axes, focus at (3, 0), and major axis is twice as long as minor axis. 49. Center (4, 2); vertex (9, 2); one focus: (4 + 2 \sqrt{50.} Center (3, 5); vertex (3, 11); one focus: (3, 5 + 4\sqrt{2} ) 51. Center (-3, 4); vertex (1, 4); one focus: (-3 + 2\sqrt{For} the following exercises, given the graph of the ellipse, determine its equation. y x y x x y y x Extensions For the following exercises, find the area of the ellipse. The area of an ellipse is given by the formula Area = a ⋅ b ⋅ \pi . _  +  (y - 3)^{2} _  = 1 _  +  (y - 6)^{2} _  = 1 _  +  (y - 2)^{2} _  = 1 Real-World Applications 62. Find the equation of the ellipse that will just fit inside a box that is 8 units wide and 4 units high. 63. Find the equation of the ellipse that will just fit inside a box that is four times as wide as it is high. Express in terms of h, the height. 64. An arch has the shape of a semi-ellipse (the top half of an ellipse). The arch has a height of 8 feet and a span of 20 feet. Find an equation for the ellipse, and use that to find the height to the nearest 0.01 foot of the arch at a distance of 4 feet from the center. 65. An arch has the shape of a semi-ellipse. The arch has a height of 12 feet and a span of 40 feet. Find an equation for the ellipse, and use that to find the distance from the center to a point at which the height is 6 feet. Round to the nearest hundredth. 66. A bridge is to be built in the shape of a semi- elliptical arch and is to have a span of 120 feet. The height of the arch at a distance of 40 feet from the center is to be 8 feet. Find the height of the arch at its center. 67. A person in a whispering gallery standing at one focus of the ellipse can whisper and be heard by a person standing at the other focus because all the sound waves that reach the ceiling are reflected to the other person. If a whispering gallery has a length of 120 feet, and the foci are located 30 feet from the center, find the height of the ceiling at the center. 68. A person is standing 8 feet from the nearest wall in a whispering gallery. If that person is at one focus, and the other focus is 80 feet away, what is the length and height at the center of the gallery? y x


## 10.2 The Hyperbola
Learning Objectives
In this section, you will:
• Locate a hyperbola’s vertices and foci.
• Write equations of hyperbolas in standard form.
• Graph hyperbolas centered at the origin.
• Graph hyperbolas not centered at the origin.
• Solve applied problems involving hyperbolas.
10. 2 The Hyperbola What do paths of comets, supersonic booms, ancient Grecian pillars, and natural draft cooling towers have in common? They can all be modeled by the same type of conic. For instance, when something moves faster than the speed of sound, a shock wave in the form of a cone is created. A portion of a conic is formed when the wave intersects the ground, resulting in a sonic boom. See Figure 1. Wake created from shock wave Portion of a hyperbola A shock wave intersecting the ground forms a portion of a conic and results in a sonic boom. Most people are familiar with the sonic boom created by supersonic aircraft, but humans were breaking the sound barrier long before the first supersonic flight. The crack of a whip occurs because the tip is exceeding the speed of sound. The bullets shot from many firearms also break the sound barrier, although the bang of the gun usually supersedes the sound of the sonic boom. Locating the Vertices and Foci of a Hyperbola In analytic geometry, a hyperbola is a conic section formed by intersecting a right circular cone with a plane at an angle such that both halves of the cone are intersected. This intersection produces two separate unbounded curves that are mirror images of each other. See Figure 2. Like the ellipse, the hyperbola can also be defined as a set of points in the coordinate plane. A hyperbola is the set of all points (x, y) in a plane such that the difference of the distances between (x, y) and the foci is a positive constant.

Notice that the definition of a hyperbola is very similar to that of an ellipse. The distinction is that the hyperbola is defined in terms of the difference of two distances, whereas the ellipse is defined in terms of the sum of two distances. As with the ellipse, every hyperbola has two axes of symmetry. The transverse axis is a line segment that passes through the center of the hyperbola and has vertices as its endpoints. The foci lie on the line that contains the transverse axis. The conjugate axis is perpendicular to the transverse axis and has the co-vertices as its endpoints. The center of a hyperbola is the midpoint of both the transverse and conjugate axes, where they intersect. Every hyperbola also has two asymptotes that pass through its center. As a hyperbola recedes from the center, its branches approach these asymptotes. The central rectangle of the hyperbola is centered at the origin with sides that pass through each vertex and co-vertex; it is a useful tool for graphing the hyperbola and its asymptotes. To sketch the asymptotes of the hyperbola, simply sketch and extend the diagonals of the central rectangle. See Figure 3. Conjugate axis Transverse axis Co-vertex y x Co-vertex Vertex Vertex Focus Focus Center Asymptote Asymptote Key features of the hyperbola In this section, we will limit our discussion to hyperbolas that are positioned vertically or horizontally in the coordinate plane; the axes will either lie on or be parallel to the x- and y-axes. We will consider two cases: those that are centered at the origin, and those that are centered at a point other than the origin. Deriving the Equation of an Ellipse Centered at the Origin Let (-c, 0) and (c, 0) be the foci of a hyperbola centered at the origin. The hyperbola is the set of all points (x, y) such that the difference of the distances from (x, y) to the foci is constant. See Figure 4. (–c, 0) (–a, 0) (a, 0) (c, 0) (x, y) y d^{2} d^{1} x If (a, 0) is a vertex of the hyperbola, the distance from (-c, 0) to (a, 0) is a - (-c) = a + c. The distance from (c, 0) to (a, 0) is c - a. The sum of the distances from the foci to the vertex is

(a + c) - (c - a) = 2a

If (x, y) is a point on the hyperbola, we can define the following variables: d^{2} = the distance from (-c, 0) to (x, y)

d^{1} = the distance from (c, 0) to (x, y) By definition of a hyperbola, d^{2} - d^{1} is constant for any point (x, y) on the hyperbola. We know that the difference of these distances is 2a for the vertex (a, 0). It follows that d^{2} - d^{1} = 2a for any point on the hyperbola. As with the derivation of the equation of an ellipse, we will begin by applying the distance formula. The rest of the derivation is algebraic. Compare this derivation with the one from the previous section for ellipses.

d^{2} - d^{1} = \sqrt{—}

(x - ( - c))^{2} + (y - 0)^{2}  - \sqrt{(x} - c)^{2} + (y - 0)^{2}  = 2a Distance formula \sqrt{(x} + c)^{2} + y 2  - \sqrt{(x} - c)^{2} + y 2  = 2a Simplify expressions.

\sqrt{(x} + c)^{2} + y 2  = 2a + \sqrt{(x} - c)^{2} + y 2  Move radical to opposite side.

(x + c)^{2} + y 2 = (2a + \sqrt{(x} - c)^{2} + y 2  ) Square both sides.

x 2 + 2cx + c^{2} + y 2 = 4a^{2} + 4a \sqrt{(x} - c)^{2} + y 2  + (x - c)^{2} + y 2 Expand the squares.

x 2 + 2cx + c^{2} + y 2 = 4a^{2} + 4a \sqrt{(x} - c)^{2} + y 2  + x 2 - 2cx + c^{2} + y 2 Expand remaining square.

2cx = 4a^{2} + 4a \sqrt{(x} - c)^{2} + y 2  - 2cx Combine like terms.

4cx - 4a^{2} = 4a \sqrt{(x} - c)^{2} + y 2  Isolate the radical.

cx - a^{2} = a \sqrt{(x} - c)^{2} + y 2  Divide by 4.

(cx - a^{2})^{2} = a^{2}  \sqrt{(x} - c)^{2} + y 2    Square both sides.

c^{2} x 2 - 2a^{2} cx + a^{4} = a^{2}(x 2 - 2cx + c^{2} + y 2) Expand the squares.

c^{2} x 2 - 2a^{2} cx + a^{4} = a^{2} x 2 - 2a^{2} cx + a^{2} c^{2} + a^{2} y 2 Distribute a^{2}.

a^{4} + c^{2} x 2 = a^{2} x 2 + a^{2} c^{2} + a^{2} y 2 Combine like terms.

c^{2} x 2 - a^{2} x 2 - a^{2} y 2 = a^{2} c^{2} - a^{4} Rearrange terms.

x 2 (c^{2} - a^{2}) - a^{2} y 2 = a^{2} (c^{2} - a^{2}) Factor common terms

x 2 b^{2} - a^{2} y 2 = a^{2} b^{2} Set b^{2} = c^{2} - a^{2}.

 x 2b^{2} ____ a^{2}b^{2}  -  a^{2}y 2 ____ a^{2}b^{2}  =  a^{2}b^{2} ____ a^{2}b^{2}  Divide both sides by a^{2}b^{2}.

 x 2

_ a^{2}  -  y 2

_ b^{2}  = 1 This equation defines a hyperbola centered at the origin with vertices (\pm a, 0) and co-vertices (0 \pm  b). standard forms of the equation of a hyperbola with center (0, 0) The standard form of the equation of a hyperbola with center (0, 0) and major axis on the x-axis is  x 2

_ a^{2}  -  y 2

_ b^{2}  = 1 where • the length of the transverse axis is 2a • the coordinates of the vertices are (\pm a, 0) • the length of the conjugate axis is 2b • the coordinates of the co-vertices are (0, \pm b) • the distance between the foci is 2c, where c^{2} = a^{2} + b^{2} • the coordinates of the foci are (\pm c, 0) • the equations of the asymptotes are y = \pm   b __ a  x

See Figure 5a. The standard form of the equation of a hyperbola with center (0, 0) and transverse axis on the y-axis is  y 2

_ a^{2}  -  x 2

_ b^{2}  = 1 where • the length of the transverse axis is 2a • the coordinates of the vertices are (0, \pm  a) • the length of the conjugate axis is 2b • the coordinates of the co-vertices are (\pm b, 0) • the distance between the foci is 2c, where c^{2} = a^{2} + b^{2} • the coordinates of the foci are (0, \pm  c) • the equations of the asymptotes are y = \pm  a _ b x See Figure 5b. Note that the vertices, co-vertices, and foci are related by the equation c^{2} = a^{2} + b^{2}. When we are given the equation of a hyperbola, we can use this relationship to identify its vertices and foci. (-c, 0) (a, 0) (-a, 0) (0, b) (0, -b) (0, -c) (0, a) (0, -a) (0, c ) (b, 0) (-b, 0) y x y (c, 0) y = a b x y = - a b x y = b a x y = - b a x x (a) (b) (a) Horizontal hyperbola with center (0, 0) (b) Vertical hyperbola with center (0, 0)

**How To…**
Given the equation of a hyperbola in standard form, locate its vertices and foci. 1. Determine whether the transverse axis lies on the x- or y-axis. Notice that a^{2} is always under the variable with the positive coefficient. So, if you set the other variable equal to zero, you can easily find the intercepts. In the case where the hyperbola is centered at the origin, the intercepts coincide with the vertices.

a. If the equation has the form  x 2

_ a^{2}  -  y 2

_ b^{2}  = 1, then the transverse axis lies on the x-axis. The vertices are located at ( \pm  a, 0), and the foci are located at (\pm  c, 0).

b. If the equation has the form  y 2

_ a^{2}  -  x 2

_ b^{2}  = 1, then the transverse axis lies on the y-axis. The vertices are located at (0, \pm  a), and the foci are located at (0, \pm  c). 2. Solve for a using the equation a = \sqrt{a^{2}} . 3. Solve for c using the equation c = \sqrt{a^{2}} + b^{2}. 


**Example  1**
Locating a Hyperbola’s Vertices and Foci Identify the vertices and foci of the hyperbola with equation  y 2

_ 49  -  x 2

_ Solution The equation has the form  y 2

_ a^{2}  -  x 2

_ b^{2}  = 1, so the transverse axis lies on the y-axis. The hyperbola is centered at the origin, so the vertices serve as the y-intercepts of the graph. To find the vertices, set x = 0, and solve for y.

1 =  y 2

_ 49  -  x 2

_ 32 

1 =  y 2

_

_ 32 

1 =  y 2

_ 49 

y = \pm  \sqrt{49}  = \pm  7 The foci are located at (0, \pm  c). Solving for c,

c = \sqrt{a^{2}} + b^{2}  = \sqrt{49} + 32  = \sqrt{Therefore,} the vertices are located at (0, \pm  7), and the foci are located at (0, 9).

**Try It #1**
Identify the vertices and foci of the hyperbola with equation  x 2

_ 9  -  y 2

_ Writing Equations of Hyperbolas in Standard Form Just as with ellipses, writing the equation for a hyperbola in standard form allows us to calculate the key features: its center, vertices, co-vertices, foci, asymptotes, and the lengths and positions of the transverse and conjugate axes. Conversely, an equation for a hyperbola can be found given its key features. We begin by finding standard equations for hyperbolas centered at the origin. Then we will turn our attention to finding standard equations for hyperbolas centered at some point other than the origin. Hyperbolas Centered at the Origin Reviewing the standard forms given for hyperbolas centered at (0, 0), we see that the vertices, co-vertices, and foci are related by the equation c^{2} = a^{2} + b^{2}. Note that this equation can also be rewritten as b^{2} = c^{2} - a^{2}. This relationship is used to write the equation for a hyperbola when given the coordinates of its foci and vertices.

**How To…**
Given the vertices and foci of a hyperbola centered at (0, 0), write its equation in standard form. 1. Determine whether the transverse axis lies on the x- or y-axis. a. If the given coordinates of the vertices and foci have the form (\pm  a, 0) and (\pm  c, 0), respectively, then the transverse axis is the x-axis. Use the standard form  x 2

_ a^{2}  -  y 2

_ b^{2}  = 1. b. If the given coordinates of the vertices and foci have the form (0, \pm  a) and (0, \pm  c), respectively, then the transverse axis is the y-axis. Use the standard form  y 2

_ a^{2}  -  x 2

_ b^{2}  = 1. 2. Find b^{2} using the equation b^{2} = c^{2} - a^{2}. 3. Substitute the values for a^{2} and b^{2} into the standard form of the equation determined in Step 1.


**Example  2**
Finding the Equation of a Hyperbola Centered at (0, 0) Given its Foci and Vertices What is the standard form equation of the hyperbola that has vertices (\pm 6, 0) and foci (\pm 2\sqrt{Solution} The vertices and foci are on the x-axis. Thus, the equation for the hyperbola will have the form  x 2

_ a^{2}  -  y 2

_ b^{2}  = 1. The vertices are (\pm 6, 0), so a = 6 and a^{2} = 36. The foci are (\pm 2\sqrt{10} , 0), so c = 2\sqrt{Solving} for b^{2}, we have

b^{2} = c^{2} - a^{2}

Substitute for c^{2} and a^{2}.

b^{2} = 4 Subtract. Finally, we substitute a^{2} = 36 and b^{2} = 4 into the standard form of the equation,  x 2

_ a^{2}  -  y 2

_ b^{2}  = 1. The equation of the hyperbola is  x 2

_ 36  -  y 2

_ 4  = 1, as shown in Figure 6.

**Try It #2**
What is the standard form equation of the hyperbola that has vertices (0, \pm  2) and foci (0, \pm  2\sqrt{5}  )? Hyperbolas Not Centered at the Origin Like the graphs for other equations, the graph of a hyperbola can be translated. If a hyperbola is translated h units horizontally and k units vertically, the center of the hyperbola will be (h, k). This translation results in the standard form of the equation we saw previously, with x replaced by (x - h) and y replaced by (y - k). standard forms of the equation of a hyperbola with center (h, k) The standard form of the equation of a hyperbola with center (h, k) and transverse axis parallel to the x-axis is  (x - h)^{2} _ a^{2}  -  (y - k)^{2} _ b^{2}  = 1 where • the length of the transverse axis is 2a • the coordinates of the vertices are (h \pm  a, k) • the length of the conjugate axis is 2b • the coordinates of the co-vertices are (h, k \pm  b) • the distance between the foci is 2c, where c 2 = a 2 + b 2 • the coordinates of the foci are (h \pm  c, k) y x

The asymptotes of the hyperbola coincide with the diagonals of the central rectangle. The length of the rectangle is 2a and its width is 2b. The slopes of the diagonals are \pm   b __ a , and each diagonal passes through the center (h, k). Using the point-slope formula, it is simple to show that the equations of the asymptotes are y = \pm   b __ a (x - h) + k. See Figure 7a. The standard form of the equation of a hyperbola with center (h, k) and transverse axis parallel to the y-axis is  (y - k)^{2} _ a^{2}  -  (x - h)^{2} _ b^{2}  = 1 where • the length of the transverse axis is 2a • the coordinates of the vertices are (h, k \pm  a) • the length of the conjugate axis is 2b • the coordinates of the co-vertices are (h \pm  b, k) • the distance between the foci is 2c, where c 2 = a 2 + b 2 • the coordinates of the foci are (h, k \pm  c) Using the reasoning above, the equations of the asymptotes are y = \pm  a __ b (x - h) + k. See Figure 7b. y = a (x - h) + k b y = - a (x - h) + k b y = - b (x - h) + k a y = b (x - h) + k a (h, k - b) (h, k + b) (h, k - c) (h, k + c) (h - b, k) (h + b, k) (h - a, k) (h + a, k) (h, k - a) (h, k + a) (h - c, k) (h + c, k) (h, k) (h, k) y y x x (a) (b) Like hyperbolas centered at the origin, hyperbolas centered at a point (h, k) have vertices, co-vertices, and foci that are related by the equation c^{2} = a^{2} + b^{2}. We can use this relationship along with the midpoint and distance formulas to find the standard equation of a hyperbola when the vertices and foci are given.

**How To…**
Given the vertices and foci of a hyperbola centered at (h, k), write its equation in standard form. 1. Determine whether the transverse axis is parallel to the x- or y-axis. a. If the y-coordinates of the given vertices and foci are the same, then the transverse axis is parallel to the x-axis. Use the standard form  (x - h)^{2} _ a^{2}  -  (y - k)^{2} _ b^{2}  = 1. b. If the x-coordinates of the given vertices and foci are the same, then the transverse axis is parallel to the y-axis. Use the standard form  (y - k)^{2} _ a^{2}  -  (x - h)^{2} _ b^{2}  = 1. 2. Identify the center of the hyperbola, (h, k), using the midpoint formula and the given coordinates for the vertices.

3. Find a^{2} by solving for the length of the transverse axis, 2a, which is the distance between the given vertices. 4. Find c^{2} using h and k found in Step 2 along with the given coordinates for the foci. 5. Solve for b^{2} using the equation b^{2} = c^{2} - a^{2}. 6. Substitute the values for h, k, a^{2}, and b^{2} into the standard form of the equation determined in Step 1.

**Example  3**
Finding the Equation of a Hyperbola Centered at (h, k) Given its Foci and Vertices What is the standard form equation of the hyperbola that has vertices at (0, -2) and (6, -2) and foci at (-2, -2) and Solution The y-coordinates of the vertices and foci are the same, so the transverse axis is parallel to the x-axis. Thus, the equation of the hyperbola will have the form

 (x - h)^{2} _ a^{2}  -  (y - k)^{2} _ b^{2}  = 1 First, we identify the center, (h, k). The center is halfway between the vertices (0, -2) and (6, -2). Applying the midpoint formula, we have

(h, k) =   0 + 6 _____ ,  -2 + (-2) _________    = (3, -2) Next, we find a^{2}. The length of the transverse axis, 2a, is bounded by the vertices. So, we can find a^{2} by finding the distance between the x-coordinates of the vertices.

2a = | 0 - 6 |

2a = 6

a = 3

a^{2} = 9 Now we need to find c^{2}. The coordinates of the foci are (h \pm  c, k). So (h - c, k) = (-2, -2) and (h + c, k) = (8, -2). We can use the x-coordinate from either of these points to solve for c. Using the point (8, -2), and substituting h = 3,

h + c = 8

3 + c = 8

c = 5

Next, solve for b^{2} using the equation b^{2} = c^{2} - a^{2} :

b^{2} = c^{2} - a^{2}

= 16 Finally, substitute the values found for h, k, a^{2}, and b^{2} into the standard form of the equation.

 (x - 3)^{2} _  -  (y + 2)^{2} _  = 1

**Try It #3**
What is the standard form equation of the hyperbola that has vertices (1, -2) and (1, 8) and foci (1, -10) and (1, 16)? Graphing Hyperbolas Centered at the Origin When we have an equation in standard form for a hyperbola centered at the origin, we can interpret its parts to identify the key features of its graph: the center, vertices, co-vertices, asymptotes, foci, and lengths and positions of the transverse and conjugate axes. To graph hyperbolas centered at the origin, we use the standard form  x 2

_ a^{2}  -  y 2

_ b^{2}  = 1 for horizontal hyperbolas and the standard form  y 2

_ a^{2}  -  x 2

_ b^{2}  = 1 for vertical hyperbolas.


**How To…**
Given a standard form equation for a hyperbola centered at (0, 0), sketch the graph. 1. Determine which of the standard forms applies to the given equation. 2. Use the standard form identified in Step 1 to determine the position of the transverse axis; coordinates for the vertices, co-vertices, and foci; and the equations for the asymptotes. a. If the equation is in the form  x 2

_ a^{2}  -  y 2

_ b^{2}  = 1, then • the transverse axis is on the x-axis • the coordinates of the vertices are (\pm a, 0) • the coordinates of the co-vertices are (0, \pm  b) • the coordinates of the foci are (\pm c, 0) • the equations of the asymptotes are y = \pm   b _ a x b. If the equation is in the form  y 2

_ a^{2}  -  x 2

_ b^{2}  = 1, then • the transverse axis is on the y-axis • the coordinates of the vertices are (0, \pm  a) • the coordinates of the co-vertices are (\pm b, 0) • the coordinates of the foci are (0, \pm  c) • the equations of the asymptotes are y = \pm  a __ b x 3. Solve for the coordinates of the foci using the equation c = \pm  \sqrt{a^{2}} + b^{2} . 4. Plot the vertices, co-vertices, foci, and asymptotes in the coordinate plane, and draw a smooth curve to form the hyperbola.

**Example  4**

### Graphing a Hyperbola Centered at (0, 0) Given an Equation in Standard Form
Graph the hyperbola given by the equation  y 2

_ 64  -  x 2

_ 36  = 1. Identify and label the vertices, co-vertices, foci, and asymptotes. Solution The standard form that applies to the given equation is  y 2

_ a^{2}  -  x 2

_ b^{2}  = 1. Thus, the transverse axis is on the y-axis The coordinates of the vertices are (0, \pm  a) = (0, \pm  \sqrt{64} ) = (0, \pm  8) The coordinates of the co-vertices are (\pm b, 0) = (\pm  \sqrt{The} coordinates of the foci are (0, \pm  c), where c = \pm  \sqrt{a^{2}} + b^{2} . Solving for c, we have c = \pm  \sqrt{a^{2}} + b^{2}  = \pm  \sqrt{64} + 36  = \pm  \sqrt{Therefore,} the coordinates of the foci are (0, \pm  10) The equations of the asymptotes are y = \pm  a __ b x = \pm  8 __ 6 x = \pm  4 __ 3 x Plot and label the vertices and co-vertices, and then sketch the central rectangle. Sides of the rectangle are parallel to the axes and pass through the vertices and co-vertices. Sketch and extend the diagonals of the central rectangle to show the asymptotes. The central rectangle and asymptotes provide the framework needed to sketch an accurate graph of the hyperbola. Label the foci and asymptotes, and draw a smooth curve to form the hyperbola, as shown in Figure 8.

y = 4 x y = - 4 x y y x x

**Try It #4**
Graph the hyperbola given by the equation  x 2 _ 144  -  y 2

_ 81  = 1. Identify and label the vertices, co-vertices, foci, and asymptotes. Graphing Hyperbolas Not Centered at the Origin Graphing hyperbolas centered at a point (h, k) other than the origin is similar to graphing ellipses centered at a point other than the origin. We use the standard forms  (x - h)^{2} _ a^{2}  -  (y - k)^{2} _ b^{2}  = 1 for horizontal hyperbolas, and  (y - k)^{2} _ a^{2}  -  (x - h)^{2} _ b^{2}  = 1 for vertical hyperbolas. From these standard form equations we can easily calculate and plot key features of the graph: the coordinates of its center, vertices, co-vertices, and foci; the equations of its asymptotes; and the positions of the transverse and conjugate axes.

**How To…**
Given a general form for a hyperbola centered at (h, k), sketch the graph. 1. Determine which of the standard forms applies to the given equation. Convert the general form to that standard form. 2. Use the standard form identified in Step 1 to determine the position of the transverse axis; coordinates for the center, vertices, co-vertices, foci; and equations for the asymptotes. a. If the equation is in the form  (x - h)^{2} _ a^{2}  -  (y - k)^{2} _ b^{2}  = 1, then • the transverse axis is parallel to the x-axis • the center is (h, k) • the coordinates of the vertices are (h \pm  a, k) • the coordinates of the co-vertices are (h, k \pm  b) • the coordinates of the foci are (h \pm  c, k) • the equations of the asymptotes are y = \pm   b __ a (x - h) + k

b. If the equation is in the form  (y - k)^{2} _______ a^{2}  -  (x - h)^{2} _______ b^{2}  = 1, then • the transverse axis is parallel to the y-axis • the center is (h, k) • the coordinates of the vertices are (h, k \pm  a) • the coordinates of the co-vertices are (h \pm  b, k) • the coordinates of the foci are (h, k \pm  c) • the equations of the asymptotes are y = \pm  a _ b (x - h) + k 3. Solve for the coordinates of the foci using the equation c = \pm  \sqrt{a^{2}} + b^{2} . 4. Plot the center, vertices, co-vertices, foci, and asymptotes in the coordinate plane and draw a smooth curve to form the hyperbola.

**Example  5**

### Graphing a Hyperbola Centered at (h, k) Given an Equation in General Form
Graph the hyperbola given by the equation 9x 2 - 4y 2 - 36x - 40y - 388 = 0. Identify and label the center, vertices, co-vertices, foci, and asymptotes. Solution Start by expressing the equation in standard form. Group terms that contain the same variable, and move the constant to the opposite side of the equation.

(9x 2 - 36x) - (4y 2 + 40y) = 388 Factor the leading coefficient of each expression.

9(x 2 - 4x) - 4(y 2 + 10y) = 388 Complete the square twice. Remember to balance the equation by adding the same constants to each side.

Rewrite as perfect squares.

9(x - 2)^{2} - 4(y + 5)^{2} = 324 Divide both sides by the constant term to place the equation in standard form.

 (x - 2)^{2} _  -  (y + 5)^{2} _  = 1 The standard form that applies to the given equation is  (x - h)^{2} _ a^{2}  -  (y - k)^{2} _ b^{2}  = 1, where a^{2} = 36 and b^{2} = 81, or a = 6 and b = 9. Thus, the transverse axis is parallel to the x-axis. It follows that: • the center of the ellipse is (h, k) = (2, -5) • the coordinates of the vertices are (h \pm  a, k) = (2 \pm  6, -5), or (-4, -5) and (8, -5) • the coordinates of the co-vertices are (h, k \pm  b) = (2, - 5 \pm  9), or (2, - 14) and (2, 4) • the coordinates of the foci are (h \pm  c, k), where c = \pm  \sqrt{a^{2}} + b 2 . Solving for c, we have c = \pm  \sqrt{36} + 81  = \pm  \sqrt{117}  = \pm  3\sqrt{13}  Therefore, the coordinates of the foci are (2 - 3\sqrt{13} , -5) and (2 + 3\sqrt{The} equations of the asymptotes are y = \pm   b __ a (x - h) + k = \pm   3 __ 2 (x - 2) - 5. Next, we plot and label the center, vertices, co-vertices, foci, and asymptotes and draw smooth curves to form the hyperbola, as shown in Figure 9.


**Try It #5**
Graph the hyperbola given by the standard form of an equation  (y + 4)^{2} _  -  (x - 3)^{2} _  = 1. Identify and label the center, vertices, co-vertices, foci, and asymptotes. Solving Applied Problems Involving Hyperbolas As we discussed at the beginning of this section, hyperbolas have real-world applications in many fields, such as astronomy, physics, engineering, and architecture. The design efficiency of hyperbolic cooling towers is particularly interesting. Cooling towers are used to transfer waste heat to the atmosphere and are often touted for their ability to generate power efficiently. Because of their hyperbolic form, these structures are able to withstand extreme winds while requiring less material than any other forms of their size and strength. See Figure 10. For example, a 500-foot tower can be made of a reinforced concrete shell only 6 or 8 inches wide! The first hyperbolic towers were designed in 1914 and were 35 meters high. Today, the tallest cooling towers are in France, standing a remarkable 170 meters tall. In Example 6 we will use the design layout of a cooling tower to find a hyperbolic equation that models its sides. y x


**Example  6**

### Solving Applied Problems Involving Hyperbolas
The design layout of a cooling tower is shown in Figure 11. The tower stands 179.6 meters tall. The diameter of the top is 72 meters. At their closest, the sides of the tower are 60 meters apart. Find the equation of the hyperbola that models the sides of the cooling tower. Assume that the center of the hyperbola— indicated by the intersection of dashed perpendicular lines in the figure—is the origin of the coordinate plane. Round final values to four decimal places. Solution We are assuming the center of the tower is at the origin, so we can use the standard form of a horizontal hyperbola centered at the origin:  x 2

_ a^{2}  -  y 2

_ b^{2}  = 1, where the branches of the hyperbola form the sides of the cooling tower. We must find the values of a^{2} and b^{2} to complete the model. First, we find a^{2}. Recall that the length of the transverse axis of a hyperbola is 2a. This length is represented by the distance where the sides are closest, which is given as 65.3 meters. So, 2a = 60. Therefore, a = 30 and a^{2} = 900. To solve for b^{2}, we need to substitute for x and y in our equation using a known point. To do this, we can use the dimensions of the tower to find some point (x, y) that lies on the hyperbola. We will use the top right corner of the tower to represent that point. Since the y-axis bisects the tower, our x-value can be represented by the radius of the top, or 36 meters. The y-value is represented by the distance from the origin to the top, which is given as 79.6 meters. Therefore,

 x 2

_ a^{2}  -  y 2

_ b^{2}  = 1 Standard form of horizontal hyperbola.

b^{2} =  y 2 _  x 2

_ a^{2}  - 1  Isolate b^{2}

_ ____  Substitute for a^{2}, x, and y

Round to four decimal places The sides of the tower can be modeled by the hyperbolic equation

 x 2 _ 900  -  y 2 _ _ 302  -  y 2 _ 72 m 60 m


**Try It #6**
A design for a cooling tower project is shown in Figure 12. Find the equation of the hyperbola that models the sides of the cooling tower. Assume that the center of the hyperbola—indicated by the intersection of dashed perpendicular lines in the figure—is the origin of the coordinate plane. Round final values to four decimal places. Access these online resources for additional instruction and practice with hyperbolas. • Conic Sections: The Hyperbola Part 1 of 2 (http://openstaxcollege.org/l/hyperbola^{1}) • Conic Sections: The Hyperbola Part 2 of 2 (http://openstaxcollege.org/l/hyperbola^{2}) • Graph a Hyperbola with Center at Origin (http://openstaxcollege.org/l/hyperbolaorigin) • Graph a Hyperbola with Center not at Origin (http://openstaxcollege.org/l/hbnotorigin) 60 m 40 m


## 10.2 Section Exercises

### 10.2 Section Exercises
Verbal 1. Define a hyperbola in terms of its foci. 2. What can we conclude about a hyperbola if its asymptotes intersect at the origin? 3. What must be true of the foci of a hyperbola? 4. If the transverse axis of a hyperbola is vertical, what do we know about the graph? 5. Where must the center of hyperbola be relative to its foci? Algebraic For the following exercises, determine whether the following equations represent hyperbolas. If so, write in standard form.

___ 36  -  y 2

__ 9  = 1 10. -9x 2 + 18x + y 2 + 4y - 14 = 0 For the following exercises, write the equation for the hyperbola in standard form if it is not already, and identify the vertices and foci, and write equations of asymptotes.

___ 25  -  y 2

___ ___ 100  -  y 2

__ 9  = 1

__ 4  -  x 2

___ _______  -  (y - 2)^{2} _______  = 1 _______  -  (x + 1)^{2} _______  = 1 _______  -  (y + 7)^{2} _______  = 1 For the following exercises, find the equations of the asymptotes for each hyperbola.

__ 32  -  x 2

__ _______  -  (y + 4)^{2} _______  = 1 _______  -  (x + 5)^{2} _______  = 1 Graphical For the following exercises, sketch a graph of the hyperbola, labeling vertices and foci.

___ 49  -  y 2

___

___ 64  -  y 2

__ 4  = 1

__ 9  -  x 2

___ _______  -  (x - 4)^{2} _______  = 1 _______  -  (y + 3)^{2} _______  = 1 _______  -  (x - 3)^{2} _______  = 1

40. -x 2 + 8x + 4y 2 - 40y + 88 = 0 For the following exercises, given information about the graph of the hyperbola, find its equation. 45. Vertices at (3, 0) and (-3, 0) and one focus at (5, 0). 46. Vertices at (0, 6) and (0, -6) and one focus at 47. Vertices at (1, 1) and (11, 1) and one focus at (12, 1). 48. Center: (0, 0); vertex: (0, -13); one focus: (0, \sqrt{49.} Center: (4, 2); vertex: (9, 2); one focus: (4 + \sqrt{50.} Center: (3, 5); vertex: (3, 11); one focus: (3, 5 + 2\sqrt{For} the following exercises, given the graph of the hyperbola, find its equation. x y Vertices Center Foci Foci y x Foci Vertices Foci y x Center Foci Foci Vertices Center y Vertices Foci Foci Center y x

Extensions For the following exercises, express the equation for the hyperbola as two functions, with y as a function of x. Express as simply as possible. Use a graphing calculator to sketch the graph of the two functions on the same axes.

_ 4  -  y 2

_ 9  = 1

_ 9  -  x 2

_ 1  = 1 _  -  (y + 3)^{2} _  = 1 59. -4x 2 - 16x + y 2 - 2y - 19 = 0 Real-World Applications For the following exercises, a hedge is to be constructed in the shape of a hyperbola near a fountain at the center of the yard. Find the equation of the hyperbola and sketch the graph. 61. The hedge will follow the asymptotes y = x and y = -x, and its closest distance to the center fountain is 5 yards. 62. The hedge will follow the asymptotes y = 2x and y = -2x, and its closest distance to the center fountain is 6 yards. 63. The hedge will follow the asymptotes y =  1 __ 2 x and y = - 1 __ 2 x, and its closest distance to the center fountain is 10 yards. 64. The hedge will follow the asymptotes y =  2 __ 3 x and y = - 2 __ 3 x, and its closest distance to the center fountain is 12 yards. 65. The hedge will follow the asymptotes y =  3 __ 4 x and y = - 3 __ 4 x, and its closest distance to the center fountain is 20 yards. For the following exercises, assume an object enters our solar system and we want to graph its path on a coordinate system with the sun at the origin and the x-axis as the axis of symmetry for the object's path. Give the equation of the flight path of each object using the given information. 66. The object enters along a path approximated by the line y = x - 2 and passes within 1 au (astronomical unit) of the sun at its closest approach, so that the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = -x + 2. 67. The object enters along a path approximated by the line y = 2x - 2 and passes within 0.5 au of the sun at its closest approach, so the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = -2x + 2. 68. The object enters along a path approximated by the line y = 0.5x + 2 and passes within 1 au of the sun at its closest approach, so the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = -0.5x - 2. 69. The object enters along a path approximated by the line y =  1 __ 3 x - 1 and passes within 1 au of the sun at its closest approach, so the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = - 1 __ 3 x + 1. 70. The object enters along a path approximated by the line y = 3x - 9 and passes within 1 au of the sun at its closest approach, so the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = -3x + 9.

Learning Objectives
In this section, you will:
• Graph parabolas with vertices at the origin.
• Write equations of parabolas in standard form.
• Graph parabolas with vertices not at the origin.
• Solve applied problems involving parabolas.
10. 3 The Parabola Did you know that the Olympic torch is lit several months before the start of the games? The ceremonial method for lighting the flame is the same as in ancient times. The ceremony takes place at the Temple of Hera in Olympia, Greece, and is rooted in Greek mythology, paying tribute to Prometheus, who stole fire from Zeus to give to all humans. One of eleven acting priestesses places the torch at the focus of a parabolic mirror (see Figure 1), which focuses light rays from the sun to ignite the flame. Parabolic mirrors (or reflectors) are able to capture energy and focus it to a single point. The advantages of this property are evidenced by the vast list of parabolic objects we use every day: satellite dishes, suspension bridges, telescopes, microphones, spotlights, and car headlights, to name a few. Parabolic reflectors are also used in alternative energy devices, such as solar cookers and water heaters, because they are inexpensive to manufacture and need little maintenance. In this section we will explore the parabola and its uses, including low-cost, energy-efficient solar designs. Graphing Parabolas with Vertices at the Origin In The Ellipse, we saw that an ellipse is formed when a plane cuts through a right circular cone. If the plane is parallel to the edge of the cone, an unbounded curve is formed. This curve is a parabola. See Figure 2.


## 10.3 The Parabola
Like the ellipse and hyperbola, the parabola can also be defined by a set of points in the coordinate plane. A parabola is the set of all points (x, y) in a plane that are the same distance from a fixed line, called the directrix, and a fixed point (the focus) not on the directrix. In Quadratic Functions, we learned about a parabola’s vertex and axis of symmetry. Now we extend the discussion to include other key features of the parabola. See Figure 3. Notice that the axis of symmetry passes through the focus and vertex and is perpendicular to the directrix. The vertex is the midpoint between the directrix and the focus. The line segment that passes through the focus and is parallel to the directrix is called the latus rectum. The endpoints of the latus rectum lie on the curve. By definition, the distance d from the focus to any point P on the parabola is equal to the distance from P to the directrix. Latus rectum Axis of symmetry Focus Directrix x y Vertex To work with parabolas in the coordinate plane, we consider two cases: those with a vertex at the origin and those with a vertex at a point other than the origin. We begin with the former. Let (x, y) be a point on the parabola with vertex (0, 0), focus (0, p), and directrix y = -p as shown in Figure 4. The distance d from point (x, y) to point (x, -p) on the directrix is the difference of the y-values: d = y + p. The distance from the focus (0, p) to the point (x, y) is also equal to d and can be expressed using the distance formula.

d = \sqrt{(x} - 0)^{2} + (y - p)^{2} 

= \sqrt{x} 2 + (y - p)^{2}  Set the two expressions for d equal to each other and solve for y to derive the equation of the parabola. We do this because the distance from (x, y) to (0, p) equals the distance from (x, y) to (x, -p).

\sqrt{x} 2 + (y - p)^{2}  = y + p We then square both sides of the equation, expand the squared terms, and simplify by combining like terms.

x 2 + (y - p)^{2} = (y + p)^{2}

x 2 + y 2 - 2py + p^{2} = y 2 + 2py + p^{2}

x 2 - 2py = 2py

x 2 = 4py The equations of parabolas with vertex (0, 0) are y 2 = 4px when the x-axis is the axis of symmetry and x 2 = 4py when the y-axis is the axis of symmetry. These standard forms are given below, along with their general graphs and key features. (0, p) d d (x, y) (x, -p) y = -p x y

standard forms of parabolas with vertex (0, 0) Axis of Symmetry Equation Focus Directrix Endpoints of Latus Rectum x-axis y 2 = 4px (p, 0) x = -p (p, \pm  2p) y-axis x 2 = 4py (0, p) y = -p (\pm  2p, p) the x-axis, the parabola opens left. (c) When p < 0 and the axis of symmetry is the y-axis, the parabola opens up. (d) When p < 0 and the axis of symmetry is the y-axis, the parabola opens down. (p, 0) (p, 0) (p, -|2p|) (p, -|2p|) (p, |2p|) (p, |2p|) y y x x (a) (c) (d) (b) x = -p x = -p y 2 = 4px y 2 = 4px p > 0 p < 0 (0, p) (0, p) (-|2p|, p) (-|2p|, p) (|2p|, p) (|2p|, p) y y x x y = -p y = -p x^{2} = 4py p > 0 x^{2} = 4py p < 0 The key features of a parabola are its vertex, axis of symmetry, focus, directrix, and latus rectum. See Figure 5. When given a standard equation for a parabola centered at the origin, we can easily identify the key features to graph the parabola. A line is said to be tangent to a curve if it intersects the curve at exactly one point. If we sketch lines tangent to the parabola at the endpoints of the latus rectum, these lines intersect on the axis of symmetry, as shown in Figure 6. x = -6 y 2 = 24x y x


**How To…**
Given a standard form equation for a parabola centered at (0, 0), sketch the graph. 1. Determine which of the standard forms applies to the given equation: y 2 = 4px or x 2 = 4py. 2. Use the standard form identified in Step 1 to determine the axis of symmetry, focus, equation of the directrix, and endpoints of the latus rectum. a. If the equation is in the form y 2 = 4px, then • the axis of symmetry is the x-axis, y = 0 • set 4p equal to the coefficient of x in the given equation to solve for p. If p > 0, the parabola opens right. If p < 0, the parabola opens left. • use p to find the coordinates of the focus, (p, 0) • use p to find the equation of the directrix, x = - p • use p to find the endpoints of the latus rectum, (p, \pm  2p). Alternately, substitute x = p into the original equation. b. If the equation is in the form x 2 = 4py, then • the axis of symmetry is the y-axis, x = 0 • set 4p equal to the coefficient of y in the given equation to solve for p. If p > 0, the parabola opens up. If p < 0, the parabola opens down. • use p to find the coordinates of the focus, (0, p) • use p to find equation of the directrix, y = - p • use p to find the endpoints of the latus rectum, (\pm 2p, p) 3. Plot the focus, directrix, and latus rectum, and draw a smooth curve to form the parabola.

**Example  1**
Graphing a Parabola with Vertex (0, 0) and the x-axis as the Axis of Symmetry Graph y 2 = 24x. Identify and label the focus, directrix, and endpoints of the latus rectum. Solution The standard form that applies to the given equation is y 2 = 4px. Thus, the axis of symmetry is the x-axis. It follows that: • 24 = 4p, so p = 6. Since p > 0, the parabola opens right • the coordinates of the focus are (p, 0) = (6, 0) • the equation of the directrix is x = -p = - 6 • the endpoints of the latus rectum have the same x-coordinate at the focus. To find the endpoints, substitute x = 6 into the original equation: (6, \pm  12) Next we plot the focus, directrix, and latus rectum, and draw a smooth curve to form the parabola. See Figure 7. y x x = -6


**Try It #1**
Graph y 2 = -16x. Identify and label the focus, directrix, and endpoints of the latus rectum.

**Example  2**
Graphing a Parabola with Vertex (0, 0) and the y-axis as the Axis of Symmetry Graph x 2 = -6y. Identify and label the focus, directrix, and endpoints of the latus rectum. Solution The standard form that applies to the given equation is x 2 = 4py. Thus, the axis of symmetry is the y-axis. It follows that: • -6 = 4p, so p = - 3 __ 2  Since p < 0, the parabola opens down. • the coordinates of the focus are (0, p) =  0, -  3 __ 2    • the equation of the directrix is y = - p =  3 __ 2  • the endpoints of the latus rectum can be found by substituting y =  3 __ 2  into the original equation,  \pm 3, -  3 __ 2    Next we plot the focus, directrix, and latus rectum, and draw a smooth curve to form the parabola.

**Try It #2**
Graph x 2 = 8y. Identify and label the focus, directrix, and endpoints of the latus rectum. Writing Equations of Parabolas in Standard Form In the previous examples, we used the standard form equation of a parabola to calculate the locations of its key features. We can also use the calculations in reverse to write an equation for a parabola when given its key features.

**How To…**
Given its focus and directrix, write the equation for a parabola in standard form. 1. Determine whether the axis of symmetry is the x- or y-axis. a. If the given coordinates of the focus have the form (p, 0), then the axis of symmetry is the x-axis.

Use the standard form y 2 = 4px. b. If the given coordinates of the focus have the form (0, p), then the axis of symmetry is the y-axis.

Use the standard form x 2 = 4py. 2. Multiply 4p. 3. Substitute the value from Step 2 into the equation determined in Step 1.

**Example  3**
Writing the Equation of a Parabola in Standard Form Given its Focus and Directrix What is the equation for the parabola with focus  - 1 __ 2 , 0   and directrix x =  1 __ 2 ? Solution The focus has the form (p, 0), so the equation will have the form y 2 = 4px. • Multiplying 4p, we have 4p = 4(-  1 _ 2 ) = -2. • Substituting for 4p, we have y 2 = 4px = -2x. Therefore, the equation for the parabola is y 2 = -2x. x^{2} = -6y y x y = 3 0, -3 3, -3


**Try It #3**
What is the equation for the parabola with focus  0,  7 __ 2    and directrix y = - 7 __ 2 ? Graphing Parabolas with Vertices Not at the Origin Like other graphs we’ve worked with, the graph of a parabola can be translated. If a parabola is translated h units horizontally and k units vertically, the vertex will be (h, k). This translation results in the standard form of the equation we saw previously with x replaced by (x - h) and y replaced by (y - k). To graph parabolas with a vertex (h, k) other than the origin, we use the standard form (y - k)^{2} = 4p(x - h) for parabolas that have an axis of symmetry parallel to the x-axis, and (x - h)^{2} = 4p(y - k) for parabolas that have an axis of symmetry parallel to the y-axis. These standard forms are given below, along with their general graphs and key features. standard forms of parabolas with vertex (h, k) Axis of Symmetry Equation Focus Directrix Endpoints of Latus Rectum y = k (y - k)^{2} = 4p(x - h) (h + p, k) x = h -p (h + p, k \pm  2p) x = h (x - h)^{2} = 4p(y - k) (h, k + p) y = k -p (h \pm  2p, k + p) (c) When p > 0, the parabola opens up. (d) When p < 0, the parabola opens down. (y - k)^{2} = 4p(x - h) (x - h)^{2} = 4p(y - h) (x - h)^{2} = 4p(y - k) (h + p, k + 2p) y = k y = k x y (a) (b) (c) (d) y y y x x (h, k) (h, k) (h, k) x = h - p y = k - p y = k - p x = h - p (h + p, k) (h, k + p) (h, k + p) (h + p, k - 2p) (h + 2p, k + p) p > 0 p > 0 x (y - k)^{2} = 4p(x - h) (h + p, k + |2p|) (h, k) (h + p, k) (h + p, k - |2p|) (h - 2p, k + p) (h - |2p|, k + p) (h + |2p|, k + p) p < 0 x = h x = h p < 0


**How To…**
Given a standard form equation for a parabola centered at (h, k), sketch the graph. 1. Determine which of the standard forms applies to the given equation: (y - k)^{2} = 4p(x - h) or (x - h)^{2} = 4p(y - k). 2. Use the standard form identified in Step 1 to determine the vertex, axis of symmetry, focus, equation of the directrix, and endpoints of the latus rectum. a. If the equation is in the form (y - k)^{2} = 4p(x - h), then: • use the given equation to identify h and k for the vertex, (h, k) • use the value of k to determine the axis of symmetry, y = k • set 4p equal to the coefficient of (x - h) in the given equation to solve for p. If p > 0, the parabola opens right. If p < 0, the parabola opens left. • use h, k, and p to find the coordinates of the focus, (h + p, k) • use h and p to find the equation of the directrix, x = h - p • use h, k, and p to find the endpoints of the latus rectum, (h + p, k \pm  2p) b. If the equation is in the form (x - h)^{2} = 4p(y - k), then: • use the given equation to identify h and k for the vertex, (h, k) • use the value of h to determine the axis of symmetry, x = h • set 4p equal to the coefficient of (y - k) in the given equation to solve for p. If p > 0, the parabola opens up. If p < 0, the parabola opens down. • use h, k, and p to find the coordinates of the focus, (h, k + p) • use k and p to find the equation of the directrix, y = k - p • use h, k, and p to find the endpoints of the latus rectum, (h \pm  2p, k + p) 3. Plot the vertex, axis of symmetry, focus, directrix, and latus rectum, and draw a smooth curve to form the parabola.

**Example  4**
Graphing a Parabola with Vertex ( h, k) and Axis of Symmetry Parallel to the x-axis Graph (y - 1)^{2} = -16(x + 3). Identify and label the vertex, axis of symmetry, focus, directrix, and endpoints of the latus rectum. Solution The standard form that applies to the given equation is (y - k)^{2} = 4p(x - h). Thus, the axis of symmetry is parallel to the x-axis. It follows that: • the vertex is (h, k) = (-3, 1) • the axis of symmetry is y = k = 1 • -16 = 4p, so p = -4. Since p < 0, the parabola opens left. • the coordinates of the focus are (h + p, k) = (-3 + (-4), 1) = (-7, 1) • the equation of the directrix is x = h - p = -3 - (-4) = 1 • the endpoints of the latus rectum are (h + p, k \pm  2p) = (-3 + (-4), 1 \pm  2(-4)), or (-7, -7) and (-7, 9) Next we plot the vertex, axis of symmetry, focus, directrix, and latus rectum, and draw a smooth curve to form the parabola. See Figure 10. (y - 1)^{2} = -16(x + 3) (-7 , -7 ) y = 1 x = 1 x y


**Try It #4**
Graph (y + 1)^{2} = 4(x - 8). Identify and label the vertex, axis of symmetry, focus, directrix, and endpoints of the latus rectum.

**Example  5**

### Graphing a Parabola from an Equation Given in General Form
Graph x 2 - 8x - 28y - 208 = 0. Identify and label the vertex, axis of symmetry, focus, directrix, and endpoints of the latus rectum. Solution Start by writing the equation of the parabola in standard form. The standard form that applies to the given equation is (x - h)^{2} = 4p (y - k). Thus, the axis of symmetry is parallel to the y-axis. To express the equation of the parabola in this form, we begin by isolating the terms that contain the variable x in order to complete the square.

x 2 - 8x - 28y - 208 = 0

x 2 - 8x = 28y + 208

(x - 4)^{2} = 28y + 224

(x - 4)^{2} = 28(y + 8)

(x - 4)^{2} = 4 ⋅ 7 ⋅ (y + 8) It follows that: • the vertex is (h, k) = (4, -8) • the axis of symmetry is x = h = 4 • since p = 7, p > 0 and so the parabola opens up • the coordinates of the focus are (h, k + p) = (4, -8 + 7) = (4, -1) • the equation of the directrix is y = k - p = -8 - 7 = -15 • the endpoints of the latus rectum are (h \pm  2p, k + p) = (4 \pm  2(7), -8 + 7), or (-10, -1) and (18, -1) Next we plot the vertex, axis of symmetry, focus, directrix, and latus rectum, and draw a smooth curve to form the parabola. See Figure 11.

**Try It #5**
Graph (x + 2)^{2} = -20 (y - 3). Identify and label the vertex, axis of symmetry, focus, directrix, and endpoints of the latus rectum. Solving Applied Problems Involving Parabolas As we mentioned at the beginning of the section, parabolas are used to design many objects we use every day, such as telescopes, suspension bridges, microphones, and radar equipment. Parabolic mirrors, such as the one used to light the Olympic torch, have a very unique reflecting property. When rays of light parallel to the parabola’s axis of symmetry are directed toward any surface of the mirror, the light is reflected directly to the focus. See Figure 12. This is why the Olympic torch is ignited when it is held at the focus of the parabolic mirror. (x - 4)^{2} = 28(y + 8) y = -15 x = 4 y x

Parabolic mirrors have the ability to focus the sun’s energy to a single point, raising the temperature hundreds of degrees in a matter of seconds. Thus, parabolic mirrors are featured in many low-cost, energy efficient solar products, such as solar cookers, solar heaters, and even travel-sized fire starters.

**Example  6**

### Solving Applied Problems Involving Parabolas
A cross-section of a design for a travel-sized solar fire starter is shown in Figure 13. The sun’s rays reflect off the parabolic mirror toward an object attached to the igniter. Because the igniter is located at the focus of the parabola, the reflected rays cause the object to burn in just seconds. a. Find the equation of the parabola that models the fire starter. Assume that the vertex of the parabolic mirror is the origin of the coordinate plane. b. Use the equation found in part ( a) to find the depth of the fire starter.

**Solution**
a. The vertex of the dish is the origin of the coordinate plane, so the parabola will take the standard form x 2 = 4py, where p > 0. The igniter, which is the focus, is 1.7 inches above the vertex of the dish. Thus we have p = 1.7.

x 2 = 4py Standard form of upward-facing parabola with vertex (0, 0)

Substitute 1.7 for p.

Multiply. b. The dish extends  4.5 ___ 2  = 2.25 inches on either side of the origin. We can substitute 2.25 for x in the equation from part ( a) to find the depth of the dish.

Equation found in part ( a).

Substitute 2.25 for x.

Solve for y. The dish is about 0.74 inches deep. Parallel rays of sunlight Parabolic reflector Focus Igniter Depth


**Try It #6**
Balcony-sized solar cookers have been designed for families living in India. The top of a dish has a diameter of 1,600 mm. The sun’s rays reflect off the parabolic mirror toward the “cooker,” which is placed 320 mm from the base. a. Find an equation that models a cross-section of the solar cooker. Assume that the vertex of the parabolic mirror is the origin of the coordinate plane, and that the parabola opens to the right (i.e., has the x-axis as its axis of symmetry). b. Use the equation found in part (a) to find the depth of the cooker. Access these online resources for additional instruction and practice with parabolas. • Conic Sections: The Parabola Part 1 of 2 (http://openstaxcollege.org/l/parabola^{1}) • Conic Sections: The Parabola Part 2 of 2 (http://openstaxcollege.org/l/parabola^{2}) • Parabola with Vertical Axis (http://openstaxcollege.org/l/parabolavertcal) • Parabola with Horizontal Axis (http://openstaxcollege.org/l/parabolahoriz)


### 10.3 Section Exercises
Verbal 1. Define a parabola in terms of its focus and directrix. 2. If the equation of a parabola is written in standard form and p is positive and the directrix is a vertical line, then what can we conclude about its graph? 3. If the equation of a parabola is written in standard form and p is negative and the directrix is a horizontal line, then what can we conclude about its graph? 4. What is the effect on the graph of a parabola if its equation in standard form has increasing values of p? 5. As the graph of a parabola becomes wider, what will happen to the distance between the focus and directrix? Algebraic For the following exercises, determine whether the given equation is a parabola. If so, rewrite the equation in standard form. 6. y 2 = 4 - x 2 9. (y - 3)^{2} = 8(x - 2) For the following exercises, rewrite the given equation in standard form, and then determine the vertex (V), focus (F), and directrix (d) of the parabola. __ 4 x 2 __ 8 y 2 ___ 17. (x - 1)^{2} = 4(y - 1) 18. (y - 2)^{2} =  4 __ 5 (x + 4) 19. (y - 4)^{2} = 2(x + 3) 20. (x + 1)^{2} = 2(y + 4) 21. (x + 4)^{2} = 24(y + 1) 22. (y + 4)^{2} = 16(x + 4) 27. x 2 - 4x + 2y - 6 = 0 28. y 2 - 6y + 12x - 3 = 0 30. x 2 + 4x + 8y - 4 = 0 Graphical For the following exercises, graph the parabola, labeling the focus and the directrix. __ 8 y 2 ___ 35. (y - 2)^{2} = - 4 __ 3 (x + 2) 36. -5(x + 5)^{2} = 4(y + 5) 37. -6(y + 5)^{2} = 4(x - 4) 38. y 2 - 6y - 8x + 1 = 0 39. x 2 + 8x + 4y + 20 = 0 41. y 2 - 8x + 10y + 9 = 0 42. x 2 + 4x + 2y + 2 = 0 44. -2x 2 + 8x - 4y - 24 = 0 For the following exercises, find the equation of the parabola given information about its graph. 45. Vertex is (0, 0); directrix is y = 4, focus is (0, -4). 46. Vertex is (0, 0); directrix is x = 4, focus is (-4, 0). 47. Vertex is (2, 2); directrix is x = 2 - \sqrt{2} , focus is (2 + \sqrt{48.} Vertex is (-2, 3); directrix is x = - 7 __ 2 , focus is  -  1 __ 2 , 3  . 49. Vertex is (\sqrt{2} , - \sqrt{3} ); directrix is x = 2\sqrt{2} , focus is (0, -\sqrt{3} ). 50. Vertex is (1, 2); directrix is y =  11 ___ 3  , focus is  1,  1 __ 3   .


## 10.3 Section Exercises
For the following exercises, determine the equation for the parabola from its graph. x Axis of symmetry Focus Vertex y y x Axis of symmetry Vertex Focus y x Axis of symmetry Focus Vertex - 31 Vertex Axis of symmetry Focus y x y x Axis of symmetry Vertex Focus

Extensions For the following exercises, the vertex and endpoints of the latus rectum of a parabola are given. Find the equation. 57. V(0, 0), Endpoints (-2, 4), (-2, -4) 59. V(-3, -1), Endpoints (0, 5), (0, -7) 60. V(4, -3), Endpoints  5, - 7 __ 2   ,  3, - 7 __ 2    Real-World Applications 61. The mirror in an automobile headlight has a parabolic cross-section with the light bulb at the focus. On a schematic, the equation of the parabola is given as x 2 = 4y. At what coordinates should you place the light bulb? 62. If we want to construct the mirror from the previous exercise such that the focus is located at (0, 0.25), what should the equation of the parabola be? 63. A satellite dish is shaped like a paraboloid of revolution. This means that it can be formed by rotating a parabola around its axis of symmetry. The receiver is to be located at the focus. If the dish is 12 feet across at its opening and 4 feet deep at its center, where should the receiver be placed? 64. Consider the satellite dish from the previous exercise. If the dish is 8 feet across at the opening and 2 feet deep, where should we place the receiver? 65. A searchlight is shaped like a paraboloid of revolution. A light source is located 1 foot from the base along the axis of symmetry. If the opening of the searchlight is 3 feet across, find the depth. 66. If the searchlight from the previous exercise has the light source located 6 inches from the base along the axis of symmetry and the opening is 4 feet, find the depth. 67. An arch is in the shape of a parabola. It has a span of 100 feet and a maximum height of 20 feet. Find the equation of the parabola, and determine the height of the arch 40 feet from the center. 68. If the arch from the previous exercise has a span of 160 feet and a maximum height of 40 feet, find the equation of the parabola, and determine the distance from the center at which the height is 69. An object is projected so as to follow a parabolic path given by y = -x 2 + 96x, where x is the horizontal distance traveled in feet and y is the height. Determine the maximum height the object reaches. 70. For the object from the previous exercise, assume the path followed is given by y = -0.5x 2 + 80x. Determine how far along the horizontal the object traveled to reach maximum height.


## 10.4 Rotation of Axis
Learning Objectives
In this section, you will:
• Identify nondegenerate conic sections given their general form equations.
• Use rotation of axes formulas.
• Write equations of rotated conics in standard form.
• Identify conics without rotating axes.
10.4 Rotation of Axis As we have seen, conic sections are formed when a plane intersects two right circular cones aligned tip to tip and extending infinitely far in opposite directions, which we also call a cone. The way in which we slice the cone will determine the type of conic section formed at the intersection. A circle is formed by slicing a cone with a plane perpendicular to the axis of symmetry of the cone. An ellipse is formed by slicing a single cone with a slanted plane not perpendicular to the axis of symmetry. A parabola is formed by slicing the plane through the top or bottom of the double-cone, whereas a hyperbola is formed when the plane slices both the top and bottom of the cone. See Figure 1. Ellipses, circles, hyperbolas, and parabolas are sometimes called the nondegenerate conic sections, in contrast to the degenerate conic sections, which are shown in Figure 2. A degenerate conic results when a plane intersects the double cone and passes through the apex. Depending on the angle of the plane, three types of degenerate conic sections are possible: a point, a line, or two intersecting lines. Circle Hyperbola Parabola Ellipse Diagonal Slice Horizontal Slice Deep Vertical Slice Vertical Slice Intersecting Lines Single Line Single Point


### Identifying Nondegenerate Conics in General Form
In previous sections of this chapter, we have focused on the standard form equations for nondegenerate conic sections. In this section, we will shift our focus to the general form equation, which can be used for any conic. The general form is set equal to zero, and the terms and coefficients are given in a particular order, as shown below.

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 where A, B, and C are not all zero. We can use the values of the coefficients to identify which type conic is represented by a given equation. You may notice that the general form equation has an xy term that we have not seen in any of the standard form equations. As we will discuss later, the xy term rotates the conic whenever B is not equal to zero. Conic Sections Example ellipse 4x 2 + 9y 2 = 1 circle 4x 2 + 4y 2 = 1 hyperbola 4x 2 - 9y 2 = 1 parabola 4x 2 = 9y or 4y 2 = 9x one line 4x + 9y = 1 intersecting lines (x - 4) (y + 4)= 0 parallel lines (x - 4)(x - 9) = 0 a point 4x 2 + 4y 2 = 0 no graph 4x 2 + 4y 2 = - 1 general form of conic sections A conic section has the general form Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 where A, B, and C are not all zero. indicates that the conic has not been rotated. Conic Sections Example ellipse Ax 2 + Cy 2 + Dx + Ey + F = 0, A \neq  C and AC > 0 circle Ax 2 + Cy 2 + Dx + Ey + F = 0, A = C hyperbola Ax 2 - Cy 2 + Dx + Ey + F = 0 or - Ax 2 + Cy 2 + Dx + Ey + F = 0, where A and C are positive parabola Ax 2 + Dx + Ey + F = 0 or Cy 2 + Dx + Ey + F = 0

**How To…**
Given the equation of a conic, identify the type of conic. 1. Rewrite the equation in the general form, Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0. 2. Identify the values of A and C from the general form. a. If A and C are nonzero, have the same sign, and are not equal to each other, then the graph may be an ellipse. b. If A and C are equal and nonzero and have the same sign, then the graph may be a circle.

c. If A and C are nonzero and have opposite signs, then the graph may be a hyperbola. d. If either A or C is zero, then the graph may be a parabola. If B = 0, the conic section will have a vertical and/or horizontal axes. If B does not equal 0, as shown below, the conic section is rotated. Notice the phrase “may be” in the definitions. That is because the equation may not represent a conic section at all, depending on the values of A, B, C, D, E, and F. For example, the degenerate case of a circle or an ellipse is a point: Ax 2 +By 2=0, when A and B have the same sign. The degenerate case of a hyperbola is two intersecting straight lines: Ax 2 +By 2=0, when A and B have opposite signs. On the other hand, the equation Ax 2 +By 2+1=0, when A and B are positive does not represent a graph at all, since there are no real ordered pairs which satisfy it.

**Example  1**

### Identifying a Conic from Its General Form
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

(-25)x 2 + 0xy + (-4)y 2 + 100x + 16y + 20 = 0 A = -25 and C = -4. Because AC > 0 and A \neq  C, the graph of this equation is an ellipse.

**Try It #1**
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

**How To…**
Given the equation of a conic, find a new representation after rotating through an angle. 1. Find x and y where x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta . 2. Substitute the expression for x and y into in the given equation, then simplify. 3. Write the equations with x′ and y′ in standard form.

**Example  2**
Finding a New Representation of an Equation after Rotating through a Given Angle Find a new representation of the equation 2x 2 - xy + 2y 2 - 30 = 0 after rotating through an angle of \theta  = 45°. Solution Find x and y, where x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta . Because \theta  = 45°,

x = x′ cos(45°) - y′ sin(45°)

x = x′   1 _ \sqrt{2}     - y′   1 _ \sqrt{2}    

x =  x′ - y′ _ \sqrt{2}   and

y = x′ sin(45°) + y′ cos(45°)

y = x′   1 _ \sqrt{2}     + y′   1 _ \sqrt{2}    

y =  x′ + y′ _ \sqrt{2}   Substitute x = x′ cos\theta  - y′ sin\theta  and y = x′ sin \theta  + y′ cos \theta  into 2x 2 - xy + 2y 2 - 30 = 0.

2   x′ - y′ _ \sqrt{2}      -   x′ - y′ _ \sqrt{2}       x′ + y′ _ \sqrt{2}     + 2   x′ + y′ _ \sqrt{2}      - 30 = 0

Simplify.

/ / 2  (x′ - y′)(x′ - y′)

__ / 2

 -  (x′ - y′)(x′ + y′)

__  + / 2  (x′ + y′)(x′ + y′)

__ / 2

 - 30 = 0 FOIL method

x′ 2  -2x′ y′ + y′ 2 -  (x′ 2 - y′ 2) _  + x′ 2  + 2x′ y′ + y′ 2 - 30 = 0 Combine like terms.

2x′ 2 + 2y′ 2 -  (x′ 2 - y′ 2) _  = 30 Combine like terms.

2 2x′ 2 + 2y′ 2 -  (x′ 2 - y′ 2) _    = 2(30) Multiply both sides by 2.

4x′ 2 + 4y′ 2 - (x′ 2 - y′ 2) = 60 Simplify.

4x′ 2 + 4y′ 2 - x′ 2 + y′ 2 = 60 Distribute.

 3x′ 2 _ 60  +  5y′ 2 _ 60  =  60 _ 60  Set equal to 1. Write the equations with x′ and y′ in the standard form.

 x′ 2 _ 20  +  y′ 2

_ This equation is an ellipse. Figure 6 shows the graph. Writing Equations of Rotated Conics in Standard Form Now that we can find the standard form of a conic when we are given an angle of rotation, we will learn how to transform the equation of a conic given in the form Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0. into standard form by rotating the axes. To do so, we will rewrite the general form as an equation in the x′ and y′ coordinate system without the x′y′ term, by rotating the axes by a measure of \theta  that satisfies cot(2\theta ) =  A - C ______ B  We have learned already that any conic may be represented by the second degree equation

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0. where A, B, and C are not all zero. However, if B \neq  0, then we have an xy term that prevents us from rewriting the equation in standard form. To eliminate it, we can rotate the axes by an acute angle \theta  where cot(2\theta ) =  A - C ______ B . • If cot(2\theta ) > 0, then 2\theta  is in the first quadrant, and \theta  is between (0°, 45°). • If cot(2\theta ) < 0, then 2\theta  is in the second quadrant, and \theta  is between (45°, 90°). • If A = C, then \theta  = 45°.

**How To…**
Given an equation for a conic in the x′ y′ system, rewrite the equation without the x′ y′ term in terms of x′ and y′, where the x′ and y′ axes are rotations of the standard axes by \theta  degrees. \theta  = 45° x x’ y’

1. Find cot(2\theta ). 2. Find sin \theta  and cos \theta . 3. Substitute sin \theta  and cos \theta  into x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta . 4. Substitute the expression for x and y into in the given equation, and then simplify. 5. Write the equations with x′ and y′ in the standard form with respect to the rotated axes.

**Example  3**
Rewriting an Equation with respect to the x ́ and y ́ axes without the x ́y ́ Term Rewrite the equation 8x 2 - 12xy + 17y 2 = 20 in the x′ y′ system without an x′ y′ term. Solution First, we find cot(2\theta ). See Figure 7.

8x 2 - 12xy + 17y 2 = 20 ⇒ A = 8, B = - 12 and C = 17

cot(2\theta ) =  A - C ______ B  =  8 - 17 ______ -12 

cot(2\theta ) =  -9 ____ -12  =  3 __ 4 

cot(2\theta ) =  3 __ 4  =  adjacent _ opposite  So the hypotenuse is

h = 5 Next, we find sin \theta  and cos \theta .

sin \theta  = \sqrt{___________}  1 - cos(2\theta ) __________   = \sqrt{1} -  3 __ 5  _   = \sqrt{5} __ 5  -  3 __ 5  _  = \sqrt{_________}  5 - 3 _____  ⋅ 1 __ 2   = \sqrt{___}

 2 __ 10   = \sqrt{__}

 1 __ 5  

sin \theta  =  1 _ \sqrt{5}  

cos \theta  = \sqrt{___________}  1 + cos(2\theta ) __________   = \sqrt{1} +  3 __ 5  _   = \sqrt{5} __ 5  +  3 __ 5  _  = \sqrt{_________}  5 + 3 _____  ⋅ 1 __ 2   = \sqrt{___}

 8 _ 10   = \sqrt{__}

 4 __ 5  

cos \theta  =  2 _ \sqrt{5}   Substitute the values of sin \theta  and cos \theta  into x = x′ cos \theta  - y′ sin \theta  and y = x′ sin \theta  + y′ cos \theta .

x = x′ cos \theta  - y′ sin \theta 

x = x′   2 _ \sqrt{5}     - y′   1 _ \sqrt{5}    

x =  2x′ - y′ _ \sqrt{5}   and

y = x′ sin \theta  + y′ cos \theta  2\theta  h x y

y = x′   1 _ \sqrt{5}     + y′   2 _ \sqrt{5}    

y =  x′ + 2y′ _ \sqrt{5}   Substitute the expressions for x and y into in the given equation, and then simplify.

8  2x′ - y′ _ \sqrt{5}      - 12   2x′ - y′ _ \sqrt{5}       x′ + 2y′ _ \sqrt{5}     + 17  x′ + 2y′ _ \sqrt{5}      = 20

8  (2x′ - y′)(2x′ - y′)

__    - 12  (2x′ - y′)(x′ + 2y′)

__    + 17  (x′ + 2y′)(x′ + 2y′)

__    = 20

8 (4x′ 2 - 4x′ y′ + y′ 2) - 12(2x′ 2 + 3x′ y′ - 2y′ 2) + 17(x′ 2 + 4x′ y′ + 4y′ 2) = 100

32x′ 2 - 32x′ y′ + 8y′ 2 - 24x′ 2 - 36x′ y′ + 24y′ 2 + 17x′ 2 + 68x′ y′ + 68y′ 2 = 100

 25 ____ ___ ___ 100  Write the equations with x′ and y′ in the standard form with respect to the new coordinate system.  x′ 2 _ 4  +  y′ 2

_ 1  = 1

**Try It #2**
Rewrite the 13x 2 - 6\sqrt{3} xy + 7y 2 = 16 in the x′ y′ system without the x′ y′ term.

**Example  4**

### Graphing an Equation That Has No x ́y ́ Terms
Graph the following equation relative to the x′ y′ system:

x 2 + 12xy - 4y 2 = 30 Solution First, we find cot(2\theta ).

x 2 + 12xy - 4y 2 = 20 ⇒ A = 1, B = 12, and C = -4

cot(2\theta ) =  A - C ______ B 

cot(2\theta ) =  1 - (-4) ________ 

cot(2\theta ) =  5 ___ 12  x y

Because cot(2\theta ) =  5 __ 12 , we can draw a reference triangle as in Figure 9.

cot(2\theta ) =  5 ___ 12  =  adjacent _ opposite  Thus, the hypotenuse is

h = 13 Next, we find sin \theta  and cos \theta . We will use half-angle identities.

sin \theta  = \sqrt{___________}  1 - cos(2\theta ) __________   = \sqrt{1} -  5 __ 13  _   = \sqrt{13} _ 13  -  5 _ 13  _   = \sqrt{______}

 8 _____ 13  ⋅ 1 __ 2   =  2 _ \sqrt{13}  

cos \theta  = \sqrt{___________}  1 + cos(2\theta ) __________   = \sqrt{1} +  5 __ 13  _   = \sqrt{13} _ 13  +  5 _ 13  _   = \sqrt{______}

 18 ___ 13  ⋅ 1 __ 2   =  3 _ \sqrt{13}   Now we find x and y.

x = x′ cos \theta  - y′ sin \theta 

x = x′   3 _ \sqrt{13}     - y′   2 _ \sqrt{13}    

x =  3x′ - 2y′ _ \sqrt{13}   and

y = x′ sin \theta  + y′ cos \theta 

y = x′   2 _ \sqrt{13}     + y′   3 _ \sqrt{13}    

y =  2x′ + 3y′ _ \sqrt{13}   Now we substitute x =  3x′ - 2y′ _ \sqrt{13}   and y =  2x′ + 3y′ _ \sqrt{13}   into x 2 + 12xy - 4y 2 = 30.

  3x′ - 2y′ _ \sqrt{13}      + 12   3x′ - 2y′ _ \sqrt{13}     2x′ + 3y′ _ \sqrt{13}    - 4  2x′ + 3y′ _ \sqrt{13}      = 30 cot(2\theta ) = 12 x y 2\theta 

  1 ___ 13   [(3x′ - 2y′ )^{2} + 12(3x′ - 2y′ )(2x′ + 3y′ ) - 4 (2x′ + 3y′ )^{2}] = 30 Factor.

  1 ___ 13   [9x′ 2 - 12x′ y′ + 4y′ 2 + 12 (6x′ 2 + 5x′ y′ - 6y′ 2) - 4 (4x′ 2 + 12x′ y′ + 9y′ 2)] = 30 Multiply.

  1 ___ 13   [9x′ 2 - 12x′ y′ + 4y′ 2 + 72x′ 2 + 60x′ y′ - 72y′ 2 - 16x′ 2 - 48x′ y′ - 36y′ 2] = 30 Distribute.

  1 ___ Combine like terms.

Multiply.

 x′ 2 _ 6  -  4y′ 2 _ 15  = 1 Divide by 390. _ 6  -  4y′ 2 _ Identifying Conics without Rotating Axes Now we have come full circle. How do we identify the type of conic described by an equation? What happens when the axes are rotated? Recall, the general form of a conic is

Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 If we apply the rotation formulas to this equation we get the form

A′ x′ 2 + B′x′y′ + C′y′ 2 + D′x′ + E′y′ + F′ = 0 It may be shown that B^{2} - 4AC = B′ 2 - 4A′ C′. The expression does not vary after rotation, so we call the expression invariant. The discriminant, B^{2} - 4AC, is invariant and remains unchanged after rotation. Because the discriminant remains unchanged, observing the discriminant enables us to identify the conic section. using the discriminant to identify a conic If the equation Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 is transformed by rotating axes into the equation A′x′ 2 + B′x′y′ + C′y′ 2 + D′x′ + E′y′ + F′ = 0, then B^{2} - 4AC = B′ 2 - 4A′C′. The equation Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 is an ellipse, a parabola, or a hyperbola, or a degenerate case of one of these. If the discriminant, B^{2} - 4AC, is • < 0, the conic section is an ellipse • = 0, the conic section is a parabola • > 0, the conic section is a hyperbola y’ x’ y x


**Example  5**

### Identifying the Conic without Rotating Axes
Identify the conic for each of the following without rotating axes. a. 5x 2 + 2\sqrt{3} xy + 2y 2 - 5 = 0 b. 5x 2 + 2\sqrt{3} xy + 12y 2 - 5 = 0

**Solution**
a. Let’s begin by determining A, B, and C.

 5 A x 2 +  2\sqrt{3} 

B xy +  2 C y 2 - 5 = 0 Now, we find the discriminant.

B^{2} - 4AC =  2\sqrt{3}   2 - 4(5)(2)

= - 28 < 0 Therefore, 5x 2 + 2\sqrt{3} xy + 2y 2 - 5 = 0 represents an ellipse. b. Again, let’s begin by determining A, B, and .

 5 A x 2 +  2\sqrt{3} 

B xy +  12 C y 2 - 5 = 0 Now, we find the discriminant.

B^{2} - 4AC =  2\sqrt{3}  

Therefore, 5x 2 + 2\sqrt{3} xy + 12y 2 - 5 = 0 represents an ellipse.

**Try It #3**
Identify the conic for each of the following without rotating axes. a. x 2 - 9xy + 3y 2 - 12 = 0 b. 10x 2 - 9xy + 4y 2 - 4 = 0 > Access this online resource for additional instruction and practice with conic sections and rotation of axes. • Introduction to Conic Sections (http://openstaxcollege.org/l/introconic) { { { {


### 10.4 Section Exercises
Verbal 1. What effect does the xy term have on the graph of a conic section? 2. If the equation of a conic section is written in the form Ax 2 + By 2 + Cx + Dy + E = 0 and AB = 0, what can we conclude? 3. If the equation of a conic section is written in the form Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0, and B^{2} - 4AC > 0, what can we conclude? 4. Given the equation ax 2 + 4x + 3y 2 - 12 = 0, what can we conclude if a > 0? 5. For the equation Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0, the value of \theta  that satisfies cot(2\theta ) =  A - C ______ B  gives us what information? Algebraic For the following exercises, determine which conic section is represented based on the given equation. 7. x 2 - 10x + 4y - 10 = 0 8. 2x 2 - 2y 2 + 4x - 6y - 2 = 0 9. 4x 2 - y 2 + 8x - 1 = 0 10. 4y 2 - 5x + 9y + 1 = 0 3 xy - 4y 2 + 9 = 0 3 xy + 6y 2 - 6x - 3 = 0 16. -x 2 + 4\sqrt{2} xy + 2y 2 - 2y + 1 = 0 2 xy + 4y 2 - 10x + 1 = 0 For the following exercises, find a new representation of the given equation after rotating through the given angle. 18. 3x 2 + xy + 3y 2 - 5 = 0, \theta  = 45° 19. 4x 2 - xy + 4y 2 - 2 = 0, \theta  = 45° 21. -2x 2 + 8xy + 1 = 0, \theta  = 45° 2 xy + 4y 2 + y + 2 = 0, \theta  = 45° For the following exercises, determine the angle \theta  that will eliminate the xy term and write the corresponding equation without the xy term. 3 xy + 4y 2 + y - 2 = 0 3 xy + 6y 2 + y - 2 = 0 3 xy + 6y 2 + 4y - 3 = 0 26. -3x 2 - \sqrt{3} xy - 2y 2 - x = 0 27. 16x 2 + 24xy + 9y 2 + 6x - 6y + 2 = 0 28. x 2 + 4xy + 4y 2 + 3x - 2 = 0 29. x 2 + 4xy + y 2 - 2x + 1 = 0 3 xy + 6y 2 - 1 = 0 Graphical For the following exercises, rotate through the given angle based on the given equation. Give the new equation and graph the original and rotated equation. 31. y = - x 2, \theta  = - 45° 32. x = y 2, \theta  = 45°

_ 4  +  y 2

_ 1  = 1, \theta  = 45°

_ 16  +  x 2

_ 9  = 1, \theta  = 45° 35. y 2 - x 2 = 1, \theta  = 45° 36. y =  x 2

_ 2  , \theta  = 30° 37. x = (y - 1)^{2}, \theta  = 30°

_ 9  +  y 2

_ 4  = 1, \theta  = 30°


## 10.4 Section Exercises
For the following exercises, graph the equation relative to the x′ y′ system in which the equation has no x′ y′ term. 40. x 2 + 10xy + y 2 - 6 = 0 41. x 2 - 10xy + y 2 - 24 = 0 3 xy + y 2 - 22 = 0 3 xy + 4y 2 - 21 = 0 3 xy + y 2 - 64 = 0 3 xy + 19y 2 - 18 = 0 3 xy + 7y 2 - 16 = 0 49. 4x 2 - 4xy + y 2 - 8\sqrt{5} x - 16\sqrt{5} y = 0 For the following exercises, determine the angle of rotation in order to eliminate the xy term. Then graph the new set of axes. 3 xy + y 2 + 10x - 12y = 0 51. 6x 2 - 5xy + 6y 2 + 20x - y = 0 3 xy + 14y 2 + 10x - 3y = 0 3 xy + 10y 2 + 20x - 40y = 0 54. 8x 2 + 3xy + 4y 2 + 2x - 4 = 0 For the following exercises, determine the value of k based on the given equation. 56. Given 4x 2 + kxy + 16y 2 + 8x + 24y - 48 = 0, find k for the graph to be a parabola. 57. Given 2x 2 + kxy + 12y 2 + 10x - 16y + 28 = 0, find k for the graph to be an ellipse. 58. Given 3x 2 + kxy + 4y 2 - 6x + 20y + 128 = 0, find k for the graph to be a hyperbola. 59. Given kx 2 + 8xy + 8y 2 - 12x + 16y + 18 = 0, find k for the graph to be a parabola. 60. Given 6x 2 + 12xy + ky 2 + 16x + 10y + 4 = 0, find k for the graph to be an ellipse.

Learning Objectives
In this section, you will:
• Identify a conic in polar form.
• Graph the polar equations of conics.
• Define conics in terms of a focus and a directrix.
Conic Sections in Polar Coordinates Most of us are familiar with orbital motion, such as the motion of a planet around the sun or an electron around an atomic nucleus. Within the planetary system, orbits of planets, asteroids, and comets around a larger celestial body are often elliptical. Comets, however, may take on a parabolic or hyperbolic orbit instead. And, in reality, the characteristics of the planets’ orbits may vary over time. Each orbit is tied to the location of the celestial body being orbited and the distance and direction of the planet or other object from that body. As a result, we tend to use polar coordinates to represent these orbits. In an elliptical orbit, the periapsis is the point at which the two objects are closest, and the apoapsis is the point at which they are farthest apart. Generally, the velocity of the orbiting body tends to increase as it approaches the periapsis and decrease as it approaches the apoapsis. Some objects reach an escape velocity, which results in an infinite orbit. These bodies exhibit either a parabolic or a hyperbolic orbit about a body; the orbiting body breaks free of the celestial body’s gravitational pull and fires off into space. Each of these orbits can be modeled by a conic section in the polar coordinate system. Identifying a Conic in Polar Form Any conic may be determined by three characteristics: a single focus, a fixed line called the directrix, and the ratio of the distances of each to a point on the graph. Consider the parabola x = 2 + y 2 shown in Figure 2. Polar axis x = 2 + y^{2} F, Focus @ pole r D P(r, \theta ) Directrix \theta 


## 10.5 Conic Sections in Polar Coordinates
In The Parabola, we learned how a parabola is defined by the focus (a fixed point) and the directrix (a fixed line). In this section, we will learn how to define any conic in the polar coordinate system in terms of a fixed point, the focus P(r, \theta ) at the pole, and a line, the directrix, which is perpendicular to the polar axis. If F is a fixed point, the focus, and D is a fixed line, the directrix, then we can let e be a fixed positive number, called the eccentricity, which we can define as the ratio of the distances from a point on the graph to the focus and the point on the graph to the directrix. Then the set of all points P such that e =  PF ___ PD  is a conic. In other words, we can define a conic as the set of all points P with the property that the ratio of the distance from P to F to the distance from P to D is equal to the constant e. For a conic with eccentricity e, • if 0 \le  e < 1, the conic is an ellipse • if e = 1, the conic is a parabola • if e > 1, the conic is an hyperbola With this definition, we may now define a conic in terms of the directrix, x = \pm  p, the eccentricity e, and the angle \theta . Thus, each conic may be written as a polar equation, an equation written in terms of r and \theta . the polar equation for a conic For a conic with a focus at the origin, if the directrix is x = \pm  p, where p is a positive real number, and the eccentricity is a positive real number e, the conic has a polar equation

r =  ep _ 1 \pm  e cos \theta   For a conic with a focus at the origin, if the directrix is y = \pm  p, where p is a positive real number, and the eccentricity is a positive real number e, the conic has a polar equation

r =  ep _ 1 \pm  e sin \theta  

**How To…**
Given the polar equation for a conic, identify the type of conic, the directrix, and the eccentricity. 1. Multiply the numerator and denominator by the reciprocal of the constant in the denominator to rewrite the equation in standard form. 2. Identify the eccentricity e as the coefficient of the trigonometric function in the denominator. 3. Compare e with 1 to determine the shape of the conic. 4. Determine the directrix as x = p if cosine is in the denominator and y = p if sine is in the denominator. Set ep equal to the numerator in standard form to solve for x or y.

**Example  1**

### Identifying a Conic Given the Polar Form
For each of the following equations, identify the conic with focus at the origin, the directrix, and the eccentricity. a. r =  _________ 3 + 2 sin \theta   b. r =  _________ 4 + 5 cos \theta   c. r =  _________ 2 - 2 sin \theta   Solution For each of the three conics, we will rewrite the equation in standard form. Standard form has a 1 as the constant in the denominator. Therefore, in all three parts, the first step will be to multiply the numerator and denominator by the reciprocal of the constant of the original equation,  1 __ c , where c is that constant. a. Multiply the numerator and denominator by  1 __ 3 . r =  _________ 3 + 2sin \theta   ⋅    1 __ 3   _   1 __ 3    =  6  1 __ 3  

__

3  1 __ 3   + 2  1 __ 3   sin \theta   =  __

1 +  2 _ 3  sin \theta  

Because sin \theta  is in the denominator, the directrix is y = p. Comparing to standard form, note that e =  2 __ 3 . Therefore, from the numerator,

2 = ep

2 = 2 __ 3 p

  3 __ 2   2 =   3 __ 2    2 __ 3  p

3 = p Since e < 1, the conic is an ellipse. The eccentricity is e =  2 __ 3  and the directrix is y = 3. b. Multiply the numerator and denominator by  1 __ 4 .

r =  _ 4 + 5 cos \theta   ⋅    1 _ 4    _   1 _ 4    

r =  _ 4   

__

4  1 _ 4    + 5  1 _ 4    cos \theta  

r =  _ 1 +  5 _ 4  cos \theta   Because cos \theta  is in the denominator, the directrix is x = p. Comparing to standard form, e =  5 __ 4 . Therefore, from the numerator,

3 = ep

3 =  5 __ 4  p

  4 __ 5   3 =   4 __ 5    5 __ 4  p

 12 ___ 5  = p Since e > 1, the conic is a hyperbola. The eccentricity is e =  5 __ 4  and the directrix is x =  12 ___ c. Multiply the numerator and denominator by  1 __ 2 .

r =  _ 2 - 2 sin \theta   ⋅    1 _ 2    _   1 _ 2    

r =  7  1 _ 2   

__

2  1 _ 2    - 2  1 _ 2    sin \theta  

r =   7 _ 2  _ 1 - sin \theta   Because sine is in the denominator, the directrix is y = -p. Comparing to standard form, e = 1. Therefore, from the numerator,

 7 __ 2  = ep

 7 __ 2  = (1)p

 7 __ 2  = p Because e = 1, the conic is a parabola. The eccentricity is e = 1 and the directrix is y = - 7


**Try It #1**
Identify the conic with focus at the origin, the directrix, and the eccentricity for r =  ________ 3 - cos \theta  . Graphing the Polar Equations of Conics When graphing in Cartesian coordinates, each conic section has a unique equation. This is not the case when graphing in polar coordinates. We must use the eccentricity of a conic section to determine which type of curve to graph, and then determine its specific characteristics. The first step is to rewrite the conic in standard form as we have done in the previous example. In other words, we need to rewrite the equation so that the denominator begins with 1. This enables us to determine e and, therefore, the shape of the curve. The next step is to substitute values for \theta  and solve for r to plot a few key points. Setting \theta  equal to 0,  \pi  __ 2 , \pi , and  3\pi  ___ 2  provides the vertices so we can create a rough sketch of the graph.

**Example  2**

### Graphing a Parabola in Polar Form
Graph r =  _________ 3 + 3 cos \theta  . Solution First, we rewrite the conic in standard form by multiplying the numerator and denominator by the reciprocal of 3, which is  1 __ 3 .

r =  _ 3 + 3 cos \theta   =  5  1 _ 3   

__

3  1 _ 3    + 3  1 _ 3    cos \theta  

r =   5 __ 3  _ 1 + cos \theta   Because e = 1, we will graph a parabola with a focus at the origin. The function has a cos \theta , and there is an addition sign in the denominator, so the directrix is x = p.

 5 __ 3  = ep

 5 __ 3  = (1)p

 5 __ 3  = p The directrix is x =  5 __ 3 . Plotting a few key points as in Table 1 will enable us to see the vertices. See Figure 3. A B C D \theta   \pi  __ 2  \pi   3\pi  ___ 2  r =  _________ 3 + 3 cos \theta    5  5 undefined  5 A Directrix B F D r x = 5

Analysis We can check our result with a graphing utility. See Figure 4.

**Example  3**

### Graphing a Hyperbola in Polar Form
Graph r =  _________ 2 - 3 sin \theta  . Solution First, we rewrite the conic in standard form by multiplying the numerator and denominator by the reciprocal of 2, which is  1 __ 2 .

r =  _ 2 - 3 sin \theta   =  8  1 _ 2   

__

2  1 _ 2    - 3  1 _ 2    sin \theta  

r =  _ 1 -  3 _ 2  cos \theta   Because e =  3 __ 2 , e > 1, so we will graph a hyperbola with a focus at the origin. The function has a sin \theta  term and there is a subtraction sign in the denominator, so the directrix is y = -p.

4 = ep

4 =   3 __ 2   p

4  2 __ 3    = p

 8 __ 3  = p The directrix is y = - 8 __ 3 . Plotting a few key points as in Table 2 will enable us to see the vertices. See Figure 5. A B C D \theta   \pi  __ 2  \pi   3\pi  ___ 2  r =  _________ 2 - 3 sin \theta   -8  8 __ A C D B r


**Example  4**

### Graphing an Ellipse in Polar Form
Graph r =  __________ 5 - 4 cos \theta .  Solution First, we rewrite the conic in standard form by multiplying the numerator and denominator by the reciprocal of 5, which is  1 __ 5 .

r =  _________ 5 - 4 cos \theta   =  _ 5   

__

5  1 _ 5    - 4  1 _ 5    cos \theta  

r =  _ 1 -  4 __ 5  sin \theta   Because e =  4 __ 5 , e < 1, so we will graph an ellipse with a focus at the origin. The function has a cos \theta , and there is a subtraction sign in the denominator, so the directrix is x = -p.

2 = ep

2 =   4 __ 5   p

2  5 __ 4    = p

 5 __ 2  = p The directrix is x = - 5 __ 2 . Plotting a few key points as in Table 3 will enable us to see the vertices. See Figure 6. A B C D \theta   \pi  __ 2  \pi   3\pi  ___ 2  r =  _________ 5 - 4 cos \theta    10 ___ D C B A r x = -5 Directrix


**Analysis**
We can check our result with a graphing utility. See Figure 7. _ 5 - 4 cos \theta   graphed on a viewing window of [-3, 12, 1] by [ -4, 4, 1], \theta  min = 0 and \theta  max = 2\pi .

**Try It #2**
Graph r =  _________ 4 - cos \theta .  Defining Conics in Terms of a Focus and a Directrix So far we have been using polar equations of conics to describe and graph the curve. Now we will work in reverse; we will use information about the origin, eccentricity, and directrix to determine the polar equation.

**How To…**
Given the focus, eccentricity, and directrix of a conic, determine the polar equation. 1. Determine whether the directrix is horizontal or vertical. If the directrix is given in terms of y, we use the general polar form in terms of sine. If the directrix is given in terms of x, we use the general polar form in terms of cosine. 2. Determine the sign in the denominator. If p < 0, use subtraction. If p > 0, use addition. 3. Write the coefficient of the trigonometric function as the given eccentricity. 4. Write the absolute value of p in the numerator, and simplify the equation.

**Example  5** — Finding the Polar Form of a Vertical Conic Given a Focus at the Origin and the Eccentricity and Directrix
Find the polar form of the conic given a focus at the origin, e = 3 and directrix y = - 2. Solution The directrix is y = -p, so we know the trigonometric function in the denominator is sine. Because y = -2, -2 < 0, so we know there is a subtraction sign in the denominator. We use the standard form of

r =  ep ________ 1 - esin \theta   and e = 3 and | -2 | = 2 = p. Therefore,

r =  (3)(2) _________ 1 - 3 sin \theta  

r =  _________ 1 - 3 sin \theta  

**Example  6**
Finding the Polar Form of a Horizontal Conic Given a Focus at the Origin and the Eccentricity and Directrix Find the polar form of a conic given a focus at the origin, e =  3 _ 5 , and directrix x = 4. Solution Because the directrix is x = p, we know the function in the denominator is cosine. Because x = 4, 4 > 0, so we know there is an addition sign in the denominator. We use the standard form of

r =  ep _________ 1 + e cos \theta   and e =  3 __ 5  and |4| = 4 = p.

Therefore,

r =    3 _ 5   (4) ___________ 1 +  3 _ 5  cos \theta  

r =   12 _ 5  ___________ 1 +  3 _ 5  cos \theta  

r =   12 _ 5  _______________

1   5 _ 5   +  3 _ 5  cos \theta  

r =   12 _ 5  ____________  5 _ 5  +  3 _ 5  cos \theta  

r =  12 _ 5  ⋅  _________ 5 + 3 cos \theta  

r =  _________ 5 + 3 cos \theta  

**Try It #3**
Find the polar form of the conic given a focus at the origin, e = 1, and directrix x = -1.

**Example  7**
Converting a Conic in Polar Form to Rectangular Form Convert the conic r =  _________ 5 - 5sin \theta   to rectangular form. Solution We will rearrange the formula to use the identities r = \sqrt{x} 2 + y^{2} , x = r cos \theta , and y = r sin \theta .

r =  _________ 5 - 5sin \theta  

r ⋅ (5 - 5 sin \theta ) =  _________ 5 - 5sin \theta   ⋅ (5 - 5 sin \theta ) Eliminate the fraction.

5r - 5r sin \theta  = 1 Distribute.

5r = 1 + 5r sin \theta  Isolate 5r.

25r 2 = (1 + 5r sin \theta )^{2} Square both sides.

25(x 2 + y 2) = (1 + 5y)^{2} Substitute r = \sqrt{x} 2 + y 2  and y = r sin \theta .

Distribute and use FOIL.

Rearrange terms and set equal to 1.

**Try It #4**
Convert the conic r =  __________ 1 + 2cos \theta   to rectangular form. Access these online resources for additional instruction and practice with conics in polar coordinates. • Polar Equations of Conic Sections (http://openstaxcollege.org/l/determineconic) • Graphing Polar Equations of Conics – 1 (http://openstaxcollege.org/l/graphconic^{1}) • Graphing Polar Equations of Conics – 2 (http://openstaxcollege.org/l/graphconic^{2})


### 10.5 Section Exercises
Verbal 1. Explain how eccentricity determines which conic section is given. 2. If a conic section is written as a polar equation, what must be true of the denominator? 3. If a conic section is written as a polar equation, and the denominator involves sin \theta , what conclusion can be drawn about the directrix? 4. If the directrix of a conic section is perpendicular to the polar axis, what do we know about the equation of the graph? 5. What do we know about the focus/foci of a conic section if it is written as a polar equation? Algebraic For the following exercises, identify the conic with a focus at the origin, and then give the directrix and eccentricity. 6. r =  __________ 1 - 2 cos \theta   7. r =  __________ 4 - 4 sin \theta   8. r =  __________ 4 - 3 cos \theta   9. r =  __________ 1 + 2 sin \theta   10. r =  __________ 4 + 3 cos \theta   11. r =  ____________

10 + 10 cos \theta   12. r =  ________ 1 - cos \theta   13. r =  __________ 7 + 2 cos \theta   14. r(1 - cos \theta ) = 3 15. r(3 + 5sin \theta ) = 11 16. r(4 - 5sin \theta ) = 1 17. r(7 + 8cos \theta ) = 7 For the following exercises, convert the polar equation of a conic section to a rectangular equation. 18. r =  __________ 1 + 3 sin \theta   19. r =  __________ 5 - 3 sin \theta   20. r =  __________ 3 - 2 cos \theta   21. r =  __________ 2 + 5 cos \theta   22. r =  __________ 2 + 2 sin \theta   23. r = __________ 8 - 8 cos \theta   24. r =  __________ 6 + 7 cos \theta   25. r =  ___________ 5 - 11 sin \theta   26. r(5 + 2 cos \theta ) = 6 27. r(2 - cos \theta ) = 1 29. r =  6sec \theta  ___________ -2 + 3 sec \theta   30. r =  6csc \theta  __________ 3 + 2 csc \theta   For the following exercises, graph the given conic section. If it is a parabola, label the vertex, focus, and directrix. If it is an ellipse, label the vertices and foci. If it is a hyperbola, label the vertices and foci. 31. r =  ________ 2 + cos \theta   32. r =  __________ 3 + 3 sin \theta   33. r =  __________ 5 - 4 sin \theta   34. r =  __________ 1 + 2 cos \theta   35. r =  __________ 4 - 5 cos \theta   36. r =  __________ 4 - 4 cos \theta   37. r =  _ 1 - sin \theta   38. r =  __________ 3 + 2 sin \theta   39. r(1 + cos \theta ) = 5 40. r(3 - 4sin \theta ) = 9 41. r(3 - 2sin \theta ) = 6 42. r(6 - 4cos \theta ) = 5 For the following exercises, find the polar equation of the conic with focus at the origin and the given eccentricity and directrix. 43. Directrix: x = 4; e =  1 __ 5  44. Directrix: x = - 4; e = 5 45. Directrix: y = 2; e = 2 46. Directrix: y = - 2; e =  1 __ 2  47. Directrix: x = 1; e = 1 48. Directrix: x = -1; e = 1 49. Directrix: x = - 1 __ 4 ; e =  7 __ 2  50. Directrix: y =  2 __ 5 ; e =  7 __ 2  51. Directrix: y = 4; e =  3 __ 2  52. Directrix: x = -2; e =  8 __ 3  53. Directrix: x = -5; e =  3 __ 4  54. Directrix: y = 2; e = 2.5 55. Directrix: x = -3; e =  1 __ 3  Extensions Recall from Rotation of Axes that equations of conics with an xy term have rotated graphs. For the following exercises, express each equation in polar form with r as a function of \theta . 57. x 2 + xy + y 2 = 4 60. 2xy + y = 1


### Key Terms
angle of rotation an acute angle formed by a set of axes rotated from the Cartesian plane where, if cot(2\theta ) > 0, then \theta  is between (0°, 45°); if cot(2\theta ) < 0, then \theta  is between (45°, 90°); and if cot(2\theta ) = 0, then \theta  = 45° center of a hyperbola the midpoint of both the transverse and conjugate axes of a hyperbola center of an ellipse the midpoint of both the major and minor axes conic section any shape resulting from the intersection of a right circular cone with a plane conjugate axis the axis of a hyperbola that is perpendicular to the transverse axis and has the co-vertices as its endpoints degenerate conic sections any of the possible shapes formed when a plane intersects a double cone through the apex. Types of degenerate conic sections include a point, a line, and intersecting lines. directrix a line perpendicular to the axis of symmetry of a parabola; a line such that the ratio of the distance between the points on the conic and the focus to the distance to the directrix is constant eccentricity the ratio of the distances from a point P on the graph to the focus F and to the directrix D represented by e =  PF ___ PD , where e is a positive real number ellipse the set of all points (x, y) in a plane such that the sum of their distances from two fixed points is a constant foci plural of focus focus (of a parabola) a fixed point in the interior of a parabola that lies on the axis of symmetry focus (of an ellipse) one of the two fixed points on the major axis of an ellipse such that the sum of the distances from these points to any point (x, y) on the ellipse is a constant hyperbola the set of all points (x, y) in a plane such that the difference of the distances between (x, y) and the foci is a positive constant latus rectum the line segment that passes through the focus of a parabola parallel to the directrix, with endpoints on the parabola major axis the longer of the two axes of an ellipse minor axis the shorter of the two axes of an ellipse nondegenerate conic section a shape formed by the intersection of a plane with a double right cone such that the plane does not pass through the apex; nondegenerate conics include circles, ellipses, hyperbolas, and parabolas parabola the set of all points (x, y) in a plane that are the same distance from a fixed line, called the directrix, and a fixed point (the focus) not on the directrix polar equation an equation of a curve in polar coordinates r and \theta  transverse axis the axis of a hyperbola that includes the foci and has the vertices as its endpoints Key Equations Horizontal ellipse, center at origin  x 2

__ a^{2}  +  y 2

__ b^{2}  = 1, a > b Vertical ellipse, center at origin  x 2

__ b^{2}  +  y 2

__ a^{2}  = 1, a > b Horizontal ellipse, center (h, k)  (x - h)^{2} _______ a^{2}  +  (y - k)^{2} _______ b^{2}  = 1, a > b Vertical ellipse, center (h, k)  (x - h)^{2} _______ b^{2}  +  (y - k)^{2} _______ a^{2}  = 1, a > b Hyperbola, center at origin, transverse axis on x-axis  x 2

__ a^{2}  -  y 2

__ b^{2}  = 1 Hyperbola, center at origin, transverse axis on y-axis  y 2

__ a^{2}  -  x 2

__ b^{2}  = 1

Hyperbola, center at (h, k), transverse axis parallel to x-axis  (x - h)^{2} _______ a^{2}  -  (y - k)^{2} _______ b^{2}  = 1 Hyperbola, center at (h, k), transverse axis parallel to y-axis  (y - k)^{2} _______ a^{2}  -  (x - h)^{2} _______ b^{2}  = 1 Parabola, vertex at origin, axis of symmetry on x-axis y 2 = 4px Parabola, vertex at origin, axis of symmetry on y-axis x 2 = 4py Parabola, vertex at (h, k), axis of symmetry on x-axis (y - k)^{2} = 4p(x - h) Parabola, vertex at (h, k), axis of symmetry on y-axis (x - h)^{2} = 4p(y - k) General Form equation of a conic section Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 Rotation of a conic section x = x' cos \theta  - y' sin \theta 

y = x' sin \theta  + y' cos \theta  Angle of rotation \theta , where cot(2\theta ) =  A - C ______ B 

### Key Concepts
• An ellipse is the set of all points (x, y) in a plane such that the sum of their distances from two fixed points is a constant. Each fixed point is called a focus (plural: foci). • When given the coordinates of the foci and vertices of an ellipse, we can write the equation of the ellipse in standard form. See Example 1 and Example 2. • When given an equation for an ellipse centered at the origin in standard form, we can identify its vertices, co-vertices, foci, and the lengths and positions of the major and minor axes in order to graph the ellipse. See

**Example 3** — and Example 4.
• When given the equation for an ellipse centered at some point other than the origin, we can identify its key features and graph the ellipse. See Example 5 and Example 6. • Real-world situations can be modeled using the standard equations of ellipses and then evaluated to find key features, such as lengths of axes and distance between foci. See Example 7. 10.2 The Hyperbola • A hyperbola is the set of all points (x, y) in a plane such that the difference of the distances between (x, y) and the foci is a positive constant. • The standard form of a hyperbola can be used to locate its vertices and foci. See Example 1. • When given the coordinates of the foci and vertices of a hyperbola, we can write the equation of the hyperbola in standard form. See Example 2 and Example 3. • When given an equation for a hyperbola, we can identify its vertices, co-vertices, foci, asymptotes, and lengths and positions of the transverse and conjugate axes in order to graph the hyperbola. See Example 4 and Example 5. • Real-world situations can be modeled using the standard equations of hyperbolas. For instance, given the dimensions of a natural draft cooling tower, we can find a hyperbolic equation that models its sides. See Example 6.

• A parabola is the set of all points (x, y) in a plane that are the same distance from a fixed line, called the directrix, and a fixed point (the focus) not on the directrix. • The standard form of a parabola with vertex (0, 0) and the x-axis as its axis of symmetry can be used to graph the parabola. If p > 0, the parabola opens right. If p < 0, the parabola opens left. See Example 1. • The standard form of a parabola with vertex (0, 0) and the y-axis as its axis of symmetry can be used to graph the parabola. If p > 0, the parabola opens up. If p < 0, the parabola opens down. See Example 2. • When given the focus and directrix of a parabola, we can write its equation in standard form. See Example 3. • The standard form of a parabola with vertex (h, k) and axis of symmetry parallel to the x-axis can be used to graph the parabola. If p > 0, the parabola opens right. If p < 0, the parabola opens left. See Example 4. • The standard form of a parabola with vertex (h, k) and axis of symmetry parallel to the y-axis can be used to graph the parabola. If p > 0, the parabola opens up. If p < 0, the parabola opens down. See Example 5. • Real-world situations can be modeled using the standard equations of parabolas. For instance, given the diameter and focus of a cross-section of a parabolic reflector, we can find an equation that models its sides. See Example 6. 10.4 Rotation of Axes • Four basic shapes can result from the intersection of a plane with a pair of right circular cones connected tail to tail. They include an ellipse, a circle, a hyperbola, and a parabola. • A nondegenerate conic section has the general form Ax 2 + Bxy + Cy 2 + Dx + Ey + F = 0 where A, B and C are not all zero. The values of A, B, and C determine the type of conic. See Example 1. • Equations of conic sections with an xy term have been rotated about the origin. See Example 2. • The general form can be transformed into an equation in the x' and y' coordinate system without the x' y' term. See Example 3 and Example 4. • An expression is described as invariant if it remains unchanged after rotating. Because the discriminant is invariant, observing it enables us to identify the conic section. See Example 5. 10.5 Conic Sections in Polar Coordinates • Any conic may be determined by a single focus, the corresponding eccentricity, and the directrix. We can also define a conic in terms of a fixed point, the focus P(r, \theta ) at the pole, and a line, the directrix, which is perpendicular to the polar axis. • A conic is the set of all points e =  PF ___ PD , where eccentricity e is a positive real number. Each conic may be written in terms of its polar equation. See Example 1. • The polar equations of conics can be graphed. See Example 2, Example 3, and Example 4. • Conics can be defined in terms of a focus, a directrix, and eccentricity. See Example 5 and Example 6. • We can use the identities r = \sqrt{x} 2 + y 2 , x = r cos \theta , and y = r sin \theta  to convert the equation for a conic from polar to rectangular form. See Example 7.

The Ellipse For the following exercises, write the equation of the ellipse in standard form. Then identify the center, vertices, and foci.

___ 25  +  y 2

___ 2.  (x - 2)^{2} _______ 100  +  (y + 3)^{2} _______ 36  = 1 3. 9x 2 + y 2 + 54x - 4y + 76 = 0 For the following exercises, graph the ellipse, noting center, vertices, and foci.

___ 36  +  y 2

__ 9  = 1 6.  (x - 4)^{2} _______  +  (y + 3)^{2} _______  = 1 7. 4x 2 + y 2 + 16x + 4y - 44 = 0 For the following exercises, use the given information to find the equation for the ellipse. 9. Center at (0, 0), focus at (3, 0), vertex at (-5, 0) 10. Center at (2, -2), vertex at (7, -2), focus at (4, -2) 11. A whispering gallery is to be constructed such that the foci are located 35 feet from the center. If the length of the gallery is to be 100 feet, what should the height of the ceiling be? The Hyperbola For the following exercises, write the equation of the hyperbola in standard form. Then give the center, vertices, and foci.

___ 81  -  y 2

__ 9  = 1 _______  -  (x - 4)^{2} _______  = 1 15. 3x 2 - y 2 - 12x - 6y - 9 = 0 For the following exercises, graph the hyperbola, labeling vertices and foci.

__ 9  -  y 2

___ _______  -  (x + 1)^{2} _______  = 1 For the following exercises, find the equation of the hyperbola. 20. Center at (0, 0), vertex at (0, 4), focus at (0, -6) 21. Foci at (3, 7) and (7, 7), vertex at (6, 7) The Parabola For the following exercises, write the equation of the parabola in standard form. Then give the vertex, focus, and directrix. 23. (x + 2)^{2} =  1 __ 2 (y - 1) 24. y 2 - 6y - 6x - 3 = 0 25. x 2 + 10x - y + 23 = 0 For the following exercises, graph the parabola, labeling vertex, focus, and directrix. 27. (y - 1)^{2} =  1 __ 2 (x + 3)

For the following exercises, write the equation of the parabola using the given information. 30. Focus at (-4, 0); directrix is x = 4 31. Focus at  2,  9 _ 8   ; directrix is y =  7 _ 8  32. A cable TV receiving dish is the shape of a paraboloid of revolution. Find the location of the receiver, which is placed at the focus, if the dish is 5 feet across at its opening and 1.5 feet deep. Rotation of Axes For the following exercises, determine which of the conic sections is represented. 35. 4x 2 + xy + 2y 2 + 8x - 26y + 9 = 0 For the following exercises, determine the angle \theta  that will eliminate the xy term, and write the corresponding equation without the xy term. 36. x 2 + 4xy - 2y 2 - 6 = 0 37. x 2 - xy + y 2 - 6 = 0 For the following exercises, graph the equation relative to the x'y' system in which the equation has no x'y' term. 39. x 2 - xy + y 2 - 2 = 0 Conic Sections in Polar Coordinates For the following exercises, given the polar equation of the conic with focus at the origin, identify the eccentricity and directrix. 41. r =  _________ 1 - 5 cos \theta   42. r =  _________ 3 + 2 cos \theta   43. r =  _________ 4 + 3 sin \theta   44. r =  _________ 5 - 5 sin \theta   For the following exercises, graph the conic given in polar form. If it is a parabola, label the vertex, focus, and directrix. If it is an ellipse or a hyperbola, label the vertices and foci. 45. r =  ________ 1 - sin \theta   46. r =  _________ 4 + 3 sin \theta   47. r =  _________ 4 + 5 cos \theta   48. r =  _________ 3 - 6 cos \theta   For the following exercises, given information about the graph of a conic with focus at the origin, find the equation in polar form. 49. Directrix is x = 3 and eccentricity e = 1 50. Directrix is y = -2 and eccentricity e = 4

For the following exercises, write the equation in standard form and state the center, vertices, and foci.

__ 9  +  y 2

__ 4  = 1 For the following exercises, sketch the graph, identifying the center, vertices, and foci. 3.  (x - 3)^{2} _______  +  (y - 2)^{2} _______  = 1 4. 2x 2 + y 2 + 8x - 6y - 7 = 0 5. Write the standard form equation of an ellipse with a center at (1, 2), vertex at (7, 2), and focus at (4, 2). 6. A whispering gallery is to be constructed with a length of 150 feet. If the foci are to be located 20 feet away from the wall, how high should the ceiling be? For the following exercises, write the equation of the hyperbola in standard form, and give the center, vertices, foci, and asymptotes.

___ 49  -  y 2

___ For the following exercises, graph the hyperbola, noting its center, vertices, and foci. State the equations of the asymptotes. 9.  (x - 3)^{2} _______  -  (y + 3)^{2} _______  = 1 10. y 2 - x 2 + 4y - 4x - 18 = 0 11. Write the standard form equation of a hyperbola with foci at (1, 0) and (1, 6), and a vertex at (1, 2). For the following exercises, write the equation of the parabola in standard form, and give the vertex, focus, and equation of the directrix. For the following exercises, graph the parabola, labeling the vertex, focus, and directrix. 14. (x - 1)^{2} = -4(y + 3) 15. y 2 + 8x - 8y + 40 = 0 16. Write the equation of a parabola with a focus at (2, 3) and directrix y = -1. 17. A searchlight is shaped like a paraboloid of revolution. If the light source is located 1.5 feet from the base along the axis of symmetry, and the depth of the searchlight is 3 feet, what should the width of the opening be? For the following exercises, determine which conic section is represented by the given equation, and then determine the angle \theta  that will eliminate the xy term. 19. x 2 + 4xy + 4y 2 + 6x - 8y = 0 For the following exercises, rewrite in the x'y' system without the x'y' term, and graph the rotated graph.

3 xy + y 2 = 4 For the following exercises, identify the conic with focus at the origin, and then give the directrix and eccentricity. 22. r =  ________ 2 - sin \theta   23. r =  _________ 4 + 6 cos \theta   For the following exercises, graph the given conic section. If it is a parabola, label vertex, focus, and directrix. If it is an ellipse or a hyperbola, label vertices and foci. 24. r =  _________ 4 - 8 sin \theta   25. r =  _________ 4 + 4 sin \theta   26. Find a polar equation of the conic with focus at the origin, eccentricity of e = 2, and directrix: x = 3.
