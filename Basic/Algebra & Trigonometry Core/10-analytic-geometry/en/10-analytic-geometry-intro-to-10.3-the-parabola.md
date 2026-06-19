# Analytic Geometry

## Introduction

---
The Greek mathematician Menaechmus (c. 380–c. 320 BCE) is generally credited with discovering the shapes formed by the intersection of a plane and a right circular cone. Depending on how he tilted the plane when it intersected the cone, he formed different shapes at the intersection—beautiful shapes with near-perfect symmetry. It was also said that Aristotle may have had an intuitive understanding of these shapes, as he observed the orbit of the planet to be circular. He presumed that the planets moved in circular orbits around Earth, and for nearly 2,000 years this was the commonly held belief. It was not until the Renaissance movement that Johannes Kepler noticed that the orbits of the planet were not circular in nature. His published law of planetary motion in the 1600s changed our view of the solar system forever. He claimed that the sun was at one end of the orbits, and the planets revolved around the sun in an oval-shaped path. In this chapter, we will investigate the two-dimensional figures that are formed when a right circular cone is intersected by a plane. We will begin by studying each of three figures created in this manner. We will develop defining equations for each figure and then learn how to use these equations to solve a variety of problems. a b

Learning Objectives
In this section, you will:
• Write equations of ellipses in standard form.
• Graph ellipses centered at the origin.
• Graph ellipses not centered at the origin.
• Solve applied problems involving ellipses.

## 10.1 The Ellipse

---
Can you imagine standing at one end of a large room and still being able to hear a whisper from a person standing at the other end? The National Statuary Hall in Washington, D.C., shown in Figure 1, is such a room.[33] It is an oval- shaped room called a whispering chamber because the shape makes it possible for sound to travel along the walls. In this section, we will investigate the shape of this room and its real-world applications, including how far apart two people in Statuary Hall can stand and still hear each other whisper. Writing Equations of Ellipses in Standard Form A conic section, or conic, is a shape resulting from intersecting a right circular cone with a plane. The angle at which the plane intersects the cone determines the shape, as shown in Figure 2. Ellipse Hyperbola Parabola Conic sections can also be described by a set of points in the coordinate plane. Later in this chapter, we will see that the graph of any quadratic equation in two variables is a conic section. The signs of the equations and the coefficients of the variable terms determine the shape. This section focuses on the four variations of the standard form of the 33. Architect of the Capitol. http://www.aoc.gov. Accessed April 15, 2014.

equation for the ellipse. An ellipse is the set of all points (x, y) in a plane such that the sum of their distances from two fixed points is a constant. Each fixed point is called a focus (plural: foci). We can draw an ellipse using a piece of cardboard, two thumbtacks, a pencil, and string. Place the thumbtacks in the cardboard to form the foci of the ellipse. Cut a piece of string longer than the distance between the two thumbtacks (the length of the string represents the constant in the definition). Tack each end of the string to the cardboard, and trace a curve with a pencil held taut against the string. The result is an ellipse. See Figure 3. Foci Every ellipse has two axes of symmetry. The longer axis is called the major axis, and the shorter axis is called the minor axis. Each endpoint of the major axis is the vertex of the ellipse (plural: vertices), and each endpoint of the minor axis is a co-vertex of the ellipse. The center of an ellipse is the midpoint of both the major and minor axes. The axes are perpendicular at the center. The foci always lie on the major axis, and the sum of the distances from the foci to any point on the ellipse (the constant sum) is greater than the distance between the foci. See Figure 4. Co-vertex Vertex Co-vertex Minor Axis Major Axis Center Focus Focus x y Vertex In this section, we restrict ellipses to those that are positioned vertically or horizontally in the coordinate plane. That is, the axes will either lie on or be parallel to the x- and y-axes. Later in the chapter, we will see ellipses that are rotated in the coordinate plane. To work with horizontal and vertical ellipses in the coordinate plane, we consider two cases: those that are centered at the origin and those that are centered at a point other than the origin. First we will learn to derive the equations of ellipses, and then we will learn how to write the equations of ellipses in standard form. Later we will use what we learn to draw the graphs.

Deriving the Equation of an Ellipse Centered at the Origin To derive the equation of an ellipse centered at the origin, we begin with the foci (-c, 0) and (c, 0). The ellipse is the set of all points (x, y) such that the sum of the distances from (x, y) to the foci is constant, as shown in Figure 5. y x (x, y) (a, 0) (c, 0) (–c, 0) (–a, 0) d¹ d² If (a, 0) is a vertex of the ellipse, the distance from (-c, 0) to (a, 0) is a - ( -c) = a + c. The distance from (c, 0) to (a, 0) is a - c . The sum of the distances from the foci to the vertex is

(a + c) + (a - c) = 2a If (x, y) is a point on the ellipse, then we can define the following variables:

d¹ = the distance from (-c, 0) to (x, y)

d² = the distance from (c, 0) to (x, y) By the definition of an ellipse, d¹ + d² is constant for any point (x, y) on the ellipse. We know that the sum of these distances is 2a for the vertex (a, 0). It follows that d¹ + d² = 2a for any point on the ellipse. We will begin the derivation by applying the distance formula. The rest of the derivation is algebraic.

d¹ + d² = √—

(x - ( - c))² + (y - 0)²  + √(x - c)² + (y - 0)²  = 2a Distance formula √(x + c)² + y 2  + √(x - c)² + y 2  = 2a Simplify expressions.

√(x + c)² + y 2  = 2a - √(x - c)² + y 2  Move radical to opposite side.

(x + c)² + y 2 = [2a -√(x - c)² + y 2 ]  Square both sides.

x 2 + 2cx + c² + y 2 = 4a² - 4a√(x - c)² + y 2  + (x - c)² + y 2 Expand the squares.

x 2 + 2cx + c² + y 2 = 4a² - 4a√(x - c)² + y 2  + x 2 - 2cx + c² + y 2 Expand remaining squares.

2cx = 4a² - 4a√(x - c)² + y 2  - 2cx Combine like terms.

4cx - 4a² = -4a√(x - c)² + y 2  Isolate the radical.

cx - a² = - a √(x - c)² + y 2  Divide by 4.

[ cx - a² ]  2 = a² [ √(x - c)² + y 2  ]   Square both sides.

c² x 2 - 2a² cx + a⁴ = a² ( x 2 - 2cx + c² + y 2 )  Expand the squares.

c² x 2 - 2a² cx + a⁴ = a² x 2 - 2a² cx + a² c² + a² y 2 Distribute a².

a² x 2 - c² x 2 + a² y 2 = a⁴ - a² c² Rewrite.

x 2(a² - c²) + a² y 2 = a²(a² - c²) Factor common terms.

x 2 b² + a² y 2 = a² b² Set b² = a² - c².

 x 2b² ____ a²b²  +  a²y 2 ____ a²b²  =  a²b² ____ a²b²  Divide both sides by a²b².

 x 2/a²  +  y 2/b²  = 1 Simplify. Thus, the standard equation of an ellipse is  x 2/a²  +  y 2/b²  = 1. This equation defines an ellipse centered at the origin. If a > b, the ellipse is stretched further in the horizontal direction, and if b > a, the ellipse is stretched further in the vertical direction.

### Writing Equations of Ellipses Centered at the Origin in Standard Form

Standard forms of equations tell us about key features of graphs. Take a moment to recall some of the standard forms of equations we’ve worked with in the past: linear, quadratic, cubic, exponential, logarithmic, and so on. By learning to interpret standard forms of equations, we are bridging the relationship between algebraic and geometric representations of mathematical phenomena. The key features of the ellipse are its center, vertices, co-vertices, foci, and lengths and positions of the major and minor axes. Just as with other equations, we can identify all of these features just by looking at the standard form of the equation. There are four variations of the standard form of the ellipse. These variations are categorized first by the location of the center (the origin or not the origin), and then by the position (horizontal or vertical). Each is presented along with a description of how the parts of the equation relate to the graph. Interpreting these parts allows us to form a mental picture of the ellipse. standard forms of the equation of an ellipse with center (0, 0) The standard form of the equation of an ellipse with center (0, 0) and major axis on the x-axis is  x 2/a²  +  y 2/b²  = 1 where • a > b • the length of the major axis is 2a • the coordinates of the vertices are (± a, 0) • the length of the minor axis is 2b • the coordinates of the co-vertices are (0, ± b) • the coordinates of the foci are (± c, 0) , where c² = a² - b². See Figure 6a. The standard form of the equation of an ellipse with center (0, 0) and major axis on the y-axis is  x 2/b²  +  y 2/a²  = 1 where • a > b • the length of the major axis is 2a • the coordinates of the vertices are (0, ±  a) • the length of the minor axis is 2b • the coordinates of the co-vertices are (± b, 0) • the coordinates of the foci are (0, ±  c) , where c² = a² - b². See Figure 6b. Note that the vertices, co-vertices, and foci are related by the equation c² = a² - b². When we are given the coordinates of the foci and vertices of an ellipse, we can use this relationship to find the equation of the ellipse in standard form. (0, b) (c, 0) (-a, 0) (-c, 0) (0, a) (0, -a) (0, -b) (a) (b) (0, -c) (0, c) (-b, 0) (b, 0) (a, 0) Major Axis Minor Axis Minor Axis Major Axis x x y y

---
### 💡 **How To…**
Given the vertices and foci of an ellipse centered at the origin, write its equation in standard form. 1. Determine whether the major axis lies on the x- or y-axis.

a. If the given coordinates of the vertices and foci have the form (± a, 0) and ( ± c, 0) respectively, then the major axis is the x-axis. Use the standard form  x 2/a²  +  y 2/b²  = 1.

b. If the given coordinates of the vertices and foci have the form (0, ± a) and ( ± c, 0), respectively, then the major axis is the y-axis. Use the standard form  x 2/b²  +  y 2/a²  = 1. 2. Use the equation c² = a² - b², along with the given coordinates of the vertices and foci, to solve for b². 3. Substitute the values for a² and b² into the standard form of the equation determined in Step 1.

---
### 📐 **Example  1**: Writing the Equation of an Ellipse Centered at the Origin in Standard Form

What is the standard form equation of the ellipse that has vertices (± 8, 0) and foci (± 5, 0)?

**Solution**

The foci are on the x-axis, so the major axis is the x-axis. Thus, the equation will have the form

 x 2/a²  +  y 2/b²  = 1 The vertices are (± 8, 0), so a = 8 and a² = 64. The foci are (± 5, 0), so c = 5 and c² = 25. We know that the vertices and foci are related by the equation c 2 = a 2 - b 2. Solving for b 2, we have:

c 2 = a 2 - b²

Substitute for c 2 and a 2.

Solve for b². Now we need only substitute a² = 64 and b² = 39 into the standard form of the equation. The equation of the ellipse is  x 2/64  +  y 2

_

