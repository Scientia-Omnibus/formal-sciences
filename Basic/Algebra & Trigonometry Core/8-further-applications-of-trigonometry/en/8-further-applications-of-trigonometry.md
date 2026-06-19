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

Knowing how to approach each of these situations enables us to solve oblique triangles without having to drop a perpendicular to form two right triangles. Instead, we can use the fact that the ratio of the measurement of one of the angles to the length of its opposite side will be equal to the other two ratios of angle measure to opposite side. Let’s see how this statement is derived by considering the triangle shown in Figure 5. \gamma  \beta  \alpha  a b c h Using the right triangle relationships, we know that sin \alpha  =  h _ b  and sin \beta  =  h _ a . Solving both equations for h gives two different expressions for h.

h = bsin \alpha  and h = asin \beta  We then set the expressions equal to each other.

bsin \alpha  = asin \beta 

  1 _ ab  (bsin \alpha ) = (asin \beta )  1 _ ab   Multiply both sides by  1 _ ab .

 sin \alpha  _ a  =  sin \beta  _ b  Similarly, we can compare the other ratios.

 sin \alpha  _ a  =  sin \gamma  _ c  and  sin \beta  _ b  =  sin \gamma  _ c  Collectively, these relationships are called the Law of Sines.

 sin \alpha  _ a  =  sin \beta  _ b  =  sin \gamma  _ c  Note the standard way of labeling triangles: angle \alpha  (alpha) is opposite side a; angle \beta  (beta) is opposite side b; and angle \gamma  (gamma) is opposite side c. See Figure 6. While calculating angles and sides, be sure to carry the exact values through to the final answer. Generally, final answers are rounded to the nearest tenth, unless otherwise specified. \gamma  \beta  \alpha  a b c Law of Sines Given a triangle with angles and opposite sides labeled as in Figure 6, the ratio of the measurement of an angle to the length of its opposite side will be equal to the other two ratios of angle measure to opposite side. All proportions will be equal. The Law of Sines is based on proportions and is presented symbolically two ways.

 sin \alpha  _ a  =  sin \beta  _ b  =  sin \gamma  _ c 

 a _ sin \alpha   =  b _ sin \beta   =  c _ sin \gamma   To solve an oblique triangle, use any pair of applicable ratios.


**Example  1**

### Solving for Two Unknown Sides and Angle of an AAS Triangle
Solve the triangle shown in Figure 7 to the nearest tenth. \gamma  \alpha  b 50° 30° c \beta  Solution The three angles must add up to 180 degrees. From this, we can determine that

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
Solve the triangle in Figure 10 for the missing side and find the missing angle measures to the nearest tenth. \gamma  \alpha  35° \beta  Solution Use the Law of Sines to find angle \beta  and angle \gamma , and then side c. Solving for \beta , we have the proportion

 sin \alpha  _ a  =  sin \beta  _ b 

 sin(35°) _  =  sin \beta  _ 8 

 8sin(35°) _  = sin \beta 

However, in the diagram, angle \beta  appears to be an obtuse angle and may be greater than 90°. How did we get an acute angle, and how do we find the measurement of \beta ? Let’s investigate further. Dropping a perpendicular from \gamma  and viewing the triangle from a right angle perspective, we have Figure 11. It appears that there may be a second triangle that will fit the given criteria. \gamma ' \beta ' \beta  \phi  \alpha ' 35° The angle supplementary to \beta  is approximately equal to 49.9°, which means that \beta  = 180° - 49.9° = 130.1°. (Remember that the sine function is positive in both the first and second quadrants.) Solving for \gamma , we have

We can then use these measurements to solve the other triangle. Since \gamma ' is supplementary to \alpha  and \beta , we have

Now we need to find c and c'. We have

 c _ sin(14.9°)  =  _ sin(35°) 

c =  6sin(14.9°) _ sin(35°)  ≈ 2.7 Finally,

 c' _ sin(95.1°)  =  _ sin(35°) 

c' =  6sin(95.1°) _ sin(35°)  ≈ 10.4 To summarize, there are two triangles with an angle of 35°, an adjacent side of 8, and an opposite side of 6, as shown in Figure 12. \gamma  \beta  \alpha  35° 14.9° b = 8 a = 6 \gamma ' \beta ' \alpha ' b' = 8 a' = 6 95.1° 49.9° 35° (a) (b) However, we were looking for the values for the triangle with an obtuse angle \beta . We can see them in the first triangle (a) in Figure 12.

**Try It #2**
Given \alpha  = 80°, a = 120, and b = 121, find the missing side and angles. If there is more than one possible solution, show both.

**Example  3**

### Solving for the Unknown Sides and Angles of a SSA Triangle
In the triangle shown in Figure 13, solve for the unknown side and angles. Round your answers to the nearest tenth. \alpha  85° \beta  a Solution In choosing the pair of ratios from the Law of Sines to use, look at the information given. In this case, we know the angle \gamma  = 85°, and its corresponding side c = 12, and we know side b = 9. We will use this proportion to solve for \beta .

 sin(85°) _  =  sin \beta  _ 9  Isolate the unknown.

 9sin(85°) _  = sin \beta 

To find \beta , apply the inverse sine function. The inverse sine will produce a single result, but keep in mind that there may be two values for \beta . It is important to verify the result, as there may be two viable solutions, only one solution (the usual case), or no solutions.

\beta  = sin-1   9sin(85°) _  

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
Finding the Triangles That Meet the Given Criteria Find all possible triangles if one side has length 4 opposite an angle of 50°, and a second side has length 10. Solution Using the given information, we can solve for the angle opposite the side of length 10. See Figure 14.

 sin \alpha  _ 10  =  sin(50°) _ 

sin \alpha  =  10sin(50°) _________ 

\alpha  50° We can stop here without finding the value of \alpha . Because the range of the sine function is [-1, 1], it is impossible for the sine value to be 1.915. In fact, inputting sin-1 (1.915) in a graphing calculator generates an ERROR DOMAIN. Therefore, no triangles can be drawn with the provided dimensions.

**Try It #4**
Determine the number of triangles possible given a = 31, b = 26, \beta  = 48°.

Finding the Area of an Oblique Triangle Using the Sine Function Now that we can solve a triangle for missing values, we can use some of those values and the sine function to find the area of an oblique triangle. Recall that the area formula for a triangle is given as Area =  1 _ 2 bh, where b is base and h is height. For oblique triangles, we must find h before we can use the area formula. Observing the two triangles in Figure 15, one acute and one obtuse, we can drop a perpendicular to represent the height and then apply the trigonometric property sin \alpha  =  opposite _ hypotenuse  to write an equation for area in oblique triangles. In the acute triangle, we have sin \alpha  =  h _ c  or csin \alpha  = h. However, in the obtuse triangle, we drop the perpendicular outside the triangle and extend the base b to form a right triangle. The angle used in calculation is \alpha ', or 180 - \alpha . \gamma  \gamma  \beta  \beta  \alpha  \alpha  \alpha ' b b a a c c h h Thus,

Area =  1 _ 2 (base)(height) =  1 _ 2 b(csin \alpha ) Similarly,

Area =  1 _ 2 a(bsin \gamma ) =  1 _ 2 a(csin \beta ) area of an oblique triangle The formula for the area of an oblique triangle is given by

Area =  1 _ 2 bcsin \alpha 

=  1 _ 2 acsin \beta 

=  1 _ 2 absin \gamma  This is equivalent to one-half of the product of two sides and the sine of their included angle.

**Example  5**
Finding the Area of an Oblique Triangle Find the area of a triangle with sides a = 90, b = 52, and angle \gamma  = 102°. Round the area to the nearest integer. Solution Using the formula, we have

Area =  1 _ 2 absin \gamma 

Area =  1 _

Area ≈ 2289 square units

**Try It #5**
Find the area of the triangle given \beta  = 42°, a = 7.2 ft, c = 3.4 ft. Round the area to the nearest tenth. Solving Applied Problems Using the Law of Sines The more we study trigonometric applications, the more we discover that the applications are countless. Some are flat, diagram-type situations, but many applications in calculus, engineering, and physics involve three dimensions and motion.


**Example  6**
Finding an Altitude Find the altitude of the aircraft in the problem introduced at the beginning of this section, shown in Figure 16. Round the altitude to the nearest tenth of a mile. a 15° 35° 20 miles Solution To find the elevation of the aircraft, we first find the distance from one station to the aircraft, such as the side a, and then use right triangle relationships to find the height of the aircraft, h. Because the angles in the triangle add up to 180 degrees, the unknown angle must be 180° - 15° - 35° = 130°. This angle is opposite the side of length 20, allowing us to set up a Law of Sines relationship.

 sin(130°) _  =  sin(35°) _ a 

asin(130°) = 20sin(35°)

a =  20sin(35°) _ sin(130°) 

The distance from one station to the aircraft is about 14.98 miles. Now that we know a, we can use right triangle relationships to solve for h.

sin(15°) =  opposite _ hypotenuse 

sin(15°) =  h _ a 

sin(15°) =  h _

The aircraft is at an altitude of approximately 3.9 miles.

**Try It #6**
The diagram shown in Figure 17 represents the height of a blimp flying over a football stadium. Find the height of the blimp if the angle of elevation at the southern end zone, point A, is 70°, the angle of elevation from the northern end zone, point B, is 62°, and the distance between the viewing points of the two end zones is 145 yards. 145 yards 70° C A B 62°

