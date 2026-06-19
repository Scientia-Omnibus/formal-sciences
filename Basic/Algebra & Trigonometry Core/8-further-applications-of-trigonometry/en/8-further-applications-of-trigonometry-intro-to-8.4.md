# Further Applications of Trigonometry

## Introduction

The world’s largest tree by volume, named General Sherman, stands 274.9 feet tall and resides in Northern California.[27] Just how do scientists know its true height? A common way to measure the height involves determining the angle of elevation, which is formed by the tree and the ground at a point some distance away from the base of the tree. This method is much more practical than climbing the tree and dropping a very long tape measure. In this chapter, we will explore applications of trigonometry that will enable us to solve many different kinds of problems, including finding the height of a tree. We extend topics we introduced in Trigonometric Functions and investigate applications more deeply and meaningfully. 27 Source: National Park Service. "The General Sherman Tree." http://www.nps.gov/seki/naturescience/sherman.htm. Accessed April 25, 2014.

Learning Objectives
In this section, you will:
• Use the Law of Sines to solve oblique triangles.
• Find the area of an oblique triangle using the sine function.
• Solve applied problems using the Law of Sines.

## 8.1 Non-right Triangles: Law of Sines

Suppose two radar stations located 20 miles apart each detect an aircraft between them. The angle of elevation measured by the first station is 35 degrees, whereas the angle of elevation measured by the second station is 15 degrees. How can we determine the altitude of the aircraft? We see in Figure 1 that the triangle formed by the aircraft and the two stations is not a right triangle, so we cannot use what we know about right triangles. In this section, we will find out how to solve problems involving non-right triangles. 15° 35° 20 miles Using the Law of Sines to Solve Oblique Triangles In any triangle, we can draw an altitude, a perpendicular line from one vertex to the opposite side, forming two right triangles. It would be preferable, however, to have methods that we can apply directly to non-right triangles without first having to create right triangles. Any triangle that is not a right triangle is an oblique triangle. Solving an oblique triangle means finding the measurements of all three angles and all three sides. To do so, we need to start with at least three of these values, including at least one of the sides. We will investigate three possible oblique triangle problem situations: 1. ASA (angle-side-angle) We know the measurements of two angles and the included side. See Figure 2. \gamma  \alpha  \beta  2. AAS (angle-angle-side) We know the measurements of two angles and a side that is not between the known angles. See Figure 3. \gamma  \alpha  \beta  3. SSA (side-side-angle) We know the measurements of two sides and an angle that is not between the known sides. See Figure 4. \gamma  \alpha  \beta 

Knowing how to approach each of these situations enables us to solve oblique triangles without having to drop a perpendicular to form two right triangles. Instead, we can use the fact that the ratio of the measurement of one of the angles to the length of its opposite side will be equal to the other two ratios of angle measure to opposite side. Let’s see how this statement is derived by considering the triangle shown in Figure 5. \gamma  \beta  \alpha  a b c h Using the right triangle relationships, we know that sin \alpha  =  \frac{h}{b}  and sin \beta  =  \frac{h}{a} . Solving both equations for h gives two different expressions for h.

h = bsin \alpha  and h = asin \beta  We then set the expressions equal to each other.

bsin \alpha  = asin \beta 

(  \frac{1}{a}b  )(bsin \alpha ) = (asin \beta )(  \frac{1}{a}b  ) Multiply both sides by  \frac{1}{a}b .

 sin \alph\frac{a}{a}  =  sin \bet\frac{a}{b}  Similarly, we can compare the other ratios.

 sin \alph\frac{a}{a}  =  sin \gamm\frac{a}{c}  and  sin \bet\frac{a}{b}  =  sin \gamm\frac{a}{c}  Collectively, these relationships are called the Law of Sines.

 sin \alph\frac{a}{a}  =  sin \bet\frac{a}{b}  =  sin \gamm\frac{a}{c}  Note the standard way of labeling triangles: angle \alpha  (alpha) is opposite side a; angle \beta  (beta) is opposite side b; and angle \gamma  (gamma) is opposite side c. See Figure 6. While calculating angles and sides, be sure to carry the exact values through to the final answer. Generally, final answers are rounded to the nearest tenth, unless otherwise specified. \gamma  \beta  \alpha  a b c Law of Sines Given a triangle with angles and opposite sides labeled as in Figure 6, the ratio of the measurement of an angle to the length of its opposite side will be equal to the other two ratios of angle measure to opposite side. All proportions will be equal. The Law of Sines is based on proportions and is presented symbolically two ways.

 sin \alph\frac{a}{a}  =  sin \bet\frac{a}{b}  =  sin \gamm\frac{a}{c} 

 \frac{a}{s}in \alpha   =  \frac{b}{s}in \beta   =  \frac{c}{s}in \gamma   To solve an oblique triangle, use any pair of applicable ratios.

**Example  1**

### Solving for Two Unknown Sides and Angle of an AAS Triangle

Solve the triangle shown in Figure 7 to the nearest tenth. \gamma  \alpha  b 50° 30° c \beta

**Solution**

The three angles must add up to 180 degrees. From this, we can determine that

\beta  = 180° - 50° - 30°

To find an unknown side, we need to know the corresponding angle and a known ratio. We know that angle \alpha  = 50° and its corresponding side a = 10. We can use the following proportion from the Law of Sines to find the length of c.

 sin(50°) _  =  sin(30°) _ c 

c  sin(50°) _  = sin(30°)

Multiply both sides by c.

c = sin(30°)  _ sin(50°)  Multiply by the reciprocal to isolate c.

Similarly, to solve for b, we set up another proportion.

 sin(50°) _  =  sin(100°) _ b 

bsin(50°) = 10sin(100°)

Multiply both sides by b.

b =  10sin(100°) _ sin(50°) 

Multiply by the reciprocal to isolate b.

Therefore, the complete set of angles and sides is

\alpha  = 50° a = 10

\gamma  = 30°

**Try It #1**

Solve the triangle shown in Figure 8 to the nearest tenth.

\alpha  98° 43° c a \beta  Using The Law of Sines to Solve SSA Triangles We can use the Law of Sines to solve any oblique triangle, but some solutions may not be straightforward. In some cases, more than one triangle may satisfy the given criteria, which we describe as an ambiguous case. Triangles classified as SSA, those in which we know the lengths of two sides and the measurement of the angle opposite one of the given sides, may result in one or two solutions, or even no solution.

possible outcomes for SSA triangles Oblique triangles in the category SSA may have four different outcomes. Figure 9 illustrates the solutions with the known sides a and b and known angle \alpha . \gamma  \beta  \alpha  a b \gamma  \beta  \alpha  a b \gamma  \beta  \alpha  a a h b \gamma  \beta  \alpha  a b (a) (b) (c) (d) No triangle, a < h Right triangle, a = h Two triangles, a > h, a < b One triangle, a \ge  b

**Example  2**

### Solving an Oblique SSA Triangle

Solve the triangle in Figure 10 for the missing side and find the missing angle measures to the nearest tenth. \gamma  \alpha  35° \beta

**Solution**

Use the Law of Sines to find angle \beta  and angle \gamma , and then side c. Solving for \beta , we have the proportion

 sin \alph\frac{a}{a}  =  sin \bet\frac{a}{b} 

 sin(35°) _  =  sin \bet\frac{a}{8} 

 8sin(35°) _  = sin \beta 

However, in the diagram, angle \beta  appears to be an obtuse angle and may be greater than 90°. How did we get an acute angle, and how do we find the measurement of \beta ? Let’s investigate further. Dropping a perpendicular from \gamma  and viewing the triangle from a right angle perspective, we have Figure 11. It appears that there may be a second triangle that will fit the given criteria. \gamma ' \beta ' \beta  \phi  \alpha ' 35° The angle supplementary to \beta  is approximately equal to 49.9°, which means that \beta  = 180° - 49.9° = 130.1°. (Remember that the sine function is positive in both the first and second quadrants.) Solving for \gamma , we have

We can then use these measurements to solve the other triangle. Since \gamma ' is supplementary to \alpha  and \beta , we have

Now we need to find c and c'. We have

 \frac{c}{s}in(14.9°)  =  _ sin(35°) 

c =  6sin(14.9°) _ sin(35°)  ≈ 2.7 Finally,

 c' _ sin(95.1°)  =  _ sin(35°) 

c' =  6sin(95.1°) _ sin(35°)  ≈ 10.4 To summarize, there are two triangles with an angle of 35°, an adjacent side of 8, and an opposite side of 6, as shown in Figure 12. \gamma  \beta  \alpha  35° 14.9° b = 8 a = 6 \gamma ' \beta ' \alpha ' b' = 8 a' = 6 95.1° 49.9° 35° (a) (b) However, we were looking for the values for the triangle with an obtuse angle \beta . We can see them in the first triangle (a) in Figure 12.

**Try It #2**

Given \alpha  = 80°, a = 120, and b = 121, find the missing side and angles. If there is more than one possible solution, show both.

**Example  3**

### Solving for the Unknown Sides and Angles of a SSA Triangle

In the triangle shown in Figure 13, solve for the unknown side and angles. Round your answers to the nearest tenth. \alpha  85° \beta  a

**Solution**

In choosing the pair of ratios from the Law of Sines to use, look at the information given. In this case, we know the angle \gamma  = 85°, and its corresponding side c = 12, and we know side b = 9. We will use this proportion to solve for \beta .

 sin(85°) _  =  sin \bet\frac{a}{9}  Isolate the unknown.

 9sin(85°) _  = sin \beta 

To find \beta , apply the inverse sine function. The inverse sine will produce a single result, but keep in mind that there may be two values for \beta . It is important to verify the result, as there may be two viable solutions, only one solution (the usual case), or no solutions.

\beta  = sin-1 (  9sin(85°) _  )

In this case, if we subtract \beta  from 180°, we find that there may be a second possible solution. Thus, \beta  = 180° - 48.3° ≈ 131.7°. To check the solution, subtract both angles, 131.7° and 85°, from 180°. This gives

which is impossible, and so \beta  ≈ 48.3°. To find the remaining missing values, we calculate \alpha  = 180° - 85° - 48.3° ≈ 46.7°. Now, only side a is needed. Use the Law of Sines to solve for a by one of the proportions.

 sin(85°) _  =  sin(46.7°) _ a 

a  sin(85°) _  = sin(46.7°)

a =  12sin(46.7°) __ sin(85°)  ≈ 8.8 The complete set of solutions for the given triangle is

b = 9

\gamma  = 85° c = 12

**Try It #3**

Given \alpha  = 80°, a = 100, b = 10, find the missing side and angles. If there is more than one possible solution, show both. Round your answers to the nearest tenth.

**Example  4**

Finding the Triangles That Meet the Given Criteria Find all possible triangles if one side has length 4 opposite an angle of 50°, and a second side has length 10.

**Solution**

Using the given information, we can solve for the angle opposite the side of length 10. See Figure 14.

 sin \alph\frac{a}{10}  =  sin(50°) _ 

sin \alpha  =  10sin(50°) _________ 

\alpha  50° We can stop here without finding the value of \alpha . Because the range of the sine function is [-1, 1], it is impossible for the sine value to be 1.915. In fact, inputting sin-1 (1.915) in a graphing calculator generates an ERROR DOMAIN. Therefore, no triangles can be drawn with the provided dimensions.

**Try It #4**

Determine the number of triangles possible given a = 31, b = 26, \beta  = 48°.

Finding the Area of an Oblique Triangle Using the Sine Function Now that we can solve a triangle for missing values, we can use some of those values and the sine function to find the area of an oblique triangle. Recall that the area formula for a triangle is given as Area =  \frac{1}{2} bh, where b is base and h is height. For oblique triangles, we must find h before we can use the area formula. Observing the two triangles in Figure 15, one acute and one obtuse, we can drop a perpendicular to represent the height and then apply the trigonometric property sin \alpha  =  opposit\frac{e}{h}ypotenuse  to write an equation for area in oblique triangles. In the acute triangle, we have sin \alpha  =  \frac{h}{c}  or csin \alpha  = h. However, in the obtuse triangle, we drop the perpendicular outside the triangle and extend the base b to form a right triangle. The angle used in calculation is \alpha ', or 180 - \alpha . \gamma  \gamma  \beta  \beta  \alpha  \alpha  \alpha ' b b a a c c h h Thus,

