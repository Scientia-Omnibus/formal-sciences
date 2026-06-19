# Periodic Functions

## Introduction
Each day, the sun rises in an easterly direction, approaches some maximum height relative to the celestial equator, and sets in a westerly direction. The celestial equator is an imaginary line that divides the visible universe into two halves in much the same way Earth’s equator is an imaginary line that divides the planet into two halves. The exact path the sun appears to follow depends on the exact location on Earth, but each location observes a predictable pattern over time. The pattern of the sun’s motion throughout the course of a year is a periodic function. Creating a visual representation of a periodic function in the form of a graph can help us analyze the properties of the function. In this chapter, we will investigate graphs of sine, cosine, and other trigonometric functions. 6.1 Graphs of the Sine and Cosine Functions 6.2 Graphs of the Other Trigonometric Functions 6.3 Inverse Trigonometric Functions

Learning Objectives
In this section, you will:
• Graph variations of y = sin(x ) and y = cos(x ).
• Use phase shifts of sine and cosine curves.

## 6.1 Graphs of the Sine and Cosine Functions
White light, such as the light from the sun, is not actually white at all. Instead, it is a composition of all the colors of the rainbow in the form of waves. The individual colors can be seen only when white light passes through an optical prism that separates the waves according to their wavelengths to form a rainbow. Light waves can be represented graphically by the sine function. In the chapter on Trigonometric Functions, we examined trigonometric functions such as the sine function. In this section, we will interpret and create graphs of sine and cosine functions. Graphing Sine and Cosine Functions Recall that the sine and cosine functions relate real number values to the x- and y-coordinates of a point on the unit circle. So what do they look like on a graph on a coordinate plane? Let’s start with the sine function. We can create a table of values and use them to sketch a graph. Table 1 lists some of the values for the sine function on a unit circle. x  \p\frac{i}{6}   \p\frac{i}{4}   \p\frac{i}{3}   \p\frac{i}{2}   2\p\frac{i}{3}   3\p\frac{i}{4}   5\p\frac{i}{6}  \pi  sin(x)  \frac{1}{2}   \sqrt{2}  _ 2   \sqrt{3}  _ 2   \sqrt{3}  _ 2   \sqrt{2}  _ 2   \frac{1}{2}  Plotting the points from the table and continuing along the x-axis gives the shape of the sine function. See Figure 2. x y 3\pi  5\pi  7\pi  \pi  2\pi  \pi  \pi  3\pi  y = sin (x)

Notice how the sine values are positive between 0 and \pi , which correspond to the values of the sine function in quadrants I and II on the unit circle, and the sine values are negative between \pi  and 2\pi , which correspond to the values of the sine function in quadrants III and IV on the unit circle. See Figure 3. y y = sin (x) x \pi  \pi  \pi  \pi  Now let’s take a similar look at the cosine function. Again, we can create a table of values and use them to sketch a graph. Table 2 lists some of the values for the cosine function on a unit circle. x  \p\frac{i}{6}   \p\frac{i}{4}   \p\frac{i}{3}   \p\frac{i}{2}   2\p\frac{i}{3}   3\p\frac{i}{4}   5\p\frac{i}{6}  \pi  cos(x)  \sqrt{3}  _ 2   \sqrt{2}  _ 2   \frac{1}{2}  - \frac{1}{2}  -  \sqrt{2}  _ 2  -  \sqrt{3}  _ 2  -1 As with the sine function, we can plots points to create a graph of the cosine function as in Figure 4. x y 2\pi  3\pi  5\pi  5\pi  3\pi  7\pi  \pi  2\pi  \pi  \pi  \pi  \pi  y = cos (x) Because we can evaluate the sine and cosine of any real number, both of these functions are defined for all real numbers. By thinking of the sine and cosine values as coordinates of points on a unit circle, it becomes clear that the range of both functions must be the interval [-1, 1]. In both graphs, the shape of the graph repeats after 2\pi , which means the functions are periodic with a period of 2\pi . A periodic function is a function for which a specific horizontal shift, P, results in a function equal to the original function: f (x + P) = f (x) for all values of x in the domain of f . When this occurs, we call the smallest such horizontal shift with P > 0 the period of the function. Figure 5 shows several periods of the sine and cosine functions. –3\pi  3\pi  2\pi  \pi  –2\pi  –\pi  x y y = cos (x) 1 period –3\pi  3\pi  2\pi  \pi  –2\pi  –\pi  x y y = sin (x) 1 period

Looking again at the sine and cosine functions on a domain centered at the y-axis helps reveal symmetries. As we can see in Figure 6, the sine function is symmetric about the origin. Recall from The Other Trigonometric Functions that we determined from the unit circle that the sine function is an odd function because sin(-x) = -sin x. Now we can clearly see this property from the graph. –2\pi  –\pi  2\pi  \pi  x y y = sin (x) is an even function. Now we can see from the graph that cos(-x) = cos x. 2\pi  –2\pi  –\pi  \pi  x y y = cos (x) characteristics of sine and cosine functions The sine and cosine functions have several distinct characteristics: • They are periodic functions with a period of 2\pi . • The domain of each function is (-\infty , \infty ) and the range is [-1, 1]. • The graph of y = sin x is symmetric about the origin, because it is an odd function. • The graph of y = cos x is symmetric about the y- axis, because it is an even function. Investigating Sinusoidal Functions As we can see, sine and cosine functions have a regular period and range. If we watch ocean waves or ripples on a pond, we will see that they resemble the sine or cosine functions. However, they are not necessarily identical. Some are taller or longer than others. A function that has the same general shape as a sine or cosine function is known as a sinusoidal function. The general forms of sinusoidal functions are y = Asin(Bx - C) + D and y = Acos(Bx - C) + D

Determining the Period of Sinusoidal Functions Looking at the forms of sinusoidal functions, we can see that they are transformations of the sine and cosine functions. We can use what we know about transformations to determine the period. In the general formula, B is related to the period by P =  2\pi  _ ∣ B ∣ . If ∣ B ∣ > 1, then the period is less than 2\pi  and the function undergoes a horizontal compression, whereas if ∣ B ∣ < 1, then the period is greater than 2\pi  and the function undergoes a horizontal stretch. For example, f (x) = sin(x), B = 1, so the period is 2\pi , which we knew. If f (x) = sin(2x), then B = 2, so the period is \pi  and the graph is compressed. If f (x) = sin (  \frac{x}{2}  ), then B =  \frac{1}{2} , so the period is 4\pi  and the graph is stretched. Notice in Figure 8 how the period is indirectly related to ∣ B ∣. x y f (x) = sin (2x) f (x) = sin (x) f (x) = sin( ) x \pi  2\pi  \pi  3\pi  period of sinusoidal functions If we let C = 0 and D = 0 in the general form equations of the sine and cosine functions, we obtain the forms y = Asin(Bx) y = Acos(Bx) The period is  2\pi  _ ∣ B ∣ .

**Example  1**

### Identifying the Period of a Sine or Cosine Function
Determine the period of the function f (x) = sin (  \p\frac{i}{6} x ).

**Solution**

Let’s begin by comparing the equation to the general form y = Asin(Bx). In the given equation, B =  \p\frac{i}{6} , so the period will be

P =  2\pi  _ ∣ B ∣ 

=  2\pi  _  \p\frac{i}{6}  

= 2\pi  ⋅  6 _ \pi  

= 12

**Try It #1**
Determine the period of the function g(x) = ( cos \frac{x}{3}  ). Determining Amplitude Returning to the general formula for a sinusoidal function, we have analyzed how the variable B relates to the period. Now let’s turn to the variable A so we can analyze how it is related to the amplitude, or greatest distance from rest. A represents the vertical stretch factor, and its absolute value ∣ A ∣ is the amplitude. The local maxima will be a distance ∣ A ∣ above the vertical midline of the graph, which is the line x = D ; because D = 0 in this case, the midline is the x-axis. The local minima will be the same distance below the midline. If ∣ A ∣ > 1, the function is stretched. For example, the amplitude of f (x) = 4sin x is twice the amplitude of f (x) = 2sin x. If ∣ A ∣ < 1, the function is compressed. Figure 9 compares several sine functions with different amplitudes.

y f (x) = 4 sin(x) f (x) = 3 sin(x) f (x) = 2 sin(x) f (x) = 1 sin(x) 3\pi  5\pi  – 3\pi  – 7\pi  –11\pi  – 5\pi  – 9\pi  9\pi  7\pi  11\pi  amplitude of sinusoidal functions If we let C = 0 and D = 0 in the general form equations of the sine and cosine functions, we obtain the forms y = Asin(Bx) and y = Acos(Bx) The amplitude is A, and the vertical height from the midline is ∣ A ∣. In addition, notice in the example that ∣ A ∣ = amplitude =  \frac{1}{2} ∣ maximum - minimum ∣

**Example  2**

### Identifying the Amplitude of a Sine or Cosine Function
What is the amplitude of the sinusoidal function f (x) = -4sin(x)? Is the function stretched or compressed vertically?

**Solution**

Let’s begin by comparing the function to the simplified form y = Asin(Bx). In the given function, A = -4, so the amplitude is ∣ A ∣ = ∣ -4 ∣ = 4. The function is stretched. Analysis The negative value of A results in a reflection across the x-axis of the sine function, as shown in Figure 10. x y \pi  3\pi  f (x) = -4 sin x – 3\pi  – \pi 

**Try It #2**
What is the amplitude of the sinusoidal function f (x) =  \frac{1}{2}  sin(x)? Is the function stretched or compressed vertically ? Analyzing Graphs of Variations of y = sin x and y = cos x Now that we understand how A and B relate to the general form equation for the sine and cosine functions, we will explore the variables C and D. Recall the general form: y = Asin(Bx - C) + D and y = Acos(Bx - C) + D or y = Asin ( B ( x -  \frac{C}{B}  ) ) + D and y = Acos ( B ( x -  \frac{C}{B}  ) ) + D

The value  \frac{C}{B}  for a sinusoidal function is called the phase shift, or the horizontal displacement of the basic sine or cosine function. If C > 0, the graph shifts to the right. If C < 0, the graph shifts to the left. The greater the value of ∣ C ∣, the more the graph is shifted. Figure 11 shows that the graph of f (x) = sin(x - \pi ) shifts to the right by \pi  units, which is more than we see in the graph of f (x) = sin ( x -  \p\frac{i}{4}  ), which shifts to the right by  \p\frac{i}{4}  units. x y \pi  2\pi  \pi  3\pi  3\pi  5\pi  f (x) = sin(x) f (x) = sin(x - \pi ) f (x) = sin x -\pi  While C relates to the horizontal shift, D indicates the vertical shift from the midline in the general formula for a sinusoidal function. See Figure 12. The function y = cos(x) + D has its midline at y = D. x y \pi  2\pi  3\pi  y = A sin(x) + D y = D Midline Any value of D other than zero shifts the graph up or down. Figure 13 compares f (x) = sin x with f (x) = sin x + 2, which is shifted 2 units up on a graph. x y \pi  2\pi  \pi  3\pi  3\pi  5\pi  f (x) = sin(x) f (x) = sin(x) + 2 variations of sine and cosine functions Given an equation in the form f (x) = Asin(Bx - C) + D or f (x) = Acos(Bx - C) + D,  \frac{C}{B}  is the phase shift and D is the vertical shift.

**Example  3**

### Identifying the Phase Shift of a Function
Determine the direction and magnitude of the phase shift for f (x) = sin ( x +  \p\frac{i}{6}  ) - 2.

**Solution**

Let’s begin by comparing the equation to the general form y = Asin(Bx - C) + D.

In the given equation, notice that B = 1 and C = - \p\frac{i}{6} . So the phase shift is

 \frac{C}{B}  = -  \pi  __ \frac{6}{1} 

= - \p\frac{i}{6}  or  \p\frac{i}{6}  units to the left. Analysis We must pay attention to the sign in the equation for the general form of a sinusoidal function. The equation shows a minus sign before C. Therefore f (x) = sin ( x +  \p\frac{i}{6}  ) - 2 can be rewritten as f (x) = sin ( x - ( - \p\frac{i}{6}  ) ) - 2. If the value of C is negative, the shift is to the left.

**Try It #3**
Determine the direction and magnitude of the phase shift for f (x) = 3cos( x -  \p\frac{i}{2}  ).

**Example  4**

### Identifying the Vertical Shift of a Function
Determine the direction and magnitude of the vertical shift for f (x) = cos(x) - 3.

**Solution**

Let’s begin by comparing the equation to the general form y = Acos(Bx - C) + D. In the given equation, D = -3 so the shift is 3 units downward.

**Try It #4**
Determine the direction and magnitude of the vertical shift for f (x) = 3sin(x) + 2.

**How To…**
Given a sinusoidal function in the form f (x) = Asin(Bx - C) + D, identify the midline, amplitude, period, and phase shift. 1. Determine the amplitude as ∣ A ∣. 2. Determine the period as P =  2\pi  _ ∣ B ∣ . 3. Determine the phase shift as  \frac{C}{B} . 4. Determine the midline as y = D.

**Example  5**

### Identifying the Variations of a Sinusoidal Function from an Equation
Determine the midline, amplitude, period, and phase shift of the function y = 3sin(2x) + 1.

**Solution**

Let’s begin by comparing the equation to the general form y = Asin(Bx - C) + D. A = 3, so the amplitude is ∣ A ∣ = 3. Next, B = 2, so the period is P =  2\pi  _ ∣ B ∣  =  2\p\frac{i}{2}  = \pi . There is no added constant inside the parentheses, so C = 0 and the phase shift is  \frac{C}{B}  =  \frac{0}{F}inally, D = 1, so the midline is y = 1. Analysis Inspecting the graph, we can determine that the period is \pi , the midline is y = 1, and the amplitude is 3. See

