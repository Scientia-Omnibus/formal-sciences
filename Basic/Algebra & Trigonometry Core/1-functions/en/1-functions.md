# Functions

## Introduction
Toward the end of the twentieth century, the values of stocks of internet and technology companies rose dramatically. As a result, the Standard and Poor’s stock market average rose as well. Figure 1 tracks the value of that initial investment of just under $100 over the 40 years. It shows that an investment that was worth less than $500 until about 1995 skyrocketed up to about $1,100 by the beginning of 2000. That five-year period became known as the “dot-com bubble” because so many internet startups were formed. As bubbles tend to do, though, the dot-com bubble eventually burst. Many companies grew too fast and then suddenly went out of business. The result caused the sharp decline represented on the graph beginning at the end of 2000. Notice, as we consider this example, that there is a definite relationship between the year and stock market average. For any year we choose, we can determine the corresponding value of the stock market average. In this chapter, we will explore these kinds of relationships and their properties. 1.1 Functions and Function Notation 1.2 Domain and Range 1.3 Rates of Change and Behavior of Graphs 1.4 Composition of Functions 1.5 Transformation of Functions 1.6 Absolute Value Functions 1.7 Inverse Functions


## 1.1 Functions and Function Notation
A jetliner changes altitude as its distance from the starting point of a flight increases. The weight of a growing child increases with time. In each case, one quantity depends on another. There is a relationship between the two quantities that we can describe, analyze, and use to make predictions. In this section, we will analyze such relationships. Determining Whether a Relation Represents a Function A relation is a set of ordered pairs. The set of the first components of each ordered pair is called the domain and the set of the second components of each ordered pair is called the range. Consider the following set of ordered pairs. The first numbers in each pair are the first five natural numbers. The second number in each pair is twice that of the first. The domain is {1, 2, 3, 4, 5}. The range is {2, 4, 6, 8, 10}. Note that each value in the domain is also known as an input value, or independent variable, and is often labeled with the lowercase letter x. Each value in the range is also known as an output value, or dependent variable, and is often labeled lowercase letter y. A function f is a relation that assigns a single value in the range to each value in the domain. In other words, no x-values are repeated. For our example that relates the first five natural numbers to numbers double their values, this relation is a function because each element in the domain, {1, 2, 3, 4, 5}, is paired with exactly one element in the range, Now let’s consider the set of ordered pairs that relates the terms “even” and “odd” to the first five natural numbers. It would appear as {(odd, 1), (even, 2), (odd, 3), (even, 4), (odd, 5)} Notice that each element in the domain, {even, odd} is not paired with exactly one element in the range, {1, 2, 3, 4, 5}. For example, the term “odd” corresponds to three values from the domain, {1, 3, 5} and the term “even” corresponds to two values from the range, {2, 4}. This violates the definition of a function, so this relation is not a function. Figure 1 compares relations that are functions and not functions. Relation is a Function Inputs Outputs Inputs Outputs Inputs Outputs Relation is a Function Relation is NOT a Function (a) (b) (c) p q r m n p q r x y z p q x y z ( b ) This relationship is also a function. In this case, each input is associated with a single output. ( c ) This relationship is not a function because input q is associated with two different outputs. function A function is a relation in which each possible input value leads to exactly one output value. We say “the output is a function of the input.” The input values make up the domain, and the output values make up the range. Learning Objectives
In this section, you will:
•
Determine whether a relation represents a function. • Find the value of a function. • Determine whether a function is one-to-one. • Use the vertical line test to identify functions. • Graph the functions listed in the library of functions.


**How To…**
Given a relationship between two quantities, determine whether the relationship is a function. 1. Identify the input values. 2. Identify the output values. 3. If each input value leads to only one output value, classify the relationship as a function. If any input value leads to two or more outputs, do not classify the relationship as a function.

**Example  1**

### Determining If Menu Price Lists Are Functions
The coffee shop menu, shown in Figure 2 consists of items and their prices. a. Is price a function of the item? b. Is the item a function of the price? Menu Item Price

**Solution**
a. Let’s begin by considering the input as the items on the menu. The output values are then the prices. See Figure 3. Menu Item Price Each item on the menu has only one price, so the price is a function of the item. b. Two items on the menu have the same price. If we consider the prices to be the input values and the items to be the output, then the same input value could have more than one output associated with it. See Figure 4. Menu Item Price Therefore, the item is a not a function of price.

**Example  2**

### Determining If Class Grade Rules Are Functions
In a particular math class, the overall percent grade corresponds to a grade point average. Is grade point average a function of the percent grade? Is the percent grade a function of the grade point average? Table 1 shows a possible rule for assigning grade points.

Percent grade Grade point average 0.0 1.0 1.5 2.0 2.5 3.0 3.5 4.0 Solution For any percent grade earned, there is an associated grade point average, so the grade point average is a function of the percent grade. In other words, if we input the percent grade, the output is a specific grade point average. In the grading system given, there is a range of percent grades that correspond to the same grade point average. For example, students who receive a grade point average of 3.0 could have a variety of percent grades ranging from 78 all the way to 86. Thus, percent grade is not a function of grade point average

**Try It #1**
lists the five greatest baseball players of all time in order of rank. Player Rank Babe Ruth Willie Mays Ty Cobb Walter Johnson Hank Aaron a. Is the rank a function of the player name? b. Is the player name a function of the rank? Using Function Notation Once we determine that a relationship is a function, we need to display and define the functional relationships so that we can understand and use them, and sometimes also so that we can program them into computers. There are various ways of representing functions. A standard function notation is one representation that facilitates working with functions. To represent “height is a function of age,” we start by identifying the descriptive variables h for height and a for age. The letters f, g, and h are often used to represent functions just as we use x, y, and z to represent numbers and A, B, and C to represent sets.

h is f of a We name the function f ; height is a function of age.

h = f (a) We use parentheses to indicate the function input.

f (a) We name the function f ; the expression is read as “f of a.” Remember, we can use any letter to name the function; the notation h(a) shows us that h depends on a. The value a must be put into the function h to get a result. The parentheses indicate that age is input into the function; they do not indicate multiplication. We can also give an algebraic expression as the input to a function. For example f (a + b) means “first add a and b, and the result is the input for the function f. ” The operations must be performed in this order to obtain the correct result. function notation The notation y = f (x) defines a function named f. This is read as “y is a function of x.” The letter x represents the input value, or independent variable. The letter y, or f (x), represents the output value, or dependent variable. 1 http://www.baseball-almanac.com/legendary/lisn^{1}00.shtml. Accessed 3/24/2014.


**Example  3**

### Using Function Notation for Days in a Month
Use function notation to represent a function whose input is the name of a month and output is the number of days in that month. Solution The number of days in a month is a function of the name of the month, so if we name the function f, we write days = f (month) or d = f (m). The name of the month is the input to a “rule” that associates a specific number (the output) with each input. 31f (January) output input rule For example, f (March) = 31, because March has 31 days. The notation d = f (m) reminds us that the number of days, d (the output), is dependent on the name of the month, m(the input). Analysis Note that the inputs to a function do not have to be numbers; function inputs can be names of people, labels of geometric objects, or any other element that determines some kind of output. However, most of the functions we will work with in this book will have numbers as inputs and outputs.

**Example  4**

### Interpreting Function Notation
A function N = f (y) gives the number of police officers, N, in a town in year y. What does f (2005) = 300 represent? Solution When we read f (2005) = 300, we see that the input year is 2005. The value for the output, the number of police officers (N), is 300. Remember N = f (y). The statement f (2005) = 300 tells us that in the year 2005 there were 300 police officers in the town.

**Try It #2**
Use function notation to express the weight of a pig in pounds as a function of its age in days d. Instead of a notation such as y = f (x), could we use the same symbol for the output as for the function, such as y = y (x), meaning “y is a function of x?” Yes, this is often done, especially in applied subjects that use higher math, such as physics and engineering. However, in exploring math itself we like to maintain a distinction between a function such as f, which is a rule or procedure, and the output y we get by applying f to a particular input x. This is why we usually use notation such as y = f (x), P = W(d), and so on. Representing Functions Using Tables A common method of representing functions is in the form of a table. The table rows or columns display the corresponding input and output values. In some cases, these values represent all we know about the relationship; other times, the table provides a few select examples from a more complete relationship. number of days in that month. This information represents all we know about the months and days for a given year (that is not a leap year). Note that, in this table, we define a days-in-a-month function f where D = f (m) identifies months by an integer rather than by name. Month number, m (input) Days in month, D (output)

input n and gives the output Q. n Q data available for the heights and ages of children. We can see right away that this table does not represent a function because the same input value, 5 years, has two different output values, 40 in. and 42 in. Age in years, a (input) Height in inches, h (output)

**How To…**
Given a table of input and output values, determine whether the table represents a function. 1. Identify the input and output values. 2. Check to see if each input value is paired with only one output value. If so, the table represents a function.

**Example  5**

### Identifying Tables that Represent Functions
Which table, Table 6, Table 7, or Table 8, represents a function (if any)?

Input Output

Input Output -3

Input Output Solution Table 6 and Table 7 define functions. In both, each input value corresponds to exactly one output value. When a table represents a function, corresponding input and output values can also be specified using function notation. The function represented by Table 6 can be represented by writing f (2) = 1, f (5) = 3, and f (8) = 6 Similarly, the statements g (-3) = 5, g (0) = 1, and g (4) = 5 represent the function in table Table 7.

**Try It #3**
Does Table 9 represent a function? Input Output


### Finding Input and Output Values of a Function
When we know an input value and want to determine the corresponding output value for a function, we evaluate the function. Evaluating will always produce one result because each input value of a function corresponds to exactly one output value. When we know an output value and want to determine the input values that would produce that output value, we set the output equal to the function’s formula and solve for the input. Solving can produce more than one solution because different input values can produce the same output value. Evaluation of Functions in Algebraic Forms When we have a function in formula form, it is usually a simple matter to evaluate the function. For example, the function f (x) = 5 - 3x 2 can be evaluated by squaring the input value, multiplying by 3, and then subtracting the product from 5.

**How To…**
Given the formula for a function, evaluate. 1. Replace the input variable in the formula with the value provided. 2. Calculate the result.

**Example  6**

### Evaluating Functions at Specific Values
Evaluate f(x) = x 2 + 3x - 4 at: a. 2 b. a c. a + h d.  f (a + h) - f (a)

__ h  Solution Replace the x in the function with each specified value. a. Because the input value is a number, 2, we can use simple algebra to simplify.

f (2) = 22 + 3(2) - 4

= 4 + 6 - 4

= 6 b. In this case, the input value is a letter so we cannot simplify the answer any further.

f (a) = a^{2} + 3a - 4 c. With an input value of a + h, we must use the distributive property.

f (a + h) = (a + h)^{2} + 3(a + h) - 4

= a^{2} + 2ah + h^{2} + 3a + 3h -4 d. In this case, we apply the input values to the function more than once, and then perform algebraic operations on the result. We already found that

f (a + h) = a^{2} + 2ah + h^{2} + 3a + 3h - 4 and we know that

f(a) = a^{2} + 3a - 4 Now we combine the results and simplify.

 f (a + h) - f(a)

__ h  =  (a^{2} + 2ah + h^{2} + 3a + 3h - 4) - (a^{2} + 3a - 4)

____

h 

=  2ah + h^{2} + 3h

___________ h 

=  h(2a + h + 3)

___________ h  Factor out h.

= 2a + h + 3

Simplify.


**Example  7**

### Evaluating Functions
Given the function h(p) = p^{2} + 2p, evaluate h(4). Solution To evaluate h(4), we substitute the value 4 for the input variable p in the given function.

h(p) = p^{2} + 2p

h(4) = (4)^{2} +2 (4)

= 24 Therefore, for an input of 4, we have an output of 24.

**Try It #4**
Given the function g(m) = \sqrt{m} - 4 . Evaluate g(5).

**Example  8**

### Solving Functions
Given the function h(p) = p^{2} + 2p, solve for h(p) = 3.

**Solution**
h(p) = 3

p^{2} + 2p = 3 Substitute the original function h(p) = p^{2} + 2p.

p^{2} + 2p - 3 = 0 Subtract 3 from each side.

(p + 3)(p - 1) = 0 Factor. If (p + 3)(p - 1) = 0, either (p + 3) = 0 or (p - 1) = 0 (or both of them equal 0). We will set each factor equal to 0 and solve for p in each case.

(p + 3) = 0, p = -3

(p - 1) = 0, p = 1 This gives us two solutions. The output h(p) = 3 when the input is either p = 1 or p = -3. We can also verify by graphing as in Figure 6. The graph verifies that h(1) = h(-3) = 3 and h(4) = 24. p h(p) p h(p)

**Try It #5**
Given the function g(m) = \sqrt{m} - 4 , solve g(m) = 2. Evaluating Functions Expressed in Formulas Some functions are defined by mathematical rules or procedures expressed in equation form. If it is possible to express the function output with a formula involving the input quantity, then we can define a function in algebraic form. For example, the equation 2n + 6p = 12 expresses a functional relationship between n and p. We can rewrite it to decide if p is a function of n.


**How To…**
Given a function in equation form, write its algebraic formula. 1. Solve the equation to isolate the output variable on one side of the equal sign, with the other side as an expression that involves only the input variable. 2. Use all the usual algebraic methods for solving equations, such as adding or subtracting the same quantity to or from both sides, or multiplying or dividing both sides of the equation by the same quantity.

**Example  9**
Finding an Equation of a Function Express the relationship 2n + 6p = 12 as a function p = f (n), if possible. Solution To express the relationship in this form, we need to be able to write the relationship where p is a function of n, which means writing it as p = [expression involving n].

2n + 6p = 12

6p = 12 - 2n Subtract 2n from both sides.

p =  12 - 2n _______  Divide both sides by 6 and simplify.

p =  12 __ 6  -  2n ___ 6 

p = 2 -  1 __ 3 n Therefore, p as a function of n is written as

p = f (n) = 2 -  1 __ 3 n Analysis It is important to note that not every relationship expressed by an equation can also be expressed as a function with a formula.

**Example  10**

### Expressing the Equation of a Circle as a Function
Does the equation x^{2} + y^{2} = 1 represent a function with x as input and y as output? If so, express the relationship as a function y = f (x). Solution First we subtract x^{2} from both sides.

y^{2} = 1 - x^{2} We now try to solve for y in this equation.

y = \pm \sqrt{1} - x^{2} 

= +\sqrt{1} - x^{2}  and -\sqrt{1} - x^{2}  We get two outputs corresponding to the same input, so this relationship cannot be represented as a single function y = f (x).

**Try It #6**
If x - 8y 3 = 0, express y as a function of x. Are there relationships expressed by an equation that do represent a function but which still cannot be represented by an algebraic formula? Yes, this can happen. For example, given the equation x = y + 2y, if we want to express y as a function of x, there is no simple algebraic formula involving only x that equals y. However, each x does determine a unique value for y, and there are mathematical procedures by which y can be found to any desired accuracy. In this case, we say that the equation gives an implicit (implied) rule for y as a function of x, even though the formula cannot be written explicitly.


### Evaluating a Function Given in Tabular Form
As we saw above, we can represent functions in tables. Conversely, we can use information in tables to write functions, and we can evaluate functions using the tables. For example, how well do our pets recall the fond memories we share with them? There is an urban legend that a goldfish has a memory of 3 seconds, but this is just a myth. Goldfish can remember up to 3 months, while the beta fish has a memory of up to 5 months. And while a puppy’s memory span is no longer than 30 seconds, the adult dog can remember for 5 minutes. This is meager compared to a cat, whose memory span lasts for 16 hours. The function that relates the type of pet to the duration of its memory span is more easily visualized with the use of a table. See Table 10. Pet Memory span in hours Puppy 0.008 Adult dog 0.083 Cat Goldfish Beta fish At times, evaluating a function in table form may be more useful than using equations. Here let us call the function P. The domain of the function is the type of pet and the range is a real number representing the number of hours the pet’s memory span lasts. We can evaluate the function P at the input value of “goldfish.” We would write P(goldfish) = 2160. Notice that, to evaluate the function in table form, we identify the input value and the corresponding output value from the pertinent row of the table. The tabular form for function P seems ideally suited to this function, more so than writing it in paragraph or function form.

**How To…**
Given a function represented by a table, identify specific output and input values. 1. Find the given input in the row (or column) of input values. 2. Identify the corresponding output value paired with that input value. 3. Find the given output values in the row (or column) of output values, noting every time that output value appears. 4. Identify the input value(s) corresponding to the given output value.

**Example  11**

### Evaluating and Solving a Tabular Function
Using Table 11, a. Evaluate g(3) b. Solve g(n) = 6. n g (n)

**Solution**
a. Evaluating g (3) means determining the output value of the function g for the input value of n = 3. The table output value corresponding to n = 3 is 7, so g (3) = 7. b. Solving g (n) = 6 means identifying the input values, n, that produce an output value of 6. Table 11 shows two solutions: 2 and 4. When we input 2 into the function g, our output is 6. When we input 4 into the function g, our output is also 6. 2 http://www.kgbanswers.com/how-long-is-a-dogs-memory-span/4221590. Accessed 3/24/2014.


**Try It #7**
Using Table 11, evaluate g(1). Finding Function Values from a Graph Evaluating a function using a graph also requires finding the corresponding output value for a given input value, only in this case, we find the output value by looking at the graph. Solving a function equation using a graph requires finding all instances of the given output value on the graph and observing the corresponding input value( s ).

**Example  12**
Reading Function Values from a Graph Given the graph in Figure 7, a. Evaluate f (2). b. Solve f (x) = 4. f (x)

**Solution**
a. To evaluate f (2), locate the point on the curve where x = 2, then read the y-coordinate of that point. The point has coordinates (2, 1), so f (2) = 1. See Figure 8. f (2) = 1 f (x) b. To solve f (x) = 4, we find the output value 4 on the vertical axis. Moving horizontally along the line y = 4, we locate two points of the curve with output value 4: (-1, 4) and (3, 4). These points represent the two solutions to f (x) = 4: -1 or 3. This means f (-1) = 4 and f (3) = 4, or when the input is -1 or 3, the output is 4. See Figure 9. f (x)


**Try It #8**
Using Figure 7, solve f (x) = 1. Determining Whether a Function is One-to-One Some functions have a given output value that corresponds to two or more input values. For example, in the stock chart shown in Figure 1 at the beginning of this chapter, the stock price was $1,000 on five different dates, meaning that there were five different input values that all resulted in the same output value of $1,000. However, some functions have only one input value for each output value, as well as having only one output for each input. We call these functions one-to-one functions. As an example, consider a school that uses only letter grades and decimal equivalents, as listed in Table 12. Letter grade Grade point average A 4.0 B 3.0 C 2.0 D 1.0 This grading system represents a one-to-one function, because each letter input yields one particular grade point average output and each grade point average corresponds to one input letter. To visualize this concept, let’s look again at the two simple functions sketched in Figure 1(a) and Figure 1(b). The function in part ( a) shows a relationship that is not a one-to-one function because inputs q and r both give output n. The function in part (b ) shows a relationship that is a one-to-one function because each input is associated with a single output. one-to-one function A one-to-one function is a function in which each output value corresponds to exactly one input value.

**Example  13**

### Determining Whether a Relationship Is a One-to-One Function
Is the area of a circle a function of its radius? If yes, is the function one-to-one? Solution A circle of radius r has a unique area measure given by A = \pi r 2, so for any input, r, there is only one output, A. The area is a function of radius r. If the function is one-to-one, the output value, the area, must correspond to a unique input value, the radius. Any area measure A is given by the formula A = \pi r^{2}. Because areas and radii are positive numbers, there is exactly one solution: r = \sqrt{___}

 A __ \pi     So the area of a circle is a one-to-one function of the circle’s radius.

**Try It #9**
a. Is a balance a function of the bank account number? b. Is a bank account number a function of the balance? c. Is a balance a one-to-one function of the bank account number?

**Try It #10**
a. If each percent grade earned in a course translates to one letter grade, is the letter grade a function of the percent grade? b. If so, is the function one-to-one?


### Using the Vertical Line Test
As we have seen in some examples above, we can represent a function using a graph. Graphs display a great many input-output pairs in a small space. The visual information they provide often makes relationships easier to understand. By convention, graphs are typically constructed with the input values along the horizontal axis and the output values along the vertical axis. The most common graphs name the input value x and the output value y, and we say y is a function of x, or y = f (x) when the function is named f. The graph of the function is the set of all points (x, y) in the plane that satisfies the equation y = f (x). If the function is defined for only a few input values, then the graph of the function is only a few points, where the x-coordinate of each point is an input value and the y-coordinate of each point is the corresponding output value. For example, the black dots on the graph in Figure 10 tell us that f (0) = 2 and f (6) = 1. However, the set of all points (x, y) satisfying y = f (x) is a curve. The curve shown includes (0, 2) and (6, 1) because the curve passes through those points. y x The vertical line test can be used to determine whether a graph represents a function. If we can draw any vertical line that intersects a graph more than once, then the graph does not define a function because a function has only one output value for each input value. See Figure 11. Function Not a Function Not a Function

**How To…**
Given a graph, use the vertical line test to determine if the graph represents a function. 1. Inspect the graph to see if any vertical line drawn would intersect the curve more than once. 2. If there is any such line, determine that the graph does not represent a function.


**Example  14**

### Applying the Vertical Line Test
Which of the graphs in Figure 12 represent( s ) a function y = f (x)? x f (x) y (a) (b) (c) x x f (x) Solution If any vertical line intersects a graph more than once, the relation represented by the graph is not a function. Notice that any vertical line would pass through only one point of the two graphs shown in parts ( a) and (b) of Figure 12. From this we can conclude that these two graphs represent functions. The third graph does not represent a function because, at most x-values, a vertical line would intersect the graph at more than one point, as shown in Figure 13. x y

**Try It #11**
Does the graph in Figure 14 represent a function? x y


### Using the Horizontal Line Test
Once we have determined that a graph defines a function, an easy way to determine if it is a one-to-one function is to use the horizontal line test. Draw horizontal lines through the graph. If any horizontal line intersects the graph more than once, then the graph does not represent a one-to-one function.

**How To…**
Given a graph of a function, use the horizontal line test to determine if the graph represents a one-to-one function. 1. Inspect the graph to see if any horizontal line drawn would intersect the curve more than once. 2. If there is any such line, determine that the function is not one-to-one.

**Example  15**
Horizontal Line Test Consider the functions shown in Figure 12(a) and Figure 12(b). Are either of the functions one-to-one? Solution The function in Figure 12(a) is not one-to-one. The horizontal line shown in Figure 15 intersects the graph of the function at two points (and we can even find horizontal lines that intersect it at three points.) x f (x) The function in Figure 12(b) is one-to-one. Any horizontal line will intersect a diagonal line at most once.

**Try It #12**
Is the graph shown here one-to-one? x y Identifying Basic Toolkit Functions In this text, we will be exploring functions—the shapes of their graphs, their unique characteristics, their algebraic formulas, and how to solve problems with them. When learning to read, we start with the alphabet. When learning to do arithmetic, we start with numbers. When working with functions, it is similarly helpful to have a base set of building-block elements. We call these our “toolkit functions,” which form a set of basic named functions for which

we know the graph, formula, and special properties. Some of these functions are programmed to individual buttons on many calculators. For these definitions we will use x as the input variable and y = f (x) as the output variable. We will see these toolkit functions, combinations of toolkit functions, their graphs, and their transformations frequently throughout this book. It will be very helpful if we can recognize these toolkit functions and their features quickly by name, formula, graph, and basic table properties. The graphs and sample table values are included with each function shown in Table 13. Toolkit Functions Name Function Graph Constant f (x) = c, where c is a constant x x f(x) f (x) Identity f (x) = x x x f(x) f (x) Absolute value f (x) = ∣ x ∣ x f (x) x f(x) Quadratic f (x) = x^{2} x x f(x) f (x) Cubic f (x) = x^{3} x 0.5 0.125 x f(x) f (x)