Area =  \frac{1}{2} (base)(height) =  \frac{1}{2} b(csin \alpha ) Similarly,

Area =  \frac{1}{2} a(bsin \gamma ) =  \frac{1}{2} a(csin \beta ) area of an oblique triangle The formula for the area of an oblique triangle is given by

Area =  \frac{1}{2} bcsin \alpha 

=  \frac{1}{2} acsin \beta 

=  \frac{1}{2} absin \gamma  This is equivalent to one-half of the product of two sides and the sine of their included angle.

**Example  5**

Finding the Area of an Oblique Triangle Find the area of a triangle with sides a = 90, b = 52, and angle \gamma  = 102°. Round the area to the nearest integer.

**Solution**

Using the formula, we have

Area =  \frac{1}{2} absin \gamma 

Area =  \frac{1}{A}rea ≈ 2289 square units

**Try It #5**

Find the area of the triangle given \beta  = 42°, a = 7.2 ft, c = 3.4 ft. Round the area to the nearest tenth. Solving Applied Problems Using the Law of Sines The more we study trigonometric applications, the more we discover that the applications are countless. Some are flat, diagram-type situations, but many applications in calculus, engineering, and physics involve three dimensions and motion.

**Example  6**

Finding an Altitude Find the altitude of the aircraft in the problem introduced at the beginning of this section, shown in Figure 16. Round the altitude to the nearest tenth of a mile. a 15° 35° 20 miles

**Solution**

To find the elevation of the aircraft, we first find the distance from one station to the aircraft, such as the side a, and then use right triangle relationships to find the height of the aircraft, h. Because the angles in the triangle add up to 180 degrees, the unknown angle must be 180° - 15° - 35° = 130°. This angle is opposite the side of length 20, allowing us to set up a Law of Sines relationship.

 sin(130°) _  =  sin(35°) _ a 

asin(130°) = 20sin(35°)

a =  20sin(35°) _ sin(130°) 

The distance from one station to the aircraft is about 14.98 miles. Now that we know a, we can use right triangle relationships to solve for h.

sin(15°) =  opposit\frac{e}{h}ypotenuse 

sin(15°) =  \frac{h}{a} 

sin(15°) =  \frac{h}{T}he aircraft is at an altitude of approximately 3.9 miles.

**Try It #6**

The diagram shown in Figure 17 represents the height of a blimp flying over a football stadium. Find the height of the blimp if the angle of elevation at the southern end zone, point A, is 70°, the angle of elevation from the northern end zone, point B, is 62°, and the distance between the viewing points of the two end zones is 145 yards. 145 yards 70° C A B 62°

Access the following online resources for additional instruction and practice with trigonometric applications. • Law of Sines: The Basics (http://openstaxcollege.org/l/sinesbasic) • Law of Sines: The Ambiguous Case (http://openstaxcollege.org/l/sinesambiguous)

### 8.1 Section Exercises

Verbal 1. Describe the altitude of a triangle. 2. Compare right triangles and oblique triangles. 3. When can you use the Law of Sines to find a missing angle? 4. In the Law of Sines, what is the relationship between the angle in the numerator and the side in the denominator? 5. What type of triangle results in an ambiguous case? Algebraic For the following exercises, assume \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c. Solve each triangle, if possible. Round each answer to the nearest tenth. For the following exercises, use the Law of Sines to solve for the missing side for each oblique triangle. Round each answer to the nearest hundredth. Assume that angle A is opposite side a, angle B is opposite side b, and angle C is opposite side c. 11. Find side b when A = 37°, B = 49°, c = 5. 12. Find side a when A = 132°, C = 23°, b = 10. 13. Find side c when B = 37°, C = 21, b = 23. For the following exercises, assume \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c. Determine whether there is no triangle, one triangle, or two triangles. Then solve each triangle, if possible. Round each answer to the nearest tenth. For the following exercises, use the Law of Sines to solve, if possible, the missing side or angle for each triangle or triangles in the ambiguous case. Round each answer to the nearest tenth. 24. Find angle A when a = 24, b = 5, B = 22°. 25. Find angle A when a = 13, b = 6, B = 20°. 26. Find angle B when A = 12°, a = 2, b = 9. For the following exercises, find the area of the triangle with the given measurements. Round each answer to the nearest tenth. Graphical For the following exercises, find the length of side x. Round to the nearest tenth. x 70° 50° x 25° 120° x 75° 45°

## 8.1 Section Exercises

x 110° 40° x 111° 22° 8.6 For the following exercises, find the measure of angle x, if possible. Round to the nearest tenth. 98° x 37° x 22° x 59° 5.3 5.7 x 41. Notice that x is an obtuse angle. 55° x 65° x For the following exercises, solve the triangle. Round each answer to the nearest tenth. 93° 24.1 32.6 A B C For the following exercises, find the area of each triangle. Round each answer to the nearest tenth. 30° 25° 51° 4.5 2.9 3.5 58° 51° 40° 30° 115° x 42° 50°

Extensions 50. Find the radius of the circle in Figure 18. Round to the nearest tenth. 145° 51. Find the diameter of the circle in Figure 19. Round to the nearest tenth. 110° 8.3 52. Find m ∠ADC in Figure 20. Round to the nearest tenth. 60° A B C D 53. Find AD in Figure 21. Round to the nearest tenth. 53° 44° B C A D 54. Solve both triangles in Figure 22. Round each answer to the nearest tenth. 48° 46° 48° 2 4.2 A B E C D 55. Find AB in the parallelogram shown in Figure 23. 130° 130° A B D C 56. Solve the triangle in Figure 24. (Hint: Draw a perpendicular from H to JK). Round each answer to the nearest tenth. 20° H K J 57. Solve the triangle in Figure 25. (Hint: Draw a perpendicular from N to LM). Round each answer to the nearest tenth. 74° 4.6 L M N

58. In Figure 26, ABCD is not a parallelogram. ∠m is obtuse. Solve both triangles. Round each answer to the nearest tenth. 35° 65° A B x m h k y D C n Real-World Applications 59. A pole leans away from the sun at an angle of 7° to the vertical, as shown in Figure 27. When the elevation of the sun is 55°, the pole casts a shadow 42 feet long on the level ground. How long is the pole? Round the answer to the nearest tenth. 60. To determine how far a boat is from shore, two radar stations 500 feet apart find the angles out to the boat, as shown in Figure 28. Determine the distance of the boat from station A and the distance of the boat from shore. Round your answers to the nearest whole foot. 70° A B 60° 61. Figure 29 shows a satellite orbiting Earth. The satellite passes directly over two tracking stations A and B, which are 69 miles apart. When the satellite is on one side of the two stations, the angles of elevation at A and B are measured to be 86.2° and 83.9°, respectively. How far is the satellite from station A and how high is the satellite above the ground? Round answers to the nearest whole mile. 83.9° 86.2° A B 62. A communications tower is located at the top of a steep hill, as shown in Figure 30. The angle of inclination of the hill is 67°. A guy wire is to be attached to the top of the tower and to the ground, 165 meters downhill from the base of the tower. The angle formed by the guy wire and the hill is 16°. Find the length of the cable required for the guy wire to the nearest whole meter. 16° 67° 165m

63. The roof of a house is at a 20° angle. An 8-foot solar panel is to be mounted on the roof and should be angled 38° relative to the horizontal for optimal results. (See Figure 31). How long does the vertical support holding up the back of the panel need to be? Round to the nearest tenth. 20° 38° 8 f 64. Similar to an angle of elevation, an angle of depression is the acute angle formed by a horizontal line and an observer’s line of sight to an object below the horizontal. A pilot is flying over a straight highway. He determines the angles of depression to two mileposts, 6.6 km apart, to be 37° and 44°, as shown in Figure 32. Find the distance of the plane from point A to the nearest tenth of a kilometer. 44° 37° A B 65. A pilot is flying over a straight highway. He determines the angles of depression to two mileposts, 4.3 km apart, to be 32° and 56°, as shown in Figure 33. Find the distance of the plane from point A to the nearest tenth of a kilometer. A B 66. In order to estimate the height of a building, two students stand at a certain distance from the building at street level. From this point, they find the angle of elevation from the street to the top of the building to be 39°. They then move 300 feet closer to the building and find the angle of elevation to be 50°. Assuming that the street is level, estimate the height of the building to the nearest foot. 67. In order to estimate the height of a building, two students stand at a certain distance from the building at street level. From this point, they find the angle of elevation from the street to the top of the building to be 35°. They then move 250 feet closer to the building and find the angle of elevation to be 53°. Assuming that the street is level, estimate the height of the building to the nearest foot. 68. Points A and B are on opposite sides of a lake. Point C is 97 meters from A. The measure of angle BAC is determined to be 101°, and the measure of angle ACB is determined to be 53°. What is the distance from A to B, rounded to the nearest whole meter? 69. A man and a woman standing 3 \frac{1}{2}  miles apart spot a hot air balloon at the same time. If the angle of elevation from the man to the balloon is 27°, and the angle of elevation from the woman to the balloon is 41°, find the altitude of the balloon to the nearest foot. 70. Two search teams spot a stranded climber on a mountain. The first search team is 0.5 miles from the second search team, and both teams are at an altitude of 1 mile. The angle of elevation from the first search team to the stranded climber is 15°. The angle of elevation from the second search team to the climber is 22°. What is the altitude of the climber? Round to the nearest tenth of a mile.

71. A street light is mounted on a pole. A 6-foot-tall man is standing on the street a short distance from the pole, casting a shadow. The angle of elevation from the tip of the man’s shadow to the top of his head of 28°. A 6-foot-tall woman is standing on the same street on the opposite side of the pole from the man. The angle of elevation from the tip of her shadow to the top of her head is 28°. If the man and woman are 20 feet apart, how far is the street light from the tip of the shadow of each person? Round the distance to the nearest tenth of a foot. 72. Three cities, A, B, and C, are located so that city A is due east of city B. If city C is located 35° west of north from city B and is 100 miles from city A and 70 miles from city B, how far is city A from city B? Round the distance to the nearest tenth of a mile. 73. Two streets meet at an 80° angle. At the corner, a park is being built in the shape of a triangle. Find the area of the park if, along one road, the park measures 180 feet, and along the other road, the park measures 215 feet. 74. Brian’s house is on a corner lot. Find the area of the front yard if the edges measure 40 and 56 feet, as shown in Figure 34. House 56 f 40 f 135° 75. The Bermuda triangle is a region of the Atlantic Ocean that connects Bermuda, Florida, and Puerto Rico. Find the area of the Bermuda triangle if the distance from Florida to Bermuda is 1030 miles, the distance from Puerto Rico to Bermuda is 980 miles, and the angle created by the two distances is 62°. 76. A yield sign measures 30 inches on all three sides. What is the area of the sign? 77. Naomi bought a modern dining table whose top is in the shape of a triangle. Find the area of the table top if two of the sides measure 4 feet and 4.5 feet, and the smaller angles measure 32° and 42°, as shown in Figure 35. 32° 4 feet 42°

Learning Objectives
In this section, you will:
• Use the Law of Cosines to solve oblique triangles.
• Solve applied problems using the Law of Cosines.
• Use Heron’s formula to find the area of a triangle.

## 8.2 Non-right Triangles: Law of COSines

Suppose a boat leaves port, travels 10 miles, turns 20 degrees, and travels another 8 miles as shown in Figure 1. How far from port is the boat? 8 mi 20° 10 mi Port Unfortunately, while the Law of Sines enables us to address many non-right triangle cases, it does not help us with triangles where the known angle is between two known sides, a SAS (side-angle-side) triangle, or when all three sides are known, but no angles are known, a SSS (side-side-side) triangle. In this section, we will investigate another tool for solving oblique triangles described by these last two cases. Using the Law of Cosines to Solve Oblique Triangles The tool we need to solve the problem of the boat’s distance from the port is the Law of Cosines, which defines the relationship among angle measurements and side lengths in oblique triangles. Three formulas make up the Law of Cosines. At first glance, the formulas may appear complicated because they include many variables. However, once the pattern is understood, the Law of Cosines is easier to work with than most formulas at this mathematical level. Understanding how the Law of Cosines is derived will be helpful in using the formulas. The derivation begins with the Generalized Pythagorean Theorem, which is an extension of the Pythagorean Theorem to non-right triangles. Here is how it works: An arbitrary non-right triangle ABC is placed in the coordinate plane with vertex A at the origin, side c drawn along the x-axis, and vertex C located at some point (x, y) in the plane, as illustrated in Figure 2. Generally, triangles exist anywhere in the plane, but for this explanation we will place the triangle as noted. x b c B A x y C (b cos\theta , b sin\theta ) x 2 c a y \theta 

We can drop a perpendicular from C to the x-axis (this is the altitude or height). Recalling the basic trigonometric identities, we know that cos \theta  =  x(adjacent) __

b(hypotenuse)  and sin \theta  =  y(opposite) __

b(hypotenuse)  In terms of \theta , x = bcos \theta  and y = bsin \theta . The (x, y) point located at C has coordinates (bcos \theta , bsin \theta ). Using the side (x - c) as one leg of a right triangle and y as the second leg, we can find the length of hypotenuse a using the Pythagorean Theorem. Thus,

a^{2} = (x - c)^{2} + y^{2}

= (bcos \theta  - c)^{2} + (bsin \theta )^{2} Substitute (bcos \theta ) for x and (bsin \theta ) for y.

= (b^{2} cos^{2} \theta  - 2bccos \theta  + c^{2}) + b^{2} sin^{2} \theta  Expand the perfect square.

= b^{2} cos^{2} \theta  + b^{2} sin^{2} \theta  + c^{2} - 2bccos \theta  Group terms noting that cos^{2} \theta  + sin^{2} \theta  = 1.

= b^{2}(cos^{2} \theta  + sin^{2} \theta ) + c^{2} - 2bccos \theta  Factor out b^{2}.

a^{2} = b^{2} + c^{2} - 2bccos \theta  The formula derived is one of the three equations of the Law of Cosines. The other equations are found in a similar fashion. Keep in mind that it is always helpful to sketch the triangle when solving for angles or sides. In a real-world scenario, try to draw a diagram of the situation. As more information emerges, the diagram may have to be altered. Make those alterations to the diagram and, in the end, the problem will be easier to solve. Law of Cosines The Law of Cosines states that the square of any side of a triangle is equal to the sum of the squares of the other two sides minus twice the product of the other two sides and the cosine of the included angle. For triangles labeled as in Figure 3, with angles \alpha , \beta , and \gamma , and opposite corresponding sides a, b, and c, respectively, the Law of Cosines is given as three equations. a^{2} = b^{2} + c^{2} - 2bc cos \alpha  b^{2} = a^{2} + c^{2} - 2ac cos \beta  c^{2} = a^{2} + b^{2} - 2ab cos \gamma  To solve for a missing side measurement, the corresponding opposite angle measure is needed. When solving for an angle, the corresponding opposite side measure is needed. We can use another version of the Law of Cosines to solve for an angle. cos \alpha  =  b^{2} + c^{2} - a^{2} _ 2bc  cos \beta  =  a^{2} + c^{2} - b^{2} _ 2ac  cos \gamma  =  a^{2} + b^{2} - c^{2} _ 2ab  a b c \alpha  \beta  \gamma 

**How To…**

Given two sides and the angle between them (SAS), find the measures of the remaining side and angles of a triangle. 1. Sketch the triangle. Identify the measures of the known sides and angles. Use variables to represent the measures of the unknown sides and angles. 2. Apply the Law of Cosines to find the length of the unknown side or angle. 3. Apply the Law of Sines or Cosines to find the measure of a second angle. 4. Compute the measure of the remaining angle.

**Example  1**

Finding the Unknown Side and Angles of a SAS Triangle Find the unknown side and angles of the triangle in Figure 4. \gamma  b 30° \beta  \alpha

**Solution**

First, make note of what is given: two sides and the angle between them. This arrangement is classified as SAS and supplies the data needed to apply the Law of Cosines. Each one of the three laws of cosines begins with the square of an unknown side opposite a known angle. For this example, the first side to solve for is side b, as we know the measurement of the opposite angle \beta .

b^{2} = a^{2} + c^{2}-2accos \beta 

Substitute the measurements for the known quantities.

\frac{3}{2}  ) Evaluate the cosine and begin to simplify.