Access the following online resources for additional instruction and practice with trigonometric applications. • Law of Sines: The Basics (http://openstaxcollege.org/l/sinesbasic) • Law of Sines: The Ambiguous Case (http://openstaxcollege.org/l/sinesambiguous)


### 8.1 Section Exercises
Verbal 1. Describe the altitude of a triangle. 2. Compare right triangles and oblique triangles. 3. When can you use the Law of Sines to find a missing angle? 4. In the Law of Sines, what is the relationship between the angle in the numerator and the side in the denominator? 5. What type of triangle results in an ambiguous case? Algebraic For the following exercises, assume \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c. Solve each triangle, if possible. Round each answer to the nearest tenth. For the following exercises, use the Law of Sines to solve for the missing side for each oblique triangle. Round each answer to the nearest hundredth. Assume that angle A is opposite side a, angle B is opposite side b, and angle C is opposite side c. 11. Find side b when A = 37°, B = 49°, c = 5. 12. Find side a when A = 132°, C = 23°, b = 10. 13. Find side c when B = 37°, C = 21, b = 23. For the following exercises, assume \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c. Determine whether there is no triangle, one triangle, or two triangles. Then solve each triangle, if possible. Round each answer to the nearest tenth. For the following exercises, use the Law of Sines to solve, if possible, the missing side or angle for each triangle or triangles in the ambiguous case. Round each answer to the nearest tenth. 24. Find angle A when a = 24, b = 5, B = 22°. 25. Find angle A when a = 13, b = 6, B = 20°. 26. Find angle B when A = 12°, a = 2, b = 9. For the following exercises, find the area of the triangle with the given measurements. Round each answer to the nearest tenth. Graphical For the following exercises, find the length of side x. Round to the nearest tenth. x 70° 50° x 25° 120° x 75° 45°


## 8.1 Section Exercises
x 110° 40° x 111° 22° 8.6 For the following exercises, find the measure of angle x, if possible. Round to the nearest tenth. 98° x 37° x 22° x 59° 5.3 5.7 x 41. Notice that x is an obtuse angle. 55° x 65° x For the following exercises, solve the triangle. Round each answer to the nearest tenth. 93° 24.1 32.6 A B C For the following exercises, find the area of each triangle. Round each answer to the nearest tenth. 30° 25° 51° 4.5 2.9 3.5 58° 51° 40° 30° 115° x 42° 50°

Extensions 50. Find the radius of the circle in Figure 18. Round to the nearest tenth. 145° 51. Find the diameter of the circle in Figure 19. Round to the nearest tenth. 110° 8.3 52. Find m ∠ADC in Figure 20. Round to the nearest tenth. 60° A B C D 53. Find AD in Figure 21. Round to the nearest tenth. 53° 44° B C A D 54. Solve both triangles in Figure 22. Round each answer to the nearest tenth. 48° 46° 48° 2 4.2 A B E C D 55. Find AB in the parallelogram shown in Figure 23. 130° 130° A B D C 56. Solve the triangle in Figure 24. (Hint: Draw a perpendicular from H to JK). Round each answer to the nearest tenth. 20° H K J 57. Solve the triangle in Figure 25. (Hint: Draw a perpendicular from N to LM). Round each answer to the nearest tenth. 74° 4.6 L M N

58. In Figure 26, ABCD is not a parallelogram. ∠m is obtuse. Solve both triangles. Round each answer to the nearest tenth. 35° 65° A B x m h k y D C n Real-World Applications 59. A pole leans away from the sun at an angle of 7° to the vertical, as shown in Figure 27. When the elevation of the sun is 55°, the pole casts a shadow 42 feet long on the level ground. How long is the pole? Round the answer to the nearest tenth. 60. To determine how far a boat is from shore, two radar stations 500 feet apart find the angles out to the boat, as shown in Figure 28. Determine the distance of the boat from station A and the distance of the boat from shore. Round your answers to the nearest whole foot. 70° A B 60° 61. Figure 29 shows a satellite orbiting Earth. The satellite passes directly over two tracking stations A and B, which are 69 miles apart. When the satellite is on one side of the two stations, the angles of elevation at A and B are measured to be 86.2° and 83.9°, respectively. How far is the satellite from station A and how high is the satellite above the ground? Round answers to the nearest whole mile. 83.9° 86.2° A B 62. A communications tower is located at the top of a steep hill, as shown in Figure 30. The angle of inclination of the hill is 67°. A guy wire is to be attached to the top of the tower and to the ground, 165 meters downhill from the base of the tower. The angle formed by the guy wire and the hill is 16°. Find the length of the cable required for the guy wire to the nearest whole meter. 16° 67° 165m

63. The roof of a house is at a 20° angle. An 8-foot solar panel is to be mounted on the roof and should be angled 38° relative to the horizontal for optimal results. (See Figure 31). How long does the vertical support holding up the back of the panel need to be? Round to the nearest tenth. 20° 38° 8 f 64. Similar to an angle of elevation, an angle of depression is the acute angle formed by a horizontal line and an observer’s line of sight to an object below the horizontal. A pilot is flying over a straight highway. He determines the angles of depression to two mileposts, 6.6 km apart, to be 37° and 44°, as shown in Figure 32. Find the distance of the plane from point A to the nearest tenth of a kilometer. 44° 37° A B 65. A pilot is flying over a straight highway. He determines the angles of depression to two mileposts, 4.3 km apart, to be 32° and 56°, as shown in Figure 33. Find the distance of the plane from point A to the nearest tenth of a kilometer. A B 66. In order to estimate the height of a building, two students stand at a certain distance from the building at street level. From this point, they find the angle of elevation from the street to the top of the building to be 39°. They then move 300 feet closer to the building and find the angle of elevation to be 50°. Assuming that the street is level, estimate the height of the building to the nearest foot. 67. In order to estimate the height of a building, two students stand at a certain distance from the building at street level. From this point, they find the angle of elevation from the street to the top of the building to be 35°. They then move 250 feet closer to the building and find the angle of elevation to be 53°. Assuming that the street is level, estimate the height of the building to the nearest foot. 68. Points A and B are on opposite sides of a lake. Point C is 97 meters from A. The measure of angle BAC is determined to be 101°, and the measure of angle ACB is determined to be 53°. What is the distance from A to B, rounded to the nearest whole meter? 69. A man and a woman standing 3 1 _ 2  miles apart spot a hot air balloon at the same time. If the angle of elevation from the man to the balloon is 27°, and the angle of elevation from the woman to the balloon is 41°, find the altitude of the balloon to the nearest foot. 70. Two search teams spot a stranded climber on a mountain. The first search team is 0.5 miles from the second search team, and both teams are at an altitude of 1 mile. The angle of elevation from the first search team to the stranded climber is 15°. The angle of elevation from the second search team to the climber is 22°. What is the altitude of the climber? Round to the nearest tenth of a mile.

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
Finding the Unknown Side and Angles of a SAS Triangle Find the unknown side and angles of the triangle in Figure 4. \gamma  b 30° \beta  \alpha  Solution First, make note of what is given: two sides and the angle between them. This arrangement is classified as SAS and supplies the data needed to apply the Law of Cosines. Each one of the three laws of cosines begins with the square of an unknown side opposite a known angle. For this example, the first side to solve for is side b, as we know the measurement of the opposite angle \beta .

b^{2} = a^{2} + c^{2}-2accos \beta 

Substitute the measurements for the known quantities.

3  _ 2   Evaluate the cosine and begin to simplify.

3 

b = \sqrt{3}   Use the square root property.

Because we are solving for a length, we use only the positive square root. Now that we know the length b, we can use the Law of Sines to fill in the remaining angles of the triangle. Solving for angle \alpha , we have

 sin \alpha  _ a  =  sin \beta  _ b 

 sin \alpha  _ 10  =  sin(30°) _

sin \alpha  =  10sin(30°) _ 6.013  Multiply both sides of the equation by 10.

\alpha  = sin-1  10sin(30°) _ Find the inverse sine of  10sin(30°) _ 6.013 .

The other possibility for \alpha  would be \alpha  = 180° - 56.3° ≈ 123.7°. In the original diagram, \alpha  is adjacent to the longest side, so \alpha  is an acute angle and, therefore, 123.7° does not make sense. Notice that if we choose to apply the Law of Cosines, we arrive at a unique answer. We do not have to consider the other possibilities, as cosine is unique for angles between 0° and 180°. Proceeding with \alpha  ≈ 56.3°, we can then find the third angle of the triangle.

The complete set of angles and sides is

a = 10

\beta  = 30°

c = 12

**Try It #1**
Find the missing side and angles of the given triangle: \alpha  = 30°, b = 12, c = 24.


**Example  2**

### Solving for an Angle of a SSS Triangle
Find the angle \alpha  for the given triangle if side a = 20, side b = 25, and side c = 18. Solution For this example, we have no angles. We can solve for any angle using the Law of Cosines. To solve for angle \alpha , we have

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

Solution For simplicity, we start by drawing a diagram similar to Figure 6 and labeling our given information. \theta  Using the Law of Cosines, we can solve for the angle \theta . Remember that the Law of Cosines uses the square of one side to find the cosine of the opposite angle. For this example, let a = 2420, b = 5050, and c = 6000. Thus, \theta  corresponds to the opposite side a = 2420.

a^{2} = b^{2} + c^{2} - 2bccos \theta 

___

 = cos \theta 

To answer the questions about the phone’s position north and east of the tower, and the distance to the highway, drop a perpendicular from the position of the cell phone, as in Figure 7. This forms two right triangles, although we only need the right triangle that includes the first tower for this problem. x y 23.3° Using the angle \theta  = 23.3° and the basic trigonometric identities, we can find the solutions. Thus

cos(23.3°) =  x _

sin(23.3°) =  y _

The cell phone is approximately 4,638 feet east and 1,998 feet north of the first tower, and 1,998 feet from the highway.

**Example  4**

### Calculating Distance Traveled Using a SAS Triangle
Returning to our problem at the beginning of this section, suppose a boat leaves port, travels 10 miles, turns 20 degrees, and travels another 8 miles. How far from port is the boat? The diagram is repeated here in Figure 8.

8 mi 20° 10 mi Port Solution The boat turned 20 degrees, so the obtuse angle of the non-right triangle is the supplemental angle, 180° - 20° = 160°. With this, we can utilize the Law of Cosines to find the missing side of the obtuse triangle—the distance of the boat to the port.

x = \sqrt{x} ≈ 17.7 miles The boat is about 17.7 miles from port. Using Heron’s Formula to Find the Area of a Triangle We already learned how to find the area of an oblique triangle when we know two sides and an angle. We also know the formula to find the area of a triangle using the base and the height. When we know the three sides, however, we can use Heron’s formula instead of finding the height. Heron of Alexandria was a geometer who lived during the first century A.D. He discovered a formula for finding the area of oblique triangles when three sides are known. Heron’s formula Heron’s formula finds the area of oblique triangles in which sides a, b, and c are known. Area = \sqrt{—}

s(s - a)(s - b)(s - c)  where s =  (a + b + c) _  is one half of the perimeter of the triangle, sometimes called the semi-perimeter.

**Example  5**
Using Heron’s Formula to Find the Area of a Given Triangle Find the area of the triangle in Figure 9 using Heron’s formula. A B a = 10 b = 15 c = 7 C Solution First, we calculate s.

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
A Chicago city developer wants to construct a building consisting of artist’s lofts on a triangular lot bordered by Rush Street, Wabash Avenue, and Pearson Street. The frontage along Rush Street is approximately 62.4 meters, along Wabash Avenue it is approximately 43.5 meters, and along Pearson Street it is approximately 34.1 meters. How many square meters are available to the developer? See Figure 10 for a view of the city property. E. Pearson St (34.1 meters) N. Wabash Ave (43.5 meters) Rush St (62.4 meters) Solution Find the measurement for s, which is one-half of the perimeter.

__ 

s = 70 m Apply Heron’s formula.

Area = \sqrt{—}

Area = \sqrt{The} developer has about 711.4 square meters.

**Try It #4**
Find the area of a triangle given a = 4.38 ft , b = 3.79 ft, and c = 5.22 ft. Access these online resources for additional instruction and practice with the Law of Cosines. • Law of Cosines (http://openstaxcollege.org/l/lawcosines) • Law of Cosines: Applications (http://openstaxcollege.org/l/cosineapp) • Law of Cosines: Applications 2 (http://openstaxcollege.org/l/cosineapp^{2})


## 8.2 Section Exercises

### 8.2 Section Exercises
Verbal 1. If you are looking for a missing side of a triangle, what do you need to know when using the Law of Cosines? 2. If you are looking for a missing angle of a triangle, what do you need to know when using the Law of Cosines? 3. Explain what s represents in Heron’s formula. 4. Explain the relationship between the Pythagorean Theorem and the Law of Cosines. 5. When must you use the Law of Cosines instead of the Pythagorean Theorem? Algebraic For the following exercises, assume \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c. If possible, solve each triangle for the unknown side. Round to the nearest tenth. For the following exercises, use the Law of Cosines to solve for the missing angle of the oblique triangle. Round to the nearest tenth. 16. a = 42, b = 19, c = 30; find angle A. 17. a = 14, b = 13, c = 20; find angle C. 18. a = 16, b = 31, c = 20; find angle B. 19. a = 13, b = 22, c = 28; find angle A. 20. a = 108, b = 132, c = 160; find angle C. For the following exercises, solve the triangle. Round to the nearest tenth. For the following exercises, use Heron’s formula to find the area of the triangle. Round to the nearest hundredth. 27. Find the area of a triangle with sides of length 18 in, 21 in, and 32 in. Round to the nearest tenth. 28. Find the area of a triangle with sides of length 20 cm, 26 cm, and 37 cm. Round to the nearest tenth. _ 2  m, b =  1 _ 3  m, c =  1 _ 4  m Graphical For the following exercises, find the length of side x. Round to the nearest tenth. x 6.5 72° 4.5 3.4 x 42o A B x 40°

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
Over 12 kilometers from port, a sailboat encounters rough weather and is blown off course by a 16-knot wind (see representing location that is different from a standard coordinate grid. Port 16-knot wind 60° 30° 330° 300° 270° 240° 210° 180° 150° 120° 90° Plotting Points Using Polar Coordinates When we think about plotting points in the plane, we usually think of rectangular coordinates (x, y) in the Cartesian coordinate plane. However, there are other ways of writing a coordinate pair and other types of grid systems. In this section, we introduce to polar coordinates, which are points labeled (r, \theta ) and plotted on a polar grid. The polar grid is represented as a series of concentric circles radiating out from the pole, or the origin of the coordinate plane. The polar grid is scaled as the unit circle with the positive x-axis now viewed as the polar axis and the origin as the pole. The first coordinate r is the radius or length of the directed line segment from the pole. The angle \theta , measured in radians, indicates the direction of r. We move counterclockwise from the polar axis by an angle of \theta , and measure a directed line segment the length of r in the direction of \theta . Even though we measure \theta  first and then r, the polar point is written with the r-coordinate first. For example, to plot the point  2,  \pi  _ 4  , we would move  \pi  _ 4  units in the counterclockwise direction and then a length of 2 from the pole. This point is plotted on the grid in Figure 2. Polar Grid


**Example  1**

### Plotting a Point on the Polar Grid
Plot the point  3,  \pi  _ 2   on the polar grid. Solution The angle  \pi  _ 2  is found by sweeping in a counterclockwise direction 90° from the polar axis. The point is located at a length of 3 units from the pole in the  \pi  _ 2  direction, as shown in Figure 3.

**Try It #1**
Plot the point  2,  \pi  _ 3   in the polar grid.

**Example  2**

### Plotting a Point in the Polar Coordinate System with a Negative Component
Plot the point  -2,  \pi  _ 6   on the polar grid. Solution We know that  \pi  _ 6  is located in the first quadrant. However, r = -2. We can approach plotting a point with a negative r in two ways: Plot the point  2,  \pi  _ 6   by moving  \pi  _ 6  in the counterclockwise direction and extending a directed line segment 2 units into the first quadrant. Then retrace the directed line segment back through the pole, and continue 2 units into the third quadrant; 2. Move  \pi  _ 6  in the counterclockwise direction, and draw the directed line segment from the pole 2 units in the negative direction, into the third quadrant. See Figure 4(a). Compare this to the graph of the polar coordinate  2,  \pi  _ 6   shown in Figure 4(b). (a) (b)

**Try It #2**
Plot the points  3, -  \pi  _ 6   and  2,  9\pi  _ 4   on the same polar grid.

Converting from Polar Coordinates to Rectangular Coordinates When given a set of polar coordinates, we may need to convert them to rectangular coordinates. To do so, we can recall the relationships that exist among the variables x, y, r, and \theta .

cos \theta  =  x _ r  → x = rcos \theta 

sin \theta  =  y _ r  → y = rsin \theta  Dropping a perpendicular from the point in the plane to the x-axis forms a right triangle, as illustrated in Figure 5. An easy way to remember the equations above is to think of cos \theta  as the adjacent side over the hypotenuse and sin \theta  as the opposite side over the hypotenuse. x r y x (x, y) or (r, \theta ) y \theta  converting from polar coordinates to rectangular coordinates To convert polar coordinates (r, \theta ) to rectangular coordinates (x, y), let

cos \theta  =  x _ r  → x = rcos \theta 

sin \theta  =  y _ r  → y = rsin \theta 

**How To…**
Given polar coordinates, convert to rectangular coordinates. 1. Given the polar coordinate (r, \theta ), write x = rcos \theta  and y = rsin \theta . 2. Evaluate cos \theta  and sin \theta . 3. Multiply cos \theta  by r to find the x-coordinate of the rectangular form. 4. Multiply sin \theta  by r to find the y-coordinate of the rectangular form.

**Example  3**

### Writing Polar Coordinates as Rectangular Coordinates
Write the polar coordinates  3,  \pi  _ 2   as rectangular coordinates. Solution Use the equivalent relationships.

x = rcos \theta 

x = 3cos  \pi  _ 2  = 0

y = rsin \theta 

y = 3sin  \pi  _ 2  = 3 The rectangular coordinates are (0, 3). See Figure 6.

Polar Grid Coordinate Grid x y

**Example  4**

### Writing Polar Coordinates as Rectangular Coordinates
Write the polar coordinates (-2, 0) as rectangular coordinates. Solution See Figure 7. Writing the polar coordinates as rectangular, we have

x = rcos \theta 

x = -2cos(0) = -2

y = rsin \theta 

y = -2sin(0) = 0 The rectangular coordinates are also (-2, 0). x y

**Try It #3**
Write the polar coordinates  -1,  2\pi  _ 3   as rectangular coordinates. Converting from Rectangular Coordinates to Polar Coordinates To convert rectangular coordinates to polar coordinates, we will use two other familiar relationships. With this conversion, however, we need to be aware that a set of rectangular coordinates will yield more than one polar point.

converting from rectangular coordinates to polar coordinates Converting from rectangular coordinates to polar coordinates requires the use of one or more of the relationships illustrated in Figure 8.

cos \theta  =  x _ r  or x = rcos \theta 

sin \theta  =  y _ r  or y = rsin \theta 

r 2 = x 2 + y 2

tan \theta  =  y _ x  x x y r (x, y), (r, \theta ) y \theta 

**Example  5**

### Writing Rectangular Coordinates as Polar Coordinates
Convert the rectangular coordinates (3, 3) to polar coordinates. Solution We see that the original point (3, 3) is in the first quadrant. To find \theta , use the formula tan \theta  =  y _ x . This gives

tan \theta  =  3 _ 3 

tan \theta  = 1

\theta  = tan-1(1)

\theta  =  \pi  _ 4  To find r, we substitute the values for x and y into the formula r = \sqrt{x} 2 + y 2 . We know that r must be positive, as  \pi  _ 4  is in the first quadrant. Thus

r = \sqrt{r} = \sqrt{9} + 9 

r = \sqrt{18}  = 3\sqrt{2}  So, r = 3\sqrt{2}  and \theta  =  \pi  _ 4 , giving us the polar point  3\sqrt{2} ,  \pi  _ 4  . See Figure 9. x y Analysis There are other sets of polar coordinates that will be the same as our first solution. For example, the points  -3\sqrt{2} ,  5\pi  ___ 4   and  3\sqrt{2} , - 7\pi  _ 4   and will coincide with the original solution of  3\sqrt{2} ,  \pi  _ 4  . The point  -3\sqrt{2} ,  5\pi  _ 4   indicates a move further counterclockwise by \pi , which is directly opposite  \pi  _ 4 . The radius is expressed as -3\sqrt{2} . However, the angle  5\pi  _ 4  is located in the third quadrant and, as r is negative, we extend the directed line segment in the opposite direction, into the first quadrant. This is the same point as  3\sqrt{2} ,  \pi  __ 4  . The point  3\sqrt{2} , -  7\pi  _ 4   is a move further clockwise by -  7\pi  _ 4 , from  \pi  _ 4 . The radius, 3\sqrt{2} , is the same.

Transforming Equations between Polar and Rectangular Forms We can now convert coordinates between polar and rectangular form. Converting equations can be more difficult, but it can be beneficial to be able to convert between the two forms. Since there are a number of polar equations that cannot be expressed clearly in Cartesian form, and vice versa, we can use the same procedures we used to convert points between the coordinate systems. We can then use a graphing calculator to graph either the rectangular form or the polar form of the equation.

**How To…**
Given an equation in polar form, graph it using a graphing calculator. 1. Change the MODE to POL, representing polar form. 2. Press the Y= button to bring up a screen allowing the input of six equations: r^{1}, r^{2}, ... , r^{6}. 3. Enter the polar equation, set equal to r. 4. Press GRAPH.

**Example  6**

### Writing a Cartesian Equation in Polar Form
Write the Cartesian equation x 2 + y 2 = 9 in polar form. Solution The goal is to eliminate x and y from the equation and introduce r and \theta . Ideally, we would write the equation r as a function of \theta . To obtain the polar form, we will use the relationships between (x, y) and (r, \theta ). Since x = rcos \theta  and y = rsin \theta , we can substitute and solve for r.

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
Rewriting a Cartesian Equation as a Polar Equation Rewrite the Cartesian equation x 2 + y 2 = 6y as a polar equation. Solution This equation appears similar to the previous example, but it requires different steps to convert the equation. We can still follow the same procedures we have already learned and make the following substitutions:

r 2 = 6y Use x 2 + y 2 = r 2.

r 2 = 6rsin \theta  Substitute y = rsin \theta .

r 2-6rsin \theta  = 0 Set equal to 0.

r (r - 6sin \theta ) = 0 Factor and solve.

r = 0 We reject r = 0, as it only represents one point, (0, 0).

or r = 6sin \theta  Therefore, the equations x 2 + y 2 = 6y and r = 6sin \theta  should give us the same graph. See Figure 11. (a) x y (b) The Cartesian or rectangular equation is plotted on the rectangular grid, and the polar equation is plotted on the polar grid. Clearly, the graphs are identical.

**Example  8**
Rewriting a Cartesian Equation in Polar Form Rewrite the Cartesian equation y = 3x + 2 as a polar equation. Solution We will use the relationships x = rcos \theta  and y = rsin \theta .

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
Covert the polar equation r = 2sec \theta  to a rectangular equation, and draw its corresponding graph. Solution The conversion is

r = 2sec \theta 

r =  2 _ cos \theta  

rcos \theta  = 2

x = 2 Notice that the equation r = 2sec \theta  drawn on the polar grid is clearly the same as the vertical line x = 2 drawn on the rectangular grid (see Figure 12). Just as x = c is the standard form for a vertical line in rectangular form, r = csec \theta  is the standard form for a vertical line in polar form. r = 2 sec \theta  x = 2 (a) (b) x y A similar discussion would demonstrate that the graph of the function r = 2csc \theta  will be the horizontal line y = 2. In fact, r = ccsc \theta  is the standard form for a horizontal line in polar form, corresponding to the rectangular form y = c.

**Example  10**
Rewriting a Polar Equation in Cartesian Form Rewrite the polar equation r =  _ 1 - 2cos \theta   as a Cartesian equation. Solution The goal is to eliminate \theta  and r, and introduce x and y. We clear the fraction, and then use substitution. In order to replace r with x and y, we must use the expression x 2 + y 2 = r 2.

r =  _ 1 - 2cos \theta  

r(1 - 2cos \theta ) = 3

r  1 - 2  x _ r    = 3

Use cos \theta  =  x _ r  to eliminate \theta .

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

(x + 2)^{2} -  y 2

_ 3  = 1

**Try It #5**
Rewrite the polar equation r = 2sin \theta  in Cartesian form.

**Example  11**
Rewriting a Polar Equation in Cartesian Form Rewrite the polar equation r = sin(2\theta ) in Cartesian form.

**Solution**
r = sin(2\theta ) Use the double angle identity for sine.

r = 2sin \theta cos \theta  Use cos \theta  =  x __ r  and sin \theta  =  y __ r .

r = 2  x __ r    y __ r   Simplify.

r =  2xy _ r 2  Multiply both sides by r 2.

r^{3} = 2xy

 \sqrt{x} 2 + y 2    = 2xy As x 2 + y 2 = r 2, r = \sqrt{x} 2 + y 2 . This equation can also be written as

(x 2 + y 2)  3 _ 2  = 2xy or x 2 + y 2 = (2xy)  2 _ 3 . Access these online resources for additional instruction and practice with polar coordinates. • Introduction to Polar Coordinates (http://openstaxcollege.org/l/intropolar) • Comparing Polar and Rectangular Coordinates (http://openstaxcollege.org/l/polarrect)


## 8.3 Section Exercises

### 8.3 Section Exercises
Verbal 1. How are polar coordinates different from rectangular coordinates? 2. How are the polar axes different from the x- and y-axes of the Cartesian plane? 3. Explain how polar coordinates are graphed. 4. How are the points  3,  \pi  _ 2   and  -3,  \pi  _ 2   related? 5. Explain why the points  -3,  \pi  _ 2   and  3, -  \pi  _ 2   are the same. Algebraic For the following exercises, convert the given polar coordinates to Cartesian coordinates with r > 0 and 0 \le  \theta  \le 2\pi . Remember to consider the quadrant in which the given point is located when determining \theta  for the point. _ 6   8.  6, -  \pi  _ 4   9.  -3,  \pi  _ 6   _ 4   For the following exercises, convert the given Cartesian coordinates to polar coordinates with r > 0, 0 \le  \theta  <2\pi . Remember to consider the quadrant in which the given point is located. For the following exercises, convert the given Cartesian equation to a polar equation. 20. x 2 + y 2 = 4y 21. x 2 + y 2 = 3x 22. x 2 - y 2 = x 23. x 2 - y 2 = 3y 24. x 2 + y 2 = 9 For the following exercises, convert the given polar equation to a Cartesian equation. Write in the standard form of a conic if possible, and identify the conic section represented. 28. r = 3sin \theta  29. r = 4cos \theta  30. r =  __

sin \theta  + 7cos \theta   31. r =  __

cos \theta  + 3sin \theta   32. r = 2sec \theta  33. r = 3csc \theta  34. r = \sqrt{rcos} \theta  + 2  35. r 2 = 4sec \theta  csc \theta  38. r =  __

4cos \theta  - 3sin \theta   39. r =  __

cos \theta  - 5sin \theta   Graphical For the following exercises, find the polar coordinates of the point. \pi  3\pi  \pi  \pi  3\pi  \pi  3\pi  \pi 

\pi  \pi  3\pi  \pi  3\pi  \pi  For the following exercises, plot the points. 45.  -2,  \pi  _ 3   46.  -1, -  \pi  _ 2   _ 4   48.  -4,  \pi  _ 3   _ 2   _ 4   _ 6   _ 6   53.  -2,  \pi  _ 4   _ 2   For the following exercises, convert the equation from rectangular to polar form and graph on the polar axis. 55. 5x - y = 6 57. x 2 +(y - 1) 2 = 1 58. (x + 2) 2 +(y + 3) 2 = 13 60. x 2 + y 2 = 5y 61. x 2 + y 2 = 3x For the following exercises, convert the equation from polar to rectangular form and graph on the rectangular plane. 63. r = - 4 64. \theta  = -  2\pi  _ 3  65. \theta  =  \pi  _ 4  66. r = sec \theta  67. r = -10sin \theta  68. r = 3cos \theta  Technology 69. Use a graphing calculator to find the rectangular coordinates of  2, -  \pi  _ 5  . Round to the nearest thousandth. 70. Use a graphing calculator to find the rectangular coordinates of  -3,  3\pi  _ 7  . Round to the nearest thousandth. 71. Use a graphing calculator to find the polar coordinates of (-7, 8) in degrees. Round to the nearest thousandth. 72. Use a graphing calculator to find the polar coordinates of (3, -4) in degrees. Round to the nearest hundredth. 73. Use a graphing calculator to find the polar coordinates of (-2, 0) in radians. Round to the nearest hundredth. Extensions 74. Describe the graph of r = asec \theta ; a > 0. 75. Describe the graph of r = asec \theta ; a < 0. 76. Describe the graph of r = acsc \theta ; a > 0. 77. Describe the graph of r = acsc \theta ; a < 0. 78. What polar equations will give an oblique line? For the following exercises, graph the polar inequality. 80. 0 \le  \theta  \le   \pi  _ 4  81. \theta  =  \pi  _ 4 , r \ge  2 82. \theta  =  \pi  _ 4 , r \ge  -3 83. 0 \le  \theta  \le   \pi  _ 3 , r < 2 84. -  \pi  _ 6  < \theta  \le   \pi  _ 3 , -3 < r < 2


## 8.4 Polar Coordinates: Graphs
Learning Objectives
In this section, you will:
• Test polar equations for symmetry.
• Graph polar equations by plotting points.
The planets move through space in elliptical, periodic orbits about the sun, as shown in Figure 1. They are in constant motion, so fixing an exact position of any planet is valid only for a moment. In other words, we can fix only a planet’s instantaneous position. This is one application of polar coordinates, represented as (r, \theta ). We interpret r as the distance from the sun and \theta  as the planet’s angular bearing, or its direction from a fixed point on the sun. In this section, we will focus on the polar system and the graphs that are generated directly from polar coordinates. Mercury Earth Venus Mars Testing Polar Equations for Symmetry Just as a rectangular equation such as y = x^{2} describes the relationship between x and y on a Cartesian grid, a polar equation describes a relationship between r and \theta  on a polar grid. Recall that the coordinate pair (r, \theta ) indicates that we move counterclockwise from the polar axis (positive x-axis) by an angle of \theta , and extend a ray from the pole (origin) r units in the direction of \theta . All points that satisfy the polar equation are on the graph. Symmetry is a property that helps us recognize and plot the graph of any equation. If an equation has a graph that is symmetric with respect to an axis, it means that if we folded the graph in half over that axis, the portion of the graph on one side would coincide with the portion on the other side. By performing three tests, we will see how to apply the properties of symmetry to polar equations. Further, we will use symmetry (in addition to plotting key points, zeros, and maximums of r) to determine the graph of a polar equation. In the first test, we consider symmetry with respect to the line \theta  =  \pi  _ 2 (y-axis). We replace (r, \theta ) with (-r, -\theta ) to determine if the new equation is equivalent to the original equation. For example, suppose we are given the equation r = 2sin \theta ;

r = 2sin \theta 

-r = 2sin(-\theta ) Replace (r, \theta ) with (-r, -\theta ).

-r = -2sin \theta  Identity: sin(-\theta )= -sin \theta .

r = 2sin \theta  Multiply both sides by-1. This equation exhibits symmetry with respect to the line \theta  =  \pi  _ 2 . In the second test, we consider symmetry with respect to the polar axis (x -axis). We replace (r, \theta ) with (r, -\theta ) or (-r, \pi  - \theta ) to determine equivalency between the tested equation and the original. For example, suppose we are given the equation r = 1 - 2cos \theta .

r = 1 - 2cos \theta 

r = 1 - 2cos(-\theta ) Replace (r, \theta ) with (r, -\theta ).

r = 1 - 2cos \theta  Even/Odd identity

The graph of this equation exhibits symmetry with respect to the polar axis. In the third test, we consider symmetry with respect to the pole (origin). We replace (r, \theta ) with (-r, \theta ) to determine if the tested equation is equivalent to the original equation. For example, suppose we are given the equation r = 2sin(3\theta ).

r = 2sin(3\theta )

-r = 2sin(3\theta ) The equation has failed the symmetry test, but that does not mean that it is not symmetric with respect to the pole. Passing one or more of the symmetry tests verifies that symmetry will be exhibited in a graph. However, failing the symmetry tests does not necessarily indicate that a graph will not be symmetric about the line \theta  =  \pi  _ 2 , the polar axis, or the pole. In these instances, we can confirm that symmetry exists by plotting reflecting points across the apparent axis of symmetry or the pole. Testing for symmetry is a technique that simplifies the graphing of polar equations, but its application is not perfect. symmetry tests A polar equation describes a curve on the polar grid. The graph of a polar equation can be evaluated for three types of symmetry, as shown in Figure 2. \theta  \theta  \theta  \theta  \theta  \theta  (a) (b) (c) _ 2  (y-axis) if replacing (r, \theta  ) with (-r, -\theta  ) yields an equivalent equation. (b) A graph is symmetric with respect to the polar axis (x-axis) if replacing (r, \theta ) with (r, -\theta  ) or (-r, \pi -\theta  ) yields an equivalent equation. (c) A graph is symmetric with respect to the pole (origin) if replacing (r, \theta  ) with (-r, \theta  ) yields an equivalent equation.

**How To…**
Given a polar equation, test for symmetry. 1. Substitute the appropriate combination of components for (r, \theta ): (-r,- \theta ) for \theta  =  \pi  _ 2  symmetry; (r,- \theta ) for polar axis symmetry; and (-r, \theta ) for symmetry with respect to the pole. 2. If the resulting equations are equivalent in one or more of the tests, the graph produces the expected symmetry.

**Example  1**
Testing a Polar Equation for Symmetry Test the equation r = 2sin \theta  for symmetry. Solution Test for each of the three types of symmetry. 1) Replacing (r, \theta ) with (-r, -\theta ) yields the same result. Thus, the graph is symmetric with respect to the line \theta  =  \pi  _ 2 .

-r = 2sin(-\theta )

-r = -2sin \theta  Even-odd identity

r = 2sin \theta  Multiply by -1 Passed 2) Replacing \theta  with -\theta  does not yield the same equation. Therefore, the graph fails the test and may or may not be symmetric with respect to the polar axis.

r = 2sin(-\theta )

r = -2sin \theta  Even-odd identity

r = -2sin \theta  \neq  2sin \theta  Failed 3) Replacing r with -r changes the equation and fails the test. The graph may or may not be symmetric with respect to the pole.

-r = 2sin \theta  r = -2sin \theta  \neq  2sin \theta  Failed


**Analysis**
Using a graphing calculator, we can see that the equation r = 2sin \theta  is a circle centered at (0, 1) with radius \pi  r = 1 and is indeed symmetric to the line \theta  =  \pi  _ 2 . We can also see that the graph is not symmetric with the polar axis or the pole. See Figure 3.

**Try It #1**
Test the equation for symmetry: r = - 2cos \theta . Graphing Polar Equations by Plotting Points To graph in the rectangular coordinate system we construct a table of x and y values. To graph in the polar coordinate system we construct a table of \theta  and r values. We enter values of \theta  into a polar equation and calculate r. However, using the properties of symmetry and finding key values of \theta  and r means fewer calculations will be needed. Finding Zeros and Maxima To find the zeros of a polar equation, we solve for the values of \theta  that result in r = 0. Recall that, to find the zeros of polynomial functions, we set the equation equal to zero and then solve for x. We use the same process for polar equations. Set r = 0, and solve for \theta . For many of the forms we will encounter, the maximum value of a polar equation is found by substituting those values of \theta  into the equation that result in the maximum value of the trigonometric functions. Consider r = 5cos \theta ; the maximum distance between the curve and the pole is 5 units. The maximum value of the cosine function is 1 when \theta  = 0, so our polar equation is 5cos \theta , and the value \theta  = 0 will yield the maximum | r |. Similarly, the maximum value of the sine function is 1 when \theta  =  \pi  _ 2 , and if our polar equation is r = 5sin \theta , the value \theta  =  \pi  _ 2  will yield the maximum | r |. We may find additional information by calculating values of r when \theta  = 0. These points would be polar axis intercepts, which may be helpful in drawing the graph and identifying the curve of a polar equation.

**Example  2**

### Finding Zeros and Maximum Values for a Polar Equation
Using the equation in Example 1, find the zeros and maximum | r | and, if necessary, the polar axis intercepts of r = 2sin \theta . Solution To find the zeros, set r equal to zero and solve for \theta .

2sin \theta  = 0

sin \theta  = 0

\theta  = sin-1 0

\theta  = n\pi 

where n is an integer Substitute any one of the \theta  values into the equation. We will use 0.

r = 2sin(0)

r =0 The points (0, 0) and (0, \pm  n\pi ) are the zeros of the equation. They all coincide, so only one point is visible on the graph. This point is also the only polar axis intercept.

To find the maximum value of the equation, look at the maximum value of the trigonometric function sin \theta , which occurs when \theta  =  \pi  _ 2  \pm  2k\pi  resulting in sin  \pi  _ 2   = 1. Substitute  \pi  _ 2  for \theta .

r = 2sin  \pi  _ 2  

r = 2(1)

r = 2 Analysis The point  2,  \pi  _ 2   will be the maximum value on the graph. Let’s plot a few more points to verify the graph of a circle. See Table 2 and Figure 4. \theta  r = 2sin \theta  r r = 2sin(0) = 0  \pi  _ 6  r = 2sin  \pi  _ 6   = 1  \pi  _ 3  r = 2sin  \pi  _ 1.73  \pi  _ 2  r = 2sin  \pi  _ 2  = 2  2\pi  _ 3  r = 2sin  2\pi  _ 1.73  5\pi  _ 6  r = 2sin  5\pi  _ 6  = 1 \pi  r = 2sin(\pi ) = 0

**Try It #2**
Without converting to Cartesian coordinates, test the given equation for symmetry and find the zeros and maximum values of | r |: r = 3cos \theta . Investigating Circles Now we have seen the equation of a circle in the polar coordinate system. In the last two examples, the same equation was used to illustrate the properties of symmetry and demonstrate how to find the zeros, maximum values, and plotted points that produced the graphs. However, the circle is only one of many shapes in the set of polar curves. There are five classic polar curves: cardioids, limaçons, lemniscates, rose curves, and Archimedes’ spirals. We will briefly touch on the polar formulas for the circle before moving on to the classic curves and their variations.

formulas for the equation of a circle Some of the formulas that produce the graph of a circle in polar coordinates are given by r = acos \theta  and r = asin \theta , where a is the diameter of the circle or the distance from the pole to the farthest point on the circumference. The radius is  | a | _ 2 , or one-half the diameter. For r = acos \theta , the center is   a _ 2 , 0 . For r = asin \theta , the center is   a _ 2 , \pi  . r = acos \theta , a > 0 r = acos \theta , a < 0 r = asin \theta , a > 0 r = asin \theta , a < 0 (a) (b) (c) (d)

**Example  3**

### Sketching the Graph of a Polar Equation for a Circle
Sketch the graph of r = 4cos \theta . Solution First, testing the equation for symmetry, we find that the graph is symmetric about the polar axis. Next, we find the zeros and maximum | r | for r = 4cos \theta . First, set r = 0, and solve for \theta  . Thus, a zero occurs at \theta  =  \pi  _ 2  \pm  k\pi . A key point to plot is  0,  \pi  _ 2   To find the maximum value of r, note that the maximum value of the cosine function is 1 when \theta  = 0 \pm  2k\pi . Substitute \theta  = 0 into the equation:

r = 4cos \theta 

r = 4cos(0)

r = 4(1) = 4 The maximum value of the equation is 4. A key point to plot is (4, 0). As r = 4cos \theta  is symmetric with respect to the polar axis, we only need to calculate r-values for \theta  over the interval [0, \pi ]. Points in the upper quadrant can then be reflected to the lower quadrant. Make a table of values similar to Table 3. The graph is shown in Figure 6. \theta   \pi  _ 6   \pi  _ 4   \pi  _ 3   \pi  _ 2   2\pi  _ 3   3\pi  _ 4   5\pi  _ 6  \pi  r 3.46 2.83 -2 -2.83 -3.46


### Investigating Cardioids
While translating from polar coordinates to Cartesian coordinates may seem simpler in some instances, graphing the classic curves is actually less complicated in the polar system. The next curve is called a cardioid, as it resembles a heart. This shape is often included with the family of curves called limaçons, but here we will discuss the cardioid on its own. formulas for a cardioid The formulas that produce the graphs of a cardioid are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  where a > 0, b > 0, and  a __ b  = 1. The cardioid graph passes through the pole, as we can see in Figure 7. r = a + bcos\theta  r = a - bcos\theta  r = a + bsin\theta  r = a - bsin\theta  (a) (b) (c) (d)

**How To…**
Given the polar equation of a cardioid, sketch its graph. 1. Check equation for the three types of symmetry. 2. Find the zeros. Set r = 0. 3. Find the maximum value of the equation according to the maximum value of the trigonometric expression. 4. Make a table of values for r and \theta . 5. Plot the points and sketch the graph.

**Example  4**

### Sketching the Graph of a Cardioid
Sketch the graph of r = 2 + 2cos \theta . Solution First, testing the equation for symmetry, we find that the graph of this equation will be symmetric about the polar axis. Next, we find the zeros and maximums. Setting r = 0, we have \theta  = \pi  +2k\pi . The zero of the equation is located at (0, \pi ). The graph passes through this point. The maximum value of r = 2 + 2cos \theta  occurs when cos \theta  is a maximum, which is when cos \theta  =1 or when \theta  = 0. Substitute \theta  =0 into the equation, and solve for r.

r = 2 + 2cos(0)

r = 2 + 2(1) = 4 The point (4, 0) is the maximum value on the graph. We found that the polar equation is symmetric with respect to the polar axis, but as it extends to all four quadrants, we need to plot values over the interval [0, \pi ]. The upper portion of the graph is then reflected over the polar axis. Next, we make a table of values, as in Table 4, and then we plot the points and draw the graph. See Figure 8. \theta   \pi  _ 4   \pi  _ 2   2\pi  _ 3  \pi  r 3.41

) Investigating Limaçons The word limaçon is Old French for “snail,” a name that describes the shape of the graph. As mentioned earlier, the cardioid is a member of the limaçon family, and we can see the similarities in the graphs. The other images in this category include the one-loop limaçon and the two-loop (or inner-loop) limaçon. One-loop limaçons are sometimes referred to as dimpled limaçons when 1 <  a __ b  < 2 and convex limaçons when  a __ b  \ge  2. formulas for one-loop limaçons The formulas that produce the graph of a dimpled one-loop limaçon are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  where a > 0, b > 0, and 1 <  a __ b  < 2. All four graphs are shown in Figure 9. r = a + bcos\theta  (a) r = a - bcos\theta  (b) r = a + bsin\theta  (c) r = a - bsin\theta  (d)