---
### ✏️ **Try It #1**
What is the standard form equation of the ellipse that has vertices (0, ±  4) and foci (0, ±  √15 )? Can we write the equation of an ellipse centered at the origin given coordinates of just one focus and vertex? Yes. Ellipses are symmetrical, so the coordinates of the vertices of an ellipse centered around the origin will always have the form (± a, 0) or (0, ±  a). Similarly, the coordinates of the foci will always have the form (± c, 0) or (0, ±  c). Knowing this, we can use a and c from the given points, along with the equation c² = a² - b², to find b². Writing Equations of Ellipses Not Centered at the Origin Like the graphs of other equations, the graph of an ellipse can be translated. If an ellipse is translated h units horizontally and k units vertically, the center of the ellipse will be (h, k). This translation results in the standard form of the equation we saw previously, with x replaced by (x - h) and y replaced by (y - k).

standard forms of the equation of an ellipse with center (h, k) The standard form of the equation of an ellipse with center (h, k) and major axis parallel to the x-axis is  (x - h)² _ a²  +  (y - k)² _ b²  = 1 where • a > b • the length of the major axis is 2a • the coordinates of the vertices are (h ±  a, k) • the length of the minor axis is 2b • the coordinates of the co-vertices are (h, k ±  b) • the coordinates of the foci are (h ±  c, k), where c² = a² - b². See Figure 7a. The standard form of the equation of an ellipse with center (h, k) and major axis parallel to the y-axis is  (x - h)² _ b²  +  (y - k)² _ a²  = 1 where • a > b • the length of the major axis is 2a • the coordinates of the vertices are (h, k ±  a) • the length of the minor axis is 2b • the coordinates of the co-vertices are (h ±  b, k) • the coordinates of the foci are (h, k ±  c), where c² = a² - b². See Figure 7b. Just as with ellipses centered at the origin, ellipses that are centered at a point (h, k) have vertices, co-vertices, and foci that are related by the equation c² = a² - b². We can use this relationship along with the midpoint and distance formulas to find the equation of the ellipse in standard form when the vertices and foci are given. y y x x (h + c¹, k) (h, k - a) (h, k - c) (h, k - b) (h, k) (h, k) (h, k + b) (h + a, k) (h + b, k) (h, k + a) (h, k + c) (h - a, k) (h - b, k) (h - c¹, k) Major Axis Major Axis Minor Axis Minor Axis (a) (b)

---
### 💡 **How To…**
Given the vertices and foci of an ellipse not centered at the origin, write its equation in standard form. 1. Determine whether the major axis is parallel to the x- or y-axis. a. If the y-coordinates of the given vertices and foci are the same, then the major axis is parallel to the x-axis. Use the standard form  (x - h)² _ a²  +  (y - k)² _ b²  = 1. b. If the x-coordinates of the given vertices and foci are the same, then the major axis is parallel to the y-axis. Use the standard form  (x - h)² _ b²  +  (y - k)² _ a²  = 1.

2. Identify the center of the ellipse (h, k) using the midpoint formula and the given coordinates for the vertices. 3. Find a² by solving for the length of the major axis, 2a, which is the distance between the given vertices. 4. Find c² using h and k, found in Step 2, along with the given coordinates for the foci. 5. Solve for b² using the equation c² = a² - b². 6. Substitute the values for h, k, a², and b² into the standard form of the equation determined in Step 1.

---
### 📐 **Example  2**
Writing the Equation of an Ellipse Centered at a Point Other Than the Origin What is the standard form equation of the ellipse that has vertices (-2, -8) and (-2, 2) and foci (-2, -7) and (-2, 1)?

**Solution**

The x-coordinates of the vertices and foci are the same, so the major axis is parallel to the y-axis. Thus, the equation of the ellipse will have the form

 (x - h)² _ b²  +  (y - k)² _ a²  = 1 First, we identify the center, (h, k). The center is halfway between the vertices, (-2, - 8) and (-2, 2). Applying the midpoint formula, we have:

(h, k) = (  -2 + (-2) _________  ,  -8 + 2 _______  ) 

= (-2, -3) Next, we find a². The length of the major axis, 2a, is bounded by the vertices. We solve for a by finding the distance between the y-coordinates of the vertices.

2a = 2 - (-8)

a = 5 Now we find c². The foci are given by (h, k ±  c). So, (h, k - c) = (-2, -7) and (h, k + c) = (-2, 1). We substitute k = -3 using either of these points to solve for c.

k + c = 1

-3 + c = 1

c = 4 Next, we solve for b² using the equation c² = a² - b².

c² = a² - b²

b² = 9 Finally, we substitute the values found for h, k, a², and b² into the standard form equation for an ellipse:

 (x + 2)² _  +  (y + 3)² _  = 1