3 

b = \sqrt{3}   Use the square root property.

Because we are solving for a length, we use only the positive square root. Now that we know the length b, we can use the Law of Sines to fill in the remaining angles of the triangle. Solving for angle \alpha , we have

 sin \alph\frac{a}{a}  =  sin \bet\frac{a}{b} 

 sin \alph\frac{a}{10}  =  sin(30°) _

sin \alpha  =  10sin(30°) _ 6.013  Multiply both sides of the equation by 10.

\alpha  = sin-1(  10sin(30°) _ Find the inverse sine of  10sin(30°) _ 6.013 .

The other possibility for \alpha  would be \alpha  = 180° - 56.3° ≈ 123.7°. In the original diagram, \alpha  is adjacent to the longest side, so \alpha  is an acute angle and, therefore, 123.7° does not make sense. Notice that if we choose to apply the Law of Cosines, we arrive at a unique answer. We do not have to consider the other possibilities, as cosine is unique for angles between 0° and 180°. Proceeding with \alpha  ≈ 56.3°, we can then find the third angle of the triangle.

The complete set of angles and sides is

a = 10

\beta  = 30°

c = 12

**Try It #1**

Find the missing side and angles of the given triangle: \alpha  = 30°, b = 12, c = 24.

**Example  2**

### Solving for an Angle of a SSS Triangle

Find the angle \alpha  for the given triangle if side a = 20, side b = 25, and side c = 18.

**Solution**

For this example, we have no angles. We can solve for any angle using the Law of Cosines. To solve for angle \alpha , we have

a^{2} = b^{2} + c^{2} -2bccos \alpha 

Substitute the appropriate measurements.

Simplify in each step.

Isolate cos \alpha .

_ -900  = cos \alpha 

0.61 ≈ cos \alpha 

cos-1(0.61) ≈ \alpha  Find the inverse cosine.

See Figure 5. c = 18 a = 20 b = 25 52.4° \gamma  \beta  \alpha 

**Analysis**
Because the inverse cosine can return any angle between 0 and 180 degrees, there will not be any ambiguous cases using this method.

**Try It #2**

Given a = 5, b = 7, and c = 10, find the missing angles. Solving Applied Problems Using the Law of Cosines Just as the Law of Sines provided the appropriate equations to solve a number of applications, the Law of Cosines is applicable to situations in which the given data fits the cosine models. We may see these in the fields of navigation, surveying, astronomy, and geometry, just to name a few.

**Example  3**

Using the Law of Cosines to Solve a Communication Problem On many cell phones with GPS, an approximate location can be given before the GPS signal is received. This is accomplished through a process called triangulation, which works by using the distances from two known points. Suppose there are two cell phone towers within range of a cell phone. The two towers are located 6,000 feet apart along a straight highway, running east to west, and the cell phone is north of the highway. Based on the signal delay, it can be determined that the signal is 5,050 feet from the first tower and 2,420 feet from the second tower. Determine the position of the cell phone north and east of the first tower, and determine how far it is from the highway.

**Solution**

For simplicity, we start by drawing a diagram similar to Figure 6 and labeling our given information. \theta  Using the Law of Cosines, we can solve for the angle \theta . Remember that the Law of Cosines uses the square of one side to find the cosine of the opposite angle. For this example, let a = 2420, b = 5050, and c = 6000. Thus, \theta  corresponds to the opposite side a = 2420.

a^{2} = b^{2} + c^{2} - 2bccos \theta 

___

 = cos \theta 

To answer the questions about the phone’s position north and east of the tower, and the distance to the highway, drop a perpendicular from the position of the cell phone, as in Figure 7. This forms two right triangles, although we only need the right triangle that includes the first tower for this problem. x y 23.3° Using the angle \theta  = 23.3° and the basic trigonometric identities, we can find the solutions. Thus

cos(23.3°) =  \frac{x}{s}in(23.3°) =  \frac{y}{T}he cell phone is approximately 4,638 feet east and 1,998 feet north of the first tower, and 1,998 feet from the highway.

**Example  4**

### Calculating Distance Traveled Using a SAS Triangle

Returning to our problem at the beginning of this section, suppose a boat leaves port, travels 10 miles, turns 20 degrees, and travels another 8 miles. How far from port is the boat? The diagram is repeated here in Figure 8.

8 mi 20° 10 mi Port

**Solution**

The boat turned 20 degrees, so the obtuse angle of the non-right triangle is the supplemental angle, 180° - 20° = 160°. With this, we can utilize the Law of Cosines to find the missing side of the obtuse triangle—the distance of the boat to the port.

x = \sqrt{x} ≈ 17.7 miles The boat is about 17.7 miles from port. Using Heron’s Formula to Find the Area of a Triangle We already learned how to find the area of an oblique triangle when we know two sides and an angle. We also know the formula to find the area of a triangle using the base and the height. When we know the three sides, however, we can use Heron’s formula instead of finding the height. Heron of Alexandria was a geometer who lived during the first century A.D. He discovered a formula for finding the area of oblique triangles when three sides are known. Heron’s formula Heron’s formula finds the area of oblique triangles in which sides a, b, and c are known. Area = \sqrt{—}

s(s - a)(s - b)(s - c)  where s =  (a + b + c) _  is one half of the perimeter of the triangle, sometimes called the semi-perimeter.

**Example  5**

Using Heron’s Formula to Find the Area of a Given Triangle Find the area of the triangle in Figure 9 using Heron’s formula. A B a = 10 b = 15 c = 7 C

**Solution**

First, we calculate s.

s =  (a + b + c) _ 

s =  (10 + 15 + 7)

__  = 16

Then we apply the formula.

Area = \sqrt{—}

s(s - a)(s - b)(s - c) 

Area = \sqrt{—}

The area is approximately 29.4 square units.

**Try It #3**

Use Heron’s formula to find the area of a triangle with sides of lengths a = 29.7 ft, b = 42.3 ft, and c = 38.4 ft.

**Example  6**

### Applying Heron’s Formula to a Real-World Problem

A Chicago city developer wants to construct a building consisting of artist’s lofts on a triangular lot bordered by Rush Street, Wabash Avenue, and Pearson Street. The frontage along Rush Street is approximately 62.4 meters, along Wabash Avenue it is approximately 43.5 meters, and along Pearson Street it is approximately 34.1 meters. How many square meters are available to the developer? See Figure 10 for a view of the city property. E. Pearson St (34.1 meters) N. Wabash Ave (43.5 meters) Rush St (62.4 meters)

**Solution**

Find the measurement for s, which is one-half of the perimeter.

__ 

s = 70 m Apply Heron’s formula.

Area = \sqrt{—}

Area = \sqrt{The} developer has about 711.4 square meters.

**Try It #4**

Find the area of a triangle given a = 4.38 ft , b = 3.79 ft, and c = 5.22 ft. Access these online resources for additional instruction and practice with the Law of Cosines. • Law of Cosines (http://openstaxcollege.org/l/lawcosines) • Law of Cosines: Applications (http://openstaxcollege.org/l/cosineapp) • Law of Cosines: Applications 2 (http://openstaxcollege.org/l/cosineapp^{2})

## 8.2 Section Exercises

### 8.2 Section Exercises

Verbal 1. If you are looking for a missing side of a triangle, what do you need to know when using the Law of Cosines? 2. If you are looking for a missing angle of a triangle, what do you need to know when using the Law of Cosines? 3. Explain what s represents in Heron’s formula. 4. Explain the relationship between the Pythagorean Theorem and the Law of Cosines. 5. When must you use the Law of Cosines instead of the Pythagorean Theorem? Algebraic For the following exercises, assume \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c. If possible, solve each triangle for the unknown side. Round to the nearest tenth. For the following exercises, use the Law of Cosines to solve for the missing angle of the oblique triangle. Round to the nearest tenth. 16. a = 42, b = 19, c = 30; find angle A. 17. a = 14, b = 13, c = 20; find angle C. 18. a = 16, b = 31, c = 20; find angle B. 19. a = 13, b = 22, c = 28; find angle A. 20. a = 108, b = 132, c = 160; find angle C. For the following exercises, solve the triangle. Round to the nearest tenth. For the following exercises, use Heron’s formula to find the area of the triangle. Round to the nearest hundredth. 27. Find the area of a triangle with sides of length 18 in, 21 in, and 32 in. Round to the nearest tenth. 28. Find the area of a triangle with sides of length 20 cm, 26 cm, and 37 cm. Round to the nearest tenth. _ 2  m, b =  \frac{1}{3}  m, c =  \frac{1}{4}  m Graphical For the following exercises, find the length of side x. Round to the nearest tenth. x 6.5 72° 4.5 3.4 x 42o A B x 40°

x 65° x 50° 123° x For the following exercises, find the measurement of angle A. A 1.5 2.5 2.3 A 4.3 6.8 8.2 A 42. Find the measure of each angle in the triangle shown in Figure 11. Round to the nearest tenth. A B C For the following exercises, solve for the unknown side. Round to the nearest tenth. 60° 30° 22° 88° 38.7 40.6 23.3 A

For the following exercises, find the area of the triangle. Round to the nearest hundredth. 1.9 2.6 4.3 12.5 8.9 16.2 Extensions 52. A parallelogram has sides of length 16 units and 10 units. The shorter diagonal is 12 units. Find the measure of the longer diagonal. 53. The sides of a parallelogram are 11 feet and 17 feet. The longer diagonal is 22 feet. Find the length of the shorter diagonal. 54. The sides of a parallelogram are 28 centimeters and 40 centimeters. The measure of the larger angle is 100°. Find the length of the shorter diagonal. 55. A regular octagon is inscribed in a circle with a radius of 8 inches. (See Figure 12.) Find the perimeter of the octagon. 56. A regular pentagon is inscribed in a circle of radius 12 cm. (See Figure 13.) Find the perimeter of the pentagon. Round to the nearest tenth of a centimeter. For the following exercises, suppose that x^{2} = 25 + 36 - 60 cos(52) represents the relationship of three sides of a triangle and the cosine of an angle. 57. Draw the triangle. 58. Find the length of the third side.

For the following exercises, find the area of the triangle. 5.3 3.4 22° 80° 12.8 18.8 18° Real-World Applications 62. A surveyor has taken the measurements shown in answers to the nearest tenth. 800 f 70° 900 f 63. A satellite calculates the distances and angle shown in the two cities. Round answers to the nearest tenth. 2.1° 64. An airplane flies 220 miles with a heading of 40°, and then flies 180 miles with a heading of 170°. How far is the plane from its starting point, and at what heading? Round answers to the nearest tenth. 65. A 113-foot tower is located on a hill that is inclined 34° to the horizontal, as shown in Figure 16. A guy- wire is to be attached to the top of the tower and anchored at a point 98 feet uphill from the base of the tower. Find the length of wire needed. 98 f 34° 113 f

66. Two ships left a port at the same time. One ship traveled at a speed of 18 miles per hour at a heading of 320°. The other ship traveled at a speed of 22 miles per hour at a heading of 194°. Find the distance between the two ships after 10 hours of travel. 67. The graph in Figure 17 represents two boats departing at the same time from the same dock. The first boat is traveling at 18 miles per hour at a heading of 327° and the second boat is traveling at 4 miles per hour at a heading of 60°. Find the distance between the two boats after 2 hours. 4 mph 18 mph 68. A triangular swimming pool measures 40 feet on one side and 65 feet on another side. These sides form an angle that measures 50°. How long is the third side (to the nearest tenth)? 69. A pilot flies in a straight path for 1 hour 30 min. She then makes a course correction, heading 10° to the right of her original course, and flies 2 hours in the new direction. If she maintains a constant speed of 680 miles per hour, how far is she from her starting position? 70. Los Angeles is 1,744 miles from Chicago, Chicago is 714 miles from New York, and New York is 2,451 miles from Los Angeles. Draw a triangle connecting these three cities, and find the angles in the triangle. 71. Philadelphia is 140 miles from Washington, D.C., Washington, D.C. is 442 miles from Boston, and Boston is 315 miles from Philadelphia. Draw a triangle connecting these three cities and find the angles in the triangle. 72. Two planes leave the same airport at the same time. One flies at 20° east of north at 500 miles per hour. The second flies at 30° east of south at 600 miles per hour. How far apart are the planes after 2 hours? 73. Two airplanes take off in different directions. One travels 300 mph due west and the other travels 25° north of west at 420 mph. After 90 minutes, how far apart are they, assuming they are flying at the same altitude? 74. A parallelogram has sides of length 15.4 units and 9.8 units. Its area is 72.9 square units. Find the measure of the longer diagonal. 75. The four sequential sides of a quadrilateral have angle between the two smallest sides is 117°. What is the area of this quadrilateral? 76. The four sequential sides of a quadrilateral have angle between the two smallest sides is 106°. What is the area of this quadrilateral? 77. Find the area of a triangular piece of land that measures 30 feet on one side and 42 feet on another; the included angle measures 132°. Round to the nearest whole square foot. 78. Find the area of a triangular piece of land that measures 110 feet on one side and 250 feet on another; the included angle measures 85°. Round to the nearest whole square foot.

Learning Objectives
In this section, you will:
• Plot points using polar coordinates.
• Convert from polar coordinates to rectangular coordinates.
• Convert from rectangular coordinates to polar coordinates.
• Transform equations between polar and rectangular forms.
• Identify and graph polar equations by converting to rectangular equations.

## 8.3 Polar Coordinates

Over 12 kilometers from port, a sailboat encounters rough weather and is blown off course by a 16-knot wind (see representing location that is different from a standard coordinate grid. Port 16-knot wind 60° 30° 330° 300° 270° 240° 210° 180° 150° 120° 90° Plotting Points Using Polar Coordinates When we think about plotting points in the plane, we usually think of rectangular coordinates (x, y) in the Cartesian coordinate plane. However, there are other ways of writing a coordinate pair and other types of grid systems. In this section, we introduce to polar coordinates, which are points labeled (r, \theta ) and plotted on a polar grid. The polar grid is represented as a series of concentric circles radiating out from the pole, or the origin of the coordinate plane. The polar grid is scaled as the unit circle with the positive x-axis now viewed as the polar axis and the origin as the pole. The first coordinate r is the radius or length of the directed line segment from the pole. The angle \theta , measured in radians, indicates the direction of r. We move counterclockwise from the polar axis by an angle of \theta , and measure a directed line segment the length of r in the direction of \theta . Even though we measure \theta  first and then r, the polar point is written with the r-coordinate first. For example, to plot the point ( 2,  \p\frac{i}{4}  ), we would move  \p\frac{i}{4}  units in the counterclockwise direction and then a length of 2 from the pole. This point is plotted on the grid in Figure 2. Polar Grid

**Example  1**

### Plotting a Point on the Polar Grid

Plot the point ( 3,  \p\frac{i}{2}  ) on the polar grid.

**Solution**

The angle  \p\frac{i}{2}  is found by sweeping in a counterclockwise direction 90° from the polar axis. The point is located at a length of 3 units from the pole in the  \p\frac{i}{2}  direction, as shown in Figure 3.

**Try It #1**

Plot the point ( 2,  \p\frac{i}{3}  ) in the polar grid.

**Example  2**

### Plotting a Point in the Polar Coordinate System with a Negative Component

Plot the point ( -2,  \p\frac{i}{6}  ) on the polar grid.

**Solution**

We know that  \p\frac{i}{6}  is located in the first quadrant. However, r = -2. We can approach plotting a point with a negative r in two ways: Plot the point ( 2,  \p\frac{i}{6}  ) by moving  \p\frac{i}{6}  in the counterclockwise direction and extending a directed line segment 2 units into the first quadrant. Then retrace the directed line segment back through the pole, and continue 2 units into the third quadrant; 2. Move  \p\frac{i}{6}  in the counterclockwise direction, and draw the directed line segment from the pole 2 units in the negative direction, into the third quadrant. See Figure 4(a). Compare this to the graph of the polar coordinate ( 2,  \p\frac{i}{6}  ) shown in Figure 4(b). (a) (b)

**Try It #2**

Plot the points ( 3, -  \p\frac{i}{6}  ) and ( 2,  9\p\frac{i}{4}  ) on the same polar grid.

Converting from Polar Coordinates to Rectangular Coordinates When given a set of polar coordinates, we may need to convert them to rectangular coordinates. To do so, we can recall the relationships that exist among the variables x, y, r, and \theta .

cos \theta  =  \frac{x}{r}  → x = rcos \theta 

sin \theta  =  \frac{y}{r}  → y = rsin \theta  Dropping a perpendicular from the point in the plane to the x-axis forms a right triangle, as illustrated in Figure 5. An easy way to remember the equations above is to think of cos \theta  as the adjacent side over the hypotenuse and sin \theta  as the opposite side over the hypotenuse. x r y x (x, y) or (r, \theta ) y \theta  converting from polar coordinates to rectangular coordinates To convert polar coordinates (r, \theta ) to rectangular coordinates (x, y), let

cos \theta  =  \frac{x}{r}  → x = rcos \theta 

sin \theta  =  \frac{y}{r}  → y = rsin \theta 

**How To…**

Given polar coordinates, convert to rectangular coordinates. 1. Given the polar coordinate (r, \theta ), write x = rcos \theta  and y = rsin \theta . 2. Evaluate cos \theta  and sin \theta . 3. Multiply cos \theta  by r to find the x-coordinate of the rectangular form. 4. Multiply sin \theta  by r to find the y-coordinate of the rectangular form.

**Example  3**

### Writing Polar Coordinates as Rectangular Coordinates

Write the polar coordinates ( 3,  \p\frac{i}{2}  ) as rectangular coordinates.

**Solution**

Use the equivalent relationships.

x = rcos \theta 

x = 3cos  \p\frac{i}{2}  = 0

y = rsin \theta 

y = 3sin  \p\frac{i}{2}  = 3 The rectangular coordinates are (0, 3). See Figure 6.

Polar Grid Coordinate Grid x y

**Example  4**

### Writing Polar Coordinates as Rectangular Coordinates

Write the polar coordinates (-2, 0) as rectangular coordinates.

**Solution**

See Figure 7. Writing the polar coordinates as rectangular, we have

x = rcos \theta 

x = -2cos(0) = -2

y = rsin \theta 

y = -2sin(0) = 0 The rectangular coordinates are also (-2, 0). x y

**Try It #3**

Write the polar coordinates ( -1,  2\p\frac{i}{3}  ) as rectangular coordinates. Converting from Rectangular Coordinates to Polar Coordinates To convert rectangular coordinates to polar coordinates, we will use two other familiar relationships. With this conversion, however, we need to be aware that a set of rectangular coordinates will yield more than one polar point.

converting from rectangular coordinates to polar coordinates Converting from rectangular coordinates to polar coordinates requires the use of one or more of the relationships illustrated in Figure 8.

cos \theta  =  \frac{x}{r}  or x = rcos \theta 

sin \theta  =  \frac{y}{r}  or y = rsin \theta 

r 2 = x 2 + y 2

tan \theta  =  \frac{y}{x}  x x y r (x, y), (r, \theta ) y \theta 

**Example  5**

### Writing Rectangular Coordinates as Polar Coordinates

Convert the rectangular coordinates (3, 3) to polar coordinates.

**Solution**

We see that the original point (3, 3) is in the first quadrant. To find \theta , use the formula tan \theta  =  \frac{y}{x} . This gives

tan \theta  =  \frac{3}{3} 

tan \theta  = 1

\theta  = tan-1(1)

\theta  =  \p\frac{i}{4}  To find r, we substitute the values for x and y into the formula r = \sqrt{x} 2 + y 2 . We know that r must be positive, as  \p\frac{i}{4}  is in the first quadrant. Thus

r = \sqrt{r} = \sqrt{9} + 9 

r = \sqrt{18}  = 3\sqrt{2}  So, r = 3\sqrt{2}  and \theta  =  \p\frac{i}{4} , giving us the polar point ( 3\sqrt{2} ,  \p\frac{i}{4}  ). See Figure 9. x y Analysis There are other sets of polar coordinates that will be the same as our first solution. For example, the points ( -3\sqrt{2} ,  5\pi  ___ 4  ) and ( 3\sqrt{2} , - 7\p\frac{i}{4}  ) and will coincide with the original solution of ( 3\sqrt{2} ,  \p\frac{i}{4}  ). The point ( -3\sqrt{2} ,  5\p\frac{i}{4}  ) indicates a move further counterclockwise by \pi , which is directly opposite  \p\frac{i}{4} . The radius is expressed as -3\sqrt{2} . However, the angle  5\p\frac{i}{4}  is located in the third quadrant and, as r is negative, we extend the directed line segment in the opposite direction, into the first quadrant. This is the same point as ( 3\sqrt{2} ,  \p\frac{i}{4}  ). The point ( 3\sqrt{2} , -  7\p\frac{i}{4}  ) is a move further clockwise by -  7\p\frac{i}{4} , from  \p\frac{i}{4} . The radius, 3\sqrt{2} , is the same.

Transforming Equations between Polar and Rectangular Forms We can now convert coordinates between polar and rectangular form. Converting equations can be more difficult, but it can be beneficial to be able to convert between the two forms. Since there are a number of polar equations that cannot be expressed clearly in Cartesian form, and vice versa, we can use the same procedures we used to convert points between the coordinate systems. We can then use a graphing calculator to graph either the rectangular form or the polar form of the equation.

**How To…**

Given an equation in polar form, graph it using a graphing calculator. 1. Change the MODE to POL, representing polar form. 2. Press the Y= button to bring up a screen allowing the input of six equations: r^{1}, r^{2}, ... , r^{6}. 3. Enter the polar equation, set equal to r. 4. Press GRAPH.

**Example  6**

### Writing a Cartesian Equation in Polar Form

Write the Cartesian equation x 2 + y 2 = 9 in polar form.

**Solution**

The goal is to eliminate x and y from the equation and introduce r and \theta . Ideally, we would write the equation r as a function of \theta . To obtain the polar form, we will use the relationships between (x, y) and (r, \theta ). Since x = rcos \theta  and y = rsin \theta , we can substitute and solve for r.

(rcos \theta )^{2} + (rsin \theta )^{2} = 9

r 2cos 2 \theta  + r 2 sin^{2} \theta  = 9

r 2(cos 2 \theta  + sin^{2} \theta ) = 9

r 2(1) = 9

Substitute cos 2 \theta  + sin 2 \theta  = 1.

r = \pm  3

Use the square root property. Thus, x 2 + y 2 = 9, r = 3, and r = -3 should generate the same graph. See Figure 10. (b) (a) x y To graph a circle in rectangular form, we must first solve for y.

x 2 + y 2 = 9

y 2 = 9- x 2

y = \pm  \sqrt{9} - x 2  Note that this is two separate functions, since a circle fails the vertical line test. Therefore, we need to enter the positive and negative square roots into the calculator separately, as two equations in the form Y^{1} = \sqrt{9-} x 2  and Y^{2} = -\sqrt{9-} x 2 . Press GRAPH.

**Example  7**

Rewriting a Cartesian Equation as a Polar Equation Rewrite the Cartesian equation x 2 + y 2 = 6y as a polar equation.

**Solution**

This equation appears similar to the previous example, but it requires different steps to convert the equation. We can still follow the same procedures we have already learned and make the following substitutions:

r 2 = 6y Use x 2 + y 2 = r 2.

r 2 = 6rsin \theta  Substitute y = rsin \theta .

r 2-6rsin \theta  = 0 Set equal to 0.

r (r - 6sin \theta ) = 0 Factor and solve.

r = 0 We reject r = 0, as it only represents one point, (0, 0).

or r = 6sin \theta  Therefore, the equations x 2 + y 2 = 6y and r = 6sin \theta  should give us the same graph. See Figure 11. (a) x y (b) The Cartesian or rectangular equation is plotted on the rectangular grid, and the polar equation is plotted on the polar grid. Clearly, the graphs are identical.

**Example  8**

Rewriting a Cartesian Equation in Polar Form Rewrite the Cartesian equation y = 3x + 2 as a polar equation.

**Solution**

We will use the relationships x = rcos \theta  and y = rsin \theta .

y = 3x + 2

rsin \theta  = 3rcos \theta  + 2

rsin \theta  - 3rcos \theta  = 2

r(sin \theta  - 3cos \theta ) = 2

Isolate r.

r =  __

sin \theta  - 3cos \theta   Solve for r.

**Try It #4**

Rewrite the Cartesian equation y 2 = 3 - x 2 in polar form. Identify and Graph Polar Equations by Converting to Rectangular Equations We have learned how to convert rectangular coordinates to polar coordinates, and we have seen that the points are indeed the same. We have also transformed polar equations to rectangular equations and vice versa. Now we will demonstrate that their graphs, while drawn on different grids, are identical.

**Example  9**

### Graphing a Polar Equation by Converting to a Rectangular Equation

Covert the polar equation r = 2sec \theta  to a rectangular equation, and draw its corresponding graph.

**Solution**

The conversion is

r = 2sec \theta 

r =  \frac{2}{c}os \theta  

rcos \theta  = 2

x = 2 Notice that the equation r = 2sec \theta  drawn on the polar grid is clearly the same as the vertical line x = 2 drawn on the rectangular grid (see Figure 12). Just as x = c is the standard form for a vertical line in rectangular form, r = csec \theta  is the standard form for a vertical line in polar form. r = 2 sec \theta  x = 2 (a) (b) x y A similar discussion would demonstrate that the graph of the function r = 2csc \theta  will be the horizontal line y = 2. In fact, r = ccsc \theta  is the standard form for a horizontal line in polar form, corresponding to the rectangular form y = c.

**Example  10**

Rewriting a Polar Equation in Cartesian Form Rewrite the polar equation r =  _ 1 - 2cos \theta   as a Cartesian equation.

**Solution**

The goal is to eliminate \theta  and r, and introduce x and y. We clear the fraction, and then use substitution. In order to replace r with x and y, we must use the expression x 2 + y 2 = r 2.

r =  _ 1 - 2cos \theta  

r(1 - 2cos \theta ) = 3

r ( 1 - 2(  \frac{x}{r}  ) ) = 3

Use cos \theta  =  \frac{x}{r}  to eliminate \theta .

r -2x = 3

r = 3 + 2x Isolate r.

r 2 = (3 + 2x) 2 Square both sides.

x 2 + y 2 = (3 + 2x) 2 Use x 2 + y 2 = r 2. The Cartesian equation is x 2 + y 2 = (3 + 2x) 2. However, to graph it, especially using a graphing calculator or computer program, we want to isolate y.

x 2 + y 2 = (3 + 2x) 2

y 2 = (3 + 2x) 2 - x 2

y = \pm  \sqrt{(3} + 2x) 2 - x 2  When our entire equation has been changed from r and \theta  to x and y, we can stop, unless asked to solve for y or simplify. See Figure 13.

Coordinate Grid Polar Grid x y x^{2} + y^{2} = (3 + 2x)^{2} r = 1 – 2 cos\theta  The “hour-glass” shape of the graph is called a hyperbola. Hyperbolas have many interesting geometric features and applications, which we will investigate further in Analytic Geometry.

**Analysis**
In this example, the right side of the equation can be expanded and the equation simplified further, as shown above. However, the equation cannot be written as a single function in Cartesian form. We may wish to write the rectangular equation in the hyperbola’s standard form. To do this, we can start with the initial equation.

x 2 + y 2 = (3 + 2x) 2

x 2 + y 2 - (3 + 2x) 2 = 0

x 2 + y 2 - (9 + 12x + 4x 2) = 0

x 2 + y 2 - 9 - 12x -4x 2 = 0

-3x 2 - 12x + y 2 = 9 Multiply through by -1.

3x 2 + 12x - y 2 = -9

3(x 2 + 4x + ) - y 2 = -9 + 12 Organize terms to complete the square for x.

3(x 2 + 4x + 4) - y 2 = -9 + 12

3(x + 2)^{2} - y 2 = 3

(x + 2)^{2} -  y \frac{2}{3}  = 1

**Try It #5**

Rewrite the polar equation r = 2sin \theta  in Cartesian form.

**Example  11**

Rewriting a Polar Equation in Cartesian Form Rewrite the polar equation r = sin(2\theta ) in Cartesian form.

**Solution**

r = sin(2\theta ) Use the double angle identity for sine.

r = 2sin \theta cos \theta  Use cos \theta  =  \frac{x}{r}  and sin \theta  =  \frac{y}{r} .

r = 2(  \frac{x}{r}  )(  \frac{y}{r}  ) Simplify.

r =  2x\frac{y}{r} 2  Multiply both sides by r 2.

r^{3} = 2xy

( \sqrt{x} 2 + y 2  )  = 2xy As x 2 + y 2 = r 2, r = \sqrt{x} 2 + y 2 . This equation can also be written as

(x 2 + y 2)  \frac{3}{2}  = 2xy or x 2 + y 2 = (2xy)  \frac{2}{3} . Access these online resources for additional instruction and practice with polar coordinates. • Introduction to Polar Coordinates (http://openstaxcollege.org/l/intropolar) • Comparing Polar and Rectangular Coordinates (http://openstaxcollege.org/l/polarrect)

## 8.3 Section Exercises

### 8.3 Section Exercises

Verbal 1. How are polar coordinates different from rectangular coordinates? 2. How are the polar axes different from the x- and y-axes of the Cartesian plane? 3. Explain how polar coordinates are graphed. 4. How are the points ( 3,  \p\frac{i}{2}  ) and ( -3,  \p\frac{i}{2}  ) related? 5. Explain why the points ( -3,  \p\frac{i}{2}  ) and ( 3, -  \p\frac{i}{2}  ) are the same. Algebraic For the following exercises, convert the given polar coordinates to Cartesian coordinates with r > 0 and 0 \le  \theta  \le 2\pi . Remember to consider the quadrant in which the given point is located when determining \theta  for the point. _ 6  ) 8. ( 6, -  \p\frac{i}{4}  ) 9. ( -3,  \p\frac{i}{6}  ) _ 4  ) For the following exercises, convert the given Cartesian coordinates to polar coordinates with r > 0, 0 \le  \theta  <2\pi . Remember to consider the quadrant in which the given point is located. For the following exercises, convert the given Cartesian equation to a polar equation. 20. x 2 + y 2 = 4y 21. x 2 + y 2 = 3x 22. x 2 - y 2 = x 23. x 2 - y 2 = 3y 24. x 2 + y 2 = 9 For the following exercises, convert the given polar equation to a Cartesian equation. Write in the standard form of a conic if possible, and identify the conic section represented. 28. r = 3sin \theta  29. r = 4cos \theta  30. r =  __

sin \theta  + 7cos \theta   31. r =  __

cos \theta  + 3sin \theta   32. r = 2sec \theta  33. r = 3csc \theta  34. r = \sqrt{rcos} \theta  + 2  35. r 2 = 4sec \theta  csc \theta  38. r =  __

4cos \theta  - 3sin \theta   39. r =  __

cos \theta  - 5sin \theta   Graphical For the following exercises, find the polar coordinates of the point. \pi  3\pi  \pi  \pi  3\pi  \pi  3\pi  \pi 

\pi  \pi  3\pi  \pi  3\pi  \pi  For the following exercises, plot the points. 45. ( -2,  \p\frac{i}{3}  ) 46. ( -1, -  \p\frac{i}{2}  ) _ 4  ) 48. ( -4,  \p\frac{i}{3}  ) _ 2  ) _ 4  ) _ 6  ) _ 6  ) 53. ( -2,  \p\frac{i}{4}  ) _ 2  ) For the following exercises, convert the equation from rectangular to polar form and graph on the polar axis. 55. 5x - y = 6 57. x 2 +(y - 1) 2 = 1 58. (x + 2) 2 +(y + 3) 2 = 13 60. x 2 + y 2 = 5y 61. x 2 + y 2 = 3x For the following exercises, convert the equation from polar to rectangular form and graph on the rectangular plane. 63. r = - 4 64. \theta  = -  2\p\frac{i}{3}  65. \theta  =  \p\frac{i}{4}  66. r = sec \theta  67. r = -10sin \theta  68. r = 3cos \theta  Technology 69. Use a graphing calculator to find the rectangular coordinates of ( 2, -  \p\frac{i}{5}  ). Round to the nearest thousandth. 70. Use a graphing calculator to find the rectangular coordinates of ( -3,  3\p\frac{i}{7}  ). Round to the nearest thousandth. 71. Use a graphing calculator to find the polar coordinates of (-7, 8) in degrees. Round to the nearest thousandth. 72. Use a graphing calculator to find the polar coordinates of (3, -4) in degrees. Round to the nearest hundredth. 73. Use a graphing calculator to find the polar coordinates of (-2, 0) in radians. Round to the nearest hundredth. Extensions 74. Describe the graph of r = asec \theta ; a > 0. 75. Describe the graph of r = asec \theta ; a < 0. 76. Describe the graph of r = acsc \theta ; a > 0. 77. Describe the graph of r = acsc \theta ; a < 0. 78. What polar equations will give an oblique line? For the following exercises, graph the polar inequality. 80. 0 \le  \theta  \le   \p\frac{i}{4}  81. \theta  =  \p\frac{i}{4} , r \ge  2 82. \theta  =  \p\frac{i}{4} , r \ge  -3 83. 0 \le  \theta  \le   \p\frac{i}{3} , r < 2 84. -  \p\frac{i}{6}  < \theta  \le   \p\frac{i}{3} , -3 < r < 2