Reciprocal f (x) =  1 __ x  x 0.5 0.5 x f(x) f (x) Reciprocal squared f (x) =  1 _ x 2  x 0.25 0.5 0.25 x f(x) f (x) Square root f (x) = \sqrt{x}  x x f(x) f (x) Cube root f (x) =  \sqrt{x}  x 0.125 0.5 x f(x) f (x) Access the following online resources for additional instruction and practice with functions. • Determine if a Relation is a Function (http://openstaxcollege.org/l/relationfunction) • Vertical Line Test (http://openstaxcollege.org/l/vertlinetest) • Introduction to Functions (http://openstaxcollege.org/l/introtofunction) • Vertical Line Test of Graph (http://openstaxcollege.org/l/vertlinegraph) • One-to-one Functions (http://openstaxcollege.org/l/onetoone) • Graphs as One-to-one Functions (http://openstaxcollege.org/l/graphonetoone)


### 1.1 Section Exercises
Verbal 1. What is the difference between a relation and a function? 2. What is the difference between the input and the output of a function? 3. Why does the vertical line test tell us whether the graph of a relation represents a function? 4. How can you determine if a relation is a one-to-one function? 5. Why does the horizontal line test tell us whether the graph of a function is one-to-one? Algebraic For the following exercises, determine whether the relation represents a function. 6. {(a, b), (c, d), (a, c)} 7. {(a, b),(b, c),(c, c)} For the following exercises, determine whether the relation represents y as a function of x. 9. y = x 2 __ x  15. x =  3y + 5 ______ 7y - 1  16. x = \sqrt{1} - y 2  17. y =  3x + 5 ______ 7x - 1  22. y = \sqrt{1} - x 2  23. x = \pm \sqrt{1} - y  24. y = \pm \sqrt{1} - x  For the following exercises, evaluate the function f at the indicated values f (-3), f (2), f (-a), -f (a), f (a + h). 27. f (x) = 2x - 5 28. f (x) = -5x 2 + 2x - 1 29. f (x) = \sqrt{2} - x  + 5 30. f (x) =  6x - 1 ______ 5x + 2  31. f (x) = ∣ x - 1 ∣ - ∣ x + 1 ∣ 32. Given the function g(x) = 5 - x 2, evaluate  g(x + h) - g(x)

__ h , h \neq  0 33. Given the function g(x) = x 2 + 2x, evaluate  g(x) - g(a) _ x - a , x \neq  a 34. Given the function k(t) = 2t - 1: a. Evaluate k(2). b. Solve k(t) = 7. 35. Given the function f (x) = 8 - 3x: a. Evaluate f (-2). b. Solve f (x) = -1. 36. Given the function p(c) = c 2 + c: a. Evaluate p(-3). b. Solve p(c) = 2. 37. Given the function f (x) = x^{2} - 3x a. Evaluate f (5). b. Solve f (x) = 4 38. Given the function f (x) = \sqrt{x} + 2 : a. Evaluate f (7). b. Solve f (x) = 4 39. Consider the relationship 3r + 2t = 18. a. Write the relationship as a function r = f (t). b. Evaluate f (-3). c. Solve f (t) = 2.


## 1.1 Section Exercises
GRAPHICAL For the following exercises, use the vertical line test to determine which graphs show relations that are functions. x y x y x y x y x y x y x y x y x y x y x y x y

52. Given the following graph a. Evaluate f (-1). b. Solve for f (x) = 3. 53. Given the following graph a. Evaluate f (0). b. Solve for f (x) = -3. 54. Given the following graph a. Evaluate f (4). b. Solve for f (x) = 1. For the following exercises, determine if the given graph is a one-to-one function. x y x y x y x y x y \pi  \pi  Numeric For the following exercises, determine whether the relation represents a function. For the following exercises, determine if the relation represented in table form represents y as a function of x. x y x y x y For the following exercises, use the function f represented in Table 14 below. x f (x) 66. Evaluate f (3). 67. Solve f (x) = 1 x y x y x y

For the following exercises, evaluate the function f at the values f (-2), f (-1), f (0), f (1), and f (2). 68. f (x) = 4 - 2x 69. f (x) = 8 - 3x 70. f (x) = 8x^{2} - 7x + 3 71. f (x) = 3 + \sqrt{x} + 3  72. f (x) =  x - 2 _____ x + 3  73. f (x) = 3x For the following exercises, evaluate the expressions, given functions f, g, and h: f (x) = 3x - 2 g(x) = 5 - x^{2} h(x) = -2x^{2} + 3x - 1 75. f   7 __ 3   - h(-2) TECHNOLOGY For the following exercises, graph y = x^{2} on the given viewing window. Determine the corresponding range for each viewing window. Show each graph. For the following exercises, graph y = x^{3} on the given viewing window. Determine the corresponding range for each viewing window. Show each graph. For the following exercises, graph y = \sqrt{x}  on the given viewing window. Determine the corresponding range for each viewing window. Show each graph. For the following exercises, graph y =  \sqrt{x}  on the given viewing window. Determine the corresponding range for each viewing window. Show each graph. REal-world applications 88. The amount of garbage, G, produced by a city with population p is given by G = f (p). G is measured in tons per week, and p is measured in thousands of people. a. The town of Tola has a population of 40,000 and produces 13 tons of garbage each week. Express this information in terms of the function f. b. Explain the meaning of the statement f (5) = 2. 89. The number of cubic yards of dirt, D, needed to cover a garden with area a square feet is given by D = g(a). a. A garden with area 5,000 ft^{2} requires 50 yd^{3} of dirt. Express this information in terms of the function g. b. Explain the meaning of the statement g(100) = 1. 90. Let f (t) be the number of ducks in a lake t years after 1990. Explain the meaning of each statement: a. f (5) = 30 b. f (10) = 40 91. Let h(t) be the height above ground, in feet, of a rocket t seconds after launching. Explain the meaning of each statement: 92. Show that the function f (x) = 3(x - 5)^{2} + 7 is not one-to-one.


## 1.2 Domain and Range
If you’re in the mood for a scary movie, you may want to check out one of the five most popular horror movies of all time—I am Legend, Hannibal, The Ring, The Grudge, and The Conjuring. Figure 1 shows the amount, in dollars, each of those movies grossed when they were released as well as the ticket sales for horror movies in general by year. Notice that we can use the data to create a function of the amount each movie earned or the total ticket sales for all horror movies by year. In creating various functions using the data, we can identify different independent and dependent variables, and we can analyze the data and the functions to determine the domain and range. In this section, we will investigate methods for determining the domain and range of functions such as these. Inflation-adjusted Gross, in Millions of Dollars I am Legend Hannibal Top-Five Grossing Horror Movies Te Ring Te Grudge Te Conjuring

8% Market Share of Horror Moveis, by Year 7% 6% 5% 4% 3% 2% 1% 0% Finding the Domain of a Function Defined by an Equation In Functions and Function Notation, we were introduced to the concepts of domain and range. In this section, we will practice determining domains and ranges for specific functions. Keep in mind that, in determining domains and ranges, we need to consider what is physically possible or meaningful in real-world examples, such as tickets sales and year in the horror movie example above. We also need to consider what is mathematically permitted. For example, we cannot include any input value that leads us to take an even root of a negative number if the domain and range consist of real numbers. Or in a function expressed as a formula, we cannot include any input value in the domain that would lead us to divide by 0. We can visualize the domain as a “holding area” that contains “raw materials” for a “function machine” and the range as another “holding area” for the machine’s products. See Figure 2. Domain Function machine a b c x y z Range We can write the domain and range in interval notation, which uses values within brackets to describe a set of numbers. In interval notation, we use a square bracket [when the set includes the endpoint and a parenthesis (to indicate that the endpoint is either not included or the interval is unbounded. For example, if a person has $100 to spend, he or she would need to express the interval that is more than 0 and less than or equal to 100 and write (0, 100]. We will discuss interval notation in greater detail later. 3 The Numbers: Where Data and the Movie Business Meet. “Box Office History for Horror Movies.” http://www.the-numbers.com/market/genre/Horror. Accessed 3/24/2014 Learning Objectives
In this section, you will:
• Find the domain of a function defined by an equation.
• Graph piecewise-defined functions.
Let’s turn our attention to finding the domain of a function whose equation is provided. Oftentimes, finding the domain of such functions involves remembering three different forms. First, if the function has no denominator or an even root, consider whether the domain could be all real numbers. Second, if there is a denominator in the function’s equation, exclude values in the domain that force the denominator to be zero. Third, if there is an even root, consider excluding values that would make the radicand negative. Before we begin, let us review the conventions of interval notation: • The smallest term from the interval is written first. • The largest term in the interval is written second, following a comma. • Parentheses, (or), are used to signify that an endpoint is not included, called exclusive. • Brackets, [or], are used to indicate that an endpoint is included, called inclusive. See Figure 3 for a summary of interval notation. Inequality Interval Notation Graph on Number Line Description x > a (a, \infty ) a ( x is greater than a x < a (-\infty , a) a ( x is less than a x \ge  a [a, \infty ) a [ x is greater than or equal to a x \le  a (-\infty , a] a ] x is less than or equal to a a < x < b (a, b) a b ( ( x is strictly between a and b a \le  x < b [a, b) a b ( [ x is between a and b, to include a a < x \le  b (a, b] a b ] ( x is between a and b, to include b a \le  x \le  b [a, b] a b [ ] x is between a and b, to include a and b

**Example  1**

### Finding the Domain of a Function as a Set of Ordered Pairs
Find the domain of the following function: {(2, 10), (3, 10), (4, 20), (5, 30), (6, 40)}. Solution First identify the input values. The input value is the first coordinate in an ordered pair. There are no restrictions, as the ordered pairs are simply listed. The domain is the set of the first coordinates of the ordered pairs.

**Try It #1**
Find the domain of the function: {(-5, 4), (0, 0), (5, -4), (10, -8), (15, -12)}

**How To…**
Given a function written in equation form, find the domain. 1. Identify the input values. 2. Identify any restrictions on the input and exclude those values from the domain. 3. Write the domain in interval form, if possible.


**Example  2**

### Finding the Domain of a Function
Find the domain of the function f (x) = x^{2} - 1. Solution The input value, shown by the variable x in the equation, is squared and then the result is lowered by one. Any real number may be squared and then be lowered by one, so there are no restrictions on the domain of this function. The domain is the set of real numbers. In interval form, the domain of f is (-\infty , \infty ).

**Try It #2**
Find the domain of the function: f (x) = 5 - x + x 3.

**How To…**
Given a function written in an equation form that includes a fraction, find the domain. 1. Identify the input values. 2. Identify any restrictions on the input. If there is a denominator in the function’s formula, set the denominator equal to zero and solve for x. If the function’s formula contains an even root, set the radicand greater than or equal to 0, and then solve. 3. Write the domain in interval form, making sure to exclude any restricted values from the domain.

**Example  3**

### Finding the Domain of a Function Involving a Denominator
Find the domain of the function f (x) =  x + 1 _____ 2 - x . Solution When there is a denominator, we want to include only values of the input that do not force the denominator to be zero. So, we will set the denominator equal to 0 and solve for x.

2 - x = 0

-x = -2

x = 2 Now, we will exclude 2 from the domain. The answers are all real numbers where x < 2 or x > 2. We can use a symbol known as the union, ∪, to combine the two sets. In interval notation, we write the solution: (-\infty , 2) ∪ (2, \infty ). x < 2 or x > 2 ↓ ↓ (-\infty , 2) ∪ (2, \infty ) In interval form, the domain of f is (-\infty , 2) ∪ (2, \infty ).

**Try It #3**
Find the domain of the function: f (x) =  1 + 4x ______ 2x - 1 .

**How To…**
Given a function written in equation form including an even root, find the domain. 1. Identify the input values. 2. Since there is an even root, exclude any real numbers that result in a negative number in the radicand. Set the radicand greater than or equal to zero and solve for x. 3. The solution(s) are the domain of the function. If possible, write the answer in interval form.


**Example  4**

### Finding the Domain of a Function with an Even Root
Find the domain of the function f (x) = \sqrt{7} - x . Solution When there is an even root in the formula, we exclude any real numbers that result in a negative number in the radicand. Set the radicand greater than or equal to zero and solve for x.

7 - x \ge  0

-x \ge  -7

x \le  7 Now, we will exclude any number greater than 7 from the domain. The answers are all real numbers less than or equal to 7, or (-\infty , 7].

**Try It #4**
Find the domain of the function f (x) = \sqrt{5} + 2x . Can there be functions in which the domain and range do not intersect at all? Yes. For example, the function f (x) = - 1 _ \sqrt{x}   has the set of all positive real numbers as its domain but the set of all negative real numbers as its range. As a more extreme example, a function’s inputs and outputs can be completely different categories (for example, names of weekdays as inputs and numbers as outputs, as on an attendance chart), in such cases the domain and range have no elements in common. Using Notations to Specify Domain and Range In the previous examples, we used inequalities and lists to describe the domain of functions. We can also use inequalities, or other statements that might define sets of values or data, to describe the behavior of the variable in set-builder notation. For example, {x | 10 \le  x < 30} describes the behavior of x in set-builder notation. The braces { } are read as “the set of,” and the vertical bar | is read as “such that,” so we would read {x | 10 \le  x < 30} as “the set of x-values such that 10 is less than or equal to x, and x is less than 30.” Inequality Notation Set-builder Notation Interval Notation 5 < h \le  10 {h | 5 < h \le  10} 5 \le  h < 10 {h | 5 \le  h < 10} 5 < h < 10 {h | 5 < h < 10} h < 10 {h | h < 10} h \ge  10 {h | h \ge  10} All real numbers 핉 (-\infty , \infty )

To combine two intervals using inequality notation or set-builder notation, we use the word “or.” As we saw in earlier examples, we use the union symbol, ∪, to combine two unconnected intervals. For example, the union of the sets {2, 3, 5} and {4, 6} is the set {2, 3, 4, 5, 6}. It is the set of all elements that belong to one or the other (or both) of the original two sets. For sets with a finite number of elements like these, the elements do not have to be listed in ascending order of numerical value. If the original two sets have some elements in common, those elements should be listed only once in the union set. For sets of real numbers on intervals, another example of a union is {x | | x | \ge  3} = (-\infty , -3] ∪ [3, \infty ) set-builder notation and interval notation Set-builder notation is a method of specifying a set of elements that satisfy a certain condition. It takes the form {x | statement about x} which is read as, “the set of all x such that the statement about x is true.” For example, {x | 4 < x \le  12} Interval notation is a way of describing sets that include all real numbers between a lower limit that may or may not be included and an upper limit that may or may not be included. The endpoint values are listed between brackets or parentheses. A square bracket indicates inclusion in the set, and a parenthesis indicates exclusion from the set. For example,

**How To…**
Given a line graph, describe the set of values using interval notation. 1. Identify the intervals to be included in the set by determining where the heavy line overlays the real line. 2. At the left end of each interval, use [with each end value to be included in the set (solid dot) or (for each excluded end value (open dot). 3. At the right end of each interval, use] with each end value to be included in the set (filled dot) or) for each excluded end value (open dot). 4. Use the union symbol ∪ to combine all intervals into one set.

**Example  5**

### Describing Sets on the Real-Number Line
Describe the intervals of values shown in Figure 6 using inequality notation, set-builder notation, and interval notation. Solution To describe the values, x, included in the intervals shown, we would say, “x is a real number greater than or equal to 1 and less than or equal to 3, or a real number greater than 5.” Inequality 1 \le  x \le  3 or x > 5 Set-builder notation { x |1 \le  x \le  3 or x > 5 } Interval notation [1, 3] ∪ (5, \infty ) Remember that, when writing or reading interval notation, using a square bracket means the boundary is included in the set. Using a parenthesis means the boundary is not included in the set.


**Try It #5**
Given this figure, specify the graphed set in

a. words b. set-builder notation c. interval notation Finding Domain and Range from Graphs Another way to identify the domain and range of functions is by using graphs. Because the domain refers to the set of possible input values, the domain of a graph consists of all the input values shown on the x-axis. The range is the set of possible output values, which are shown on the y-axis. Keep in mind that if the graph continues beyond the portion of the graph we can see, the domain and range may be greater than the visible values. See Figure 8. x y Domain Range We can observe that the graph extends horizontally from -5 to the right without bound, so the domain is [-5, \infty ). The vertical extent of the graph is all range values 5 and below, so the range is (-\infty , 5]. Note that the domain and range are always written from smaller to larger values, or from left to right for domain, and from the bottom of the graph to the top of the graph for range.

**Example  6**

### Finding Domain and Range from a Graph
Find the domain and range of the function f whose graph is shown in Figure 9. f x y

Solution We can observe that the horizontal extent of the graph is -3 to 1, so the domain of f is (-3, 1]. The vertical extent of the graph is 0 to -4, so the range is [-4, 0]. See Figure 10. f Range Domain x y

**Example  7**

### Finding Domain and Range from a Graph of Oil Production
Find the domain and range of the function f whose graph is shown in Figure 11. Tousand barrels per day Alaska Crude Oil Production Solution The input quantity along the horizontal axis is “years,” which we represent with the variable t for time. The output quantity is “thousands of barrels of oil per day,” which we represent with the variable b for barrels. The graph may continue to the left and right beyond what is viewed, but based on the portion of the graph that is visible, we can determine the domain as 1973 \le  t \le  2008 and the range as approximately 180 \le  b \le  2010. In interval notation, the domain is [1973, 2008], and the range is about [180, 2010]. For the domain and the range, we approximate the smallest and largest values since they do not fall exactly on the grid lines.

**Try It #6**
Given Figure 12, identify the domain and range using interval notation. Millions of people World Population Increase Year

Can a function’s domain and range be the same? Yes. For example, the domain and range of the cube root function are both the set of all real numbers. 4 http://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCRFPAK^{2}&f=A.


### Finding Domains and Ranges of the Toolkit Functions
We will now return to our set of toolkit functions to determine the domain and range of each. x f(x) = c f(x) Domain: (-\infty , \infty ) Range: [c, c]

For the constant function f(x) = c, the domain consists of all real numbers; there are no restrictions on the input. The only output value is the constant c, so the range is the set {c} that contains this single element. In interval notation, this is written as [c, c], the interval that both begins and ends with c. x f(x) Domain: (-\infty , \infty ) Range: (-\infty , \infty ) For the identity function f(x) = x, there is no restriction on x. Both the domain and range are the set of all real numbers. x f(x) Domain: (-\infty , \infty ) Range: [0, \infty ) For the absolute value function f(x) = ∣ x ∣, there is no restriction on x. However, because absolute value is defined as a distance from 0, the output can only be greater than or equal to 0. Domain: (-\infty , \infty ) Range: [0, \infty ) x f(x) For the quadratic function f(x) = x 2, the domain is all real numbers since the horizontal extent of the graph is the whole real number line. Because the graph does not include any negative values for the range, the range is only nonnegative real numbers. Domain: (-\infty , \infty ) Range: (-\infty , \infty ) x f(x) For the cubic function f(x) = x 3, the domain is all real numbers because the horizontal extent of the graph is the whole real number line. The same applies to the vertical extent of the graph, so the domain and range include all real numbers.

x f(x) Domain: (-\infty , 0) ∪ (0, \infty ) Range: (-\infty , 0) ∪ (0, \infty ) For the reciprocal function f(x) =  1 _ x , we cannot divide by 0, so we must exclude 0 from the domain. Further, 1 divided by any value can never be 0, so the range also will not include 0. In set-builder notation, we could also write {x | x \neq  0}, the set of all real numbers that are not zero. Domain: (-\infty , 0) ∪ (0, \infty ) Range: (0, \infty ) x f(x) For the reciprocal squared function f(x) =  1 __ x 2 , we cannot divide by 0, so we must exclude 0 from the domain. There is also no x that can give an output of 0, so 0 is excluded from the range as well. Note that the output of this function is always positive due to the square in the denominator, so the range includes only positive numbers. x f(x) Domain: [0, \infty ) Range: [0, \infty ) For the square root function f(x) = \sqrt{x} , we cannot take the square root of a negative real number, so the domain must be 0 or greater. The range also excludes negative numbers because the square root of a positive number x is defined to be positive, even though the square of the negative number -\sqrt{x}  also gives us x. x f(x) Domain: (-\infty , \infty ) Range: (-\infty , \infty ) For the cube root function f(x) =  \sqrt{x}  the domain and range include all real numbers. Note that there is no problem taking a cube root, or any odd-integer root, of a negative number, and the resulting output is negative (it is an odd function).

**How To…**
Given the formula for a function, determine the domain and range. 1. Exclude from the domain any input values that result in division by zero. 2. Exclude from the domain any input values that have nonreal (or undefined) number outputs. 3. Use the valid input values to determine the range of the output values. 4. Look at the function graph and table values to confirm the actual function behavior.

**Example  8**

### Finding the Domain and Range Using Toolkit Functions
Find the domain and range of f (x) = 2x^{3} - x.

**Solution**
There are no restrictions on the domain, as any real number may be cubed and then subtracted from the result. The domain is (-\infty , \infty ) and the range is also (-\infty , \infty ).


**Example  9**

### Finding the Domain and Range
Find the domain and range of f (x) =  2 ____ x + 1 . Solution We cannot evaluate the function at -1 because division by zero is undefined. The domain is (-\infty , -1) ∪ (-1, \infty ). Because the function is never zero, we exclude 0 from the range. The range is (-\infty , 0) ∪ (0, \infty ).

**Example  10**

### Finding the Domain and Range
Find the domain and range of f (x) = 2\sqrt{x} + 4 . Solution We cannot take the square root of a negative number, so the value inside the radical must be nonnegative. x + 4 \ge  0 when x \ge  -4 The domain of f (x) is [-4, \infty ). We then find the range. We know that f (-4) = 0, and the function value increases as x increases without any upper limit. We conclude that the range of f is [0, \infty ). Analysis Figure 22 represents the function f .

x f f(x)

**Try It #7**
Find the domain and range of f (x) = -\sqrt{2} - x . Graphing Piecewise-Defined Functions Sometimes, we come across a function that requires more than one formula in order to obtain the given output. For example, in the toolkit functions, we introduced the absolute value function f (x) = |x|. With a domain of all real numbers and a range of values greater than or equal to 0, absolute value can be defined as the magnitude, or modulus, of a real number value regardless of sign. It is the distance from 0 on the number line. All of these definitions require the output to be greater than or equal to 0. If we input 0, or a positive value, the output is the same as the input. f (x) = x if x \ge  0 If we input a negative value, the output is the opposite of the input. f (x) = -x if x < 0 Because this requires two different processes or pieces, the absolute value function is an example of a piecewise function. A piecewise function is a function in which more than one formula is used to define the output over different pieces of the domain. We use piecewise functions to describe situations in which a rule or relationship changes as the input value crosses certain “boundaries.” For example, we often encounter situations in business for which the cost per piece of a certain item is discounted once the number ordered exceeds a certain value. Tax brackets are another real-world example of piecewise functions. For example, consider a simple tax system in which incomes up to $10,000 are taxed at 10%, and any additional income is taxed at 20%. The tax on a total income S would be 0.1S if S \le  $10,000 and $1000 + 0.2(S - $10,000)

piecewise function A piecewise function is a function in which more than one formula is used to define the output. Each formula has its own domain, and the domain of the function is the union of all these smaller domains. We notate this idea like this: f (x) = formula 1 if x is in domain 1 formula 2 if x is in domain 2 formula 3 if x is in domain 3 { In piecewise notation, the absolute value function is |x| = x if x \ge  0 -x if x < 0 {

**How To…**
Given a piecewise function, write the formula and identify the domain for each interval. 1. Identify the intervals for which different rules apply. 2. Determine formulas that describe how to calculate an output from an input in each interval. 3. Use braces and if-statements to write the function.

**Example  11**

### Writing a Piecewise Function
A museum charges $5 per person for a guided tour with a group of 1 to 9 people or a fixed $50 fee for a group of 10 or more people. Write a function relating the number of people, n, to the cost, C. Solution Two different formulas will be needed. For n-values under 10, C = 5n. For values of n that are 10 or greater, C(n) = 5n if 0 < n < 10 50 if n \ge  10 { Analysis The function is represented in Figure 23. The graph is a diagonal line from n = 0 to n = 10 and a constant after that. In this example, the two formulas agree at the meeting point where n = 10, but not all piecewise functions have this property. C(n) C(n) n

**Example  12**

### Working with a Piecewise Function
A cell phone company uses the function below to determine the cost, C, in dollars for g gigabytes of data transfer. C(g) = if 0 < g < 2 25 + 10(g - 2) if g \ge  2 { Find the cost of using 1.5 gigabytes of data and the cost of using 4 gigabytes of data. Solution To find the cost of using 1.5 gigabytes of data, C(1.5), we first look to see which part of the domain our input falls in. Because 1.5 is less than 2, we use the first formula. To find the cost of using 4 gigabytes of data, C(4), we see that our input of 4 is greater than 2, so we use the second formula. C(4) = 25 + 10(4 - 2) = $45

Analysis The function is represented in Figure 24. We can see where the function changes from a constant to a shifted and stretched identity at g = 2. We plot the graphs for the different formulas on a common set of axes, making sure each formula is applied on its proper domain. C(g) C(g) g

**How To…**
Given a piecewise function, sketch a graph. 1. Indicate on the x-axis the boundaries defined by the intervals on each piece of the domain. 2. For each piece of the domain, graph on that interval using the corresponding equation pertaining to that piece. Do not graph two functions over one interval because it would violate the criteria of a function.

**Example  13**

### Graphing a Piecewise Function
Sketch a graph of the function. f (x) = x^{2} if x \le  1 3 if 1 < x \le  2 x if x > 2 { Solution Each of the component functions is from our library of toolkit functions, so we know their shapes. We can imagine graphing each function and then limiting the graph to the indicated domain. At the endpoints of the domain, we draw open circles to indicate where the endpoint is not included because of a less-than or greater-than inequality; we draw a closed circle where the endpoint is included because of a less-than-or-equal-to or greater-than-or-equal-to inequality. (a) x f(x) (b) x f(x) (c) x f(x)

Now that we have sketched each piece individually, we combine them in the same coordinate plane. See Figure 26. x f(x) Analysis Note that the graph does pass the vertical line test even at x = 1 and x = 2 because the points (1, 3) and (2, 2) are not part of the graph of the function, though (1, 1) and (2, 3) are.

**Try It #8**
Graph the following piecewise function. f (x) = \sqrt{x}  x^{3} if x < -1 -2 if -1 < x < 4

if x > 4 {

Can more than one formula from a piecewise function be applied to a value in the domain? No. Each value corresponds to one equation in a piecewise formula. Access these online resources for additional instruction and practice with domain and range. • Domain and Range of Square Root Functions (http://openstaxcollege.org/l/domainsqroot) • Determining Domain and Range (http://openstaxcollege.org/l/determinedomain) • Find Domain and Range Given the Graph (http://openstaxcollege.org/l/drgraph) • Find Domain and Range Given a Table (http://openstaxcollege.org/l/drtable) • Find Domain and Range Given Points on a Coordinate Plane (http://openstaxcollege.org/l/drcoordinate)


## 1.2 Section Exercises

### 1.2 Section Exercises
Verbal 1. Why does the domain differ for different functions? 2. How do we determine the domain of a function defined by an equation? 3. Explain why the domain of f (x) =  \sqrt{x}  is different from the domain of f (x) = \sqrt{x} . 4. When describing sets of numbers using interval notation, when do you use a parenthesis and when do you use a bracket? 5. How do you graph a piecewise function? Algebraic For the following exercises, find the domain of each function using interval notation. 6. f (x) = -2x(x - 1)(x - 2) 7. f (x) = 5 - 2x^{2} 8. f (x) = 3\sqrt{x} - 2  9. f (x) = 3 - \sqrt{6} - 2x  10. f (x) = \sqrt{4} - 3x  11. f (x) = \sqrt{x} 2 + 4  12. f (x) =  \sqrt{1} - 2x  13. f (x) =  \sqrt{x} - 1  14. f (x) =  9 _____ x - 6  15. f (x) =  3x + 1 ______ 4x + 2  16. f (x) =  \sqrt{x} + 4  _______ x - 4  17. f (x) =  x - 3 __________

x^{2} + 9x - 22  18. f (x) =  ________ x^{2} - x - 6  19. f (x) =  2x^{3} - 250 __________

x^{2} - 2x - 15  20. f (x) =  _ \sqrt{x} - 3   21. f (x) =  2x + 1 _ \sqrt{5} - x   22. f (x) =  \sqrt{x} - 4  _ \sqrt{x} - 6   23. f (x) =  \sqrt{x} - 6  _ \sqrt{x} - 4   24. f (x) =  x __ x  25. f (x) =  x^{2} - 9x _ x^{2} - 81  26. Find the domain of the function f (x) = \sqrt{2x} 3 - 50x  by: a. using algebra. b. graphing the function in the radicand and determining intervals on the x-axis for which the radicand is nonnegative. GRAPHICAL For the following exercises, write the domain and range of each function using interval notation. x y x y x y

x y x y x y x y x y –6, – ) ( 6, ) ( ) ( 6, ) ( x y x y x y For the following exercises, sketch a graph of the piecewise function. Write the domain in interval notation. 38. f (x) = x + 1 if x < -2 -2x - 3 if x \ge  -2 { 39. f (x) = 2x - 1 if x < 1 1 + x if x \ge  1 { 40. f (x) = x + 1 if x < 0 x - 1 if x > 0 { 41. f (x) = 3 if x < 0 \sqrt{x}  if x \ge  0 { 42. f (x) = x^{2} if x < 0 1 - x if x > 0 { 43. f (x) = x^{2} if x < 0 x + 2 if x \ge  0 { 44. f (x) = x + 1 if x < 1 x^{3} if x \ge  1 { 45. f (x) = | x | if x < 2 if x \ge  2 {

Numeric For the following exercises, given each function f, evaluate f (-3), f (-2), f (-1), and f (0). 46. f (x) = x + 1 if x < -2 -2x - 3 if x \ge  -2 { 47. f (x) = 1 if x \le  -3 0 if x > -3 { 48. f (x) = -2x 2 + 3 if x \le  -1 5x - 7 if x > -1 { For the following exercises, given each function f, evaluate f (-1), f (0), f (2), and f (4). 49. f (x) = 7x + 3 if x < 0 7x + 6 if x \ge  0 { 50. f (x) = x 2 - 2 if x < 2 4 + | x - 5 | if x \ge  2 { 51. f (x) = 5x if x < 0 3 if 0 \le  x \le  3 x 2 if x > 3 { For the following exercises, write the domain for the piecewise function in interval notation. 52. f (x) = x + 1 if x < -2 -2x - 3 if x \ge  -2 { 53. f (x) = x^{2} - 2 if x < 1 -x^{2} + 2 if x > 1 { 54. f (x) = 2x - 3 if x < 0 -3x^{2} if x \ge  2 { Technology 55. Graph y =  1 __ x 2  on the viewing window [-0.5, -0.1] and [0.1, 0.5]. Determine the corresponding range for the viewing window. Show the graphs. 56. Graph y =  1 _ x  on the viewing window [-0.5, -0.1] and [0.1, 0.5]. Determine the corresponding range for the viewing window. Show the graphs. Extension 57. Suppose the range of a function f is [-5, 8]. What is the range of | f (x) |? 58. Create a function in which the range is all nonnegative real numbers. 59. Create a function in which the domain is x > 2. Real-World Applications 60. The height h of a projectile is a function of the time t it is in the air. The height in feet for t seconds is given by the function h(t) = -16t 2 + 96t. What is the domain of the function? What does the domain mean in the context of the problem? 61. The cost in dollars of making x items is given by the function C(x) = 10x + 500. a. The fixed cost is determined when zero items are produced. Find the fixed cost for this item. b. What is the cost of making 25 items? c. Suppose the maximum cost allowed is $1500. What are the domain and range of the cost function, C(x)?

Rates of Change and Behavior of Graphs Gasoline costs have experienced some wild fluctuations over the last several decades. Table 1 [5] lists the average cost, in dollars, of a gallon of gasoline for the years 2005–2012. The cost of gasoline can be considered as a function of year. y C(y) 2.31 2.62 2.84 3.30 2.41 2.84 3.58 3.68 If we were interested only in how the gasoline prices changed between 2005 and 2012, we could compute that the cost per gallon had increased from $2.31 to $3.68, an increase of $1.37. While this is interesting, it might be more useful to look at how much the price changed per year. In this section, we will investigate changes such as these. Finding the Average Rate of Change of a Function The price change per year is a rate of change because it describes how an output quantity changes relative to the change in the input quantity. We can see that the price of gasoline in Table 1 did not change by the same amount each year, so the rate of change was not constant. If we use only the beginning and ending data, we would be finding the average rate of change over the specified period of time. To find the average rate of change, we divide the change in the output value by the change in the input value.

Average rate of change =  Change in output

__

Change in input 

=  ∆y _ ∆x 

=  y^{2} - y^{1} _ x^{2} - x^{1} 

=  f (x^{2}) - f (x^{1}) __ x^{2}- x^{1}  The Greek letter ∆ (delta) signifies the change in a quantity; we read the ratio as “delta-y over delta-x” or “the change in y divided by the change in x.” Occasionally we write ∆ f instead of ∆y, which still represents the change in the function’s output value resulting from a change to its input value. It does not mean we are changing the function into some other function. In our example, the gasoline price increased by $1.37 from 2005 to 2012. Over 7 years, the average rate of change was

 ∆y _ ∆x  =  $1.37 _ 7 years  ≈ 0.196 dollars per year On average, the price of gas increased by about 19.6 each year. Other examples of rates of change include: • A population of rats increasing by 40 rats per week • A car traveling 68 miles per hour (distance traveled changes by 68 miles each hour as time passes) • A car driving 27 miles per gallon (distance traveled changes by 27 miles for each gallon) • The current through an electrical circuit increasing by 0.125 amperes for every volt of increased voltage • The amount of money in a college account decreasing by $4,000 per quarter 5 http://www.eia.gov/totalenergy/data/annual/showtext.cfm?t=ptb^{0}524. Accessed 3/5/2014. Learning Objectives
In this section, you will:
• Find the average rate of change of a function.
• Use a graph to determine where a function is increasing, decreasing, or constant.
• Use a graph to locate local maxima and local minima.
• Use a graph to locate the absolute maximum and absolute minimum.

## 1.3 Rates of Change and Behavior of Graphs
rate of change A rate of change describes how an output quantity changes relative to the change in the input quantity. The units on a rate of change are “output units per input units.” The average rate of change between two input values is the total change of the function values (output values) divided by the change in the input values.  \Delta y _ \Delta x  =  f (x^{2}) - f (x^{1}) __ x^{2} - x^{1} 

**How To…**
Given the value of a function at different points, calculate the average rate of change of a function for the interval between two values x^{1} and x^{2}. 1. Calculate the difference y^{2} - y^{1} = \Delta y. 2. Calculate the difference x^{2} - x^{1} = \Delta x. 3. Find the ratio  \Delta y _ \Delta x .

**Example  1**

### Computing an Average Rate of Change
Using the data in Table 1, find the average rate of change of the price of gasoline between 2007 and 2009. Solution In 2007, the price of gasoline was $2.84. In 2009, the cost was $2.41. The average rate of change is

 \Delta y ___ \Delta x  =  y^{2} - y^{1} _ x^{2} - x^{1} 

__

______ 2 years 

= -$0.22 per year Analysis Note that a decrease is expressed by a negative change or “negative increase.” A rate of change is negative when the output decreases as the input increases or when the output increases as the input decreases.

**Try It #1**
Using the data in Table 1 at the beginning of this section, find the average rate of change between 2005 and 2010.

**Example  2**

### Computing Average Rate of Change from a Graph
Given the function g (t) shown in Figure 1, find the average rate of change on the interval [-1, 2]. t g(t)

Solution At t = -1, Figure 2 shows g (-1) = 4. At t = 2, the graph shows g (2) = 1. t g(t) ∆g(t) = –3 ∆t = 3 The horizontal change \Delta  t = 3 is shown by the red arrow, and the vertical change \Delta  g(t) = -3 is shown by the turquoise arrow. The output changes by –3 while the input changes by 3, giving an average rate of change of  1 - 4 _______ 2 - (-1)  =  -3 ___ 3  = -1 Analysis Note that the order we choose is very important. If, for example, we use  y^{2} - y^{1} _ x^{1} - x^{2}  , we will not get the correct answer. Decide which point will be 1 and which point will be 2, and keep the coordinates fixed as ( x^{1} , y^{1} ) and ( x^{2} , y^{2} ).

**Example  3**

### Computing Average Rate of Change from a Table
After picking up a friend who lives 10 miles away, Anna records her distance from home over time. The values are shown in Table 2. Find her average speed over the first 6 hours. t (hours) D(t) (miles) Solution Here, the average speed is the average rate of change. She traveled 282 miles in 6 hours, for an average speed of

_______ 6 - 0  =  282 ___ 6 

= 47 The average speed is 47 miles per hour. Analysis Because the speed is not constant, the average speed depends on the interval chosen. For the interval [2, 3], the average speed is 63 miles per hour.

**Example  4**

### Computing Average Rate of Change for a Function Expressed as a Formula
Compute the average rate of change of f (x) = x 2 - 1 __ x  on the interval [2, 4]. Solution We can start by computing the function values at each endpoint of the interval.

f (2) = 22 -  1 __ 2  f(4) = 42 -  1 __ 4 

= 4 -  1 __ 2  = 16 -  1 __ 4 

=  7 __ 2  =  63 __ 4  Now we compute the average rate of change.

Average rate of change =  f (4) - f (2) _ 4 - 2 

=   63 __ 4  -  7 __ 2  _ 4 - 2 

=   49 __ 4 

_ 2 

=  49 __ 8 

**Try It #2**
Find the average rate of change of f (x) = x - 2\sqrt{x}  on the interval [1, 9].

**Example  5**

### Finding the Average Rate of Change of a Force
The electrostatic force F, measured in newtons, between two charged particles can be related to the distance between the particles d, in centimeters, by the formula F(d) =  2 _ d 2 . Find the average rate of change of force if the distance between the particles is increased from 2 cm to 6 cm.

**Solution**
We are computing the average rate of change of F (d) =  2 __ d 2  on the interval [2, 6].

Average rate of change =  F(6) - F(2) __ 6 - 2 

=   2 _ 62  -  2 _ 22  _ 6 - 2  Simplify.

=   2 __ 36  -  2 __ 4  _ 

=  - 16 __ 36  _ 4  Combine numerator terms.

= - 1 __ 9  Simplify. The average rate of change is - 1 __ 9  newton per centimeter.

**Example  6**
Finding an Average Rate of Change as an Expression Find the average rate of change of g(t) = t^{2} + 3t + 1 on the interval [0, a]. The answer will be an expression involving a. Solution We use the average rate of change formula.

Average rate of change =  g(a) - g(0) _ a - 0  Evaluate.

=  (a^{2} + 3a + 1) - (02 + 3(0) + 1)

___

a - 0  Simplify.

=  a^{2} + 3a + 1 - 1

_____________ a  Simplify and factor.

=  a(a + 3) _______ a  Divide by the common factor a.

= a + 3 This result tells us the average rate of change in terms of a between t = 0 and any other point t = a. For example, on the interval [0, 5], the average rate of change would be 5 + 3 = 8.


**Try It #3**
Find the average rate of change of f (x) = x^{2} + 2x - 8 on the interval [5, a]. Using a Graph to Determine Where a Function is Increasing, Decreasing, or Constant As part of exploring how functions change, we can identify intervals over which the function is changing in specific ways. We say that a function is increasing on an interval if the function values increase as the input values increase within that interval. Similarly, a function is decreasing on an interval if the function values decrease as the input values increase over that interval. The average rate of change of an increasing function is positive, and the average rate of change of a decreasing function is negative. Figure 3 shows examples of increasing and decreasing intervals on a function. x f(x) f(b) > f(a) where b > a f(b) < f(a) where b > a f(b) > f(a) where b > a Increasing Increasing Decreasing While some functions are increasing (or decreasing) over their entire domain, many others are not. A value of the input where a function changes from increasing to decreasing (as we go from left to right, that is, as the input variable increases) is called a local maximum. If a function has more than one, we say it has local maxima. Similarly, a value of the input where a function changes from decreasing to increasing as the input variable increases is called a local minimum. The plural form is “local minima.” Together, local maxima and minima are called local extrema, or local extreme values, of the function. (The singular form is “extremum.”) Often, the term local is replaced by the term relative. In this text, we will use the term local. Clearly, a function is neither increasing nor decreasing on an interval where it is constant. A function is also neither increasing nor decreasing at extrema. Note that we have to speak of local extrema, because any given local extremum as defined here is not necessarily the highest maximum or lowest minimum in the function’s entire domain. For the function whose graph is shown in Figure 4, the local maximum is 16, and it occurs at x = -2. The local minimum is -16 and it occurs at x = 2. x Local maximum = 16 occurs at x = –2 Local minimum = –16 occurs at x = 2 f(x) Decreasing Increasing Increasing

To locate the local maxima and minima from a graph, we need to observe the graph to determine where the graph attains its highest and lowest points, respectively, within an open interval. Like the summit of a roller coaster, the graph of a function is higher at a local maximum than at nearby points on both sides. The graph will also be lower at a local minimum than at neighboring points. Figure 5 illustrates these ideas for a local maximum. f(x) f(b) x a b Local maximum Increasing function Decreasing function c These observations lead us to a formal definition of local extrema. local minima and local maxima A function f is an increasing function on an open interval if f (b) > f (a) for every two input values a and b in the interval where b > a. A function f is a decreasing function on an open interval if f (b) < f (a) for every two input values a and b in the interval where b > a. A function f has a local maximum at a point b in an open interval (a, c) if f (b) \ge  f (x) for every point x (x does not equal b) in the interval. f has a local minimum at a point b in the interval (a, c) if f (b) \le  f (x) for every point x (x does not equal both) in the interval.

**Example  7**
Finding Increasing and Decreasing Intervals on a Graph Given the function p(t) in Figure 6, identify the intervals on which the function appears to be increasing. t p Solution We see that the function is not constant on any interval. The function is increasing where it slants upward as we move to the right and decreasing where it slants downward as we move to the right. The function appears to be increasing from t = 1 to t = 3 and from t = 4 on. In interval notation, we would say the function appears to be increasing on the interval (1, 3) and the interval (4, \infty ).

Analysis Notice in this example that we used open intervals (intervals that do not include the endpoints), because the function is neither increasing nor decreasing at t = 1, t = 3, and t = 4. These points are the local extrema (two minima and a maximum).

**Example  8**

### Finding Local Extrema from a Graph
Graph the function f (x) =  2 __ x  +  x __ 3 . Then use the graph to estimate the local extrema of the function and to determine the intervals on which the function is increasing. Solution Using technology, we find that the graph of the function looks like that in Figure 7. It appears there is a low point, or local minimum, between x = 2 and x = 3, and a mirror-image high point, or local maximum, somewhere between x = -3 and x = -2. x f(x) Analysis Most graphing calculators and graphing utilities can estimate the location of maxima and minima. Figure 8 provides screen images from two different technologies, showing the estimate for the local maximum and minimum. x Maximum y (b) (a) Based on these estimates, the function is increasing on the interval (-\infty , -2.449) and (2.449, \infty ). Notice that, while we expect the extrema to be symmetric, the two different technologies agree only up to four decimals due to the differing approximation algorithms used by each. (The exact location of the extrema is at \pm \sqrt{—} 6 , but determining this requires calculus.)

**Try It #4**
Graph the function f (x) = x^{3} - 6x^{2} - 15x + 20 to estimate the local extrema of the function. Use these to determine the intervals on which the function is increasing and decreasing.


**Example  9**

### Finding Local Maxima and Minima from a Graph
For the function f whose graph is shown in Figure 9, find all local maxima and minima. x y f Solution Observe the graph of f. The graph attains a local maximum at x = 1 because it is the highest point in an open interval around x = 1. The local maximum is the y-coordinate at x = 1, which is 2. The graph attains a local minimum at x = -1 because it is the lowest point in an open interval around x = -1. The local minimum is the y-coordinate at x = -1, which is -2. Analyzing the Toolkit Functions for Increasing or Decreasing Intervals We will now return to our toolkit functions and discuss their graphical behavior in Figure 10, Figure 11, and Figure 12. Function Increasing/Decreasing Example Constant Function f(x) = c Neither increasing nor decreasing y x Identity Function f(x) = x Increasing y x Quadratic Function f(x) = x^{2} Increasing on (0, \infty ) Decreasing on (-\infty , 0) Minimum at x = 0 y x

Function Increasing/Decreasing Example Cubic Function f(x) = x^{3} Increasing y x Reciprocal f(x) =  1 __ x  Decreasing (-\infty , 0) ∪ (0, \infty ) y x Reciprocal Squared f(x) =  1 _ x^{2}  Increasing on (-\infty , 0) Decreasing on (0, \infty ) y x Function Increasing/Decreasing Example Cube Root f(x) =  \sqrt{x}  Increasing y x Square Root f(x) = \sqrt{x}  Increasing on (0, \infty ) y x Absolute Value f(x) = ∣ x ∣ Increasing on (0, \infty ) Decreasing on (-\infty , 0) y x

Use A Graph to Locate the Absolute Maximum and Absolute Minimum There is a difference between locating the highest and lowest points on a graph in a region around an open interval (locally) and locating the highest and lowest points on the graph for the entire domain. The y-coordinates (output) at the highest and lowest points are called the absolute maximum and absolute minimum, respectively. To locate absolute maxima and minima from a graph, we need to observe the graph to determine where the graph attains it highest and lowest points on the domain of the function. See Figure 13. x f Absolute minimum is f (0) = -2 Absolute maximum is f (2) = 2 y Not every function has an absolute maximum or minimum value. The toolkit function f (x) = x^{3} is one such function. absolute maxima and minima The absolute maximum of f at x = c is f (c) where f (c) \ge  f (x) for all x in the domain of f. The absolute minimum of f at x = d is f (d) where f (d) \le  f (x) for all x in the domain of f.

**Example  10**
Finding Absolute Maxima and Minima from a Graph For the function f shown in Figure 14, find all absolute maxima and minima. x y f Solution Observe the graph of f. The graph attains an absolute maximum in two locations, x = -2 and x = 2, because at these locations, the graph attains its highest point on the domain of the function. The absolute maximum is the y-coordinate at x = -2 and x = 2, which is 16. The graph attains an absolute minimum at x = 3, because it is the lowest point on the domain of the function’s graph. The absolute minimum is the y-coordinate at x = 3, which is -10. > Access this online resource for additional instruction and practice with rates of change. • Average Rate of Change (http://openstaxcollege.org/l/aroc)


### 1.3 Section Exercises
Verbal 1. Can the average rate of change of a function be constant? 2. If a function f is increasing on (a, b) and decreasing on (b, c), then what can be said about the local extremum of f on (a, c)? 3. How are the absolute maximum and minimum similar to and different from the local extrema? 4. How does the graph of the absolute value function compare to the graph of the quadratic function, y = x 2, in terms of increasing and decreasing intervals? Algebraic For the following exercises, find the average rate of change of each function on the interval specified for real numbers b or h. 5. f (x) = 4x 2 - 7 on [1, b] 6. g (x) = 2x 2 - 9 on [4, b] 7. p(x) = 3x + 4 on [2, 2 + h] 8. k(x) = 4x - 2 on [3, 3 + h] 9. f (x) = 2x 2 + 1 on [x, x + h] 10. g(x) = 3x 2 - 2 on [x, x + h] 11. a(t) =  1 ____ t + 4  on [9, 9 + h] 12. b(x) =  1 _____ x + 3  on [1, 1 + h] 13. j(x) = 3x 3 on [1, 1 + h] 14. r(t) = 4t 3 on [2, 2 + h] 15.  f (x + h) - f(x)

__ h  given f(x) = 2x^{2} - 3x on [x, x + h] Graphical For the following exercises, consider the graph of f shown in Figure 15.

16. Estimate the average rate of change from x = 1 to x = 4.

17. Estimate the average rate of change from x = 2 to x = 5.

For the following exercises, use the graph of each function to estimate the intervals on which the function is increasing or decreasing. x y x y x y x y


## 1.3 Section Exercises
x y For the following exercises, consider the graph shown in Figure 16. 22. Estimate the intervals where the function is increasing or decreasing. 23. Estimate the point(s) at which the graph of f has a local maximum or a local minimum. x y For the following exercises, consider the graph in Figure 17. 24. If the complete graph of the function is shown, estimate the intervals where the function is increasing or decreasing. 25. If the complete graph of the function is shown, estimate the absolute maximum and absolute minimum. x y Numeric 26. Table 3 gives the annual sales (in millions of dollars) of a product from 1998 to 2006. What was the average rate of change of annual sales (a) between 2001 and 2002, and (b) between 2001 and 2004? Year Sales (millions of dollars) 27. Table 4 gives the population of a town (in thousands) from 2000 to 2008. What was the average rate of change of population (a) between 2002 and 2004, and (b) between 2002 and 2006? Year Population (thousands)

For the following exercises, find the average rate of change of each function on the interval specified. 28. f (x) = x 2 on [1, 5] 29. h(x) = 5 - 2x 2 on [-2, 4] 30. q(x) = x^{3} on [-4, 2] 31. g (x) = 3x 3 - 1 on [-3, 3] _ x  on [1, 3] 33. p(t) =  (t 2 - 4)(t + 1)

____________ t 2 + 3  on [-3, 1] 34. k (t) = 6t^{2} +  4 __ t^{3}  on [-1, 3] Technology For the following exercises, use a graphing utility to estimate the local extrema of each function and to estimate the intervals on which the function is increasing and decreasing. 35. f(x) = x 4 - 4x 3 + 5 36. h(x) = x 5 + 5x 4 + 10x 3 + 10x 2 - 1 37. g(t) = t\sqrt{t} + 3  38. k(t) = 3t  2 _ 3  - t 39. m(x) = x 4 + 2x 3 - 12x 2 - 10x + 4 40. n(x) = x 4 - 8x 3 + 18x 2 - 6x + 2 Extension 41. The graph of the function f is shown in Figure 18. Maximum

Based on the calculator screen shot, the point (1.333, 5.185) is which of the following? a. a relative (local) maximum of the function b. the vertex of the function c. the absolute maximum of the function d. a zero of the function 42. Let f (x) =  1 __ x . Find a number c such that the average rate of change of the function f on the interval (1, c) is - 1 __ 4  43. Let f(x) =  1 __ x . Find the number b such that the average rate of change of f on the interval (2, b) is - 1 __ 10 . Real-World Applications 44. At the start of a trip, the odometer on a car read 21,395. At the end of the trip, 13.5 hours later, the odometer read 22,125. Assume the scale on the odometer is in miles. What is the average speed the car traveled during this trip? 45. A driver of a car stopped at a gas station to fill up his gas tank. He looked at his watch, and the time read exactly 3:40 p.m. At this time, he started pumping gas into the tank. At exactly 3:44, the tank was full and he noticed that he had pumped 10.7 gallons. What is the average rate of flow of the gasoline into the gas tank? 46. Near the surface of the moon, the distance that an object falls is a function of time. It is given by d(t) = 2.6667t^{2}, where t is in seconds and d(t) is in feet. If an object is dropped from a certain height, find the average velocity of the object from t = 1 to t = 2. 47. The graph in Figure 19 illustrates the decay of a radioactive substance over t days. t A Time (days) Amount (milligrams) Use the graph to estimate the average decay rate from t = 5 to t = 15.


## 1.4 Composition of Functions
Suppose we want to calculate how much it costs to heat a house on a particular day of the year. The cost to heat a house will depend on the average daily temperature, and in turn, the average daily temperature depends on the particular day of the year. Notice how we have just defined two relationships: The cost depends on the temperature, and the temperature depends on the day. Using descriptive variables, we can notate these two functions. The function C(T) gives the cost C of heating a house for a given average daily temperature in T degrees Celsius. The function T(d) gives the average daily temperature on day d of the year. For any given day, Cost = C(T(d)) means that the cost depends on the temperature, which in turns depends on the day of the year. Thus, we can evaluate the cost function at the temperature T(d). For example, we could evaluate T(5) to determine the average daily temperature on the 5th day of the year. Then, we could evaluate the cost function at that temperature. We would write C(T(5)). Cost for the temperature Temperature on day 5 C(T(5)) By combining these two relationships into one function, we have performed function composition, which is the focus of this section. Combining Functions Using Algebraic Operations Function composition is only one way to combine existing functions. Another way is to carry out the usual algebraic operations on functions, such as addition, subtraction, multiplication and division. We do this by performing the operations with the function outputs, defining the result as the output of our new function. Suppose we need to add two columns of numbers that represent a husband and wife’s separate annual incomes over a period of years, with the result being their total household income. We want to do this for every year, adding only that year’s incomes and then collecting all the data in a new column. If w(y) is the wife’s income and h(y) is the husband’s income in year y, and we want T to represent the total income, then we can define a new function. T(y) = h(y) + w(y) If this holds true for every year, then we can focus on the relation between the functions without reference to a year and write T = h + w Just as for this sum of two functions, we can define difference, product, and ratio functions for any pair of functions that have the same kinds of inputs (not necessarily numbers) and also the same kinds of outputs (which do have to be numbers so that the usual operations of algebra can apply to them, and which also must have the same units or no units when we add and subtract). In this way, we can think of adding, subtracting, multiplying, and dividing functions. Learning Objectives
In this section, you will:
• Combine functions using algebraic operations.
• Create a new function by composition of functions.
• Evaluate composite functions.
• Find the domain of a composite function.
• Decompose a composite function into its component functions.
For two functions f (x) and g(x) with real number outputs, we define new functions f + g, f - g, fg, and  f _ g  by the relations

(f + g)(x) = f (x) + g(x)

(f - g)(x) = f (x) - g(x)

(fg)(x) = f (x)g(x)

  f _ g  (x) =  f (x) _ g(x) 

**Example  1**

### Performing Algebraic Operations on Functions
Find and simplify the functions (g - f)(x) and   g _ f  (x), given f (x) = x - 1 and g(x) = x 2 - 1. Are they the same function? Solution Begin by writing the general form, and then substitute the given functions.

(g - f )(x) = g(x) - f (x)

(g - f )(x) = x 2 - 1 - (x - 1)

(g - f )(x) = x 2 - x

(g - f )(x) = x(x - 1)

  g _ f  (x) =  g(x) _ f (x) 

  g _ f  (x) =  x^{2} - 1 _ x - 1  where x \neq  1

  g _ f  (x) =  (x + 1)(x - 1)

____________ x - 1  where x \neq  1

  g _ f  (x) = x + 1 where x \neq  1 No, the functions are not the same. Note: For   g _ f  (x), the condition x \neq  1 is necessary because when x = 1, the denominator is equal to 0, which makes the function undefined.

**Try It #1**
Find and simplify the functions (fg)(x) and (f - g)(x). f (x) = x - 1 and g(x) = x 2 - 1 Are they the same function? Create a Function by Composition of Functions Performing algebraic operations on functions combines them into a new function, but we can also create functions by composing functions. When we wanted to compute a heating cost from a day of the year, we created a new function that takes a day as input and yields a cost as output. The process of combining functions so that the output of one function becomes the input of another is known as a composition of functions. The resulting function is known as a composite function. We represent this combination by the following notation: ( f ∘ g)(x) = f (g(x))

We read the left-hand side as “f composed with g at x,” and the right-hand side as “f of g of x.” The two sides of the equation have the same mathematical meaning and are equal. The open circle symbol ∘ is called the composition operator. We use this operator mainly when we wish to emphasize the relationship between the functions themselves without referring to any particular input value. Composition is a binary operation that takes two functions and forms a new function, much as addition or multiplication takes two numbers and gives a new number. However, it is important not to confuse function composition with multiplication because, as we learned above, in most cases f (g(x)) \neq  f (x)g(x). It is also important to understand the order of operations in evaluating a composite function. We follow the usual convention with parentheses by starting with the innermost parentheses first, and then working to the outside. In the equation above, the function g takes the input x first and yields an output g(x). Then the function f takes g(x) as an input and yields an output f (g(x)). x is the input of g g(x), the output of g is the input of f (f ° g)(x) = f(g(x)) In general, f ∘ g and g ∘ f are different functions. In other words, in many cases f ( g(x)) \neq  g(f (x)) for all x. We will also see that sometimes two functions can be composed only in one specific order. For example, if f (x) = x^{2} and g(x) = x + 2, then

f (g(x)) = f (x + 2)

= (x + 2)^{2}

= x^{2} + 4x + 4 but

g(f (x)) = g(x^{2})

= x^{2} + 2 These expressions are not equal for all values of x, so the two functions are not equal. It is irrelevant that the expressions happen to be equal for the single input value x = - 1 _ 2 . Note that the range of the inside function (the first function to be evaluated) needs to be within the domain of the outside function. Less formally, the composition has to make sense in terms of inputs and outputs. composition of functions When the output of one function is used as the input of another, we call the entire operation a composition of functions. For any input x and functions f and g, this action defines a composite function, which we write as f ∘ g such that (f ∘ g)(x) = f (g(x)) The domain of the composite function f ∘ g is all x such that x is in the domain of g and g(x) is in the domain of f. It is important to realize that the product of functions fg is not the same as the function composition f (g(x)), because, in general, f (x)g(x) \neq  f (g(x)).

**Example  2**
Determining whether Composition of Functions is Commutative Using the functions provided, find f (g(x)) and g(f (x)). Determine whether the composition of the functions is commutative. f (x) = 2x + 1 g(x) = 3 - x

Solution Let’s begin by substituting g(x) into f (x).

f (g(x)) = 2(3 - x) + 1

= 6 - 2x + 1

= 7 - 2x Now we can substitute f (x) into g(x).

g(f (x)) = 3 - (2x + 1)

= 3 - 2x - 1

= - 2x + 2 We find that g(f (x)) \neq  f (g(x)), so the operation of function composition is not commutative.

**Example  3**

### Interpreting Composite Functions
The function c(s) gives the number of calories burned completing s sit-ups, and s(t) gives the number of sit-ups a person can complete in t minutes. Interpret c(s(3)). Solution The inside expression in the composition is s(3). Because the input to the s-function is time, t = 3 represents 3 minutes, and s(3) is the number of sit-ups completed in 3 minutes. Using s(3) as the input to the function c(s) gives us the number of calories burned during the number of sit-ups that can be completed in 3 minutes, or simply the number of calories burned in 3 minutes (by doing sit-ups).

**Example  4**

### Investigating the Order of Function Composition
Suppose f (x) gives miles that can be driven in x hours and g(y) gives the gallons of gas used in driving y miles. Which of these expressions is meaningful: f (g(y)) or g(f (x))? Solution The function y = f (x) is a function whose output is the number of miles driven corresponding to the number of hours driven. number of miles = f (number of hours) The function g(y) is a function whose output is the number of gallons used corresponding to the number of miles driven. This means: number of gallons = g (number of miles) The expression g(y) takes miles as the input and a number of gallons as the output. The function f (x) requires a number of hours as the input. Trying to input a number of gallons does not make sense. The expression f (g(y)) is meaningless. The expression f (x) takes hours as input and a number of miles driven as the output. The function g(y) requires a number of miles as the input. Using f (x) (miles driven) as an input value for g(y), where gallons of gas depends on miles driven, does make sense. The expression g(f (x)) makes sense, and will yield the number of gallons of gas used, g, driving a certain number of miles, f (x), in x hours. Are there any situations where f (g(y)) and g(f (x)) would both be meaningful or useful expressions ? Yes. For many pure mathematical functions, both compositions make sense, even though they usually produce different new functions. In real-world problems, functions whose inputs and outputs have the same units also may give compositions that are meaningful in either order.

**Try It #2**
The gravitational force on a planet a distance r from the sun is given by the function G(r). The acceleration of a planet subjected to any force F is given by the function a(F). Form a meaningful composition of these two functions, and explain what it means.


### Evaluating Composite Functions
Once we compose a new function from two existing functions, we need to be able to evaluate it for any input in its domain. We will do this with specific numerical inputs for functions expressed as tables, graphs, and formulas and with variables as inputs to functions expressed as formulas. In each case, we evaluate the inner function using the starting input and then use the inner function’s output as the input for the outer function. Evaluating Composite Functions Using Tables When working with functions given as tables, we read input and output values from the table entries and always work from the inside to the outside. We evaluate the inside function first and then use the output of the inside function as the input to the outside function.

**Example  5**
Using a Table to Evaluate a Composite Function Using Table 1, evaluate f (g(3)) and g(f (3)). x f (x) g(x) Solution To evaluate f (g(3)), we start from the inside with the input value 3. We then evaluate the inside expression g(3) using the table that defines the function g: g(3) = 2. We can then use that result as the input to the function f, so g(3) is replaced by 2 and we get f (2). Then, using the table that defines the function f, we find that f (2) = 8.

g(3) = 2 f (g(3)) = f (2) = 8 To evaluate g(f (3)), we first evaluate the inside expression f (3) using the first table: f (3) = 3. Then, using the table for g, we can evaluate g(f (3)) = g(3) = 2 x g(x) f (g(x)) f (x) g(f (x))

**Try It #3**
Using Table 1, evaluate f (g(1)) and g(f (4)). Evaluating Composite Functions Using Graphs When we are given individual functions as graphs, the procedure for evaluating composite functions is similar to the process we use for evaluating tables. We read the input and output values, but this time, from the x- and y-axes of the graphs.


**How To…**
Given a composite function and graphs of its individual functions, evaluate it using the information provided by the graphs. 1. Locate the given input to the inner function on the x-axis of its graph. 2. Read off the output of the inner function from the y-axis of its graph. 3. Locate the inner function output on the x-axis of the graph of the outer function. 4. Read the output of the outer function from the y-axis of its graph. This is the output of the composite function.

**Example  6**
Using a Graph to Evaluate a Composite Function Using Figure 1, evaluate f (g(1)). x g(x) (a) x f(x) (b) Solution To evaluate f (g(1)), we start with the inside evaluation. See Figure 2. x g(x) x f (x) g(1) = 3 f (3) = 6 We evaluate g(1) using the graph of g(x), finding the input of 1 on the x-axis and finding the output value of the graph at that input. Here, g(1) = 3. We use this value as the input to the function f. f (g(1)) = f (3) We can then evaluate the composite function by looking to the graph of f (x), finding the input of 3 on the x-axis and reading the output value of the graph at this input. Here, f (3) = 6, so f ( g(1)) = 6.


**Analysis**
x g(x) x f(x)

**Try It #4**
Using Figure 1, evaluate g(f (2)). Evaluating Composite Functions Using Formulas When evaluating a composite function where we have either created or been given formulas, the rule of working from the inside out remains the same. The input value to the outer function will be the output of the inner function, which may be a numerical value, a variable name, or a more complicated expression. While we can compose the functions for each individual input value, it is sometimes helpful to find a single formula that will calculate the result of a composition f ( g(x)). To do this, we will extend our idea of function evaluation. Recall that, when we evaluate a function like f (t) = t^{2} - t, we substitute the value inside the parentheses into the formula wherever we see the input variable.

**How To…**
Given a formula for a composite function, evaluate the function. 1. Evaluate the inside function using the input value or variable provided. 2. Use the resulting output as the input to the outside function.

**Example  7**
Evaluating a Composition of Functions Expressed as Formulas with a Numerical Input Given f (t) = t^{2} - t and h(x) = 3x + 2, evaluate f (h(1)). Solution Because the inside expression is h(1), we start by evaluating h(x) at 1.

h(1) = 3(1) + 2

h(1) = 5 Then f (h(1)) = f (5), so we evaluate f (t) at an input of 5.

f (h(1)) = f (5)

f (h(1)) = 52 - 5

f (h(1)) = 20 Analysis It makes no difference what the input variables t and x were called in this problem because we evaluated for specific numerical values.


**Try It #5**
Given f (t) = t 2 - t and h(x) = 3x + 2, evaluate a. h(f (2)) b. h(f (-2)) Finding the Domain of a Composite Function As we discussed previously, the domain of a composite function such as f ∘ g is dependent on the domain of g and the domain of f. It is important to know when we can apply a composite function and when we cannot, that is, to know the domain of a function such as f ∘ g. Let us assume we know the domains of the functions f and g separately. If we write the composite function for an input x as f (g(x)), we can see right away that x must be a member of the domain of g in order for the expression to be meaningful, because otherwise we cannot complete the inner function evaluation. However, we also see that g(x) must be a member of the domain of f, otherwise the second function evaluation in f (g(x)) cannot be completed, and the expression is still undefined. Thus the domain of f ∘ g consists of only those inputs in the domain of g that produce outputs from g belonging to the domain of f. Note that the domain of f composed with g is the set of all x such that x is in the domain of g and g(x) is in the domain of f. domain of a composite function The domain of a composite function f (g(x)) is the set of those inputs x in the domain of g for which g(x) is in the domain of f.

**How To…**
Given a function composition f (g(x)), determine its domain. 1. Find the domain of g. 2. Find the domain of f. 3. Find those inputs x in the domain of g for which g(x) is in the domain of f. That is, exclude those inputs x from the domain of g for which g(x) is not in the domain of f. The resulting set is the domain of f ∘ g.

**Example  8**

### Finding the Domain of a Composite Function
Find the domain of (f ∘ g)(x) where f (x) =  5 ____ x - 1  and g(x) =  _____ 3x - 2  Solution The domain of g(x) consists of all real numbers except x =  2 __ 3 , since that input value would cause us to divide by 0. Likewise, the domain of f consists of all real numbers except 1. So we need to exclude from the domain of g(x) that value of x for which g(x) = 1.

 _____ 3x - 2  = 1

4 = 3x - 2

6 = 3x

x = 2 So the domain of f ∘ g is the set of all real numbers except  2 __ 3  and 2. This means that x \neq   2 __ 3  or x \neq  2 We can write this in interval notation as  - \infty ,  2 __ 3   ∪   2 __ 3 , 2  ∪ (2, \infty )

Finding the Domain of a Composite Function Involving Radicals Find the domain of (f ∘ g)(x) where f (x) = \sqrt{x} + 2  and g(x) = \sqrt{3} - x  Solution Because we cannot take the square root of a negative number, the domain of g is (-\infty , 3]. Now we check the domain of the composite function (f ∘ g)(x) = \sqrt{___________} \sqrt{3} - x +2  For (f ∘ g)(x) = \sqrt{___________} \sqrt{3} - x +2  , \sqrt{3} - x +2 \ge  0, since the radicand of a square root must be positive. Since the square roots are positive, \sqrt{3} - x  \ge  0, 3 - x \ge  0, which gives a domain of (-\infty , 3]. Analysis This example shows that knowledge of the range of functions (specifically the inner function) can also be helpful in finding the domain of a composite function. It also shows that the domain of f ∘ g can contain values that are not in the domain of f, though they must be in the domain of g.

**Try It #6**
Find the domain of (f ∘ g)(x) where f (x) =  1 ____ x - 2  and g(x) = \sqrt{x} + 4  Decomposing a Composite Function into its Component Functions In some cases, it is necessary to decompose a complicated function. In other words, we can write it as a composition of two simpler functions. There may be more than one way to decompose a composite function, so we may choose the decomposition that appears to be most expedient.

**Example  9**

### Decomposing a Function
Write f (x) = \sqrt{5} - x 2  as the composition of two functions. Solution We are looking for two functions, g and h, so f (x) = g(h(x)). To do this, we look for a function inside a function in the formula for f (x). As one possibility, we might notice that the expression 5 - x^{2} is the inside of the square root. We could then decompose the function as h(x) = 5 - x^{2} and g(x) = \sqrt{x}  We can check our answer by recomposing the functions. g(h(x)) = g(5 - x^{2}) = \sqrt{5} - x^{2} 

**Try It #7**
Write f (x) =  __

3 - \sqrt{4} + x^{2}   as the composition of two functions. Access these online resources for additional instruction and practice with composite functions. • Composite Functions (http://openstaxcollege.org/l/compfunction) • Composite Function Notation Application (http://openstaxcollege.org/l/compfuncnot) • Composite Functions Using Graphs (http://openstaxcollege.org/l/compfuncgraph) • Decompose Functions (http://openstaxcollege.org/l/decompfunction) • Composite Function Values (http://openstaxcollege.org/l/compfuncvalue)


### 1.4 section EXERCISES
Verbal 1. How does one find the domain of the quotient of two functions,  f _ g ? 2. What is the composition of two functions, f ∘ g ? 3. If the order is reversed when composing two functions, can the result ever be the same as the answer in the original order of the composition ? If yes, give an example. If no, explain why not. 4. How do you find the domain for the composition of two functions, f ∘ g ? Algebraic 5. Given f (x) = x 2 + 2x and g(x) = 6 - x 2, find f + g, f - g, fg, and  f _ g . Determine the domain for each function in interval notation. 6. Given f (x) = -3x^{2} + x and g(x) = 5, find f + g, f - g, fg, and  f _ g . Determine the domain for each function in interval notation. 7. Given f (x) = 2x 2 + 4x and g(x) =  1 _ 2x , find f + g, f - g, fg, and  f _ g . Determine the domain for each function in interval notation. 8. Given f (x) =  _ x - 4 and g(x) =  1 _ 6 - x , find f + g, f - g, fg, and  f _ g . Determine the domain for each function in interval notation. 9. Given f (x) = 3x 2 and g(x) = \sqrt{x} - 5 , find f + g, f - g, fg, and  f _ g . Determine the domain for each function in interval notation. 10. Given f (x) = \sqrt{x}  and g(x) = |x - 3|, find  g _ f . Determine the domain for each function in interval notation. 11. Given f (x) = 2x 2 + 1 and g(x) = 3x - 5, find the following: a. f ( g(2)) b. f ( g(x)) c. g( f (x)) d. ( g ∘ g)(x) e. ( f ∘ f )(-2) For the following exercises, use each pair of functions to find f (g(x)) and g(f (x)). Simplify your answers. 12. f (x) = x 2 + 1, g(x) = \sqrt{x} + 2  13. f (x) = \sqrt{x}  + 2, g(x) = x 2 + 3 14. f (x) = |x|, g(x) = 5x + 1 15. f (x) =  \sqrt{x} , g(x) =  x + 1 _ x^{3}  16. f (x) =  1 _ x - 6 , g(x) =  7 _ x  + 6 17. f (x) =  1 ___ x-4 , g(x) =  2 _ x  + 4 For the following exercises, use each set of functions to find f (g(h(x))). Simplify your answers. 18. f (x) = x  4 + 6, g(x) = x - 6, and h(x) = \sqrt{x}  19. f (x) = x 2 + 1, g(x) =  1 _ x  , and h(x) = x + 3 20. Given f (x) =  1 _ x , and g(x) = x - 3, find the following: a. ( f ∘ g)(x) b. the domain of ( f ∘ g)(x) in interval notation c. ( g ∘ f )(x) d. the domain of ( g ∘ f )(x) e.   f _ g  x 21. Given f (x) = \sqrt{2} - 4x  and g(x) = - 3 _ x , find the following: a. ( g ∘ f )(x) b. the domain of ( g ∘ f )(x) in interval notation


## 1.4 Section Exercises
22. Given the functions f (x) =  1 - x _ x  and g(x) =  _ 1 + x^{2} , find the following: a. ( g ∘ f )(x) b. ( g ∘ f )(2) 23. Given functions p(x) =  1 _ \sqrt{x}   and m(x) = x 2 - 4, state the domain of each of the following functions using interval notation: a.  p(x) _ m(x)  b. p(m(x)) c. m(p(x)) 24. Given functions q(x) =  1 _ \sqrt{x}   and h(x) = x 2 - 9, state the domain of each of the following functions using interval notation. a.  q(x) _ h(x)  b. q(h(x)) c. h(q(x)) 25. For f (x) =  1 _ x  and g(x) = \sqrt{x} - 1 , write the domain of ( f ∘ g)(x) in interval notation. For the following exercises, find functions f (x) and g(x) so the given function can be expressed as h(x) = f (g(x)). 26. h(x) = (x + 2)^{2} 27. h(x) = (x - 5)^{3} 28. h(x) =  3 _ x - 5  29. h(x) =  _______ (x + 2)^{2}  30. h(x) = 4 +  \sqrt{x}  31. h(x) = \sqrt{_______}  ______ 2x - 3   32. h(x) =  _ (3x 2 - 4)-3  33. h(x) = \sqrt{_______}  3x - 2 ______ x + 5   34. h(x) =   8 + x 3 _ 8 - x 3   35. h(x) = \sqrt{2x} + 6  36. h(x) = (5x - 1)^{3} 37. h(x) =  \sqrt{x} - 1  38. h(x) = |x 2 + 7| 39. h(x) =  _ (x - 2)^{3}  40. h(x) =   _ 2x - 3   41. h(x) = \sqrt{_______}  2x - 1 _ 3x + 4   Graphical For the following exercises, use the graphs of f, shown in Figure 4, and g, shown in Figure 5, to evaluate the expressions. f(x) x f f(x) x g 42. f ( g(3)) 43. f ( g(1)) 44. g( f (1)) 45. g( f (0)) 46. f ( f (5)) 47. f ( f (4)) 48. g( g(2)) 49. g( g(0))

For the following exercises, use graphs of f (x), shown in Figure 6, g(x), shown in Figure 7, and h(x), shown in Figure 8, to evaluate the expressions. f(x) x f(x) g(x) x f(x) h(x) x f(x) 50. g( f (1)) 51. g( f (2)) 52. f ( g(4)) 53. f ( g(1)) 54. f (h(2)) 55. h( f (2)) 56. f ( g(h(4))) 57. f ( g( f (-2))) Numeric For the following exercises, use the function values for f and g shown in Table 3 to evaluate each expression. x f (x) g(x) 58. f ( g(8)) 59. f ( g(5)) 60. g( f (5)) 61. g( f (3)) 62. f ( f (4)) 63. f ( f (1)) 64. g( g(2)) 65. g( g(6)) For the following exercises, use the function values for f and g shown in Table 4 to evaluate the expressions. x -3 -2 -1 f (x) -1 g(x) -8 -3 -3 -8 66. ( f ∘ g)(1) 67. ( f ∘ g)(2) 68. ( g ∘ f )(2) 69. ( g ∘ f )(3) 70. ( g ∘ g )(1) 71. ( f ∘ f )(3) For the following exercises, use each pair of functions to find f (g(0)) and g(f (0)). 72. f (x) = 4x + 8, g(x) = 7 - x^{2} 73. f (x) = 5x + 7, g(x) = 4 - 2x^{2} 74. f (x) = \sqrt{x} + 4 , g(x) = 12 - x^{3} 75. f (x) =  1 _ x + 2 , g(x) = 4x + 3 For the following exercises, use the functions f (x) = 2x^{2} + 1 and g(x) = 3x + 5 to evaluate or find the composite function as indicated. 76. f ( g(2)) 77. f ( g(x)) 78. g( f ( - 3)) 79. ( g ∘ g )(x)

Extensions For the following exercises, use f (x) = x^{3} + 1 and g(x) =  \sqrt{x} - 1 . 80. Find ( f ∘ g)(x) and ( g ∘ f )(x). Compare the two answers. 81. Find ( f ∘ g)(2) and ( g ∘ f )(2). 82. What is the domain of ( g ∘ f )(x) ? 83. What is the domain of ( f ∘ g)(x) ? 84. Let f (x) =  1 __ x . a. Find ( f ∘ f )(x). b. Is ( f ∘ f )(x) for any function f the same result as the answer to part (a) for any function ? Explain. For the following exercises, let F (x) = (x + 1)^{5}, f (x) = x^{5}, and g(x) = x + 1. 85. True or False: ( g ∘ f )(x) = F (x). 86. True or False: ( f ∘ g )(x) = F (x). For the following exercises, find the composition when f (x) = x^{2} + 2 for all x \ge  0 and g(x) = \sqrt{x} - 2 . 87. ( f ∘ g)(6) ; ( g ∘ f )(6) 88. ( g ∘ f )(a) ; ( f ∘ g )(a) 89. ( f ∘ g )(11) ; (g ∘ f )(11) Real-World Applications 90. The function D(p) gives the number of items that will be demanded when the price is p. The production cost C(x) is the cost of producing x items. To determine the cost of production when the price is $6, you would do which of the following ? a. Evaluate D(C(6)). b. Evaluate C(D(6)). c. Solve D(C(x)) = 6. d. Solve C(D(p)) = 6. 91. The function A(d) gives the pain level on a scale of 0 to 10 experienced by a patient with d milligrams of a pain- reducing drug in her system. The milligrams of the drug in the patient’s system after t minutes is modeled by m(t). Which of the following would you do in order to determine when the patient will be at a pain level of 4 ? a. Evaluate A(m(4)). b. Evaluate m(A(4)). c. Solve A(m(t)) = 4. d. Solve m(A(d)) = 4. 92. A store offers customers a 30 % discount on the price x of selected items. Then, the store takes off an additional 15 % at the cash register. Write a price function P(x) that computes the final price of the item in terms of the original price x. (Hint: Use function composition to find your answer.) 93. A rain drop hitting a lake makes a circular ripple. If the radius, in inches, grows as a function of time in minutes according to r(t) = 25 

\sqrt{t} + 2 , find the area of the ripple as a function of time. Find the area of the ripple at t = 2. 94. A forest fire leaves behind an area of grass burned in an expanding circular pattern. If the radius of the circle of burning grass is increasing with time according to the formula r(t) = 2t + 1, express the area burned as a function of time, t (minutes). 95. Use the function you found in the previous exercise to find the total area burned after 5 minutes. 96. The radius r, in inches, of a spherical balloon is related to the volume, V, by r(V) = 3\sqrt{___}

 3V ___ 4\pi   . Air is pumped into the balloon, so the volume after t seconds is given by V(t) = 10 + 20t. a. Find the composite function r(V(t)). b. Find the exact time when the radius reaches 10 inches. 97. The number of bacteria in a refrigerated food product is given by N(T) = 23T 2 - 56T + 1, 3 < T < 33, where T is the temperature of the food. When the food is removed from the refrigerator, the temperature is given by T(t) = 5t + 1.5, where t is the time in hours. a. Find the composite function N(T(t)). b. Find the time (round to two decimal places) when the bacteria count reaches 6,752.

1. 5 Transformation of Functions We all know that a flat mirror enables us to see an accurate image of ourselves and whatever is behind us. When we tilt the mirror, the images we see may shift horizontally or vertically. But what happens when we bend a flexible mirror? Like a carnival funhouse mirror, it presents us with a distorted image of ourselves, stretched or compressed horizontally or vertically. In a similar way, we can distort or transform mathematical functions to better adapt them to describing objects or processes in the real world. In this section, we will take a look at several kinds of transformations. Graphing Functions Using Vertical and Horizontal Shifts Often when given a problem, we try to model the scenario using mathematics in the form of words, tables, graphs, and equations. One method we can employ is to adapt the basic graphs of the toolkit functions to build new models for a given scenario. There are systematic ways to alter functions to construct appropriate models for the problems we are trying to solve. Identifying Vertical Shifts One simple kind of transformation involves shifting the entire graph of a function up, down, right, or left. The simplest shift is a vertical shift, moving the graph up or down, because this transformation involves adding a positive or negative constant to the function. In other words, we add the same constant to the output value of the function regardless of the input. For a function g (x) = f (x) + k, the function f (x) is shifted vertically k units. See Figure 2 for an example. Learning Objectives
In this section, you will:
• Graph functions using vertical and horizontal shifts.
• Graph functions using reflections about the x-axis and the y-axis.
• Determine whether a function is even, odd, or neither from its graph.
• Graph functions using compressions and stretches.
• Combine transformations.

## 1.5 Transformation of Functions
x f(x)+1 f(x) f(x) \sqrt{—} x . To help you visualize the concept of a vertical shift, consider that y = f (x). Therefore, f (x) + k is equivalent to y + k. Every unit of y is replaced by y + k, so the y-value increases or decreases depending on the value of k. The result is a shift upward or downward. vertical shift Given a function f (x), a new function g(x) = f (x) + k, where k is a constant, is a vertical shift of the function f (x). All the output values change by k units. If k is positive, the graph will shift up. If k is negative, the graph will shift down.


**Example  1**

### Adding a Constant to a Function
To regulate temperature in a green building, airflow vents near the roof open and close throughout the day. Figure 3 shows the area of open vents V (in square feet) throughout the day in hours after midnight, t. During the summer, the facilities manager decides to try to better regulate temperature by increasing the amount of open vents by 20 square feet throughout the day and night. Sketch a graph of this new function. t V Solution We can sketch a graph of this new function by adding 20 to each of the output values of the original function. This will have the effect of shifting the graph vertically up, as shown in Figure 4. t V Up 20

Notice that in Figure 4, for each input value, the output value has increased by 20, so if we call the new function S(t), we could write S(t) = V(t) + 20 This notation tells us that, for any value of t, S(t) can be found by evaluating the function V at the same input and then adding 20 to the result. This defines S as a transformation of the function V, in this case a vertical shift up 20 units. Notice that, with a vertical shift, the input values stay the same and only the output values change. See Table 1. t V(t) S(t)

**How To…**
Given a tabular function, create a new row to represent a vertical shift. 1. Identify the output row or column. 2. Determine the magnitude of the shift. 3. Add the shift to the value in each output cell. Add a positive value for up or a negative value for down.

**Example  2**

### Shifting a Tabular Function Vertically
A function f (x) is given in Table 2. Create a table for the function g(x) = f (x) - 3. x f (x) Solution The formula g (x) = f (x) - 3 tells us that we can find the output values of g by subtracting 3 from the output values of f. For example:

f (2) = 1 Given

g(x) = f (x) - 3 Given transformation

g(2) = f (2) - 3

= 1 - 3

= -2 Subtracting 3 from each f (x) value, we can complete a table of values for g(x) as shown in Table 3. x f (x) g(x) -2 Analysis As with the earlier vertical shift, notice the input values stay the same and only the output values change.

**Try It #1**
The function h(t) = –4.9t^{2} + 30t gives the height h of a ball (in meters) thrown upward from the ground after t seconds. Suppose the ball was instead thrown from the top of a 10-m building. Relate this new height function b(t) to h(t), and then find a formula for b(t).


### Identifying Horizontal Shifts
We just saw that the vertical shift is a change to the output, or outside, of the function. We will now look at how changes to input, on the inside of the function, change its graph and meaning. A shift to the input results in a movement of the graph of the function left or right in what is known as a horizontal shift, shown in Figure 5. x f(x+1) f(x) f(x)

\sqrt{x} . Note that h = +1 shifts the graph to the left, that is, towards negative values of x. For example, if f (x) = x^{2}, then g(x) = (x - 2)^{2} is a new function. Each input is reduced by 2 prior to squaring the function. The result is that the graph is shifted 2 units to the right, because we would need to increase the prior input by 2 units to yield the same output value as given in f. horizontal shift Given a function f, a new function g(x) = f (x - h), where h is a constant, is a horizontal shift of the function f. If h is positive, the graph will shift right. If h is negative, the graph will shift left.

**Example  3**

### Adding a Constant to an Input
Returning to our building airflow example from Figure 3, suppose that in autumn the facilities manager decides that the original venting plan starts too late, and wants to begin the entire venting program 2 hours earlier. Sketch a graph of the new function. Solution We can set V(t) to be the original program and F (t) to be the revised program.

V(t) = the original venting plan

F(t) = starting 2 hrs sooner In the new graph, at each time, the airflow is the same as the original function V was 2 hours later. For example, in the original function V, the airflow starts to change at 8 a.m., whereas for the function F, the airflow starts to change at 6 a.m. The comparable function values are V(8) = F(6). See Figure 6. Notice also that the vents first opened to 220 ft^{2} at 10 a.m. under the original plan, while under the new plan the vents reach 220 ft^{2} at 8 a.m., so V(10) = F(8). In both cases, we see that, because F (t) starts 2 hours sooner, h = -2. That means that the same output values are reached when F (t) = V(t - (-2)) = V(t + 2). t V Lef 2

Analysis Note that V(t + 2) has the effect of shifting the graph to the left. Horizontal changes or “inside changes” affect the domain of a function (the input) instead of the range and often seem counterintuitive. The new function F(t) uses the same outputs as V(t), but matches those outputs to inputs 2 hours earlier than those of V(t). Said another way, we must add 2 hours to the input of V to find the corresponding output for F : F(t) = V(t + 2).

**How To…**
Given a tabular function, create a new row to represent a horizontal shift. 1. Identify the input row or column. 2. Determine the magnitude of the shift. 3. Add the shift to the value in each input cell.

**Example  4**

### Shifting a Tabular Function Horizontally
A function f (x) is given in Table 4. Create a table for the function g (x) = f (x - 3). x f (x) Solution The formula g(x) = f (x - 3) tells us that the output values of g are the same as the output value of f when the input value is 3 less than the original value. For example, we know that f (2) = 1. To get the same output from the function g, we will need an input value that is 3 larger. We input a value that is 3 larger for g (x) because the function takes 3 away before evaluating the function f.

g (5) = f (5 - 3)

= f (2)

= 1 We continue with the other values to create Table 5. x x - 3 f (x - 3) g(x) The result is that the function g (x) has been shifted to the right by 3. Notice the output values for g (x) remain the same as the output values for f (x), but the corresponding input values, x, have shifted to the right by 3. Specifically, 2 shifted to 5, 4 shifted to 7, 6 shifted to 9, and 8 shifted to 11. Analysis Figure 7 represents both of the functions. We can see the horizontal shift in each point. x y f (x) g (x) = f(x – 3)


**Example  5**

### Identifying a Horizontal Shift of a Toolkit Function
find a formula for g (x). f (x) x Solution Notice that the graph is identical in shape to the f (x) = x^{2} function, but the x-values are shifted to the right 2 units. The vertex used to be at (0,0), but now the vertex is at (2,0). The graph is the basic quadratic function shifted 2 units to the right, so

g (x) = f (x - 2) Notice how we must input the value x = 2 to get the output value y = 0; the x-values must be 2 units larger because of the shift to the right by 2 units. We can then use the definition of the f (x) function to write a formula for g (x) by evaluating f (x - 2).

f (x) = x^{2}

g (x) = f (x - 2)

g (x) = f (x - 2) = (x - 2)^{2} Analysis To determine whether the shift is +2 or -2, consider a single reference point on the graph. For a quadratic, looking at the vertex point is convenient. In the original function, f (0) = 0. In our shifted function, g (2) = 0. To obtain the output value of 0 from the function f, we need to decide whether a plus or a minus sign will work to satisfy g (2) = f (x - 2) = f (0) = 0. For this to work, we will need to subtract 2 units from our input values.

**Example  6**

### Interpreting Horizontal versus Vertical Shifts
The function G (m) gives the number of gallons of gas required to drive m miles. Interpret G (m) + 10 and G (m + 10). Solution G (m) + 10 can be interpreted as adding 10 to the output, gallons. This is the gas required to drive m miles, plus another 10 gallons of gas. The graph would indicate a vertical shift. G (m + 10) can be interpreted as adding 10 to the input, miles. So this is the number of gallons of gas required to drive 10 miles more than m miles. The graph would indicate a horizontal shift.

**Try It #2**
Given the function f (x) = \sqrt{x} , graph the original function f (x) and the transformation g (x) = f (x + 2) on the same axes. Is this a horizontal or a vertical shift? Which way is the graph shifted and by how many units? Combining Vertical and Horizontal Shifts Now that we have two transformations, we can combine them together. Vertical shifts are outside changes that affect the output ( y-) axis values and shift the function up or down. Horizontal shifts are inside changes that affect the input (x-) axis values and shift the function left or right. Combining the two types of shifts will cause the graph of a function to shift up or down and right or left.


**How To…**
Given a function and both a vertical and a horizontal shift, sketch the graph. 1. Identify the vertical and horizontal shifts from the formula. 2. The vertical shift results from a constant added to the output. Move the graph up for a positive constant and down for a negative constant. 3. The horizontal shift results from a constant added to the input. Move the graph left for a positive constant and right for a negative constant. 4. Apply the shifts to the graph in either order.

**Example  7**

### Graphing Combined Vertical and Horizontal Shifts
Given f (x) = ∣ x ∣, sketch a graph of h (x) = f (x + 1) - 3. Solution The function f is our toolkit absolute value function. We know that this graph has a V shape, with the point at the origin. The graph of h has transformed f in two ways: f (x + 1) is a change on the inside of the function, giving a horizontal shift left by 1, and the subtraction by 3 in f (x + 1) - 3 is a change to the outside of the function, giving a vertical shift down by 3. The transformation of the graph is illustrated in Figure 9. Let us follow one point of the graph of f (x) = ∣ x ∣. • The point (0, 0) is transformed first by shifting left 1 unit: (0, 0) → (-1, 0) • The point (-1, 0) is transformed next by shifting down 3 units: (-1, 0) → (-1, -3) x y y = |x + 1| y = |x + 1| – 3 y = |x| x y y = |x + 1| – 3

**Try It #3**
Given f (x) = ∣ x ∣, sketch a graph of h(x) = f (x - 2) + 4.


**Example  8**

### Identifying Combined Vertical and Horizontal Shifts
Write a formula for the graph shown in Figure 11, which is a transformation of the toolkit square root function. h(x) x Solution The graph of the toolkit function starts at the origin, so this graph has been shifted 1 to the right and up 2. In function notation, we could write that as h(x) = f (x - 1) + 2 Using the formula for the square root function, we can write h(x) = \sqrt{x} - 1  + 2 Analysis Note that this transformation has changed the domain and range of the function. This new graph has domain [1, \infty ) and range [2, \infty ).

**Try It #4**
Write a formula for a transformation of the toolkit reciprocal function f (x) =  1 __ x  that shifts the function’s graph one unit to the right and one unit up. Graphing Functions Using Reflections about the Axes Another transformation that can be applied to a function is a reflection over the x- or y-axis. A vertical reflection reflects a graph vertically across the x-axis, while a horizontal reflection reflects a graph horizontally across the y-axis. The reflections are shown in Figure 12. Horizontal reflection Original function Vertical reflection x y f(x) f(–x) –f(x) Notice that the vertical reflection produces a new graph that is a mirror image of the base or original graph about the x-axis. The horizontal reflection produces a new graph that is a mirror image of the base or original graph about the y-axis.

reflections Given a function f (x), a new function g(x) = -f (x) is a vertical reflection of the function f (x), sometimes called a reflection about (or over, or through) the x-axis. Given a function f (x), a new function g(x) = f (-x) is a horizontal reflection of the function f (x), sometimes called a reflection about the y-axis.

**How To…**
Given a function, reflect the graph both vertically and horizontally. 1. Multiply all outputs by –1 for a vertical reflection. The new graph is a reflection of the original graph about the x-axis. 2. Multiply all inputs by –1 for a horizontal reflection. The new graph is a reflection of the original graph about the y-axis.

**Example  9**
Reflecting a Graph Horizontally and Vertically Reflect the graph of s(t) = \sqrt{—} t  a. vertically and b. horizontally.

**Solution**
a. Reflecting the graph vertically means that each output value will be reflected over the horizontal t-axis as shown in Figure 13. t s(t) t v(t) Because each output value is the opposite of the original output value, we can write V(t) = -s(t) or V(t) = -\sqrt{—} t  Notice that this is an outside change, or vertical shift, that affects the output s(t) values, so the negative sign belongs outside of the function. b. Reflecting horizontally means that each input value will be reflected over the vertical axis as shown in Figure 14. t s(t) t H(t)

Because each input value is the opposite of the original input value, we can write H(t) = s(-t) or H(t) = \sqrt{-t}  Notice that this is an inside change or horizontal change that affects the input values, so the negative sign is on the inside of the function. Note that these transformations can affect the domain and range of the functions. While the original square root function has domain [0, \infty ) and range [0, \infty ), the vertical reflection gives the V(t) function the range (-\infty , 0] and the horizontal reflection gives the H(t) function the domain (-\infty , 0].

**Try It #5**
Reflect the graph of f (x) = |x - 1| a. vertically and b. horizontally.

**Example  10**
Reflecting a Tabular Function Horizontally and Vertically A function f (x) is given as Table 6. Create a table for the functions below. a. g(x) = -f (x) b. h(x) = f (-x) x f (x)

**Solution**
a. For g(x), the negative sign outside the function indicates a vertical reflection, so the x-values stay the same and each output value will be the opposite of the original output value. See Table 7. x g (x) b. For h(x), the negative sign inside the function indicates a horizontal reflection, so each input value will be the opposite of the original input value and the h(x) values stay the same as the f (x) values. See Table 8. x h(x)

**Try It #6**
A function f (x) is given as Table 9. Create a table for the functions below. x -2 f(x) a. g(x) = -f (x) b. h(x) = f (-x)


**Example  11**

### Applying a Learning Model Equation
A common model for learning has an equation similar to k(t) = -2-t + 1, where k is the percentage of mastery that can be achieved after t practice sessions. This is a transformation of the function f (t) = 2t shown in Figure 15. Sketch a graph of k(t). t f (t) Solution This equation combines three transformations into one equation. • A horizontal reflection: f (-t) = 2-t • A vertical reflection: -f (-t) = -2-t • A vertical shift: -f (-t) + 1 = -2-t + 1 We can sketch a graph by applying these transformations one at a time to the original function. Let us follow two points through each of the three transformations. We will choose the points (0, 1) and (1, 2). 1. First, we apply a horizontal reflection: (0, 1) (-1, 2). 2. Then, we apply a vertical reflection: (0, -1) (1, -2). 3. Finally, we apply a vertical shift: (0, 0) (1, 1). This means that the original points, (0,1) and (1,2) become (0,0) and (1,1) after we apply the transformations. In Figure 16, the first graph results from a horizontal reflection. The second results from a vertical reflection. The third results from a vertical shift up 1 unit. t f (t) (a) (b) (c) t f (t) t k(t) Analysis As a model for learning, this function would be limited to a domain of t \ge  0, with corresponding range [0, 1).

**Try It #7**
Given the toolkit function f (x) = x 2, graph g(x) = -f (x) and h(x) = f (-x). Take note of any surprising behavior for these functions.

Determining Even and Odd Functions Some functions exhibit symmetry so that reflections result in the original graph. For example, horizontally reflecting the toolkit functions f (x) = x^{2} or f (x) = x will result in the original graph. We say that these types of graphs are symmetric about the y-axis. Functions whose graphs are symmetric about the y-axis are called even functions. If the graphs of f (x) = x^{3} or f (x) =  1 _ x  were reflected over both axes, the result would be the original graph, as shown in Figure 17. x y y (a) (b) x f (x) = x^{3} f (-x) y (c) x -f (-x) (c) Horizontal and vertical reflections reproduce the original cubic function. We say that these graphs are symmetric about the origin. A function with a graph that is symmetric about the origin is called an odd function. Note: A function can be neither even nor odd if it does not exhibit either symmetry. For example, f (x) = 2x is neither even nor odd. Also, the only function that is both even and odd is the constant function f (x) = 0. even and odd functions A function is called an even function if for every input x: f (x) = f (-x) The graph of an even function is symmetric about the y-axis. A function is called an odd function if for every input x: f (x) = -f (-x) The graph of an odd function is symmetric about the origin.

**How To…**
Given the formula for a function, determine if the function is even, odd, or neither. 1. Determine whether the function satisfies f (x) = f (-x). If it does, it is even. 2. Determine whether the function satisfies f (x) = -f (-x). If it does, it is odd. 3. If the function does not satisfy either rule, it is neither even nor odd.

**Example  12**
Determining whether a Function Is Even, Odd, or Neither Is the function f (x) = x 3 + 2x even, odd, or neither? Solution Without looking at a graph, we can determine whether the function is even or odd by finding formulas for the reflections and determining if they return us to the original function. Let’s begin with the rule for even functions. f (-x) = (-x)^{3} + 2(-x) = -x 3 - 2x This does not return us to the original function, so this function is not even. We can now test the rule for odd functions. -f (-x) = -(-x 3 - 2x) = x 3 + 2x Because -f (-x) = f (x), this is an odd function.

Analysis Consider the graph of f in Figure 18. Notice that the graph is symmetric about the origin. For every point (x, y) on the graph, the corresponding point (-x, -y) is also on the graph. For example, (1, 3) is on the graph of f, and the corresponding point (-1, -3) is also on the graph. x f (x) f

**Try It #8**
Is the function f (s) = s 4 + 3s 2 + 7 even, odd, or neither? Graphing Functions Using Stretches and Compressions Adding a constant to the inputs or outputs of a function changed the position of a graph with respect to the axes, but it did not affect the shape of a graph. We now explore the effects of multiplying the inputs or outputs by some quantity. We can transform the inside (input values) of a function or we can transform the outside (output values) of a function. Each change has a specific effect that can be seen graphically. Vertical Stretches and Compressions When we multiply a function by a positive constant, we get a function whose graph is stretched or compressed vertically in relation to the graph of the original function. If the constant is greater than 1, we get a vertical stretch; if the constant is between 0 and 1, we get a vertical compression. Figure 19 shows a function multiplied by constant factors 2 and 0.5 and the resulting vertical stretch and compression. Vertical stretch Vertical compression x y 2f(x) f(x) vertical stretches and compressions Given a function f (x), a new function g(x) = af (x), where a is a constant, is a vertical stretch or vertical compression of the function f (x). • If a > 1, then the graph will be stretched. • If 0 < a < 1, then the graph will be compressed. • If a < 0, then there will be combination of a vertical stretch or compression with a vertical reflection.


**How To…**
Given a function, graph its vertical stretch. 1. Identify the value of a. 2. Multiply all range values by a. 3. If a > 1, the graph is stretched by a factor of a. If 0 < a < 1, the graph is compressed by a factor of a. If a < 0, the graph is either stretched or compressed and also reflected about the x-axis.

**Example  13**

### Graphing a Vertical Stretch
A function P(t) models the population of fruit flies. The graph is shown in Figure 20. t P(t) A scientist is comparing this population to another population, Q, whose growth follows the same pattern, but is twice as large. Sketch a graph of this population. Solution Because the population is always twice as large, the new population’s output values are always twice the original function’s output values. Graphically, this is shown in Figure 21. If we choose four reference points, (0, 1), (3, 3), (6, 2) and (7, 0) we will multiply all of the outputs by 2. The following shows where the new points for the new graph will be located. t Q(t) Symbolically, the relationship is written as Q(t) = 2P(t) This means that for any input t, the value of the function Q is twice the value of the function P. Notice that the effect on the graph is a vertical stretching of the graph, where every point doubles its distance from the horizontal axis. The input values, t, stay the same while the output values are twice as large as before.


**How To…**
Given a tabular function and assuming that the transformation is a vertical stretch or compression, create a table for a vertical compression. 1. Determine the value of a. 2. Multiply all of the output values by a.

**Example  14**
Finding a Vertical Compression of a Tabular Function A function f is given as Table 10. Create a table for the function g(x) =  1 __ 2 f (x). x f (x) Solution The formula g(x) =  1 __ 2 f (x) tells us that the output values of g are half of the output values of f with the same inputs. For example, we know that f (4) = 3. Then g(4) =  1 __ 2 f (4) =  1 __ 2 (3) =  3 __ 2  We do the same for the other values to produce Table 11. x g(x)  1 __ 2   3 __ 2   7 __ 2   11 __ 2  Analysis The result is that the function g(x) has been compressed vertically by  1 __ 2 . Each output value is divided in half, so the graph is half the original height.

**Try It #9**
A function f is given as Table 12. Create a table for the function g(x) =  3 __ 4  f (x). x f(x)

**Example  15**

### Recognizing a Vertical Stretch
The graph in Figure 22 is a transformation of the toolkit function f (x) = x^{3}. Relate this new function g(x) to f (x), and then find a formula for g(x). x g(x)

Solution When trying to determine a vertical stretch or shift, it is helpful to look for a point on the graph that is relatively clear. In this graph, it appears that g(2) = 2. With the basic cubic function at the same input, f (2) = 23 = 8. Based on that, it appears that the outputs of g are  1 __ 4  the outputs of the function f because g(2) =  1 __ 4  f (2). From this we can fairly safely conclude that g(x) =  1 __ 4  f (x). We can write a formula for g by using the definition of the function f. g(x) =  1 __ 4  f (x) =  1 __ 4 x^{3}

**Try It #10**
Write the formula for the function that we get when we stretch the identity toolkit function by a factor of 3, and then shift it down by 2 units. Horizontal Stretches and Compressions Now we consider changes to the inside of a function. When we multiply a function’s input by a positive constant, we get a function whose graph is stretched or compressed horizontally in relation to the graph of the original function. If the constant is between 0 and 1, we get a horizontal stretch; if the constant is greater than 1, we get a horizontal compression of the function. x y Horizontal stretch Horizontal compression y = (2x)^{2} y = x^{2} Given a function y = f (x), the form y = f (bx) results in a horizontal stretch or compression. Consider the function y = x^{2}. Observe Figure 23. The graph of y = (0.5x)^{2} is a horizontal stretch of the graph of the function y = x 2 by a factor of 2. The graph of y = (2x)^{2} is a horizontal compression of the graph of the function y = x 2 by a factor of 2. horizontal stretches and compressions Given a function f (x), a new function g(x) = f (bx), where b is a constant, is a horizontal stretch or horizontal compression of the function f (x). • If b > 1, then the graph will be compressed by  1 __ b . • If 0 < b < 1, then the graph will be stretched by  1 __ b . • If b < 0, then there will be combination of a horizontal stretch or compression with a horizontal reflection.

**How To…**
Given a description of a function, sketch a horizontal compression or stretch. 1. Write a formula to represent the function. 2. Set g(x) = f (bx) where b > 1 for a compression or 0 < b < 1 for a stretch.


**Example  16**

### Graphing a Horizontal Compression
Suppose a scientist is comparing a population of fruit flies to a population that progresses through its lifespan twice as fast as the original population. In other words, this new population, R, will progress in 1 hour the same amount as the original population does in 2 hours, and in 2 hours, it will progress as much as the original population does in 4 hours. Sketch a graph of this population. Solution Symbolically, we could write

R(1) = P(2),

R(2) = P(4), and in general,

R(t) = P(2t). See Figure 24 for a graphical comparison of the original population and the compressed population. Original population, P(t) (a) Transformed population, R(t) (b) f (x) x f (x) x Analysis Note that the effect on the graph is a horizontal compression where all input values are half of their original distance from the vertical axis.

**Example  17**
Finding a Horizontal Stretch for a Tabular Function A function f (x) is given as Table 13. Create a table for the function g(x) = f   1 __ 2 x . x f (x) Solution The formula g(x) = f   1 __ 2 x  tells us that the output values for g are the same as the output values for the function f at an input half the size. Notice that we do not have enough information to determine g(2) because g(2) = f   1 __ 2  ⋅ 2  = f (1), and we do not have a value for f (1) in our table. Our input values to g will need to be twice as large to get inputs for f that we can evaluate. For example, we can determine g(4). g(4) = f   1 __ 2  ⋅ 4  = f (2) = 1 We do the same for the other values to produce Table 14. x g(x)

x y (a) x y (b) Analysis Because each input value has been doubled, the result is that the function g(x) has been stretched horizontally by a factor of 2.

**Example  18**

### Recognizing a Horizontal Compression on a Graph
Relate the function g(x) to f (x) in Figure 26. f g f (x) x Solution The graph of g(x) looks like the graph of f (x) horizontally compressed. Because f (x) ends at (6, 4) and g(x) ends at (2, 4), we can see that the x-values have been compressed by  1 __ 3 , because 6   1 __ 3   = 2. We might also notice that g(2) = f (6) and g(1) = f (3). Either way, we can describe this relationship as g(x) = f (3x). This is a horizontal compression by  1 __ 3 .

**Analysis**
Notice that the coefficient needed for a horizontal stretch or compression is the reciprocal of the stretch or compression. So to stretch the graph horizontally by a scale factor of 4, we need a coefficient of  1 __ 4  in our function: f   1 __ 4 x . This means that the input values must be four times larger to produce the same result, requiring the input to be larger, causing the horizontal stretching.

**Try It #11**
Write a formula for the toolkit square root function horizontally stretched by a factor of 3.


### Performing a Sequence of Transformations
When combining transformations, it is very important to consider the order of the transformations. For example, vertically shifting by 3 and then vertically stretching by 2 does not create the same graph as vertically stretching by 2 and then vertically shifting by 3, because when we shift first, both the original function and the shift get stretched, while only the original function gets stretched when we stretch first. When we see an expression such as 2f (x) + 3, which transformation should we start with? The answer here follows nicely from the order of operations. Given the output value of f (x), we first multiply by 2, causing the vertical stretch, and then add 3, causing the vertical shift. In other words, multiplication before addition. Horizontal transformations are a little trickier to think about. When we write g(x) = f (2x + 3), for example, we have to think about how the inputs to the function g relate to the inputs to the function f . Suppose we know f (7) = 12. What input to g would produce that output? In other words, what value of x will allow g(x) = f (2x + 3) = 12? We would need 2x + 3 = 7. To solve for x, we would first subtract 3, resulting in a horizontal shift, and then divide by 2, causing a horizontal compression. This format ends up being very difficult to work with, because it is usually much easier to horizontally stretch a graph before shifting. We can work around this by factoring inside the function. f (bx + p) = f  b  x +  p _ b    Let’s work through an example. f (x) = (2x + 4)^{2} We can factor out a 2. f (x) = (2(x + 2))^{2} Now we can more clearly observe a horizontal shift to the left 2 units and a horizontal compression. Factoring in this way allows us to horizontally stretch first and then shift horizontally. combining transformations When combining vertical transformations written in the form af (x) + k, first vertically stretch by a and then vertically shift by k. When combining horizontal transformations written in the form f (bx - h), first horizontally shift by h and then horizontally stretch by  1 __ b . When combining horizontal transformations written in the form f (b(x - h)), first horizontally stretch by  1 _ b  and then horizontally shift by h. Horizontal and vertical transformations are independent. It does not matter whether horizontal or vertical transformations are performed first.

**Example  19**
Finding a Triple Transformation of a Tabular Function Given Table 15 for the function f (x), create a table of values for the function g(x) = 2f (3x) + 1. x f (x) Solution There are three steps to this transformation, and we will work from the inside out. Starting with the horizontal transformations, f (3x) is a horizontal compression by  1 __ 3 , which means we multiply each x-value by  1 __ 3 . See Table 16. x f (3x)

Looking now to the vertical transformations, we start with the vertical stretch, which will multiply the output values by 2. We apply this to the previous transformation. See Table 17. x 2f (3x) Finally, we can apply the vertical shift, which will add 1 to all the output values. See Table 18. x g(x) = 2f (3x) + 1

**Example  20**
Finding a Triple Transformation of a Graph Use the graph of f (x) in Figure 27 to sketch a graph of k(x) = f   1 __ 2 x + 1  - 3. x f (x) Solution To simplify, let’s start by factoring out the inside of the function. f   1 __ 2 x + 1  - 3 = f   1 __ 2 (x + 2)  - 3 By factoring the inside, we can first horizontally stretch by 2, as indicated by the  1 __ 2  on the inside of the function. Remember that twice the size of 0 is still 0, so the point (0, 2) remains at (0, 2) while the point (2, 0) will stretch to (4, 0). See Figure 28. x f (x)

Next, we horizontally shift left by 2 units, as indicated by x + 2. See Figure 29. x f (x) Last, we vertically shift down by 3 to complete our sketch, as indicated by the -3 on the outside of the function. See x f (x) > Access this online resource for additional instruction and practice with transformation of functions. • Function Transformations (http://openstaxcollege.org/l/functrans)


## 1.5 Section Exercises

### 1.5 Section Exercises
Verbal 1. When examining the formula of a function that is the result of multiple transformations, how can you tell a horizontal shift from a vertical shift? 2. When examining the formula of a function that is the result of multiple transformations, how can you tell a horizontal stretch from a vertical stretch? 3. When examining the formula of a function that is the result of multiple transformations, how can you tell a horizontal compression from a vertical compression? 4. When examining the formula of a function that is the result of multiple transformations, how can you tell a reflection with respect to the x-axis from a reflection with respect to the y-axis? 5. How can you determine whether a function is odd or even from the formula of the function? Algebraic 6. Write a formula for the function obtained when the graph of f (x) = \sqrt{x}  is shifted up 1 unit and to the left 2 units. 7. Write a formula for the function obtained when the graph of f (x) = |x| is shifted down 3 units and to the right 1 unit. 8. Write a formula for the function obtained when the graph of f (x) =  1 _ x  is shifted down 4 units and to the right 3 units. 9. Write a formula for the function obtained when the graph of f (x) =  1 _ x^{2}  is shifted up 2 units and to the left 4 units. For the following exercises, describe how the graph of the function is a transformation of the graph of the original function f. 10. y = f (x - 49) 11. y = f (x + 43) 12. y = f (x + 3) 13. y = f (x - 4) 14. y = f (x) + 5 15. y = f (x) + 8 16. y = f (x) - 2 17. y = f (x) - 7 18. y = f (x - 2) + 3 19. y = f (x + 4) - 1 For the following exercises, determine the interval(s) on which the function is increasing and decreasing. 20. f (x) = 4(x + 1)^{2} - 5 21. g(x) = 5(x + 3)^{2} - 2 22. a(x) = \sqrt{-x} + 4  23. k(x) = -3\sqrt{x}  - 1 f x y GRAPHICAL For the following exercises, use the graph of f (x) = 2x shown in Figure 31 to sketch a graph of each transformation of f (x). 24. g(x) = 2x + 1 25. h(x) = 2x - 3 26. w(x) = 2x - 1 For the following exercises, sketch a graph of the function as a transformation of the graph of one of the toolkit functions. 27. f (t) = (t + 1)^{2} - 3 28. h(x) = |x - 1| + 4 29. k(x) = (x - 2)^{3} - 1 30. m(t) = 3 + \sqrt{t} + 2 

Numeric 31. Tabular representations for the functions f, g, and h are given below. Write g(x) and h(x) as transformations of f (x). x f (x) x g(x) x h(x) 32. Tabular representations for the functions f, g, and h are given below. Write g(x) and h(x) as transformations of f (x). x f (x) x g(x) x h(x) For the following exercises, write an equation for each graphed function by using transformations of the graphs of one of the toolkit functions. f x y f x y f x y x f y x f y x f y

x f y x f y For the following exercises, use the graphs of transformations of the square root function to find a formula for each of the functions. x f y x f y For the following exercises, use the graphs of the transformed toolkit functions to write a formula for each of the resulting functions. x f y x f y x f y x f y

For the following exercises, determine whether the function is odd, even, or neither. 47. f (x) = 3x 4 48. g(x) = \sqrt{x}  49. h(x) =  1 __ x  + 3x 50. f (x) = (x - 2)^{2} 51. g(x) = 2x^{4} 52. h(x) = 2x - x^{3} For the following exercises, describe how the graph of each function is a transformation of the graph of the original function f. 53. g(x) = -f (x) 54. g(x) = f (-x) 55. g(x) = 4f (x) 56. g(x) = 6f (x) 57. g(x) = f (5x) 58. g(x) = f (2x) 59. g(x) = f   1 __ 3 x  60. g(x) = f   1 __ 5 x  61. g(x) = 3f (-x) 62. g(x) = -f (3x) For the following exercises, write a formula for the function g that results when the graph of a given toolkit function is transformed as described. 63. The graph of f (x) = ∣ x ∣ is reflected over the y-axis and horizontally compressed by a factor of  1 __ 4 . 64. The graph of f (x) = \sqrt{x}  is reflected over the x-axis and horizontally stretched by a factor of 2. 65. The graph of f (x) =  1 __ x^{2}  is vertically compressed by a factor of  1 __ 3 , then shifted to the left 2 units and down 3 units. 66. The graph of f (x) =  1 __ x  is vertically stretched by a factor of 8, then shifted to the right 4 units and up 2 units. 67. The graph of f (x) = x^{2} is vertically compressed by a factor of  1 __ 2 , then shifted to the right 5 units and up 1 unit. 68. The graph of f (x) = x^{2} is horizontally stretched by a factor of 3, then shifted to the left 4 units and down 3 units. For the following exercises, describe how the formula is a transformation of a toolkit function. Then sketch a graph of the transformation. 69. g(x) = 4(x + 1)^{2} - 5 70. g(x) = 5(x + 3)^{2} - 2 71. h(x) = -2∣ x - 4 ∣ + 3 72. k(x) = -3\sqrt{x}  - 1 73. m(x) =  1 __ 2  x^{3} 74. n(x) =  1 __ 3 |x - 2| 75. p(x) =   1 __ 3 x  - 3 76. q(x) =   1 __ 4 x  + 1 77. a(x) = \sqrt{-x} + 4  For the following exercises, use the graph in Figure 32 to sketch the given transformations. x y f 78. g(x) = f (x) - 2 79. g(x) = -f (x) 80. g(x) = f (x + 1) 81. g(x) = f (x - 2)


## 1.6 Absolute Value Functions
1. 6 Absolute Value Functions Until the 1920s, the so-called spiral nebulae were believed to be clouds of dust and gas in our own galaxy, some tens of thousands of light years away. Then, astronomer Edwin Hubble proved that these objects are galaxies in their own right, at distances of millions of light years. Today, astronomers can detect galaxies that are billions of light years away. Distances in the universe can be measured in all directions. As such, it is useful to consider distance as an absolute value function. In this section, we will investigate absolute value functions. Understanding Absolute Value Recall that in its basic form f (x) = | x |, the absolute value function, is one of our toolkit functions. The absolute value function is commonly thought of as providing the distance the number is from zero on a number line. Algebraically, for whatever the input value is, the output is the value without regard to sign. absolute value function The absolute value function can be defined as a piecewise function f (x) = ∣ x ∣ = x if x \ge  0 -x if x < 0 {

**Example  1**
Determine a Number within a Prescribed Distance Describe all values x within or including a distance of 4 from the number 5. Solution We want the distance between x and 5 to be less than or equal to 4. We can draw a number line, such as the one in Figure 2, to represent the condition to be satisfied. The distance from x to 5 can be represented using the absolute value as ∣ x - 5 ∣. We want the values of x that satisfy the condition ∣ x - 5 ∣ \le  4. Analysis Note that

-4 \le  x - 5 x - 5 \le  4

1 \le  x x \le  9 So ∣ x - 5 ∣ \le  4 is equivalent to 1 \le  x \le  9. However, mathematicians generally prefer absolute value notation. Learning Objectives In this section you will: • Graph an absolute value function. • Solve an absolute value equation. • Solve an absolute value inequality.


**Try It #1**
Describe all values x within a distance of 3 from the number 2.

**Example  2**
Resistance of a Resistor Electrical parts, such as resistors and capacitors, come with specified values of their operating parameters: resistance, capacitance, etc. However, due to imprecision in manufacturing, the actual values of these parameters vary somewhat from piece to piece, even when they are supposed to be the same. The best that manufacturers can do is to try to guarantee that the variations will stay within a specified range, often \pm 1%, \pm 5%, or \pm 10%. Suppose we have a resistor rated at 680 ohms, \pm 5%. Use the absolute value function to express the range of possible values of the actual resistance. Solution 5% of 680 ohms is 34 ohms. The absolute value of the difference between the actual and nominal resistance should not exceed the stated variability, so, with the resistance R in ohms, | R - 680 | \le  34

**Try It #2**
Students who score within 20 points of 80 will pass a test. Write this as a distance from 80 using absolute value notation. Graphing an Absolute Value Function The most significant feature of the absolute value graph is the corner point at which the graph changes direction. This point is shown at the origin in Figure 3. x y y = |x| a factor of 2, and shifted up 4 units. This means that the corner point is located at (3, 4) for this transformed function. x y Vertical stretch y = 2|x - 3| Right 3 y = |x - 3| y = |x| Up 4 y = 2|x - 3| + 4


**Example  3**

### Writing an Equation for an Absolute Value Function
Write an equation for the function graphed in Figure 5. x y Solution The basic absolute value function changes direction at the origin, so this graph has been shifted to the right 3 units and down 2 units from the basic toolkit function. See Figure 6. x y We also notice that the graph appears vertically stretched, because the width of the final graph on a horizontal line is not equal to 2 times the vertical distance from the corner to this line, as it would be for an unstretched absolute value function. Instead, the width is equal to 1 times the vertical distance as shown in Figure 7. x y Ratio 2/1 Ratio 1/1 From this information we can write the equation f (x) = 2| x - 3 | - 2, treating the stretch as a vertical stretch, or

f (x) = | 2(x - 3) | - 2, treating the stretch as a horizontal compression. Analysis Note that these equations are algebraically equivalent—the stretch for an absolute value function can be written interchangeably as a vertical or horizontal stretch or compression.

If we couldn’t observe the stretch of the function from the graphs, could we algebraically determine it? Yes. If we are unable to determine the stretch based on the width of the graph, we can solve for the stretch factor by putting in a known pair of values for x and f (x). f (x) = a| x - 3 | - 2 Now substituting in the point (1, 2)

2 = a| 1 - 3 | - 2

4 = 2a

a = 2

**Try It #3**
Write the equation for the absolute value function that is horizontally shifted left 2 units, is vertically flipped, and verti- cally shifted up 3 units. Do the graphs of absolute value functions always intersect the vertical axis? The horizontal axis? Yes, they always intersect the vertical axis. The graph of an absolute value function will intersect the vertical axis when the input is zero. No, they do not always intersect the horizontal axis. The graph may or may not intersect the horizontal axis, depending on how the graph has been shifted and reflected. It is possible for the absolute value function to intersect the horizontal axis at zero, one, or two points (see Figure 8). x y (a) (b) (c) x y x y The absolute value function intersects the horizontal axis at two points. Solving an Absolute Value Equation Now that we can graph an absolute value function, we will learn how to solve an absolute value equation. To solve an equation such as 8 = | 2x - 6| , we notice that the absolute value will be equal to 8 if the quantity inside the absolute value is 8 or -8. This leads to two different equations we can solve independently. 2x - 6 = 8 or 2x - 6 = -8

2x = -2

x = 7 x = -1 Knowing how to solve problems involving absolute value functions is useful. For example, we may need to identify numbers or points on a line that are at a specified distance from a given reference point. An absolute value equation is an equation in which the unknown variable appears in absolute value bars. For example,

| x | = 4,

| 2x - 1 | = 3

| 5x + 2 | - 4 = 9

solutions to absolute value equations For real numbers A and B, an equation of the form | A | = B, with B \ge  0, will have solutions when A = B or A = -B. If B < 0, the equation | A | = B has no solution.

**How To…**
Given the formula for an absolute value function, find the horizontal intercepts of its graph. 1. Isolate the absolute value term. 2. Use | A | = B to write A = B or -A = B, assuming B > 0. 3. Solve for x.

**Example  4**
Finding the Zeros of an Absolute Value Function For the function f (x) = | 4x + 1 | - 7 , find the values of x such that f (x) = 0.

**Solution**
0 = | 4x + 1 | - 7 Substitute 0 for f (x). 7 = | 4x + 1 | Isolate the absolute value on one side of the equation. 7 = 4x + 1 or -7 = 4x + 1 Break into two separate equations and solve. 6 = 4x -8 = 4x x =  6 __ x =  -8 ___ 4  = -2 The function outputs 0 when x = 1.5 or x = -2. See Figure 9. x y f 1.5 0.5 2.5 x where f(x) = 0 x where f(x) = 0

**Try It #4**
For the function f (x) = | 2x - 1 | - 3, find the values of x such that f (x) = 0. Should we always expect two answers when solving ∣ A ∣ = B? No. We may find one, two, or even no answers. For example, there is no solution to 2 + | 3x - 5 | = 1.

**How To…**
Given an absolute value equation, solve it. 1. Isolate the absolute value term. 2. Use | A | = B to write A = B or A = -B. 3. Solve for x.


**Example  5**

### Solving an Absolute Value Equation
Solve 1 = 4| x - 2| + 2. Solution Isolating the absolute value on one side of the equation gives the following.

1 = 4| x - 2 | + 2

-1 = 4| x - 2 |

- 1 _ 4  = | x - 2 | The absolute value always returns a positive value, so it is impossible for the absolute value to equal a negative value. At this point, we notice that this equation has no solutions. In Example 5, if f(x) = 1 and g(x) = 4∣ x - 2 ∣ + 2 were graphed on the same set of axes, would the graphs intersect? No. The graphs of f and g would not intersect, as shown in Figure 10. This confirms, graphically, that the equation 1 = 4| x - 2 | + 2 has no solution. x y f (x) = 1 g(x) = 4|x - 2| + 2

**Try It #5**
Find where the graph of the function f (x) = -| x + 2 | + 3 intersects the horizontal and vertical axes. Solving an Absolute Value Inequality Absolute value equations may not always involve equalities. Instead, we may need to solve an equation within a range of values. We would use an absolute value inequality to solve such an equation. An absolute value inequality is an equation of the form | A | < B, | A | \le  B, | A | \ge  B, or | A | \ge  B, where an expression A (and possibly but not usually B) depends on a variable x. Solving the inequality means finding the set of all x that satisfy the inequality. Usually this set will be an interval or the union of two intervals. There are two basic approaches to solving absolute value inequalities: graphical and algebraic. The advantage of the graphical approach is we can read the solution by interpreting the graphs of two functions. The advantage of the algebraic approach is it yields solutions that may be difficult to read from the graph. For example, we know that all numbers within 200 units of 0 may be expressed as | x | < 200 or -200 < x < 200 Suppose we want to know all possible returns on an investment if we could earn some amount of money within $200 of $600. We can solve algebraically for the set of values x such that the distance between x and 600 is less than 200. We represent the distance between x and 600 as | x - 600 |.

This means our returns would be between $400 and $800. Sometimes an absolute value inequality problem will be presented to us in terms of a shifted and/or stretched or compressed absolute value function, where we must determine for which values of the input the function’s output will be negative or positive.

**How To…**
Given an absolute value inequality of the form | x - A | \le  B for real numbers a and b where b is positive, solve the absolute value inequality algebraically. 1. Find boundary points by solving | x - A | = B. 2. Test intervals created by the boundary points to determine where | x - A | \le  B. 3. Write the interval or union of intervals satisfying the inequality in interval, inequality, or set-builder notation.

**Example  6**

### Solving an Absolute Value Inequality
Solve | x - 5| < 4. Solution With both approaches, we will need to know first where the corresponding equality is true. In this case we first will find where | x - 5| = 4. We do this because the absolute value is a function with no breaks, so the only way the function values can switch from being less than 4 to being greater than 4 is by passing through where the values equal 4. Solve | x - 5| = 4. x - 5 = 4 or x - 5 = -4

x = 9 x = 1 After determining that the absolute value is equal to 4 at x = 1 and x = 9, we know the graph can change only from being less than 4 to greater than 4 at these values. This divides the number line up into three intervals: x < 1, 1 < x < 9, and x > 9. To determine when the function is less than 4, we could choose a value in each interval and see if the output is less than or greater than 4, as shown in Table 1. Interval test x f (x) < 4 or > 4? x < 1 | 0 - 5| = 5 Greater than 1 < x < 9 | 6 - 5| = 1 Less than x > 9 | 11 - 5| = 6 Greater than Because 1 \le  x \le  9 is the only interval in which the output at the test value is less than 4, we can conclude that the solution to | x - 5| \le  4 is 1 \le  x \le  9, or [1, 9]. To use a graph, we can sketch the function f (x) = | x - 5| . To help us see where the outputs are 4, the line g(x) = 4 could also be sketched as in Figure 11. g f Te graph of f is below or on the graph of g f (x) x

We can see the following: • The output values of the absolute value are equal to 4 at x = 1 and x = 9. • The graph of f is below the graph of g on 1 < x < 9. This means the output values of f (x) are less than the output values of g(x). • The absolute value is less than or equal to 4 between these two points, when 1 \le  x \le  9. In interval notation, this would be the interval [1, 9]. Analysis For absolute value inequalities,

| x - A | < C, | x - A | > C,

-C < x - A < C, x - A < -C or x - A > C. The < or > symbol may be replaced by \le  or \ge . So, for this example, we could use this alternative approach.

| x - 5| \le  4

-4 \le  x - 5 \le  4 Rewrite by removing the absolute value bars.

-4 + 5 \le  x - 5 + 5 \le  4 + 5 Isolate the x.

1 \le  x \le  9

**Try It #6**
Solve | x + 2| \le  6.

**How To…**
Given an absolute value function, solve for the set of inputs where the output is positive (or negative). 1. Set the function equal to zero, and solve for the boundary points of the solution set. 2. Use test points or a graph to determine where the function’s output is positive or negative.

**Example  7**
Using a Graphical Approach to Solve Absolute Value Inequalities Given the function f (x) = - 1 __ 2 | 4x - 5 | + 3, determine the x-values for which the function values are negative. Solution We are trying to determine where f (x) < 0, which is when - 1 __ 2 | 4x - 5| + 3 < 0. We begin by isolating the absolute value.

- 1 __ 2 | 4x - 5| < -3 Multiply both sides by -2, and reverse the inequality.

| 4x - 5| > 6 Next we solve for the equality | 4x - 5| = 6.

4x - 5 = 6 or 4x - 5 = -6

4x - 5 = 6 4x = -1

x =  11 __ 4  x = - 1 __ 4  Now, we can examine the graph of f to observe where the output is negative. We will observe where the branches are below the x-axis. Notice that it is not even important exactly what the graph looks like, as long as we know that it crosses the horizontal axis at x = - 1 __ 4  and x =  11 __ 4  and that the graph has been reflected vertically. See Figure 12.

x y Below x-axis Below x-axis We observe that the graph of the function is below the x-axis left of x = - 1 __ 4  and right of x =  11 __ 4  This means the function values are negative to the left of the first horizontal intercept at x = - 1 __ 4 , and negative to the right of the second intercept at x =  11 __ 4 .This gives us the solution to the inequality. x < - 1 __ 4  or x >  11 __ 4  In interval notation, this would be (-\infty , -0.25) ∪ (2.75, \infty ).

**Try It #7**
Solve -2| k - 4| \le  -6. Access these online resources for additional instruction and practice with absolute value. • Graphing Absolute Value Functions (http://openstaxcollege.org/l/graphabsvalue) • Graphing Absolute Value Functions 2 (http://openstaxcollege.org/l/graphabsvalue^{2}) • Equations of Absolute Value Function (http://openstaxcollege.org/l/findeqabsval) • Equations of Absolute Value Function 2 (http://openstaxcollege.org/l/findeqabsval^{2}) • Solving Absolute Value Equations (http://openstaxcollege.org/l/solveabsvalueeq)

1.6 SECTION EXERCISES Verbal 1. How do you solve an absolute value equation? 2. How can you tell whether an absolute value function has two x-intercepts without graphing the function? 3. When solving an absolute value function, the isolated absolute value term is equal to a negative number. What does that tell you about the graph of the absolute value function? 4. How can you use the graph of an absolute value function to determine the x-values for which the function values are negative? 5. How do you solve an absolute value inequality algebraically? Algebraic 6. Describe all numbers x that are at a distance of 4 from the number 8. Express this using absolute value notation. 7. Describe all numbers x that are at a distance of  1 __ 2  from the number -4. Express this using absolute value notation. 8. Describe the situation in which the distance that point x is from 10 is at least 15 units. Express this using absolute value notation. 9. Find all function values f (x) such that the distance from f (x) to the value 8 is less than 0.03 units. Express this using absolute value notation. For the following exercises, solve the equations below and express the answer using set notation. 10. | x + 3 | = 9 11. | 6 - x | = 5 12. | 5x - 2 | = 11 13. | 4x - 2 | = 11 14. 2| 4 - x | = 7 15. 3| 5 - x | = 5 16. 3| x + 1 | - 4 = 5 17. 5| x - 4 | - 7 = 2 18. 0 = -| x - 3 | + 2 19. 2| x - 3 | + 1 = 2 20. | 3x - 2 | = 7 21. | 3x - 2 | = -7 __ 2 x - 5  = 11 __ 3 x + 5  = 14 24. -  1 __ 3 x + 5  + 14 = 0 For the following exercises, find the x- and y-intercepts of the graphs of each function. 25. f (x) = 2| x +1 | - 10 26. f (x) = 4| x - 3 | + 4 27. f (x) = -3| x - 2 | - 1 28. f (x) = -2| x +1 | + 6 For the following exercises, solve each inequality and write the solution in interval notation. 29. | x - 2 | > 10 30. 2| v - 7 | - 4 \ge  42 31. | 3x - 4 | \le  8 32. | x - 4 | \ge  8 33. | 3x - 5 | \ge  13 34. | 3x - 5 | \ge  -13 __ 4 x - 5  \ge  7 __ 4 x - 5  + 1 \le  16


## 1.6 Section Exercises
Graphical For the following exercises, graph the absolute value function. Plot at least five points by hand for each graph. 37. y = | x - 1 | 38. y = | x + 1 | 39. y = | x | + 1 For the following exercises, graph the given functions by hand. 40. y = | x | - 2 41. y = -| x | 42. y = -| x | - 2 43. y = -| x - 3 | - 2 44. f (x) = -| x - 1 | - 2 45. f (x) = -| x + 3 | + 4 46. f (x) = 2| x + 3 | + 1 47. f (x) = 3| x - 2 | + 3 48. f (x) = | 2x - 4 | - 3 49. f (x) = | 3x + 9 | + 2 50. f (x) = -| x - 1 | - 3 51. f (x) = -| x + 4 | -3 52. f (x) =  1 __ 2 | x + 4 | - 3 Technology 53. Use a graphing utility to graph f (x) = 10| x - 2| on the viewing window [0, 4]. Identify the corresponding range. Show the graph. 54. Use a graphing utility to graph f (x) = -100| x| + 100 on the viewing window [-5, 5]. Identify the corresponding range. Show the graph. For the following exercises, graph each function using a graphing utility. Specify the viewing window. 56. f (x) = 4 \times  109 ∣ x - (5 \times  109) ∣ + 2 \times  109 Extensions For the following exercises, solve the inequality. 57. |-2x -  2 __ 3 (x + 1)| + 3 > -1 58. If possible, find all values of a such that there are no x-intercepts for f (x) = 2| x + 1| + a. 59. If possible, find all values of a such that there are no y-intercepts for f (x) = 2| x + 1| + a. Real-World Applications 60. Cities A and B are on the same east-west line. Assume that city A is located at the origin. If the distance from city A to city B is at least 100 miles and x represents the distance from city B to city A, express this using absolute value notation. 61. The true proportion p of people who give a favorable rating to Congress is 8% with a margin of error of 1.5%. Describe this statement using an absolute value equation. 62. Students who score within 18 points of the number 82 will pass a particular test. Write this statement using absolute value notation and use the variable x for the score. 63. A machinist must produce a bearing that is within 0.01 inches of the correct diameter of 5.0 inches. Using x as the diameter of the bearing, write this statement using absolute value notation. 64. The tolerance for a ball bearing is 0.01. If the true diameter of the bearing is to be 2.0 inches and the measured value of the diameter is x inches, express the tolerance using absolute value notation.


## 1.7 Inverse Functions
A reversible heat pump is a climate-control system that is an air conditioner and a heater in a single device. Operated in one direction, it pumps heat out of a house to provide cooling. Operating in reverse, it pumps heat into the building from the outside, even in cool weather, to provide heating. As a heater, a heat pump is several times more efficient than conventional electrical resistance heating. If some physical machines can run in two directions, we might ask whether some of the function “machines” we have been studying can also run backwards. Figure 1 provides a visual representation of this question. In this section, we will consider the reverse nature of functions. x x f ? y y Verifying That Two Functions Are Inverse Functions Suppose a fashion designer traveling to Milan for a fashion show wants to know what the temperature will be. He is not familiar with the Celsius scale. To get an idea of how temperature measurements are related, he asks his assistant, Betty, to convert 75 degrees Fahrenheit to degrees Celsius. She finds the formula C =  5 __ 9 (F - 32) and substitutes 75 for F to calculate  5 __ Knowing that a comfortable 75 degrees Fahrenheit is about 24 degrees Celsius, he sends his assistant the week’s weather forecast from Figure 2 for Milan, and asks her to convert all of the temperatures to degrees Fahrenheit. 30°C | 20°C 26°C | 18°C

Mon

Tue Web

Thu Learning Objectives
In this section, you will:
• Verify inverse functions.
• Determine the domain and range of an inverse function, and restrict the domain of a function to make it one-to-one.
• Find or evaluate the inverse of a function.
• Use the graph of a one-to-one function to graph its inverse function on the same axes.
At first, Betty considers using the formula she has already found to complete the conversions. After all, she knows her algebra, and can easily solve the equation for F after substituting a value for C. For example, to convert 26 degrees Celsius, she could write

__ 9 (F - 32)

__ 5  = F - 32

F = 26 ⋅  9 __ After considering this option for a moment, however, she realizes that solving the equation for each of the temperatures will be awfully tedious. She realizes that since evaluation is easier than solving, it would be much more convenient to have a different formula, one that takes the Celsius temperature and outputs the Fahrenheit temperature. The formula for which Betty is searching corresponds to the idea of an inverse function, which is a function for which the input of the original function becomes the output of the inverse function and the output of the original function becomes the input of the inverse function. Given a function f (x), we represent its inverse as f -1(x), read as “ f inverse of x.” The raised -1 is part of the notation. It is not an exponent; it does not imply a power of -1. In other words, f -1(x) does not mean  1 ___ f (x)  because  1 ___ f (x)  is the reciprocal of f and not the inverse. The “exponent-like” notation comes from an analogy between function composition and multiplication: just as a-1 a = 1 (1 is the identity element for multiplication) for any nonzero number a, so f -1 ∘ f equals the identity function, that is, (f -1 ∘ f )(x) = f -1( f (x)) = f -1 (y) = x This holds for all x in the domain of f. Informally, this means that inverse functions “undo” each other. However, just as zero does not have a reciprocal, some functions do not have inverses. Given a function f (x), we can verify whether some other function g (x) is the inverse of f (x) by checking whether either g ( f (x)) = x or f (g (x)) = x is true. We can test whichever equation is more convenient to work with because they are logically equivalent (that is, if one is true, then so is the other.) For example, y = 4x and y =  1 __ 4 x are inverse functions. (f -1 ∘ f )(x) = f -1 (4x) =  1 __ 4 (4x) = x and (f ∘ f -1)(x) = f   1 __ 4 x  = 4   1 __ 4 x  = x A few coordinate pairs from the graph of the function y = 4x are (-2, -8), (0, 0), and (2, 8). A few coordinate pairs from the graph of the function y =  1 __ 4 x are (-8, -2), (0, 0), and (8, 2). If we interchange the input and output of each coordinate pair of a function, the interchanged coordinate pairs would appear on the graph of the inverse function. inverse function For any one-to-one function f (x) = y, a function f -1 (x) is an inverse function of f if f -1(y) = x. This can also be written as f -1( f (x)) = x for all x in the domain of f . It also follows that f ( f -1(x)) = x for all x in the domain of f -1 if f -1 is the inverse of f . The notation f -1 is read “ f inverse.” Like any other function, we can use any variable name as the input for f -1, so we will often write f -1(x), which we read as “ f inverse of x.” Keep in mind that f -1(x) \neq   1 ___ f (x)  and not all functions have inverses.


**Example  1**

### Identifying an Inverse Function for a Given Input-Output Pair
If for a particular one-to-one function f (2) = 4 and f (5) = 12, what are the corresponding input and output values for the inverse function? Solution The inverse function reverses the input and output quantities, so if f (2) = 4, then f -1 (4) = 2; f (5) = 12, then f -1 (12) = 5. Alternatively, if we want to name the inverse function g, then g (4) = 2 and g (12) = 5. Analysis Notice that if we show the coordinate pairs in a table form, the input and output are clearly reversed. See (x, f (x)) (x, g (x))

**Try It #1**
Given that h-1(6) = 2, what are the corresponding input and output values of the original function h?

**How To…**
Given two functions f (x) and g (x), test whether the functions are inverses of each other. 1. Determine whether f (g(x)) = x or g(f (x)) = x. 2. If both statements are true, then g = f -1 and f = g -1. If either statement is false, then both are false, and g \neq  f -1 and f \neq  g-1.

**Example  2**
Testing Inverse Relationships Algebraically If f (x) =  1 ____ x + 2  and g (x) =  1 __ x  - 2, is g = f -1?

**Solution**
g (f (x)) =  _   1 _ x + 2    - 2

= x + 2 - 2

= x so

g = f -1 and f = g -1 This is enough to answer yes to the question, but we can also verify the other formula.

f (g (x)) =  _  1 __ x  - 2 + 2 

=  1 _  1 __ x  

= x Analysis Notice the inverse operations are in reverse order of the operations from the original function.

**Try It #2**
If f (x) = x^{3} - 4 and g (x) =  \sqrt{x} - 4  , is g = f -1?


**Example  3**
Determining Inverse Relationships for Power Functions If f (x) = x^{3} (the cube function) and g (x) =  1 __ 3 x, is g = f -1? Solution f (g (x)) =  x^{3}

__ 27  \neq  x No, the functions are not inverses. Analysis The correct inverse to the cube is, of course, the cube root  \sqrt{x}  = x^{1}/3 that is, the one-third is an exponent, not a multiplier.

**Try It #3**
If f (x) = (x - 1)^{3} and g (x) =  \sqrt{x}  + 1, is g = f -1? Finding Domain and Range of Inverse Functions The outputs of the function f are the inputs to f -1, so the range of f is also the domain of f -1. Likewise, because the inputs to f are the outputs of f -1, the domain of f is the range of f -1. We can visualize the situation as in Figure 3. Domain of f Range of f b a Range of f –1 Domain of f –1 f –1(x) f (x) When a function has no inverse function, it is possible to create a new function where that new function on a limited domain does have an inverse function. For example, the inverse of f (x) = \sqrt{x}  is f -1(x) = x^{2}, because a square “undoes” a square root; but the square is only the inverse of the square root on the domain [0, \infty ), since that is the range of f (x) = \sqrt{x} . We can look at this problem from the other side, starting with the square (toolkit quadratic) function f (x) = x^{2}. If we want to construct an inverse to this function, we run into a problem, because for every given output of the quadratic function, there are two corresponding inputs (except when the input is 0). For example, the output 9 from the quadratic function corresponds to the inputs 3 and –3. But an output from a function is an input to its inverse; if this inverse input corresponds to more than one inverse output (input of the original function), then the “inverse” is not a function at all! To put it differently, the quadratic function is not a one-to-one function; it fails the horizontal line test, so it does not have an inverse function. In order for a function to have an inverse, it must be a one-to-one function. In many cases, if a function is not one-to-one, we can still restrict the function to a part of its domain on which it is one-to-one. For example, we can make a restricted version of the square function f (x) = x^{2} with its domain limited to [0, \infty ), which is a one-to-one function (it passes the horizontal line test) and which has an inverse (the square-root function). If f (x) = (x - 1)^{2} on [1, \infty ), then the inverse function is f -1(x) = \sqrt{x}  + 1. • The domain of f = range of f -1 = [1, \infty ). • The domain of f -1 = range of f = [0, \infty ). Is it possible for a function to have more than one inverse? No. If two supposedly different functions, say, g and h, both meet the definition of being inverses of another function f, then you can prove that g = h. We have just seen that some functions only have inverses if we restrict the domain of the original function. In these cases, there may be more than one way to restrict the domain, leading to different inverses. However, on any one domain, the original function still has only one unique inverse.

domain and range of inverse functions The range of a function f (x) is the domain of the inverse function f -1(x). The domain of f (x) is the range of f -1(x).

**How To…**
Given a function, find the domain and range of its inverse. 1. If the function is one-to-one, write the range of the original function as the domain of the inverse, and write the domain of the original function as the range of the inverse. 2. If the domain of the original function needs to be restricted to make it one-to-one, then this restricted domain becomes the range of the inverse function.

**Example  4**
Finding the Inverses of Toolkit Functions Identify which of the toolkit functions besides the quadratic function are not one-to-one, and find a restricted domain on which each function is one-to-one, if any. The toolkit functions are reviewed in Table 2. We restrict the domain in such a fashion that the function assumes all y-values exactly once. Constant Identity Quadratic Cubic Reciprocal f (x) = c f (x) = x f (x) = x 2 f (x) = x 3 f (x) =  1 _ x  Reciprocal squared Cube root Square root Absolute value f (x) =  1 _ x^{2}  f (x) =  \sqrt{x}  f (x) = \sqrt{x}  f (x) = ∣x∣ Solution The constant function is not one-to-one, and there is no domain (except a single point) on which it could be one-to-one, so the constant function has no meaningful inverse. The absolute value function can be restricted to the domain [0, \infty ), where it is equal to the identity function. The reciprocal-squared function can be restricted to the domain (0, \infty ). Analysis We can see that these functions (if unrestricted) are not one-to-one by looking at their graphs, shown in Figure 4. They both would fail the horizontal line test. However, if a function is restricted to a certain domain so that it passes the horizontal line test, then in that restricted domain, it can have an inverse. x f (x) (a) (b) x f (x)

**Try It #4**
The domain of function f is (1, \infty ) and the range of function f is (-\infty , -2). Find the domain and range of the inverse function.

Finding and Evaluating Inverse Functions Once we have a one-to-one function, we can evaluate its inverse at specific inverse function inputs or construct a complete representation of the inverse function in many cases. Inverting Tabular Functions Suppose we want to find the inverse of a function represented in table form. Remember that the domain of a function is the range of the inverse and the range of the function is the domain of the inverse. So we need to interchange the domain and range. Each row (or column) of inputs becomes the row (or column) of outputs for the inverse function. Similarly, each row (or column) of outputs becomes the row (or column) of inputs for the inverse function.

**Example  5**

### Interpreting the Inverse of a Tabular Function
A function f (t) is given in Table 3, showing distance in miles that a car has traveled in t minutes. Find and interpret f -1(70). t (minutes) f (t) (miles) Solution The inverse function takes an output of f and returns an input for f. So in the expression f -1(70), 70 is an output value of the original function, representing 70 miles. The inverse will return the corresponding input of the original function f, 90 minutes, so f -1(70) = 90. The interpretation of this is that, to drive 70 miles, it took 90 minutes. Alternatively, recall that the definition of the inverse was that if f (a) = b, then f -1(b) = a. By this definition, if we are given f -1(70) = a, then we are looking for a value a so that f (a) = 70. In this case, we are looking for a t so that f (t) = 70, which is when t = 90.

**Try It #5**
Using Table 4, find and interpret a. f (60), and b. f -1(60). t (minutes) f (t) (miles) Evaluating the Inverse of a Function, Given a Graph of the Original Function We saw in Functions and Function Notation that the domain of a function can be read by observing the horizontal extent of its graph. We find the domain of the inverse function by observing the vertical extent of the graph of the original function, because this corresponds to the horizontal extent of the inverse function. Similarly, we find the range of the inverse function by observing the horizontal extent of the graph of the original function, as this is the vertical extent of the inverse function. If we want to evaluate an inverse function, we find its input within its domain, which is all or part of the vertical axis of the original function’s graph.

**How To…**
Given the graph of a function, evaluate its inverse at specific points. 1. Find the desired input on the y-axis of the given graph. 2. Read the inverse function’s output from the x-axis of the given graph.


**Example  6**

### Evaluating a Function and Its Inverse from a Graph at Specific Points
A function g(x) is given in Figure 5. Find g(3) and g-1(3). g(x) x Solution To evaluate g(3), we find 3 on the x-axis and find the corresponding output value on the y-axis. The point (3, 1) tells us that g(3) = 1. To evaluate g -1(3), recall that by definition g -1(3) means the value of x for which g(x) = 3. By looking for the output value 3 on the vertical axis, we find the point (5, 3) on the graph, which means g(5) = 3, so by definition, g -1(3) = 5. See Figure 6. g(x) x

**Try It #6**
Using the graph in Figure 6, a. find g-1(1), and b. estimate g-1(4). Finding Inverses of Functions Represented by Formulas Sometimes we will need to know an inverse function for all elements of its domain, not just a few. If the original function is given as a formula— for example, y as a function of x— we can often find the inverse function by solving to obtain x as a function of y.

**How To…**
Given a function represented by a formula, find the inverse. 1. Make sure f is a one-to-one function. 2. Solve for x. 3. Interchange x and y.

**Example  7**
Inverting the Fahrenheit-to-Celsius Function Find a formula for the inverse function that gives Fahrenheit temperature as a function of Celsius temperature. C =  5 __ 9 (F - 32)


**Solution**
C =  5 __ 9  (F - 32)

C ⋅  9 __ 5  = F - 32

F =  9 __ 5 C + 32 By solving in general, we have uncovered the inverse function. If

C = h(F) =  5 __ 9 (F - 32), then

F = h-1(C) =  9 __ In this case, we introduced a function h to represent the conversion because the input and output variables are descriptive, and writing C-1 could get confusing.

**Try It #7**
Solve for x in terms of y given y =  1 __ 3 (x - 5)

**Example  8**

### Solving to Find an Inverse Function
Find the inverse of the function f (x) =  2 ____ x - 3  + 4.

**Solution**
y =  2 ____ x - 3  + 4 Set up an equation.

y - 4 =  2 _____ x - 3  Subtract 4 from both sides.

x - 3 =  2 ____ y - 4  Multiply both sides by x - 3 and divide by y - 4.

x =  2 ____ y - 4  + 3 Add 3 to both sides. So f -1 (y) =  _____ y - 4 + 3 or f -1 (x) =  2 ____ x - 4  + 3. Analysis The domain and range of f exclude the values 3 and 4, respectively. f and f -1 are equal at two points but are not the same function, as we can see by creating Table 5. x f -1(y) f (x) y

**Example  9**

### Solving to Find an Inverse with Radicals
Find the inverse of the function f (x) = 2 + \sqrt{x} - 4 . Solution y = 2 + \sqrt{x} - 4 

(y - 2)^{2} = x - 4

x = (y - 2)^{2} + 4 So f -1 (x) = (x - 2)^{2} + 4. The domain of f is [4, \infty ). Notice that the range of f is [2, \infty ), so this means that the domain of the inverse function f -1 is also [2, \infty ). Analysis The formula we found for f -1(x) looks like it would be valid for all real x. However, f -1 itself must have an inverse (namely, f) so we have to restrict the domain of f -1 to [2, \infty ) in order to make f -1 a one-to-one function. This domain of f -1 is exactly the range of f.


**Try It #8**
What is the inverse of the function f (x) = 2 - \sqrt{x}  ? State the domains of both the function and the inverse function. Finding Inverse Functions and Their Graphs Now that we can find the inverse of a function, we will explore the graphs of functions and their inverses. Let us return to the quadratic function f (x) = x^{2} restricted to the domain [0, \infty ), on which this function is one-to-one, and graph it as in Figure 7. x f (x) Restricting the domain to [0, \infty ) makes the function one-to-one (it will obviously pass the horizontal line test), so it has an inverse on this restricted domain. We already know that the inverse of the toolkit quadratic function is the square root function, that is, f -1(x) = \sqrt{x} . What happens if we graph both f and f -1 on the same set of axes, using the x-axis for the input to both f and f -1 ? We notice a distinct relationship: The graph of f -1(x) is the graph of f (x) reflected about the diagonal line y = x, which we will call the identity line, shown in Figure 8. x y f (x) y = x f –1(x) This relationship will be observed for all one-to-one functions, because it is a result of the function and its inverse swapping inputs and outputs. This is equivalent to interchanging the roles of the vertical and horizontal axes.


**Example  10**
Finding the Inverse of a Function Using Reflection about the Identity Line Given the graph of f (x) in Figure 9, sketch a graph of f -1(x). x y Solution This is a one-to-one function, so we will be able to sketch an inverse. Note that the graph shown has an apparent domain of (0, \infty ) and range of (-\infty , \infty ), so the inverse will have a domain of (-\infty , \infty ) and range of (0, \infty ). If we reflect this graph over the line y = x, the point (1, 0) reflects to (0, 1) and the point (4, 2) reflects to (2, 4). Sketching the inverse on the same axes as the original graph gives Figure 10. x y f (x) y = x f –1(x)

**Try It #9**
Draw graphs of the functions f and f -1 from Example 8. Is there any function that is equal to its own inverse? Yes. If f = f -1, then f (f (x)) = x, and we can think of several functions that have this property. The identity function does, and so does the reciprocal function, because  1 _  1 _ x   = x Any function f (x) = c - x, where c is a constant, is also equal to its own inverse. Access these online resources for additional instruction and practice with inverse functions. • Inverse Functions (http://openstaxcollege.org/l/inversefunction) • Inverse Function Values Using Graph (http://openstaxcollege.org/l/inversfuncgraph) • Restricting the Domain and Finding the Inverse (http://openstaxcollege.org/l/restrictdomain)

1.7 Section EXERCISES Verbal 1. Describe why the horizontal line test is an effective way to determine whether a function is one-to-one? 2. Why do we restrict the domain of the function f (x) = x^{2} to find the function’s inverse? 3. Can a function be its own inverse? Explain. 4. Are one-to-one functions either always increasing or always decreasing? Why or why not? 5. How do you find the inverse of a function algebraically? Algebraic 6. Show that the function f (x) = a - x is its own inverse for all real numbers a. For the following exercises, find f -1(x) for each function. 7. f (x) = x + 3 8. f (x) = x + 5 9. f (x) = 2 - x 10. f (x) = 3 - x 11. f (x) =  x _____ x + 2  12. f (x) =  2x + 3 ______ 5x + 4  For the following exercises, find a domain on which each function f is one-to-one and non-decreasing. Write the domain in interval notation. Then find the inverse of f restricted to that domain. 13. f (x) = (x + 7)^{2} 14. f (x) = (x - 6)^{2} 15. f (x) = x^{2} - 5 16. Given f (x) =  x __ 2 + x  and g(x) =  2x _____ 1 - x : a. Find f (g(x)) and g (f (x)). b. What does the answer tell us about the relationship between f (x) and g(x)? For the following exercises, use function composition to verify that f (x) and g(x) are inverse functions. 17. f (x) =  \sqrt{x} - 1  and g (x) = x^{3} + 1 18. f (x) = -3x + 5 and g (x) =  x - 5 _____ -3  Graphical For the following exercises, use a graphing utility to determine whether each function is one-to-one. 19. f (x) = \sqrt{x}  20. f (x) =  \sqrt{3x} + 1  21. f (x) = -5x + 1 22. f (x) = x^{3} - 27 For the following exercises, determine whether the graph represents a one-to-one function. x y f x y f


## 1.7 Section Exercises
For the following exercises, use the graph of f shown in Figure 11. x y f 25. Find f (0). 26. Solve f (x) = 0. 28. Solve f -1(x) = 0. For the following exercises, use the graph of the one-to-one function shown in Figure 12. x y f 29. Sketch the graph of f -1. 30. Find f (6) and f -1(2). 31. If the complete graph of f is shown, find the domain of f. 32. If the complete graph of f is shown, find the range of f. Numeric For the following exercises, evaluate or solve, assuming that the function f is one-to-one. 33. If f (6) = 7, find f -1(7). 34. If f (3) = 2, find f -1(2). 35. If f -1(-4) = -8, find f (-8). 36. If f -1(-2) = -1, find f (-1). For the following exercises, use the values listed in Table 6 to evaluate or solve. x f (x) 37. Find f (1). 38. Solve f (x) = 3. 40. Solve f -1(x) = 7. 41. Use the tabular representation of f in Table 7 to create a table for f -1(x). x f (x)

Technology For the following exercises, find the inverse function. Then, graph the function and its inverse. 42. f (x) =  3 _____ x - 2  43. f (x) = x 3 - 1 44. Find the inverse function of f (x) =  1 _ x - 1 . Use a graphing utility to find its domain and range. Write the domain and range in interval notation. Real-World Applications 45. To convert from x degrees Celsius to y degrees Fahrenheit, we use the formula f (x) =  9 __ Find the inverse function, if it exists, and explain its meaning. 46. The circumference C of a circle is a function of its radius given by C(r) = 2\pi r. Express the radius of a circle as a function of its circumference. Call this function r(C). Find r(36\pi ) and interpret its meaning. 47. A car travels at a constant speed of 50 miles per hour. The distance the car travels in miles is a function of time, t, in hours given by d(t) = 50t. Find the inverse function by expressing the time of travel in terms of the distance traveled. Call this function t(d). Find t(180) and interpret its meaning.


### Key Terms
absolute maximum the greatest value of a function over an interval absolute minimum the lowest value of a function over an interval absolute value equation an equation of the form ∣A∣ = B, with B \ge  0; it will have solutions when A = B or A = -B absolute value inequality a relationship in the form ∣A∣ < B, ∣A∣ \le  B, ∣A∣ > B, or ∣A∣ \ge  B average rate of change the difference in the output values of a function found for two values of the input divided by the difference between the inputs composite function the new function formed by function composition, when the output of one function is used as the input of another decreasing function a function is decreasing in some open interval if f (b) < f (a) for any two input values a and b in the given interval where b > a dependent variable an output variable domain the set of all possible input values for a relation even function a function whose graph is unchanged by horizontal reflection, f (x) = f (-x), and is symmetric about the y-axis function a relation in which each input value yields a unique output value horizontal compression a transformation that compresses a function’s graph horizontally, by multiplying the input by a constant b > 1 horizontal line test a method of testing whether a function is one-to-one by determining whether any horizontal line intersects the graph more than once horizontal reflection a transformation that reflects a function’s graph across the y-axis by multiplying the input by -1 horizontal shift a transformation that shifts a function’s graph left or right by adding a positive or negative constant to the input horizontal stretch a transformation that stretches a function’s graph horizontally by multiplying the input by a constant 0 < b < 1 increasing function a function is increasing in some open interval if f (b) > f (a) for any two input values a and b in the given interval where b > a independent variable an input variable input each object or value in a domain that relates to another object or value by a relationship known as a function interval notation a method of describing a set that includes all numbers between a lower limit and an upper limit; the lower and upper values are listed between brackets or parentheses, a square bracket indicating inclusion in the set, and a parenthesis indicating exclusion inverse function for any one-to-one function f (x), the inverse is a function f -1(x) such that f -1(f (x)) = x for all x in the domain of f; this also implies that f ( f -1(x)) = x for all x in the domain of f -1 local extrema collectively, all of a function’s local maxima and minima local maximum a value of the input where a function changes from increasing to decreasing as the input value increases. local minimum a value of the input where a function changes from decreasing to increasing as the input value increases. odd function a function whose graph is unchanged by combined horizontal and vertical reflection, f (x) = - f (-x), and is symmetric about the origin one-to-one function a function for which each value of the output is associated with a unique input value output each object or value in the range that is produced when an input value is entered into a function piecewise function a function in which more than one formula is used to define the output range the set of output values that result from the input values in a relation

rate of change the change of an output quantity relative to the change of the input quantity relation a set of ordered pairs set-builder notation a method of describing a set by a rule that all of its members obey; it takes the form {x ∣ statement about x} vertical compression a function transformation that compresses the function’s graph vertically by multiplying the output by a constant 0 < a < 1 vertical line test a method of testing whether a graph represents a function by determining whether a vertical line intersects the graph no more than once vertical reflection a transformation that reflects a function’s graph across the x-axis by multiplying the output by -1 vertical shift a transformation that shifts a function’s graph up or down by adding a positive or negative constant to the output vertical stretch a transformation that stretches a function’s graph vertically by multiplying the output by a constant a > 1 Key Equations Constant function f (x) = c, where c is a constant Identity function f (x) = x Absolute value function f (x) = ∣x∣ Quadratic function f (x) = x^{2} Cubic function f (x) = x^{3} Reciprocal function f (x) =  1 _ x  Reciprocal squared function f (x) =  1 _ x^{2}  Square root function f (x) = \sqrt{x}  Cube root function f (x) =  \sqrt{x}  Average rate of change  \Delta y _ \Delta x  =  f (x^{2}) - f (x^{1}) _ x^{2} - x^{1}  Composite function (f ∘ g)(x) = f (g(x)) Vertical shift g(x) = f (x) + k (up for k > 0) Horizontal shift g(x) = f (x - h) (right for h > 0) Vertical reflection g(x) = -f (x) Horizontal reflection g(x) = f (-x) Vertical stretch g(x) = af (x) (a > 0) Vertical compression g(x) = af (x) (0 < a < 1) Horizontal stretch g(x) = f (bx) (0 < b < 1) Horizontal compression g(x) = f (bx) (b > 1)


### Key Concepts
• A relation is a set of ordered pairs. A function is a specific type of relation in which each domain value, or input, leads to exactly one range value, or output. See Example 1 and Example 2. • Function notation is a shorthand method for relating the input to the output in the form y = f (x). See Example 3 and Example 4. • In tabular form, a function can be represented by rows or columns that relate to input and output values. See

**Example 5** — .
• To evaluate a function, we determine an output value for a corresponding input value. Algebraic forms of a function can be evaluated by replacing the input variable with a given value. See Example 6 and Example 7. • To solve for a specific function value, we determine the input values that yield the specific output value. See

**Example 8** — .
• An algebraic form of a function can be written from an equation. See Example 9 and Example 10. • Input and output values of a function can be identified from a table. See Example 11. • Relating input values to output values on a graph is another way to evaluate a function. See Example 12. • A function is one-to-one if each output value corresponds to only one input value. See Example 13. • A graph represents a function if any vertical line drawn on the graph intersects the graph at no more than one point. See Example 14. • The graph of a one-to-one function passes the horizontal line test. See Example 15. 1.2 Domain and Range • The domain of a function includes all real input values that would not cause us to attempt an undefined mathematical operation, such as dividing by zero or taking the square root of a negative number. • The domain of a function can be determined by listing the input values of a set of ordered pairs. See Example 1. • The domain of a function can also be determined by identifying the input values of a function written as an equation. See Example 2, Example 3, and Example 4. • Interval values represented on a number line can be described using inequality notation, set-builder notation, and interval notation. See Example 5. • For many functions, the domain and range can be determined from a graph. See Example 6 and Example 7. • An understanding of toolkit functions can be used to find the domain and range of related functions. See Example 8,

**Example 9** — , and Example 10.
• A piecewise function is described by more than one formula. See Example 11 and Example 12. • A piecewise function can be graphed using each algebraic formula on its assigned subdomain. See Example 13. 1.3 Rates of Change and Behavior of Graphs • A rate of change relates a change in an output quantity to a change in an input quantity. The average rate of change is determined using only the beginning and ending data. See Example 1. • Identifying points that mark the interval on a graph can be used to find the average rate of change. See Example 2. • Comparing pairs of input and output values in a table can also be used to find the average rate of change. See

**Example 3** — .
• An average rate of change can also be computed by determining the function values at the endpoints of an interval described by a formula. See Example 4 and Example 5. • The average rate of change can sometimes be determined as an expression. See Example 6. • A function is increasing where its rate of change is positive and decreasing where its rate of change is negative. See

**Example 7** — .
• A local maximum is where a function changes from increasing to decreasing and has an output value larger (more positive or less negative) than output values at neighboring input values.

• A local minimum is where the function changes from decreasing to increasing (as the input increases) and has an output value smaller (more negative or less positive) than output values at neighboring input values. • Minima and maxima are also called extrema. • We can find local extrema from a graph. See Example 8 and Example 9. • The highest and lowest points on a graph indicate the maxima and minima. See Example 10. 1.4 Composition of Functions • We can perform algebraic operations on functions. See Example 1. • When functions are combined, the output of the first (inner) function becomes the input of the second (outer) function. • The function produced by combining two functions is a composite function. See Example 2 and Example 3. • The order of function composition must be considered when interpreting the meaning of composite functions. See Example 4. • A composite function can be evaluated by evaluating the inner function using the given input value and then evaluating the outer function taking as its input the output of the inner function. • A composite function can be evaluated from a table. See Example 5. • A composite function can be evaluated from a graph. See Example 6. • A composite function can be evaluated from a formula. See Example 7. • The domain of a composite function consists of those inputs in the domain of the inner function that correspond to outputs of the inner function that are in the domain of the outer function. See Example 8 and Example 9. • Just as functions can be combined to form a composite function, composite functions can be decomposed into simpler functions. • Functions can often be decomposed in more than one way. See Example 10. 1.5 Transformation of Functions • A function can be shifted vertically by adding a constant to the output. See Example 1 and Example 2. • A function can be shifted horizontally by adding a constant to the input. See Example 3, Example 4, and Example 5. • Relating the shift to the context of a problem makes it possible to compare and interpret vertical and horizontal shifts. See Example 6. • Vertical and horizontal shifts are often combined. See Example 7 and Example 8. • A vertical reflection reflects a graph about the x-axis. A graph can be reflected vertically by multiplying the output by –1. • A horizontal reflection reflects a graph about the y-axis. A graph can be reflected horizontally by multiplying the input by –1. • A graph can be reflected both vertically and horizontally. The order in which the reflections are applied does not affect the final graph. See Example 9. • A function presented in tabular form can also be reflected by multiplying the values in the input and output rows or columns accordingly. See Example 10. • A function presented as an equation can be reflected by applying transformations one at a time. See Example 11. • Even functions are symmetric about the y-axis, whereas odd functions are symmetric about the origin. • Even functions satisfy the condition f (x) = f (-x). • Odd functions satisfy the condition f (x) = -f (-x). • A function can be odd, even, or neither. See Example 12. • A function can be compressed or stretched vertically by multiplying the output by a constant. See Example 13,

**Example 14** — , and Example 15.
• A function can be compressed or stretched horizontally by multiplying the input by a constant. See Example 16,

**Example 17** — , and Example 18.

• The order in which different transformations are applied does affect the final function. Both vertical and horizontal transformations must be applied in the order given. However, a vertical transformation may be combined with a horizontal transformation in any order. See Example 19 and Example 20. 1.6 Absolute Value Functions • The absolute value function is commonly used to measure distances between points. See Example 1. • Applied problems, such as ranges of possible values, can also be solved using the absolute value function. See

**Example 2** — .
• The graph of the absolute value function resembles a letter V. It has a corner point at which the graph changes direction. See Example 3. • In an absolute value equation, an unknown variable is the input of an absolute value function. • If the absolute value of an expression is set equal to a positive number, expect two solutions for the unknown variable. See Example 4. • An absolute value equation may have one solution, two solutions, or no solutions. See Example 5. • An absolute value inequality is similar to an absolute value equation but takes the form ∣A∣ < B, ∣A∣ \le  B, ∣A∣ > B, or ∣A∣ \ge  B. It can be solved by determining the boundaries of the solution set and then testing which segments are in the set. See Example 6. • Absolute value inequalities can also be solved graphically. See Example 7. 1.7 Inverse Functions • If g(x) is the inverse of f (x), then g(f (x)) = f (g(x)) = x. See Example 1, Example 2, and Example 3. • Each of the toolkit functions has an inverse. See Example 4. • For a function to have an inverse, it must be one-to-one (pass the horizontal line test). • A function that is not one-to-one over its entire domain may be one-to-one on part of its domain. • For a tabular function, exchange the input and output rows to obtain the inverse. See Example 5. • The inverse of a function can be determined at specific points on its graph. See Example 6. • To find the inverse of a formula, solve the equation y = f (x) for x as a function of y. Then exchange the labels x and y. See Example 7, Example 8, and Example 9. • The graph of an inverse function is the reflection of the graph of the original function across the line y = x. See

**Example 10** — .

Functions and Function Notation For the following exercises, determine whether the relation is a function. 1. {(a, b), (c, d), (e, d)} 3. y 2 + 4 = x, for x the independent variable and y the dependent variable 4. Is the graph in Figure 1 a function? f y For the following exercises, evaluate the function at the indicated values: f (-3); f (2); f (-a); -f (a); f (a + h). 5. f (x) = -2x 2 + 3x f (x) = 2∣3 x - 1∣ For the following exercises, determine whether the functions are one-to-one. 7. f (x) = -3x + 5 8. f (x) = ∣x - 3∣ For the following exercises, use the vertical line test to determine if the relation whose graph is provided is a function. x y x y x y For the following exercises, graph the functions. 12. f (x) = ∣x + 1∣ 13. f (x) = x 2 - 2 x

For the following exercises, use Figure 2 to approximate the values. x y 16. If f (x) = -2, then solve for x. 17. If f (x) = 1, then solve for x. For the following exercises, use the function h(t) = -16t 2 + 80t to find the values. 18.  h(2) - h(1) __ 2 - 1  19.  h(a) - h(1) __ a - 1  Domain and Range For the following exercises, find the domain of each function, expressing answers using interval notation. 20. f (x) =  _ 3x + 2  21. f (x) =  x - 3 ___________ x 2 - 4x - 12  22. f (x) =  \sqrt{x} - 6  _ \sqrt{x} - 4   23. Graph this piecewise function: f (x) = { x + 1 x < -2

-2x - 3 x \ge  -2 Rates of Change and Behavior of Graphs For the following exercises, find the average rate of change of the functions from x = 1 to x = 2. 24. f (x) = 4x - 3 25. f (x) = 10x 2 + x 26. f (x) = - 2 _ x 2  For the following exercises, use the graphs to determine the intervals on which the functions are increasing, decreasing, or constant. x y x y x y 30. Find the local minimum of the function graphed in Exercise 27. 31. Find the local extrema for the function graphed in Exercise 28.

32. For the graph in Figure 3, the domain of the function is [-3, 3]. The range is [-10, 10]. Find the absolute minimum of the function on this interval. x y 33. Find the absolute maximum of the function graphed in Figure 3. Composition of Functions For the following exercises, find (f ∘ g)(x) and (g ∘ f)(x) for each pair of functions. 34. f (x) = 4 - x, g(x) = -4x 35. f (x) = 3x + 2, g(x) = 5 - 6x 36. f (x) = x 2 + 2x, g(x) = 5x + 1 37. f (x) = \sqrt{x} + 2 , g(x) =  1 _ x  38. f (x) =  x + 3 _____ , g(x) = \sqrt{1} - x  For the following exercises, find (f ∘ g) and the domain for (f ∘ g)(x) for each pair of functions. 39. f (x) =  x + 1 _ x + 4 , g(x) =  1 _ x  40. f (x) =  1 _ x + 3 , g(x) =  1 _ x - 9  41. f (x) =  1 _ x , g(x) = \sqrt{x}  42. f (x) =  _ x^{2} - 1 , g(x) = \sqrt{x} + 1  For the following exercises, express each function H as a composition of two functions f and g where H(x) = (f ∘ g)(x). 43. H(x) = \sqrt{_______}  2x - 1 ______ 3x + 4   44. H(x) =  _ (3x 2 - 4)-3  Transformation of Functions For the following exercises, sketch a graph of the given function. 45. f (x) = (x - 3)^{2} 46. f (x) = (x + 4)^{3} 47. f (x) = \sqrt{x}  + 5 48. f (x) = -x 3 49. f (x) =  \sqrt{-x}  50. f (x) = 5\sqrt{-x}  - 4 51. f (x) = 4[∣x - 2∣ - 6] 52. f (x) = -(x + 2)^{2} - 1 For the following exercises, sketch the graph of the function g if the graph of the function f is shown in Figure 4. x y 53. g(x) = f (x - 1) 54. g(x) = 3f (x)

For the following exercises, write the equation for the standard function represented by each of the graphs below. x y x y For the following exercises, determine whether each function below is even, odd, or neither. 57. f (x) = 3x 4 58. g(x) = \sqrt{x}  59. h(x) =  1 _ x  + 3x For the following exercises, analyze the graph and determine whether the graphed function is even, odd, or neither. x y x y x y Absolute Value Functions For the following exercises, write an equation for the transformation of f (x) = | x |. x y x y x y For the following exercises, graph the absolute value function. 66. f (x) = | x - 5 | 67. f (x) = -| x - 3 | 68. f (x) = | 2x - 4 |

For the following exercises, solve the absolute value equation. 69. | x + 4 | = 18 __ 3 x + 5  =   3 __ 4 x - 2  For the following exercises, solve the inequality and express the solution using interval notation. 71. | 3x - 2 | < 7 __ 3 x - 2  \le  7 Inverse Functions For the following exercises, find f -1(x) for each function. 73. f (x) = 9 + 10x 74. f (x) =  x _ x + 2  For the following exercise, find a domain on which the function f is one-to-one and non-decreasing. Write the domain in interval notation. Then find the inverse of f restricted to that domain. 75. f (x) = x 2 + 1 76. Given f (x) = x 3 - 5 and g(x) =  \sqrt{x} + 5  : a. Find f (g(x)) and g(f (x)). b. What does the answer tell us about the relationship between f (x) and g(x)? For the following exercises, use a graphing utility to determine whether each function is one-to-one. 77. f (x) =  1 _ x  78. f (x) = -3x 2 + x 79. If f (5) = 2, find f -1(2). 80. If f (1) = 4, find f -1(4).

For the following exercises, determine whether each of the following relations is a function. 1. y = 2x + 8 For the following exercises, evaluate the function f (x) = -3x 2 + 2x at the given input. 3. f (-2) 4. f (a) 5. Show that the function f (x) = -2(x - 1)^{2} + 3 is not one-to-one. 6. Write the domain of the function f (x) = \sqrt{3} - x  in interval notation. 7. Given f (x) = 2x 2 - 5x, find f (a + 1) - f (1). 8. Graph the function f (x) = { x + 1 if -2 < x < 3 -x if x \ge  3 9. Find the average rate of change of the function f (x) = 3 - 2x 2 + x by finding  f (b) - f (a) _ b - a . For the following exercises, use the functions f (x) = 3 - 2x 2 + x and g(x) = \sqrt{x}  to find the composite functions. 10. (g ∘ f )(x) 11. (g ∘ f )(1) 12. Express H(x) =  \sqrt{5x} 2 - 3x  as a composition of two functions, f and g, where (f ∘ g)(x) = H(x). For the following exercises, graph the functions by translating, stretching, and/or compressing a toolkit function. 13. f (x) = \sqrt{x} + 6  - 1 14. f (x) =  1 _ x + 2  - 1 For the following exercises, determine whether the functions are even, odd, or neither. 15. f (x) = - 5 _ x^{2}  + 9x 6 16. f (x) = - 5 _ x 3  + 9x 5 17. f (x) =  1 _ x  18. Graph the absolute value function f (x) = -2| x - 1 | + 3. 19. Solve | 2x - 3 | = 17. 20. Solve -  1 _ 3 x - 3  \ge  17. Express the solution in interval notation. For the following exercises, find the inverse of the function. 21. f (x) = 3x - 5 22. f (x) =  4 _ x + 7 

For the following exercises, use the graph of g shown in Figure 1. x y 23. On what intervals is the function increasing? 24. On what intervals is the function decreasing? 25. Approximate the local minimum of the function. Express the answer as an ordered pair. 26. Approximate the local maximum of the function. Express the answer as an ordered pair. For the following exercises, use the graph of the piecewise function shown in Figure 2. x y f 27. Find f (2). 28. Find f (-2). 29. Write an equation for the piecewise function. For the following exercises, use the values listed in Table 1. x F (x) 30. Find F (6). 31. Solve the equation F (x) = 5. 32. Is the graph increasing or decreasing on its domain? 33. Is the function represented by the graph one-to-one? 35. Given f (x) = -2x + 11, find f -1(x).