\pi  2\pi  \pi  3\pi  Midline: y = 1 x y Amplitude: |A| = 3 Period = \pi  y = 3 sin (2x) + 1

**Try It #5**
Determine the midline, amplitude, period, and phase shift of the function y =  \frac{1}{2} cos (  \frac{x}{3}  –  \p\frac{i}{3}  ).

**Example  6**

### Identifying the Equation for a Sinusoidal Function from a Graph
Determine the formula for the cosine function in Figure 15. 0.5 –2\pi  –\pi  2\pi  \pi  3\pi  4\pi  x y

**Solution**

To determine the equation, we need to identify each value in the general form of a sinusoidal function. y = Asin(Bx - C) + D y = Acos(Bx - C) + D The graph could represent either a sine or a cosine function that is shifted and/or reflected. When x = 0, the graph has an extreme point, (0, 0). Since the cosine function has an extreme point for x = 0, let us write our equation in terms of a cosine function. Let’s start with the midline. We can see that the graph rises and falls an equal distance above and below y = 0.5. This value, which is the midline, is D in the equation, so D = 0.5. The greatest distance above and below the midline is the amplitude. The maxima are 0.5 units above the midline and the minima are 0.5 units below the midline. So ∣ A ∣ = 0.5. Another way we could have determined the amplitude is by recognizing that the difference between the height of local maxima and minima is 1, so ∣ A ∣ =  \frac{1}{2}  = 0.5. Also, the graph is reflected about the x-axis so that A = -0.5. The graph is not horizontally stretched or compressed, so B = 1; and the graph is not shifted horizontally, so C = 0. Putting this all together, g(x) = -0.5cos(x) + 0.5

**Try It #6**
Determine the formula for the sine function in Figure 16. –2\pi  –\pi  2\pi  \pi  x y


**Example  7**

### Identifying the Equation for a Sinusoidal Function from a Graph
Determine the equation for the sinusoidal function in Figure 17. x y

**Solution**

With the highest value at 1 and the lowest value at -5, the midline will be halfway between at -2. So D = -2. The distance from the midline to the highest or lowest value gives an amplitude of ∣ A ∣ = 3. The period of the graph is 6, which can be measured from the peak at x = 1 to the next peak at x = 7, or from the distance between the lowest points. Therefore, P =  2\pi  _ ∣ B ∣  = 6. Using the positive value for B, we find that B =  2\p\frac{i}{P}  =  2\p\frac{i}{6}  =  \p\frac{i}{3}  So far, our equation is either y = 3sin (  \p\frac{i}{3} x - C ) - 2 or y = 3cos (  \p\frac{i}{3} x - C ) - 2. For the shape and shift, we have more than one option. We could write this as any one of the following: • a cosine shifted to the right • a negative cosine shifted to the left • a sine shifted to the left • a negative sine shifted to the right While any of these would be correct, the cosine shifts are easier to work with than the sine shifts in this case because they involve integer values. So our function becomes y = 3cos (  \p\frac{i}{3} x -  \p\frac{i}{3}  ) - 2 or y = -3cos (  \p\frac{i}{3} x +  2\p\frac{i}{3}  ) -2 Again, these functions are equivalent, so both yield the same graph.

**Try It #7**
Write a formula for the function graphed in Figure 18. x y


### Graphing Variations of y = sin x and y = cos x
Throughout this section, we have learned about types of variations of sine and cosine functions and used that information to write equations from graphs. Now we can use the same information to create graphs from equations. Instead of focusing on the general form equations y = Asin(Bx - C) + D and y = Acos(Bx - C) + D, we will let C = 0 and D = 0 and work with a simplified form of the equations in the following examples.

**How To…**
Given the function y = Asin(Bx), sketch its graph. 1. Identify the amplitude, ∣ A ∣. 2. Identify the period, P =  2\pi  ___ ∣ B ∣ . 3. Start at the origin, with the function increasing to the right if A is positive or decreasing if A is negative. 4. At x =  \pi  ____ 2∣ B ∣  there is a local maximum for A > 0 or a minimum for A < 0, with y = A. 5. The curve returns to the x-axis at x =  \pi  ___ ∣ B ∣ . 6. There is a local minimum for A > 0 (maximum for A < 0 ) at x =  3\pi  ____ 2∣ B ∣  with y = -A. 7. The curve returns again to the x-axis at x =  \pi  ____ 2∣ B ∣ .

**Example  8**

### Graphing a Function and Identifying the Amplitude and Period
Sketch a graph of f (x) = -2sin(  \pi \frac{x}{2}  ).

**Solution**

Let’s begin by comparing the equation to the form y = Asin(Bx). Step 1. We can see from the equation that A = -2, so the amplitude is 2. ∣ A ∣ = 2 Step 2. The equation shows that B =  \p\frac{i}{2} , so the period is

P =  2\pi  _  \p\frac{i}{2}  

= 2\pi  ⋅  2 __ \pi  

= 4 Step 3. Because A is negative, the graph descends as we move to the right of the origin. Step 4–7. The x-intercepts are at the beginning of one period, x = 0, the horizontal midpoints are at x = 2 and at the end of one period at x = 4. The quarter points include the minimum at x = 1 and the maximum at x = 3. A local minimum will occur 2 units below the midline, at x = 1, and a local maximum will occur at 2 units above the midline, at x = 3. Figure 19 shows the graph of the function. x y y = f (x) = -2sin \pi x


**Try It #8**
Sketch a graph of g(x) = -0.8cos(2x). Determine the midline, amplitude, period, and phase shift.

**How To…**
Given a sinusoidal function with a phase shift and a vertical shift, sketch its graph. 1. Express the function in the general form y = Asin(Bx - C) + D or y = Acos(Bx - C) + D. 2. Identify the amplitude, ∣ A ∣. 3. Identify the period, P =  2\pi  ___ ∣ B ∣ . 4. Identify the phase shift,  \frac{C}{B} . 5. Draw the graph of f (x) = Asin(Bx) shifted to the right or left by  \frac{C}{B}  and up or down by D.

**Example  9**

### Graphing a Transformed Sinusoid
Sketch a graph of f (x) = 3sin (  \p\frac{i}{4} x -  \p\frac{i}{4}  ).

**Solution**
Step 1. The function is already written in general form: f (x) = 3sin (  \p\frac{i}{4} x -  \p\frac{i}{4}  ). This graph will have the shape of a sine function, starting at the midline and increasing to the right. Step 2. ∣ A ∣ = ∣ 3 ∣ = 3. The amplitude is 3. Step 3. Since ∣ B ∣ =   \p\frac{i}{4}   =  \p\frac{i}{4} , we determine the period as follows. P =  2\pi  ___ ∣ B ∣  =  2\pi  _  \p\frac{i}{4}   = 2\pi  ⋅  4 _ \pi   = 8 The period is 8. Step 4. Since C =  \p\frac{i}{4} , the phase shift is  \frac{C}{B}  =   \p\frac{i}{4}  _  \p\frac{i}{4}   = 1. The phase shift is 1 unit. Step 5. Figure 20 shows the graph of the function. x y f (x) = 3 sin 4 \pi  \pi  x -


**Try It #9**
Draw a graph of g(x) = -2cos (  \p\frac{i}{3} x +  \p\frac{i}{6}  ). Determine the midline, amplitude, period, and phase shift.

**Example  10**

### Identifying the Properties of a Sinusoidal Function
Given y = -2cos (  \p\frac{i}{2} x + \pi  ) + 3, determine the amplitude, period, phase shift, and horizontal shift. Then graph the function.

**Solution**

Begin by comparing the equation to the general form and use the steps outlined in Example 9. y = Acos(Bx - C) + D Step 1. The function is already written in general form. Step 2. Since A = -2, the amplitude is ∣ A ∣ = 2. Step 3. ∣ B ∣ =  \p\frac{i}{2} , so the period is P =  2\pi  ___ ∣ B ∣  =  2\pi  _  \p\frac{i}{2}   = 2\pi  ⋅  2 __ \pi   = 4. The period is 4. Step 4. C = -\pi , so we calculate the phase shift as  \frac{C}{B}  =  -\pi  _  \p\frac{i}{2}   = -\pi  ⋅  2 __ \pi   = -2. The phase shift is -2. Step 5. D = 3, so the midline is y = 3, and the vertical shift is up 3. Since A is negative, the graph of the cosine function has been reflected about the x-axis. Figure 21 shows one cycle of the graph of the function. x y Midline: y = 3 Period = 4 Amplitude = 2 y = -2 cos 2 \pi x + \pi  + 3 Using Transformations of Sine and Cosine Functions We can use the transformations of sine and cosine functions in numerous applications. As mentioned at the beginning of the chapter, circular motion can be modeled using either the sine or cosine function.

**Example  11**
Finding the Vertical Component of Circular Motion A point rotates around a circle of radius 3 centered at the origin. Sketch a graph of the y-coordinate of the point as a function of the angle of rotation.

**Solution**

Recall that, for a point on a circle of radius r, the y-coordinate of the point is y = r sin(x), so in this case, we get the equation y(x) = 3 sin(x). The constant 3 causes a vertical stretch of the y-values of the function by a factor of 3, which we can see in the graph in Figure 22. \pi  3\pi  5\pi  7\pi  x y y(x) = 3 sin x


**Analysis**
Notice that the period of the function is still 2\pi  ; as we travel around the circle, we return to the point (3, 0) for x = 2\pi , 4\pi , 6\pi , ... Because the outputs of the graph will now oscillate between –3 and 3, the amplitude of the sine wave is 3.

**Try It #10**
What is the amplitude of the function f (x) = 7cos(x)? Sketch a graph of this function.

**Example  12**
Finding the Vertical Component of Circular Motion A circle with radius 3 ft is mounted with its center 4 ft off the ground. The point closest to the ground is labeled P, as shown in Figure 23. Sketch a graph of the height above the ground of the point P as the circle is rotated; then find a function that gives the height in terms of the angle of rotation. P 3 f 4 f

**Solution**

Sketching the height, we note that it will start 1 ft above the ground, then increase up to 7 ft above the ground, and continue to oscillate 3 ft above and below the center value of 4 ft, as shown in Figure 24. \pi  2\pi  3\pi  4\pi  x y Midline: y = 4 y = -3 cos x + 4 Although we could use a transformation of either the sine or cosine function, we start by looking for characteristics that would make one function easier to use than the other. Let’s use a cosine function because it starts at the highest or lowest value, while a sine function starts at the middle value. A standard cosine starts at the highest value, and this graph starts at the lowest value, so we need to incorporate a vertical reflection. Second, we see that the graph oscillates 3 above and below the center, while a basic cosine has an amplitude of 1, so this graph has been vertically stretched by 3, as in the last example. Finally, to move the center of the circle up to a height of 4, the graph has been vertically shifted up by 4. Putting these transformations together, we find that y = -3cos(x) + 4


**Try It #11**
A weight is attached to a spring that is then hung from a board, as shown in Figure 25. As the spring oscillates up and down, the position y of the weight relative to the board ranges from -1 in. (at time x = 0) to -7 in. (at time x = \pi ) below the board. Assume the position of y is given as a sinusoidal function of x. Sketch a graph of the function, and then find a cosine function that gives the position y in terms of x. y

**Example  13**
Determining a Rider’s Height on a Ferris Wheel The London Eye is a huge Ferris wheel with a diameter of 135 meters (443 feet). It completes one rotation every 30 minutes. Riders board from a platform 2 meters above the ground. Express a rider’s height above ground as a function of time in minutes.

**Solution**