## 8.4 Polar Coordinates: Graphs

Learning Objectives
In this section, you will:
• Test polar equations for symmetry.
• Graph polar equations by plotting points.
The planets move through space in elliptical, periodic orbits about the sun, as shown in Figure 1. They are in constant motion, so fixing an exact position of any planet is valid only for a moment. In other words, we can fix only a planet’s instantaneous position. This is one application of polar coordinates, represented as (r, \theta ). We interpret r as the distance from the sun and \theta  as the planet’s angular bearing, or its direction from a fixed point on the sun. In this section, we will focus on the polar system and the graphs that are generated directly from polar coordinates. Mercury Earth Venus Mars Testing Polar Equations for Symmetry Just as a rectangular equation such as y = x^{2} describes the relationship between x and y on a Cartesian grid, a polar equation describes a relationship between r and \theta  on a polar grid. Recall that the coordinate pair (r, \theta ) indicates that we move counterclockwise from the polar axis (positive x-axis) by an angle of \theta , and extend a ray from the pole (origin) r units in the direction of \theta . All points that satisfy the polar equation are on the graph. Symmetry is a property that helps us recognize and plot the graph of any equation. If an equation has a graph that is symmetric with respect to an axis, it means that if we folded the graph in half over that axis, the portion of the graph on one side would coincide with the portion on the other side. By performing three tests, we will see how to apply the properties of symmetry to polar equations. Further, we will use symmetry (in addition to plotting key points, zeros, and maximums of r) to determine the graph of a polar equation. In the first test, we consider symmetry with respect to the line \theta  =  \p\frac{i}{2} (y-axis). We replace (r, \theta ) with (-r, -\theta ) to determine if the new equation is equivalent to the original equation. For example, suppose we are given the equation r = 2sin \theta ;