**How To…**
Given a polar equation for a one-loop limaçon, sketch the graph. 1. Test the equation for symmetry. Remember that failing a symmetry test does not mean that the shape will not exhibit symmetry. Often the symmetry may reveal itself when the points are plotted. 2. Find the zeros. 3. Find the maximum values according to the trigonometric expression. 4. Make a table. 5. Plot the points and sketch the graph.

**Example  5**

### Sketching the Graph of a One-Loop Limaçon
Graph the equation r = 4 - 3sin \theta . Solution First, testing the equation for symmetry, we find that it fails all three symmetry tests, meaning that the graph may or may not exhibit symmetry, so we cannot use the symmetry to help us graph it. However, this equation has a graph that clearly displays symmetry with respect to the line \theta  =  \pi  __ 2 , yet it fails all the three symmetry tests. A graphing calculator will immediately illustrate the graph’s reflective quality. Next, we find the zeros and maximum, and plot the reflecting points to verify any symmetry. Setting r =0 results in \theta  being undefined. What does this mean? How could \theta  be undefined? The angle \theta  is undefined for any value of sin \theta  > 1. Therefore, \theta  is undefined because there is no value of \theta  for which sin \theta  > 1. Consequently, the graph does not pass

through the pole. Perhaps the graph does cross the polar axis, but not at the pole. We can investigate other intercepts by calculating r when \theta  = 0.

r(0) = 4 - 3sin(0)

r = 4-3 ⋅ 0 = 4 So, there is at least one polar axis intercept at (4, 0). Next, as the maximum value of the sine function is 1 when \theta  =  \pi  _ 2 , we will substitute \theta  =  \pi  _ 2  into the equation and solve for r. Thus, r = 1. Make a table of the coordinates similar to Table 5. \theta   \pi  _ 6   \pi  _ 3   \pi  _ 2   2\pi  _ 3   5\pi  _ 6  \pi   7\pi  _ 6   4\pi  _ 3   3\pi  _ 2   5\pi  _ 3   11\pi  _ 6  2\pi  r 2.5 1.4 1.4 2.5 5.5 6.6 6.6 5.5 The graph is shown in Figure 10. )

**Analysis**
This is an example of a curve for which making a table of values is critical to producing an accurate graph. The symmetry tests fail; the zero is undefined. While it may be apparent that an equation involving sin \theta  is likely symmetric with respect to the line \theta  =  \pi  __ 2 , evaluating more points helps to verify that the graph is correct.

**Try It #3**
Sketch the graph of r = 3 - 2cos \theta . Another type of limaçon, the inner-loop limaçon, is named for the loop formed inside the general limaçon shape. It was discovered by the German artist Albrecht Dürer(1471-1528), who revealed a method for drawing the inner-loop limaçon in his 1525 book Underweysung der Messing. A century later, the father of mathematician Blaise Pascal, Étienne Pascal(1588-1651), rediscovered it. formulas for inner-loop limaçons The formulas that generate the inner-loop limaçons are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  where a > 0, b > 0, and a < b. The graph of the inner-loop limaçon passes through the pole twice: once for the outer loop, and once for the inner loop. See Figure 11 for the graphs. r = a + bcos\theta , a < b (a) r = a - bcos\theta , a < b (b) r = a + bsin\theta , a < b (c) r = a - bsin\theta , a < b (d)


**Example  6**

### Sketching the Graph of an Inner-Loop Limaçon
Sketch the graph of r = 2 + 5cos \theta . Solution Testing for symmetry, we find that the graph of the equation is symmetric about the polar axis. Next, finding the zeros reveals that when r = 0, \theta  = 1.98. The maximum | r | is found when cos \theta  =1 or when \theta  = 0. Thus, the maximum is found at the point (7, 0). Even though we have found symmetry, the zero, and the maximum, plotting more points will help to define the shape, and then a pattern will emerge. See Table 6. \theta   \pi  __ 6   \pi  __ 3   \pi  __ 2   2\pi  ___ 3   5\pi  ___ 6  \pi   7\pi  ___ 6   4\pi  ___ 3   3\pi  ___ 2   5\pi  ___ 3   11\pi  ____ 6  2\pi  r 6.3 4.5 -0.5 -2.3 -3 -2.3 -0.5 4.5 6.3 As expected, the values begin to repeat after \theta  = \pi . The graph is shown in Figure 12. (-3, \pi ) Investigating Lemniscates The lemniscate is a polar curve resembling the infinity symbol \infty  or a figure 8. Centered at the pole, a lemniscate is symmetrical by definition. formulas for lemniscates The formulas that generate the graph of a lemniscate are given by r^{2} = a^{2} cos 2\theta  and r^{2} = a^{2} sin 2\theta  where a \neq  0. The formula r^{2} = a^{2} sin 2\theta  is symmetric with respect to the pole. The formula r^{2} = a^{2} cos 2\theta  is symmetric with respect to the pole, the line \theta  =  \pi  __ 2 , and the polar axis. See Figure 13 for the graphs. r^{2} = a^{2}cos(2\theta ) r^{2} = -a^{2}cos(2\theta ) r^{2} = a^{2}sin(2\theta ) r^{2} = -a^{2}sin(2\theta ) (a) (b) (c) (d)

**Example  7**

### Sketching the Graph of a Lemniscate
Sketch the graph of r^{2} = 4cos 2\theta . Solution The equation exhibits symmetry with respect to the line \theta  =  \pi  _ 2 , the polar axis, and the pole. Let’s find the zeros. It should be routine by now, but we will approach this equation a little differently by making the substitution u = 2\theta .

0 = 4cos 2\theta 

0 = 4cos u

0 = cos u

cos-1 0 =  \pi  _ 2 

u =  \pi  _ 2  Substitute 2\theta  back in for u.

2\theta  =  \pi  _ 2 

\theta  =  \pi  _ 4  So, the point  0,  \pi  _ 4   is a zero of the equation. Now let’s find the maximum value. Since the maximum of cos u = 1 when u = 0, the maximum cos 2\theta  = 1 when 2\theta  = 0. Thus,

r^{2} = 4cos(0)

r^{2} = 4(1) = 4

r = \pm  \sqrt{4}  = 2 We have a maximum at (2, 0). Since this graph is symmetric with respect to the pole, the line \theta  =  \pi  _ 2 , and the polar axis, we only need to plot points in the first quadrant. Make a table similar to Table 7. \theta   \pi  _ 6   \pi  _ 4   \pi  _ 3   \pi  _ 2  r \sqrt{2}  \sqrt{2}  Plot the points on the graph, such as the one shown in Figure 14.

**Analysis**
Making a substitution such as u = 2\theta  is a common practice in mathematics because it can make calculations simpler. However, we must not forget to replace the substitution term with the original term at the end, and then solve for the unknown. Some of the points on this graph may not show up using the Trace function on the TI-84 graphing calculator, and the calculator table may show an error for these same points of r. This is because there are no real square roots for these values of \theta . In other words, the corresponding r-values of \sqrt{4cos(2\theta} )  are complex numbers because there is a negative number under the radical. Investigating Rose Curves The next type of polar equation produces a petal-like shape called a rose curve. Although the graphs look complex, a simple polar equation generates the pattern.

rose curves The formulas that generate the graph of a rose curve are given by r = acos n\theta  and r = asin n\theta  where a \neq  0. If n is even, the curve has 2n petals. If n is odd, the curve has n petals. See Figure 15. r = acos(n\theta ), n even (a) r = asin(n\theta ), n odd (b)

**Example  8**

### Sketching the Graph of a Rose Curve (n Even)
Sketch the graph of r = 2cos 4\theta . Solution Testing for symmetry, we find again that the symmetry tests do not tell the whole story. The graph is not only symmetric with respect to the polar axis, but also with respect to the line \theta  =  \pi  _ 2  and the pole. Now we will find the zeros. First make the substitution u = 4\theta .

0 = 2cos 4\theta 

0 = cos 4\theta 

0 = cos u

cos-1 0 = u

u =  \pi  _ 2 

4\theta  =  \pi  _ 2 

\theta  =  \pi  _ 8  The zero is \theta  =  \pi  _ 8 . The point  0,  \pi  _ 8   is on the curve. Next, we find the maximum | r |. We know that the maximum value of cos u = 1 when \theta  = 0. Thus,

r = 2cos(4 ⋅ 0)

r = 2cos(0)

r = 2(1) = 2 The point (2, 0) is on the curve. The graph of the rose curve has unique properties, which are revealed in Table 8. \theta   \pi  _ 8   \pi  _ 4   3\pi  _ 8   \pi  _ 2   5\pi  _ 8   3\pi  _ 4  r -2 -2 As r = 0 when \theta  =  \pi  __ 8 , it makes sense to divide values in the table by  \pi  __ 8  units. A definite pattern emerges. Look at the range of r-values: 2, 0, -2, 0, 2, 0, -2, and so on. This represents the development of the curve one petal at a time. Starting at r = 0, each petal extends out a distance of r = 2, and then turns back to zero 2n times for a total of eight petals. See the graph in Figure 16.

n = 4 a

**Analysis**
When these curves are drawn, it is best to plot the points in order, as in the Table 8. This allows us to see how the graph hits a maximum (the tip of a petal), loops back crossing the pole, hits the opposite maximum, and loops back to the pole. The action is continuous until all the petals are drawn.

**Try It #4**
Sketch the graph of r = 4sin(2\theta ).

**Example  9**

### Sketching the Graph of a Rose Curve ( n Odd)
Sketch the graph of r = 2sin(5\theta ). Solution The graph of the equation shows symmetry with respect to the line \theta  =  \pi  _ 2 . Next, find the zeros and maximum. We will want to make the substitution u = 5\theta .

0 = 2sin(5\theta )

0 = sin u

sin-1 0 = 0

u = 0

5\theta  = 0

\theta  = 0 The maximum value is calculated at the angle where sin \theta  is a maximum. Therefore,

r = 2sin 5 ⋅  \pi  _ 2  

r = 2(1) = 2 Thus, the maximum value of the polar equation is 2. This is the length of each petal. As the curve for n odd yields the same number of petals as n, there will be five petals on the graph. See Figure 17. a Create a table of values similar to Table 9. \theta   \pi  _ 6   \pi  _ 3   \pi  _ 2   2\pi  _ 3   5\pi  _ 6  \pi  r -1.73 -1.73


**Try It #5**
Sketch the graph of r = 3cos(3\theta ). Investigating the Archimedes’ Spiral The final polar equation we will discuss is the Archimedes’ spiral, named for its discoverer, the Greek mathematician Archimedes (c. 287 BCE–c. 212 BCE), who is credited with numerous discoveries in the fields of geometry and mechanics. Archimedes’ spiral The formula that generates the graph of the Archimedes’ spiral is given by r = \theta  for \theta  \ge  0. As \theta  increases, r increases at a constant rate in an ever-widening, never-ending, spiraling path. See Figure 18. r = \theta , [0, 2\pi ] (a) r = \theta , [0, 4\pi ] (b)

**How To…**
Given an Archimedes’ spiral over [0, 2\pi ], sketch the graph. 1. Make a table of values for r and \theta  over the given domain. 2. Plot the points and sketch the graph.

**Example  10**

### Sketching the Graph of an Archimedes’ Spiral
Sketch the graph of r = \theta  over [0, 2\pi ]. Solution As r is equal to \theta , the plot of the Archimedes’ spiral begins at the pole at the point (0, 0). While the graph hints of symmetry, there is no formal symmetry with regard to passing the symmetry tests. Further, there is no maximum value, unless the domain is restricted. Create a table such as Table 10. \theta   \pi  _ 4   \pi  _ 2  \pi   3\pi  _ 2   7\pi  _ 4  2\pi  r 0.785 1.57 3.14 4.71 5.50 6.28 Notice that the r-values are just the decimal form of the angle measured in radians. We can see them on a graph in (\pi , \pi )


**Analysis**
The domain of this polar curve is [0, 2\pi ]. In general, however, the domain of this function is (-\infty , \infty ). Graphing the equation of the Archimedes’ spiral is rather simple, although the image makes it seem like it would be complex.