With a diameter of 135 m, the wheel has a radius of 67.5 m. The height will oscillate with amplitude 67.5 m above and below the center. Passengers board 2 m above ground level, so the center of the wheel must be located 67.5 + 2 = 69.5 m above ground level. The midline of the oscillation will be at 69.5 m. The wheel takes 30 minutes to complete 1 revolution, so the height will oscillate with a period of 30 minutes. Lastly, because the rider boards at the lowest point, the height will start at the smallest value and increase, following the shape of a vertically reflected cosine curve. • Amplitude: 67.5, so A = 67.5 • Midline: 69.5, so D = 69.5 • Period: 30, so B =  2\pi  ___ 30  =  \p\frac{i}{15}  • Shape: -cos(t) An equation for the rider’s height would be y = - 67.5cos(  \p\frac{i}{w}here t is in minutes and y is measured in meters. Access these online resources for additional instruction and practice with graphs of sine and cosine functions. • Amplitude and Period of Sine and Cosine (http://openstaxcollege.org/l/ampperiod) • Translations of Sine and Cosine (http://openstaxcollege.org/l/translasincos) • Graphing Sine and Cosine Transformations (http://openstaxcollege.org/l/transformsincos) • Graphing the Sine Function (http://openstaxcollege.org/l/graphsinefunc)

6.1 Section EXERCISES Verbal 1. Why are the sine and cosine functions called periodic functions? 2. How does the graph of y = sin x compare with the graph of y = cos x? Explain how you could horizontally translate the graph of y = sin x to obtain y = cos x. 3. For the equation Acos(Bx + C) + D, what constants affect the range of the function and how do they affect the range? 4. How does the range of a translated sine function relate to the equation y = Asin(Bx + C) + D? 5. How can the unit circle be used to construct the graph of f(t) = sin t? Graphical For the following exercises, graph two full periods of each function and state the amplitude, period, and midline. State the maximum and minimum y-values and their corresponding x-values on one period for x > 0. Round answers to two decimal places if necessary. 6. f (x) = 2sin x 7. f (x) =  \frac{2}{3} cos x 8. f (x) = -3sin x 9. f (x) = 4sin x 10. f (x) = 2cos x 11. f (x) = cos(2x) 12. f (x) = 2sin(  \frac{1}{2} x ) 13. f (x) = 4cos(\pi x) 14. f (x) = 3cos (  \frac{6}{5} x ) 15. y = 3sin(8(x + 4)) + 5 16. y = 2sin(3x - 21) + 4 17. y = 5sin(5x + 20) - 2 For the following exercises, graph one full period of each function, starting at x = 0. For each function, state the amplitude, period, and midline. State the maximum and minimum y-values and their corresponding x-values on one period for x > 0. State the phase shift and vertical translation, if applicable. Round answers to two decimal places if necessary. 18. f(t) = 2sin ( t -  5\pi  ___ 6  ) 19. f(t) = -cos ( t +  \p\frac{i}{3}  ) + 1 20. f (t) = 4cos ( 2( t +  \p\frac{i}{4}  ) ) - 3 21. f(t) = -sin (  \frac{1}{2} t +  5\pi  ___ 3  ) 22. f (x) = 4sin (  \p\frac{i}{2} (x - 3) ) + 7 23. Determine the amplitude, midline, period, and an equation involving the sine function for the graph shown in Figure 26. x f(x) 24. Determine the amplitude, period, midline, and an equation involving cosine for the graph shown in x f(x) \pi  –\pi  \pi  3\pi  3\pi  \pi 


## 6.1 Section Exercises
25. Determine the amplitude, period, midline, and an equation involving cosine for the graph shown in x f(x) 26. Determine the amplitude, period, midline, and an equation involving sine for the graph shown in x f(x) 27. Determine the amplitude, period, midline, and an equation involving cosine for the graph shown in - x f(x) -2 + \pi  \pi  \pi  28. Determine the amplitude, period, midline, and an equation involving sine for the graph shown in x f(x) 29. Determine the amplitude, period, midline, and an equation involving cosine for the graph shown in x f(x) 30. Determine the amplitude, period, midline, and an equation involving sine for the graph shown in x f(x)

Algebraic For the following exercises, let f (x) = sin x. 31. On [0, 2\pi ), solve f (x) = 0. 32. On [0, 2\pi ), solve f (x) =  \frac{1}{2} . 33. Evaluate f (  \p\frac{i}{2}  ). 34. On [0, 2\pi ), f (x) =  \sqrt{2}  ____ 2 . Find all values of x. 35. On [0, 2\pi ), the maximum value(s) of the function occur(s) at what x-value(s)? 36. On [0, 2\pi ), the minimum value(s) of the function occur(s) at what x-value(s)? 37. Show that f(-x) = -f (x). This means that f (x) = sin x is an odd function and possesses symmetry with respect to ________________. For the following exercises, let f (x) = cos x. 38. On [0, 2\pi ), solve the equation f (x) = cos x = 0. 39. On [0, 2\pi ), solve f (x) =  \frac{1}{2} . 40. On [0, 2\pi ), find the x-intercepts of f (x) = cos x. 41. On [0, 2\pi ), find the x-values at which the function has a maximum or minimum value. 42. On [0, 2\pi ), solve the equation f (x) =  \sqrt{3}  ____ 2 . Technology 43. Graph h(x) = x + sin x on [0, 2\pi ]. Explain why the graph appears as it does. 44. Graph h(x) = x + sin x on [-100, 100]. Did the graph appear as predicted in the previous exercise? 45. Graph f (x) = x sin x on [0, 2\pi ] and verbalize how the graph varies from the graph of f (x) = sin x. 46. Graph f (x) = x sin x on the window [-10, 10] and explain what the graph shows. 47. Graph f (x) =  sin x ____ x  on the window [-5\pi , 5\pi ] and explain what the graph shows. Real-World Applications 48. A Ferris wheel is 25 meters in diameter and boarded from a platform that is 1 meter above the ground. The six o’clock position on the Ferris wheel is level with the loading platform. The wheel completes 1 full revolution in 10 minutes. The function h(t) gives a person’s height in meters above the ground t minutes after the wheel begins to turn. a. Find the amplitude, midline, and period of h(t). b. Find a formula for the height function h(t). c. How high off the ground is a person after 5 minutes?


## 6.2 Graphs of the Other Trigonometric Functions
Learning Objectives
In this section, you will:
•
Analyze the graph of y = tan x. • Graph variations of y = tan x. • Analyze the graphs of y = sec x and y = csc x. • Graph variations of y = sec x and y = csc x. • Analyze the graph of y = cot x. • Graph variations of y = cot x.
We know the tangent function can be used to find distances, such as the height of a building, mountain, or flagpole. But what if we want to measure repeated occurrences of distance? Imagine, for example, a police car parked next to a warehouse. The rotating light from the police car would travel across the wall of the warehouse in regular intervals. If the input is time, the output would be the distance the beam of light travels. The beam of light would repeat the distance at regular intervals. The tangent function can be used to approximate this distance. Asymptotes would be needed to illustrate the repeated cycles when the beam runs parallel to the wall because, seemingly, the beam of light could appear to extend forever. The graph of the tangent function would clearly illustrate the repeated intervals. In this section, we will explore the graphs of the tangent and other trigonometric functions. Analyzing the Graph of y = tan x We will begin with the graph of the tangent function, plotting points as we did for the sine and cosine functions. Recall that tan x =  sin x ____ cos x  The period of the tangent function is \pi  because the graph repeats itself on intervals of k\pi  where k is a constant. If we graph the tangent function on - \p\frac{i}{2}  to  \p\frac{i}{2} , we can see the behavior of the graph on one complete cycle. If we look at any larger interval, we will see that the characteristics of the graph repeat. We can determine whether tangent is an odd or even function by using the definition of tangent. tan(-x) =  sin(-x) ______ cos(-x)  Definition of tangent. =  -sin x ______ cos x  Sine is an odd function, cosine is even. = - sin x ____ cos x  The quotient of an odd and an even function is odd. = -tan x Definition of tangent. Therefore, tangent is an odd function. We can further analyze the graphical behavior of the tangent function by looking at values for some of the special angles, as listed in Table 1. x - \p\frac{i}{2}  - \p\frac{i}{3}  - \p\frac{i}{4}  - \p\frac{i}{6}   \p\frac{i}{6}   \p\frac{i}{4}   \p\frac{i}{3}   \p\frac{i}{2}  tan(x) undefined -\sqrt{3}  -1 -  \sqrt{3}  ____ 3  \sqrt{3}  ____ 3  \sqrt{3}  undefined These points will help us draw our graph, but we need to determine how the graph behaves where it is undefined. If we look more closely at values when  \p\frac{i}{3}  < x <  \p\frac{i}{2} , we can use a table to look for a trend. Because  \pi  _  \p\frac{i}{2}  ≈ 1.57, we will evaluate x at radian measures 1.05 < x < 1.57 as shown in Table 2.

x 1.3 1.5 1.55 1.56 tan x 3.6 14.1 48.1 92.6 As x approaches  \p\frac{i}{2} , the outputs of the function get larger and larger. Because y = tan x is an odd function, we see the corresponding table of negative values in Table 3. x -1.3 -1.5 -1.55 -1.56 tan x -3.6 -14.1 -48.1 -92.6 We can see that, as x approaches - \p\frac{i}{2} , the outputs get smaller and smaller. Remember that there are some values of x for which cos x = 0. For example, cos (  \p\frac{i}{2}  ) = 0 and cos (  3\p\frac{i}{2}  ) = 0. At these values, the tangent function is undefined, so the graph of y = tan x has discontinuities at x =  \p\frac{i}{2}  and  3\p\frac{i}{2} . At these values, the graph of the tangent has vertical asymptotes. Figure 1 represents the graph of y = tan x. The tangent is positive from 0 to  \p\frac{i}{2}  and from \pi  to  3\p\frac{i}{2} , corresponding to quadrants I and III of the unit circle. \pi  –\pi  x y x = -\pi  \pi  x = x = -3\pi  3\pi  x = y = tan(x) Graphing Variations of y = tan x As with the sine and cosine functions, the tangent function can be described by a general equation. y = Atan(Bx) We can identify horizontal and vertical stretches and compressions using values of A and B. The horizontal stretch can typically be determined from the period of the graph. With tangent graphs, it is often necessary to determine a vertical stretch using a point on the graph. Because there are no maximum or minimum values of a tangent function, the term amplitude cannot be interpreted as it is for the sine and cosine functions. Instead, we will use the phrase stretching/compressing factor when referring to the constant A. features of the graph of y = Atan(Bx) • The stretching factor is ∣ A ∣. • The period is P =  \pi  ___ ∣ B ∣ . • The domain is all real numbers x, where x \neq   \pi  ____ 2∣ B ∣  +  \pi  _ ∣ B ∣ k such that k is an integer. • The range is (-\infty , \infty ). • The asymptotes occur at x =  \p\frac{i}{2}∣ B ∣  +  \pi  _ ∣ B ∣ k, where k is an integer. • y = Atan(Bx) is an odd function.


### Graphing One Period of a Stretched or Compressed Tangent Function
We can use what we know about the properties of the tangent function to quickly sketch a graph of any stretched and/ or compressed tangent function of the form f (x) = Atan(Bx). We focus on a single period of the function including the origin, because the periodic property enables us to extend the graph to the rest of the function’s domain if we wish. Our limited domain is then the interval ( - \frac{P}{2} ,  \frac{P}{2}  ) and the graph has vertical asymptotes at \pm  \frac{P}{2}  where P =  \p\frac{i}{B} . On ( - \p\frac{i}{2} ,  \p\frac{i}{2}  ), the graph will come up from the left asymptote at x = - \p\frac{i}{2} , cross through the origin, and continue to increase as it approaches the right asymptote at x =  \p\frac{i}{2} . To make the function approach the asymptotes at the correct rate, we also need to set the vertical scale by actually evaluating the function for at least one point that the graph will pass through. For example, we can use f (  \frac{P}{4}  ) = Atan ( B \frac{P}{4}  ) = Atan ( B \p\frac{i}{4}B  ) = A because tan (  \p\frac{i}{4}  ) = 1.

**How To…**
Given the function f (x) = Atan(Bx), graph one period. 1. Identify the stretching factor, ∣ A ∣. 2. Identify B and determine the period, P =  \pi  _ ∣ B ∣ . 3. Draw vertical asymptotes at x = - \frac{P}{2}  and x =  \frac{P}{2} . 4. For A > 0, the graph approaches the left asymptote at negative output values and the right asymptote at positive output values (reverse for A < 0). 5. Plot reference points at (  \frac{P}{4} , A ), (0, 0), and ( - \frac{P}{4} , -A ), and draw the graph through these points.

**Example  1**

### Sketching a Compressed Tangent
Sketch a graph of one period of the function y = 0.5tan (  \p\frac{i}{2} x ).

**Solution**

First, we identify A and B.

y = 0.5 tan (  \p\frac{i}{2} x )

↑

y = Atan(Bx) Because A = 0.5 and B =  \p\frac{i}{2} , we can find the stretching/compressing factor and period. The period is  \pi  _  \p\frac{i}{2}   = 2, so the asymptotes are at x = \pm 1. At a quarter period from the origin, we have

f (0.5) = 0.5tan (  0.5\pi  ____ 2  )

= 0.5tan (  \p\frac{i}{4}  )

= 0.5 This means the curve must pass through the points (0.5, 0.5), (0, 0), and (-0.5, -0.5). The only inflection point is at the origin. Figure 2 shows the graph of one period of the function.

x = -1 x = 1 x y y = 0.5 tan 2 \pi x

**Try It #1**
Sketch a graph of f (x) = 3tan (  \p\frac{i}{6} x ). Graphing One Period of a Shifted Tangent Function Now that we can graph a tangent function that is stretched or compressed, we will add a vertical and/or horizontal (or phase) shift. In this case, we add C and D to the general form of the tangent function. f (x) = Atan(Bx - C) + D The graph of a transformed tangent function is different from the basic tangent function tan x in several ways: features of the graph of y = Atan(Bx - C) + D • The stretching factor is ∣ A ∣. • The period is  \pi  ___ ∣ B ∣ . • The domain is x \neq   \frac{C}{B}  +  \pi  ___ 2∣ B ∣ k, where k is an odd integer. • The range is (-\infty , \infty ). • The vertical asymptotes occur at x =  \frac{C}{B}  +  \pi  ____ 2∣ B ∣ k, where k is an odd integer. • There is no amplitude. • y = Atan(Bx) is an odd function because it is the quotient of odd and even functions (sine and cosine respectively).

**How To…**
Given the function y = Atan(Bx - C) + D, sketch the graph of one period. 1. Express the function given in the form y = Atan(Bx - C) + D. 2. Identify the stretching/compressing factor, ∣ A ∣. 3. Identify B and determine the period, P =  \pi  ___ ∣ B ∣ . 4. Identify C and determine the phase shift,  \frac{C}{B} . 5. Draw the graph of y = Atan(Bx) shifted to the right by  \frac{C}{B}  and up by D. 6. Sketch the vertical asymptotes, which occur at x =  \frac{C}{B}  +  \pi  ____ 2∣ B ∣ k, where k is an odd integer. 7. Plot any three reference points and draw the graph through these points.


**Example  2**

### Graphing One Period of a Shifted Tangent Function
Graph one period of the function y = -2tan(\pi x + \pi ) - 1.

**Solution**
Step 1. The function is already written in the form y = Atan(Bx - C) + D. Step 2. A = -2, so the stretching factor is ∣ A ∣ = 2. Step 3. B = \pi , so the period is P =  \pi  ___ ∣ B ∣  =  \pi  __ \pi   = 1. Step 4. C = -\pi , so the phase shift is  \frac{C}{B}  =  -\pi  ___ \pi   = -1. Step 5-7. The asymptotes are at x = - \frac{3}{2}  and x = - \frac{1}{2}  and the three recommended reference points are (-1.25, 1), (-1, -1), and (-0.75, -3). The graph is shown in Figure 3. 0.5 x y y = -2 tan (\pi x + \pi ) - 1 Analysis Note that this is a decreasing function because A < 0.

**Try It #2**
How would the graph in Example 2 look different if we made A = 2 instead of -2?

**How To…**
Given the graph of a tangent function, identify horizontal and vertical stretches. 1. Find the period P from the spacing between successive vertical asymptotes or x-intercepts. 2. Write f (x) = Atan(  \p\frac{i}{P} x ). 3. Determine a convenient point (x, f (x)) on the given graph and use it to determine A.

**Example  3**

### Identifying the Graph of a Stretched Tangent
Find a formula for the function graphed in Figure 4. x = -12 x = -4 x = 4 x = 12 x y


**Solution**

The graph has the shape of a tangent function. Step 1. One cycle extends from –4 to 4, so the period is P = 8. Since P =  \pi  ___ ∣ B ∣ , we have B =  \p\frac{i}{P}  =  \p\frac{i}{8} . Step 2. The equation must have the form f (x) = Atan (  \p\frac{i}{8} x ). Step 3. To find the vertical stretch A, we can use the point (2, 2). 2 = Atan(  \p\frac{i}{8}  \cdot  2 ) = Atan (  \p\frac{i}{4}  ) Because tan (  \p\frac{i}{4}  ) = 1, A = 2. This function would have a formula f (x) = 2tan (  \p\frac{i}{8} x ).

**Try It #3**
Find a formula for the function in Figure 5. \pi  –\pi  \pi  \pi  x = -3\pi  x = -\pi  \pi  x = 3\pi  x = x y Analyzing the Graphs of y = sec x and y = csc x The secant was defined by the reciprocal identity sec x =  1 ____ cos x . Notice that the function is undefined when the cosine is 0, leading to vertical asymptotes at  \p\frac{i}{2} ,  3\p\frac{i}{2} , etc. Because the cosine is never more than 1 in absolute value, the secant, being the reciprocal, will never be less than 1 in absolute value. We can graph y = sec x by observing the graph of the cosine function because these two functions are reciprocals of one another. See Figure 6. The graph of the cosine is shown as a blue wave so we can see the relationship. Where the graph of the cosine function decreases, the graph of the secant function increases. Where the graph of the cosine function increases, the graph of the secant function decreases. When the cosine function is zero, the secant is undefined. The secant graph has vertical asymptotes at each value of x where the cosine graph crosses the x-axis; we show these in the graph below with dashed vertical lines, but will not show all the asymptotes explicitly on all later graphs involving the secant and cosecant. Note that, because cosine is an even function, secant is also an even function. That is, sec(-x) = sec x. x y y = cos (x) y = sec (x) 2\pi  –2\pi  x = -3\pi  3\pi  x = ____ cos x  As we did for the tangent function, we will again refer to the constant ∣ A ∣ as the stretching factor, not the amplitude.

features of the graph of y = Asec(Bx) • The stretching factor is ∣ A ∣. • The period is  2\pi  ___ ∣ B ∣ . • The domain is x \neq   \pi  ____ 2∣ B ∣ k, where k is an odd integer. • The range is (-\infty , - ∣ A ∣] ∪ [∣ A ∣, \infty ). • The vertical asymptotes occur at x =  \pi  ____ 2∣ B ∣ k, where k is an odd integer. • There is no amplitude. • y = Asec(Bx) is an even function because cosine is an even function. Similar to the secant, the cosecant is defined by the reciprocal identity csc x =  1 ____ sin x . Notice that the function is undefined when the sine is 0, leading to a vertical asymptote in the graph at 0, \pi , etc. Since the sine is never more than 1 in absolute value, the cosecant, being the reciprocal, will never be less than 1 in absolute value. We can graph y = csc x by observing the graph of the sine function because these two functions are reciprocals of one another. See Figure 7. The graph of sine is shown as a blue wave so we can see the relationship. Where the graph of the sine function decreases, the graph of the cosecant function increases. Where the graph of the sine function increases, the graph of the cosecant function decreases. The cosecant graph has vertical asymptotes at each value of x where the sine graph crosses the x-axis; we show these in the graph below with dashed vertical lines. Note that, since sine is an odd function, the cosecant function is also an odd function. That is, csc(-x) = -cscx. The graph of cosecant, which is shown in Figure 7, is similar to the graph of secant. x y y = csc (x) y = sin (x) x = -2\pi  x = 2\pi  x = -\pi  x = \pi  ____ sinx  features of the graph of y = Acsc(Bx) • The stretching factor is ∣ A ∣. • The period is  2\pi  ___ ∣ B ∣ . • The domain is x \neq   \pi  ___ ∣ B ∣ k, where k is an integer. • The range is (-\infty , -∣ A ∣] ∪ [∣ A ∣, \infty ). • The asymptotes occur at x =  \pi  ___ ∣ B ∣ k, where k is an integer. • y = Acsc(Bx) is an odd function because sine is an odd function. Graphing Variations of y = sec x and y = csc x For shifted, compressed, and/or stretched versions of the secant and cosecant functions, we can follow similar methods to those we used for tangent and cotangent. That is, we locate the vertical asymptotes and also evaluate the functions for a few points (specifically the local extrema). If we want to graph only a single period, we can choose the interval for the

period in more than one way. The procedure for secant is very similar, because the cofunction identity means that the secant graph is the same as the cosecant graph shifted half a period to the left. Vertical and phase shifts may be applied to the cosecant function in the same way as for the secant and other functions. The equations become the following. y = Asec(Bx - C) + D y = Acsc(Bx - C) + D features of the graph of y = Asec(Bx - C) + D • The stretching factor is ∣ A ∣. • The period is  2\pi  ___ ∣ B ∣ . • The domain is x \neq   \frac{C}{B}  +  \pi  ____ 2∣ B ∣ k, where k is an odd integer. • The range is (-\infty , -∣ A ∣ + D] ∪ [∣ A ∣ + D, \infty ). • The vertical asymptotes occur at x =  \frac{C}{B}  +  \pi  ____ 2∣ B ∣ k, where k is an odd integer. • There is no amplitude. • y = Asec(Bx) is an even function because cosine is an even function. features of the graph of y = Acsc(Bx - C) + D • The stretching factor is ∣ A ∣. • The period is  2\pi  ___ ∣ B ∣ . • The domain is x \neq   \frac{C}{B}  +  \pi  ____ ∣ B ∣ k, where k is an integer. • The range is (-\infty , -∣ A ∣ + D] ∪ [∣ A ∣ + D, \infty ). • The vertical asymptotes occur at x =  \frac{C}{B}  +  \pi  ___ ∣ B ∣ k, where k is an integer. • There is no amplitude. • y = Acsc(Bx) is an odd function because sine is an odd function.

**How To…**
Given a function of the form y = Asec(Bx), graph one period. 1. Express the function given in the form y = Asec(Bx). 2. Identify the stretching/compressing factor, ∣ A ∣. 3. Identify B and determine the period, P =  2\pi  ___ ∣ B ∣ . 4. Sketch the graph of y = Acos(Bx). 5. Use the reciprocal relationship between y = cos x and y = sec x to draw the graph of y = Asec(Bx). 6. Sketch the asymptotes. 7. Plot any two reference points and draw the graph through these points.

**Example  4**

### Graphing a Variation of the Secant Function
Graph one period of f (x) = 2.5sec(0.4x).

**Solution**
Step 1. The given function is already written in the general form, y = Asec(Bx). Step 2. A = 2.5 so the stretching factor is 2.5. Step 3. B = 0.4 so P =  2\pi  ___ 0.4  = 5\pi . The period is 5\pi  units. Step 4. Sketch the graph of the function g(x) = 2.5cos(0.4x). Step 5. Use the reciprocal relationship of the cosine and secant functions to draw the cosecant function.

Steps 6–7. Sketch two asymptotes at x = 1.25\pi  and x = 3.75\pi . We can use two reference points, the local minimum at (0, 2.5) and the local maximum at (2.5\pi , -2.5). Figure 8 shows the graph. \pi  –\pi  3\pi  2\pi  4\pi  x y f (x) = 2.5 sec (0.4x)

**Try It #4**
Graph one period of f (x) = -2.5sec(0.4x). Do the vertical shift and stretch/compression affect the secant’s range? Yes. The range of f (x) = Asec(Bx - C) + D is (-\infty , -∣ A ∣ + D] ∪ [∣ A ∣ + D, \infty ).

**How To…**
Given a function of the form f (x) = Asec(Bx - C) + D, graph one period. 1. Express the function given in the form y = A sec(Bx - C) + D. 2. Identify the stretching/compressing factor, ∣ A ∣. 3. Identify B and determine the period,  2\pi  ___ ∣ B ∣ . 4. Identify C and determine the phase shift,  \frac{C}{B} . 5. Draw the graph of y = A sec(Bx) but shift it to the right by  \frac{C}{B}  and up by D. 6. Sketch the vertical asymptotes, which occur at x =  \frac{C}{B}  +  \pi  ____ 2∣ B ∣ k, where k is an odd integer.

**Example  5**

### Graphing a Variation of the Secant Function
Graph one period of y = 4sec (  \p\frac{i}{3} x -  \p\frac{i}{2}  ) + 1.

**Solution**
Step 1. Express the function given in the form y = 4sec (  \p\frac{i}{3} x -  \p\frac{i}{2}  ) + 1. Step 2. The stretching/compressing factor is ∣ A ∣ = 4. Step 3. The period is

 2\pi  ___ ∣ B ∣  =  2\pi  _  \p\frac{i}{3}  

=  2\pi  ___ 1  \cdot   3 __ \pi  

= 6 Step 4. The phase shift is

 \frac{C}{B}  =   \p\frac{i}{2} 

_  \p\frac{i}{3}  

=  \p\frac{i}{2}  \cdot   3 __ \pi  

= 1.5

Step 5. Draw the graph of y = Asec(Bx), but shift it to the right by  \frac{C}{B}  = 1.5 and up by D = 6. Step 6. Sketch the vertical asymptotes, which occur at x = 0, x = 3, and x = 6. There is a local minimum at (1.5, 5) and a local maximum at (4.5, -3). Figure 9 shows the graph. x = 3 x = 6 x y y = 4 sec + 1 \pi  \pi  x -

**Try It #5**
Graph one period of f (x) = -6sec(4x + 2) - 8. The domain of csc x was given to be all x such that x \neq  k\pi  for any integer k. Would the domain of y = Acsc(Bx - C) + D be x \neq   C + k\pi  ______ B ? Yes. The excluded points of the domain follow the vertical asymptotes. Their locations show the horizontal shift and compression or expansion implied by the transformation to the original function’s input.

**How To…**
Given a function of the form y = Acsc(Bx), graph one period. 1. Express the function given in the form y = Acsc(Bx). 2. Identify the stretching/compressing factor, ∣ A ∣. 3. Identify B and determine the period, P =  2\pi  ___ ∣ B ∣ . 4. Draw the graph of y = Asin(Bx). 5. Use the reciprocal relationship between y = sin x and y = csc x to draw the graph of y = Acsc(Bx). 6. Sketch the asymptotes. 7. Plot any two reference points and draw the graph through these points.

**Example  6**

### Graphing a Variation of the Cosecant Function
Graph one period of f (x) = -3csc(4x).

**Solution**
Step 1. The given function is already written in the general form, y = Acsc(Bx). Step 2. ∣ A ∣ = ∣ -3 ∣ = 3, so the stretching factor is 3. Step 3. B = 4, so P =  2\p\frac{i}{4}  =  \p\frac{i}{2} . The period is  \p\frac{i}{2}  units. Step 4. Sketch the graph of the function g(x) = -3sin(4x). Step 5. Use the reciprocal relationship of the sine and cosecant functions to draw the cosecant function. Steps 6–7. Sketch three asymptotes at x = 0, x =  \p\frac{i}{4} , and x =  \p\frac{i}{2} . We can use two reference points, the local maximum at (  \p\frac{i}{8} , -3 ) and the local minimum at (  3\p\frac{i}{8} , 3 ). Figure 10 shows the graph.

\pi  3\pi  \pi  x = \pi  x = x y f(x) = –3 csc (4x)

**Try It #6**
Graph one period of f (x) = 0.5csc(2x).

**How To…**
Given a function of the form f (x) = Acsc(Bx - C) + D, graph one period. 1. Express the function given in the form y = Acsc(Bx - C) + D. 2. Identify the stretching/compressing factor, ∣ A ∣. 3. Identify B and determine the period,  2\pi  ___ ∣ B ∣ . 4. Identify C and determine the phase shift,  \frac{C}{B} . 5. Draw the graph of y = Acsc(Bx) but shift it to the right by  \frac{C}{B}  and up by D. 6. Sketch the vertical asymptotes, which occur at x =  \frac{C}{B}  +  \pi  ___ ∣ B ∣ k, where k is an integer.

**Example  7**
Graphing a Vertically Stretched, Horizontally Compressed, and Vertically Shifted Cosecant Sketch a graph of y = 2csc (  \p\frac{i}{2} x ) + 1. What are the domain and range of this function?

**Solution**
Step 1. Express the function given in the form y = 2csc (  \p\frac{i}{2} x ) + 1. Step 2. Identify the stretching/compressing factor, ∣ A ∣ = 2. Step 3. The period is  2\pi  ___ ∣ B ∣  =  2\pi  _  \p\frac{i}{2}   =  2\p\frac{i}{1}  \cdot   2 _ \pi   = 4. Step 4. The phase shift is  0 _  \p\frac{i}{2}   = 0. Step 5. Draw the graph of y = Acsc(Bx) but shift it up D = 1. Step 6. Sketch the vertical asymptotes, which occur at x = 0, x = 2, x = 4. The graph for this function is shown in Figure 11. x y x = 4 x = 2 x = -2 x = -4 y = 2 csc + 1 \pi  x


**Analysis**
The vertical asymptotes shown on the graph mark off one period of the function, and the local extrema in this interval are shown by dots. Notice how the graph of the transformed cosecant relates to the graph of f (x) = 2sin (  \p\frac{i}{2} x ) + 1, shown as the blue wave.

**Try It #7**
Given the graph of f (x) = 2cos (  \p\frac{i}{2} x ) + 1 shown in Figure 12, sketch the graph of g(x) = 2sec (  \p\frac{i}{2} x ) + 1 on the same axes. x f (x) f (x) = 2 cos + 1 \pi  x Analyzing the Graph of y = cot x The last trigonometric function we need to explore is cotangent. The cotangent is defined by the reciprocal identity cot x =  1 ____ tan x . Notice that the function is undefined when the tangent function is 0, leading to a vertical asymptote in the graph at 0, \pi , etc. Since the output of the tangent function is all real numbers, the output of the cotangent function is also all real numbers. We can graph y = cot x by observing the graph of the tangent function because these two functions are reciprocals of one another. See Figure 13. Where the graph of the tangent function decreases, the graph of the cotangent function increases. Where the graph of the tangent function increases, the graph of the cotangent function decreases. The cotangent graph has vertical asymptotes at each value of x where tan x = 0; we show these in the graph below with dashed lines. Since the cotangent is the reciprocal of the tangent, cot x has vertical asymptotes at all values of x where tan x = 0, and cot x = 0 at all values of x where tan x has its vertical asymptotes. x y \pi  \pi  3\pi  3\pi  x = -2\pi  x = 2\pi  x = -\pi  x = \pi  f (x) = cot x features of the graph of y = Acot(Bx) • The stretching factor is ∣ A ∣. • The period is P =  \pi  ___ ∣ B ∣ . • The domain is x \neq   \pi  ___ ∣ B ∣ k, where k is an integer. • The range is (-\infty , \infty ). • The asymptotes occur at x =  \pi  ___ ∣ B ∣ k, where k is an integer. • y = Acot(Bx) is an odd function.


### Graphing Variations of y = cot x
We can transform the graph of the cotangent in much the same way as we did for the tangent. The equation becomes the following. y = Acot(Bx - C) + D features of the graph of y = Acot(Bx - C) + D • The stretching factor is ∣ A ∣. • The period is  \pi  ___ ∣ B ∣ . • The domain is x \neq   \frac{C}{B}  +  \pi  ___ ∣ B ∣ k, where k is an integer. • The range is (-\infty , \infty ). • The vertical asymptotes occur at x =  \frac{C}{B}  +  \pi  ___ ∣ B ∣ k, where k is an integer. • There is no amplitude. • y = Acot(Bx) is an odd function because it is the quotient of even and odd functions (cosine and sine, respectively)

**How To…**
Given a modified cotangent function of the form f (x) = Acot(Bx), graph one period. 1. Express the function in the form f (x) = Acot(Bx). 2. Identify the stretching factor, ∣ A ∣. 3. Identify the period, P =  \pi  ___ ∣ B ∣ . 4. Draw the graph of y = Atan(Bx). 5. Plot any two reference points. 6. Use the reciprocal relationship between tangent and cotangent to draw the graph of y = Acot(Bx). 7. Sketch the asymptotes.

**Example  8**

### Graphing Variations of the Cotangent Function
Determine the stretching factor, period, and phase shift of y = 3cot(4x), and then sketch a graph.

**Solution**
Step 1. Expressing the function in the form f (x) = Acot(Bx) gives f (x) = 3cot(4x). Step 2. The stretching factor is ∣ A ∣ = 3. Step 3. The period is P =  \p\frac{i}{4} . Step 4. Sketch the graph of y = 3tan(4x). Step 5. Plot two reference points. Two such points are (  \p\frac{i}{16} , 3 ) and (  3\p\frac{i}{S}tep 6. Use the reciprocal relationship to draw y = 3cot(4x). Step 7. Sketch the asymptotes, x = 0, x =  \p\frac{i}{4} . The blue graph in Figure 14 shows y = 3tan(4x) and the red graph shows y = 3cot(4x). y = 3 tan (4x) y = 3 cot (4x) x = -\pi  x = -\pi  \pi  x = \pi  x =


**How To…**
Given a modified cotangent function of the form f (x) = Acot(Bx - C) + D, graph one period. 1. Express the function in the form f (x) = Acot(Bx - C) + D. 2. Identify the stretching factor, ∣ A ∣. 3. Identify the period, P =  \pi  ___ ∣ B ∣ . 4. Identify the phase shift,  \frac{C}{B} . 5. Draw the graph of y = Atan(Bx) shifted to the right by  \frac{C}{B}  and up by D. 6. Sketch the asymptotes x =  \frac{C}{B}  +  \pi  ___ ∣ B ∣ k, where k is an integer. 7. Plot any three reference points and draw the graph through these points.

**Example  9**

### Graphing a Modified Cotangent
Sketch a graph of one period of the function f (x) = 4cot(  \p\frac{i}{8} x -  \p\frac{i}{2}  ) - 2.

**Solution**
Step 1. The function is already written in the general form f (x) = Acot(Bx - C) + D. Step 2. A = 4, so the stretching factor is 4. Step 3. B =  \p\frac{i}{8} , so the period is P =  \pi  ___ ∣ B ∣  =  \pi  _  \p\frac{i}{8}   = 8. Step 4. C =  \p\frac{i}{2} , so the phase shift is  \frac{C}{B} =   \p\frac{i}{2} 

_

 \p\frac{i}{8}   = 4. Step 5. We draw f (x) = 4tan(  \p\frac{i}{8} x -  \p\frac{i}{2}  ) - 2. Step 6-7. Three points we can use to guide the graph are (6, 2), (8, -2), and (10, -6). We use the reciprocal relationship of tangent and cotangent to draw f (x) = 4cot (  \p\frac{i}{8} x -  \p\frac{i}{2}  ) - 2. Step 8. The vertical asymptotes are x = 4 and x = 12. The graph is shown in Figure 15. y x = 4 x = 12 f (x) = 4 cot - 2 \pi  \pi  x - x Using the Graphs of Trigonometric Functions to Solve Real-World Problems Many real-world scenarios represent periodic functions and may be modeled by trigonometric functions. As an example, let’s return to the scenario from the section opener. Have you ever observed the beam formed by the rotating light on a police car and wondered about the movement of the light beam itself across the wall? The periodic behavior of the distance the light shines as a function of time is obvious, but how do we determine the distance? We can use the tangent function.


**Example  10**
Using Trigonometric Functions to Solve Real-World Scenarios Suppose the function y = 5tan(  \p\frac{i}{4} t ) marks the distance in the movement of a light beam from the top of a police car across a wall where t is the time in seconds and y is the distance in feet from a point on the wall directly across from the police car. a. Find and interpret the stretching factor and period. b. Graph on the interval [0, 5]. c. Evaluate f (1) and discuss the function’s value at that input.

**Solution**
a. We know from the general form of y = Atan(Bt) that ∣ A ∣ is the stretching factor and  \p\frac{i}{B}  is the period. y = 5 tan (  \p\frac{i}{4} t )

↑ ↑

A B We see that the stretching factor is 5. This means that the beam of light will have moved 5 ft after half the period. The period is  \pi  _  \p\frac{i}{4}   =  \p\frac{i}{1}  \cdot   4 __ \pi   = 4. This means that every 4 seconds, the beam of light sweeps the wall. The distance from the spot across from the police car grows larger as the police car approaches. b. To graph the function, we draw an asymptote at t = 2 and use the stretching factor and period. See Figure 17 t = 2 t y y = 5 tan \pi  t c. Period: f (1) = 5tan(  \p\frac{i}{4} (1) ) = 5(1) = 5; after 1 second, the beam of light has moved 5 ft from the spot across from the police car. Access these online resources for additional instruction and practice with graphs of other trigonometric functions. • Graphing the Tangent Function (http://openstaxcollege.org/l/graphtangent) • Graphing Cosecant and Secant Functions (http://openstaxcollege.org/l/graphcscsec) • Graphing the Cotangent Function (http://openstaxcollege.org/l/graphcot)


### 6.2 section EXERCISES
Verbal 1. Explain how the graph of the sine function can be used to graph y = csc x. 2. How can the graph of y = cos x be used to construct the graph of y = sec x? 3. Explain why the period of tan x is equal to \pi . 4. Why are there no intercepts on the graph of y = csc x? 5. How does the period of y = csc x compare with the period of y = sin x? Algebraic For the following exercises, match each trigonometric function with one of the graphs in Figure 18. x y – \pi  \pi  I II III IV x y – \pi  \pi  x y \pi  x y –\pi  2\pi  –2\pi  \pi  –\pi  –\pi  2\pi  –2\pi  x = \pi  6. f (x) = tan x 7. f (x) = sec x 8. f (x) = csc x 9. f (x) = cot x For the following exercises, find the period and horizontal shift of each of the functions. 10. f (x) = 2tan(4x - 32) 11. h(x) = 2sec(  \p\frac{i}{4} (x + 1) ) 12. m(x) = 6csc(  \p\frac{i}{3} x + \pi  ) 13. If tan x = -1.5, find tan(-x). 14. If sec x = 2, find sec(-x). 15. If csc x = -5, find csc(-x). 16. If xsin x = 2, find (-x)sin(-x). For the following exercises, rewrite each expression such that the argument x is positive. 17. cot(-x)cos(-x) + sin(-x) 18. cos(-x) + tan(-x)sin(-x) Graphical For the following exercises, sketch two periods of the graph for each of the following functions. Identify the stretching factor, period, and asymptotes. 19. f (x) = 2tan(4x - 32) 20. h(x) = 2sec(  \p\frac{i}{4} (x + 1) ) 21. m(x) = 6csc(  \p\frac{i}{3} x + \pi  ) 22. j(x) = tan(  \p\frac{i}{2} x ) 23. p(x) = tan( x -  \p\frac{i}{2}  ) 24. f (x) = 4tan(x) 25. f (x) = tan( x +  \p\frac{i}{4}  ) 26. f (x) = \pi  tan(\pi x - \pi ) - \pi  27. f (x) = 2csc(x) 28. f (x) = - \frac{1}{4} csc(x) 29. f (x) = 4sec(3x) 30. f (x) = -3cot(2x) 31. f (x) = 7sec(5x) 32. f (x) =  \frac{9}{10} csc(\pi x) 33. f (x) = 2csc ( x +  \p\frac{i}{4}  ) - 1 34. f (x) = -sec( x -  \p\frac{i}{3}  ) - 2 35. f (x) =  \frac{7}{5} csc( x -  \p\frac{i}{4}  ) 36. f (x) = 5( cot( x +  \p\frac{i}{2}  ) - 3 )


## 6.2 Section Exercises
For the following exercises, find and graph two periods of the periodic function with the given stretching factor, ∣ A ∣, period, and phase shift. 37. A tangent curve, A = 1, period of  \p\frac{i}{3} ; and phase shift (h, k) = (  \p\frac{i}{4} , 2 ) 38. A tangent curve, A = -2, period of  \p\frac{i}{4} , and phase shift (h, k) = ( - \p\frac{i}{4} , -2 ) For the following exercises, find an equation for the graph of each function. f (x) x = -\pi  x = \pi  x = -\pi  \pi  x = x x = -1 x = 1 x 0.5 f (x) x f (x) x = - x = -\pi  x = \pi  \pi  x = \pi  x f (x) 5\pi  \pi  – 3\pi  x = -5\pi  x = -\pi  3\pi  x = x f (x) x = -2\pi  x = 2\pi  x = -\pi  x = \pi  x f (x) \pi  –2\pi  –\pi  2\pi  x f (x) -0.01 0.01 Technology For the following exercises, use a graphing calculator to graph two periods of the given function. Note: most graphing calculators do not have a cosecant button; therefore, you will need to input csc x as  1 ____ sin x . 46. f (x) = |csc(x)| 47. f (x) = |cot(x)| 48. f (x) = 2csc(x) 49. f (x) =  csc(x) _____ sec(x)  50. Graph f (x) = 1 + sec^{2} (x) - tan^{2} (x). What is the function shown in the graph? 51. f (x) = sec(0.001x) 52. f (x) = cot(100\pi x) 53. f (x) = sin^{2} x + cos^{2} x

Real-World Applications 54. The function f (x) = 20tan (  \p\frac{i}{10} x ) marks the distance in the movement of a light beam from a police car across a wall for time x, in seconds, and distance f (x), in feet. a. Graph on the interval [0, 5]. b. Find and interpret the stretching factor, period, and asymptote. c. Evaluate f (1) and f (2.5) and discuss the function’s values at those inputs. 55. Standing on the shore of a lake, a fisherman sights a boat far in the distance to his left. Let x, measured in radians, be the angle formed by the line of sight to the ship and a line due north from his position. Assume due north is 0 and x is measured negative to the left and positive to the right. (See Figure 19.) The boat travels from due west to due east and, ignoring the curvature of the Earth, the distance d(x), in kilometers, from the fisherman to the boat is given by the function d(x) = 1.5sec(x). a. What is a reasonable domain for d(x)? b. Graph d(x) on this domain. c. Find and discuss the meaning of any vertical asymptotes on the graph of d(x). d. Calculate and interpret d ( - \p\frac{i}{3}  ). Round to the second decimal place. e. Calculate and interpret d (  \p\frac{i}{6}  ). Round to the second decimal place. f. What is the minimum distance between the fisherman and the boat? When does this occur? 56. A laser rangefinder is locked on a comet approaching Earth. The distance g(x), in kilometers, of the comet after x days, for x in the interval 0 to 30 days, is given by g(x) = 250,000csc (  \p\frac{i}{30} x ). a. Graph g(x) on the interval [0, 35]. b. Evaluate g(5) and interpret the information. c. What is the minimum distance between the comet and Earth? When does this occur? To which constant in the equation does this correspond? d. Find and discuss the meaning of any vertical asymptotes. 57. A video camera is focused on a rocket on a launching pad 2 miles from the camera. The angle of elevation from the ground to the rocket after x seconds is  \pi  ___ a. Write a function expressing the altitude h(x), in miles, of the rocket above the ground after x seconds. Ignore the curvature of the Earth. b. Graph h(x) on the interval (0, 60). c. Evaluate and interpret the values h(0) and h(30). d. What happens to the values of h(x) as x approaches 60 seconds? Interpret the meaning of this in terms of the problem.


## 6.3 Inverse Trigonometric Functions
Learning Objectives
In this section, you will:
• Understand and use the inverse sine, cosine, and tangent functions.
• Find the exact value of expressions involving the inverse sine, cosine, and tangent functions.
• Use a calculator to evaluate inverse trigonometric functions.
• Find exact values of composite functions with inverse trigonometric functions.
For any right triangle, given one other angle and the length of one side, we can figure out what the other angles and sides are. But what if we are given only two sides of a right triangle? We need a procedure that leads us from a ratio of sides to an angle. This is where the notion of an inverse to a trigonometric function comes into play. In this section, we will explore the inverse trigonometric functions. Understanding and Using the Inverse Sine, Cosine, and Tangent Functions In order to use inverse trigonometric functions, we need to understand that an inverse trigonometric function “undoes” what the original trigonometric function “does,” as is the case with any other function and its inverse. In other words, the domain of the inverse function is the range of the original function, and vice versa, as summarized in Figure 1.

Trig Functions Inverse Trig Functions

Domain: Measure of an angle Domain: Ratio

Range: Ratio Range: Measure of an angle For example, if f (x) = sin x, then we would write f -1(x) = sin-1 x. Be aware that sin-1 x does not mean  1 ___ sinx . The following examples illustrate the inverse trigonometric functions: • Since sin (  \p\frac{i}{6}  ) =  \frac{1}{2} , then  \p\frac{i}{6}  = sin-1 (  \frac{1}{2}  ). • Since cos(\pi ) = -1, then \pi  = cos-1(-1). • Since tan (  \p\frac{i}{4}  ) = 1, then  \p\frac{i}{4}  = tan-1(1). In previous sections, we evaluated the trigonometric functions at various angles, but at times we need to know what angle would yield a specific sine, cosine, or tangent value. For this, we need inverse functions. Recall that, for a one- to-one function, if f(a) = b, then an inverse function would satisfy f -1(b) = a. Bear in mind that the sine, cosine, and tangent functions are not one-to-one functions. The graph of each function would fail the horizontal line test. In fact, no periodic function can be one-to-one because each output in its range corresponds to at least one input in every period, and there are an infinite number of periods. As with other functions that are not one-to-one, we will need to restrict the domain of each function to yield a new function that is one-to- one. We choose a domain for each function that includes the number 0. Figure 2 shows the graph of the sine function limited to [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ]  and the graph of the cosine function limited to [0, \pi ]. x y \pi  \pi  – \pi  – \pi  f(x) = sin x

x y \pi  \pi  \pi  3\pi  f (x) = cos \frac{x}{2} ,  \p\frac{i}{2}  ] ; (b) Cosine function on a restricted domain of [0, \pi ] (a) (b)

__ 2 ,  \p\frac{i}{2}  ). x y \pi  \pi  \pi  f (x) = tan x x = - \pi  x = __ 2 ,  \p\frac{i}{2}  ) These conventional choices for the restricted domain are somewhat arbitrary, but they have important, helpful characteristics. Each domain includes the origin and some positive values, and most importantly, each results in a one-to-one function that is invertible. The conventional choice for the restricted domain of the tangent function also has the useful property that it extends from one vertical asymptote to the next instead of being divided into two parts by an asymptote. On these restricted domains, we can define the inverse trigonometric functions. • The inverse sine function y = sin-1 x means x = sin y. The inverse sine function is sometimes called the arcsine function, and notated arcsinx. y = sin-1 x has domain [-1, 1] and range [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ]  • The inverse cosine function y = cos-1 x means x = cos y. The inverse cosine function is sometimes called the arccosine function, and notated arccos x.

y = cos-1 x has domain [-1, 1] and range [0, \pi ] • The inverse tangent function y = tan-1 x means x = tan y. The inverse tangent function is sometimes called the arctangent function, and notated arctan x.

y = tan-1 x has domain (-\infty , \infty ) and range ( - \p\frac{i}{2} ,  \p\frac{i}{2}  ) The graphs of the inverse functions are shown in Figure 4, Figure 5, and Figure 6. Notice that the output of each of these inverse functions is a number, an angle in radian measure. We see that sin-1 x has domain [-1, 1] and range [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] , cos-1 x has domain [-1, 1] and range [0, \pi ], and tan-1 x has domain of all real numbers and range ( - \p\frac{i}{2} ,  \p\frac{i}{2}  ). To find the domain and range of inverse trigonometric functions, switch the domain and range of the original functions. Each graph of the inverse trigonometric function is a reflection of the graph of the original function about the line y = x. – \pi  – \pi  – \pi  – \pi  \pi  \pi  \pi  \pi  y = sin (x) y = x y = sin–1 (x) x y

y = cos (x) y = x y = cos–1 (x) \pi  \pi  \pi  \pi  – \pi  – \pi  x y y = tan (x) y = x y = tan–1 (x) – \pi  – \pi  – \pi  – \pi  \pi  \pi  \pi  \pi  x y relations for inverse sine, cosine, and tangent functions For angles in the interval [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] , if sin y = x, then sin-1 x = y. For angles in the interval [0, \pi ], if cos y = x, then cos-1 x = y. For angles in the interval ( - \p\frac{i}{2} ,  \p\frac{i}{2}  ), if tan y = x, then tan-1 x = y.

**Example  1**

### Writing a Relation for an Inverse Function
Given sin (  5\p\frac{i}{12}  ) ≈ 0.96593, write a relation involving the inverse sine.

**Solution**

Use the relation for the inverse sine. If sin y = x, then sin-1 x = y. In this problem, x = 0.96593, and y =  5\p\frac{i}{12} . ___ 12 

**Try It #1**
Given cos(0.5) ≈ 0.8776, write a relation involving the inverse cosine. Finding the Exact Value of Expressions Involving the Inverse Sine, Cosine, and Tangent Functions Now that we can identify inverse functions, we will learn to evaluate them. For most values in their domains, we must evaluate the inverse trigonometric functions by using a calculator, interpolating from a table, or using some other numerical technique. Just as we did with the original trigonometric functions, we can give exact values for the inverse functions when we are using the special angles, specifically  \p\frac{i}{6}  (30°),  \p\frac{i}{4}  (45°), and  \p\frac{i}{3} (60°), and their reflections into other quadrants.

**How To…**
Given a “special” input value, evaluate an inverse trigonometric function. 1. Find angle x for which the original trigonometric function has an output equal to the given input for the inverse trigonometric function. 2. If x is not in the defined range of the inverse, find another angle y that is in the defined range and has the same sine, cosine, or tangent as x, depending on which corresponds to the given inverse function.

**Example  2**

### Evaluating Inverse Trigonometric Functions for Special Input Values
Evaluate each of the following.

a. sin-1(  \frac{1}{2}  ) b. sin-1( -  \sqrt{2}  ____ 2  ) c. cos-1( - \sqrt{3}  ____ 2  ) d. tan-1(1)


**Solution**

a. Evaluating sin-1(  \frac{1}{2}  ) is the same as determining the angle that would have a sine value of  \frac{1}{2} . In other words, what angle x would satisfy sin(x) =  \frac{1}{2} ? There are multiple values that would satisfy this relationship, such as  \p\frac{i}{6}  and  5\p\frac{i}{6} , but we know we need the angle in the interval [ -  \p\frac{i}{2} ,  \p\frac{i}{2}  ] , so the answer will be sin-1(  \frac{1}{2}  ) =  \p\frac{i}{6} . Remember that the inverse is a function, so for each input, we will get exactly one output.

b. To evaluate sin-1( -  \sqrt{2}  _ 2  ), we know that  5\p\frac{i}{4}  and  7\p\frac{i}{4}  both have a sine value of -  \sqrt{2}  _ 2 , but neither is in the interval [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] . For that, we need the negative angle coterminal with  7\pi  ___ 4 : sin-1( -  \sqrt{2}  ____ 2  ) = - \p\frac{i}{4} .

c. To evaluate cos-1( -  \sqrt{3}  _ 2  ), we are looking for an angle in the interval [0, \pi ] with a cosine value of -  \sqrt{3}  _ 2 . The angle that satisfies this is cos-1( -  \sqrt{3}  _ 2  ) =  5\p\frac{i}{6} .

d. Evaluating tan-1(1), we are looking for an angle in the interval ( - \p\frac{i}{2} ,  \p\frac{i}{2}  ) with a tangent value of 1. The correct angle is tan-1(1) =  \p\frac{i}{4} .

**Try It #2**
Evaluate each of the following. a. sin-1(-1) b. tan-1 (-1) c. cos-1 (-1) d. cos-1 (  \frac{1}{2}  ) Using a Calculator to Evaluate Inverse Trigonometric Functions To evaluate inverse trigonometric functions that do not involve the special angles discussed previously, we will need to use a calculator or other type of technology. Most scientific calculators and calculator-emulating applications have specific keys or buttons for the inverse sine, cosine, and tangent functions. These may be labeled, for example, SIN-1, ARCSIN, or ASIN. In the previous chapter, we worked with trigonometry on a right triangle to solve for the sides of a triangle given one side and an additional angle. Using the inverse trigonometric functions, we can solve for the angles of a right triangle given two sides, and we can use a calculator to find the values to several decimal places. In these examples and exercises, the answers will be interpreted as angles and we will use \theta  as the independent variable. The value displayed on the calculator may be in degrees or radians, so be sure to set the mode appropriate to the application.

**Example  3**

### Evaluating the Inverse Sine on a Calculator
Evaluate sin-1(0.97) using a calculator.

**Solution**

Because the output of the inverse function is an angle, the calculator will give us a degree value if in degree mode and a radian value if in radian mode. Calculators also use the same domain restrictions on the angles as we are using. In radian mode, sin-1(0.97) ≈ 1.3252. In degree mode, sin-1(0.97) ≈ 75.93°. Note that in calculus and beyond we will use radians in almost all cases.

**Try It #3**
Evaluate cos-1 (-0.4) using a calculator.


**How To…**
Given two sides of a right triangle like the one shown in Figure 7, find an angle. p h a \theta  1. If one given side is the hypotenuse of length h and the side of length a adjacent to the desired angle is given, use the equation \theta  = cos-1(  \frac{a}{h}  ). 2. If one given side is the hypotenuse of length h and the side of length p opposite to the desired angle is given, use the equation \theta  = sin-1(  \frac{p}{h}  ) 3. If the two legs (the sides adjacent to the right angle) are given, then use the equation \theta  = tan-1(  \frac{p}{a}  ).

**Example  4**

### Applying the Inverse Cosine to a Right Triangle
Solve the triangle in Figure 8 for the angle \theta . \theta

**Solution**

Because we know the hypotenuse and the side adjacent to the angle, it makes sense for us to use the cosine function.

cos \theta  =  \frac{9}{12} 

\theta  = cos-1(  \frac{9}{12}  ) Apply definition of the inverse.

Evaluate.

**Try It #4**
Solve the triangle in Figure 9 for the angle \theta . \theta 

Finding Exact Values of Composite Functions with Inverse Trigonometric Functions There are times when we need to compose a trigonometric function with an inverse trigonometric function. In these cases, we can usually find exact values for the resulting expressions without resorting to a calculator. Even when the input to the composite function is a variable or an expression, we can often find an expression for the output. To help sort out different cases, let f (x) and g(x) be two different trigonometric functions belonging to the set {sin(x), cos(x), tan(x)} and let f -1(y) and g -1(y) be their inverses. Evaluating Compositions of the Form f (f -1(y )) and f -1(f (x )) For any trigonometric function, f (f -1 (y)) = y for all y in the proper domain for the given function. This follows from the definition of the inverse and from the fact that the range of f was defined to be identical to the domain of f -1. However, we have to be a little more careful with expressions of the form f -1(f (x)). compositions of a trigonometric function and its inverse sin(sin-1 x) = x for -1 \le  x \le  1 cos(cos-1 x) = x for -1 \le  x \le  1 tan(tan-1 x) = x for -\infty  < x < \infty  sin-1(sin x) = x only for - \p\frac{i}{2}  \le  x \le   \p\frac{i}{2}  cos-1(cos x) = x only for 0 \le  x \le  \pi  tan-1(tan x) = x only for - \p\frac{i}{2}  < x <  \p\frac{i}{2}  Is it correct that sin-1(sin x) = x? No. This equation is correct if x belongs to the restricted domain [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] , but sine is defined for all real input values, and for x outside the restricted interval, the equation is not correct because its inverse always returns a value in [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] . The situation is similar for cosine and tangent and their inverses. For example, sin-1( sin (  3\p\frac{i}{4}  ) ) =  \p\frac{i}{4} .

**How To…**
Given an expression of the form f -1(f(\theta )) where f(\theta ) = sin \theta , cos \theta , or tan \theta , evaluate. 1. If \theta  is in the restricted domain of f , then f -1(f(\theta )) = \theta . 2. If not, then find an angle \phi  within the restricted domain of f such that f(\phi ) = f(\theta ). Then f -1(f(\theta )) = \phi .

**Example  5**
Using Inverse Trigonometric Functions Evaluate the following: a. sin-1( sin (  \p\frac{i}{3}  ) ) b. sin-1( sin (  2\pi  ___ 3  ) ) c. cos-1( cos (  2\pi  ___ 3  ) ) d. cos-1( cos ( - \p\frac{i}{3}  ) )

**Solution**

a.  \p\frac{i}{3}  is in [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] , so sin-1( sin (  \p\frac{i}{3}  ) ) =  \p\frac{i}{3} .

b.  2\pi  ___ 3  is not in [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] , but sin (  2\pi  ___ 3  ) = sin (  \p\frac{i}{3}  ), so sin-1( sin (  2\pi  ___ 3  ) ) =  \p\frac{i}{3} .

c.  2\pi  ___ 3  is in [0, \pi ], so cos-1( cos (  2\pi  ___ 3  ) ) =  2\pi  ___ 3 .

d. - \p\frac{i}{3}  is not in [0, \pi ], but cos ( - \p\frac{i}{3}  ) = cos(  \p\frac{i}{3}  ) because cosine is an even function.  \p\frac{i}{3}  is in [0, \pi ], so cos-1( cos  ( - \p\frac{i}{3}  ) ) =  \p\frac{i}{3} .


**Try It #5**
Evaluate tan-1 ( tan (  \p\frac{i}{8}  ) ) and tan-1 ( tan (  11\pi  ___ 9  ) ). Evaluating Compositions of the Form f -1(g(x )) Now that we can compose a trigonometric function with its inverse, we can explore how to evaluate a composition of a trigonometric function and the inverse of another trigonometric function. We will begin with compositions of the form f-1(g(x)). For special values of x, we can exactly evaluate the inner function and then the outer, inverse function. However, we can find a more general approach by considering the relation between the two acute angles of a right triangle where one is \theta , making the other  \p\frac{i}{2}  - \theta . Consider the sine and cosine of each angle of the right triangle in a c b \theta  \theta  \pi  – Because cos \theta  =  \frac{b}{c}  = sin (  \p\frac{i}{2}  - \theta  ), we have sin-1 (cos \theta ) =  \p\frac{i}{2}  - \theta  if 0 \le  \theta  \le  \pi . If \theta  is not in this domain, then we need to find another angle that has the same cosine as \theta  and does belong to the restricted domain; we then subtract this angle from  \p\frac{i}{2} . Similarly, sin \theta  =  \frac{a}{c}  = cos (  \p\frac{i}{2}  - \theta  ), so cos-1 (sin \theta ) =  \p\frac{i}{2}  - \theta  if - \p\frac{i}{2}  \le  \theta  \le   \p\frac{i}{2} . These are just the function-cofunction relationships presented in another way.

**How To…**
Given functions of the form sin-1 (cos x) and cos-1 (sin x), evaluate them. 1. If x is in [0, \pi ], then sin-1 (cos x) =  \p\frac{i}{2}  - x. 2. If x is not in [0, \pi ], then find another angle y in [0, \pi ] such that cos y = cos x. sin-1 (cos x) =  \p\frac{i}{2}  - y 3. If x is in [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] , then cos-1 (sin x) =  \p\frac{i}{2}  - x. 4. If x is not in [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] , then find another angle y in [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ]  such that sin y = sin x. cos-1 (sin x) =  \p\frac{i}{2}  - y

**Example  6**

### Evaluating the Composition of an Inverse Sine with a Cosine
Evaluate sin-1( cos (  13\pi  ___ 6  ) ) a. by direct evaluation. b. by the method described previously.

**Solution**

a. Here, we can directly evaluate the inside of the composition.

cos (  13\pi  ___ 6  ) = cos (  \p\frac{i}{6}  + 2\pi  )

= cos (  \p\frac{i}{6}  )

=  \sqrt{3}  ____ 2 

Now, we can evaluate the inverse function as we did earlier.

sin-1(  \sqrt{3}  ____ 2  ) =  \p\frac{i}{3} 

b. We have x =  13\p\frac{i}{6} , y =  \p\frac{i}{6} , and

sin-1 ( cos(  13\pi  ___ 6  ) ) =  \p\frac{i}{2}  -  \p\frac{i}{6} 

=  \p\frac{i}{3} 

**Try It #6**
Evaluate cos-1( sin ( - 11\pi  ___ 4  ) ). Evaluating Compositions of the Form f (g -1(x )) To evaluate compositions of the form f (g -1(x)), where f and g are any two of the functions sine, cosine, or tangent and x is any input in the domain of g -1, we have exact formulas, such as sin(cos-1 x) = \sqrt{1} - x^{2} . When we need to use them, we can derive these formulas by using the trigonometric relations between the angles and sides of a right triangle, together with the use of Pythagorean’s relation between the lengths of the sides. We can use the Pythagorean identity, sin^{2} x + cos^{2} x = 1, to solve for one when given the other. We can also use the inverse trigonometric functions to find compositions involving algebraic expressions.

**Example  7**

### Evaluating the Composition of a Sine with an Inverse Cosine
Find an exact value for sin ( cos-1(  \frac{4}{5}  ) ).

**Solution**

Beginning with the inside, we can say there is some angle such that \theta  = cos-1(  \frac{4}{5}  ), which means cos \theta  =  \frac{4}{5} , and we are looking for sin \theta . We can use the Pythagorean identity to do this.

sin^{2} \theta  + cos^{2} \theta  = 1 Use our known value for cosine.

sin^{2} \theta  + (  \frac{4}{5}  ) = 1 Solve for sine.

sin^{2} \theta  = 1 -  \frac{16}{25} 

sin \theta  = \pm  \sqrt{___}

 \frac{9}{25}   = \pm  \frac{3}{5}  Since \theta  = cos-1(  \frac{4}{5}  ) is in quadrant I, sin \theta  must be positive, so the solution is  \frac{3}{5} . See Figure 11. \thet\frac{a}{5} , then sin \theta  =  \frac{3}{5}  We know that the inverse cosine always gives an angle on the interval [0, \pi ], so we know that the sine of that angle must be positive; therefore sin ( cos-1(  \frac{4}{5}  ) ) = sin \theta  =  \frac{3}{5} .

**Try It #7**
Evaluate cos ( tan-1(  \frac{5}{12}  ) ).


**Example  8**

### Evaluating the Composition of a Sine with an Inverse Tangent
Find an exact value for sin ( tan-1(  \frac{7}{4}  ) ).

**Solution**

While we could use a similar technique as in Example 6, we will demonstrate a different technique here. From the inside, we know there is an angle such that tan \theta  =  \frac{7}{4} . We can envision this as the opposite and adjacent sides on a right triangle, as shown in Figure 12. \theta  Using the Pythagorean Theorem, we can find the hypotenuse of this triangle.

42 + 72 = hypotenuse 2

hypotenuse = \sqrt{65}  Now, we can evaluate the sine of the angle as the opposite side divided by the hypotenuse.

sin \theta  =  7 _ \sqrt{65}   This gives us our desired composition.

sin ( tan-1 (  \frac{7}{4}  ) ) = sin \theta 

=  7 _ \sqrt{65}  

=  7 \sqrt{65}  ______ 

**Try It #8**
Evaluate cos ( sin-1(  \frac{7}{9}  ) ).

**Example  9** — Finding the Cosine of the Inverse Sine of an Algebraic Expression
Find a simplified expression for cos ( sin-1(  \frac{x}{3}  ) ) for -3 \le  x \le  3.

**Solution**
We know there is an angle \theta  such that sin \theta  =  \frac{x}{3} .

sin^{2} \theta  + cos^{2} \theta  = 1 Use the Pythagorean Theorem.

(  \frac{x}{3}  ) 2 + cos^{2} \theta  = 1 Solve for cosine.

cos^{2} \theta  = 1 -  x^{2}

_ 9 

cos \theta  = \pm  \sqrt{______}

 9 - x^{2} ______   = \pm   \sqrt{9} - x^{2}  _______  Because we know that the inverse sine must give an angle on the interval [ - \p\frac{i}{2} ,  \p\frac{i}{2}  ] , we can deduce that the cosine of that angle must be positive.

cos ( sin-1(  \frac{x}{3}  ) ) =  \sqrt{9} - x^{2}  _______ 

**Try It #9**
Find a simplified expression for sin(tan-1 (4x)) for - \frac{1}{4}  \le  x \le   \frac{1}{4} . > Access this online resource for additional instruction and practice with inverse trigonometric functions. • Evaluate Expressions Involving Inverse Trigonometric Functions (http://openstaxcollege.org/l/evalinverstrig)

6.3 SECTION EXERCISES Verbal 1. Why do the functions f (x) = sin-1 x and g(x) = cos-1 x have different ranges? 2. Since the functions y = cos x and y = cos-1 x are inverse functions, why is cos-1( cos ( - \pi  ___ 6  ) ) not equal to -  \p\frac{i}{6} ? 3. Explain the meaning of  \p\frac{i}{6}  = arcsin(0.5). 4. Most calculators do not have a key to evaluate sec-1(2). Explain how this can be done using the cosine function or the inverse cosine function. 5. Why must the domain of the sine function, sin x, be restricted to [ - \pi  ___ 2 ,  \p\frac{i}{2}  ]  for the inverse sine function to exist? 6. Discuss why this statement is incorrect: arccos (cos x) = x for all x. 7. Determine whether the following statement is true or false and explain your answer: arccos(-x) = \pi  - arccos x. Algebraic For the following exercises, evaluate the expressions. 8. sin-1(  \sqrt{2}  ____ 2  ) 9. sin-1( - \frac{1}{2}  ) 10. cos-1(  \frac{1}{2}  ) 11. cos-1( - \sqrt{2}  ____ 2  ) 13. tan-1( -\sqrt{3}  ) 14. tan-1 (-1) 15. tan-1( \sqrt{3}  ) 16. tan-1(  -1 _ \sqrt{3}   ) For the following exercises, use a calculator to evaluate each expression. Express answers to the nearest hundredth. 19. arccos (  \frac{3}{5}  ) For the following exercises, find the angle \theta  in the given right triangle. Round answers to the nearest hundredth. \theta  \theta  For the following exercises, find the exact value, if possible, without a calculator. If it is not possible, explain why. 24. sin-1(cos(\pi )) 25. tan-1(sin(\pi )) 26. cos-1 ( sin(  \p\frac{i}{3}  ) ) 27. tan-1 ( sin(  \p\frac{i}{3}  ) ) 28. sin-1 ( cos(  -\p\frac{i}{2}  ) ) 29. tan-1 ( sin(  4\p\frac{i}{3}  ) ) 30. sin-1 ( sin(  5\p\frac{i}{6}  ) ) 31. tan-1 ( sin(  -5\p\frac{i}{2}  ) ) 32. cos ( sin-1(  \frac{4}{5}  ) ) 33. sin ( cos-1(  \frac{3}{5}  ) ) 34. sin ( tan-1(  \frac{4}{3}  ) ) 35. cos ( tan-1(  \frac{12}{5}  ) ) 36. cos ( sin-1(  \frac{1}{2}  ) )


## 6.3 Section Exercises
For the following exercises, find the exact value of the expression in terms of x with the help of a reference triangle. 37. tan(sin-1 (x - 1)) 38. sin(cos-1 (1 - x)) 39. cos ( sin-1(  \frac{1}{x}  ) ) 40. cos(tan-1 (3x - 1)) 41. tan ( sin-1( x +  \frac{1}{2}  ) ) Extensions For the following exercise, evaluate the expression without using a calculator. Give the exact value. 42. sin-1(  \frac{1}{2}  ) - cos-1(  \sqrt{2}  ___ 2  ) + sin-1(  \sqrt{3}  _ 2  ) - cos-1(1) cos-1(  \sqrt{3}  _ 2  ) - sin-1(  \sqrt{2}  ___ 2  ) + cos-1(  \frac{1}{2}  ) - sin-1(0) For the following exercises, find the function if sin t =  x ____ x + 1 . 43. cos t 44. sec t 45. cot t 46. cos ( sin-1(  x ____ x + 1  ) ) 47. tan-1(  x _ \sqrt{2x} + 1   ) Graphical 48. Graph y = sin-1 x and state the domain and range of the function. 49. Graph y = arccos x and state the domain and range of the function. 50. Graph one cycle of y = tan-1 x and state the domain and range of the function. 51. For what value of x does sin x = sin-1 x? Use a graphing calculator to approximate the answer. 52. For what value of x does cos x = cos-1 x? Use a graphing calculator to approximate the answer. Real-World Applications 53. Suppose a 13-foot ladder is leaning against a building, reaching to the bottom of a second-floor window 12 feet above the ground. What angle, in radians, does the ladder make with the building? 54. Suppose you drive 0.6 miles on a road so that the vertical distance changes from 0 to 150 feet. What is the angle of elevation of the road? 55. An isosceles triangle has two congruent sides of length 9 inches. The remaining side has a length of 8 inches. Find the angle that a side of 9 inches makes with the 8-inch side. 56. Without using a calculator, approximate the value of arctan(10,000). Explain why your answer is reasonable. 57. A truss for the roof of a house is constructed from two identical right triangles. Each has a base of 12 feet and height of 4 feet. Find the measure of the acute angle adjacent to the 4-foot side. 58. The line y =  \frac{3}{5} x passes through the origin in the x,y- plane. What is the measure of the angle that the line makes with the positive x-axis? 59. The line y = - \frac{3}{7}  x passes through the origin in the x,y-plane. What is the measure of the angle that the line makes with the negative x-axis? 60. What percentage grade should a road have if the angle of elevation of the road is 4 degrees? (The percentage grade is defined as the change in the altitude of the road over a 100-foot horizontal distance. For example a 5% grade means that the road rises 5 feet for every 100 feet of horizontal distance.) 61. A 20-foot ladder leans up against the side of a building so that the foot of the ladder is 10 feet from the base of the building. If specifications call for the ladder’s angle of elevation to be between 35 and 45 degrees, does the placement of this ladder satisfy safety specifications? 62. Suppose a 15-foot ladder leans against the side of a house so that the angle of elevation of the ladder is 42 degrees. How far is the foot of the ladder from the side of the house?


### Key Terms
amplitude the vertical height of a function; the constant A appearing in the definition of a sinusoidal function arccosine another name for the inverse cosine; arccos x = cos-1 x arcsine another name for the inverse sine; arcsin x = sin-1 x arctangent another name for the inverse tangent; arctan x = tan-1 x inverse cosine function the function cos-1 x, which is the inverse of the cosine function and the angle that has a cosine equal to a given number inverse sine function the function sin-1 x, which is the inverse of the sine function and the angle that has a sine equal to a given number inverse tangent function the function tan-1 x, which is the inverse of the tangent function and the angle that has a tangent equal to a given number midline the horizontal line y = D, where D appears in the general form of a sinusoidal function periodic function a function f (x) that satisfies f (x + P) = f (x) for a specific constant P and any value of x phase shift the horizontal displacement of the basic sine or cosine function; the constant  \frac{C}{B}  sinusoidal function any function that can be expressed in the form f (x) = Asin(Bx - C) + D or f (x) = Acos(Bx - C) + D key equations Sinusoidal functions f (x) = Asin(Bx - C) + D

f (x) = Acos(Bx - C) + D Shifted, compressed, and/or stretched tangent function y = A tan(Bx - C) + D Shifted, compressed, and/or stretched secant function y = A sec(Bx - C) + D Shifted, compressed, and/or stretched cosecant function y = A csc(Bx - C) + D Shifted, compressed, and/or stretched cotangent function y = A cot(Bx - C) + D

### Key Concepts
• Periodic functions repeat after a given value. The smallest such value is the period. The basic sine and cosine functions have a period of 2\pi . • The function sin x is odd, so its graph is symmetric about the origin. The function cos x is even, so its graph is symmetric about the y-axis. • The graph of a sinusoidal function has the same general shape as a sine or cosine function. • In the general formula for a sinusoidal function, the period is P =  2\pi  _ ∣B∣  See Example 1. • In the general formula for a sinusoidal function, ∣A∣ represents amplitude. If ∣A∣ > 1, the function is stretched, whereas if ∣A∣ < 1, the function is compressed. See Example 2. • The value  \frac{C}{B}  in the general formula for a sinusoidal function indicates the phase shift. See Example 3. • The value D in the general formula for a sinusoidal function indicates the vertical shift from the midline. See Example 4. • Combinations of variations of sinusoidal functions can be detected from an equation. See Example 5. • The equation for a sinusoidal function can be determined from a graph. See Example 6 and Example 7. • A function can be graphed by identifying its amplitude and period. See Example 8 and Example 9. • A function can also be graphed by identifying its amplitude, period, phase shift, and horizontal shift. See Example 10. • Sinusoidal functions can be used to solve real-world problems. See Example 11, Example 12, and Example 13.

• The tangent function has period \pi . • f (x) = Atan(Bx - C) + D is a tangent with vertical and/or horizontal stretch/compression and shift. See Example 1,

**Example 2** — , and Example 3.
• The secant and cosecant are both periodic functions with a period of 2\pi . f (x) = Asec(Bx - C) + D gives a shifted, compressed, and/or stretched secant function graph. See Example 4 and Example 5. • f (x) = Acsc(Bx - C) + D gives a shifted, compressed, and/or stretched cosecant function graph. See Example 6 and

**Example 7** — .
• The cotangent function has period \pi  and vertical asymptotes at 0, \pm \pi , \pm 2\pi , ... • The range of cotangent is (-\infty , \infty ), and the function is decreasing at each point in its range. • The cotangent is zero at \pm  \p\frac{i}{2} , \pm  3\pi  __ • f (x) = Acot(Bx - C) + D is a cotangent with vertical and/or horizontal stretch/compression and shift. See Example 8 and Example 9. • Real-world scenarios can be solved using graphs of trigonometric functions. See Example 10. 6.3 Inverse Trigonometric Functions • An inverse function is one that “undoes” another function. The domain of an inverse function is the range of the original function and the range of an inverse function is the domain of the original function. • Because the trigonometric functions are not one-to-one on their natural domains, inverse trigonometric functions are defined for restricted domains. • For any trigonometric function f (x), if x = f-1(y), then f (x) = y. However, f (x) = y only implies x = f-1(y) if x is in the restricted domain of f . See Example 1. • Special angles are the outputs of inverse trigonometric functions for special input values; for example,  \p\frac{i}{4}  = tan-1(1) and  \p\frac{i}{6}  = sin-1(  \frac{1}{2}  ). See Example 2. • A calculator will return an angle within the restricted domain of the original trigonometric function. See Example 3. • Inverse functions allow us to find an angle when given two sides of a right triangle. See Example 4. • In function composition, if the inside function is an inverse trigonometric function, then there are exact expressions; for example, sin(cos-1 (x)) = \sqrt{1} - x^{2} . See Example 5. • If the inside function is a trigonometric function, then the only possible combinations are sin-1 (cos x) =  \p\frac{i}{2}  - x if 0 \le  x \le  \pi  and cos-1 (sin x) =  \p\frac{i}{2}  - x if -  \p\frac{i}{2}  \le  x \le   \p\frac{i}{2} . See Example 6 and Example 7. • When evaluating the composition of a trigonometric function with an inverse trigonometric function, draw a reference triangle to assist in determining the ratio of sides that represents the output of the trigonometric function. See Example 8. • When evaluating the composition of a trigonometric function with an inverse trigonometric function, you may use trig identities to assist in determining the ratio of sides. See Example 9.

Graphs of the Sine and Cosine Functions For the following exercises, graph the functions for two periods and determine the amplitude or stretching factor, period, midline equation, and asymptotes. 1. f (x) = -3cos x + 3 2. f (x) =  \frac{1}{4} sin x 3. f (x) = 3cos ( x +  \p\frac{i}{6}  ) 4. f (x) = -2sin ( x -  2\p\frac{i}{3}  ) 5. f (x) = 3sin ( x -  \p\frac{i}{4}  ) - 4 6. f (x) = 2( cos( x -  4\p\frac{i}{3}  ) + 1 ) 7. f (x) = 6sin ( 3x -  \p\frac{i}{6}  ) - 1 8. f (x) = -100sin(50x - 20) Graphs of the Other Trigonometric Functions For the following exercises, graph the functions for two periods and determine the amplitude or stretching factor, period, midline equation, and asymptotes. 9. f (x) = tan x - 4 10. f (x) = 2tan( x -  \p\frac{i}{6}  ) 11. f (x) = -3tan(4x) - 2 For the following exercises, graph two full periods. Identify the period, the phase shift, the amplitude, and asymptotes. 13. f (x) =  \frac{1}{3} sec x 14. f (x) = 3cot x 15. f (x) = 4csc(5x) 16. f (x) = 8sec (  \frac{1}{4} x ) 17. f (x) =  \frac{2}{3} csc (  \frac{1}{2} x ) 18. f (x) = -csc(2x + \pi ) For the following exercises, use this scenario: The population of a city has risen and fallen over a 20-year interval. Its population may be modeled by the following function: y = 12,000 + 8,000sin(0.628x), where the domain is the years since 1980 and the range is the population of the city. 19. What is the largest and smallest population the city may have? 20. Graph the function on the domain of [0, 40]. 21. What are the amplitude, period, and phase shift for the function? 22. Over this domain, when does the population reach 23. What is the predicted population in 2007? 2010? For the following exercises, suppose a weight is attached to a spring and bobs up and down, exhibiting symmetry. 24. Suppose the graph of the displacement function is shown in Figure 1, where the values on the x-axis represent the time in seconds and the y-axis represents the displacement in inches. Give the equation that models the vertical displacement of the weight on the spring. x y

25. At time = 0, what is the displacement of the weight? 26. At what time does the displacement from the equilibrium point equal zero? 27. What is the time required for the weight to return to its initial height of 5 inches? In other words, what is the period for the displacement function? Inverse Trigonometric Functions For the following exercises, find the exact value without the aid of a calculator. 29. cos-1(  \sqrt{3}  _ 2  ) 31. cos-1(  1 _ \sqrt{2}   ) 32. sin-1 (  -\sqrt{3}  _  ) 33. sin-1( cos(  \p\frac{i}{6}  ) ) 34. cos-1( tan(  3\p\frac{i}{4}  ) ) 35. sin ( sec-1(  \frac{3}{5}  ) ) 36. cot ( sin-1(  \frac{3}{5}  ) ) 37. tan ( cos-1(  \frac{5}{13}  ) ) 38. sin ( cos-1(  \frac{x}{x} + 1  ) ) 39. Graph f (x) = cos x and f (x) = sec x on the interval [0, 2\pi ) and explain any observations. 40. Graph f (x) = sin x and f (x) = csc x and explain any observations. 41. Graph the function f (x) =  \frac{x}{1}  -  x^{3}

_ 3!  +  x^{5}

_ 5!  -  x^{7}

_ 7!  on the interval [-1, 1] and compare the graph to the graph of f (x) = sin x on the same interval. Describe any observations.

For the following exercises, sketch the graph of each function for two full periods. Determine the amplitude, the period, and the equation for the midline. 1. f (x) = 0.5sin x 2. f (x) = 5cos x 3. f (x) = 5sin x 4. f (x) = sin(3x) 5. f (x) = -cos ( x +  \p\frac{i}{3}  ) + 1 6. f (x) = 5sin ( 3( x -  \p\frac{i}{6}  ) ) + 4 7. f (x) = 3cos (  \frac{1}{3} x -  5\p\frac{i}{6}  ) 8. f (x) = tan(4x) 9. f (x) = -2tan ( x -  7\p\frac{i}{6}  ) + 2 10. f (x) = \pi cos(3x + \pi ) 11. f (x) = 5csc(3x) 12. f (x) = \pi sec (  \p\frac{i}{2} x ) 13. f (x) = 2csc ( x +  \p\frac{i}{4}  ) - 3 For the following exercises, determine the amplitude, period, and midline of the graph, and then find a formula for the function. 14. Give in terms of a sine function. x y 15. Give in terms of a sine function. x y 16. Give in terms of a tangent function. x y – \pi  \pi  –\pi  – 3\pi  3\pi  \pi  For the following exercises, find the amplitude, period, phase shift, and midline. 17. y = sin (  \p\frac{i}{6} x + \pi  ) - 3 18. y = 8sin (  7\p\frac{i}{6} x +  7\p\frac{i}{2}  ) + 6 19. The outside temperature over the course of a day can be modeled as a sinusoidal function. Suppose you know the temperature is 68°F at midnight and the high and low temperatures during the day are 80°F and 56°F, respectively. Assuming t is the number of hours since midnight, find a function for the temperature, D, in terms of t. 20. Water is pumped into a storage bin and empties according to a periodic rate. The depth of the water is 3 feet at its lowest at 2:00 a.m. and 71 feet at its highest, which occurs every 5 hours. Write a cosine function that models the depth of the water as a function of time, and then graph the function for one period. For the following exercises, find the period and horizontal shift of each function. 21. g(x) = 3tan(6x + 42) 22. n(x) = 4csc (  5\p\frac{i}{3} x -  20\p\frac{i}{3}  ) 23. Write the equation for the graph in Figure 1 in terms of the secant function and give the period and phase shift. x y

24. If tan x = 3, find tan(-x). 25. If sec x = 4, find sec(-x). For the following exercises, graph the functions on the specified window and answer the questions. 26. Graph m(x) = sin(2x) + cos(3x) on the viewing window [-10, 10] by [-3, 3]. Approximate the graph’s period. 27. Graph n(x) = 0.02sin(50\pi x) on the following domains in x: [0, 1] and [0, 3]. Suppose this function models sound waves. Why would these views look so different? 28. Graph f (x) =  sin x _____ x  on [-0.5, 0.5] and explain any observations. For the following exercises, let f (x) =  \frac{3}{5}  cos(6x). 29. What is the largest possible value for f (x)? 30. What is the smallest possible value for f (x)? 31. Where is the function increasing on the interval For the following exercises, find and graph one period of the periodic function with the given amplitude, period, and phase shift. 32. Sine curve with amplitude 3, period  \p\frac{i}{3} , and phase shift (h, k) = (  \p\frac{i}{4} , 2 ) 33. Cosine curve with amplitude 2, period  \p\frac{i}{6} , and phase shift (h, k) = ( - \p\frac{i}{4} , 3 ) For the following exercises, graph the function. Describe the graph and, wherever applicable, any periodic behavior, amplitude, asymptotes, or undefined points. 34. f (x) = 5cos(3x) + 4sin(2x) 35. f (x) = esint For the following exercises, find the exact value. 36. sin-1 (  \sqrt{3}  _ 2  ) 37. tan-1( \sqrt{3}  ) 38. cos-1 ( -  \sqrt{3}  _ 2  ) 39. cos-1(sin(\pi )) 40. cos-1 ( tan(  7\p\frac{i}{4}  ) ) 41. cos(sin-1(1 - 2x)) 43. cos(tan-1(x^{2})) For the following exercises, suppose sin t =  \frac{x}{x} + 1 . 44. tan t 45. csc t 46. Given Figure 2, find the measure of angle \theta  to three decimal places. Answer in radians. \theta  For the following exercises, determine whether the equation is true or false. 47. arcsin ( sin (  5\p\frac{i}{6}  ) ) =  5\p\frac{i}{6}  48. arccos ( cos (  5\p\frac{i}{6}  ) ) =  5\p\frac{i}{6}  49. The grade of a road is 7%. This means that for every horizontal distance of 100 feet on the road, the vertical rise is 7 feet. Find the angle the road makes with the horizontal in radians.