r = 2sin \theta 

-r = 2sin(-\theta ) Replace (r, \theta ) with (-r, -\theta ).

-r = -2sin \theta  Identity: sin(-\theta )= -sin \theta .

r = 2sin \theta  Multiply both sides by-1. This equation exhibits symmetry with respect to the line \theta  =  \p\frac{i}{2} . In the second test, we consider symmetry with respect to the polar axis (x -axis). We replace (r, \theta ) with (r, -\theta ) or (-r, \pi  - \theta ) to determine equivalency between the tested equation and the original. For example, suppose we are given the equation r = 1 - 2cos \theta .

r = 1 - 2cos \theta 

r = 1 - 2cos(-\theta ) Replace (r, \theta ) with (r, -\theta ).

r = 1 - 2cos \theta  Even/Odd identity

The graph of this equation exhibits symmetry with respect to the polar axis. In the third test, we consider symmetry with respect to the pole (origin). We replace (r, \theta ) with (-r, \theta ) to determine if the tested equation is equivalent to the original equation. For example, suppose we are given the equation r = 2sin(3\theta ).

r = 2sin(3\theta )

-r = 2sin(3\theta ) The equation has failed the symmetry test, but that does not mean that it is not symmetric with respect to the pole. Passing one or more of the symmetry tests verifies that symmetry will be exhibited in a graph. However, failing the symmetry tests does not necessarily indicate that a graph will not be symmetric about the line \theta  =  \p\frac{i}{2} , the polar axis, or the pole. In these instances, we can confirm that symmetry exists by plotting reflecting points across the apparent axis of symmetry or the pole. Testing for symmetry is a technique that simplifies the graphing of polar equations, but its application is not perfect. symmetry tests A polar equation describes a curve on the polar grid. The graph of a polar equation can be evaluated for three types of symmetry, as shown in Figure 2. \theta  \theta  \theta  \theta  \theta  \theta  (a) (b) (c) _ 2  (y-axis) if replacing (r, \theta  ) with (-r, -\theta  ) yields an equivalent equation. (b) A graph is symmetric with respect to the polar axis (x-axis) if replacing (r, \theta ) with (r, -\theta  ) or (-r, \pi -\theta  ) yields an equivalent equation. (c) A graph is symmetric with respect to the pole (origin) if replacing (r, \theta  ) with (-r, \theta  ) yields an equivalent equation.