**Try It #6**
Sketch the graph of r = -\theta  over the interval [0, 4\pi ]. Summary of Curves We have explored a number of seemingly complex polar curves in this section. Figure 20 and Figure 21 summarize the graphs and equations for each of these curves. r = asin \theta  r = acos \theta  r = a \pm  bcos \theta  r = a \pm  bsin \theta  r = a \pm  bcos \theta  r = a \pm  bsin \theta  r = a \pm  bcos \theta  r = a \pm  bsin \theta  a > 0, b > 0, a < b a > 0, b > 0, 1 < a/b < 2 a > 0, b > 0, a/b = 1 (a) Circle Cardioid One-Loop Limaçon Inner-Loop Limaçon (b) (c) (d) r^{2} = a^{2}cos 2\theta  r^{2} = a^{2}sin 2\theta  a \neq  0 (a) Lemniscate Rose Curve (n even) Rose Curve (n odd) Archimedes’ Spiral r = acos n\theta  r = asin n\theta  n even, 2n petals (b) n odd, n petals r = acos n\theta  r = asin n\theta  (c) r = \theta  \theta  \ge  0 (d) Access these online resources for additional instruction and practice with graphs of polar coordinates. • Graphing Polar Equations Part 1 (http://openstaxcollege.org/l/polargraph^{1}) • Graphing Polar Equations Part 2 (http://openstaxcollege.org/l/polargraph^{2}) • Animation: The Graphs of Polar Equations (http://openstaxcollege.org/l/polaranim) • Graphing Polar Equations on the TI-84 (http://openstaxcollege.org/l/polarTI^{8}4)


## 8.4 Section Exercises

### 8.4 Section Exercises
Verbal 1. Describe the three types of symmetry in polar graphs, and compare them to the symmetry of the Cartesian plane. 2. Which of the three types of symmetries for polar graphs correspond to the symmetries with respect to the x-axis, y-axis, and origin? 3. What are the steps to follow when graphing polar equations? 4. Describe the shapes of the graphs of cardioids, limaçons, and lemniscates. 5. What part of the equation determines the shape of the graph of a polar equation? Graphical For the following exercises, test the equation for symmetry. 6. r = 5cos 3\theta  7. r = 3 - 3cos \theta  8. r = 3 + 2sin \theta  9. r = 3sin 2\theta  12. r = 4cos  \theta  _ 2  13. r =  2 _ \theta   14. r = 3\sqrt{1-cos^{2}\theta}   15. r = \sqrt{5sin} 2\theta   For the following exercises, graph the polar equation. Identify the name of the shape. 16. r = 3cos \theta  17. r = 4sin \theta  18. r = 2 + 2cos \theta  19. r = 2 - 2cos \theta  20. r = 5 - 5sin \theta  21. r = 3 + 3sin \theta  22. r = 3 + 2sin \theta  23. r = 7 + 4sin \theta  24. r = 4 + 3cos \theta  25. r = 5 + 4cos \theta  26. r = 10 + 9cos \theta  27. r = 1 + 3sin \theta  28. r = 2 + 5sin \theta  29. r = 5 + 7sin \theta  30. r = 2 + 4cos \theta  31. r = 5 + 6cos \theta  32. r 2 = 36cos(2\theta ) 33. r 2 = 10cos(2\theta ) 34. r 2 = 4sin(2\theta ) 35. r 2 = 10sin(2\theta ) 36. r = 3sin(2\theta ) 37. r = 3cos(2\theta ) 38. r = 5sin(3\theta ) 39. r = 4sin(4\theta ) 40. r = 4sin(5\theta ) 41. r = -\theta  43. r = - 3\theta  Technology For the following exercises, use a graphing calculator to sketch the graph of the polar equation. 44. r =  1 _ \theta   45. r =  1 _ \sqrt{\theta}    46. r = 2sin \theta  tan \theta , a cissoid 47. r = 2\sqrt{1} - sin^{2} \theta  , a hippopede 48. r = 5 + cos(4\theta ) 49. r = 2 - sin(2\theta ) 51. r = \theta  + 1 52. r = \theta sin \theta  53. r = \theta cos \theta  For the following exercises, use a graphing utility to graph each pair of polar equations on a domain of [0, 4\pi ] and then explain the differences shown in the graphs. 54. r = \theta , r = -\theta  55. r = \theta , r = \theta  + sin \theta  56. r = sin \theta  + \theta , r = sin \theta  - \theta  57. r = 2sin  \theta  _ 2  , r = \theta sin  \theta  _ 2   58. r = sin(cos(3\theta )) r = sin(3\theta )

59. On a graphing utility, graph r = sin  16 _ 5 \theta   on [0, 4\pi ], [0, 8\pi ], [0, 12\pi ], and [0, 16\pi ]. Describe the effect of increasing the width of the domain. 60. On a graphing utility, graph and sketch r = sin \theta  +  sin   5 _ 2 \theta    61. On a graphing utility, graph each polar equation. Explain the similarities and differences you observe in the graphs. r^{1} = 3sin(3\theta ) r^{2} = 2sin(3\theta ) r^{3} = sin(3\theta ) 62. On a graphing utility, graph each polar equation. Explain the similarities and differences you observe in the graphs. r^{1} = 3 + 3cos \theta  r^{2} = 2 + 2cos \theta  r^{3} = 1 + cos \theta  63. On a graphing utility, graph each polar equation. Explain the similarities and differences you observe in the graphs.

r^{1} = 3\theta 

r^{2} = 2\theta 

r^{3} = \theta  Extensions For the following exercises, draw each polar equation on the same set of polar axes, and find the points of intersection. 64. r^{1} = 3 + 2sin \theta , r^{2} = 2 65. r^{1} = 6 - 4cos \theta , r^{2} = 4 66. r^{1} = 1 + sin \theta , r^{2} = 3sin \theta  67. r^{1} = 1 + cos \theta , r^{2} = 3cos \theta  68. r^{1} = cos(2\theta ), r^{2} = sin(2\theta ) 69. r^{1} = sin^{2} (2\theta ), r^{2} = 1 - cos(4\theta ) 70. r^{1} = \sqrt{3} , r^{2} = 2sin(\theta ) 2 = sin \theta , r^{2} 2 = cos \theta  72. r^{1} = 1 + cos \theta , r^{2} = 1 - sin \theta 


## 8.5 Polar Form of Complex Numbers
Learning Objectives
In this section, you will:
• Plot complex numbers in the complex plane.
• Find the absolute value of a complex number.
• Write complex numbers in polar form.
• Convert a complex number from polar to rectangular form.
• Find products of complex numbers in polar form.
• Find quotients of complex numbers in polar form.
• Find powers of complex numbers in polar form.
• Find roots of complex numbers in polar form.
“God made the integers; all else is the work of man.” This rather famous quote by nineteenth-century German mathematician Leopold Kronecker sets the stage for this section on the polar form of a complex number. Complex numbers were invented by people and represent over a thousand years of continuous investigation and struggle by mathematicians such as Pythagoras, Descartes, De Moivre, Euler, Gauss, and others. Complex numbers answered questions that for centuries had puzzled the greatest minds in science. We first encountered complex numbers in Complex Numbers. In this section, we will focus on the mechanics of working with complex numbers: translation of complex numbers from polar form to rectangular form and vice versa, interpretation of complex numbers in the scheme of applications, and application of De Moivre’s Theorem. Plotting Complex Numbers in the Complex Plane Plotting a complex number a + bi is similar to plotting a real number, except that the horizontal axis represents the real part of the number, a, and the vertical axis represents the imaginary part of the number, bi.

**How To…**
Given a complex number a + bi, plot it in the complex plane. 1. Label the horizontal axis as the real axis and the vertical axis as the imaginary axis. 2. Plot the point in the complex plane by moving a units in the horizontal direction and b units in the vertical direction.

**Example  1**

### Plotting a Complex Number in the Complex Plane
Plot the complex number 2 - 3i in the complex plane. Solution From the origin, move two units in the positive horizontal direction and three units in the negative vertical direction. See Figure 1. Real Imaginary 2 – 3i


**Try It #1**
Plot the point 1 + 5i in the complex plane. Finding the Absolute Value of a Complex Number The first step toward working with a complex number in polar form is to find the absolute value. The absolute value of a complex number is the same as its magnitude, or ∣ z ∣. It measures the distance from the origin to a point in the plane. For example, the graph of z = 2 + 4i, in Figure 2, shows ∣ z ∣. Real Imaginary (2 + 4i) |z| = absolute value of a complex number Given z = x + yi, a complex number, the absolute value of z is defined as

∣ z ∣ = \sqrt{x^{2}} + y^{2}  It is the distance from the origin to the point (x, y). Notice that the absolute value of a real number gives the distance of the number from 0, while the absolute value of a complex number gives the distance of the number from the origin, (0, 0).

**Example  2**
Finding the Absolute Value of a Complex Number with a Radical Find the absolute value of z = \sqrt{5}  - i. Solution Using the formula, we have

∣ z ∣ = \sqrt{x^{2}} + y^{2} 

∣ z ∣ = \sqrt{\sqrt{}} 5 2 + (-1)^{2} 

∣ z ∣ = \sqrt{5} + 1 

∣ z ∣ = \sqrt{6}  See Figure 3. Real Imaginary


**Try It #2**
Find the absolute value of the complex number z = 12 - 5i.

**Example  3**
Finding the Absolute Value of a Complex Number Given z = 3 - 4i, find ∣ z ∣. Solution Using the formula, we have

∣ z ∣ = \sqrt{x^{2}}+ y^{2} 

∣ z ∣ = \sqrt{(3})^{2} + (-4)^{2} 

∣ z ∣ = \sqrt{∣} z ∣ = \sqrt{25} 

∣ z ∣ = 5 The absolute value of z is 5. See Figure 4. Real Imaginary |z| = 5 (3 - 4i)

**Try It #3**
Given z =1 - 7i, find ∣ z ∣. Writing Complex Numbers in Polar Form The polar form of a complex number expresses a number in terms of an angle \theta  and its distance from the origin r. Given a complex number in rectangular form expressed as z = x + yi, we use the same conversion formulas as we do to write the number in trigonometric form:

x = rcos \theta 

y = rsin \theta 

r = \sqrt{x^{2}}+ y^{2}  We review these relationships in Figure 5. Real Imaginary r \theta  y x x + yi

We use the term modulus to represent the absolute value of a complex number, or the distance from the origin to the point (x, y). The modulus, then, is the same as r, the radius in polar form. We use \theta  to indicate the angle of direction (just as with polar coordinates). Substituting, we have

z = x + yi

z = rcos \theta  + (rsin \theta )i

z = r(cos \theta  + isin \theta ) polar form of a complex number Writing a complex number in polar form involves the following conversion formulas:

x = rcos \theta 

y = rsin \theta 

r = \sqrt{x^{2}}+ y^{2}  Making a direct substitution, we have

z = x + yi

z = (rcos \theta ) + i(rsin \theta )

z = r(cos \theta  + isin \theta ) where r is the modulus and \theta  is the argument. We often use the abbreviation rcis \theta  to represent r(cos \theta  + isin \theta ).

**Example  4**

### Expressing a Complex Number Using Polar Coordinates
Express the complex number 4i using polar coordinates. Solution On the complex plane, the number z = 4i is the same as z = 0 + 4i. Writing it in polar form, we have to calculate r first.

r = \sqrt{x^{2}}+ y^{2} 

r = \sqrt{r} = \sqrt{16} 

r = 4 Next, we look at x. If x = rcos \theta , and x = 0, then \theta  =  \pi  _ 2 . In polar coordinates, the complex number z = 0 + 4i can be written as z = 4 cos   \pi  _ 2   + isin   \pi  _ 2    or 4cis   \pi  _ 2  . See Figure 6. Real Imaginary z = 4i \pi 

**Try It #4**
Express z = 3i as rcis \theta  in polar form.


**Example  5**
Finding the Polar Form of a Complex Number Find the polar form of -4 + 4i. Solution First, find the value of r.

r = \sqrt{x^{2}}+ y^{2} 

r = \sqrt{(-4})^{2} + (42) 

r = \sqrt{32} 

r = 4\sqrt{2}  Find the angle \theta  using the formula:

cos \theta  =  x _ r 

cos \theta  =  -4 ______ 4\sqrt{2}  

cos \theta  = -  1 _____ \sqrt{2}  

\theta  = cos-1  -  1 _____ \sqrt{2}   =  3\pi  _ 4  Thus, the solution is 4\sqrt{2} cis  3\pi  _ 4   .

**Try It #5**
Write z = \sqrt{_}

3  + i in polar form. Converting a Complex Number from Polar to Rectangular Form Converting a complex number from polar form to rectangular form is a matter of evaluating what is given and using the distributive property. In other words, given z = r(cos \theta  + isin \theta ), first evaluate the trigonometric functions cos \theta  and sin \theta . Then, multiply through by r.

**Example  6**
Converting from Polar to Rectangular Form Convert the polar form of the given complex number to rectangular form:

z = 12 cos   \pi  _ 6   + isin   \pi  _ 6    Solution We begin by evaluating the trigonometric expressions.

cos   \pi  _ 6   =  \sqrt{3}  _ 2  and sin   \pi  _ 6   =  1 _ 2  After substitution, the complex number is

z = 12  \sqrt{3}  _ 2  +  1 _ 2 i  We apply the distributive property:

z = 12  \sqrt{3}  _ 2  +  1 _ 2 i 

= (12) \sqrt{3}  _ 2  + (12) 1 _ 2 i

= 6\sqrt{3}  + 6i The rectangular form of the given point in complex form is 6\sqrt{3}  + 6i.


**Example  7**
Finding the Rectangular Form of a Complex Number Find the rectangular form of the complex number given r = 13 and tan \theta  =  5 _ 12 . Solution If tan \theta  =  5 _ 12 , and tan \theta  =  y _ x , we first determine r = \sqrt{x^{2}}+ y^{2}  = \sqrt{122} + 52  = 13. We then find cos \theta  =  x _ r  and sin \theta  =  y _ r .

z = 13(cos \theta  + isin \theta )

_ 13  +  5 _ 13 i 

= 12 + 5i The rectangular form of the given number in complex form is 12 + 5i.

**Try It #6**
Convert the complex number to rectangular form:

z = 4 cos  11\pi  _ 6  + isin  11\pi  _ 6   Finding Products of Complex Numbers in Polar Form Now that we can convert complex numbers to polar form we will learn how to perform operations on complex numbers in polar form. For the rest of this section, we will work with formulas developed by French mathematician Abraham De Moivre (1667–1754). These formulas have made working with products, quotients, powers, and roots of complex numbers much simpler than they appear. The rules are based on multiplying the moduli and adding the arguments. products of complex numbers in polar form If z^{1} = r^{1}(cos \theta 1 + isin \theta 1) and z^{2} = r^{2}(cos \theta 2 + isin \theta 2), then the product of these numbers is given as:

z^{1}z^{2} = r^{1}r^{2}[cos(\theta 1 + \theta 2) + isin(\theta 1 + \theta 2)]

z^{1}z^{2} = r^{1}r^{2}cis(\theta 1 + \theta 2) Notice that the product calls for multiplying the moduli and adding the angles.

**Example  8**
Finding the Product of Two Complex Numbers in Polar Form Find the product of z^{1}z^{2}, given z^{1} = 4(cos(80°) + isin(80°)) and z^{2} = 2(cos(145°) + isin(145°)). Solution Follow the formula

z^{1}z^{2} = 4 ⋅ 2[cos(80° + 145°) + isin(80° + 145°)]

z^{1}z^{2} = 8[cos(225°) + isin(225°)]

z^{1}z^{2} = 8 cos   5\pi  _ 4   + isin   5\pi  _ 4    

z^{1}z^{2} = 8 -  \sqrt{2}  _ 2  + i  -  \sqrt{2}  _ 2    

z^{1}z^{2} = - 4\sqrt{2}  - 4i\sqrt{2}  Finding Quotients of Complex Numbers in Polar Form The quotient of two complex numbers in polar form is the quotient of the two moduli and the difference of the two arguments.

quotients of complex numbers in polar form If z^{1} = r^{1}(cos \theta 1 + isin \theta 1) and z^{2} = r^{2}(cos \theta 2 + isin \theta 2), then the quotient of these numbers is

 z^{1} __ z^{2}  =  r^{1} __ r^{2} [cos(\theta 1 -\theta 2) + isin(\theta 1 - \theta 2)], z^{2} \neq  0

 z^{1} __ z^{2}  =  r^{1} __ r^{2}  cis(\theta 1 - \theta 2), z^{2} \neq  0 Notice that the moduli are divided, and the angles are subtracted.

**How To…**
Given two complex numbers in polar form, find the quotient. 1. Divide  r^{1} __ r^{2} . 2. Find \theta 1 - \theta 2. 3. Substitute the results into the formula: z = r(cos \theta  + isin \theta ). Replace r with  r^{1} __ r^{2} , and replace \theta  with \theta 1 - \theta 2. 4. Calculate the new trigonometric expressions and multiply through by r.

**Example  9**
Finding the Quotient of Two Complex Numbers Find the quotient of z^{1} = 2(cos(213°) + isin(213°)) and z^{2} = 4(cos(33°) + isin(33°)). Solution Using the formula, we have

 z^{1} __ z^{2}  =  2 __ 4 [cos(213° - 33°) + isin(213° - 33°)]

 z^{1} __ z^{2}  =  1 __ 2 [cos(180°) + isin(180°)]

 z^{1} __ z^{2}  =  1 __ 2 [ - 1 + 0i]

 z^{1} __ z^{2}  = -  1 __ 2 + 0i

 z^{1} __ z^{2}  = -  1 __ 2 

**Try It #7**
Find the product and the quotient of z^{1} = 2\sqrt{3} (cos(150°) + isin(150°)) and z^{2} = 2(cos(30°) + isin(30°)). Finding Powers of Complex Numbers in Polar Form Finding powers of complex numbers is greatly simplified using De Moivre’s Theorem. It states that, for a positive integer n, zn is found by raising the modulus to the nth power and multiplying the argument by n. It is the standard method used in modern mathematics. De Moivre’s Theorem If z = r(cos \theta  + isin \theta ) is a complex number, then

zn = r n[cos(n\theta ) + isin(n\theta )]

zn = r n cis(n\theta ) where n is a positive integer.


**Example  10**

### Evaluating an Expression Using De Moivre’s Theorem
Evaluate the expression (1 + i)^{5} using De Moivre’s Theorem. Solution Since De Moivre’s Theorem applies to complex numbers written in polar form, we must first write (1 + i) in polar form. Let us find r.

r = \sqrt{x^{2}} + y^{2} 

r = \sqrt{(1})^{2} + (1)^{2} 

r = \sqrt{2}  Then we find \theta . Using the formula tan \theta  =  y _ x  gives

tan \theta  =  1 _ 1 

tan \theta  = 1

\theta  =  \pi  _ 4  Use De Moivre’s Theorem to evaluate the expression.

(a + bi)n = rn[cos(n\theta ) + isin(n\theta )]

(1 + i)^{5} = (\sqrt{2} )^{5} cos  5 ⋅  \pi  _ 4  + isin  5 ⋅  \pi  _ 4    

(1 + i)^{5} = 4\sqrt{2}   cos   5\pi  _ 4   + isin   5\pi  _ 4    

(1 + i)^{5} = 4\sqrt{2}   -  \sqrt{2}  _ 2  + i  -  \sqrt{2}  _ 2    

(1 + i)^{5} = - 4 - 4i Finding Roots of Complex Numbers in Polar Form To find the nth root of a complex number in polar form, we use the nth Root Theorem or De Moivre’s Theorem and raise the complex number to a power with a rational exponent. There are several ways to represent a formula for finding nth roots of complex numbers in polar form. the nth root theorem To find the nth root of a complex number in polar form, use the formula given as

z 1 __ n  = r 1 __ n  cos   \theta  _ n +  2k\pi  _ n   + isin   \theta  _ n +  2k\pi  _ n     where k = 0, 1, 2, 3, . . . , n - 1. We add  2k\pi  _ n  to  \theta  _ n  in order to obtain the periodic roots.


**Example  11**
Finding the nth Root of a Complex Number Evaluate the cube roots of z = 8 cos   2\pi  ___ 3    + isin   2\pi  ___ 3     . Solution We have

z  1 __ 3  = 8  1 __ 3  cos    2\pi  ___ 3 

_ 3 +  2k\pi  ____ 3   + isin    2\pi  ___ 3 

_ 3 +  2k\pi  ____ 3     

z  1 __ 3  = 2 cos   2\pi  ___ 9  +  2k\pi  ____ 3   + isin   2\pi  ___ 9  +  2k\pi  ____ 3      There will be three roots: k = 0, 1, 2. When k = 0, we have

z  1 __ 3  = 2 cos   2\pi  ___ 9   + isin   2\pi  ___ 9      When k = 1, we have

z  1 __ 3  = 2 cos   2\pi  ___ 9  +  6\pi  ___ 9   + isin   2\pi  ___ 9  +  6\pi  ___ 9      Add  2(1)\pi  _  to each angle.

z  1 __ 3  = 2 cos   8\pi  ___ 9   + isin   8\pi  ___ 9      When k = 2, we have

z  1 __ 3  = 2 cos   2\pi  ___ 9  +  12\pi  ____ 9   + isin   2\pi  ___ 9  +  12\pi  ____ 9      Add  2(2)\pi  _  to each angle.

z  1 __ 3  = 2 cos   14\pi  ____ 9   + isin   14\pi  ____ 9      Remember to find the common denominator to simplify fractions in situations like this one. For k = 1, the angle simplification is

  2\pi  ___ 3 

_ 3  +  2(1)\pi  _____ 3  =  2\pi  ___ 3   1 __ 3    +  2(1)\pi  _____ 3   3 __ 3   

=  2\pi  ___ 9  +  6\pi  ___ 9 

=  8\pi  ___ 9 

**Try It #8**
Find the four fourth roots of 16(cos(120°) + isin(120°)). Access these online resources for additional instruction and practice with polar forms of complex numbers. • The Product and Quotient of Complex Numbers in Trigonometric Form (http://openstaxcollege.org/l/prodquocomplex) • De Moivre’s Theorem (http://openstaxcollege.org/l/demoivre)


### 8.5 Section Exercises
Verbal 1. A complex number is a + bi. Explain each part. 2. What does the absolute value of a complex number represent? 3. How is a complex number converted to polar form? 4. How do we find the product of two complex numbers? 5. What is De Moivre’s Theorem and what is it used for? Algebraic For the following exercises, find the absolute value of the given complex number. 7. -7 + i 9. \sqrt{_}

2  - 6i For the following exercises, write the complex number in polar form. __ 2  -  1 __ 2  i 3  + i For the following exercises, convert the complex number from polar to rectangular form. 17. z = 7cis   \pi  _ 6    18. z = 2cis   \pi  _ 3    19. z = 4cis   7\pi  _ 6    20. z = 7cis(25°) 22. z = \sqrt{2} cis(100°) For the following exercises, find z^{1} z^{2} in polar form. 3 cis(116°); z^{2} = 2cis(82°) 24. z^{1} = \sqrt{2} cis(205°); z^{2} = 2\sqrt{2} cis(118°) 25. z^{1} = 3cis(120°); z^{2} =  1 _ 4 cis(60°) 26. z^{1} = 3cis   \pi  _ 4   ; z^{2} = 5cis   \pi  _ 6    27. z^{1} = \sqrt{5} cis   5\pi  _ 8   ; z^{2} = \sqrt{15}  cis   \pi  _ 12    28. z^{1} = 4cis   \pi  _ 2   ; z^{2} = 2cis   \pi  _ 4    For the following exercises, find  z^{1} _ z^{2}  in polar form. 30. z^{1} = \sqrt{2} cis(90°); z^{2} = 2cis(60°) 32. z^{1} = 6cis   \pi  _ 3   ; z^{2} = 2cis   \pi  _ 4    2 cis(\pi ); z^{2} = \sqrt{2} cis   2\pi  _ 3    34. z^{1} = 2cis   3\pi  _ 5   ; z^{2} = 3cis   \pi  _ 4    For the following exercises, find the powers of each complex number in polar form. 35. Find z^{3} when z = 5cis(45°). 36. Find z^{4} when z = 2cis(70°). 37. Find z^{2} when z = 3cis(120°). 38. Find z^{2} when z = 4cis   \pi  _ 4   . 39. Find z^{4} when z = cis   3\pi  _ 16   . 40. Find z^{3} when z = 3cis   5\pi  _ 3   .


## 8.5 Section Exercises
For the following exercises, evaluate each root. 41. Evaluate the cube root of z when z = 27cis(240°). 42. Evaluate the square root of z when z = 16cis(100°). 43. Evaluate the cube root of z when z = 32cis   2\pi  _ 3   . 44. Evaluate the square root of z when z = 32cis(\pi ). 45. Evaluate the cube root of z when z = 8cis   7\pi  _ 4   . Graphical For the following exercises, plot the complex number in the complex plane. Technology For the following exercises, find all answers rounded to the nearest hundredth. 56. Use the rectangular to polar feature on the graphing calculator to change 5 + 5i to polar form. 57. Use the rectangular to polar feature on the graphing calculator to change 3 - 2i to polar form. 58. Use the rectangular to polar feature on the graphing calculator to change -3 - 8i to polar form. 59. Use the polar to rectangular feature on the graphing calculator to change 4cis(120°) to rectangular form. 60. Use the polar to rectangular feature on the graphing calculator to change 2cis(45°) to rectangular form. 61. Use the polar to rectangular feature on the graphing calculator to change 5cis(210°) to rectangular form.


## 8.6 Parametric Equations
Consider the path a moon follows as it orbits a planet, which simultaneously rotates around the sun, as seen in Figure 1. At any moment, the moon is located at a particular spot relative to the planet. But how do we write and solve the equation for the position of the moon when the distance from the planet, the speed of the moon’s orbit around the planet, and the speed of rotation around the sun are all unknowns? We can solve only for one variable at a time. In this section, we will consider sets of equations given by x(t) and y(t) where t is the independent variable of time. We can use these parametric equations in a number of applications when we are looking for not only a particular position but also the direction of the movement. As we trace out successive values of t, the orientation of the curve becomes clear. This is one of the primary advantages of using parametric equations: we are able to trace the movement of an object along a path according to time. We begin this section with a look at the basic components of parametric equations and what it means to parameterize a curve. Then we will learn how to eliminate the parameter, translate the equations of a curve defined parametrically into rectangular equations, and find the parametric equations for curves defined by rectangular equations. Parameterizing a Curve When an object moves along a curve—or curvilinear path—in a given direction and in a given amount of time, the position of the object in the plane is given by the x-coordinate and the y-coordinate. However, both x and y vary over time and so are functions of time. For this reason, we add another variable, the parameter, upon which both x and y are dependent functions. In the example in the section opener, the parameter is time, t. The x position of the moon at time, t, is represented as the function x(t), and the y position of the moon at time, t, is represented as the function y(t). Together, x(t) and y(t) are called parametric equations, and generate an ordered pair (x(t), y(t)). Parametric equations primarily describe motion and direction. When we parameterize a curve, we are translating a single equation in two variables, such as x and y, into an equivalent pair of equations in three variables, x, y, and t. One of the reasons we parameterize a curve is because the parametric equations yield more information: specifically, the direction of the object’s motion over time. When we graph parametric equations, we can observe the individual behaviors of x and of y. There are a number of shapes that cannot be represented in the form y = f (x), meaning that they are not functions. For example, consider the graph of a circle, given as r 2 = x 2 + y 2. Solving for y gives y = \pm  \sqrt{r^{2}} - x^{2} , or two equations: y^{1} = \sqrt{r^{2}} - x^{2}  and y^{2} = -\sqrt{r^{2}} - x^{2} . If we graph y^{1} and y^{2} together, the graph will not pass the vertical line test, as shown in Figure 2. Thus, the equation for the graph of a circle is not a function. Learning Objectives
In this section, you will:
• Parameterize a curve.
• Eliminate the parameter.
• Find a rectangular equation for a curve defined parametrically.
• Find parametric equations for curves defined by rectangular equations.
x y Vertical line test on circle r^{2} = x^{2} + y^{2} However, if we were to graph each equation on its own, each one would pass the vertical line test and therefore would represent a function. In some instances, the concept of breaking up the equation for a circle into two functions is similar to the concept of creating parametric equations, as we use two functions to produce a non-function. This will become clearer as we move forward. parametric equations Suppose t is a number on an interval, I. The set of ordered pairs, (x(t), y(t)), where x = f (t) and y = g(t), forms a plane curve based on the parameter t. The equations x = f (t) and y = g(t) are the parametric equations.

**Example  1**
Parameterizing a Curve Parameterize the curve y = x^{2} - 1 letting x(t) = t. Graph both equations. Solution If x(t) = t, then to find y(t) we replace the variable x with the expression given in x(t). In other words, y(t) = t 2 - 1. Make a table of values similar to Table 1, and sketch the graph. t x(t) y(t) -4 -4 y(-4) = (-4)^{2} - 1 = 15 -3 -3 y(-3) = (-3)^{2} - 1 = 8 -2 -2 y(-2) = (-2)^{2} - 1 = 3 -1 -1 y(-1) = (-1)^{2} - 1 = 0 y(0) = (0)^{2} - 1 = - 1 y(1) = (1)^{2} - 1 = 0 y(2) = (2)^{2} - 1 = 3 y(3) = (3)^{2} - 1 = 8 y(4) = (4)^{2} - 1 = 15 See the graphs in Figure 3. It may be helpful to use the TRACE feature of a graphing calculator to see how the points are generated as t increases. x y (a) x y (b) (a) Parametric y(t ) = t 2 - 1 (b) Rectangular y = x 2 - 1


**Analysis**
The arrows indicate the direction in which the curve is generated. Notice the curve is identical to the curve of y = x^{2} - 1.

**Try It #1**
Construct a table of values and plot the parametric equations: x(t) = t - 3, y(t) = 2t + 4; - 1 \le  t \le  2.

**Example  2**
Finding a Pair of Parametric Equations Find a pair of parametric equations that models the graph of y = 1 - x^{2}, using the parameter x(t) = t. Plot some points and sketch the graph. Solution If x(t) = t and we substitute t for x into the y equation, then y(t) = 1 - t^{2}. Our pair of parametric equations is

x(t) = t

y(t) = 1 - t^{2} To graph the equations, first we construct a table of values like that in Table 2. We can choose values around t = 0, from t = - 3 to t = 3. The values in the x(t) column will be the same as those in the t column because x(t) = t. Calculate values for the column y(t). t x(t) = t y(t) = 1 - t^{2} -3 -3 y(-3) = 1 - (-3)^{2} = - 8 -2 -2 y(-2) = 1 - (-2)^{2} = - 3 -1 -1 y(-1) = 1 - (-1)^{2} = 0 y(0) = 1 - 0 = 1 y(1) = 1 - (1)^{2} = 0 y(2) = 1 - (2)^{2} = - 3 y(3) = 1 - (3)^{2} = - 8 The graph of y = 1 - t^{2} is a parabola facing downward, as shown in Figure 4. We have mapped the curve over the interval [-3, 3], shown as a solid line with arrows indicating the orientation of the curve according to t. Orientation refers to the path traced along the curve in terms of increasing values of t. As this parabola is symmetric with respect to the line x = 0, the values of x are reflected across the y-axis. x y

**Try It #2**
Parameterize the curve given by x = y^{3} - 2y.


**Example  3**
Finding Parametric Equations That Model Given Criteria An object travels at a steady rate along a straight path (-5, 3) to (3, -1) in the same plane in four seconds. The coordinates are measured in meters. Find parametric equations for the position of the object. Solution The parametric equations are simple linear expressions, but we need to view this problem in a step-by-step fashion. The x-value of the object starts at -5 meters and goes to 3 meters. This means the distance x has changed by 8 meters in 4 seconds, which is a rate of  8m _ 4s , or 2 m/s. We can write the x-coordinate as a linear function with respect to time as x(t) = 2t - 5. In the linear function template y = mx + b, 2t = mx and -5 = b. Similarly, the y-value of the object starts at 3 and goes to -1, which is a change in the distance y of -4 meters in 4 seconds, which is a rate of  -4m _ 4s , or -1 m/s. We can also write the y-coordinate as the linear function y(t) = -t + 3. Together, these are the parametric equations for the position of the object, where x and y are expressed in meters and t represents time:

x(t) = 2t - 5

y(t) = -t + 3 Using these equations, we can build a table of values for t, x, and y (see Table 3). In this example, we limited values of t to non-negative numbers. In general, any value of t can be used. t x(t) = 2t - 5 y(t) = -t + 3 x = 2(0) - 5 = -5 y = -(0) + 3 = 3 x = 2(1) - 5 = -3 y = -(1) + 3 = 2 x = 2(2) - 5 = -1 y = -(2) + 3 = 1 x = 2(3) - 5 = 1 y = -(3) + 3 = 0 x = 2(4) - 5 = 3 y = -(4) + 3 = - 1 From this table, we can create three graphs, as shown in Figure 5. t x (a) t y (b) x y t =1 t =3 (c) (a) A graph of x vs. t, representing the horizontal position over time. (b) A graph of y vs. t, representing the vertical position over time. (c) A graph of y vs. x, representing the position of the object in the plane at time t.

**Analysis**
Again, we see that, in Figure 5(c), when the parameter represents time, we can indicate the movement of the object along the path with arrows. Eliminating the Parameter In many cases, we may have a pair of parametric equations but find that it is simpler to draw a curve if the equation involves only two variables, such as x and y. Eliminating the parameter is a method that may make graphing some curves easier. However, if we are concerned with the mapping of the equation according to time, then it will be necessary to indicate the orientation of the curve as well. There are various methods for eliminating the parameter t from a set of parametric equations; not every method works for every type of equation. Here we will review the methods for the most common types of equations.

Eliminating the Parameter from Polynomial, Exponential, and Logarithmic Equations For polynomial, exponential, or logarithmic equations expressed as two parametric equations, we choose the equation that is most easily manipulated and solve for t. We substitute the resulting expression for t into the second equation. This gives one equation in x and y.

**Example  4**
Eliminating the Parameter in Polynomials Given x(t) = t^{2} + 1 and y(t) = 2 + t, eliminate the parameter, and write the parametric equations as a Cartesian equation. Solution We will begin with the equation for y because the linear equation is easier to solve for t.

y = 2 + t

y - 2 = t Next, substitute y - 2 for t in x(t).

x = t^{2} + 1

x = (y - 2)^{2} + 1 Substitute the expression for t into x.

x = y^{2} - 4y + 4 + 1

x = y^{2} - 4y + 5

x = y^{2} - 4y + 5 The Cartesian form is x = y^{2} - 4y + 5.

**Analysis**
This is an equation for a parabola in which, in rectangular terms, x is dependent on y. From the curve’s vertex at (1, 2), the graph sweeps out to the right. See Figure 6. In this section, we consider sets of equations given by the functions x(t) and y(t), where t is the independent variable of time. Notice, both x and y are functions of time; so in general y is not a function of x. x y

**Try It #3**
Given the equations below, eliminate the parameter and write as a rectangular equation for y as a function of x.

x(t) = 2t^{2} + 6

y(t) = 5 - t

**Example  5**
Eliminating the Parameter in Exponential Equations Eliminate the parameter and write as a Cartesian equation: x(t) = e-t and y(t) = 3et, t > 0. Solution Isolate et.

x = e-t

et =  1 _ x 

Substitute the expression into y(t).

y = 3et

y = 3  1 _ x  

y =  3 _ x  The Cartesian form is y =  3 _ x 

**Analysis**
The graph of the parametric equation is shown in Figure 7(a). The domain is restricted to t > 0. The Cartesian equation, y = 3x is shown in Figure 7(b) and has only one restriction on the domain, x \neq  0. x y (a) (b) x(t) = e-t y(t) = 3et x y 3x y =

**Example  6**
Eliminating the Parameter in Logarithmic Equations Eliminate the parameter and write as a Cartesian equation: x(t) = \sqrt{—} t  + 2 and y(t) = log(t). Solution Solve the first equation for t.

x = \sqrt{—} t  + 2

x - 2 = \sqrt{—} t 

(x - 2)^{2} = t Square both sides. Then, substitute the expression for t into the y equation.

y = log(t)

y = log(x - 2)^{2} The Cartesian form is y = log(x - 2)^{2}.

**Analysis**
To be sure that the parametric equations are equivalent to the Cartesian equation, check the domains. The parametric equations restrict the domain on x = \sqrt{—} t  + 2 to t > 0; we restrict the domain on x to x > 2. The domain for the parametric equation y = log(t) is restricted to t > 0; we limit the domain on y = log(x - 2)^{2} to x > 2.

**Try It #4**
Eliminate the parameter and write as a rectangular equation.

x(t) = t^{2}

y(t) = ln(t) t > 0 Eliminating the Parameter from Trigonometric Equations Eliminating the parameter from trigonometric equations is a straightforward substitution. We can use a few of the familiar trigonometric identities and the Pythagorean Theorem.

First, we use the identities:

x(t) = acos t

y(t) = bsin t Solving for cos t and sin t, we have

 x _ a  = cos t

 y _ a  = sin t Then, use the Pythagorean Theorem:

cos^{2} t + sin^{2} t = 1 Substituting gives

cos^{2} t + sin^{2} t =   x _ a    2 +   y _ b     = 1

**Example  7**
Eliminating the Parameter from a Pair of Trigonometric Parametric Equations Eliminate the parameter from the given pair of trigonometric equations where 0 \le  t \le  2\pi  and sketch the graph.

x(t) = 4cos t

y(t) = 3sin t Solution Solving for cos t and sin t, we have

x = 4cos t

 x _ 4  = cos t

y = 3sin t

 y _ 3  = sin t Next, use the Pythagorean identity and make the substitutions.

cos^{2} t + sin^{2} t = 1

  x _ 4    2 +   y _ 3     = 1

 x^{2}

_ 16  +  y^{2}

_ 9  = 1 The graph for the equation is shown in Figure 8. x y t = 0 \pi  t =

**Analysis**
Applying the general equations for conic sections (introduced in Analytic Geometry, we can identify  x^{2}

_ 16  +  y^{2}

_ 9  = 1 as an ellipse centered at (0, 0). Notice that when t = 0 the coordinates are (4, 0), and when t =  \pi  _ 2  the coordinates are (0, 3). This shows the orientation of the curve with increasing values of t.


**Try It #5**
Eliminate the parameter from the given pair of parametric equations and write as a Cartesian equation: x(t) = 2cos t and y(t) = 3sin t. Finding Cartesian Equations from Curves Defined Parametrically When we are given a set of parametric equations and need to find an equivalent Cartesian equation, we are essentially “eliminating the parameter.” However, there are various methods we can use to rewrite a set of parametric equations as a Cartesian equation. The simplest method is to set one equation equal to the parameter, such as x(t) = t. In this case, y(t) can be any expression. For example, consider the following pair of equations.

x(t) = t

y(t) = t 2 - 3 Rewriting this set of parametric equations is a matter of substituting x for t. Thus, the Cartesian equation is y = x^{2} - 3.

**Example  8**
Finding a Cartesian Equation Using Alternate Methods Use two different methods to find the Cartesian equation equivalent to the given set of parametric equations.

x(t) = 3t - 2

y(t) = t + 1

**Solution**
Method 1. First, let’s solve the x equation for t. Then we can substitute the result into the y equation.

x = 3t - 2

x + 2 = 3t

 x + 2 _  = t Now substitute the expression for t into the y equation.

y = t + 1

y =  x + 2 _   + 1

y =  x _ 3  +  2 _ 3  + 1

y =  1 _ 3 x +  5 _ 3  Method 2. Solve the y equation for t and substitute this expression in the x equation.

y = t + 1

y - 1 = t Make the substitution and then solve for y.

x = 3(y - 1) - 2

x = 3y - 3 - 2

x = 3y - 5

x + 5 = 3y

 x + 5 _  = y

y =  1 _ 3 x +  5 _ 3 


**Try It #6**
Write the given parametric equations as a Cartesian equation: x(t) = t^{3} and y(t) = t 6. Finding Parametric Equations for Curves Defined by Rectangular Equations Although we have just shown that there is only one way to interpret a set of parametric equations as a rectangular equation, there are multiple ways to interpret a rectangular equation as a set of parametric equations. Any strategy we may use to find the parametric equations is valid if it produces equivalency. In other words, if we choose an expression to represent x, and then substitute it into the y equation, and it produces the same graph over the same domain as the rectangular equation, then the set of parametric equations is valid. If the domain becomes restricted in the set of parametric equations, and the function does not allow the same values for x as the domain of the rectangular equation, then the graphs will be different.

**Example  9**
Finding a Set of Parametric Equations for Curves Defined by Rectangular Equations Find a set of equivalent parametric equations for y = (x + 3)^{2} + 1. Solution An obvious choice would be to let x(t) = t. Then y(t) = (t + 3)^{2} + 1. But let’s try something more interesting. What if we let x = t + 3? Then we have

y = (x + 3)^{2} + 1

y = ((t + 3) + 3)^{2} + 1

y = (t + 6)^{2} + 1 The set of parametric equations is

x(t) = t + 3

y(t) = (t + 6)^{2} + 1 See Figure 9. x y (a) Parametric x = t + 3 y = (t + 6)^{2} + 1 x y (b) Rectangular y = (x + 3)^{2} + 1 Access these online resources for additional instruction and practice with parametric equations. • Introduction to Parametric Equations (http://openstaxcollege.org/l/introparametric) • Converting Parametric Equations to Rectangular Form (http://openstaxcollege.org/l/convertpara)


## 8.6 Section Exercises

### 8.6 Section Exercises
Verbal 1. What is a system of parametric equations? 2. Some examples of a third parameter are time, length, speed, and scale. Explain when time is used as a parameter. 3. Explain how to eliminate a parameter given a set of parametric equations. 4. What is a benefit of writing a system of parametric equations as a Cartesian equation? 5. What is a benefit of using parametric equations? 6. Why are there many sets of parametric equations to represent on Cartesian function? Algebraic For the following exercises, eliminate the parameter t to rewrite the parametric equation as a Cartesian equation. 7. x(t) = 5 - t y(t) = 8 - 2t { 8. x(t) = 6 - 3t y(t) = 10 - t { 9. x(t) = 2t + 1 y(t) = 3\sqrt{t}  { 10. x(t) = 3t - 1 y(t) = 2t 2 { 11. x(t) = 2e t y(t) = 1 - 5t { 12. x(t) = e –2t y(t) = 2e -t { 13. x(t) = 4 log (t) y(t) = 3 + 2t { 14. x(t) = log (2t) y(t) = \sqrt{t} - 1  { 15. x(t) = t 3 - t y(t) = 2t { 16. x(t) = t - t 4 y(t) = t + 2 { 17. x(t) = e 2t y(t) = e 6t { 18. x(t) = t 5 y(t) = t^{1}0 { 19. x(t) = 4 cos t y(t) = 5 sin t { 20. x(t) = 3 sin t y(t) = 6 cos t { 21. x(t) = 2 cos^{2} t y(t) = -sin t { 22. x(t) = cos t + 4 y(t) = 2 sin^{2} t { 23. x(t) = t - 1 y(t) = t 2 { 24. x(t) = -t y(t) = t 3 + 1 { 25. x(t) = 2t - 1 y(t) = t^{3} - 2 { For the following exercises, rewrite the parametric equation as a Cartesian equation by building an x-y table. 26. x(t) = 2t - 1 y(t) = t + 4 { 27. x(t) = 4 - t y(t) = 3t + 2 { 28. x(t) = 2t - 1 y(t) = 5t { 29. x(t) = 4t - 1 y(t) = 4t + 2 { For the following exercises, parameterize (write parametric equations for) each Cartesian equation by setting x(t) = t or by setting y(t) = t. 30. y(x) = 3x^{2} + 3 31. y(x) = 2 sin x + 1 32. x(y) = 3 log (y) + y 33. x(y) = \sqrt{y}  + 2y For the following exercises, parameterize (write parametric equations for) each Cartesian equation by using x(t) = a cos t and y(t) = b sin t. Identify the curve.

_ 4  +  y 2

_ 9  = 1

_ 16  +  y 2

_ 38. Parameterize the line from (3, 0) to (-2, -5) so that the line is at (3, 0) at t = 0, and at (-2, -5) at t = 1. 39. Parameterize the line from (-1, 0) to (3, -2) so that the line is at (-1, 0) at t = 0, and at (3, -2) at t = 1. 40. Parameterize the line from (-1, 5) to (2, 3) so that the line is at (-1, 5) at t = 0, and at (2, 3) at t = 1. 41. Parameterize the line from (4, 1) to (6, -2) so that the line is at (4, 1) at t = 0, and at (6, -2) at t = 1.

Technology For the following exercises, use the table feature in the graphing calculator to determine whether the graphs intersect. 42. x^{1}(t) = 3t y^{1}(t) = 2t - 1 { and x^{2}(t) = t + 3 y^{2}(t) = 4t - 4 { 43. x^{1}(t) = t 2 y^{1}(t) = 2t - 1 { and x^{2}(t) = -t + 6 y^{2}(t) = t + 1 { For the following exercises, use a graphing calculator to complete the table of values for each set of parametric equations. 44. x^{1}(t) = 3t 2 - 3t + 7 y^{1}(t) = 2t + 3 {

t x y -1 45. x^{1}(t) = t 2 - 4 y^{1}(t) = 2t 2 - 1 {

t x y 46. x^{1}(t) = t 4 y^{1}(t) = t 3 + 4 {

t x y -1 Extensions 47. Find two different sets of parametric equations for y = (x + 1)^{2}. 48. Find two different sets of parametric equations for y = 3x - 2. 49. Find two different sets of parametric equations for y = x 2 - 4x + 4.


## 8.7 Parametric Equations: Graphs
It is the bottom of the ninth inning, with two outs and two men on base. The home team is losing by two runs. The batter swings and hits the baseball at 140 feet per second and at an angle of approximately 45° to the horizontal. How far will the ball travel? Will it clear the fence for a game-winning home run? The outcome may depend partly on other factors (for example, the wind), but mathematicians can model the path of a projectile and predict approximately how far it will travel using parametric equations. In this section, we’ll discuss parametric equations and some common applications, such as projectile motion problems. Graphing Parametric Equations by Plotting Points In lieu of a graphing calculator or a computer graphing program, plotting points to represent the graph of an equation is the standard method. As long as we are careful in calculating the values, point-plotting is highly dependable.

**How To…**
Given a pair of parametric equations, sketch a graph by plotting points. 1. Construct a table with three columns: t, x(t), and y(t). 2. Evaluate x and y for values of t over the interval for which the functions are defined. 3. Plot the resulting pairs (x, y).

**Example  1**

### Sketching the Graph of a Pair of Parametric Equations by Plotting Points
Sketch the graph of the parametric equations x(t) = t 2 + 1, y(t) = 2 + t. Solution Construct a table of values for t, x(t), and y(t), as in Table 1, and plot the points in a plane. Learning Objectives
In this section, you will:
• Graph plane curves described by parametric equations by plotting points.
• Graph parametric equations.
t x(t) = t 2 + 1 y(t) = 2 + t -5 -3 -4 -2 -3 -1 -2 -1 The graph is a parabola with vertex at the point (1, 2), opening to the right. See Figure 2. x y

**Analysis**
As values for t progress in a positive direction from 0 to 5, the plotted points trace out the top half of the parabola. As values of t become negative, they trace out the lower half of the parabola. There are no restrictions on the domain. The arrows indicate direction according to increasing values of t. The graph does not represent a function, as it will fail the vertical line test. The graph is drawn in two parts: the positive values for t, and the negative values for t.

**Try It #1**
Sketch the graph of the parametric equations x = \sqrt{—} t , y = 2t + 3, 0 \le  t \le  3.

**Example  2**

### Sketching the Graph of Trigonometric Parametric Equations
Construct a table of values for the given parametric equations and sketch the graph:

x = 2cos t

y = 4sin t Solution Construct a table like that in Table 2 using angle measure in radians as inputs for t, and evaluating x and y. Using angles with known sine and cosine values for t makes calculations easier.

t x = 2cos t y = 4sin t x = 2cos(0) = 2 y = 4sin(0) = 0  \pi  __ 6  x = 2cos   \pi  __ 6    = \sqrt{3}  y = 4sin   \pi  __ 6    = 2  \pi  __ 3  x = 2cos   \pi  __ 3    = 1 y = 4sin   \pi  __ 3    = 2\sqrt{__}

3   \pi  __ 2  x = 2cos   \pi  __ 2    = 0 y = 4sin   \pi  __ 2    = 4  2\pi  ___ 3  x = 2cos   2\pi  ___ 3    = -1 y = 4sin   2\pi  ___ 3    = -2\sqrt{3}   5\pi  ___ 6  x = 2cos   5\pi  ___ 6    = -\sqrt{3}  y = 4sin   5\pi  ___ 6    = 2 \pi  x = 2cos(\pi ) = -2 y = 4sin(\pi ) = 0  7\pi  ___ 6  x = 2cos   7\pi  ___ 6    = -\sqrt{3}  y = 4sin   7\pi  ___ 6    = -2  4\pi  ___ 3  x = 2cos   4\pi  ___ 3    = -1 y = 4sin   4\pi  ___ 3    = -2\sqrt{3}   3\pi  ___ 2  x = 2cos   3\pi  ___ 2    = 0 y = 4sin   3\pi  ___ 2    = -4  5\pi  ___ 3  x = 2cos   5\pi  ___ 3    = 1 y = 4sin   5\pi  ___ 3    = -2\sqrt{3}   11\pi  ____ 6  x = 2cos   11\pi  ____ 6    = \sqrt{3}  y = 4sin   11\pi  ____ 6    = -2 2\pi  x = 2cos(2\pi ) = 2 y = 4sin(2\pi ) = 0 x y 5 (0, 4) t = (2, 0) t = 0 ( 3, –2) t = \pi  11\pi  (– 3, 2) t = 5\pi  By the symmetry shown in the values of x and y, we see that the parametric equations represent an ellipse. The ellipse is mapped in a counterclockwise direction as shown by the arrows indicating increasing t values.

**Analysis**
We have seen that parametric equations can be graphed by plotting points. However, a graphing calculator will save some time and reveal nuances in a graph that may be too tedious to discover using only hand calculations.

Make sure to change the mode on the calculator to parametric (PAR). To confirm, the Y= window should show

X^{1}T =

Y^{1}T = instead of Y^{1}= .

**Try It #2**
Graph the parametric equations: x = 5cos t, y = 3sin t.

**Example  3**

### Graphing Parametric Equations and Rectangular Form Together
Graph the parametric equations x = 5cos t and y = 2sin t. First, construct the graph using data points generated from the parametric form. Then graph the rectangular form of the equation. Compare the two graphs. Solution Construct a table of values like that in Table 3. t x = 5cos t y = 2sin t x = 5cos(0) = 5 y = 2sin(0) = 0 x = 5cos(1) ≈ 2.7 y = 2sin(1) ≈ 1.7 x = 5cos(2) ≈ -2.1 y = 2sin(2) ≈ 1.8 x = 5cos(3) ≈ -4.95 y = 2sin(3) ≈ 0.28 x = 5cos(4) ≈ -3.3 y = 2sin(4) ≈ -1.5 x = 5cos(5) ≈ 1.4 y = 2sin(5) ≈ -1.9 -1 x = 5cos(-1) ≈ 2.7 y = 2sin(-1) ≈ -1.7 -2 x = 5cos(-2) ≈ -2.1 y = 2sin(-2) ≈ -1.8 -3 x = 5cos(-3) ≈ -4.95 y = 2sin(-3) ≈ -0.28 -4 x = 5cos(-4) ≈ -3.3 y = 2sin(-4) ≈ 1.5 -5 x = 5cos(-5) ≈ 1.4 y = 2sin(-5) ≈ 1.9 Plot the (x, y) values from the table. See Figure 4. x y x y Rectangular Parametric Next, translate the parametric equations to rectangular form. To do this, we solve for t in either x(t) or y(t), and then substitute the expression for t in the other equation. The result will be a function y(x) if solving for t as a function of x, or x(y) if solving for t as a function of y.

x = 5cos t

 x _ 5  = cos t Solve for cos t.

y = 2sin t Solve for sin t.

 y _ 2  = sin t

Then, use the Pythagorean Theorem.

cos^{2} t + sin^{2} t = 1

  x _ 5    2 +   y _ 2     = 1

 x 2

_ 25  +  y 2

_ 4  = 1

**Analysis**
In Figure 5, the data from the parametric equations and the rectangular equation are plotted together. The parametric equations are plotted in blue; the graph for the rectangular equation is drawn on top of the parametric in a dashed style colored red. Clearly, both forms produce the same graph. x y

**Example  4**
Graphing Parametric Equations and Rectangular Equations on the Coordinate System Graph the parametric equations x = t + 1 and y = \sqrt{—} t , t \ge  0, and the rectangular equivalent y = \sqrt{x} - 1  on the same coordinate system. Solution Construct a table of values for the parametric equations, as we did in the previous example, and graph y = \sqrt{—} t , t \ge  0 on the same grid, as in Figure 6. x y

**Analysis**
With the domain on t restricted, we only plot positive values of t. The parametric data is graphed in blue and the graph of the rectangular equation is dashed in red. Once again, we see that the two forms overlap.

**Try It #3**
Sketch the graph of the parametric equations x = 2cos \theta  and y = 4sin \theta , along with the rectangular equation on the same grid.

Applications of Parametric Equations Many of the advantages of parametric equations become obvious when applied to solving real-world problems. Although rectangular equations in x and y give an overall picture of an object's path, they do not reveal the position of an object at a specific time. Parametric equations, however, illustrate how the values of x and y change depending on t, as the location of a moving object at a particular time. A common application of parametric equations is solving problems involving projectile motion. In this type of motion, an object is propelled forward in an upward direction forming an angle of \theta  to the horizontal, with an initial speed of v^{0}, and at a height h above the horizontal. The path of an object propelled at an inclination of \theta  to the horizontal, with initial speed v^{0}, and at a height h above the horizontal, is given by

x = (v^{0}cos \theta  )t

y = -  1 __ 2  gt 2 + (v^{0}sin \theta  )t + h where g accounts for the effects of gravity and h is the initial height of the object. Depending on the units involved in the problem, use g = 32 ft/s^{2} or g = 9.8 m/s^{2}. The equation for x gives horizontal distance, and the equation for y gives the vertical distance.

**How To…**
Given a projectile motion problem, use parametric equations to solve. 1. The horizontal distance is given by x = (v^{0} cos \theta )t. Substitute the initial speed of the object for v^{0}. 2. The expression cos \theta  indicates the angle at which the object is propelled. Substitute that angle in degrees for cos \theta . 3. The vertical distance is given by the formula y = -  1 __ 2 gt^{2} + (v^{0} sin \theta )t + h. The term -  1 __ 2 gt^{2} represents the effect of gravity. Depending on units involved, use g = 32 ft/s^{2} or g = 9.8 m/s^{2}. Again, substitute the initial speed for v^{0}, and the height at which the object was propelled for h. 4. Proceed by calculating each term to solve for t.

**Example  5**
Finding the Parametric Equations to Describe the Motion of a Baseball Solve the problem presented at the beginning of this section. Does the batter hit the game-winning home run? Assume that the ball is hit with an initial velocity of 140 feet per second at an angle of 45° to the horizontal, making contact 3 feet above the ground. a. Find the parametric equations to model the path of the baseball. b. Where is the ball after 2 seconds? c. How long is the ball in the air? d. Is it a home run?

**Solution**
a. Use the formulas to set up the equations. The horizontal position is found using the parametric equation for x. Thus,

x = (v^{0} cos \theta )t

x = (140cos(45°))t The vertical position is found using the parametric equation for y. Thus,

y = - 16t^{2} + (v^{0} sin \theta )t + h

y = - 16t^{2} + (140sin(45°))t + 3 b. Substitute 2 into the equations to find the horizontal and vertical positions of the ball.

x = (140cos(45°))(2)

x = 198 feet

y = -16(2)^{2} + (140sin(45°))(2) + 3

y = 137 feet After 2 seconds, the ball is 198 feet away from the batter’s box and 137 feet above the ground.

c. To calculate how long the ball is in the air, we have to find out when it will hit ground, or when y = 0. Thus,

y = -16t 2 +(140sin(45°))t + 3

y = 0

Set y (t) = 0 and solve the quadratic.

When t = 6.2173 seconds, the ball has hit the ground. (The quadratic equation can be solved in various ways, but this problem was solved using a computer math program.) d. We cannot confirm that the hit was a home run without considering the size of the outfield, which varies from field to field. However, for simplicity’s sake, let’s assume that the outfield wall is 400 feet from home plate in the deepest part of the park. Let’s also assume that the wall is 10 feet high. In order to determine whether the ball clears the wall, we need to calculate how high the ball is when x = 400 feet. So we will set x = 400, solve for t, and input t into y.

x = (140cos(45°))t

The ball is 141.8 feet in the air when it soars out of the ballpark. It was indeed a home run. See Figure 7. Trajectory of ball Position of hitter Outfield wall Height (ft) Distance (ft) Access the following online resource for additional instruction and practice with graphs of parametric equations. • Graphing Parametric Equations on the TI-84 (http://openstaxcollege.org/l/graphpara^{8}4)


### 8.7 Section Exercises
Verbal 1. What are two methods used to graph parametric equations? 2. What is one difference in point-plotting parametric equations compared to Cartesian equations? 3. Why are some graphs drawn with arrows? 4. Name a few common types of graphs of parametric equations. 5. Why are parametric graphs important in understanding projectile motion? Graphical For the following exercises, graph each set of parametric equations by making a table of values. Include the orientation on the graph. 6. x(t) = t y(t) = t 2 - 1 {

7. x(t) = t - 1 y(t) = t 2 { t -3 -2 -1 x y 8. x(t) = 2 + t y(t) = 3 - 2t { t - 2 - 1 x y 9. x(t) = -2 - 2t y(t) = 3 + t { t - 3 - 2 - 1 x y 10. x(t) = t^{3} y(t) = t + 2 { t - 2 - 1 x y 11. x(t) = t^{2} y(t) = t + 3 { t - 2 - 1 x y For the following exercises, sketch the curve and include the orientation. 12. x(t) = t y(t) = \sqrt{t}  { 13. x(t) = -\sqrt{t}  y(t) = t { 14. x(t) = 5 - | t | y(t) = t + 2 { 15. x(t) = -t + 2 y(t) = 5 - | t | { 16. x(t) = 4sin t y(t) = 2cos t { 17. x(t) = 2sin t y(t) = 4cos t { 18. x(t) = 3cos^{2} t y(t) = -3sin t { 19. x(t) = 3cos^{2} t y(t) = -3sin^{2} t { 20. x(t) = sec t y(t) = tan t { 21. x(t) = sec t y(t) = tan^{2} t { 22. x(t) =  1 ___ e^{2}t  y(t) = e-t { For the following exercises, graph the equation and include the orientation. Then, write the Cartesian equation. 23. x(t) = t - 1 y(t) = -t^{2} { 24. x(t) = t^{3} y(t) = t + 3 { 25. x(t) = 2cos t y(t) = - sin t { t x y -3 -2 -1


## 8.7 Section Exercises
26. x(t) = 7cos t y(t) = 7sin t { 27. x(t) = e 2t y(t) = -e t { For the following exercises, graph the equation and include the orientation. 28. x = t^{2}, y = 3t, 0 \le  t \le  5 29. x = 2t, y = t^{2}, -5 \le  t \le  5 30. x = t, y = \sqrt{25} - t^{2} , 0 < t \le  5 31. x(t) = -t, y(t) = \sqrt{_} t , t \ge  5 32. x(t) = -2cos t, y = 6sin t 0 \le  t \le  \pi  33. x(t) = -sec t, y = tan t, - \pi  __ 2  < t <  \pi  __ 2  For the following exercises, use the parametric equations for integers a and b: x(t) = acos((a + b)t) y(t) = acos((a - b)t) 34. Graph on the domain [-\pi , 0], where a = 2 and b = 1, and include the orientation. 35. Graph on the domain [-\pi , 0], where a = 3 and b = 2, and include the orientation. 36. Graph on the domain [-\pi , 0], where a = 4 and b = 3, and include the orientation. 37. Graph on the domain [-\pi , 0], where a = 5 and b = 4, and include the orientation. 38. If a is 1 more than b, describe the effect the values of a and b have on the graph of the parametric equations. 39. Describe the graph if a = 100 and b = 99. 40. What happens if b is 1 more than a? Describe the graph. 41. If the parametric equations x(t) = t 2 and y(t) = 6 - 3t have the graph of a horizontal parabola opening to the right, what would change the direction of the curve? For the following exercises, describe the graph of the set of parametric equations. 42. x(t) = - t^{2} and y(t) is linear 43. y(t) = t^{2} and x(t) is linear 44. y(t) = - t^{2} and x(t) is linear 45. Write the parametric equations of a circle with center (0, 0), radius 5, and a counterclockwise orientation. 46. Write the parametric equations of an ellipse with center (0, 0), major axis of length 10, minor axis of length 6, and a counterclockwise orientation. For the following exercises, use a graphing utility to graph on the window [-3, 3] by [-3, 3] on the domain [0, 2\pi ) for the following values of a and b , and include the orientation. x(t) = sin(at) y(t) = sin(bt) { Technology For the following exercises, look at the graphs that were created by parametric equations of the form x(t) = acos(bt) y(t) = csin(dt) { Use the parametric mode on the graphing calculator to find the values of a, b, c, and d to achieve each graph. x y x y x y x y

For the following exercises, use a graphing utility to graph the given parametric equations. a. x(t) = cos t - 1 y(t) = sin t + t { b. x(t) = cos t + t y(t) = sin t - 1 { c. x(t) = t - sin t y(t) = cos t - 1 { 57. Graph all three sets of parametric equations on the domain [0, 2\pi ]. 58. Graph all three sets of parametric equations on the domain [0, 4\pi ]. 59. Graph all three sets of parametric equations on the domain [-4\pi , 6\pi ]. 60. The graph of each set of parametric equations appears to “creep” along one of the axes. What controls which axis the graph creeps along? 61. Explain the effect on the graph of the parametric ­equation when we switched sin t and cos t. 62. Explain the effect on the graph of the parametric equation when we changed the domain. Extensions 63. An object is thrown in the air with vertical velocity of 20 ft/s and horizontal velocity of 15 ft/s. The object’s height can be described by the equation y(t) = - 16t^{2} + 20t, while the object moves horizontally with constant velocity 15 ft/s. Write parametric equations for the object’s position, and then eliminate time to write height as a function of horizontal position. 64. A skateboarder riding on a level surface at a constant speed of 9 ft/s throws a ball in the air, the height of which can be described by the equation y(t) = - 16t^{2} + 10t + 5.Write parametric equations for the ball’s position, and then eliminate time to write height as a function of horizontal position. For the following exercises, use this scenario: A dart is thrown upward with an initial velocity of 65 ft/s at an angle of elevation of 52°. Consider the position of the dart at any time t. Neglect air resistance. 65. Find parametric equations that model the problem situation. 66. Find all possible values of x that represent the situation. 67. When will the dart hit the ground? 68. Find the maximum height of the dart. 69. At what time will the dart reach maximum height? For the following exercises, look at the graphs of each of the four parametric equations. Although they look unusual and beautiful, they are so common that they have names, as indicated in each exercise. Use a graphing utility to graph each on the indicated domain. 70. An epicycloid: x(t) = 14cos t - cos(14t) y(t) = 14sin t + sin(14t) {

on the domain [0, 2\pi ]. 71. An hypocycloid: x(t) = 6sin t + 2sin(6t) y(t) = 6cos t - 2cos(6t) {

on the domain [0, 2\pi ]. 72. An hypotrochoid: x(t) = 2sin t + 5cos(6t) y(t) = 5cos t - 2sin(6t) {

on the domain [0, 2\pi ]. 73. A rose: x(t) = 5sin(2t) sin t y(t) = 5sin(2t) cos t {

on the domain [0, 2\pi ].


## 8.8 Vectors
Learning Objectives
In this section, you will:
• View vectors geometrically.
• Find magnitude and direction.
• Perform vector addition and scalar multiplication.
• Find the component form of a vector.
• Find the unit vector in the direction of v.
• Perform operations with vectors in terms of i and j.
• Find the dot product of two vectors.
An airplane is flying at an airspeed of 200 miles per hour headed on a SE bearing of 140°. A north wind (from north to south) is blowing at 16.2 miles per hour, as shown in Figure 1. What are the ground speed and actual bearing of the plane? N A O B X C 140 ̊ 16.2 \alpha  Ground speed refers to the speed of a plane relative to the ground. Airspeed refers to the speed a plane can travel relative to its surrounding air mass. These two quantities are not the same because of the effect of wind. In an earlier section, we used triangles to solve a similar problem involving the movement of boats. Later in this section, we will find the airplane’s groundspeed and bearing, while investigating another approach to problems of this type. First, however, let’s examine the basics of vectors. A Geometric View of Vectors A vector is a specific quantity drawn as a line segment with an arrowhead at one end. It has an initial point, where it begins, and a terminal point, where it ends. A vector is defined by its magnitude, or the length of the line, and its direction, indicated by an arrowhead at the terminal point. Thus, a vector is a directed line segment. There are various symbols that distinguish vectors from other quantities: • Lower case, boldfaced type, with or without an arrow on top such as v, u, w, v, u, w. • Given initial point P and terminal point Q, a vector can be represented as PQ. The arrowhead on top is what indicates that it is not just a line, but a directed line segment. • Given an initial point of (0, 0) and terminal point (a, b), a vector may be represented as 〈a, b〉. This last symbol 〈a, b〉 has special significance. It is called the standard position. The position vector has an initial point (0, 0) and a terminal point 〈a, b〉. To change any vector into the position vector, we think about the change in the x-coordinates and the change in the y-coordinates. Thus, if the initial point of a vector CD is C(x^{1}, y^{1}) and the terminal point is D(x^{2}, y^{2}), then the position vector is found by calculating AB = 〈x^{2} - x^{1}, y^{2} - y^{1}〉

= 〈a, b〉 →→→ → → →

In Figure 2, we see the original vector CD and the position vector AB. x D A C y B (a, b) properties of vectors A vector is a directed line segment with an initial point and a terminal point. Vectors are identified by magnitude, or the length of the line, and direction, represented by the arrowhead pointing toward the terminal point. The position vector has an initial point at (0, 0) and is identified by its terminal point 〈a, b〉.

**Example  1**
Find the Position Vector Consider the vector whose initial point is P(2, 3) and terminal point is Q(6, 4). Find the position vector. Solution The position vector is found by subtracting one x-coordinate from the other x-coordinate, and one y-coordinate from the other y-coordinate. Thus

v = 〈6 -2, 4 -3〉

The position vector begins at (0, 0) and terminates at (4, 1). The graphs of both vectors are shown in Figure 3. x y We see that the position vector is 〈4, 1〉.

**Example  2**

### Drawing a Vector with the Given Criteria and Its Equivalent Position Vector
Find the position vector given that vector v has an initial point at (-3, 2) and a terminal point at (4, 5), then graph both vectors in the same plane. Solution The position vector is found using the following calculation:

v = 〈4 - ( - 3), 5 - 2〉

Thus, the position vector begins at (0, 0) and terminates at (7, 3). See Figure 4. → →

x y Position vector

**Try It #1**
Draw a vector v that connects from the origin to the point (3, 5). Finding Magnitude and Direction To work with a vector, we need to be able to find its magnitude and its direction. We find its magnitude using the Pythagorean Theorem or the distance formula, and we find its direction using the inverse tangent function. magnitude and direction of a vector Given a position vector v = 〈a, b〉, the magnitude is found by | v | = \sqrt{a^{2}} + b^{2} . The direction is equal to the angle formed with the x-axis, or with the y-axis, depending on the application. For a position vector, the direction is found by tan \theta  =   b __ a    ⇒ \theta  = tan-1  b __ a   , as illustrated in Figure 5. x y |v| \theta  〈a, b〉 Two vectors v and u are considered equal if they have the same magnitude and the same direction. Additionally, if both vectors have the same position vector, they are equal.

**Example  3**
Finding the Magnitude and Direction of a Vector Find the magnitude and direction of the vector with initial point P(-8, 1) and terminal point Q(-2, -5). Draw the vector. Solution First, find the position vector.

u = 〈-2, - (-8), -5-1〉

= 〈6, - 6〉 We use the Pythagorean Theorem to find the magnitude.

| u | =\sqrt{(6})^{2} + (-6)^{2} 

= \sqrt{72} 

= 6\sqrt{2} 

The direction is given as

tan \theta  =  -6 ___ 6  = -1 ⇒ \theta  = tan -1(-1)

= -45° However, the angle terminates in the fourth quadrant, so we add 360° to obtain a positive angle. Thus, -45° + 360° = 315°. See Figure 6. 315° x y

**Example  4**
Showing That Two Vectors Are Equal Show that vector v with initial point at (5, -3) and terminal point at (-1, 2) is equal to vector u with initial point at (-1, -3) and terminal point at (-7, 2). Draw the position vector on the same grid as v and u. Next, find the magnitude and direction of each vector. Solution As shown in Figure 7, draw the vector v starting at initial (5, -3) and terminal point (-1, 2). Draw the vector u with initial point (-1, -3) and terminal point (-7, 2). Find the standard position for each. Next, find and sketch the position vector for v and u. We have

v = 〈-1 - 5, 2 - ( - 3)〉

= 〈-6, 5〉

u = 〈-7 - (-1), 2 - (-3)〉

= 〈-6, 5〉 Since the position vectors are the same, v and u are the same. An alternative way to check for vector equality is to show that the magnitude and direction are the same for both vectors. To show that the magnitudes are equal, use the Pythagorean Theorem.

| v | = \sqrt{—}

(-1 - 5)^{2} + (2 - (-3))^{2} 

= \sqrt{(-6})^{2} + (5)^{2} 

= \sqrt{—}

= \sqrt{61} 

| u | = \sqrt{—}

(-7 - (-1))^{2} + (2 - (-3))^{2} 

= \sqrt{(-6})^{2} + (5)^{2} 

= \sqrt{—}

= \sqrt{61}  As the magnitudes are equal, we now need to verify the direction. Using the tangent function with the position vector gives

tan \theta  = - 5 _ 6  ⇒ \theta  = tan-1 - 5 _ 6  

However, we can see that the position vector terminates in the second quadrant, so we add 180°. Thus, the direction

x v u Position vector y Performing Vector Addition and Scalar Multiplication Now that we understand the properties of vectors, we can perform operations involving them. While it is convenient to think of the vector u = 〈x, y〉 as an arrow or directed line segment from the origin to the point (x, y), vectors can be situated anywhere in the plane. The sum of two vectors u and v, or vector addition, produces a third vector u+ v, the resultant vector. To find u + v, we first draw the vector u, and from the terminal end of u, we drawn the vector v. In other words, we have the initial point of v meet the terminal end of u. This position corresponds to the notion that we move along the first vector and then, from its terminal point, we move along the second vector. The sum u + v is the resultant vector because it results from addition or subtraction of two vectors. The resultant vector travels directly from the beginning of u to the end of v in a straight path, as shown in Figure 8. -v v u u u - v u + v Vector subtraction is similar to vector addition. To find u - v, view it as u + (-v). Adding -v is reversing direction of v and adding it to the end of u. The new vector begins at the start of u and stops at the end point of -v. See Figure 9 for a visual that compares vector addition and vector subtraction using parallelograms. u v u + v –v u u u – v

**Example  5**

### Adding and Subtracting Vectors
Given u = 〈3, - 2〉 and v = 〈-1, 4〉, find two new vectors u + v, and u - v. Solution To find the sum of two vectors, we add the components. Thus,

u + v = 〈3, - 2〉 + 〈-1, 4〉

= 〈3 + ( - 1), - 2 + 4〉

See Figure 10(a). To find the difference of two vectors, add the negative components of v to u. Thus,

u + (-v) = 〈3, - 2〉 + 〈1, -4〉

= 〈3 + 1, - 2 + (-4)〉

= 〈4, - 6〉

See Figure 10(b). x u v u + v y (a) - v (b) x u u - v y Multiplying By a Scalar While adding and subtracting vectors gives us a new vector with a different magnitude and direction, the process of multiplying a vector by a scalar, a constant, changes only the magnitude of the vector or the length of the line. Scalar multiplication has no effect on the direction unless the scalar is negative, in which case the direction of the resulting vector is opposite the direction of the original vector. scalar multiplication Scalar multiplication involves the product of a vector and a scalar. Each component of the vector is multiplied by the scalar. Thus, to multiply v = 〈a, b〉 by k, we have

kv = 〈ka, kb〉 Only the magnitude changes, unless k is negative, and then the vector reverses direction.

**Example  6**

### Performing Scalar Multiplication
Given vector v = 〈3, 1〉 , find 3v,  1 _ 2 v, and -v. Solution See Figure 11 for a geometric interpretation. If v = 〈3, 1〉, then

3v = 〈3 ⋅ 3, 3 ⋅ 1〉

 1 _ 2 v = 〈 1 _ 2  ⋅ 3,  1 _ 2  ⋅ 1〉

= 〈 3 _ _ 2 〉

-v = 〈-3, -1〉 3v v –v v

**Analysis**
Notice that the vector 3v is three times the length of v,  1 _ 2 v is half the length of v, and -v is the same length of v, but in the opposite direction.


**Try It #2**
Find the scalar multiple 3u given u = 〈5, 4〉 .

**Example  7**
Using Vector Addition and Scalar Multiplication to Find a New Vector Given u = 〈3, - 2〉 and v = 〈-1, 4〉, find a new vector w = 3u + 2v. Solution First, we must multiply each vector by the scalar.

3u = 3 〈3, - 2〉

= 〈9, - 6〉

= 〈-2, 8〉 Then, add the two together.

w = 3u + 2v

= 〈9, - 6〉 + 〈-2, 8〉

= 〈9 - 2, - 6 + 8〉

So, w = 〈7, 2〉. Finding Component Form In some applications involving vectors, it is helpful for us to be able to break a vector down into its components. Vectors are comprised of two components: the horizontal component is the x direction, and the vertical component is the y direction. For example, we can see in the graph in Figure 12 that the position vector 〈2, 3〉 comes from adding the vectors v^{1} and v^{2}. We have v^{1} with initial point (0, 0) and terminal point (2, 0).

v^{1} = 〈2 - 0, 0 - 0〉

We also have v^{2} with initial point (0, 0) and terminal point (0, 3).

v^{2} = 〈0 - 0, 3 - 0〉

Therefore, the position vector is

v = 〈2 + 0, 3 + 0〉

Using the Pythagorean Theorem, the magnitude of v^{1} is 2, and the magnitude of v^{2} is 3. To find the magnitude of v, use the formula with the position vector.

| v | = \sqrt{__________} ∣ v^{1} ∣2 + ∣ v^{2} ∣2

= \sqrt{—}

= \sqrt{13}  The magnitude of v is \sqrt{13} . To find the direction, we use the tangent function tan \theta  =  y _ x .

tan \theta  =  v^{2} _ v^{1} 

tan \theta  =  3 _ 2 

\theta  = tan-1   3 _

x y 56.3° v^{1} v^{2} |v| Thus, the magnitude of v is \sqrt{13}  and the direction is 56.3° off the horizontal.

**Example  8**
Finding the Components of the Vector Find the components of the vector v with initial point (3, 2) and terminal point (7, 4). Solution First find the standard position.

v = 〈7 - 3, 4 - 2〉

See the illustration in Figure 13. x y The horizontal component is v^{1} = 〈4, 0〉 and the vertical component is v^{2} = 〈0, 2〉. Finding the Unit Vector in the Direction of v In addition to finding a vector’s components, it is also useful in solving problems to find a vector in the same direction as the given vector, but of magnitude 1. We call a vector with a magnitude of 1 a unit vector. We can then preserve the direction of the original vector while simplifying calculations. Unit vectors are defined in terms of components. The horizontal unit vector is written as i = 〈1, 0〉 and is directed along the positive horizontal axis. The vertical unit vector is written as j = 〈0, 1〉 and is directed along the positive vertical axis. See Figure 14. x y j = 〈0, 1〉 i = 〈1, 0〉

the unit vectors If v is a nonzero vector, then  v _ ∣ v ∣  is a unit vector in the direction of v. Any vector divided by its magnitude is a unit vector. Notice that magnitude is always a scalar, and dividing by a scalar is the same as multiplying by the reciprocal of the scalar.

**Example  9**
Finding the Unit Vector in the Direction of v Find a unit vector in the same direction as v = 〈-5, 12〉. Solution First, we will find the magnitude.

| v | = \sqrt{(-5})^{2} + (12)^{2} 

= \sqrt{—}

= \sqrt{169} 

= 13 Then we divide each component by | v |, which gives a unit vector in the same direction as v:

 v _ | v |  = -  5 _ 13  i +  12 _ 13  j or, in component form

 v _ | v |  = 〈-  5 _ _ 13 〉 See Figure 15. x y - Verify that the magnitude of the unit vector equals 1. The magnitude of - 5 _ 13 i +  12 _ 13 j is given as

\sqrt{__________________}

 -  5 ___ 13   2 +   12 ___ 13   2  = \sqrt{_________}

 25 ____ ___

= \sqrt{____}

 169 _ 169 

= 1 The vector u =  5 ___ 13  i +  12 ___ 13  j is the unit vector in the same direction as v = 〈-5, 12〉. Performing Operations with Vectors in Terms of i and j So far, we have investigated the basics of vectors: magnitude and direction, vector addition and subtraction, scalar multiplication, the components of vectors, and the representation of vectors geometrically. Now that we are familiar with the general strategies used in working with vectors, we will represent vectors in rectangular coordinates in terms of i and j.

vectors in the rectangular plane Given a vector v with initial point P = (x^{1}, y^{1}) and terminal point Q = (x^{2}, y^{2}), v is written as v = (x^{2} - x^{1})i + (y^{1} - y^{2}) j The position vector from (0, 0) to (a, b), where (x^{2} - x^{1}) = a and (y^{2} - y^{1}) = b, is written as v = ai + bj. This vector sum is called a linear combination of the vectors i and j. The magnitude of v = ai + bj is given as | v | = \sqrt{a^{2}} + b^{2} . See Figure 16. v = ai + bj bj ai

**Example  10**

### Writing a Vector in Terms of i and j
Given a vector v with initial point P = (2, -6) and terminal point Q = (-6, 6), write the vector in terms of i and j. Solution Begin by writing the general form of the vector. Then replace the coordinates with the given values.

v = (x^{2} - x^{1})i + (y^{2} - y^{1}) j

= ( -6 - 2)i + (6 - ( - 6)) j

= - 8i + 12 j

**Example  11**

### Writing a Vector in Terms of i and j Using Initial and Terminal Points
Given initial point P^{1} = (-1, 3) and terminal point P^{2} = (2, 7), write the vector v in terms of i and j. Solution Begin by writing the general form of the vector. Then replace the coordinates with the given values.

v = (x^{2} - x^{1})i + (y^{2} - y^{1}) j

v = (2 - ( - 1))i + (7 - 3) j

= 3i + 4 j

**Try It #3**
Write the vector u with initial point P = (-1, 6) and terminal point Q = (7, - 5) in terms of i and j. Performing Operations on Vectors in Terms of i and j When vectors are written in terms of i and j, we can carry out addition, subtraction, and scalar multiplication by performing operations on corresponding components. adding and subtracting vectors in rectangular coordinates Given v = ai + bj and u = ci + dj, then

v + u = (a + c)i + (b + d)j

v - u = (a - c)i + (b - d)j


**Example  12**
Finding the Sum of the Vectors Find the sum of v^{1} = 2i - 3j and v^{2} = 4i + 5j. Solution According to the formula, we have

v^{1} + v^{2} = (2 + 4)i + ( - 3 + 5) j

= 6i + 2 j Calculating the Component Form of a Vector: Direction We have seen how to draw vectors according to their initial and terminal points and how to find the position vector. We have also examined notation for vectors drawn specifically in the Cartesian coordinate plane using i and j. For any of these vectors, we can calculate the magnitude. Now, we want to combine the key points, and look further at the ideas of magnitude and direction. Calculating direction follows the same straightforward process we used for polar coordinates. We find the direction of the vector by finding the angle to the horizontal. We do this by using the basic trigonometric identities, but with |v| replacing r. vector components in terms of magnitude and direction Given a position vector v = 〈x, y〉 and a direction angle \theta ,

cos \theta  =  x _ | v |  and sin \theta  =  y _ | v | 

x = | v | cos \theta  y = | v | sin \theta  Thus, v = xi + yj = |v|cos \theta i + |v|sin \theta j, and magnitude is expressed as |v| = \sqrt{x^{2}} + y^{2} .

**Example  13**

### Writing a Vector in Terms of Magnitude and Direction
Write a vector with length 7 at an angle of 135° to the positive x-axis in terms of magnitude and direction. Solution Using the conversion formulas x = |v| cos \theta i and y =|v| sin \theta  j, we find that

x = 7cos(135°)i

= -  7\sqrt{2}  _ 2 

y = 7sin(135°) j

=  7\sqrt{2}  _ 2  This vector can be written as v = 7cos(135°)i + 7sin(135°) j or simplified as

v = -  7\sqrt{2}  _ 2 i +  7\sqrt{2}  _ 2 j

**Try It #4**
A vector travels from the origin to the point (3, 5). Write the vector in terms of magnitude and direction. Finding the Dot Product of Two Vectors As we discussed earlier in the section, scalar multiplication involves multiplying a vector by a scalar, and the result is a vector. As we have seen, multiplying a vector by a number is called scalar multiplication. If we multiply a vector by a vector, there are two possibilities: the dot product and the cross product. We will only examine the dot product here; you may encounter the cross product in more advanced mathematics courses. The dot product of two vectors involves multiplying two vectors together, and the result is a scalar.

dot product The dot product of two vectors v = 〈a, b〉 and u = 〈c, d〉 is the sum of the product of the horizontal components and the product of the vertical components.

v ⋅ u = ac + bd To find the angle between the two vectors, use the formula below.

cos \theta  =  v ___ | v |  ⋅  u ___ | u | 

**Example  14**
Finding the Dot Product of Two Vectors Find the dot product of v = 〈5, 12〉 and u = 〈-3, 4〉. Solution Using the formula, we have

v ⋅ u = 〈5, 12〉 ⋅ 〈-3, 4〉

= 5 ⋅ ( -3) + 12 ⋅ 4

= 33

**Example  15**
Finding the Dot Product of Two Vectors and the Angle between Them Find the dot product of v^{1} = 5i + 2j and v^{2} = 3i + 7j. Then, find the angle between the two vectors. Solution Finding the dot product, we multiply corresponding components.

v^{1} ⋅ v^{2} = 〈5, 2〉 ⋅ 〈3, 7〉

= 5 ⋅ 3 + 2 ⋅ 7

= 29 To find the angle between them, we use the formula cos \theta  =  v _ | v |  ⋅  u _ | u | 

 v _ | v |  ⋅  u _ | u |  = 〈 ______ \sqrt{29}   +  ______ \sqrt{29}  〉 ⋅ 〈 ______ \sqrt{58}   +  ______ \sqrt{58}  〉

=  ______ \sqrt{29}   ⋅  ______ \sqrt{58}   +  ______ \sqrt{29}   ⋅  ______ \sqrt{58}  

=  ________ \sqrt{—}  +  ________ \sqrt{—}  =  ________ \sqrt{See} Figure 17. x y 45°


**Example  16**
Finding the Angle between Two Vectors Find the angle between u = 〈-3, 4〉 and v = 〈5, 12〉. Solution Using the formula, we have

\theta  = cos-1   u _ | u |  ⋅  v _ | v |   

  u _ ∣ u ∣  ⋅  v _ ∣ v ∣    =  -3i + 4j _  ⋅  5i + 12j _ 

=  - 3 _ 5  ⋅  5 _ 13    +   4 _ 5  ⋅  12 _ 13   

= - 15 _ _ 65 

=  33 _ 65 

\theta  = cos-1  33 _ 65   

See Figure 18. x y 59.5°

**Example  17**
Finding Ground Speed and Bearing Using Vectors We now have the tools to solve the problem we introduced in the opening of the section. An airplane is flying at an airspeed of 200 miles per hour headed on a SE bearing of 140°. A north wind (from north to south) is blowing at 16.2 miles per hour. What are the ground speed and actual bearing of the plane? See Figure 19. N A O B X C 140 ̊ 16.2 \alpha  Solution The ground speed is represented by x in the diagram, and we need to find the angle \alpha  in order to calculate the adjusted bearing, which will be 140° + \alpha  .

Notice in Figure 19, that angle BCO must be equal to angle AOC by the rule of alternating interior angles, so angle BCO is 140°. We can find x by the Law of Cosines:

x = \sqrt{The} ground speed is approximately 213 miles per hour. Now we can calculate the bearing using the Law of Sines.

 sin \alpha  _ 16.2  =  sin(140°) _

sin \alpha  =  16.2sin(140°) __ 212.7 

Therefore, the plane has a SE bearing of 140° + 2.8° = 142.8°. The ground speed is 212.7 miles per hour. Access these online resources for additional instruction and practice with vectors. • Introduction to Vectors (http://openstaxcollege.org/l/introvectors) • Vector Operations (http://openstaxcollege.org/l/vectoroperation) • The Unit Vector (http://openstaxcollege.org/l/unitvector)


## 8.8 Section Exercises

### 8.8 Section Exercises
Verbal 1. What are the characteristics of the letters that are commonly used to represent vectors? 2. How is a vector more specific than a line segment? 3. What are i and j, and what do they represent? 4. What is component form? 5. When a unit vector is expressed as 〈a, b〉, which letter is the coefficient of the i and which the j? Algebraic 6. Given a vector with initial point (5, 2) and terminal point (-1, - 3), find an equivalent vector whose initial point is (0, 0). Write the vector in component form 〈a, b〉. 7. Given a vector with initial point (-4, 2) and terminal point (3, - 3), find an equivalent vector whose initial point is (0, 0). Write the vector in component form 〈a, b〉. 8. Given a vector with initial point (7, - 1) and terminal point (-1, - 7), find an equivalent vector whose initial point is (0, 0). Write the vector in component form 〈a, b〉. For the following exercises, determine whether the two vectors u and v are equal, where u has an initial point P^{1} and a terminal point P^{2} and v has an initial point P^{3} and a terminal point P^{4}. P^{4} = (9, - 4) P^{4} = (-1, - 4) 14. Given initial point P^{1} = (-3, 1) and terminal point P^{2} = (5, 2), write the vector v in terms of i and j. 15. Given initial point P^{1} = (6, 0) and terminal point P^{2} = (-1, - 3), write the vector v in terms of i and j. For the following exercises, use the vectors u = i + 5j, v = -2i - 3j, and w = 4i - j. 16. Find u + (v - w) 17. Find 4v + 2u For the following exercises, use the given vectors to compute u + v, u - v, and 2u - 3v. 18. u = 〈2, - 3〉 , v = 〈1, 5〉 19. u = 〈-3, 4〉 , v = 〈-2, 1〉 20. Let v = -4i + 3j. Find a vector that is half the length and points in the same direction as v. 21. Let v = 5i + 2j. Find a vector that is twice the length and points in the opposite direction as v. For the following exercises, find a unit vector in the same direction as the given vector. 22. a = 3i + 4j 23. b = -2i + 5j 24. c = 10i - j 25. d = -  1 __ 3 i +  5 __ 2 j 27. u = -14i + 2j For the following exercises, find the magnitude and direction of the vector, 0 \le  \theta  < 2\pi . 32. Given u = 3i - 4j and v = -2i + 3j, calculate u ⋅ v. 33. Given u = -i - j and v = i + 5j, calculate u ⋅ v. 34. Given u = 〈-2, 4〉 and v = 〈-3, 1〉, calculate u ⋅ v. 35. Given u = 〈-1, 6〉 and v = 〈6, - 1〉, calculate u ⋅ v.

Graphical For the following exercises, given v, draw v, 3v and  1 __ 2 v. For the following exercises, use the vectors shown to sketch u + v, u - v, and 2u. v u v u v u For the following exercises, use the vectors shown to sketch 2u + v. u v u v For the following exercises, use the vectors shown to sketch u - 3v. u v u v For the following exercises, write the vector shown in component form.

48. Given initial point P^{1} = (2, 1) and terminal point  P^{2} = (-1, 2), write the vector v in terms of i and j, then draw the vector on the graph. 49. Given initial point P^{1} = (4, - 1) and terminal point  P^{2} = (-3, 2), write the vector v in terms of i and j. Draw the points and the vector on the graph. 50. Given initial point P^{1} = (3, 3) and terminal point  P^{2} = (-3, 3), write the vector v in terms of i and j. Draw the points and the vector on the graph. Extensions For the following exercises, use the given magnitude and direction in standard position, write the vector in component form. 51. | v | = 6, \theta  = 45 ° 52. | v | = 8, \theta  = 220° 53. | v | = 2, \theta  = 300° 54. | v | = 5, \theta  = 135° 55. A 60-pound box is resting on a ramp that is inclined 12°. Rounding to the nearest tenth, a. Find the magnitude of the normal (perpendicular) component of the force. b. Find the magnitude of the component of the force that is parallel to the ramp. 56. A 25-pound box is resting on a ramp that is inclined 8°. Rounding to the nearest tenth, a. Find the magnitude of the normal (perpendicular) component of the force. b. Find the magnitude of the component of the force that is parallel to the ramp. 57. Find the magnitude of the horizontal and vertical components of a vector with magnitude 8 pounds pointed in a direction of 27° above the horizontal. Round to the nearest hundredth. 58. Find the magnitude of the horizontal and vertical components of the vector with magnitude 4 pounds pointed in a direction of 127° above the horizontal. Round to the nearest hundredth. 59. Find the magnitude of the horizontal and vertical components of a vector with magnitude 5 pounds pointed in a direction of 55° above the horizontal. Round to the nearest hundredth. 60. Find the magnitude of the horizontal and vertical components of the vector with magnitude 1 pound pointed in a direction of 8° above the horizontal. Round to the nearest hundredth. Real-World Applications 61. A woman leaves home and walks 3 miles west, then 2 miles southwest. How far from home is she, and in what direction must she walk to head directly home? 62. A boat leaves the marina and sails 6 miles north, then 2 miles northeast. How far from the marina is the boat, and in what direction must it sail to head directly back to the marina? 63. A man starts walking from home and walks 4 miles east, 2 miles southeast, 5 miles south, 4 miles southwest, and 2 miles east. How far has he walked? If he walked straight home, how far would he have to walk? 64. A woman starts walking from home and walks 4 miles east, 7 miles southeast, 6 miles south, 5 miles southwest, and 3 miles east. How far has she walked? If she walked straight home, how far would she have to walk? 65. A man starts walking from home and walks 3 miles at 20° north of west, then 5 miles at 10° west of south, then 4 miles at 15° north of east. If he walked straight home, how far would he have to the walk, and in what direction? 66. A woman starts walking from home and walks 6 miles at 40° north of east, then 2 miles at 15° east of south, then 5 miles at 30° south of west. If she walked straight home, how far would she have to walk, and in what direction?

67. An airplane is heading north at an airspeed of 600 km/hr, but there is a wind blowing from the southwest at 80 km/hr. How many degrees off course will the plane end up flying, and what is the plane’s speed relative to the ground? 68. An airplane is heading north at an airspeed of 500 km/hr, but there is a wind blowing from the northwest at 50 km/hr. How many degrees off course will the plane end up flying, and what is the plane’s speed relative to the ground? 69. An airplane needs to head due north, but there is a wind blowing from the southwest at 60 km/hr. The plane flies with an airspeed of 550 km/hr. To end up flying due north, how many degrees west of north will the pilot need to fly the plane? 70. An airplane needs to head due north, but there is a wind blowing from the northwest at 80 km/hr. The plane flies with an airspeed of 500 km/hr. To end up flying due north, how many degrees west of north will the pilot need to fly the plane? 71. As part of a video game, the point (5, 7) is rotated counterclockwise about the origin through an angle of 35°. Find the new coordinates of this point. 72. As part of a video game, the point (7, 3) is rotated counterclockwise about the origin through an angle of 40°. Find the new coordinates of this point. 73. Two children are throwing a ball back and forth straight across the back seat of a car. The ball is being thrown 10 mph relative to the car, and the car is traveling 25 mph down the road. If one child doesn't catch the ball, and it flies out the window, in what direction does the ball fly (ignoring wind resistance)? 74. Two children are throwing a ball back and forth straight across the back seat of a car. The ball is being thrown 8 mph relative to the car, and the car is traveling 45 mph down the road. If one child doesn't catch the ball, and it flies out the window, in what direction does the ball fly (ignoring wind resistance)? 75. A 50-pound object rests on a ramp that is inclined 19°. Find the magnitude of the components of the force parallel to and perpendicular to (normal) the ramp to the nearest tenth of a pound. 76. Suppose a body has a force of 10 pounds acting on it to the right, 25 pounds acting on it upward, and 5 pounds acting on it 45° from the horizontal. What single force is the resultant force acting on the body? 77. Suppose a body has a force of 10 pounds acting on it to the right, 25 pounds acting on it -135° from the horizontal, and 5 pounds acting on it directed 150° from the horizontal. What single force is the resultant force acting on the body? 78. The condition of equilibrium is when the sum of the forces acting on a body is the zero vector. Suppose a body has a force of 2 pounds acting on it to the right, 5 pounds acting on it upward, and 3 pounds acting on it 45° from the horizontal. What single force is needed to produce a state of equilibrium on the body? 79. Suppose a body has a force of 3 pounds acting on it to the left, 4 pounds acting on it upward, and 2 pounds acting on it 30° from the horizontal. What single force is needed to produce a state of equilibrium on the body? Draw the vector.


### Key Terms
altitude a perpendicular line from one vertex of a triangle to the opposite side, or in the case of an obtuse triangle, to the line containing the opposite side, forming two right triangles ambiguous case a scenario in which more than one triangle is a valid solution for a given oblique SSA triangle Archimedes’ spiral a polar curve given by r = \theta . When multiplied by a constant, the equation appears as r = a\theta . As r = \theta , the curve continues to widen in a spiral path over the domain. argument the angle associated with a complex number; the angle between the line from the origin to the point and the positive real axis cardioid a member of the limaçon family of curves, named for its resemblance to a heart; its equation is given as r = a \pm  bcos \theta  and r = a \pm  bsin \theta , where  a _ b  = 1 convex limaçon a type of one-loop limaçon represented by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  such that  a _ b  \ge  2 De Moivre’s Theorem formula used to find the nth power or nth roots of a complex number; states that, for a positive integer n, z n is found by raising the modulus to the nth power and multiplying the angles by n dimpled limaçon a type of one-loop limaçon represented by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  such that 1 <  a _ b  < 2 dot product given two vectors, the sum of the product of the horizontal components and the product of the vertical components Generalized Pythagorean Theorem an extension of the Law of Cosines; relates the sides of an oblique triangle and is used for SAS and SSS triangles initial point the origin of a vector inner-loop limaçon a polar curve similar to the cardioid, but with an inner loop; passes through the pole twice; represented by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  where a < b Law of Cosines states that the square of any side of a triangle is equal to the sum of the squares of the other two sides minus twice the product of the other two sides and the cosine of the included angle Law of Sines states that the ratio of the measurement of one angle of a triangle to the length of its opposite side is equal to the remaining two ratios of angle measure to opposite side; any pair of proportions may be used to solve for a missing angle or side lemniscate a polar curve resembling a figure 8 and given by the equation r 2 = a^{2} cos 2\theta  and r 2 = a^{2} sin 2\theta , a \neq  0 magnitude the length of a vector; may represent a quantity such as speed, and is calculated using the Pythagorean Theorem modulus the absolute value of a complex number, or the distance from the origin to the point (x, y); also called the amplitude oblique triangle any triangle that is not a right triangle one-loop limaçon a polar curve represented by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  such that a > 0, b > 0, and  a _ b  > 1; may be dimpled or convex; does not pass through the pole parameter a variable, often representing time, upon which x and y are both dependent polar axis on the polar grid, the equivalent of the positive x-axis on the rectangular grid polar coordinates on the polar grid, the coordinates of a point labeled (r, \theta ), where \theta  indicates the angle of rotation from the polar axis and r represents the radius, or the distance of the point from the pole in the direction of \theta  polar equation an equation describing a curve on the polar grid polar form of a complex number a complex number expressed in terms of an angle \theta  and its distance from the origin r; can be found by using conversion formulas x = rcos \theta , y = rsin \theta , and r = \sqrt{x^{2}} + y^{2}  pole the origin of the polar grid

resultant a vector that results from addition or subtraction of two vectors, or from scalar multiplication rose curve a polar equation resembling a flower, given by the equations r = acos n\theta  and r = asin n\theta ; when n is even there are 2n petals, and the curve is highly symmetrical; when n is odd there are n petals. scalar a quantity associated with magnitude but not direction; a constant scalar multiplication the product of a constant and each component of a vector standard position the placement of a vector with the initial point at (0, 0) and the terminal point (a, b), represented by the change in the x-coordinates and the change in the y-coordinates of the original vector terminal point the end point of a vector, usually represented by an arrow indicating its direction unit vector a vector that begins at the origin and has magnitude of 1; the horizontal unit vector runs along the x-axis and is defined as v^{1} = 〈1, 0〉 the vertical unit vector runs along the y-axis and is defined as v^{2} = 〈0, 1〉. vector a quantity associated with both magnitude and direction, represented as a directed line segment with a starting point (initial point) and an end point (terminal point) vector addition the sum of two vectors, found by adding corresponding components Key Equations Law of Sines  sin \alpha  _____ a  =  sin \beta  ____ b  =  sin \gamma  ____ c   a _ sin \alpha   =  b _ sin \beta   =  c _ sin \gamma   Area for oblique triangles

Area =  1 _ 2 bcsin \alpha 

=  1 _ 2 acsin \beta 

=  1 _ 2 absin \gamma  Law of Cosines a^{2} = b^{2} + c^{2} - 2bccos \alpha  b^{2} = a^{2} + c^{2} - 2accos \beta  c^{2} = a^{2} + b^{2} - 2abcos \gamma  Heron’s formula Area = \sqrt{—}

s(s - a)(s - b)(s - c)  where s =  (a + b + c) _  Conversion formulas cos \theta  =  x _ r  → x = rcos \theta  sin \theta  =  y _ r  → y = rsin \theta  r^{2} = x^{2} + y^{2} tan \theta  =  y _ x 

### Key Concepts
• The Law of Sines can be used to solve oblique triangles, which are non-right triangles. • According to the Law of Sines, the ratio of the measurement of one of the angles to the length of its opposite side equals the other two ratios of angle measure to opposite side.

• There are three possible cases: ASA, AAS, SSA. Depending on the information given, we can choose the appropriate equation to find the requested solution. See Example 1. • The ambiguous case arises when an oblique triangle can have different outcomes. • There are three possible cases that arise from SSA arrangement—a single solution, two possible solutions, and no solution. See Example 2 and Example 3. • The Law of Sines can be used to solve triangles with given criteria. See Example 4. • The general area formula for triangles translates to oblique triangles by first finding the appropriate height value. See

**Example 5** — .
• There are many trigonometric applications. They can often be solved by first drawing a diagram of the given information and then using the appropriate equation. See Example 6. 8.2 Non-right Triangles: Law of Cosines • The Law of Cosines defines the relationship among angle measurements and lengths of sides in oblique triangles. • The Generalized Pythagorean Theorem is the Law of Cosines for two cases of oblique triangles: SAS and SSS. Dropping an imaginary perpendicular splits the oblique triangle into two right triangles or forms one right triangle, which allows sides to be related and measurements to be calculated. See Example 1 and Example 2. • The Law of Cosines is useful for many types of applied problems. The first step in solving such problems is generally to draw a sketch of the problem presented. If the information given fits one of the three models (the three equations), then apply the Law of Cosines to find a solution. See Example 3 and Example 4. • Heron’s formula allows the calculation of area in oblique triangles. All three sides must be known to apply Heron’s formula. See Example 5 and See Example 6. 8.3 Polar Coordinates • The polar grid is represented as a series of concentric circles radiating out from the pole, or origin. • To plot a point in the form (r, \theta ), \theta  > 0, move in a counterclockwise direction from the polar axis by an angle of \theta , and then extend a directed line segment from the pole the length of r in the direction of \theta . If \theta  is negative, move in a clockwise direction, and extend a directed line segment the length of r in the direction of \theta . See Example 1. • If r is negative, extend the directed line segment in the opposite direction of \theta . See Example 2. • To convert from polar coordinates to rectangular coordinates, use the formulas x = rcos \theta  and y = rsin \theta . See Example 3 and Example 4. • To convert from rectangular coordinates to polar coordinates, use one or more of the formulas: cos \theta  =  x _ r , sin \theta  =  y _ r , tan \theta  =  y _ x , and r = \sqrt{x^{2}} + y^{2} . See Example 5. • Transforming equations between polar and rectangular forms means making the appropriate substitutions based on the available formulas, together with algebraic manipulations. See Example 6, Example 7, and Example 8. • Using the appropriate substitutions makes it possible to rewrite a polar equation as a rectangular equation, and then graph it in the rectangular plane. See Example 9, Example 10, and Example 11. 8.4 Polar Coordinates: Graphs • It is easier to graph polar equations if we can test the equations for symmetry with respect to the line \theta  =  \pi  _ 2 , the polar axis, or the pole. • There are three symmetry tests that indicate whether the graph of a polar equation will exhibit symmetry. If an equation fails a symmetry test, the graph may or may not exhibit symmetry. See Example 1. • Polar equations may be graphed by making a table of values for \theta  and r. • The maximum value of a polar equation is found by substituting the value \theta  that leads to the maximum value of the trigonometric expression. • The zeros of a polar equation are found by setting r = 0 and solving for \theta . See Example 2. • Some formulas that produce the graph of a circle in polar coordinates are given by r = acos \theta  and r = asin \theta . See

**Example 3** — .
• The formulas that produce the graphs of a cardioid are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta , for a > 0, b > 0, and  a _ b  = 1. See Example 4.

• The formulas that produce the graphs of a one-loop limaçon are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  for 1 <  a _ b  < 2. See Example 5. • The formulas that produce the graphs of an inner-loop limaçon are given by r = a \pm  bcos \theta  and r = a \pm  bsin \theta  for a > 0, b > 0, and a < b. See Example 6. • The formulas that produce the graphs of a lemniscates are given by r^{2} = a^{2} cos 2\theta  and r^{2} = a^{2} sin 2\theta , where a \neq  0. See Example 7. • The formulas that produce the graphs of rose curves are given by r = acos n\theta  and r = asin n\theta , where a \neq  0; if n is even, there are 2n petals, and if n is odd, there are n petals. See Example 8 and Example 9. • The formula that produces the graph of an Archimedes’ spiral is given by r = \theta , \theta  \ge  0. See Example 10. 8.5 Polar Form of Complex Numbers • Complex numbers in the form a + bi are plotted in the complex plane similar to the way rectangular coordinates are plotted in the rectangular plane. Label the x-axis as the real axis and the y-axis as the imaginary axis. See Example 1. • The absolute value of a complex number is the same as its magnitude. It is the distance from the origin to the point:  ∣ z ∣ = \sqrt{a^{2}} + b^{2} . See Example 2 and Example 3. • To write complex numbers in polar form, we use the formulas x = rcos \theta , y = rsin \theta , and r = \sqrt{x^{2}} + y^{2} . Then, z = r(cos \theta  + isin \theta ). See Example 4 and Example 5. • To convert from polar form to rectangular form, first evaluate the trigonometric functions. Then, multiply through by r. See Example 6 and Example 7. • To find the product of two complex numbers, multiply the two moduli and add the two angles. Evaluate the trigonometric functions, and multiply using the distributive property. See Example 8. • To find the quotient of two complex numbers in polar form, find the quotient of the two moduli and the difference of the two angles. See Example 9. • To find the power of a complex number zn, raise r to the power n, and multiply \theta  by n. See Example 10. • Finding the roots of a complex number is the same as raising a complex number to a power, but using a rational exponent. See Example 11. 8.6 Parametric Equations • Parameterizing a curve involves translating a rectangular equation in two variables, x and y, into two equations in three variables, x, y, and t. Often, more information is obtained from a set of parametric equations. See Example 1,

**Example 2** — , and Example 3.
• Sometimes equations are simpler to graph when written in rectangular form. By eliminating t, an equation in x and y is the result. • To eliminate t, solve one of the equations for t, and substitute the expression into the second equation. See

**Example 4** — , Example 5, Example 6, and Example 7.
• Finding the rectangular equation for a curve defined parametrically is basically the same as eliminating the parameter. Solve for t in one of the equations, and substitute the expression into the second equation. See Example 8. • There are an infinite number of ways to choose a set of parametric equations for a curve defined as a rectangular equation. • Find an expression for x such that the domain of the set of parametric equations remains the same as the original rectangular equation. See Example 9.

• When there is a third variable, a third parameter on which x and y depend, parametric equations can be used. • To graph parametric equations by plotting points, make a table with three columns labeled t, x(t), and y(t). Choose values for t in increasing order. Plot the last two columns for x and y. See Example 1 and Example 2. • When graphing a parametric curve by plotting points, note the associated t-values and show arrows on the graph indicating the orientation of the curve. See Example 3 and Example 4. • Parametric equations allow the direction or the orientation of the curve to be shown on the graph. Equations that are not functions can be graphed and used in many applications involving motion. See Example 5. • Projectile motion depends on two parametric equations: x = (v^{0} cos \theta )t and y = - 16t^{2} + (v^{0} sin \theta )t + h. Initial velocity is symbolized as v^{0}. \theta  represents the initial angle of the object when thrown, and h represents the height at which the object is propelled. 8.8 Vectors • The position vector has its initial point at the origin. See Example 1. • If the position vector is the same for two vectors, they are equal. See Example 2. Vectors are defined by their magnitude and direction. See Example 3. • If two vectors have the same magnitude and direction, they are equal. See Example 4. • Vector addition and subtraction result in a new vector found by adding or subtracting corresponding elements. See

**Example 5** — .
• Scalar multiplication is multiplying a vector by a constant. Only the magnitude changes; the direction stays the same. See Example 6 and Example 7. • Vectors are comprised of two components: the horizontal component along the positive x-axis, and the vertical component along the positive y-axis. See Example 8. • The unit vector in the same direction of any nonzero vector is found by dividing the vector by its magnitude. • The magnitude of a vector in the rectangular coordinate system is ∣ v ∣ = \sqrt{a^{2}} + b^{2} . See Example 9. • In the rectangular coordinate system, unit vectors may be represented in terms of i and j where i represents the horizontal component and j represents the vertical component. Then, v = ai + bj is a scalar multiple of v by real numbers a and b. See Example 10 and Example 11. • Adding and subtracting vectors in terms of i and j consists of adding or subtracting corresponding coefficients of i and corresponding coefficients of j. See Example 12. • A vector v = ai + bj is written in terms of magnitude and direction as v = ∣ v ∣cos \theta i + ∣ v ∣sin \theta j. See Example 13. • The dot product of two vectors is the product of the i terms plus the product of the j terms. See Example 14. • We can use the dot product to find the angle between two vectors. Example 15 and Example 16. • Dot products are useful for many types of physics applications. See Example 17.

Non-right Triangles: Law of Sines For the following exercises, assume \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c. Solve each triangle, if possible. Round each answer to the nearest tenth. 3. Solve the triangle.

a c C 24° 36° 4. Find the area of the triangle.

75° 5. A pilot is flying over a straight highway. He determines the angles of depression to two mileposts, 2.1 km apart, to be 25° and 49°, as shown in Figure 1. Find the distance of the plane from point A and the elevation of the plane.

Non-right Triangles: Law of Cosines 6. Solve the triangle, rounding to the nearest tenth, assuming \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c: a = 4, b = 6, c = 8. 7. Solve the triangle in Figure 2, rounding to the nearest tenth.

54° B C a 8. Find the area of a triangle with sides of length 8.3, 6.6, and 9.1. 9. To find the distance between two cities, a satellite calculates the distances and angle shown in Figure 3 (not to scale). Find the distance between the cities. Round answers to the nearest tenth.

1.8° A B

Polar Coordinates 10. Plot the point with polar coordinates  3,  \pi  __ 6   . 11. Plot the point with polar coordinates  5, -  2\pi  ___ 3    12. Convert  6, -  3\pi  ___ 4    to rectangular coordinates. 13. Convert  -2,  3\pi  ___ 2    to rectangular coordinates. 14. Convert (7, -2) to polar coordinates. 15. Convert (-9, -4) to polar coordinates. For the following exercises, convert the given Cartesian equation to a polar equation. 18. x^{2} + y^{2} = - 2y For the following exercises, convert the given polar equation to a Cartesian equation. 19. r = 7cos \theta  20. r =  -2 ____________

4cos \theta  + sin \theta   For the following exercises, convert to rectangular form and graph. 21. \theta  =  3\pi  ___ 4  22. r = 5sec \theta  Polar Coordinates: Graphs For the following exercises, test each equation for symmetry. 23. r = 4 + 4sin \theta  25. Sketch a graph of the polar equation r = 1 - 5sin \theta . Label the axis intercepts. 26. Sketch a graph of the polar equation r = 5sin(7\theta ). 27. Sketch a graph of the polar equation r = 3 - 3cos \theta  Polar Form of Complex Numbers For the following exercises, find the absolute value of each complex number. Write the complex number in polar form. __ 2  -  \sqrt{3}  ____ 2  i For the following exercises, convert the complex number from polar to rectangular form. 32. z = 5cis   5\pi  ___ 6    33. z = 3cis(40°) For the following exercises, find the product z^{1}z^{2} in polar form. 34. z^{1} = 2cis(89°), z^{2} = 5cis(23°) 35. z^{1} = 10cis   \pi  __ 6   , z^{2} = 6cis   \pi  __ 3    For the following exercises, find the quotient  z^{1} _ z^{2}  in polar form. 37. z^{1} = 27cis   5\pi  ___ 3   , z^{2} = 9cis   \pi  __ 3    For the following exercises, find the powers of each complex number in polar form. 38. Find z^{4} when z = 2cis(70°) 39. Find z^{2} when z = 5cis   3\pi  ___ 4    For the following exercises, evaluate each root. 40. Evaluate the cube root of z when z = 64cis(210°). 41. Evaluate the square root of z when z = 25cis   3\pi  ___ 2   . For the following exercises, plot the complex number in the complex plane. Parametric Equations For the following exercises, eliminate the parameter t to rewrite the parametric equation as a Cartesian equation. 44.  x(t) = 3t - 1

y(t) = \sqrt{—} t 

   45.  x(t) = - cos t

y(t) = 2sin^{2} t   

46. Parameterize (write a parametric equation for) each Cartesian equation by using x(t) = acos t and y(t) = bsin t for  x^{2}

___ 25  +  y^{2}

___ 47. Parameterize the line from (-2, 3) to (4, 7) so that the line is at (-2, 3) at t = 0 and (4, 7) at t = 1. Parametric Equations: Graphs For the following exercises, make a table of values for each set of parametric equations, graph the equations, and include an orientation; then write the Cartesian equation. 48.  x(t) = 3t^{2}

y(t) = 2t - 1    49.  x(t) = e t

y(t) = -2e 5t  50.  x(t) = 3cos t

y(t) = 2sin t    51. A ball is launched with an initial velocity of 80 feet per second at an angle of 40° to the horizontal. The ball is released at a height of 4 feet above the ground. a. Find the parametric equations to model the path of the ball. b. Where is the ball after 3 seconds? c. How long is the ball in the air? Vectors For the following exercises, determine whether the two vectors, u and v, are equal, where u has an initial point P^{1} and a terminal point P^{2}, and v has an initial point P^{3} and a terminal point P^{4}. P^{4} = (-8, 2) For the following exercises, use the vectors u = 2i - j, v = 4i - 3j, and w = -2i + 5j to evaluate the expression. 54. u - v 55. 2v - u + w For the following exercises, find a unit vector in the same direction as the given vector. 56. a = 8i - 6j 57. b = -3i - j For the following exercises, find the magnitude and direction of the vector. For the following exercises, calculate u ⋅ v. 60. u = -2i + j and v = 3i + 7j 61. u = i + 4j and v = 4i + 3j 62. Given v = 〈-3, 4〉 draw v, 2v, and  1 _ 2 v. 63. Given the vectors shown in Figure 4, sketch u + v, u - v and 3v. u v 64. Given initial point P^{1} = (3, 2) and terminal point P^{2} = (-5, -1), write the vector v in terms of i and j. Draw the points and the vector on the graph.

1. Assume \alpha  is opposite side a, \beta  is opposite side b, and \gamma  is opposite side c. Solve the triangle, if possible, and round each answer to the nearest tenth, given \beta  = 68°, 2. Find the area of the triangle in Figure 1. Round each answer to the nearest tenth. 6.25 60° 3. A pilot flies in a straight path for 2 hours. He then makes a course correction, heading 15° to the right of his original course, and flies 1 hour in the new direction. If he maintains a constant speed of 575 miles per hour, how far is he from his starting position? 4. Convert (2, 2) to polar coordinates, and then plot the point. 5. Convert  2,  \pi  __ 3   to rectangular coordinates. 6. Convert the polar equation to a Cartesian equation: x^{2} + y^{2} = 5y. 7. Convert to rectangular form and graph: r = - 3csc \theta . 8. Test the equation for symmetry: r = - 4sin (2\theta ). 9. Graph r = 3 + 3cos \theta . 10. Graph r = 3 - 5sin \theta . 11. Find the absolute value of the complex number 12. Write the complex number in polar form: 4 + i. 13. Convert the complex number from polar to rectangular form: z = 5cis  2\pi  ___ 3   . Given z^{1} = 8cis(36°) and z^{2} = 2cis(15°), evaluate each expression. 15.  z^{1} _ z^{2} 

z^{1}  18. Plot the complex number -5 - i in the complex plane. 19. Eliminate the parameter t to rewrite the following parametric equations as a Cartesian equation:  x(t) = t + 1

y(t) = 2t^{2}   20. Parameterize (write a parametric equation for) the following Cartesian equation by using x(t) = acos t and y(t) = bsin t:  x^{2} ___ 36  +  y^{2}

___ 21. Graph the set of parametric equations and find the Cartesian equation:  x(t) = -2sin t

y(t) = 5cos t   22. A ball is launched with an initial velocity of 95 feet per second at an angle of 52° to the horizontal. The ball is released at a height of 3.5 feet above the ground. a. Find the parametric equations to model the path of the ball. b. Where is the ball after 2 seconds? c. How long is the ball in the air? For the following exercises, use the vectors u = i -3j and v = 2i + 3j. 24. Calculate u ∙ v. 25. Find a unit vector in the same direction as v. 26. Given vector v has an initial point P^{1} = (2, 2) and terminal point P^{2} = (-1, 0), write the vector v in terms of i and j. On the graph, draw v, and - v.