---
### ✏️ **Try It #2**
What is the standard form equation of the ellipse that has vertices (-3, 3) and (5, 3) and foci (1 - 2√3 , 3) and (1 + 2√Graphing Ellipses Centered at the Origin Just as we can write the equation for an ellipse given its graph, we can graph an ellipse given its equation. To graph ellipses centered at the origin, we use the standard form  x 2/a²  +  y 2/b²  = 1, a > b for horizontal ellipses and  x 2/b²  +  y 2/a²  = 1, a > b for vertical ellipses.

---
### 💡 **How To…**
Given the standard form of an equation for an ellipse centered at (0, 0), sketch the graph. 1. Use the standard forms of the equations of an ellipse to determine the major axis, vertices, co-vertices, and foci. a. If the equation is in the form  x 2/a²  +  y 2/b²  = 1, where a > b, then • the major axis is the x-axis • the coordinates of the vertices are (± a, 0) • the coordinates of the co-vertices are (0, ±  b) • the coordinates of the foci are (± c, 0) b. If the equation is in the form  x 2/b²  +  y 2/a²  = 1, where a > b, then • the major axis is the y-axis • the coordinates of the vertices are (0, ±  a) • the coordinates of the co-vertices are (± b, 0) • the coordinates of the foci are (0, ±  c) 2. Solve for c using the equation c² = a² - b². 3. Plot the center, vertices, co-vertices, and foci in the coordinate plane, and draw a smooth curve to form the ellipse.

---
### 📐 **Example  3**: Graphing an Ellipse Centered at the Origin

Graph the ellipse given by the equation,  x 2/9  +  y 2/25  = 1. Identify and label the center, vertices, co-vertices, and foci.

**Solution**

First, we determine the position of the major axis. Because 25 > 9, the major axis is on the y-axis. Therefore, the equation is in the form  x 2/b 2  +  y 2/a 2  = 1, where b 2 = 9 and a² = 25. It follows that: • the center of the ellipse is (0, 0) • the coordinates of the vertices are (0, ±  a) = (0, ±  √25 ) = (0, ±  5) • the coordinates of the co-vertices are (± b, 0) = (±  √• the coordinates of the foci are (0, ±  c), where c 2 = a 2 - b 2 Solving for c, we have:

c = ±  √a² - b² 

= ±  √—

= ±  √16 

= ±  4 Therefore, the coordinates of the foci are (0, ±  4). Next, we plot and label the center, vertices, co-vertices, and foci, and draw a smooth curve to form the ellipse. See y x

---
### ✏️ **Try It #3**
Graph the ellipse given by the equation  x 2/36  +  y 2/4  = 1. Identify and label the center, vertices, co-vertices, and foci.

---
### 📐 **Example  4**
Graphing an Ellipse Centered at the Origin from an Equation Not in Standard Form Graph the ellipse given by the equation 4x 2 + 25y 2 = 100. Rewrite the equation in standard form. Then identify and label the center, vertices, co-vertices, and foci.

**Solution**

First, use algebra to rewrite the equation in standard form.

 4x 2 ____ _ ___ 100 

 x 2/25  +  y 2/4  = 1 Next, we determine the position of the major axis. Because 25 > 4, the major axis is on the x-axis. Therefore, the equation is in the form  x 2/a²  +  y 2/b²  = 1, where a² = 25 and b² = 4. It follows that: • the center of the ellipse is (0, 0) • the coordinates of the vertices are (± a, 0) = (± √• the coordinates of the co-vertices are (0, ±  b) = (0, ±  √4 ) = (0, ±  2) • the coordinates of the foci are (± c, 0), where c 2 = a 2 - b 2. Solving for c, we have:

c = ±  √a² - b² 

= ±  √—

= ±  √21  Therefore the coordinates of the foci are (±  √Next, we plot and label the center, vertices, co-vertices, and foci, and draw a smooth curve to form the ellipse. See y x

---
### ✏️ **Try It #4**
Graph the ellipse given by the equation 49x 2 + 16y 2 = 784. Rewrite the equation in standard form. Then identify and label the center, vertices, co-vertices, and foci. Graphing Ellipses Not Centered at the Origin When an ellipse is not centered at the origin, we can still use the standard forms to find the key features of the graph. When the ellipse is centered at some point, (h, k), we use the standard forms  (x - h)² _ a 2  +  (y - k)² _ b 2  = 1, a > b for horizontal ellipses and  (x - h)² _ b 2  +  (y - k)² _ a²  = 1, a > b for vertical ellipses. From these standard equations, we can easily determine the center, vertices, co-vertices, foci, and positions of the major and minor axes.

---
### 💡 **How To…**
Given the standard form of an equation for an ellipse centered at (h, k), sketch the graph. 1. Use the standard forms of the equations of an ellipse to determine the center, position of the major axis, vertices, co-vertices, and foci. a. If the equation is in the form  (x - h)² _ a²  +  (y - k)² _ b²  = 1, where a > b, then • the center is (h, k) • the major axis is parallel to the x-axis • the coordinates of the vertices are (h ±  a, k) • the coordinates of the co-vertices are (h, k ±  b) • the coordinates of the foci are (h ±  c, k) b. If the equation is in the form  (x - h)² _ b²  +  (y - k)² _ a²  = 1, where a > b, then • the center is (h, k) • the major axis is parallel to the y-axis • the coordinates of the vertices are (h, k ±  a) • the coordinates of the co-vertices are (h ±  b, k) • the coordinates of the foci are (h, k ±  c) 2. Solve for c using the equation c 2 = a² - b². 3. Plot the center, vertices, co-vertices, and foci in the coordinate plane, and draw a smooth curve to form the ellipse.

---
### 📐 **Example  5**: Graphing an Ellipse Centered at (h, k)

Graph the ellipse given by the equation,  (x + 2)² _  +  (y - 5)² _  = 1. Identify and label the center, vertices, co-vertices, and foci.

**Solution**

First, we determine the position of the major axis. Because 9 > 4, the major axis is parallel to the y-axis. Therefore, the equation is in the form  (x - h)² _ b²  +  (y - k)² _ a²  = 1, where b² = 4 and a² = 9. It follows that: • the center of the ellipse is (h, k) = (-2, 5) • the coordinates of the vertices are (h, k ±  a) = (-2, 5 ±  √9 ) = (-2, 5 ±  3), or (-2, 2) and (-2, 8) • the coordinates of the co-vertices are (h ±  b, k) = (-2 ±  √4 , 5) = (-2 ±  2, 5), or (-4, 5) and (0, 5) • the coordinates of the foci are (h, k ±  c), where c 2 = a 2 - b 2. Solving for c, we have:

c = ±  √a² - b² 

= ±  √9 - 4 

= ±  √5  Therefore, the coordinates of the foci are (-2, 5 -√5 ) and (-2, 5 + √5 ). Next, we plot and label the center, vertices, co-vertices, and foci, and draw a smooth curve to form the ellipse. (-2, 5 + √5) y x

---
### ✏️ **Try It #5**
Graph the ellipse given by the equation  (x - 4)² _  +  (y - 2)² _  = 1. Identify and label the center, vertices, co-vertices, and foci.

---
### 💡 **How To…**
Given the general form of an equation for an ellipse centered at (h, k), express the equation in standard form. 1. Recognize that an ellipse described by an equation in the form ax 2 + by 2 + cx + dy + e = 0 is in general form. 2. Rearrange the equation by grouping terms that contain the same variable. Move the constant term to the opposite side of the equation. 3. Factor out the coefficients of the x 2 and y 2 terms in preparation for completing the square. 4. Complete the square for each variable to rewrite the equation in the form of the sum of multiples of two binomials squared set equal to a constant, m¹ (x - h)² + m²(y - k)² = m³, where m¹, m², and m³ are constants. 5. Divide both sides of the equation by the constant term to express the equation in standard form.

---
### 📐 **Example  6**
Graphing an Ellipse Centered at ( h, k) by First Writing It in Standard Form Graph the ellipse given by the equation 4x 2 + 9y 2 - 40x + 36y + 100 = 0. Identify and label the center, vertices, co-vertices, and foci.

**Solution**

We must begin by rewriting the equation in standard form.

Group terms that contain the same variable, and move the constant to the opposite side of the equation.

(4x 2 - 40x) + (9y 2 + 36y) = -100 Factor out the coefficients of the squared terms.

4(x 2 - 10x)+ 9(y 2 + 4y) = -100 Complete the square twice. Remember to balance the equation by adding the same constants to each side.

4(x 2 - 10x + 25)+ 9(y 2 + 4y + 4) = -100 + 100 + 36 Rewrite as perfect squares.

4(x - 5)² + 9(y + 2)² = 36 Divide both sides by the constant term to place the equation in standard form.

 (x - 5)² _  +  (y + 2)² _  = 1 Now that the equation is in standard form, we can determine the position of the major axis. Because 9 > 4, the major axis is parallel to the x-axis. Therefore, the equation is in the form  (x - h)² _ a²  +  (y - k)² _ b²  = 1, where a² = 9 and b² = 4. It follows that: • the center of the ellipse is (h, k) = (5, -2) • the coordinates of the vertices are (h ±  a, k) = (5 ±  √— 9 , -2) = (5 ±  3, -2), or (2, -2) and (8, -2) • the coordinates of the co-vertices are (h, k ±  b) = (5, -2 ±  √— 4 )= (5, -2 ±  2), or (5, -4) and (5, 0) • the coordinates of the foci are (h ±  c, k), where c² = a² - b². Solving for c, we have:

c = ±  √a² - b² 

= ±  √9 - 4 

= ±  √5  Therefore, the coordinates of the foci are (5 - √5 , -2) and (5 + √Next we plot and label the center, vertices, co-vertices, and foci, and draw a smooth curve to form the ellipse as shown in Figure 11.

9 x

---
### ✏️ **Try It #6**
Express the equation of the ellipse given in standard form. Identify the center, vertices, co-vertices, and foci of the ellipse. 4x 2 + y 2 - 24x + 2y + 21 = 0 Solving Applied Problems Involving Ellipses Many real-world situations can be represented by ellipses, including orbits of planets, satellites, moons and comets, and shapes of boat keels, rudders, and some airplane wings. A medical device called a lithotripter uses elliptical reflectors to break up kidney stones by generating sound waves. Some buildings, called whispering chambers, are designed with elliptical domes so that a person whispering at one focus can easily be heard by someone standing at the other focus. This occurs because of the acoustic properties of an ellipse. When a sound wave originates at one focus of a whispering chamber, the sound wave will be reflected off the elliptical dome and back to the other focus. See Figure 12. In the whisper chamber at the Museum of Science and Industry in Chicago, two people standing at the foci—about 43 feet apart—can hear each other whisper.

---
### 📐 **Example  7**
Locating the Foci of a Whispering Chamber The Statuary Hall in the Capitol Building in Washington, D.C. is a whispering chamber. Its dimensions are 46 feet wide by 96 feet long as shown in Figure 13. a. What is the standard form of the equation of the ellipse representing the outline of the room? Hint: assume a horizontal ellipse, and let the center of the room be the point (0, 0). b. If two senators standing at the foci of this room can hear each other whisper, how far apart are the senators? Round to the nearest foot. 96 feet 46 feet

**Solution**

a. We are assuming a horizontal ellipse with center (0, 0), so we need to find an equation of the form  x 2/a²  +  y 2/b²  = 1, where a > b. We know that the length of the major axis, 2a, is longer than the length of the minor axis, 2b. So the length of the room, 96, is represented by the major axis, and the width of the room, 46, is represented by the minor axis. • Solving for a, we have 2a = 96, so a = 48, and a² = 2304. • Solving for b, we have 2b = 46, so b = 23, and b² = 529. Therefore, the equation of the ellipse is  x 2/2304  +  y 2/b. To find the distance between the senators, we must find the distance between the foci, (± c, 0), where c² = a² - b². Solving for c, we have:

c² = a² - b²

Substitute using the values found in part (a).

c = ±  √Take the square root of both sides.

c = ±  √Subtract.

c ≈ ±  42 Round to the nearest foot. The points (± 42, 0) represent the foci. Thus, the distance between the senators is 2(42) = 84 feet.

---
### ✏️ **Try It #7**
Suppose a whispering chamber is 480 feet long and 320 feet wide. a. What is the standard form of the equation of the ellipse representing the room? Hint: assume a horizontal ellipse, and let the center of the room be the point (0, 0). b. If two people are standing at the foci of this room and can hear each other whisper, how far apart are the people? Round to the nearest foot. Access these online resources for additional instruction and practice with ellipses. • Conic Sections: The Ellipse (http://openstaxcollege.org/l/conicellipse) • Graph an Ellipse with Center at the Origin (http://openstaxcollege.org/l/grphellorigin) • Graph an Ellipse with Center Not at the Origin (http://openstaxcollege.org/l/grphellnot)

## 10.1 Section Exercises

---
### 10.1 Section Exercises

Verbal 1. Define an ellipse in terms of its foci. 2. Where must the foci of an ellipse lie? 3. What special case of the ellipse do we have when the major and minor axis are of the same length? 4. For the special case mentioned in the previous question, what would be true about the foci of that ellipse? 5. What can be said about the symmetry of the graph of an ellipse with center at the origin and foci along the y-axis? Algebraic For the following exercises, determine whether the given equations represent ellipses. If yes, write in standard form. 6. 2x 2 + y = 4 For the following exercises, write the equation of an ellipse in standard form, and identify the end points of the major and minor axes as well as the foci.

_ 4  +  y 2

_ _ 100  +  y 2

_ _______  +  (y - 4)² _______  = 1 _  +  (y + 1)² _  = 1 _  +  (y - 7)² _  = 1 _______  +  (y - 7)² _______  = 1 For the following exercises, find the foci for the given ellipses. _  +  (y + 1)² _  = 1 _  +  (y - 2)² _  = 1 30. x 2 + 4y 2 + 4x + 8y = 1 Graphical For the following exercises, graph the given ellipses, noting center, vertices, and foci.

_ 25  +  y 2

_

_ 16  +  y 2/9  = 1 _  +  (y - 4)² _  = 1 _  +  (y - 3)² _  = 1/2  +  (y + 1)² _  = 1 For the following exercises, use the given information about the graph of each ellipse to determine its equation. 46. Center at the origin, symmetric with respect to the x- and y-axes, focus at (4, 0), and point on graph (0, 3). 47. Center at the origin, symmetric with respect to the x- and y-axes, focus at (0, -2), and point on graph

48. Center at the origin, symmetric with respect to the x- and y-axes, focus at (3, 0), and major axis is twice as long as minor axis. 49. Center (4, 2); vertex (9, 2); one focus: (4 + 2 √50. Center (3, 5); vertex (3, 11); one focus: (3, 5 + 4√2 ) 51. Center (-3, 4); vertex (1, 4); one focus: (-3 + 2√For the following exercises, given the graph of the ellipse, determine its equation. y x y x x y y x Extensions For the following exercises, find the area of the ellipse. The area of an ellipse is given by the formula Area = a ⋅ b ⋅ π . _  +  (y - 3)² _  = 1 _  +  (y - 6)² _  = 1 _  +  (y - 2)² _  = 1 Real-World Applications 62. Find the equation of the ellipse that will just fit inside a box that is 8 units wide and 4 units high. 63. Find the equation of the ellipse that will just fit inside a box that is four times as wide as it is high. Express in terms of h, the height. 64. An arch has the shape of a semi-ellipse (the top half of an ellipse). The arch has a height of 8 feet and a span of 20 feet. Find an equation for the ellipse, and use that to find the height to the nearest 0.01 foot of the arch at a distance of 4 feet from the center. 65. An arch has the shape of a semi-ellipse. The arch has a height of 12 feet and a span of 40 feet. Find an equation for the ellipse, and use that to find the distance from the center to a point at which the height is 6 feet. Round to the nearest hundredth. 66. A bridge is to be built in the shape of a semi- elliptical arch and is to have a span of 120 feet. The height of the arch at a distance of 40 feet from the center is to be 8 feet. Find the height of the arch at its center. 67. A person in a whispering gallery standing at one focus of the ellipse can whisper and be heard by a person standing at the other focus because all the sound waves that reach the ceiling are reflected to the other person. If a whispering gallery has a length of 120 feet, and the foci are located 30 feet from the center, find the height of the ceiling at the center. 68. A person is standing 8 feet from the nearest wall in a whispering gallery. If that person is at one focus, and the other focus is 80 feet away, what is the length and height at the center of the gallery? y x

## 10.2 The Hyperbola

---
Learning Objectives
In this section, you will:
• Locate a hyperbola’s vertices and foci.
• Write equations of hyperbolas in standard form.
• Graph hyperbolas centered at the origin.
• Graph hyperbolas not centered at the origin.
• Solve applied problems involving hyperbolas.
10. 2 The Hyperbola What do paths of comets, supersonic booms, ancient Grecian pillars, and natural draft cooling towers have in common? They can all be modeled by the same type of conic. For instance, when something moves faster than the speed of sound, a shock wave in the form of a cone is created. A portion of a conic is formed when the wave intersects the ground, resulting in a sonic boom. See Figure 1. Wake created from shock wave Portion of a hyperbola A shock wave intersecting the ground forms a portion of a conic and results in a sonic boom. Most people are familiar with the sonic boom created by supersonic aircraft, but humans were breaking the sound barrier long before the first supersonic flight. The crack of a whip occurs because the tip is exceeding the speed of sound. The bullets shot from many firearms also break the sound barrier, although the bang of the gun usually supersedes the sound of the sonic boom. Locating the Vertices and Foci of a Hyperbola In analytic geometry, a hyperbola is a conic section formed by intersecting a right circular cone with a plane at an angle such that both halves of the cone are intersected. This intersection produces two separate unbounded curves that are mirror images of each other. See Figure 2. Like the ellipse, the hyperbola can also be defined as a set of points in the coordinate plane. A hyperbola is the set of all points (x, y) in a plane such that the difference of the distances between (x, y) and the foci is a positive constant.

Notice that the definition of a hyperbola is very similar to that of an ellipse. The distinction is that the hyperbola is defined in terms of the difference of two distances, whereas the ellipse is defined in terms of the sum of two distances. As with the ellipse, every hyperbola has two axes of symmetry. The transverse axis is a line segment that passes through the center of the hyperbola and has vertices as its endpoints. The foci lie on the line that contains the transverse axis. The conjugate axis is perpendicular to the transverse axis and has the co-vertices as its endpoints. The center of a hyperbola is the midpoint of both the transverse and conjugate axes, where they intersect. Every hyperbola also has two asymptotes that pass through its center. As a hyperbola recedes from the center, its branches approach these asymptotes. The central rectangle of the hyperbola is centered at the origin with sides that pass through each vertex and co-vertex; it is a useful tool for graphing the hyperbola and its asymptotes. To sketch the asymptotes of the hyperbola, simply sketch and extend the diagonals of the central rectangle. See Figure 3. Conjugate axis Transverse axis Co-vertex y x Co-vertex Vertex Vertex Focus Focus Center Asymptote Asymptote Key features of the hyperbola In this section, we will limit our discussion to hyperbolas that are positioned vertically or horizontally in the coordinate plane; the axes will either lie on or be parallel to the x- and y-axes. We will consider two cases: those that are centered at the origin, and those that are centered at a point other than the origin. Deriving the Equation of an Ellipse Centered at the Origin Let (-c, 0) and (c, 0) be the foci of a hyperbola centered at the origin. The hyperbola is the set of all points (x, y) such that the difference of the distances from (x, y) to the foci is constant. See Figure 4. (–c, 0) (–a, 0) (a, 0) (c, 0) (x, y) y d² d¹ x If (a, 0) is a vertex of the hyperbola, the distance from (-c, 0) to (a, 0) is a - (-c) = a + c. The distance from (c, 0) to (a, 0) is c - a. The sum of the distances from the foci to the vertex is

(a + c) - (c - a) = 2a

If (x, y) is a point on the hyperbola, we can define the following variables: d² = the distance from (-c, 0) to (x, y)

d¹ = the distance from (c, 0) to (x, y) By definition of a hyperbola, d² - d¹ is constant for any point (x, y) on the hyperbola. We know that the difference of these distances is 2a for the vertex (a, 0). It follows that d² - d¹ = 2a for any point on the hyperbola. As with the derivation of the equation of an ellipse, we will begin by applying the distance formula. The rest of the derivation is algebraic. Compare this derivation with the one from the previous section for ellipses.

d² - d¹ = √—

(x - ( - c))² + (y - 0)²  - √(x - c)² + (y - 0)²  = 2a Distance formula √(x + c)² + y 2  - √(x - c)² + y 2  = 2a Simplify expressions.

√(x + c)² + y 2  = 2a + √(x - c)² + y 2  Move radical to opposite side.

(x + c)² + y 2 = (2a + √(x - c)² + y 2  ) Square both sides.

x 2 + 2cx + c² + y 2 = 4a² + 4a √(x - c)² + y 2  + (x - c)² + y 2 Expand the squares.

x 2 + 2cx + c² + y 2 = 4a² + 4a √(x - c)² + y 2  + x 2 - 2cx + c² + y 2 Expand remaining square.

2cx = 4a² + 4a √(x - c)² + y 2  - 2cx Combine like terms.

4cx - 4a² = 4a √(x - c)² + y 2  Isolate the radical.

cx - a² = a √(x - c)² + y 2  Divide by 4.

(cx - a²)² = a² ( √(x - c)² + y 2  )  Square both sides.

c² x 2 - 2a² cx + a⁴ = a²(x 2 - 2cx + c² + y 2) Expand the squares.

c² x 2 - 2a² cx + a⁴ = a² x 2 - 2a² cx + a² c² + a² y 2 Distribute a².

a⁴ + c² x 2 = a² x 2 + a² c² + a² y 2 Combine like terms.

c² x 2 - a² x 2 - a² y 2 = a² c² - a⁴ Rearrange terms.

x 2 (c² - a²) - a² y 2 = a² (c² - a²) Factor common terms

x 2 b² - a² y 2 = a² b² Set b² = c² - a².

 x 2b² ____ a²b²  -  a²y 2 ____ a²b²  =  a²b² ____ a²b²  Divide both sides by a²b².

 x 2/a²  -  y 2/b²  = 1 This equation defines a hyperbola centered at the origin with vertices (± a, 0) and co-vertices (0 ±  b). standard forms of the equation of a hyperbola with center (0, 0) The standard form of the equation of a hyperbola with center (0, 0) and major axis on the x-axis is  x 2/a²  -  y 2/b²  = 1 where • the length of the transverse axis is 2a • the coordinates of the vertices are (± a, 0) • the length of the conjugate axis is 2b • the coordinates of the co-vertices are (0, ± b) • the distance between the foci is 2c, where c² = a² + b² • the coordinates of the foci are (± c, 0) • the equations of the asymptotes are y = ±   (b)/(a)  x

See Figure 5a. The standard form of the equation of a hyperbola with center (0, 0) and transverse axis on the y-axis is  y 2/a²  -  x 2/b²  = 1 where • the length of the transverse axis is 2a • the coordinates of the vertices are (0, ±  a) • the length of the conjugate axis is 2b • the coordinates of the co-vertices are (± b, 0) • the distance between the foci is 2c, where c² = a² + b² • the coordinates of the foci are (0, ±  c) • the equations of the asymptotes are y = ±  (a)/(b) x See Figure 5b. Note that the vertices, co-vertices, and foci are related by the equation c² = a² + b². When we are given the equation of a hyperbola, we can use this relationship to identify its vertices and foci. (-c, 0) (a, 0) (-a, 0) (0, b) (0, -b) (0, -c) (0, a) (0, -a) (0, c ) (b, 0) (-b, 0) y x y (c, 0) y = a b x y = - a b x y = b a x y = - b a x x (a) (b) (a) Horizontal hyperbola with center (0, 0) (b) Vertical hyperbola with center (0, 0)

---
### 💡 **How To…**
Given the equation of a hyperbola in standard form, locate its vertices and foci. 1. Determine whether the transverse axis lies on the x- or y-axis. Notice that a² is always under the variable with the positive coefficient. So, if you set the other variable equal to zero, you can easily find the intercepts. In the case where the hyperbola is centered at the origin, the intercepts coincide with the vertices.

a. If the equation has the form  x 2/a²  -  y 2/b²  = 1, then the transverse axis lies on the x-axis. The vertices are located at ( ±  a, 0), and the foci are located at (±  c, 0).

b. If the equation has the form  y 2/a²  -  x 2/b²  = 1, then the transverse axis lies on the y-axis. The vertices are located at (0, ±  a), and the foci are located at (0, ±  c). 2. Solve for a using the equation a = √a² . 3. Solve for c using the equation c = √a² + b². 

---
### 📐 **Example  1**
Locating a Hyperbola’s Vertices and Foci Identify the vertices and foci of the hyperbola with equation  y 2/49  -  x 2/Solution The equation has the form  y 2/a²  -  x 2/b²  = 1, so the transverse axis lies on the y-axis. The hyperbola is centered at the origin, so the vertices serve as the y-intercepts of the graph. To find the vertices, set x = 0, and solve for y.

1 =  y 2/49  -  x 2/32 

1 =  y 2

_

_ 32 

1 =  y 2/49 

y = ±  √49  = ±  7 The foci are located at (0, ±  c). Solving for c,

c = √a² + b²  = √49 + 32  = √Therefore, the vertices are located at (0, ±  7), and the foci are located at (0, 9).

---
### ✏️ **Try It #1**
Identify the vertices and foci of the hyperbola with equation  x 2/9  -  y 2/Writing Equations of Hyperbolas in Standard Form Just as with ellipses, writing the equation for a hyperbola in standard form allows us to calculate the key features: its center, vertices, co-vertices, foci, asymptotes, and the lengths and positions of the transverse and conjugate axes. Conversely, an equation for a hyperbola can be found given its key features. We begin by finding standard equations for hyperbolas centered at the origin. Then we will turn our attention to finding standard equations for hyperbolas centered at some point other than the origin. Hyperbolas Centered at the Origin Reviewing the standard forms given for hyperbolas centered at (0, 0), we see that the vertices, co-vertices, and foci are related by the equation c² = a² + b². Note that this equation can also be rewritten as b² = c² - a². This relationship is used to write the equation for a hyperbola when given the coordinates of its foci and vertices.

---
### 💡 **How To…**
Given the vertices and foci of a hyperbola centered at (0, 0), write its equation in standard form. 1. Determine whether the transverse axis lies on the x- or y-axis. a. If the given coordinates of the vertices and foci have the form (±  a, 0) and (±  c, 0), respectively, then the transverse axis is the x-axis. Use the standard form  x 2/a²  -  y 2/b²  = 1. b. If the given coordinates of the vertices and foci have the form (0, ±  a) and (0, ±  c), respectively, then the transverse axis is the y-axis. Use the standard form  y 2/a²  -  x 2/b²  = 1. 2. Find b² using the equation b² = c² - a². 3. Substitute the values for a² and b² into the standard form of the equation determined in Step 1.

---
### 📐 **Example  2**
Finding the Equation of a Hyperbola Centered at (0, 0) Given its Foci and Vertices What is the standard form equation of the hyperbola that has vertices (± 6, 0) and foci (± 2√Solution The vertices and foci are on the x-axis. Thus, the equation for the hyperbola will have the form  x 2/a²  -  y 2/b²  = 1. The vertices are (± 6, 0), so a = 6 and a² = 36. The foci are (± 2√10 , 0), so c = 2√Solving for b², we have

b² = c² - a²

Substitute for c² and a².

b² = 4 Subtract. Finally, we substitute a² = 36 and b² = 4 into the standard form of the equation,  x 2/a²  -  y 2/b²  = 1. The equation of the hyperbola is  x 2/36  -  y 2/4  = 1, as shown in Figure 6.

---
### ✏️ **Try It #2**
What is the standard form equation of the hyperbola that has vertices (0, ±  2) and foci (0, ±  2√5  )? Hyperbolas Not Centered at the Origin Like the graphs for other equations, the graph of a hyperbola can be translated. If a hyperbola is translated h units horizontally and k units vertically, the center of the hyperbola will be (h, k). This translation results in the standard form of the equation we saw previously, with x replaced by (x - h) and y replaced by (y - k). standard forms of the equation of a hyperbola with center (h, k) The standard form of the equation of a hyperbola with center (h, k) and transverse axis parallel to the x-axis is  (x - h)² _ a²  -  (y - k)² _ b²  = 1 where • the length of the transverse axis is 2a • the coordinates of the vertices are (h ±  a, k) • the length of the conjugate axis is 2b • the coordinates of the co-vertices are (h, k ±  b) • the distance between the foci is 2c, where c 2 = a 2 + b 2 • the coordinates of the foci are (h ±  c, k) y x

The asymptotes of the hyperbola coincide with the diagonals of the central rectangle. The length of the rectangle is 2a and its width is 2b. The slopes of the diagonals are ±   (b)/(a) , and each diagonal passes through the center (h, k). Using the point-slope formula, it is simple to show that the equations of the asymptotes are y = ±   (b)/(a) (x - h) + k. See Figure 7a. The standard form of the equation of a hyperbola with center (h, k) and transverse axis parallel to the y-axis is  (y - k)² _ a²  -  (x - h)² _ b²  = 1 where • the length of the transverse axis is 2a • the coordinates of the vertices are (h, k ±  a) • the length of the conjugate axis is 2b • the coordinates of the co-vertices are (h ±  b, k) • the distance between the foci is 2c, where c 2 = a 2 + b 2 • the coordinates of the foci are (h, k ±  c) Using the reasoning above, the equations of the asymptotes are y = ±  (a)/(b) (x - h) + k. See Figure 7b. y = a (x - h) + k b y = - a (x - h) + k b y = - b (x - h) + k a y = b (x - h) + k a (h, k - b) (h, k + b) (h, k - c) (h, k + c) (h - b, k) (h + b, k) (h - a, k) (h + a, k) (h, k - a) (h, k + a) (h - c, k) (h + c, k) (h, k) (h, k) y y x x (a) (b) Like hyperbolas centered at the origin, hyperbolas centered at a point (h, k) have vertices, co-vertices, and foci that are related by the equation c² = a² + b². We can use this relationship along with the midpoint and distance formulas to find the standard equation of a hyperbola when the vertices and foci are given.

---
### 💡 **How To…**
Given the vertices and foci of a hyperbola centered at (h, k), write its equation in standard form. 1. Determine whether the transverse axis is parallel to the x- or y-axis. a. If the y-coordinates of the given vertices and foci are the same, then the transverse axis is parallel to the x-axis. Use the standard form  (x - h)² _ a²  -  (y - k)² _ b²  = 1. b. If the x-coordinates of the given vertices and foci are the same, then the transverse axis is parallel to the y-axis. Use the standard form  (y - k)² _ a²  -  (x - h)² _ b²  = 1. 2. Identify the center of the hyperbola, (h, k), using the midpoint formula and the given coordinates for the vertices.

3. Find a² by solving for the length of the transverse axis, 2a, which is the distance between the given vertices. 4. Find c² using h and k found in Step 2 along with the given coordinates for the foci. 5. Solve for b² using the equation b² = c² - a². 6. Substitute the values for h, k, a², and b² into the standard form of the equation determined in Step 1.

---
### 📐 **Example  3**
Finding the Equation of a Hyperbola Centered at (h, k) Given its Foci and Vertices What is the standard form equation of the hyperbola that has vertices at (0, -2) and (6, -2) and foci at (-2, -2) and

**Solution**

The y-coordinates of the vertices and foci are the same, so the transverse axis is parallel to the x-axis. Thus, the equation of the hyperbola will have the form

 (x - h)² _ a²  -  (y - k)² _ b²  = 1 First, we identify the center, (h, k). The center is halfway between the vertices (0, -2) and (6, -2). Applying the midpoint formula, we have

(h, k) = (  0 + 6 _____ ,  -2 + (-2) _________  )  = (3, -2) Next, we find a². The length of the transverse axis, 2a, is bounded by the vertices. So, we can find a² by finding the distance between the x-coordinates of the vertices.

2a = | 0 - 6 |

2a = 6

a = 3

a² = 9 Now we need to find c². The coordinates of the foci are (h ±  c, k). So (h - c, k) = (-2, -2) and (h + c, k) = (8, -2). We can use the x-coordinate from either of these points to solve for c. Using the point (8, -2), and substituting h = 3,

h + c = 8

3 + c = 8

c = 5

Next, solve for b² using the equation b² = c² - a² :

b² = c² - a²

= 16 Finally, substitute the values found for h, k, a², and b² into the standard form of the equation.

 (x - 3)² _  -  (y + 2)² _  = 1

---
### ✏️ **Try It #3**
What is the standard form equation of the hyperbola that has vertices (1, -2) and (1, 8) and foci (1, -10) and (1, 16)? Graphing Hyperbolas Centered at the Origin When we have an equation in standard form for a hyperbola centered at the origin, we can interpret its parts to identify the key features of its graph: the center, vertices, co-vertices, asymptotes, foci, and lengths and positions of the transverse and conjugate axes. To graph hyperbolas centered at the origin, we use the standard form  x 2/a²  -  y 2/b²  = 1 for horizontal hyperbolas and the standard form  y 2/a²  -  x 2/b²  = 1 for vertical hyperbolas.

---
### 💡 **How To…**
Given a standard form equation for a hyperbola centered at (0, 0), sketch the graph. 1. Determine which of the standard forms applies to the given equation. 2. Use the standard form identified in Step 1 to determine the position of the transverse axis; coordinates for the vertices, co-vertices, and foci; and the equations for the asymptotes. a. If the equation is in the form  x 2/a²  -  y 2/b²  = 1, then • the transverse axis is on the x-axis • the coordinates of the vertices are (± a, 0) • the coordinates of the co-vertices are (0, ±  b) • the coordinates of the foci are (± c, 0) • the equations of the asymptotes are y = ±   (b)/(a) x b. If the equation is in the form  y 2/a²  -  x 2/b²  = 1, then • the transverse axis is on the y-axis • the coordinates of the vertices are (0, ±  a) • the coordinates of the co-vertices are (± b, 0) • the coordinates of the foci are (0, ±  c) • the equations of the asymptotes are y = ±  (a)/(b) x 3. Solve for the coordinates of the foci using the equation c = ±  √a² + b² . 4. Plot the vertices, co-vertices, foci, and asymptotes in the coordinate plane, and draw a smooth curve to form the hyperbola.

---
### 📐 **Example  4**: Graphing a Hyperbola Centered at (0, 0) Given an Equation in Standard Form

Graph the hyperbola given by the equation  y 2/64  -  x 2/36  = 1. Identify and label the vertices, co-vertices, foci, and asymptotes.

**Solution**

The standard form that applies to the given equation is  y 2/a²  -  x 2/b²  = 1. Thus, the transverse axis is on the y-axis The coordinates of the vertices are (0, ±  a) = (0, ±  √64 ) = (0, ±  8) The coordinates of the co-vertices are (± b, 0) = (±  √The coordinates of the foci are (0, ±  c), where c = ±  √a² + b² . Solving for c, we have c = ±  √a² + b²  = ±  √64 + 36  = ±  √Therefore, the coordinates of the foci are (0, ±  10) The equations of the asymptotes are y = ±  (a)/(b) x = ±  8/6 x = ±  4/3 x Plot and label the vertices and co-vertices, and then sketch the central rectangle. Sides of the rectangle are parallel to the axes and pass through the vertices and co-vertices. Sketch and extend the diagonals of the central rectangle to show the asymptotes. The central rectangle and asymptotes provide the framework needed to sketch an accurate graph of the hyperbola. Label the foci and asymptotes, and draw a smooth curve to form the hyperbola, as shown in Figure 8.

y = 4 x y = - 4 x y y x x

---
### ✏️ **Try It #4**
Graph the hyperbola given by the equation  x 2/144  -  y 2/81  = 1. Identify and label the vertices, co-vertices, foci, and asymptotes. Graphing Hyperbolas Not Centered at the Origin Graphing hyperbolas centered at a point (h, k) other than the origin is similar to graphing ellipses centered at a point other than the origin. We use the standard forms  (x - h)² _ a²  -  (y - k)² _ b²  = 1 for horizontal hyperbolas, and  (y - k)² _ a²  -  (x - h)² _ b²  = 1 for vertical hyperbolas. From these standard form equations we can easily calculate and plot key features of the graph: the coordinates of its center, vertices, co-vertices, and foci; the equations of its asymptotes; and the positions of the transverse and conjugate axes.

---
### 💡 **How To…**
Given a general form for a hyperbola centered at (h, k), sketch the graph. 1. Determine which of the standard forms applies to the given equation. Convert the general form to that standard form. 2. Use the standard form identified in Step 1 to determine the position of the transverse axis; coordinates for the center, vertices, co-vertices, foci; and equations for the asymptotes. a. If the equation is in the form  (x - h)² _ a²  -  (y - k)² _ b²  = 1, then • the transverse axis is parallel to the x-axis • the center is (h, k) • the coordinates of the vertices are (h ±  a, k) • the coordinates of the co-vertices are (h, k ±  b) • the coordinates of the foci are (h ±  c, k) • the equations of the asymptotes are y = ±   (b)/(a) (x - h) + k

b. If the equation is in the form  (y - k)² _______ a²  -  (x - h)² _______ b²  = 1, then • the transverse axis is parallel to the y-axis • the center is (h, k) • the coordinates of the vertices are (h, k ±  a) • the coordinates of the co-vertices are (h ±  b, k) • the coordinates of the foci are (h, k ±  c) • the equations of the asymptotes are y = ±  (a)/(b) (x - h) + k 3. Solve for the coordinates of the foci using the equation c = ±  √a² + b² . 4. Plot the center, vertices, co-vertices, foci, and asymptotes in the coordinate plane and draw a smooth curve to form the hyperbola.

---
### 📐 **Example  5**: Graphing a Hyperbola Centered at (h, k) Given an Equation in General Form

Graph the hyperbola given by the equation 9x 2 - 4y 2 - 36x - 40y - 388 = 0. Identify and label the center, vertices, co-vertices, foci, and asymptotes.

**Solution**

Start by expressing the equation in standard form. Group terms that contain the same variable, and move the constant to the opposite side of the equation.

(9x 2 - 36x) - (4y 2 + 40y) = 388 Factor the leading coefficient of each expression.

9(x 2 - 4x) - 4(y 2 + 10y) = 388 Complete the square twice. Remember to balance the equation by adding the same constants to each side.

Rewrite as perfect squares.

9(x - 2)² - 4(y + 5)² = 324 Divide both sides by the constant term to place the equation in standard form.

 (x - 2)² _  -  (y + 5)² _  = 1 The standard form that applies to the given equation is  (x - h)² _ a²  -  (y - k)² _ b²  = 1, where a² = 36 and b² = 81, or a = 6 and b = 9. Thus, the transverse axis is parallel to the x-axis. It follows that: • the center of the ellipse is (h, k) = (2, -5) • the coordinates of the vertices are (h ±  a, k) = (2 ±  6, -5), or (-4, -5) and (8, -5) • the coordinates of the co-vertices are (h, k ±  b) = (2, - 5 ±  9), or (2, - 14) and (2, 4) • the coordinates of the foci are (h ±  c, k), where c = ±  √a² + b 2 . Solving for c, we have c = ±  √36 + 81  = ±  √117  = ±  3√13  Therefore, the coordinates of the foci are (2 - 3√13 , -5) and (2 + 3√The equations of the asymptotes are y = ±   (b)/(a) (x - h) + k = ±   3/2 (x - 2) - 5. Next, we plot and label the center, vertices, co-vertices, foci, and asymptotes and draw smooth curves to form the hyperbola, as shown in Figure 9.

---
### ✏️ **Try It #5**
Graph the hyperbola given by the standard form of an equation  (y + 4)² _  -  (x - 3)² _  = 1. Identify and label the center, vertices, co-vertices, foci, and asymptotes. Solving Applied Problems Involving Hyperbolas As we discussed at the beginning of this section, hyperbolas have real-world applications in many fields, such as astronomy, physics, engineering, and architecture. The design efficiency of hyperbolic cooling towers is particularly interesting. Cooling towers are used to transfer waste heat to the atmosphere and are often touted for their ability to generate power efficiently. Because of their hyperbolic form, these structures are able to withstand extreme winds while requiring less material than any other forms of their size and strength. See Figure 10. For example, a 500-foot tower can be made of a reinforced concrete shell only 6 or 8 inches wide! The first hyperbolic towers were designed in 1914 and were 35 meters high. Today, the tallest cooling towers are in France, standing a remarkable 170 meters tall. In Example 6 we will use the design layout of a cooling tower to find a hyperbolic equation that models its sides. y x

---
### 📐 **Example  6**: Solving Applied Problems Involving Hyperbolas

The design layout of a cooling tower is shown in Figure 11. The tower stands 179.6 meters tall. The diameter of the top is 72 meters. At their closest, the sides of the tower are 60 meters apart. Find the equation of the hyperbola that models the sides of the cooling tower. Assume that the center of the hyperbola— indicated by the intersection of dashed perpendicular lines in the figure—is the origin of the coordinate plane. Round final values to four decimal places.

**Solution**

We are assuming the center of the tower is at the origin, so we can use the standard form of a horizontal hyperbola centered at the origin:  x 2/a²  -  y 2/b²  = 1, where the branches of the hyperbola form the sides of the cooling tower. We must find the values of a² and b² to complete the model. First, we find a². Recall that the length of the transverse axis of a hyperbola is 2a. This length is represented by the distance where the sides are closest, which is given as 65.3 meters. So, 2a = 60. Therefore, a = 30 and a² = 900. To solve for b², we need to substitute for x and y in our equation using a known point. To do this, we can use the dimensions of the tower to find some point (x, y) that lies on the hyperbola. We will use the top right corner of the tower to represent that point. Since the y-axis bisects the tower, our x-value can be represented by the radius of the top, or 36 meters. The y-value is represented by the distance from the origin to the top, which is given as 79.6 meters. Therefore,

 x 2/a²  -  y 2/b²  = 1 Standard form of horizontal hyperbola.

b² =  y 2/x 2/a²  - 1  Isolate b²

_ ____  Substitute for a², x, and y

Round to four decimal places The sides of the tower can be modeled by the hyperbolic equation

 x 2/900  -  y 2 _ _ 302  -  y 2/72 m 60 m

---
### ✏️ **Try It #6**
A design for a cooling tower project is shown in Figure 12. Find the equation of the hyperbola that models the sides of the cooling tower. Assume that the center of the hyperbola—indicated by the intersection of dashed perpendicular lines in the figure—is the origin of the coordinate plane. Round final values to four decimal places. Access these online resources for additional instruction and practice with hyperbolas. • Conic Sections: The Hyperbola Part 1 of 2 (http://openstaxcollege.org/l/hyperbola¹) • Conic Sections: The Hyperbola Part 2 of 2 (http://openstaxcollege.org/l/hyperbola²) • Graph a Hyperbola with Center at Origin (http://openstaxcollege.org/l/hyperbolaorigin) • Graph a Hyperbola with Center not at Origin (http://openstaxcollege.org/l/hbnotorigin) 60 m 40 m

## 10.2 Section Exercises

---
### 10.2 Section Exercises

Verbal 1. Define a hyperbola in terms of its foci. 2. What can we conclude about a hyperbola if its asymptotes intersect at the origin? 3. What must be true of the foci of a hyperbola? 4. If the transverse axis of a hyperbola is vertical, what do we know about the graph? 5. Where must the center of hyperbola be relative to its foci? Algebraic For the following exercises, determine whether the following equations represent hyperbolas. If so, write in standard form.

___ 36  -  y 2/9  = 1 10. -9x 2 + 18x + y 2 + 4y - 14 = 0 For the following exercises, write the equation for the hyperbola in standard form if it is not already, and identify the vertices and foci, and write equations of asymptotes.

___ 25  -  y 2

___ ___ 100  -  y 2/9  = 1/4  -  x 2

___ _______  -  (y - 2)² _______  = 1 _______  -  (x + 1)² _______  = 1 _______  -  (y + 7)² _______  = 1 For the following exercises, find the equations of the asymptotes for each hyperbola.

__ 32  -  x 2

__ _______  -  (y + 4)² _______  = 1 _______  -  (x + 5)² _______  = 1 Graphical For the following exercises, sketch a graph of the hyperbola, labeling vertices and foci.

___ 49  -  y 2

___

___ 64  -  y 2/4  = 1/9  -  x 2

___ _______  -  (x - 4)² _______  = 1 _______  -  (y + 3)² _______  = 1 _______  -  (x - 3)² _______  = 1

40. -x 2 + 8x + 4y 2 - 40y + 88 = 0 For the following exercises, given information about the graph of the hyperbola, find its equation. 45. Vertices at (3, 0) and (-3, 0) and one focus at (5, 0). 46. Vertices at (0, 6) and (0, -6) and one focus at 47. Vertices at (1, 1) and (11, 1) and one focus at (12, 1). 48. Center: (0, 0); vertex: (0, -13); one focus: (0, √49. Center: (4, 2); vertex: (9, 2); one focus: (4 + √50. Center: (3, 5); vertex: (3, 11); one focus: (3, 5 + 2√For the following exercises, given the graph of the hyperbola, find its equation. x y Vertices Center Foci Foci y x Foci Vertices Foci y x Center Foci Foci Vertices Center y Vertices Foci Foci Center y x

Extensions For the following exercises, express the equation for the hyperbola as two functions, with y as a function of x. Express as simply as possible. Use a graphing calculator to sketch the graph of the two functions on the same axes.

_ 4  -  y 2/9  = 1/9  -  x 2/1  = 1 _  -  (y + 3)² _  = 1 59. -4x 2 - 16x + y 2 - 2y - 19 = 0 Real-World Applications For the following exercises, a hedge is to be constructed in the shape of a hyperbola near a fountain at the center of the yard. Find the equation of the hyperbola and sketch the graph. 61. The hedge will follow the asymptotes y = x and y = -x, and its closest distance to the center fountain is 5 yards. 62. The hedge will follow the asymptotes y = 2x and y = -2x, and its closest distance to the center fountain is 6 yards. 63. The hedge will follow the asymptotes y =  1/2 x and y = - 1/2 x, and its closest distance to the center fountain is 10 yards. 64. The hedge will follow the asymptotes y =  2/3 x and y = - 2/3 x, and its closest distance to the center fountain is 12 yards. 65. The hedge will follow the asymptotes y =  3/4 x and y = - 3/4 x, and its closest distance to the center fountain is 20 yards. For the following exercises, assume an object enters our solar system and we want to graph its path on a coordinate system with the sun at the origin and the x-axis as the axis of symmetry for the object's path. Give the equation of the flight path of each object using the given information. 66. The object enters along a path approximated by the line y = x - 2 and passes within 1 au (astronomical unit) of the sun at its closest approach, so that the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = -x + 2. 67. The object enters along a path approximated by the line y = 2x - 2 and passes within 0.5 au of the sun at its closest approach, so the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = -2x + 2. 68. The object enters along a path approximated by the line y = 0.5x + 2 and passes within 1 au of the sun at its closest approach, so the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = -0.5x - 2. 69. The object enters along a path approximated by the line y =  1/3 x - 1 and passes within 1 au of the sun at its closest approach, so the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = - 1/3 x + 1. 70. The object enters along a path approximated by the line y = 3x - 9 and passes within 1 au of the sun at its closest approach, so the sun is one focus of the hyperbola. It then departs the solar system along a path approximated by the line y = -3x + 9.

Learning Objectives
In this section, you will:
• Graph parabolas with vertices at the origin.
• Write equations of parabolas in standard form.
• Graph parabolas with vertices not at the origin.
• Solve applied problems involving parabolas.
10. 3 The Parabola Did you know that the Olympic torch is lit several months before the start of the games? The ceremonial method for lighting the flame is the same as in ancient times. The ceremony takes place at the Temple of Hera in Olympia, Greece, and is rooted in Greek mythology, paying tribute to Prometheus, who stole fire from Zeus to give to all humans. One of eleven acting priestesses places the torch at the focus of a parabolic mirror (see Figure 1), which focuses light rays from the sun to ignite the flame. Parabolic mirrors (or reflectors) are able to capture energy and focus it to a single point. The advantages of this property are evidenced by the vast list of parabolic objects we use every day: satellite dishes, suspension bridges, telescopes, microphones, spotlights, and car headlights, to name a few. Parabolic reflectors are also used in alternative energy devices, such as solar cookers and water heaters, because they are inexpensive to manufacture and need little maintenance. In this section we will explore the parabola and its uses, including low-cost, energy-efficient solar designs. Graphing Parabolas with Vertices at the Origin In The Ellipse, we saw that an ellipse is formed when a plane cuts through a right circular cone. If the plane is parallel to the edge of the cone, an unbounded curve is formed. This curve is a parabola. See Figure 2.

## 10.3 The Parabola

---
Like the ellipse and hyperbola, the parabola can also be defined by a set of points in the coordinate plane. A parabola is the set of all points (x, y) in a plane that are the same distance from a fixed line, called the directrix, and a fixed point (the focus) not on the directrix. In Quadratic Functions, we learned about a parabola’s vertex and axis of symmetry. Now we extend the discussion to include other key features of the parabola. See Figure 3. Notice that the axis of symmetry passes through the focus and vertex and is perpendicular to the directrix. The vertex is the midpoint between the directrix and the focus. The line segment that passes through the focus and is parallel to the directrix is called the latus rectum. The endpoints of the latus rectum lie on the curve. By definition, the distance d from the focus to any point P on the parabola is equal to the distance from P to the directrix. Latus rectum Axis of symmetry Focus Directrix x y Vertex To work with parabolas in the coordinate plane, we consider two cases: those with a vertex at the origin and those with a vertex at a point other than the origin. We begin with the former. Let (x, y) be a point on the parabola with vertex (0, 0), focus (0, p), and directrix y = -p as shown in Figure 4. The distance d from point (x, y) to point (x, -p) on the directrix is the difference of the y-values: d = y + p. The distance from the focus (0, p) to the point (x, y) is also equal to d and can be expressed using the distance formula.

d = √(x - 0)² + (y - p)² 

= √x 2 + (y - p)²  Set the two expressions for d equal to each other and solve for y to derive the equation of the parabola. We do this because the distance from (x, y) to (0, p) equals the distance from (x, y) to (x, -p).

√x 2 + (y - p)²  = y + p We then square both sides of the equation, expand the squared terms, and simplify by combining like terms.

x 2 + (y - p)² = (y + p)²

x 2 + y 2 - 2py + p² = y 2 + 2py + p²

x 2 - 2py = 2py

x 2 = 4py The equations of parabolas with vertex (0, 0) are y 2 = 4px when the x-axis is the axis of symmetry and x 2 = 4py when the y-axis is the axis of symmetry. These standard forms are given below, along with their general graphs and key features. (0, p) d d (x, y) (x, -p) y = -p x y

standard forms of parabolas with vertex (0, 0) Axis of Symmetry Equation Focus Directrix Endpoints of Latus Rectum x-axis y 2 = 4px (p, 0) x = -p (p, ±  2p) y-axis x 2 = 4py (0, p) y = -p (±  2p, p) the x-axis, the parabola opens left. (c) When p < 0 and the axis of symmetry is the y-axis, the parabola opens up. (d) When p < 0 and the axis of symmetry is the y-axis, the parabola opens down. (p, 0) (p, 0) (p, -|2p|) (p, -|2p|) (p, |2p|) (p, |2p|) y y x x (a) (c) (d) (b) x = -p x = -p y 2 = 4px y 2 = 4px p > 0 p < 0 (0, p) (0, p) (-|2p|, p) (-|2p|, p) (|2p|, p) (|2p|, p) y y x x y = -p y = -p x² = 4py p > 0 x² = 4py p < 0 The key features of a parabola are its vertex, axis of symmetry, focus, directrix, and latus rectum. See Figure 5. When given a standard equation for a parabola centered at the origin, we can easily identify the key features to graph the parabola. A line is said to be tangent to a curve if it intersects the curve at exactly one point. If we sketch lines tangent to the parabola at the endpoints of the latus rectum, these lines intersect on the axis of symmetry, as shown in Figure 6. x = -6 y 2 = 24x y x

---
### 💡 **How To…**
Given a standard form equation for a parabola centered at (0, 0), sketch the graph. 1. Determine which of the standard forms applies to the given equation: y 2 = 4px or x 2 = 4py. 2. Use the standard form identified in Step 1 to determine the axis of symmetry, focus, equation of the directrix, and endpoints of the latus rectum. a. If the equation is in the form y 2 = 4px, then • the axis of symmetry is the x-axis, y = 0 • set 4p equal to the coefficient of x in the given equation to solve for p. If p > 0, the parabola opens right. If p < 0, the parabola opens left. • use p to find the coordinates of the focus, (p, 0) • use p to find the equation of the directrix, x = - p • use p to find the endpoints of the latus rectum, (p, ±  2p). Alternately, substitute x = p into the original equation. b. If the equation is in the form x 2 = 4py, then • the axis of symmetry is the y-axis, x = 0 • set 4p equal to the coefficient of y in the given equation to solve for p. If p > 0, the parabola opens up. If p < 0, the parabola opens down. • use p to find the coordinates of the focus, (0, p) • use p to find equation of the directrix, y = - p • use p to find the endpoints of the latus rectum, (± 2p, p) 3. Plot the focus, directrix, and latus rectum, and draw a smooth curve to form the parabola.

---
### 📐 **Example  1**
Graphing a Parabola with Vertex (0, 0) and the x-axis as the Axis of Symmetry Graph y 2 = 24x. Identify and label the focus, directrix, and endpoints of the latus rectum.

**Solution**

The standard form that applies to the given equation is y 2 = 4px. Thus, the axis of symmetry is the x-axis. It follows that: • 24 = 4p, so p = 6. Since p > 0, the parabola opens right • the coordinates of the focus are (p, 0) = (6, 0) • the equation of the directrix is x = -p = - 6 • the endpoints of the latus rectum have the same x-coordinate at the focus. To find the endpoints, substitute x = 6 into the original equation: (6, ±  12) Next we plot the focus, directrix, and latus rectum, and draw a smooth curve to form the parabola. See Figure 7. y x x = -6

---
### ✏️ **Try It #1**
Graph y 2 = -16x. Identify and label the focus, directrix, and endpoints of the latus rectum.

---
### 📐 **Example  2**
Graphing a Parabola with Vertex (0, 0) and the y-axis as the Axis of Symmetry Graph x 2 = -6y. Identify and label the focus, directrix, and endpoints of the latus rectum.

**Solution**

The standard form that applies to the given equation is x 2 = 4py. Thus, the axis of symmetry is the y-axis. It follows that: • -6 = 4p, so p = - 3/2  Since p < 0, the parabola opens down. • the coordinates of the focus are (0, p) = ( 0, -  3/2  )  • the equation of the directrix is y = - p =  3/2  • the endpoints of the latus rectum can be found by substituting y =  3/2  into the original equation, ( ± 3, -  3/2  )  Next we plot the focus, directrix, and latus rectum, and draw a smooth curve to form the parabola.

---
### ✏️ **Try It #2**
Graph x 2 = 8y. Identify and label the focus, directrix, and endpoints of the latus rectum. Writing Equations of Parabolas in Standard Form In the previous examples, we used the standard form equation of a parabola to calculate the locations of its key features. We can also use the calculations in reverse to write an equation for a parabola when given its key features.

---
### 💡 **How To…**
Given its focus and directrix, write the equation for a parabola in standard form. 1. Determine whether the axis of symmetry is the x- or y-axis. a. If the given coordinates of the focus have the form (p, 0), then the axis of symmetry is the x-axis.

Use the standard form y 2 = 4px. b. If the given coordinates of the focus have the form (0, p), then the axis of symmetry is the y-axis.

Use the standard form x 2 = 4py. 2. Multiply 4p. 3. Substitute the value from Step 2 into the equation determined in Step 1.

---
### 📐 **Example  3**
Writing the Equation of a Parabola in Standard Form Given its Focus and Directrix What is the equation for the parabola with focus ( - 1/2 , 0 )  and directrix x =  1/2 ?

**Solution**

The focus has the form (p, 0), so the equation will have the form y 2 = 4px. • Multiplying 4p, we have 4p = 4(-  1/2 ) = -2. • Substituting for 4p, we have y 2 = 4px = -2x. Therefore, the equation for the parabola is y 2 = -2x. x² = -6y y x y = 3 0, -3 3, -3

---
### ✏️ **Try It #3**
What is the equation for the parabola with focus ( 0,  7/2  )  and directrix y = - 7/2 ? Graphing Parabolas with Vertices Not at the Origin Like other graphs we’ve worked with, the graph of a parabola can be translated. If a parabola is translated h units horizontally and k units vertically, the vertex will be (h, k). This translation results in the standard form of the equation we saw previously with x replaced by (x - h) and y replaced by (y - k). To graph parabolas with a vertex (h, k) other than the origin, we use the standard form (y - k)² = 4p(x - h) for parabolas that have an axis of symmetry parallel to the x-axis, and (x - h)² = 4p(y - k) for parabolas that have an axis of symmetry parallel to the y-axis. These standard forms are given below, along with their general graphs and key features. standard forms of parabolas with vertex (h, k) Axis of Symmetry Equation Focus Directrix Endpoints of Latus Rectum y = k (y - k)² = 4p(x - h) (h + p, k) x = h -p (h + p, k ±  2p) x = h (x - h)² = 4p(y - k) (h, k + p) y = k -p (h ±  2p, k + p) (c) When p > 0, the parabola opens up. (d) When p < 0, the parabola opens down. (y - k)² = 4p(x - h) (x - h)² = 4p(y - h) (x - h)² = 4p(y - k) (h + p, k + 2p) y = k y = k x y (a) (b) (c) (d) y y y x x (h, k) (h, k) (h, k) x = h - p y = k - p y = k - p x = h - p (h + p, k) (h, k + p) (h, k + p) (h + p, k - 2p) (h + 2p, k + p) p > 0 p > 0 x (y - k)² = 4p(x - h) (h + p, k + |2p|) (h, k) (h + p, k) (h + p, k - |2p|) (h - 2p, k + p) (h - |2p|, k + p) (h + |2p|, k + p) p < 0 x = h x = h p < 0

---
### 💡 **How To…**
Given a standard form equation for a parabola centered at (h, k), sketch the graph. 1. Determine which of the standard forms applies to the given equation: (y - k)² = 4p(x - h) or (x - h)² = 4p(y - k). 2. Use the standard form identified in Step 1 to determine the vertex, axis of symmetry, focus, equation of the directrix, and endpoints of the latus rectum. a. If the equation is in the form (y - k)² = 4p(x - h), then: • use the given equation to identify h and k for the vertex, (h, k) • use the value of k to determine the axis of symmetry, y = k • set 4p equal to the coefficient of (x - h) in the given equation to solve for p. If p > 0, the parabola opens right. If p < 0, the parabola opens left. • use h, k, and p to find the coordinates of the focus, (h + p, k) • use h and p to find the equation of the directrix, x = h - p • use h, k, and p to find the endpoints of the latus rectum, (h + p, k ±  2p) b. If the equation is in the form (x - h)² = 4p(y - k), then: • use the given equation to identify h and k for the vertex, (h, k) • use the value of h to determine the axis of symmetry, x = h • set 4p equal to the coefficient of (y - k) in the given equation to solve for p. If p > 0, the parabola opens up. If p < 0, the parabola opens down. • use h, k, and p to find the coordinates of the focus, (h, k + p) • use k and p to find the equation of the directrix, y = k - p • use h, k, and p to find the endpoints of the latus rectum, (h ±  2p, k + p) 3. Plot the vertex, axis of symmetry, focus, directrix, and latus rectum, and draw a smooth curve to form the parabola.

---
### 📐 **Example  4**
Graphing a Parabola with Vertex ( h, k) and Axis of Symmetry Parallel to the x-axis Graph (y - 1)² = -16(x + 3). Identify and label the vertex, axis of symmetry, focus, directrix, and endpoints of the latus rectum.

**Solution**

The standard form that applies to the given equation is (y - k)² = 4p(x - h). Thus, the axis of symmetry is parallel to the x-axis. It follows that: • the vertex is (h, k) = (-3, 1) • the axis of symmetry is y = k = 1 • -16 = 4p, so p = -4. Since p < 0, the parabola opens left. • the coordinates of the focus are (h + p, k) = (-3 + (-4), 1) = (-7, 1) • the equation of the directrix is x = h - p = -3 - (-4) = 1 • the endpoints of the latus rectum are (h + p, k ±  2p) = (-3 + (-4), 1 ±  2(-4)), or (-7, -7) and (-7, 9) Next we plot the vertex, axis of symmetry, focus, directrix, and latus rectum, and draw a smooth curve to form the parabola. See Figure 10. (y - 1)² = -16(x + 3) (-7 , -7 ) y = 1 x = 1 x y

---
### ✏️ **Try It #4**
Graph (y + 1)² = 4(x - 8). Identify and label the vertex, axis of symmetry, focus, directrix, and endpoints of the latus rectum.

---
### 📐 **Example  5**: Graphing a Parabola from an Equation Given in General Form

Graph x 2 - 8x - 28y - 208 = 0. Identify and label the vertex, axis of symmetry, focus, directrix, and endpoints of the latus rectum.

**Solution**

Start by writing the equation of the parabola in standard form. The standard form that applies to the given equation is (x - h)² = 4p (y - k). Thus, the axis of symmetry is parallel to the y-axis. To express the equation of the parabola in this form, we begin by isolating the terms that contain the variable x in order to complete the square.

x 2 - 8x - 28y - 208 = 0

x 2 - 8x = 28y + 208

(x - 4)² = 28y + 224

(x - 4)² = 28(y + 8)

(x - 4)² = 4 ⋅ 7 ⋅ (y + 8) It follows that: • the vertex is (h, k) = (4, -8) • the axis of symmetry is x = h = 4 • since p = 7, p > 0 and so the parabola opens up • the coordinates of the focus are (h, k + p) = (4, -8 + 7) = (4, -1) • the equation of the directrix is y = k - p = -8 - 7 = -15 • the endpoints of the latus rectum are (h ±  2p, k + p) = (4 ±  2(7), -8 + 7), or (-10, -1) and (18, -1) Next we plot the vertex, axis of symmetry, focus, directrix, and latus rectum, and draw a smooth curve to form the parabola. See Figure 11.

---
### ✏️ **Try It #5**
Graph (x + 2)² = -20 (y - 3). Identify and label the vertex, axis of symmetry, focus, directrix, and endpoints of the latus rectum. Solving Applied Problems Involving Parabolas As we mentioned at the beginning of the section, parabolas are used to design many objects we use every day, such as telescopes, suspension bridges, microphones, and radar equipment. Parabolic mirrors, such as the one used to light the Olympic torch, have a very unique reflecting property. When rays of light parallel to the parabola’s axis of symmetry are directed toward any surface of the mirror, the light is reflected directly to the focus. See Figure 12. This is why the Olympic torch is ignited when it is held at the focus of the parabolic mirror. (x - 4)² = 28(y + 8) y = -15 x = 4 y x

Parabolic mirrors have the ability to focus the sun’s energy to a single point, raising the temperature hundreds of degrees in a matter of seconds. Thus, parabolic mirrors are featured in many low-cost, energy efficient solar products, such as solar cookers, solar heaters, and even travel-sized fire starters.

---
### 📐 **Example  6**: Solving Applied Problems Involving Parabolas

A cross-section of a design for a travel-sized solar fire starter is shown in Figure 13. The sun’s rays reflect off the parabolic mirror toward an object attached to the igniter. Because the igniter is located at the focus of the parabola, the reflected rays cause the object to burn in just seconds. a. Find the equation of the parabola that models the fire starter. Assume that the vertex of the parabolic mirror is the origin of the coordinate plane. b. Use the equation found in part ( a) to find the depth of the fire starter.

**Solution**

a. The vertex of the dish is the origin of the coordinate plane, so the parabola will take the standard form x 2 = 4py, where p > 0. The igniter, which is the focus, is 1.7 inches above the vertex of the dish. Thus we have p = 1.7.

x 2 = 4py Standard form of upward-facing parabola with vertex (0, 0)

Substitute 1.7 for p.

Multiply. b. The dish extends  4.5 ___ 2  = 2.25 inches on either side of the origin. We can substitute 2.25 for x in the equation from part ( a) to find the depth of the dish.

Equation found in part ( a).

Substitute 2.25 for x.

Solve for y. The dish is about 0.74 inches deep. Parallel rays of sunlight Parabolic reflector Focus Igniter Depth

---
### ✏️ **Try It #6**
Balcony-sized solar cookers have been designed for families living in India. The top of a dish has a diameter of 1,600 mm. The sun’s rays reflect off the parabolic mirror toward the “cooker,” which is placed 320 mm from the base. a. Find an equation that models a cross-section of the solar cooker. Assume that the vertex of the parabolic mirror is the origin of the coordinate plane, and that the parabola opens to the right (i.e., has the x-axis as its axis of symmetry). b. Use the equation found in part (a) to find the depth of the cooker. Access these online resources for additional instruction and practice with parabolas. • Conic Sections: The Parabola Part 1 of 2 (http://openstaxcollege.org/l/parabola¹) • Conic Sections: The Parabola Part 2 of 2 (http://openstaxcollege.org/l/parabola²) • Parabola with Vertical Axis (http://openstaxcollege.org/l/parabolavertcal) • Parabola with Horizontal Axis (http://openstaxcollege.org/l/parabolahoriz)

### 10.3 Section Exercises

Verbal 1. Define a parabola in terms of its focus and directrix. 2. If the equation of a parabola is written in standard form and p is positive and the directrix is a vertical line, then what can we conclude about its graph? 3. If the equation of a parabola is written in standard form and p is negative and the directrix is a horizontal line, then what can we conclude about its graph? 4. What is the effect on the graph of a parabola if its equation in standard form has increasing values of p? 5. As the graph of a parabola becomes wider, what will happen to the distance between the focus and directrix? Algebraic For the following exercises, determine whether the given equation is a parabola. If so, rewrite the equation in standard form. 6. y 2 = 4 - x 2 9. (y - 3)² = 8(x - 2) For the following exercises, rewrite the given equation in standard form, and then determine the vertex (V), focus (F), and directrix (d) of the parabola. __ 4 x 2/8 y 2 ___ 17. (x - 1)² = 4(y - 1) 18. (y - 2)² =  4/5 (x + 4) 19. (y - 4)² = 2(x + 3) 20. (x + 1)² = 2(y + 4) 21. (x + 4)² = 24(y + 1) 22. (y + 4)² = 16(x + 4) 27. x 2 - 4x + 2y - 6 = 0 28. y 2 - 6y + 12x - 3 = 0 30. x 2 + 4x + 8y - 4 = 0 Graphical For the following exercises, graph the parabola, labeling the focus and the directrix. __ 8 y 2 ___ 35. (y - 2)² = - 4/3 (x + 2) 36. -5(x + 5)² = 4(y + 5) 37. -6(y + 5)² = 4(x - 4) 38. y 2 - 6y - 8x + 1 = 0 39. x 2 + 8x + 4y + 20 = 0 41. y 2 - 8x + 10y + 9 = 0 42. x 2 + 4x + 2y + 2 = 0 44. -2x 2 + 8x - 4y - 24 = 0 For the following exercises, find the equation of the parabola given information about its graph. 45. Vertex is (0, 0); directrix is y = 4, focus is (0, -4). 46. Vertex is (0, 0); directrix is x = 4, focus is (-4, 0). 47. Vertex is (2, 2); directrix is x = 2 - √2 , focus is (2 + √48. Vertex is (-2, 3); directrix is x = - 7/2 , focus is ( -  1/2 , 3 ) . 49. Vertex is (√2 , - √3 ); directrix is x = 2√2 , focus is (0, -√3 ). 50. Vertex is (1, 2); directrix is y =  11 ___ 3  , focus is ( 1,  1/3  ) .

## 10.3 Section Exercises

---
For the following exercises, determine the equation for the parabola from its graph. x Axis of symmetry Focus Vertex y y x Axis of symmetry Vertex Focus y x Axis of symmetry Focus Vertex - 31 Vertex Axis of symmetry Focus y x y x Axis of symmetry Vertex Focus

Extensions For the following exercises, the vertex and endpoints of the latus rectum of a parabola are given. Find the equation. 57. V(0, 0), Endpoints (-2, 4), (-2, -4) 59. V(-3, -1), Endpoints (0, 5), (0, -7) 60. V(4, -3), Endpoints ( 5, - 7/2  ) , ( 3, - 7/2  )  Real-World Applications 61. The mirror in an automobile headlight has a parabolic cross-section with the light bulb at the focus. On a schematic, the equation of the parabola is given as x 2 = 4y. At what coordinates should you place the light bulb? 62. If we want to construct the mirror from the previous exercise such that the focus is located at (0, 0.25), what should the equation of the parabola be? 63. A satellite dish is shaped like a paraboloid of revolution. This means that it can be formed by rotating a parabola around its axis of symmetry. The receiver is to be located at the focus. If the dish is 12 feet across at its opening and 4 feet deep at its center, where should the receiver be placed? 64. Consider the satellite dish from the previous exercise. If the dish is 8 feet across at the opening and 2 feet deep, where should we place the receiver? 65. A searchlight is shaped like a paraboloid of revolution. A light source is located 1 foot from the base along the axis of symmetry. If the opening of the searchlight is 3 feet across, find the depth. 66. If the searchlight from the previous exercise has the light source located 6 inches from the base along the axis of symmetry and the opening is 4 feet, find the depth. 67. An arch is in the shape of a parabola. It has a span of 100 feet and a maximum height of 20 feet. Find the equation of the parabola, and determine the height of the arch 40 feet from the center. 68. If the arch from the previous exercise has a span of 160 feet and a maximum height of 40 feet, find the equation of the parabola, and determine the distance from the center at which the height is 69. An object is projected so as to follow a parabolic path given by y = -x 2 + 96x, where x is the horizontal distance traveled in feet and y is the height. Determine the maximum height the object reaches. 70. For the object from the previous exercise, assume the path followed is given by y = -0.5x 2 + 80x. Determine how far along the horizontal the object traveled to reach maximum height.