**How To…**

Given a polar equation, test for symmetry. 1. Substitute the appropriate combination of components for (r, \theta ): (-r,- \theta ) for \theta  =  \p\frac{i}{2}  symmetry; (r,- \theta ) for polar axis symmetry; and (-r, \theta ) for symmetry with respect to the pole. 2. If the resulting equations are equivalent in one or more of the tests, the graph produces the expected symmetry.

**Example  1**

Testing a Polar Equation for Symmetry Test the equation r = 2sin \theta  for symmetry.

**Solution**

Test for each of the three types of symmetry. 1) Replacing (r, \theta ) with (-r, -\theta ) yields the same result. Thus, the graph is symmetric with respect to the line \theta  =  \p\frac{i}{2} .

-r = 2sin(-\theta )

-r = -2sin \theta  Even-odd identity

r = 2sin \theta  Multiply by -1 Passed 2) Replacing \theta  with -\theta  does not yield the same equation. Therefore, the graph fails the test and may or may not be symmetric with respect to the polar axis.

r = 2sin(-\theta )

r = -2sin \theta  Even-odd identity

r = -2sin \theta  \neq  2sin \theta  Failed 3) Replacing r with -r changes the equation and fails the test. The graph may or may not be symmetric with respect to the pole.

-r = 2sin \theta  r = -2sin \theta  \neq  2sin \theta  Failed

**Analysis**
Using a graphing calculator, we can see that the equation r = 2sin \theta  is a circle centered at (0, 1) with radius \pi  r = 1 and is indeed symmetric to the line \theta  =  \p\frac{i}{2} . We can also see that the graph is not symmetric with the polar axis or the pole. See Figure 3.

**Try It #1**

Test the equation for symmetry: r = - 2cos \theta . Graphing Polar Equations by Plotting Points To graph in the rectangular coordinate system we construct a table of x and y values. To graph in the polar coordinate system we construct a table of \theta  and r values. We enter values of \theta  into a polar equation and calculate r. However, using the properties of symmetry and finding key values of \theta  and r means fewer calculations will be needed. Finding Zeros and Maxima To find the zeros of a polar equation, we solve for the values of \theta  that result in r = 0. Recall that, to find the zeros of polynomial functions, we set the equation equal to zero and then solve for x. We use the same process for polar equations. Set r = 0, and solve for \theta . For many of the forms we will encounter, the maximum value of a polar equation is found by substituting those values of \theta  into the equation that result in the maximum value of the trigonometric functions. Consider r = 5cos \theta ; the maximum distance between the curve and the pole is 5 units. The maximum value of the cosine function is 1 when \theta  = 0, so our polar equation is 5cos \theta , and the value \theta  = 0 will yield the maximum | r |. Similarly, the maximum value of the sine function is 1 when \theta  =  \p\frac{i}{2} , and if our polar equation is r = 5sin \theta , the value \theta  =  \p\frac{i}{2}  will yield the maximum | r |. We may find additional information by calculating values of r when \theta  = 0. These points would be polar axis intercepts, which may be helpful in drawing the graph and identifying the curve of a polar equation.

**Example  2**

### Finding Zeros and Maximum Values for a Polar Equation

Using the equation in Example 1, find the zeros and maximum | r | and, if necessary, the polar axis intercepts of r = 2sin \theta .

**Solution**

To find the zeros, set r equal to zero and solve for \theta .

2sin \theta  = 0

sin \theta  = 0

\theta  = sin-1 0

\theta  = n\pi 

where n is an integer Substitute any one of the \theta  values into the equation. We will use 0.

r = 2sin(0)

r =0 The points (0, 0) and (0, \pm  n\pi ) are the zeros of the equation. They all coincide, so only one point is visible on the graph. This point is also the only polar axis intercept.

To find the maximum value of the equation, look at the maximum value of the trigonometric function sin \theta , which occurs when \theta  =  \p\frac{i}{2}  \pm  2k\pi  resulting in sin(  \p\frac{i}{2}  ) = 1. Substitute  \p\frac{i}{2}  for \theta .

r = 2sin(  \p\frac{i}{2}  )

r = 2(1)

r = 2 Analysis The point ( 2,  \p\frac{i}{2}  ) will be the maximum value on the graph. Let’s plot a few more points to verify the graph of a circle. See Table 2 and Figure 4. \theta  r = 2sin \theta  r r = 2sin(0) = 0  \p\frac{i}{6}  r = 2sin(  \p\frac{i}{6}  ) = 1  \p\frac{i}{3}  r = 2sin(  \p\frac{i}{1}.73  \p\frac{i}{2}  r = 2sin(  \p\frac{i}{2}  )= 2  2\p\frac{i}{3}  r = 2sin(  2\p\frac{i}{1}.73  5\p\frac{i}{6}  r = 2sin(  5\p\frac{i}{6}  )= 1 \pi  r = 2sin(\pi ) = 0

**Try It #2**

Without converting to Cartesian coordinates, test the given equation for symmetry and find the zeros and maximum values of | r |: r = 3cos \theta . Investigating Circles Now we have seen the equation of a circle in the polar coordinate system. In the last two examples, the same equation was used to illustrate the properties of symmetry and demonstrate how to find the zeros, maximum values, and plotted points that produced the graphs. However, the circle is only one of many shapes in the set of polar curves. There are five classic polar curves: cardioids, limaçons, lemniscates, rose curves, and Archimedes’ spirals. We will briefly touch on the polar formulas for the circle before moving on to the classic curves and their variations.

formulas for the equation of a circle Some of the formulas that produce the graph of a circle in polar coordinates are given by r = acos \theta  and r = asin \theta , where a is the diameter of the circle or the distance from the pole to the farthest point on the circumference. The radius is  | a | _ 2 , or one-half the diameter. For r = acos \theta , the center is (  \frac{a}{2} , 0 ). For r = asin \theta , the center is (  \frac{a}{2} , \pi  ). r = acos \theta , a > 0 r = acos \theta , a < 0 r = asin \theta , a > 0 r = asin \theta , a < 0 (a) (b) (c) (d)

**Example  3**

### Sketching the Graph of a Polar Equation for a Circle

Sketch the graph of r = 4cos \theta .

**Solution**

First, testing the equation for symmetry, we find that the graph is symmetric about the polar axis. Next, we find the zeros and maximum | r | for r = 4cos \theta . First, set r = 0, and solve for \theta  . Thus, a zero occurs at \theta  =  \p\frac{i}{2}  \pm  k\pi . A key point to plot is ( 0,  \p\frac{i}{2}  ) To find the maximum value of r, note that the maximum value of the cosine function is 1 when \theta  = 0 \pm  2k\pi . Substitute \theta  = 0 into the equation:

r = 4cos \theta 

r = 4cos(0)

r = 4(1) = 4 The maximum value of the equation is 4. A key point to plot is (4, 0). As r = 4cos \theta  is symmetric with respect to the polar axis, we only need to calculate r-values for \theta  over the interval [0, \pi ]. Points in the upper quadrant can then be reflected to the lower quadrant. Make a table of values similar to Table 3. The graph is shown in Figure 6. \theta   \p\frac{i}{6}   \p\frac{i}{4}   \p\frac{i}{3}   \p\frac{i}{2}   2\p\frac{i}{3}   3\p\frac{i}{4}   5\p\frac{i}{6}  \pi  r 3.46 2.83 -2 -2.83 -3.46

### Investigating Cardioids

While translating from polar coordinates to Cartesian coordinates may seem simpler in some instances, graphing the classic curves is actually less complicated in the polar system. The next curve is called a cardioid, as it resembles a heart. This shape is often included with the family of curves called limaçons, but here we will discuss the cardioid on its own. formulas for a cardioid The formulas that produce the graphs of a cardioid are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  where a > 0, b > 0, and  \frac{a}{b}  = 1. The cardioid graph passes through the pole, as we can see in Figure 7. r = a + bcos\theta  r = a - bcos\theta  r = a + bsin\theta  r = a - bsin\theta  (a) (b) (c) (d)

**How To…**

Given the polar equation of a cardioid, sketch its graph. 1. Check equation for the three types of symmetry. 2. Find the zeros. Set r = 0. 3. Find the maximum value of the equation according to the maximum value of the trigonometric expression. 4. Make a table of values for r and \theta . 5. Plot the points and sketch the graph.

**Example  4**

### Sketching the Graph of a Cardioid

Sketch the graph of r = 2 + 2cos \theta .

**Solution**

First, testing the equation for symmetry, we find that the graph of this equation will be symmetric about the polar axis. Next, we find the zeros and maximums. Setting r = 0, we have \theta  = \pi  +2k\pi . The zero of the equation is located at (0, \pi ). The graph passes through this point. The maximum value of r = 2 + 2cos \theta  occurs when cos \theta  is a maximum, which is when cos \theta  =1 or when \theta  = 0. Substitute \theta  =0 into the equation, and solve for r.

r = 2 + 2cos(0)

r = 2 + 2(1) = 4 The point (4, 0) is the maximum value on the graph. We found that the polar equation is symmetric with respect to the polar axis, but as it extends to all four quadrants, we need to plot values over the interval [0, \pi ]. The upper portion of the graph is then reflected over the polar axis. Next, we make a table of values, as in Table 4, and then we plot the points and draw the graph. See Figure 8. \theta   \p\frac{i}{4}   \p\frac{i}{2}   2\p\frac{i}{3}  \pi  r 3.41

) Investigating Limaçons The word limaçon is Old French for “snail,” a name that describes the shape of the graph. As mentioned earlier, the cardioid is a member of the limaçon family, and we can see the similarities in the graphs. The other images in this category include the one-loop limaçon and the two-loop (or inner-loop) limaçon. One-loop limaçons are sometimes referred to as dimpled limaçons when 1 <  \frac{a}{b}  < 2 and convex limaçons when  \frac{a}{b}  \ge  2. formulas for one-loop limaçons The formulas that produce the graph of a dimpled one-loop limaçon are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  where a > 0, b > 0, and 1 <  \frac{a}{b}  < 2. All four graphs are shown in Figure 9. r = a + bcos\theta  (a) r = a - bcos\theta  (b) r = a + bsin\theta  (c) r = a - bsin\theta  (d)

**How To…**

Given a polar equation for a one-loop limaçon, sketch the graph. 1. Test the equation for symmetry. Remember that failing a symmetry test does not mean that the shape will not exhibit symmetry. Often the symmetry may reveal itself when the points are plotted. 2. Find the zeros. 3. Find the maximum values according to the trigonometric expression. 4. Make a table. 5. Plot the points and sketch the graph.

**Example  5**

### Sketching the Graph of a One-Loop Limaçon

Graph the equation r = 4 - 3sin \theta .

**Solution**

First, testing the equation for symmetry, we find that it fails all three symmetry tests, meaning that the graph may or may not exhibit symmetry, so we cannot use the symmetry to help us graph it. However, this equation has a graph that clearly displays symmetry with respect to the line \theta  =  \p\frac{i}{2} , yet it fails all the three symmetry tests. A graphing calculator will immediately illustrate the graph’s reflective quality. Next, we find the zeros and maximum, and plot the reflecting points to verify any symmetry. Setting r =0 results in \theta  being undefined. What does this mean? How could \theta  be undefined? The angle \theta  is undefined for any value of sin \theta  > 1. Therefore, \theta  is undefined because there is no value of \theta  for which sin \theta  > 1. Consequently, the graph does not pass

through the pole. Perhaps the graph does cross the polar axis, but not at the pole. We can investigate other intercepts by calculating r when \theta  = 0.

r(0) = 4 - 3sin(0)

r = 4-3 ⋅ 0 = 4 So, there is at least one polar axis intercept at (4, 0). Next, as the maximum value of the sine function is 1 when \theta  =  \p\frac{i}{2} , we will substitute \theta  =  \p\frac{i}{2}  into the equation and solve for r. Thus, r = 1. Make a table of the coordinates similar to Table 5. \theta   \p\frac{i}{6}   \p\frac{i}{3}   \p\frac{i}{2}   2\p\frac{i}{3}   5\p\frac{i}{6}  \pi   7\p\frac{i}{6}   4\p\frac{i}{3}   3\p\frac{i}{2}   5\p\frac{i}{3}   11\p\frac{i}{6}  2\pi  r 2.5 1.4 1.4 2.5 5.5 6.6 6.6 5.5 The graph is shown in Figure 10. )

**Analysis**
This is an example of a curve for which making a table of values is critical to producing an accurate graph. The symmetry tests fail; the zero is undefined. While it may be apparent that an equation involving sin \theta  is likely symmetric with respect to the line \theta  =  \p\frac{i}{2} , evaluating more points helps to verify that the graph is correct.

**Try It #3**

Sketch the graph of r = 3 - 2cos \theta . Another type of limaçon, the inner-loop limaçon, is named for the loop formed inside the general limaçon shape. It was discovered by the German artist Albrecht Dürer(1471-1528), who revealed a method for drawing the inner-loop limaçon in his 1525 book Underweysung der Messing. A century later, the father of mathematician Blaise Pascal, Étienne Pascal(1588-1651), rediscovered it. formulas for inner-loop limaçons The formulas that generate the inner-loop limaçons are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  where a > 0, b > 0, and a < b. The graph of the inner-loop limaçon passes through the pole twice: once for the outer loop, and once for the inner loop. See Figure 11 for the graphs. r = a + bcos\theta , a < b (a) r = a - bcos\theta , a < b (b) r = a + bsin\theta , a < b (c) r = a - bsin\theta , a < b (d)

**Example  6**

### Sketching the Graph of an Inner-Loop Limaçon

Sketch the graph of r = 2 + 5cos \theta .

**Solution**

Testing for symmetry, we find that the graph of the equation is symmetric about the polar axis. Next, finding the zeros reveals that when r = 0, \theta  = 1.98. The maximum | r | is found when cos \theta  =1 or when \theta  = 0. Thus, the maximum is found at the point (7, 0). Even though we have found symmetry, the zero, and the maximum, plotting more points will help to define the shape, and then a pattern will emerge. See Table 6. \theta   \p\frac{i}{6}   \p\frac{i}{3}   \p\frac{i}{2}   2\pi  ___ 3   5\pi  ___ 6  \pi   7\pi  ___ 6   4\pi  ___ 3   3\pi  ___ 2   5\pi  ___ 3   11\pi  ____ 6  2\pi  r 6.3 4.5 -0.5 -2.3 -3 -2.3 -0.5 4.5 6.3 As expected, the values begin to repeat after \theta  = \pi . The graph is shown in Figure 12. (-3, \pi ) Investigating Lemniscates The lemniscate is a polar curve resembling the infinity symbol \infty  or a figure 8. Centered at the pole, a lemniscate is symmetrical by definition. formulas for lemniscates The formulas that generate the graph of a lemniscate are given by r^{2} = a^{2} cos 2\theta  and r^{2} = a^{2} sin 2\theta  where a \neq  0. The formula r^{2} = a^{2} sin 2\theta  is symmetric with respect to the pole. The formula r^{2} = a^{2} cos 2\theta  is symmetric with respect to the pole, the line \theta  =  \p\frac{i}{2} , and the polar axis. See Figure 13 for the graphs. r^{2} = a^{2}cos(2\theta ) r^{2} = -a^{2}cos(2\theta ) r^{2} = a^{2}sin(2\theta ) r^{2} = -a^{2}sin(2\theta ) (a) (b) (c) (d)

**Example  7**

### Sketching the Graph of a Lemniscate

Sketch the graph of r^{2} = 4cos 2\theta .

**Solution**

The equation exhibits symmetry with respect to the line \theta  =  \p\frac{i}{2} , the polar axis, and the pole. Let’s find the zeros. It should be routine by now, but we will approach this equation a little differently by making the substitution u = 2\theta .

0 = 4cos 2\theta 

0 = 4cos u

0 = cos u

cos-1 0 =  \p\frac{i}{2} 

u =  \p\frac{i}{2}  Substitute 2\theta  back in for u.

2\theta  =  \p\frac{i}{2} 

\theta  =  \p\frac{i}{4}  So, the point ( 0,  \p\frac{i}{4}  ) is a zero of the equation. Now let’s find the maximum value. Since the maximum of cos u = 1 when u = 0, the maximum cos 2\theta  = 1 when 2\theta  = 0. Thus,

r^{2} = 4cos(0)

r^{2} = 4(1) = 4

r = \pm  \sqrt{4}  = 2 We have a maximum at (2, 0). Since this graph is symmetric with respect to the pole, the line \theta  =  \p\frac{i}{2} , and the polar axis, we only need to plot points in the first quadrant. Make a table similar to Table 7. \theta   \p\frac{i}{6}   \p\frac{i}{4}   \p\frac{i}{3}   \p\frac{i}{2}  r \sqrt{2}  \sqrt{2}  Plot the points on the graph, such as the one shown in Figure 14.

**Analysis**
Making a substitution such as u = 2\theta  is a common practice in mathematics because it can make calculations simpler. However, we must not forget to replace the substitution term with the original term at the end, and then solve for the unknown. Some of the points on this graph may not show up using the Trace function on the TI-84 graphing calculator, and the calculator table may show an error for these same points of r. This is because there are no real square roots for these values of \theta . In other words, the corresponding r-values of \sqrt{4cos(2\theta} )  are complex numbers because there is a negative number under the radical. Investigating Rose Curves The next type of polar equation produces a petal-like shape called a rose curve. Although the graphs look complex, a simple polar equation generates the pattern.

rose curves The formulas that generate the graph of a rose curve are given by r = acos n\theta  and r = asin n\theta  where a \neq  0. If n is even, the curve has 2n petals. If n is odd, the curve has n petals. See Figure 15. r = acos(n\theta ), n even (a) r = asin(n\theta ), n odd (b)

**Example  8**

### Sketching the Graph of a Rose Curve (n Even)

Sketch the graph of r = 2cos 4\theta .

**Solution**

Testing for symmetry, we find again that the symmetry tests do not tell the whole story. The graph is not only symmetric with respect to the polar axis, but also with respect to the line \theta  =  \p\frac{i}{2}  and the pole. Now we will find the zeros. First make the substitution u = 4\theta .

0 = 2cos 4\theta 

0 = cos 4\theta 

0 = cos u

cos-1 0 = u

u =  \p\frac{i}{2} 

4\theta  =  \p\frac{i}{2} 

\theta  =  \p\frac{i}{8}  The zero is \theta  =  \p\frac{i}{8} . The point ( 0,  \p\frac{i}{8}  ) is on the curve. Next, we find the maximum | r |. We know that the maximum value of cos u = 1 when \theta  = 0. Thus,

r = 2cos(4 ⋅ 0)

r = 2cos(0)

r = 2(1) = 2 The point (2, 0) is on the curve. The graph of the rose curve has unique properties, which are revealed in Table 8. \theta   \p\frac{i}{8}   \p\frac{i}{4}   3\p\frac{i}{8}   \p\frac{i}{2}   5\p\frac{i}{8}   3\p\frac{i}{4}  r -2 -2 As r = 0 when \theta  =  \p\frac{i}{8} , it makes sense to divide values in the table by  \p\frac{i}{8}  units. A definite pattern emerges. Look at the range of r-values: 2, 0, -2, 0, 2, 0, -2, and so on. This represents the development of the curve one petal at a time. Starting at r = 0, each petal extends out a distance of r = 2, and then turns back to zero 2n times for a total of eight petals. See the graph in Figure 16.

n = 4 a

**Analysis**
When these curves are drawn, it is best to plot the points in order, as in the Table 8. This allows us to see how the graph hits a maximum (the tip of a petal), loops back crossing the pole, hits the opposite maximum, and loops back to the pole. The action is continuous until all the petals are drawn.

**Try It #4**

Sketch the graph of r = 4sin(2\theta ).

**Example  9**

### Sketching the Graph of a Rose Curve ( n Odd)

Sketch the graph of r = 2sin(5\theta ).

**Solution**

The graph of the equation shows symmetry with respect to the line \theta  =  \p\frac{i}{2} . Next, find the zeros and maximum. We will want to make the substitution u = 5\theta .

0 = 2sin(5\theta )

0 = sin u

sin-1 0 = 0

u = 0

5\theta  = 0

\theta  = 0 The maximum value is calculated at the angle where sin \theta  is a maximum. Therefore,

r = 2sin( 5 ⋅  \p\frac{i}{2}  )

r = 2(1) = 2 Thus, the maximum value of the polar equation is 2. This is the length of each petal. As the curve for n odd yields the same number of petals as n, there will be five petals on the graph. See Figure 17. a Create a table of values similar to Table 9. \theta   \p\frac{i}{6}   \p\frac{i}{3}   \p\frac{i}{2}   2\p\frac{i}{3}   5\p\frac{i}{6}  \pi  r -1.73 -1.73

**Try It #5**

Sketch the graph of r = 3cos(3\theta ). Investigating the Archimedes’ Spiral The final polar equation we will discuss is the Archimedes’ spiral, named for its discoverer, the Greek mathematician Archimedes (c. 287 BCE–c. 212 BCE), who is credited with numerous discoveries in the fields of geometry and mechanics. Archimedes’ spiral The formula that generates the graph of the Archimedes’ spiral is given by r = \theta  for \theta  \ge  0. As \theta  increases, r increases at a constant rate in an ever-widening, never-ending, spiraling path. See Figure 18. r = \theta , [0, 2\pi ] (a) r = \theta , [0, 4\pi ] (b)

**How To…**

Given an Archimedes’ spiral over [0, 2\pi ], sketch the graph. 1. Make a table of values for r and \theta  over the given domain. 2. Plot the points and sketch the graph.

**Example  10**

### Sketching the Graph of an Archimedes’ Spiral

Sketch the graph of r = \theta  over [0, 2\pi ].

**Solution**

As r is equal to \theta , the plot of the Archimedes’ spiral begins at the pole at the point (0, 0). While the graph hints of symmetry, there is no formal symmetry with regard to passing the symmetry tests. Further, there is no maximum value, unless the domain is restricted. Create a table such as Table 10. \theta   \p\frac{i}{4}   \p\frac{i}{2}  \pi   3\p\frac{i}{2}   7\p\frac{i}{4}  2\pi  r 0.785 1.57 3.14 4.71 5.50 6.28 Notice that the r-values are just the decimal form of the angle measured in radians. We can see them on a graph in (\pi , \pi )

**Analysis**
The domain of this polar curve is [0, 2\pi ]. In general, however, the domain of this function is (-\infty , \infty ). Graphing the equation of the Archimedes’ spiral is rather simple, although the image makes it seem like it would be complex.

**Try It #6**

Sketch the graph of r = -\theta  over the interval [0, 4\pi ]. Summary of Curves We have explored a number of seemingly complex polar curves in this section. Figure 20 and Figure 21 summarize the graphs and equations for each of these curves. r = asin \theta  r = acos \theta  r = a \pm  bcos \theta  r = a \pm  bsin \theta  r = a \pm  bcos \theta  r = a \pm  bsin \theta  r = a \pm  bcos \theta  r = a \pm  bsin \theta  a > 0, b > 0, a < b a > 0, b > 0, 1 < a/b < 2 a > 0, b > 0, a/b = 1 (a) Circle Cardioid One-Loop Limaçon Inner-Loop Limaçon (b) (c) (d) r^{2} = a^{2}cos 2\theta  r^{2} = a^{2}sin 2\theta  a \neq  0 (a) Lemniscate Rose Curve (n even) Rose Curve (n odd) Archimedes’ Spiral r = acos n\theta  r = asin n\theta  n even, 2n petals (b) n odd, n petals r = acos n\theta  r = asin n\theta  (c) r = \theta  \theta  \ge  0 (d) Access these online resources for additional instruction and practice with graphs of polar coordinates. • Graphing Polar Equations Part 1 (http://openstaxcollege.org/l/polargraph^{1}) • Graphing Polar Equations Part 2 (http://openstaxcollege.org/l/polargraph^{2}) • Animation: The Graphs of Polar Equations (http://openstaxcollege.org/l/polaranim) • Graphing Polar Equations on the TI-84 (http://openstaxcollege.org/l/polarTI^{8}4)

## 8.4 Section Exercises

### 8.4 Section Exercises

Verbal 1. Describe the three types of symmetry in polar graphs, and compare them to the symmetry of the Cartesian plane. 2. Which of the three types of symmetries for polar graphs correspond to the symmetries with respect to the x-axis, y-axis, and origin? 3. What are the steps to follow when graphing polar equations? 4. Describe the shapes of the graphs of cardioids, limaçons, and lemniscates. 5. What part of the equation determines the shape of the graph of a polar equation? Graphical For the following exercises, test the equation for symmetry. 6. r = 5cos 3\theta  7. r = 3 - 3cos \theta  8. r = 3 + 2sin \theta  9. r = 3sin 2\theta  12. r = 4cos  \thet\frac{a}{2}  13. r =  2 _ \theta   14. r = 3\sqrt{1-cos^{2}\theta}   15. r = \sqrt{5sin} 2\theta   For the following exercises, graph the polar equation. Identify the name of the shape. 16. r = 3cos \theta  17. r = 4sin \theta  18. r = 2 + 2cos \theta  19. r = 2 - 2cos \theta  20. r = 5 - 5sin \theta  21. r = 3 + 3sin \theta  22. r = 3 + 2sin \theta  23. r = 7 + 4sin \theta  24. r = 4 + 3cos \theta  25. r = 5 + 4cos \theta  26. r = 10 + 9cos \theta  27. r = 1 + 3sin \theta  28. r = 2 + 5sin \theta  29. r = 5 + 7sin \theta  30. r = 2 + 4cos \theta  31. r = 5 + 6cos \theta  32. r 2 = 36cos(2\theta ) 33. r 2 = 10cos(2\theta ) 34. r 2 = 4sin(2\theta ) 35. r 2 = 10sin(2\theta ) 36. r = 3sin(2\theta ) 37. r = 3cos(2\theta ) 38. r = 5sin(3\theta ) 39. r = 4sin(4\theta ) 40. r = 4sin(5\theta ) 41. r = -\theta  43. r = - 3\theta  Technology For the following exercises, use a graphing calculator to sketch the graph of the polar equation. 44. r =  1 _ \theta   45. r =  1 _ \sqrt{\theta}    46. r = 2sin \theta  tan \theta , a cissoid 47. r = 2\sqrt{1} - sin^{2} \theta  , a hippopede 48. r = 5 + cos(4\theta ) 49. r = 2 - sin(2\theta ) 51. r = \theta  + 1 52. r = \theta sin \theta  53. r = \theta cos \theta  For the following exercises, use a graphing utility to graph each pair of polar equations on a domain of [0, 4\pi ] and then explain the differences shown in the graphs. 54. r = \theta , r = -\theta  55. r = \theta , r = \theta  + sin \theta  56. r = sin \theta  + \theta , r = sin \theta  - \theta  57. r = 2sin(  \thet\frac{a}{2}  ), r = \theta sin(  \thet\frac{a}{2}  ) 58. r = sin(cos(3\theta )) r = sin(3\theta )

59. On a graphing utility, graph r = sin(  \frac{16}{5} \theta  ) on [0, 4\pi ], [0, 8\pi ], [0, 12\pi ], and [0, 16\pi ]. Describe the effect of increasing the width of the domain. 60. On a graphing utility, graph and sketch r = sin \theta  + ( sin (  \frac{5}{2} \theta  ) ) 61. On a graphing utility, graph each polar equation. Explain the similarities and differences you observe in the graphs. r^{1} = 3sin(3\theta ) r^{2} = 2sin(3\theta ) r^{3} = sin(3\theta ) 62. On a graphing utility, graph each polar equation. Explain the similarities and differences you observe in the graphs. r^{1} = 3 + 3cos \theta  r^{2} = 2 + 2cos \theta  r^{3} = 1 + cos \theta  63. On a graphing utility, graph each polar equation. Explain the similarities and differences you observe in the graphs.

r^{1} = 3\theta 

r^{2} = 2\theta 

r^{3} = \theta  Extensions For the following exercises, draw each polar equation on the same set of polar axes, and find the points of intersection. 64. r^{1} = 3 + 2sin \theta , r^{2} = 2 65. r^{1} = 6 - 4cos \theta , r^{2} = 4 66. r^{1} = 1 + sin \theta , r^{2} = 3sin \theta  67. r^{1} = 1 + cos \theta , r^{2} = 3cos \theta  68. r^{1} = cos(2\theta ), r^{2} = sin(2\theta ) 69. r^{1} = sin^{2} (2\theta ), r^{2} = 1 - cos(4\theta ) 70. r^{1} = \sqrt{3} , r^{2} = 2sin(\theta ) 2 = sin \theta , r^{2} 2 = cos \theta  72. r^{1} = 1 + cos \theta , r^{2} = 1 - sin \theta 

