# Functions

## Introduction

---
Toward the end of the twentieth century, the values of stocks of internet and technology companies rose dramatically. As a result, the Standard and Poor’s stock market average rose as well. Figure 1 tracks the value of that initial investment of just under $100 over the 40 years. It shows that an investment that was worth less than $500 until about 1995 skyrocketed up to about $1,100 by the beginning of 2000. That five-year period became known as the “dot-com bubble” because so many internet startups were formed. As bubbles tend to do, though, the dot-com bubble eventually burst. Many companies grew too fast and then suddenly went out of business. The result caused the sharp decline represented on the graph beginning at the end of 2000. Notice, as we consider this example, that there is a definite relationship between the year and stock market average. For any year we choose, we can determine the corresponding value of the stock market average. In this chapter, we will explore these kinds of relationships and their properties. 1.1 Functions and Function Notation 1.2 Domain and Range 1.3 Rates of Change and Behavior of Graphs 1.4 Composition of Functions 1.5 Transformation of Functions 1.6 Absolute Value Functions 1.7 Inverse Functions

## 1.1 Functions and Function Notation

---
A jetliner changes altitude as its distance from the starting point of a flight increases. The weight of a growing child increases with time. In each case, one quantity depends on another. There is a relationship between the two quantities that we can describe, analyze, and use to make predictions. In this section, we will analyze such relationships. Determining Whether a Relation Represents a Function A relation is a set of ordered pairs. The set of the first components of each ordered pair is called the domain and the set of the second components of each ordered pair is called the range. Consider the following set of ordered pairs. The first numbers in each pair are the first five natural numbers. The second number in each pair is twice that of the first. The domain is {1, 2, 3, 4, 5}. The range is {2, 4, 6, 8, 10}. Note that each value in the domain is also known as an input value, or independent variable, and is often labeled with the lowercase letter x. Each value in the range is also known as an output value, or dependent variable, and is often labeled lowercase letter y. A function f is a relation that assigns a single value in the range to each value in the domain. In other words, no x-values are repeated. For our example that relates the first five natural numbers to numbers double their values, this relation is a function because each element in the domain, {1, 2, 3, 4, 5}, is paired with exactly one element in the range, Now let’s consider the set of ordered pairs that relates the terms “even” and “odd” to the first five natural numbers. It would appear as {(odd, 1), (even, 2), (odd, 3), (even, 4), (odd, 5)} Notice that each element in the domain, {even, odd} is not paired with exactly one element in the range, {1, 2, 3, 4, 5}. For example, the term “odd” corresponds to three values from the domain, {1, 3, 5} and the term “even” corresponds to two values from the range, {2, 4}. This violates the definition of a function, so this relation is not a function. Figure 1 compares relations that are functions and not functions. Relation is a Function Inputs Outputs Inputs Outputs Inputs Outputs Relation is a Function Relation is NOT a Function (a) (b) (c) p q r m n p q r x y z p q x y z ( b ) This relationship is also a function. In this case, each input is associated with a single output. ( c ) This relationship is not a function because input q is associated with two different outputs. function A function is a relation in which each possible input value leads to exactly one output value. We say “the output is a function of the input.” The input values make up the domain, and the output values make up the range. Learning Objectives
In this section, you will:
•
Determine whether a relation represents a function. • Find the value of a function. • Determine whether a function is one-to-one. • Use the vertical line test to identify functions. • Graph the functions listed in the library of functions.

---
### 💡 **How To…**
Given a relationship between two quantities, determine whether the relationship is a function. 1. Identify the input values. 2. Identify the output values. 3. If each input value leads to only one output value, classify the relationship as a function. If any input value leads to two or more outputs, do not classify the relationship as a function.

---
### 📐 **Example  1**: Determining If Menu Price Lists Are Functions

The coffee shop menu, shown in Figure 2 consists of items and their prices. a. Is price a function of the item? b. Is the item a function of the price? Menu Item Price

**Solution**

a. Let’s begin by considering the input as the items on the menu. The output values are then the prices. See Figure 3. Menu Item Price Each item on the menu has only one price, so the price is a function of the item. b. Two items on the menu have the same price. If we consider the prices to be the input values and the items to be the output, then the same input value could have more than one output associated with it. See Figure 4. Menu Item Price Therefore, the item is a not a function of price.

---
### 📐 **Example  2**: Determining If Class Grade Rules Are Functions

In a particular math class, the overall percent grade corresponds to a grade point average. Is grade point average a function of the percent grade? Is the percent grade a function of the grade point average? Table 1 shows a possible rule for assigning grade points.

Percent grade Grade point average 0.0 1.0 1.5 2.0 2.5 3.0 3.5 4.0

**Solution**

For any percent grade earned, there is an associated grade point average, so the grade point average is a function of the percent grade. In other words, if we input the percent grade, the output is a specific grade point average. In the grading system given, there is a range of percent grades that correspond to the same grade point average. For example, students who receive a grade point average of 3.0 could have a variety of percent grades ranging from 78 all the way to 86. Thus, percent grade is not a function of grade point average

---
### ✏️ **Try It #1**
lists the five greatest baseball players of all time in order of rank. Player Rank Babe Ruth Willie Mays Ty Cobb Walter Johnson Hank Aaron a. Is the rank a function of the player name? b. Is the player name a function of the rank? Using Function Notation Once we determine that a relationship is a function, we need to display and define the functional relationships so that we can understand and use them, and sometimes also so that we can program them into computers. There are various ways of representing functions. A standard function notation is one representation that facilitates working with functions. To represent “height is a function of age,” we start by identifying the descriptive variables h for height and a for age. The letters f, g, and h are often used to represent functions just as we use x, y, and z to represent numbers and A, B, and C to represent sets.

h is f of a We name the function f ; height is a function of age.

h = f (a) We use parentheses to indicate the function input.

f (a) We name the function f ; the expression is read as “f of a.” Remember, we can use any letter to name the function; the notation h(a) shows us that h depends on a. The value a must be put into the function h to get a result. The parentheses indicate that age is input into the function; they do not indicate multiplication. We can also give an algebraic expression as the input to a function. For example f (a + b) means “first add a and b, and the result is the input for the function f. ” The operations must be performed in this order to obtain the correct result. function notation The notation y = f (x) defines a function named f. This is read as “y is a function of x.” The letter x represents the input value, or independent variable. The letter y, or f (x), represents the output value, or dependent variable. 1 http://www.baseball-almanac.com/legendary/lisn¹00.shtml. Accessed 3/24/2014.

---
### 📐 **Example  3**: Using Function Notation for Days in a Month

Use function notation to represent a function whose input is the name of a month and output is the number of days in that month.

**Solution**

The number of days in a month is a function of the name of the month, so if we name the function f, we write days = f (month) or d = f (m). The name of the month is the input to a “rule” that associates a specific number (the output) with each input. 31f (January) output input rule For example, f (March) = 31, because March has 31 days. The notation d = f (m) reminds us that the number of days, d (the output), is dependent on the name of the month, m(the input). Analysis Note that the inputs to a function do not have to be numbers; function inputs can be names of people, labels of geometric objects, or any other element that determines some kind of output. However, most of the functions we will work with in this book will have numbers as inputs and outputs.

---
### 📐 **Example  4**: Interpreting Function Notation

A function N = f (y) gives the number of police officers, N, in a town in year y. What does f (2005) = 300 represent?

**Solution**

When we read f (2005) = 300, we see that the input year is 2005. The value for the output, the number of police officers (N), is 300. Remember N = f (y). The statement f (2005) = 300 tells us that in the year 2005 there were 300 police officers in the town.

---
### ✏️ **Try It #2**
Use function notation to express the weight of a pig in pounds as a function of its age in days d. Instead of a notation such as y = f (x), could we use the same symbol for the output as for the function, such as y = y (x), meaning “y is a function of x?” Yes, this is often done, especially in applied subjects that use higher math, such as physics and engineering. However, in exploring math itself we like to maintain a distinction between a function such as f, which is a rule or procedure, and the output y we get by applying f to a particular input x. This is why we usually use notation such as y = f (x), P = W(d), and so on. Representing Functions Using Tables A common method of representing functions is in the form of a table. The table rows or columns display the corresponding input and output values. In some cases, these values represent all we know about the relationship; other times, the table provides a few select examples from a more complete relationship. number of days in that month. This information represents all we know about the months and days for a given year (that is not a leap year). Note that, in this table, we define a days-in-a-month function f where D = f (m) identifies months by an integer rather than by name. Month number, m (input) Days in month, D (output)

input n and gives the output Q. n Q data available for the heights and ages of children. We can see right away that this table does not represent a function because the same input value, 5 years, has two different output values, 40 in. and 42 in. Age in years, a (input) Height in inches, h (output)

---
### 💡 **How To…**
Given a table of input and output values, determine whether the table represents a function. 1. Identify the input and output values. 2. Check to see if each input value is paired with only one output value. If so, the table represents a function.

---
### 📐 **Example  5**: Identifying Tables that Represent Functions

Which table, Table 6, Table 7, or Table 8, represents a function (if any)?

Input Output

Input Output -3

Input Output

**Solution**

Table 6 and Table 7 define functions. In both, each input value corresponds to exactly one output value. When a table represents a function, corresponding input and output values can also be specified using function notation. The function represented by Table 6 can be represented by writing f (2) = 1, f (5) = 3, and f (8) = 6 Similarly, the statements g (-3) = 5, g (0) = 1, and g (4) = 5 represent the function in table Table 7.

---
### ✏️ **Try It #3**
Does Table 9 represent a function? Input Output

### Finding Input and Output Values of a Function

When we know an input value and want to determine the corresponding output value for a function, we evaluate the function. Evaluating will always produce one result because each input value of a function corresponds to exactly one output value. When we know an output value and want to determine the input values that would produce that output value, we set the output equal to the function’s formula and solve for the input. Solving can produce more than one solution because different input values can produce the same output value. Evaluation of Functions in Algebraic Forms When we have a function in formula form, it is usually a simple matter to evaluate the function. For example, the function f (x) = 5 - 3x 2 can be evaluated by squaring the input value, multiplying by 3, and then subtracting the product from 5.

---
### 💡 **How To…**
Given the formula for a function, evaluate. 1. Replace the input variable in the formula with the value provided. 2. Calculate the result.

---
### 📐 **Example  6**: Evaluating Functions at Specific Values

Evaluate f(x) = x 2 + 3x - 4 at: a. 2 b. a c. a + h d.  f (a + h) - f (a)

__ h

**Solution**

Replace the x in the function with each specified value. a. Because the input value is a number, 2, we can use simple algebra to simplify.

f (2) = 22 + 3(2) - 4

= 4 + 6 - 4

= 6 b. In this case, the input value is a letter so we cannot simplify the answer any further.

f (a) = a² + 3a - 4 c. With an input value of a + h, we must use the distributive property.

f (a + h) = (a + h)² + 3(a + h) - 4

= a² + 2ah + h² + 3a + 3h -4 d. In this case, we apply the input values to the function more than once, and then perform algebraic operations on the result. We already found that

f (a + h) = a² + 2ah + h² + 3a + 3h - 4 and we know that

f(a) = a² + 3a - 4 Now we combine the results and simplify.

 f (a + h) - f(a)

__ h  =  (a² + 2ah + h² + 3a + 3h - 4) - (a² + 3a - 4)

____

h 

=  2ah + h² + 3h

___________ h 

=  h(2a + h + 3)

___________ h  Factor out h.

= 2a + h + 3

Simplify.

---
### 📐 **Example  7**: Evaluating Functions

Given the function h(p) = p² + 2p, evaluate h(4).

**Solution**

To evaluate h(4), we substitute the value 4 for the input variable p in the given function.

h(p) = p² + 2p

h(4) = (4)² +2 (4)

= 24 Therefore, for an input of 4, we have an output of 24.

---
### ✏️ **Try It #4**
Given the function g(m) = √m - 4 . Evaluate g(5).

---
### 📐 **Example  8**: Solving Functions

Given the function h(p) = p² + 2p, solve for h(p) = 3.

**Solution**

h(p) = 3

p² + 2p = 3 Substitute the original function h(p) = p² + 2p.

p² + 2p - 3 = 0 Subtract 3 from each side.

(p + 3)(p - 1) = 0 Factor. If (p + 3)(p - 1) = 0, either (p + 3) = 0 or (p - 1) = 0 (or both of them equal 0). We will set each factor equal to 0 and solve for p in each case.

(p + 3) = 0, p = -3

(p - 1) = 0, p = 1 This gives us two solutions. The output h(p) = 3 when the input is either p = 1 or p = -3. We can also verify by graphing as in Figure 6. The graph verifies that h(1) = h(-3) = 3 and h(4) = 24. p h(p) p h(p)

---
### ✏️ **Try It #5**
Given the function g(m) = √m - 4 , solve g(m) = 2. Evaluating Functions Expressed in Formulas Some functions are defined by mathematical rules or procedures expressed in equation form. If it is possible to express the function output with a formula involving the input quantity, then we can define a function in algebraic form. For example, the equation 2n + 6p = 12 expresses a functional relationship between n and p. We can rewrite it to decide if p is a function of n.

---
### 💡 **How To…**
Given a function in equation form, write its algebraic formula. 1. Solve the equation to isolate the output variable on one side of the equal sign, with the other side as an expression that involves only the input variable. 2. Use all the usual algebraic methods for solving equations, such as adding or subtracting the same quantity to or from both sides, or multiplying or dividing both sides of the equation by the same quantity.

---
### 📐 **Example  9**
Finding an Equation of a Function Express the relationship 2n + 6p = 12 as a function p = f (n), if possible.

**Solution**

To express the relationship in this form, we need to be able to write the relationship where p is a function of n, which means writing it as p = [expression involving n].

2n + 6p = 12

6p = 12 - 2n Subtract 2n from both sides.

p =  12 - 2n _______  Divide both sides by 6 and simplify.

p =  12/6  -  2n ___ 6 

p = 2 -  1/3 n Therefore, p as a function of n is written as

p = f (n) = 2 -  1/3 n Analysis It is important to note that not every relationship expressed by an equation can also be expressed as a function with a formula.

---
### 📐 **Example  10**: Expressing the Equation of a Circle as a Function

Does the equation x² + y² = 1 represent a function with x as input and y as output? If so, express the relationship as a function y = f (x).

**Solution**

First we subtract x² from both sides.

y² = 1 - x² We now try to solve for y in this equation.

y = ± √1 - x² 

= +√1 - x²  and -√1 - x²  We get two outputs corresponding to the same input, so this relationship cannot be represented as a single function y = f (x).

---
### ✏️ **Try It #6**
If x - 8y 3 = 0, express y as a function of x. Are there relationships expressed by an equation that do represent a function but which still cannot be represented by an algebraic formula? Yes, this can happen. For example, given the equation x = y + 2y, if we want to express y as a function of x, there is no simple algebraic formula involving only x that equals y. However, each x does determine a unique value for y, and there are mathematical procedures by which y can be found to any desired accuracy. In this case, we say that the equation gives an implicit (implied) rule for y as a function of x, even though the formula cannot be written explicitly.

### Evaluating a Function Given in Tabular Form

As we saw above, we can represent functions in tables. Conversely, we can use information in tables to write functions, and we can evaluate functions using the tables. For example, how well do our pets recall the fond memories we share with them? There is an urban legend that a goldfish has a memory of 3 seconds, but this is just a myth. Goldfish can remember up to 3 months, while the beta fish has a memory of up to 5 months. And while a puppy’s memory span is no longer than 30 seconds, the adult dog can remember for 5 minutes. This is meager compared to a cat, whose memory span lasts for 16 hours. The function that relates the type of pet to the duration of its memory span is more easily visualized with the use of a table. See Table 10. Pet Memory span in hours Puppy 0.008 Adult dog 0.083 Cat Goldfish Beta fish At times, evaluating a function in table form may be more useful than using equations. Here let us call the function P. The domain of the function is the type of pet and the range is a real number representing the number of hours the pet’s memory span lasts. We can evaluate the function P at the input value of “goldfish.” We would write P(goldfish) = 2160. Notice that, to evaluate the function in table form, we identify the input value and the corresponding output value from the pertinent row of the table. The tabular form for function P seems ideally suited to this function, more so than writing it in paragraph or function form.

---
### 💡 **How To…**
Given a function represented by a table, identify specific output and input values. 1. Find the given input in the row (or column) of input values. 2. Identify the corresponding output value paired with that input value. 3. Find the given output values in the row (or column) of output values, noting every time that output value appears. 4. Identify the input value(s) corresponding to the given output value.

---
### 📐 **Example  11**: Evaluating and Solving a Tabular Function

Using Table 11, a. Evaluate g(3) b. Solve g(n) = 6. n g (n)

**Solution**

a. Evaluating g (3) means determining the output value of the function g for the input value of n = 3. The table output value corresponding to n = 3 is 7, so g (3) = 7. b. Solving g (n) = 6 means identifying the input values, n, that produce an output value of 6. Table 11 shows two solutions: 2 and 4. When we input 2 into the function g, our output is 6. When we input 4 into the function g, our output is also 6. 2 http://www.kgbanswers.com/how-long-is-a-dogs-memory-span/4221590. Accessed 3/24/2014.

---
### ✏️ **Try It #7**
Using Table 11, evaluate g(1). Finding Function Values from a Graph Evaluating a function using a graph also requires finding the corresponding output value for a given input value, only in this case, we find the output value by looking at the graph. Solving a function equation using a graph requires finding all instances of the given output value on the graph and observing the corresponding input value( s ).

---
### 📐 **Example  12**
Reading Function Values from a Graph Given the graph in Figure 7, a. Evaluate f (2). b. Solve f (x) = 4. f (x)

**Solution**

a. To evaluate f (2), locate the point on the curve where x = 2, then read the y-coordinate of that point. The point has coordinates (2, 1), so f (2) = 1. See Figure 8. f (2) = 1 f (x) b. To solve f (x) = 4, we find the output value 4 on the vertical axis. Moving horizontally along the line y = 4, we locate two points of the curve with output value 4: (-1, 4) and (3, 4). These points represent the two solutions to f (x) = 4: -1 or 3. This means f (-1) = 4 and f (3) = 4, or when the input is -1 or 3, the output is 4. See Figure 9. f (x)

---
### ✏️ **Try It #8**
Using Figure 7, solve f (x) = 1. Determining Whether a Function is One-to-One Some functions have a given output value that corresponds to two or more input values. For example, in the stock chart shown in Figure 1 at the beginning of this chapter, the stock price was $1,000 on five different dates, meaning that there were five different input values that all resulted in the same output value of $1,000. However, some functions have only one input value for each output value, as well as having only one output for each input. We call these functions one-to-one functions. As an example, consider a school that uses only letter grades and decimal equivalents, as listed in Table 12. Letter grade Grade point average A 4.0 B 3.0 C 2.0 D 1.0 This grading system represents a one-to-one function, because each letter input yields one particular grade point average output and each grade point average corresponds to one input letter. To visualize this concept, let’s look again at the two simple functions sketched in Figure 1(a) and Figure 1(b). The function in part ( a) shows a relationship that is not a one-to-one function because inputs q and r both give output n. The function in part (b ) shows a relationship that is a one-to-one function because each input is associated with a single output. one-to-one function A one-to-one function is a function in which each output value corresponds to exactly one input value.

---
### 📐 **Example  13**: Determining Whether a Relationship Is a One-to-One Function

Is the area of a circle a function of its radius? If yes, is the function one-to-one?

**Solution**

A circle of radius r has a unique area measure given by A = π r 2, so for any input, r, there is only one output, A. The area is a function of radius r. If the function is one-to-one, the output value, the area, must correspond to a unique input value, the radius. Any area measure A is given by the formula A = π r². Because areas and radii are positive numbers, there is exactly one solution: r = √___

 A __ π     So the area of a circle is a one-to-one function of the circle’s radius.

---
### ✏️ **Try It #9**
a. Is a balance a function of the bank account number? b. Is a bank account number a function of the balance? c. Is a balance a one-to-one function of the bank account number?

---
### ✏️ **Try It #10**
a. If each percent grade earned in a course translates to one letter grade, is the letter grade a function of the percent grade? b. If so, is the function one-to-one?

### Using the Vertical Line Test

As we have seen in some examples above, we can represent a function using a graph. Graphs display a great many input-output pairs in a small space. The visual information they provide often makes relationships easier to understand. By convention, graphs are typically constructed with the input values along the horizontal axis and the output values along the vertical axis. The most common graphs name the input value x and the output value y, and we say y is a function of x, or y = f (x) when the function is named f. The graph of the function is the set of all points (x, y) in the plane that satisfies the equation y = f (x). If the function is defined for only a few input values, then the graph of the function is only a few points, where the x-coordinate of each point is an input value and the y-coordinate of each point is the corresponding output value. For example, the black dots on the graph in Figure 10 tell us that f (0) = 2 and f (6) = 1. However, the set of all points (x, y) satisfying y = f (x) is a curve. The curve shown includes (0, 2) and (6, 1) because the curve passes through those points. y x The vertical line test can be used to determine whether a graph represents a function. If we can draw any vertical line that intersects a graph more than once, then the graph does not define a function because a function has only one output value for each input value. See Figure 11. Function Not a Function Not a Function

---
### 💡 **How To…**
Given a graph, use the vertical line test to determine if the graph represents a function. 1. Inspect the graph to see if any vertical line drawn would intersect the curve more than once. 2. If there is any such line, determine that the graph does not represent a function.

---
### 📐 **Example  14**: Applying the Vertical Line Test

Which of the graphs in Figure 12 represent( s ) a function y = f (x)? x f (x) y (a) (b) (c) x x f (x)

**Solution**

If any vertical line intersects a graph more than once, the relation represented by the graph is not a function. Notice that any vertical line would pass through only one point of the two graphs shown in parts ( a) and (b) of Figure 12. From this we can conclude that these two graphs represent functions. The third graph does not represent a function because, at most x-values, a vertical line would intersect the graph at more than one point, as shown in Figure 13. x y

---
### ✏️ **Try It #11**
Does the graph in Figure 14 represent a function? x y

### Using the Horizontal Line Test

Once we have determined that a graph defines a function, an easy way to determine if it is a one-to-one function is to use the horizontal line test. Draw horizontal lines through the graph. If any horizontal line intersects the graph more than once, then the graph does not represent a one-to-one function.

---
### 💡 **How To…**
Given a graph of a function, use the horizontal line test to determine if the graph represents a one-to-one function. 1. Inspect the graph to see if any horizontal line drawn would intersect the curve more than once. 2. If there is any such line, determine that the function is not one-to-one.

---
### 📐 **Example  15**
Horizontal Line Test Consider the functions shown in Figure 12(a) and Figure 12(b). Are either of the functions one-to-one?

**Solution**

The function in Figure 12(a) is not one-to-one. The horizontal line shown in Figure 15 intersects the graph of the function at two points (and we can even find horizontal lines that intersect it at three points.) x f (x) The function in Figure 12(b) is one-to-one. Any horizontal line will intersect a diagonal line at most once.

---
### ✏️ **Try It #12**
Is the graph shown here one-to-one? x y Identifying Basic Toolkit Functions In this text, we will be exploring functions—the shapes of their graphs, their unique characteristics, their algebraic formulas, and how to solve problems with them. When learning to read, we start with the alphabet. When learning to do arithmetic, we start with numbers. When working with functions, it is similarly helpful to have a base set of building-block elements. We call these our “toolkit functions,” which form a set of basic named functions for which

we know the graph, formula, and special properties. Some of these functions are programmed to individual buttons on many calculators. For these definitions we will use x as the input variable and y = f (x) as the output variable. We will see these toolkit functions, combinations of toolkit functions, their graphs, and their transformations frequently throughout this book. It will be very helpful if we can recognize these toolkit functions and their features quickly by name, formula, graph, and basic table properties. The graphs and sample table values are included with each function shown in Table 13. Toolkit Functions Name Function Graph Constant f (x) = c, where c is a constant x x f(x) f (x) Identity f (x) = x x x f(x) f (x) Absolute value f (x) = ∣ x ∣ x f (x) x f(x) Quadratic f (x) = x² x x f(x) f (x) Cubic f (x) = x³ x 0.5 0.125 x f(x) f (x)

Reciprocal f (x) =  1/x  x 0.5 0.5 x f(x) f (x) Reciprocal squared f (x) =  1/x 2  x 0.25 0.5 0.25 x f(x) f (x) Square root f (x) = √x  x x f(x) f (x) Cube root f (x) =  √x  x 0.125 0.5 x f(x) f (x) Access the following online resources for additional instruction and practice with functions. • Determine if a Relation is a Function (http://openstaxcollege.org/l/relationfunction) • Vertical Line Test (http://openstaxcollege.org/l/vertlinetest) • Introduction to Functions (http://openstaxcollege.org/l/introtofunction) • Vertical Line Test of Graph (http://openstaxcollege.org/l/vertlinegraph) • One-to-one Functions (http://openstaxcollege.org/l/onetoone) • Graphs as One-to-one Functions (http://openstaxcollege.org/l/graphonetoone)

### 1.1 Section Exercises

Verbal 1. What is the difference between a relation and a function? 2. What is the difference between the input and the output of a function? 3. Why does the vertical line test tell us whether the graph of a relation represents a function? 4. How can you determine if a relation is a one-to-one function? 5. Why does the horizontal line test tell us whether the graph of a function is one-to-one? Algebraic For the following exercises, determine whether the relation represents a function. 6. {(a, b), (c, d), (a, c)} 7. {(a, b),(b, c),(c, c)} For the following exercises, determine whether the relation represents y as a function of x. 9. y = x 2/x  15. x =  3y + 5 ______ 7y - 1  16. x = √1 - y 2  17. y =  3x + 5 ______ 7x - 1  22. y = √1 - x 2  23. x = ± √1 - y  24. y = ± √1 - x  For the following exercises, evaluate the function f at the indicated values f (-3), f (2), f (-a), -f (a), f (a + h). 27. f (x) = 2x - 5 28. f (x) = -5x 2 + 2x - 1 29. f (x) = √2 - x  + 5 30. f (x) =  6x - 1 ______ 5x + 2  31. f (x) = ∣ x - 1 ∣ - ∣ x + 1 ∣ 32. Given the function g(x) = 5 - x 2, evaluate  g(x + h) - g(x)

__ h , h ≠  0 33. Given the function g(x) = x 2 + 2x, evaluate  g(x) - g(a) _ x - a , x ≠  a 34. Given the function k(t) = 2t - 1: a. Evaluate k(2). b. Solve k(t) = 7. 35. Given the function f (x) = 8 - 3x: a. Evaluate f (-2). b. Solve f (x) = -1. 36. Given the function p(c) = c 2 + c: a. Evaluate p(-3). b. Solve p(c) = 2. 37. Given the function f (x) = x² - 3x a. Evaluate f (5). b. Solve f (x) = 4 38. Given the function f (x) = √x + 2 : a. Evaluate f (7). b. Solve f (x) = 4 39. Consider the relationship 3r + 2t = 18. a. Write the relationship as a function r = f (t). b. Evaluate f (-3). c. Solve f (t) = 2.

## 1.1 Section Exercises

---
GRAPHICAL For the following exercises, use the vertical line test to determine which graphs show relations that are functions. x y x y x y x y x y x y x y x y x y x y x y x y

52. Given the following graph a. Evaluate f (-1). b. Solve for f (x) = 3. 53. Given the following graph a. Evaluate f (0). b. Solve for f (x) = -3. 54. Given the following graph a. Evaluate f (4). b. Solve for f (x) = 1. For the following exercises, determine if the given graph is a one-to-one function. x y x y x y x y x y π  π  Numeric For the following exercises, determine whether the relation represents a function. For the following exercises, determine if the relation represented in table form represents y as a function of x. x y x y x y For the following exercises, use the function f represented in Table 14 below. x f (x) 66. Evaluate f (3). 67. Solve f (x) = 1 x y x y x y

For the following exercises, evaluate the function f at the values f (-2), f (-1), f (0), f (1), and f (2). 68. f (x) = 4 - 2x 69. f (x) = 8 - 3x 70. f (x) = 8x² - 7x + 3 71. f (x) = 3 + √x + 3  72. f (x) =  x - 2 _____ x + 3  73. f (x) = 3x For the following exercises, evaluate the expressions, given functions f, g, and h: f (x) = 3x - 2 g(x) = 5 - x² h(x) = -2x² + 3x - 1 75. f (  7/3  ) - h(-2) TECHNOLOGY For the following exercises, graph y = x² on the given viewing window. Determine the corresponding range for each viewing window. Show each graph. For the following exercises, graph y = x³ on the given viewing window. Determine the corresponding range for each viewing window. Show each graph. For the following exercises, graph y = √x  on the given viewing window. Determine the corresponding range for each viewing window. Show each graph. For the following exercises, graph y =  √x  on the given viewing window. Determine the corresponding range for each viewing window. Show each graph. REal-world applications 88. The amount of garbage, G, produced by a city with population p is given by G = f (p). G is measured in tons per week, and p is measured in thousands of people. a. The town of Tola has a population of 40,000 and produces 13 tons of garbage each week. Express this information in terms of the function f. b. Explain the meaning of the statement f (5) = 2. 89. The number of cubic yards of dirt, D, needed to cover a garden with area a square feet is given by D = g(a). a. A garden with area 5,000 ft² requires 50 yd³ of dirt. Express this information in terms of the function g. b. Explain the meaning of the statement g(100) = 1. 90. Let f (t) be the number of ducks in a lake t years after 1990. Explain the meaning of each statement: a. f (5) = 30 b. f (10) = 40 91. Let h(t) be the height above ground, in feet, of a rocket t seconds after launching. Explain the meaning of each statement: 92. Show that the function f (x) = 3(x - 5)² + 7 is not one-to-one.

## 1.2 Domain and Range

---
If you’re in the mood for a scary movie, you may want to check out one of the five most popular horror movies of all time—I am Legend, Hannibal, The Ring, The Grudge, and The Conjuring. Figure 1 shows the amount, in dollars, each of those movies grossed when they were released as well as the ticket sales for horror movies in general by year. Notice that we can use the data to create a function of the amount each movie earned or the total ticket sales for all horror movies by year. In creating various functions using the data, we can identify different independent and dependent variables, and we can analyze the data and the functions to determine the domain and range. In this section, we will investigate methods for determining the domain and range of functions such as these. Inflation-adjusted Gross, in Millions of Dollars I am Legend Hannibal Top-Five Grossing Horror Movies Te Ring Te Grudge Te Conjuring

8% Market Share of Horror Moveis, by Year 7% 6% 5% 4% 3% 2% 1% 0% Finding the Domain of a Function Defined by an Equation In Functions and Function Notation, we were introduced to the concepts of domain and range. In this section, we will practice determining domains and ranges for specific functions. Keep in mind that, in determining domains and ranges, we need to consider what is physically possible or meaningful in real-world examples, such as tickets sales and year in the horror movie example above. We also need to consider what is mathematically permitted. For example, we cannot include any input value that leads us to take an even root of a negative number if the domain and range consist of real numbers. Or in a function expressed as a formula, we cannot include any input value in the domain that would lead us to divide by 0. We can visualize the domain as a “holding area” that contains “raw materials” for a “function machine” and the range as another “holding area” for the machine’s products. See Figure 2. Domain Function machine a b c x y z Range We can write the domain and range in interval notation, which uses values within brackets to describe a set of numbers. In interval notation, we use a square bracket [when the set includes the endpoint and a parenthesis (to indicate that the endpoint is either not included or the interval is unbounded. For example, if a person has $100 to spend, he or she would need to express the interval that is more than 0 and less than or equal to 100 and write (0, 100]. We will discuss interval notation in greater detail later. 3 The Numbers: Where Data and the Movie Business Meet. “Box Office History for Horror Movies.” http://www.the-numbers.com/market/genre/Horror. Accessed 3/24/2014 Learning Objectives
In this section, you will:
• Find the domain of a function defined by an equation.
• Graph piecewise-defined functions.
Let’s turn our attention to finding the domain of a function whose equation is provided. Oftentimes, finding the domain of such functions involves remembering three different forms. First, if the function has no denominator or an even root, consider whether the domain could be all real numbers. Second, if there is a denominator in the function’s equation, exclude values in the domain that force the denominator to be zero. Third, if there is an even root, consider excluding values that would make the radicand negative. Before we begin, let us review the conventions of interval notation: • The smallest term from the interval is written first. • The largest term in the interval is written second, following a comma. • Parentheses, (or), are used to signify that an endpoint is not included, called exclusive. • Brackets, [or], are used to indicate that an endpoint is included, called inclusive. See Figure 3 for a summary of interval notation. Inequality Interval Notation Graph on Number Line Description x > a (a, ∞ ) a ( x is greater than a x < a (-∞ , a) a ( x is less than a x ≥  a [a, ∞ ) a [ x is greater than or equal to a x ≤  a (-∞ , a] a ] x is less than or equal to a a < x < b (a, b) a b ( ( x is strictly between a and b a ≤  x < b [a, b) a b ( [ x is between a and b, to include a a < x ≤  b (a, b] a b ] ( x is between a and b, to include b a ≤  x ≤  b [a, b] a b [ ] x is between a and b, to include a and b

---
### 📐 **Example  1**: Finding the Domain of a Function as a Set of Ordered Pairs

Find the domain of the following function: {(2, 10), (3, 10), (4, 20), (5, 30), (6, 40)}.

**Solution**

First identify the input values. The input value is the first coordinate in an ordered pair. There are no restrictions, as the ordered pairs are simply listed. The domain is the set of the first coordinates of the ordered pairs.

---
### ✏️ **Try It #1**
Find the domain of the function: {(-5, 4), (0, 0), (5, -4), (10, -8), (15, -12)}

---
### 💡 **How To…**
Given a function written in equation form, find the domain. 1. Identify the input values. 2. Identify any restrictions on the input and exclude those values from the domain. 3. Write the domain in interval form, if possible.

---
### 📐 **Example  2**: Finding the Domain of a Function

Find the domain of the function f (x) = x² - 1.

**Solution**

The input value, shown by the variable x in the equation, is squared and then the result is lowered by one. Any real number may be squared and then be lowered by one, so there are no restrictions on the domain of this function. The domain is the set of real numbers. In interval form, the domain of f is (-∞ , ∞ ).

---
### ✏️ **Try It #2**
Find the domain of the function: f (x) = 5 - x + x 3.

---
### 💡 **How To…**
Given a function written in an equation form that includes a fraction, find the domain. 1. Identify the input values. 2. Identify any restrictions on the input. If there is a denominator in the function’s formula, set the denominator equal to zero and solve for x. If the function’s formula contains an even root, set the radicand greater than or equal to 0, and then solve. 3. Write the domain in interval form, making sure to exclude any restricted values from the domain.

---
### 📐 **Example  3**: Finding the Domain of a Function Involving a Denominator

Find the domain of the function f (x) =  x + 1 _____ 2 - x .

**Solution**

When there is a denominator, we want to include only values of the input that do not force the denominator to be zero. So, we will set the denominator equal to 0 and solve for x.

2 - x = 0

-x = -2

x = 2 Now, we will exclude 2 from the domain. The answers are all real numbers where x < 2 or x > 2. We can use a symbol known as the union, ∪, to combine the two sets. In interval notation, we write the solution: (-∞ , 2) ∪ (2, ∞ ). x < 2 or x > 2 ↓ ↓ (-∞ , 2) ∪ (2, ∞ ) In interval form, the domain of f is (-∞ , 2) ∪ (2, ∞ ).

---
### ✏️ **Try It #3**
Find the domain of the function: f (x) =  1 + 4x ______ 2x - 1 .

---
### 💡 **How To…**
Given a function written in equation form including an even root, find the domain. 1. Identify the input values. 2. Since there is an even root, exclude any real numbers that result in a negative number in the radicand. Set the radicand greater than or equal to zero and solve for x. 3. The solution(s) are the domain of the function. If possible, write the answer in interval form.

---
### 📐 **Example  4**: Finding the Domain of a Function with an Even Root

Find the domain of the function f (x) = √7 - x .

**Solution**

When there is an even root in the formula, we exclude any real numbers that result in a negative number in the radicand. Set the radicand greater than or equal to zero and solve for x.

7 - x ≥  0

-x ≥  -7

x ≤  7 Now, we will exclude any number greater than 7 from the domain. The answers are all real numbers less than or equal to 7, or (-∞ , 7].

---
### ✏️ **Try It #4**
Find the domain of the function f (x) = √5 + 2x . Can there be functions in which the domain and range do not intersect at all? Yes. For example, the function f (x) = - 1 _ √x   has the set of all positive real numbers as its domain but the set of all negative real numbers as its range. As a more extreme example, a function’s inputs and outputs can be completely different categories (for example, names of weekdays as inputs and numbers as outputs, as on an attendance chart), in such cases the domain and range have no elements in common. Using Notations to Specify Domain and Range In the previous examples, we used inequalities and lists to describe the domain of functions. We can also use inequalities, or other statements that might define sets of values or data, to describe the behavior of the variable in set-builder notation. For example, {x | 10 ≤  x < 30} describes the behavior of x in set-builder notation. The braces { } are read as “the set of,” and the vertical bar | is read as “such that,” so we would read {x | 10 ≤  x < 30} as “the set of x-values such that 10 is less than or equal to x, and x is less than 30.” Inequality Notation Set-builder Notation Interval Notation 5 < h ≤  10 {h | 5 < h ≤  10} 5 ≤  h < 10 {h | 5 ≤  h < 10} 5 < h < 10 {h | 5 < h < 10} h < 10 {h | h < 10} h ≥  10 {h | h ≥  10} All real numbers 핉 (-∞ , ∞ )

To combine two intervals using inequality notation or set-builder notation, we use the word “or.” As we saw in earlier examples, we use the union symbol, ∪, to combine two unconnected intervals. For example, the union of the sets {2, 3, 5} and {4, 6} is the set {2, 3, 4, 5, 6}. It is the set of all elements that belong to one or the other (or both) of the original two sets. For sets with a finite number of elements like these, the elements do not have to be listed in ascending order of numerical value. If the original two sets have some elements in common, those elements should be listed only once in the union set. For sets of real numbers on intervals, another example of a union is {x | | x | ≥  3} = (-∞ , -3] ∪ [3, ∞ ) set-builder notation and interval notation Set-builder notation is a method of specifying a set of elements that satisfy a certain condition. It takes the form {x | statement about x} which is read as, “the set of all x such that the statement about x is true.” For example, {x | 4 < x ≤  12} Interval notation is a way of describing sets that include all real numbers between a lower limit that may or may not be included and an upper limit that may or may not be included. The endpoint values are listed between brackets or parentheses. A square bracket indicates inclusion in the set, and a parenthesis indicates exclusion from the set. For example,

---
### 💡 **How To…**
Given a line graph, describe the set of values using interval notation. 1. Identify the intervals to be included in the set by determining where the heavy line overlays the real line. 2. At the left end of each interval, use [with each end value to be included in the set (solid dot) or (for each excluded end value (open dot). 3. At the right end of each interval, use] with each end value to be included in the set (filled dot) or) for each excluded end value (open dot). 4. Use the union symbol ∪ to combine all intervals into one set.

---
### 📐 **Example  5**: Describing Sets on the Real-Number Line

Describe the intervals of values shown in Figure 6 using inequality notation, set-builder notation, and interval notation.

**Solution**

To describe the values, x, included in the intervals shown, we would say, “x is a real number greater than or equal to 1 and less than or equal to 3, or a real number greater than 5.” Inequality 1 ≤  x ≤  3 or x > 5 Set-builder notation { x |1 ≤  x ≤  3 or x > 5 } Interval notation [1, 3] ∪ (5, ∞ ) Remember that, when writing or reading interval notation, using a square bracket means the boundary is included in the set. Using a parenthesis means the boundary is not included in the set.

---
### ✏️ **Try It #5**
Given this figure, specify the graphed set in

a. words b. set-builder notation c. interval notation Finding Domain and Range from Graphs Another way to identify the domain and range of functions is by using graphs. Because the domain refers to the set of possible input values, the domain of a graph consists of all the input values shown on the x-axis. The range is the set of possible output values, which are shown on the y-axis. Keep in mind that if the graph continues beyond the portion of the graph we can see, the domain and range may be greater than the visible values. See Figure 8. x y Domain Range We can observe that the graph extends horizontally from -5 to the right without bound, so the domain is [-5, ∞ ). The vertical extent of the graph is all range values 5 and below, so the range is (-∞ , 5]. Note that the domain and range are always written from smaller to larger values, or from left to right for domain, and from the bottom of the graph to the top of the graph for range.

---
### 📐 **Example  6**: Finding Domain and Range from a Graph

Find the domain and range of the function f whose graph is shown in Figure 9. f x y

**Solution**

We can observe that the horizontal extent of the graph is -3 to 1, so the domain of f is (-3, 1]. The vertical extent of the graph is 0 to -4, so the range is [-4, 0]. See Figure 10. f Range Domain x y

---
### 📐 **Example  7**: Finding Domain and Range from a Graph of Oil Production

Find the domain and range of the function f whose graph is shown in Figure 11. Tousand barrels per day Alaska Crude Oil Production

**Solution**

The input quantity along the horizontal axis is “years,” which we represent with the variable t for time. The output quantity is “thousands of barrels of oil per day,” which we represent with the variable b for barrels. The graph may continue to the left and right beyond what is viewed, but based on the portion of the graph that is visible, we can determine the domain as 1973 ≤  t ≤  2008 and the range as approximately 180 ≤  b ≤  2010. In interval notation, the domain is [1973, 2008], and the range is about [180, 2010]. For the domain and the range, we approximate the smallest and largest values since they do not fall exactly on the grid lines.

---
### ✏️ **Try It #6**
Given Figure 12, identify the domain and range using interval notation. Millions of people World Population Increase Year

Can a function’s domain and range be the same? Yes. For example, the domain and range of the cube root function are both the set of all real numbers. 4 http://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=MCRFPAK²&f=A.

### Finding Domains and Ranges of the Toolkit Functions

We will now return to our set of toolkit functions to determine the domain and range of each. x f(x) = c f(x) Domain: (-∞ , ∞ ) Range: [c, c]

For the constant function f(x) = c, the domain consists of all real numbers; there are no restrictions on the input. The only output value is the constant c, so the range is the set {c} that contains this single element. In interval notation, this is written as [c, c], the interval that both begins and ends with c. x f(x) Domain: (-∞ , ∞ ) Range: (-∞ , ∞ ) For the identity function f(x) = x, there is no restriction on x. Both the domain and range are the set of all real numbers. x f(x) Domain: (-∞ , ∞ ) Range: [0, ∞ ) For the absolute value function f(x) = ∣ x ∣, there is no restriction on x. However, because absolute value is defined as a distance from 0, the output can only be greater than or equal to 0. Domain: (-∞ , ∞ ) Range: [0, ∞ ) x f(x) For the quadratic function f(x) = x 2, the domain is all real numbers since the horizontal extent of the graph is the whole real number line. Because the graph does not include any negative values for the range, the range is only nonnegative real numbers. Domain: (-∞ , ∞ ) Range: (-∞ , ∞ ) x f(x) For the cubic function f(x) = x 3, the domain is all real numbers because the horizontal extent of the graph is the whole real number line. The same applies to the vertical extent of the graph, so the domain and range include all real numbers.

x f(x) Domain: (-∞ , 0) ∪ (0, ∞ ) Range: (-∞ , 0) ∪ (0, ∞ ) For the reciprocal function f(x) =  1/x , we cannot divide by 0, so we must exclude 0 from the domain. Further, 1 divided by any value can never be 0, so the range also will not include 0. In set-builder notation, we could also write {x | x ≠  0}, the set of all real numbers that are not zero. Domain: (-∞ , 0) ∪ (0, ∞ ) Range: (0, ∞ ) x f(x) For the reciprocal squared function f(x) =  1/x 2 , we cannot divide by 0, so we must exclude 0 from the domain. There is also no x that can give an output of 0, so 0 is excluded from the range as well. Note that the output of this function is always positive due to the square in the denominator, so the range includes only positive numbers. x f(x) Domain: [0, ∞ ) Range: [0, ∞ ) For the square root function f(x) = √x , we cannot take the square root of a negative real number, so the domain must be 0 or greater. The range also excludes negative numbers because the square root of a positive number x is defined to be positive, even though the square of the negative number -√x  also gives us x. x f(x) Domain: (-∞ , ∞ ) Range: (-∞ , ∞ ) For the cube root function f(x) =  √x  the domain and range include all real numbers. Note that there is no problem taking a cube root, or any odd-integer root, of a negative number, and the resulting output is negative (it is an odd function).

---
### 💡 **How To…**
Given the formula for a function, determine the domain and range. 1. Exclude from the domain any input values that result in division by zero. 2. Exclude from the domain any input values that have nonreal (or undefined) number outputs. 3. Use the valid input values to determine the range of the output values. 4. Look at the function graph and table values to confirm the actual function behavior.

---
### 📐 **Example  8**: Finding the Domain and Range Using Toolkit Functions

Find the domain and range of f (x) = 2x³ - x.

**Solution**

There are no restrictions on the domain, as any real number may be cubed and then subtracted from the result. The domain is (-∞ , ∞ ) and the range is also (-∞ , ∞ ).

---
### 📐 **Example  9**: Finding the Domain and Range

Find the domain and range of f (x) =  2 ____ x + 1 .

**Solution**

We cannot evaluate the function at -1 because division by zero is undefined. The domain is (-∞ , -1) ∪ (-1, ∞ ). Because the function is never zero, we exclude 0 from the range. The range is (-∞ , 0) ∪ (0, ∞ ).

---
### 📐 **Example  10**: Finding the Domain and Range

Find the domain and range of f (x) = 2√x + 4 .

**Solution**

We cannot take the square root of a negative number, so the value inside the radical must be nonnegative. x + 4 ≥  0 when x ≥  -4 The domain of f (x) is [-4, ∞ ). We then find the range. We know that f (-4) = 0, and the function value increases as x increases without any upper limit. We conclude that the range of f is [0, ∞ ). Analysis Figure 22 represents the function f .

x f f(x)

---
### ✏️ **Try It #7**
Find the domain and range of f (x) = -√2 - x . Graphing Piecewise-Defined Functions Sometimes, we come across a function that requires more than one formula in order to obtain the given output. For example, in the toolkit functions, we introduced the absolute value function f (x) = |x|. With a domain of all real numbers and a range of values greater than or equal to 0, absolute value can be defined as the magnitude, or modulus, of a real number value regardless of sign. It is the distance from 0 on the number line. All of these definitions require the output to be greater than or equal to 0. If we input 0, or a positive value, the output is the same as the input. f (x) = x if x ≥  0 If we input a negative value, the output is the opposite of the input. f (x) = -x if x < 0 Because this requires two different processes or pieces, the absolute value function is an example of a piecewise function. A piecewise function is a function in which more than one formula is used to define the output over different pieces of the domain. We use piecewise functions to describe situations in which a rule or relationship changes as the input value crosses certain “boundaries.” For example, we often encounter situations in business for which the cost per piece of a certain item is discounted once the number ordered exceeds a certain value. Tax brackets are another real-world example of piecewise functions. For example, consider a simple tax system in which incomes up to $10,000 are taxed at 10%, and any additional income is taxed at 20%. The tax on a total income S would be 0.1S if S ≤  $10,000 and $1000 + 0.2(S - $10,000)

piecewise function A piecewise function is a function in which more than one formula is used to define the output. Each formula has its own domain, and the domain of the function is the union of all these smaller domains. We notate this idea like this: f (x) = formula 1 if x is in domain 1 formula 2 if x is in domain 2 formula 3 if x is in domain 3 { In piecewise notation, the absolute value function is |x| = x if x ≥  0 -x if x < 0 {

---
### 💡 **How To…**
Given a piecewise function, write the formula and identify the domain for each interval. 1. Identify the intervals for which different rules apply. 2. Determine formulas that describe how to calculate an output from an input in each interval. 3. Use braces and if-statements to write the function.

---
### 📐 **Example  11**: Writing a Piecewise Function

A museum charges $5 per person for a guided tour with a group of 1 to 9 people or a fixed $50 fee for a group of 10 or more people. Write a function relating the number of people, n, to the cost, C.

**Solution**

Two different formulas will be needed. For n-values under 10, C = 5n. For values of n that are 10 or greater, C(n) = 5n if 0 < n < 10 50 if n ≥  10 { Analysis The function is represented in Figure 23. The graph is a diagonal line from n = 0 to n = 10 and a constant after that. In this example, the two formulas agree at the meeting point where n = 10, but not all piecewise functions have this property. C(n) C(n) n

---
### 📐 **Example  12**: Working with a Piecewise Function

A cell phone company uses the function below to determine the cost, C, in dollars for g gigabytes of data transfer. C(g) = if 0 < g < 2 25 + 10(g - 2) if g ≥  2 { Find the cost of using 1.5 gigabytes of data and the cost of using 4 gigabytes of data.

**Solution**

To find the cost of using 1.5 gigabytes of data, C(1.5), we first look to see which part of the domain our input falls in. Because 1.5 is less than 2, we use the first formula. To find the cost of using 4 gigabytes of data, C(4), we see that our input of 4 is greater than 2, so we use the second formula. C(4) = 25 + 10(4 - 2) = $45

Analysis The function is represented in Figure 24. We can see where the function changes from a constant to a shifted and stretched identity at g = 2. We plot the graphs for the different formulas on a common set of axes, making sure each formula is applied on its proper domain. C(g) C(g) g

---
### 💡 **How To…**
Given a piecewise function, sketch a graph. 1. Indicate on the x-axis the boundaries defined by the intervals on each piece of the domain. 2. For each piece of the domain, graph on that interval using the corresponding equation pertaining to that piece. Do not graph two functions over one interval because it would violate the criteria of a function.

---
### 📐 **Example  13**: Graphing a Piecewise Function

Sketch a graph of the function. f (x) = x² if x ≤  1 3 if 1 < x ≤  2 x if x > 2 {

**Solution**

Each of the component functions is from our library of toolkit functions, so we know their shapes. We can imagine graphing each function and then limiting the graph to the indicated domain. At the endpoints of the domain, we draw open circles to indicate where the endpoint is not included because of a less-than or greater-than inequality; we draw a closed circle where the endpoint is included because of a less-than-or-equal-to or greater-than-or-equal-to inequality. (a) x f(x) (b) x f(x) (c) x f(x)

Now that we have sketched each piece individually, we combine them in the same coordinate plane. See Figure 26. x f(x) Analysis Note that the graph does pass the vertical line test even at x = 1 and x = 2 because the points (1, 3) and (2, 2) are not part of the graph of the function, though (1, 1) and (2, 3) are.

---
### ✏️ **Try It #8**
Graph the following piecewise function. f (x) = √x  x³ if x < -1 -2 if -1 < x < 4

if x > 4 {

Can more than one formula from a piecewise function be applied to a value in the domain? No. Each value corresponds to one equation in a piecewise formula. Access these online resources for additional instruction and practice with domain and range. • Domain and Range of Square Root Functions (http://openstaxcollege.org/l/domainsqroot) • Determining Domain and Range (http://openstaxcollege.org/l/determinedomain) • Find Domain and Range Given the Graph (http://openstaxcollege.org/l/drgraph) • Find Domain and Range Given a Table (http://openstaxcollege.org/l/drtable) • Find Domain and Range Given Points on a Coordinate Plane (http://openstaxcollege.org/l/drcoordinate)

## 1.2 Section Exercises

---
### 1.2 Section Exercises

Verbal 1. Why does the domain differ for different functions? 2. How do we determine the domain of a function defined by an equation? 3. Explain why the domain of f (x) =  √x  is different from the domain of f (x) = √x . 4. When describing sets of numbers using interval notation, when do you use a parenthesis and when do you use a bracket? 5. How do you graph a piecewise function? Algebraic For the following exercises, find the domain of each function using interval notation. 6. f (x) = -2x(x - 1)(x - 2) 7. f (x) = 5 - 2x² 8. f (x) = 3√x - 2  9. f (x) = 3 - √6 - 2x  10. f (x) = √4 - 3x  11. f (x) = √x 2 + 4  12. f (x) =  √1 - 2x  13. f (x) =  √x - 1  14. f (x) =  9 _____ x - 6  15. f (x) =  3x + 1 ______ 4x + 2  16. f (x) =  √x + 4  _______ x - 4  17. f (x) =  x - 3 __________

x² + 9x - 22  18. f (x) =  ________ x² - x - 6  19. f (x) =  2x³ - 250 __________

x² - 2x - 15  20. f (x) =  _ √x - 3   21. f (x) =  2x + 1 _ √5 - x   22. f (x) =  √x - 4  _ √x - 6   23. f (x) =  √x - 6  _ √x - 4   24. f (x) =  (x)/(x)  25. f (x) =  x² - 9(x)/(x)² - 81  26. Find the domain of the function f (x) = √2x 3 - 50x  by: a. using algebra. b. graphing the function in the radicand and determining intervals on the x-axis for which the radicand is nonnegative. GRAPHICAL For the following exercises, write the domain and range of each function using interval notation. x y x y x y

x y x y x y x y x y –6, – ) ( 6, ) ( ) ( 6, ) ( x y x y x y For the following exercises, sketch a graph of the piecewise function. Write the domain in interval notation. 38. f (x) = x + 1 if x < -2 -2x - 3 if x ≥  -2 { 39. f (x) = 2x - 1 if x < 1 1 + x if x ≥  1 { 40. f (x) = x + 1 if x < 0 x - 1 if x > 0 { 41. f (x) = 3 if x < 0 √x  if x ≥  0 { 42. f (x) = x² if x < 0 1 - x if x > 0 { 43. f (x) = x² if x < 0 x + 2 if x ≥  0 { 44. f (x) = x + 1 if x < 1 x³ if x ≥  1 { 45. f (x) = | x | if x < 2 if x ≥  2 {

Numeric For the following exercises, given each function f, evaluate f (-3), f (-2), f (-1), and f (0). 46. f (x) = x + 1 if x < -2 -2x - 3 if x ≥  -2 { 47. f (x) = 1 if x ≤  -3 0 if x > -3 { 48. f (x) = -2x 2 + 3 if x ≤  -1 5x - 7 if x > -1 { For the following exercises, given each function f, evaluate f (-1), f (0), f (2), and f (4). 49. f (x) = 7x + 3 if x < 0 7x + 6 if x ≥  0 { 50. f (x) = x 2 - 2 if x < 2 4 + | x - 5 | if x ≥  2 { 51. f (x) = 5x if x < 0 3 if 0 ≤  x ≤  3 x 2 if x > 3 { For the following exercises, write the domain for the piecewise function in interval notation. 52. f (x) = x + 1 if x < -2 -2x - 3 if x ≥  -2 { 53. f (x) = x² - 2 if x < 1 -x² + 2 if x > 1 { 54. f (x) = 2x - 3 if x < 0 -3x² if x ≥  2 { Technology 55. Graph y =  1/x 2  on the viewing window [-0.5, -0.1] and [0.1, 0.5]. Determine the corresponding range for the viewing window. Show the graphs. 56. Graph y =  1/x  on the viewing window [-0.5, -0.1] and [0.1, 0.5]. Determine the corresponding range for the viewing window. Show the graphs. Extension 57. Suppose the range of a function f is [-5, 8]. What is the range of | f (x) |? 58. Create a function in which the range is all nonnegative real numbers. 59. Create a function in which the domain is x > 2. Real-World Applications 60. The height h of a projectile is a function of the time t it is in the air. The height in feet for t seconds is given by the function h(t) = -16t 2 + 96t. What is the domain of the function? What does the domain mean in the context of the problem? 61. The cost in dollars of making x items is given by the function C(x) = 10x + 500. a. The fixed cost is determined when zero items are produced. Find the fixed cost for this item. b. What is the cost of making 25 items? c. Suppose the maximum cost allowed is $1500. What are the domain and range of the cost function, C(x)?

Rates of Change and Behavior of Graphs Gasoline costs have experienced some wild fluctuations over the last several decades. Table 1 [5] lists the average cost, in dollars, of a gallon of gasoline for the years 2005–2012. The cost of gasoline can be considered as a function of year. y C(y) 2.31 2.62 2.84 3.30 2.41 2.84 3.58 3.68 If we were interested only in how the gasoline prices changed between 2005 and 2012, we could compute that the cost per gallon had increased from $2.31 to $3.68, an increase of $1.37. While this is interesting, it might be more useful to look at how much the price changed per year. In this section, we will investigate changes such as these. Finding the Average Rate of Change of a Function The price change per year is a rate of change because it describes how an output quantity changes relative to the change in the input quantity. We can see that the price of gasoline in Table 1 did not change by the same amount each year, so the rate of change was not constant. If we use only the beginning and ending data, we would be finding the average rate of change over the specified period of time. To find the average rate of change, we divide the change in the output value by the change in the input value.

Average rate of change =  Change in outpu(t)/(C)hange in input 

=  ∆y _ ∆x 

=  y² - y¹ _ x² - x¹ 

=  f (x²) - f (x¹) __ x²- x¹  The Greek letter ∆ (delta) signifies the change in a quantity; we read the ratio as “delta-y over delta-x” or “the change in y divided by the change in x.” Occasionally we write ∆ f instead of ∆y, which still represents the change in the function’s output value resulting from a change to its input value. It does not mean we are changing the function into some other function. In our example, the gasoline price increased by $1.37 from 2005 to 2012. Over 7 years, the average rate of change was

 ∆y _ ∆x  =  $1.37/7 years  ≈ 0.196 dollars per year On average, the price of gas increased by about 19.6% each year. Other examples of rates of change include: • A population of rats increasing by 40 rats per week • A car traveling 68 miles per hour (distance traveled changes by 68 miles each hour as time passes) • A car driving 27 miles per gallon (distance traveled changes by 27 miles for each gallon) • The current through an electrical circuit increasing by 0.125 amperes for every volt of increased voltage • The amount of money in a college account decreasing by $4,000 per quarter 5 http://www.eia.gov/totalenergy/data/annual/showtext.cfm?t=ptb⁰524. Accessed 3/5/2014. Learning Objectives
In this section, you will:
• Find the average rate of change of a function.
• Use a graph to determine where a function is increasing, decreasing, or constant.
• Use a graph to locate local maxima and local minima.
• Use a graph to locate the absolute maximum and absolute minimum.

## 1.3 Rates of Change and Behavior of Graphs

---
rate of change A rate of change describes how an output quantity changes relative to the change in the input quantity. The units on a rate of change are “output units per input units.” The average rate of change between two input values is the total change of the function values (output values) divided by the change in the input values.  Δ y _ Δ x  =  f (x²) - f (x¹) __ x² - x¹ 

---
### 💡 **How To…**
Given the value of a function at different points, calculate the average rate of change of a function for the interval between two values x¹ and x². 1. Calculate the difference y² - y¹ = Δ y. 2. Calculate the difference x² - x¹ = Δ x. 3. Find the ratio  Δ y _ Δ x .

---
### 📐 **Example  1**: Computing an Average Rate of Change

Using the data in Table 1, find the average rate of change of the price of gasoline between 2007 and 2009.

**Solution**

In 2007, the price of gasoline was $2.84. In 2009, the cost was $2.41. The average rate of change is

 Δ y ___ Δ x  =  y² - y¹ _ x² - x¹ 

__

______ 2 years 

= -$0.22 per year Analysis Note that a decrease is expressed by a negative change or “negative increase.” A rate of change is negative when the output decreases as the input increases or when the output increases as the input decreases.

---
### ✏️ **Try It #1**
Using the data in Table 1 at the beginning of this section, find the average rate of change between 2005 and 2010.

---
### 📐 **Example  2**: Computing Average Rate of Change from a Graph

Given the function g (t) shown in Figure 1, find the average rate of change on the interval [-1, 2]. t g(t)

**Solution**

At t = -1, Figure 2 shows g (-1) = 4. At t = 2, the graph shows g (2) = 1. t g(t) ∆g(t) = –3 ∆t = 3 The horizontal change Δ  t = 3 is shown by the red arrow, and the vertical change Δ  g(t) = -3 is shown by the turquoise arrow. The output changes by –3 while the input changes by 3, giving an average rate of change of  1 - 4 _______ 2 - (-1)  =  -3 ___ 3  = -1 Analysis Note that the order we choose is very important. If, for example, we use  y² - y¹ _ x¹ - x²  , we will not get the correct answer. Decide which point will be 1 and which point will be 2, and keep the coordinates fixed as ( x¹ , y¹ ) and ( x² , y² ).

---
### 📐 **Example  3**: Computing Average Rate of Change from a Table

After picking up a friend who lives 10 miles away, Anna records her distance from home over time. The values are shown in Table 2. Find her average speed over the first 6 hours. t (hours) D(t) (miles)

**Solution**

Here, the average speed is the average rate of change. She traveled 282 miles in 6 hours, for an average speed of

_______ 6 - 0  =  282 ___ 6 

= 47 The average speed is 47 miles per hour. Analysis Because the speed is not constant, the average speed depends on the interval chosen. For the interval [2, 3], the average speed is 63 miles per hour.

---
### 📐 **Example  4**: Computing Average Rate of Change for a Function Expressed as a Formula

Compute the average rate of change of f (x) = x 2 - 1/x  on the interval [2, 4].

**Solution**

We can start by computing the function values at each endpoint of the interval.

f (2) = 22 -  1/2  f(4) = 42 -  1/4 

= 4 -  1/2  = 16 -  1/4 

=  7/2  =  63/4  Now we compute the average rate of change.

Average rate of change =  f (4) - f (2) _ 4 - 2 

=   63/4  -  7/2  _ 4 - 2 

=   49/4 

_ 2 

=  49/8 

---
### ✏️ **Try It #2**
Find the average rate of change of f (x) = x - 2√x  on the interval [1, 9].

---
### 📐 **Example  5**: Finding the Average Rate of Change of a Force

The electrostatic force F, measured in newtons, between two charged particles can be related to the distance between the particles d, in centimeters, by the formula F(d) =  2/d 2 . Find the average rate of change of force if the distance between the particles is increased from 2 cm to 6 cm.

**Solution**

We are computing the average rate of change of F (d) =  2/d 2  on the interval [2, 6].

Average rate of change =  F(6) - F(2) __ 6 - 2 

=   2/62  -  2/22  _ 6 - 2  Simplify.

=   2/36  -  2/4  _ 

=  - 16/36  _ 4  Combine numerator terms.

= - 1/9  Simplify. The average rate of change is - 1/9  newton per centimeter.

---
### 📐 **Example  6**
Finding an Average Rate of Change as an Expression Find the average rate of change of g(t) = t² + 3t + 1 on the interval [0, a]. The answer will be an expression involving a.

**Solution**

We use the average rate of change formula.

Average rate of change =  g(a) - g(0) _ a - 0  Evaluate.

=  (a² + 3a + 1) - (02 + 3(0) + 1)

___

a - 0  Simplify.

=  a² + 3a + 1 - 1

_____________ a  Simplify and factor.

=  a(a + 3) _______ a  Divide by the common factor a.

= a + 3 This result tells us the average rate of change in terms of a between t = 0 and any other point t = a. For example, on the interval [0, 5], the average rate of change would be 5 + 3 = 8.

---
### ✏️ **Try It #3**
Find the average rate of change of f (x) = x² + 2x - 8 on the interval [5, a]. Using a Graph to Determine Where a Function is Increasing, Decreasing, or Constant As part of exploring how functions change, we can identify intervals over which the function is changing in specific ways. We say that a function is increasing on an interval if the function values increase as the input values increase within that interval. Similarly, a function is decreasing on an interval if the function values decrease as the input values increase over that interval. The average rate of change of an increasing function is positive, and the average rate of change of a decreasing function is negative. Figure 3 shows examples of increasing and decreasing intervals on a function. x f(x) f(b) > f(a) where b > a f(b) < f(a) where b > a f(b) > f(a) where b > a Increasing Increasing Decreasing While some functions are increasing (or decreasing) over their entire domain, many others are not. A value of the input where a function changes from increasing to decreasing (as we go from left to right, that is, as the input variable increases) is called a local maximum. If a function has more than one, we say it has local maxima. Similarly, a value of the input where a function changes from decreasing to increasing as the input variable increases is called a local minimum. The plural form is “local minima.” Together, local maxima and minima are called local extrema, or local extreme values, of the function. (The singular form is “extremum.”) Often, the term local is replaced by the term relative. In this text, we will use the term local. Clearly, a function is neither increasing nor decreasing on an interval where it is constant. A function is also neither increasing nor decreasing at extrema. Note that we have to speak of local extrema, because any given local extremum as defined here is not necessarily the highest maximum or lowest minimum in the function’s entire domain. For the function whose graph is shown in Figure 4, the local maximum is 16, and it occurs at x = -2. The local minimum is -16 and it occurs at x = 2. x Local maximum = 16 occurs at x = –2 Local minimum = –16 occurs at x = 2 f(x) Decreasing Increasing Increasing

To locate the local maxima and minima from a graph, we need to observe the graph to determine where the graph attains its highest and lowest points, respectively, within an open interval. Like the summit of a roller coaster, the graph of a function is higher at a local maximum than at nearby points on both sides. The graph will also be lower at a local minimum than at neighboring points. Figure 5 illustrates these ideas for a local maximum. f(x) f(b) x a b Local maximum Increasing function Decreasing function c These observations lead us to a formal definition of local extrema. local minima and local maxima A function f is an increasing function on an open interval if f (b) > f (a) for every two input values a and b in the interval where b > a. A function f is a decreasing function on an open interval if f (b) < f (a) for every two input values a and b in the interval where b > a. A function f has a local maximum at a point b in an open interval (a, c) if f (b) ≥  f (x) for every point x (x does not equal b) in the interval. f has a local minimum at a point b in the interval (a, c) if f (b) ≤  f (x) for every point x (x does not equal both) in the interval.

---
### 📐 **Example  7**
Finding Increasing and Decreasing Intervals on a Graph Given the function p(t) in Figure 6, identify the intervals on which the function appears to be increasing. t p

**Solution**

We see that the function is not constant on any interval. The function is increasing where it slants upward as we move to the right and decreasing where it slants downward as we move to the right. The function appears to be increasing from t = 1 to t = 3 and from t = 4 on. In interval notation, we would say the function appears to be increasing on the interval (1, 3) and the interval (4, ∞ ).

Analysis Notice in this example that we used open intervals (intervals that do not include the endpoints), because the function is neither increasing nor decreasing at t = 1, t = 3, and t = 4. These points are the local extrema (two minima and a maximum).

---
### 📐 **Example  8**: Finding Local Extrema from a Graph

Graph the function f (x) =  2/x  +  x/3 . Then use the graph to estimate the local extrema of the function and to determine the intervals on which the function is increasing.

**Solution**

Using technology, we find that the graph of the function looks like that in Figure 7. It appears there is a low point, or local minimum, between x = 2 and x = 3, and a mirror-image high point, or local maximum, somewhere between x = -3 and x = -2. x f(x) Analysis Most graphing calculators and graphing utilities can estimate the location of maxima and minima. Figure 8 provides screen images from two different technologies, showing the estimate for the local maximum and minimum. x Maximum y (b) (a) Based on these estimates, the function is increasing on the interval (-∞ , -2.449) and (2.449, ∞ ). Notice that, while we expect the extrema to be symmetric, the two different technologies agree only up to four decimals due to the differing approximation algorithms used by each. (The exact location of the extrema is at ± √— 6 , but determining this requires calculus.)

---
### ✏️ **Try It #4**
Graph the function f (x) = x³ - 6x² - 15x + 20 to estimate the local extrema of the function. Use these to determine the intervals on which the function is increasing and decreasing.

---
### 📐 **Example  9**: Finding Local Maxima and Minima from a Graph

For the function f whose graph is shown in Figure 9, find all local maxima and minima. x y f

**Solution**

Observe the graph of f. The graph attains a local maximum at x = 1 because it is the highest point in an open interval around x = 1. The local maximum is the y-coordinate at x = 1, which is 2. The graph attains a local minimum at x = -1 because it is the lowest point in an open interval around x = -1. The local minimum is the y-coordinate at x = -1, which is -2. Analyzing the Toolkit Functions for Increasing or Decreasing Intervals We will now return to our toolkit functions and discuss their graphical behavior in Figure 10, Figure 11, and Figure 12. Function Increasing/Decreasing Example Constant Function f(x) = c Neither increasing nor decreasing y x Identity Function f(x) = x Increasing y x Quadratic Function f(x) = x² Increasing on (0, ∞ ) Decreasing on (-∞ , 0) Minimum at x = 0 y x

Function Increasing/Decreasing Example Cubic Function f(x) = x³ Increasing y x Reciprocal f(x) =  1/x  Decreasing (-∞ , 0) ∪ (0, ∞ ) y x Reciprocal Squared f(x) =  1/x²  Increasing on (-∞ , 0) Decreasing on (0, ∞ ) y x Function Increasing/Decreasing Example Cube Root f(x) =  √x  Increasing y x Square Root f(x) = √x  Increasing on (0, ∞ ) y x Absolute Value f(x) = ∣ x ∣ Increasing on (0, ∞ ) Decreasing on (-∞ , 0) y x

Use A Graph to Locate the Absolute Maximum and Absolute Minimum There is a difference between locating the highest and lowest points on a graph in a region around an open interval (locally) and locating the highest and lowest points on the graph for the entire domain. The y-coordinates (output) at the highest and lowest points are called the absolute maximum and absolute minimum, respectively. To locate absolute maxima and minima from a graph, we need to observe the graph to determine where the graph attains it highest and lowest points on the domain of the function. See Figure 13. x f Absolute minimum is f (0) = -2 Absolute maximum is f (2) = 2 y Not every function has an absolute maximum or minimum value. The toolkit function f (x) = x³ is one such function. absolute maxima and minima The absolute maximum of f at x = c is f (c) where f (c) ≥  f (x) for all x in the domain of f. The absolute minimum of f at x = d is f (d) where f (d) ≤  f (x) for all x in the domain of f.

---
### 📐 **Example  10**
Finding Absolute Maxima and Minima from a Graph For the function f shown in Figure 14, find all absolute maxima and minima. x y f

**Solution**

Observe the graph of f. The graph attains an absolute maximum in two locations, x = -2 and x = 2, because at these locations, the graph attains its highest point on the domain of the function. The absolute maximum is the y-coordinate at x = -2 and x = 2, which is 16. The graph attains an absolute minimum at x = 3, because it is the lowest point on the domain of the function’s graph. The absolute minimum is the y-coordinate at x = 3, which is -10. > Access this online resource for additional instruction and practice with rates of change. • Average Rate of Change (http://openstaxcollege.org/l/aroc)

### 1.3 Section Exercises

Verbal 1. Can the average rate of change of a function be constant? 2. If a function f is increasing on (a, b) and decreasing on (b, c), then what can be said about the local extremum of f on (a, c)? 3. How are the absolute maximum and minimum similar to and different from the local extrema? 4. How does the graph of the absolute value function compare to the graph of the quadratic function, y = x 2, in terms of increasing and decreasing intervals? Algebraic For the following exercises, find the average rate of change of each function on the interval specified for real numbers b or h. 5. f (x) = 4x 2 - 7 on [1, b] 6. g (x) = 2x 2 - 9 on [4, b] 7. p(x) = 3x + 4 on [2, 2 + h] 8. k(x) = 4x - 2 on [3, 3 + h] 9. f (x) = 2x 2 + 1 on [x, x + h] 10. g(x) = 3x 2 - 2 on [x, x + h] 11. a(t) =  1 ____ t + 4  on [9, 9 + h] 12. b(x) =  1 _____ x + 3  on [1, 1 + h] 13. j(x) = 3x 3 on [1, 1 + h] 14. r(t) = 4t 3 on [2, 2 + h] 15.  f (x + h) - f(x)

__ h  given f(x) = 2x² - 3x on [x, x + h] Graphical For the following exercises, consider the graph of f shown in Figure 15.

16. Estimate the average rate of change from x = 1 to x = 4.

17. Estimate the average rate of change from x = 2 to x = 5.

For the following exercises, use the graph of each function to estimate the intervals on which the function is increasing or decreasing. x y x y x y x y

## 1.3 Section Exercises

---
x y For the following exercises, consider the graph shown in Figure 16. 22. Estimate the intervals where the function is increasing or decreasing. 23. Estimate the point(s) at which the graph of f has a local maximum or a local minimum. x y For the following exercises, consider the graph in Figure 17. 24. If the complete graph of the function is shown, estimate the intervals where the function is increasing or decreasing. 25. If the complete graph of the function is shown, estimate the absolute maximum and absolute minimum. x y Numeric 26. Table 3 gives the annual sales (in millions of dollars) of a product from 1998 to 2006. What was the average rate of change of annual sales (a) between 2001 and 2002, and (b) between 2001 and 2004? Year Sales (millions of dollars) 27. Table 4 gives the population of a town (in thousands) from 2000 to 2008. What was the average rate of change of population (a) between 2002 and 2004, and (b) between 2002 and 2006? Year Population (thousands)

For the following exercises, find the average rate of change of each function on the interval specified. 28. f (x) = x 2 on [1, 5] 29. h(x) = 5 - 2x 2 on [-2, 4] 30. q(x) = x³ on [-4, 2] 31. g (x) = 3x 3 - 1 on [-3, 3] _ x  on [1, 3] 33. p(t) =  (t 2 - 4)(t + 1)

____________ t 2 + 3  on [-3, 1] 34. k (t) = 6t² +  4/t³  on [-1, 3] Technology For the following exercises, use a graphing utility to estimate the local extrema of each function and to estimate the intervals on which the function is increasing and decreasing. 35. f(x) = x 4 - 4x 3 + 5 36. h(x) = x 5 + 5x 4 + 10x 3 + 10x 2 - 1 37. g(t) = t√t + 3  38. k(t) = 3t  2/3  - t 39. m(x) = x 4 + 2x 3 - 12x 2 - 10x + 4 40. n(x) = x 4 - 8x 3 + 18x 2 - 6x + 2 Extension 41. The graph of the function f is shown in Figure 18. Maximum

Based on the calculator screen shot, the point (1.333, 5.185) is which of the following? a. a relative (local) maximum of the function b. the vertex of the function c. the absolute maximum of the function d. a zero of the function 42. Let f (x) =  1/x . Find a number c such that the average rate of change of the function f on the interval (1, c) is - 1/4  43. Let f(x) =  1/x . Find the number b such that the average rate of change of f on the interval (2, b) is - 1/10 . Real-World Applications 44. At the start of a trip, the odometer on a car read 21,395. At the end of the trip, 13.5 hours later, the odometer read 22,125. Assume the scale on the odometer is in miles. What is the average speed the car traveled during this trip? 45. A driver of a car stopped at a gas station to fill up his gas tank. He looked at his watch, and the time read exactly 3:40 p.m. At this time, he started pumping gas into the tank. At exactly 3:44, the tank was full and he noticed that he had pumped 10.7 gallons. What is the average rate of flow of the gasoline into the gas tank? 46. Near the surface of the moon, the distance that an object falls is a function of time. It is given by d(t) = 2.6667t², where t is in seconds and d(t) is in feet. If an object is dropped from a certain height, find the average velocity of the object from t = 1 to t = 2. 47. The graph in Figure 19 illustrates the decay of a radioactive substance over t days. t A Time (days) Amount (milligrams) Use the graph to estimate the average decay rate from t = 5 to t = 15.

## 1.4 Composition of Functions

---
Suppose we want to calculate how much it costs to heat a house on a particular day of the year. The cost to heat a house will depend on the average daily temperature, and in turn, the average daily temperature depends on the particular day of the year. Notice how we have just defined two relationships: The cost depends on the temperature, and the temperature depends on the day. Using descriptive variables, we can notate these two functions. The function C(T) gives the cost C of heating a house for a given average daily temperature in T degrees Celsius. The function T(d) gives the average daily temperature on day d of the year. For any given day, Cost = C(T(d)) means that the cost depends on the temperature, which in turns depends on the day of the year. Thus, we can evaluate the cost function at the temperature T(d). For example, we could evaluate T(5) to determine the average daily temperature on the 5th day of the year. Then, we could evaluate the cost function at that temperature. We would write C(T(5)). Cost for the temperature Temperature on day 5 C(T(5)) By combining these two relationships into one function, we have performed function composition, which is the focus of this section. Combining Functions Using Algebraic Operations Function composition is only one way to combine existing functions. Another way is to carry out the usual algebraic operations on functions, such as addition, subtraction, multiplication and division. We do this by performing the operations with the function outputs, defining the result as the output of our new function. Suppose we need to add two columns of numbers that represent a husband and wife’s separate annual incomes over a period of years, with the result being their total household income. We want to do this for every year, adding only that year’s incomes and then collecting all the data in a new column. If w(y) is the wife’s income and h(y) is the husband’s income in year y, and we want T to represent the total income, then we can define a new function. T(y) = h(y) + w(y) If this holds true for every year, then we can focus on the relation between the functions without reference to a year and write T = h + w Just as for this sum of two functions, we can define difference, product, and ratio functions for any pair of functions that have the same kinds of inputs (not necessarily numbers) and also the same kinds of outputs (which do have to be numbers so that the usual operations of algebra can apply to them, and which also must have the same units or no units when we add and subtract). In this way, we can think of adding, subtracting, multiplying, and dividing functions. Learning Objectives
In this section, you will:
• Combine functions using algebraic operations.
• Create a new function by composition of functions.
• Evaluate composite functions.
• Find the domain of a composite function.
• Decompose a composite function into its component functions.
For two functions f (x) and g(x) with real number outputs, we define new functions f + g, f - g, fg, and  (f)/(g)  by the relations

(f + g)(x) = f (x) + g(x)

(f - g)(x) = f (x) - g(x)

(fg)(x) = f (x)g(x)

(  (f)/(g)  )(x) =  f (x) _ g(x) 

---
### 📐 **Example  1**: Performing Algebraic Operations on Functions

Find and simplify the functions (g - f)(x) and (  (g)/(f)  )(x), given f (x) = x - 1 and g(x) = x 2 - 1. Are they the same function?

**Solution**

Begin by writing the general form, and then substitute the given functions.

(g - f )(x) = g(x) - f (x)

(g - f )(x) = x 2 - 1 - (x - 1)

(g - f )(x) = x 2 - x

(g - f )(x) = x(x - 1)

(  (g)/(f)  )(x) =  g(x) _ f (x) 

(  (g)/(f)  )(x) =  x² - 1/x - 1  where x ≠  1

(  (g)/(f)  )(x) =  (x + 1)(x - 1)

____________ x - 1  where x ≠  1

(  (g)/(f)  )(x) = x + 1 where x ≠  1 No, the functions are not the same. Note: For (  (g)/(f)  )(x), the condition x ≠  1 is necessary because when x = 1, the denominator is equal to 0, which makes the function undefined.

---
### ✏️ **Try It #1**
Find and simplify the functions (fg)(x) and (f - g)(x). f (x) = x - 1 and g(x) = x 2 - 1 Are they the same function? Create a Function by Composition of Functions Performing algebraic operations on functions combines them into a new function, but we can also create functions by composing functions. When we wanted to compute a heating cost from a day of the year, we created a new function that takes a day as input and yields a cost as output. The process of combining functions so that the output of one function becomes the input of another is known as a composition of functions. The resulting function is known as a composite function. We represent this combination by the following notation: ( f ∘ g)(x) = f (g(x))

We read the left-hand side as “f composed with g at x,” and the right-hand side as “f of g of x.” The two sides of the equation have the same mathematical meaning and are equal. The open circle symbol ∘ is called the composition operator. We use this operator mainly when we wish to emphasize the relationship between the functions themselves without referring to any particular input value. Composition is a binary operation that takes two functions and forms a new function, much as addition or multiplication takes two numbers and gives a new number. However, it is important not to confuse function composition with multiplication because, as we learned above, in most cases f (g(x)) ≠  f (x)g(x). It is also important to understand the order of operations in evaluating a composite function. We follow the usual convention with parentheses by starting with the innermost parentheses first, and then working to the outside. In the equation above, the function g takes the input x first and yields an output g(x). Then the function f takes g(x) as an input and yields an output f (g(x)). x is the input of g g(x), the output of g is the input of f (f ° g)(x) = f(g(x)) In general, f ∘ g and g ∘ f are different functions. In other words, in many cases f ( g(x)) ≠  g(f (x)) for all x. We will also see that sometimes two functions can be composed only in one specific order. For example, if f (x) = x² and g(x) = x + 2, then

f (g(x)) = f (x + 2)

= (x + 2)²

= x² + 4x + 4 but

g(f (x)) = g(x²)

= x² + 2 These expressions are not equal for all values of x, so the two functions are not equal. It is irrelevant that the expressions happen to be equal for the single input value x = - 1/2 . Note that the range of the inside function (the first function to be evaluated) needs to be within the domain of the outside function. Less formally, the composition has to make sense in terms of inputs and outputs. composition of functions When the output of one function is used as the input of another, we call the entire operation a composition of functions. For any input x and functions f and g, this action defines a composite function, which we write as f ∘ g such that (f ∘ g)(x) = f (g(x)) The domain of the composite function f ∘ g is all x such that x is in the domain of g and g(x) is in the domain of f. It is important to realize that the product of functions fg is not the same as the function composition f (g(x)), because, in general, f (x)g(x) ≠  f (g(x)).

---
### 📐 **Example  2**
Determining whether Composition of Functions is Commutative Using the functions provided, find f (g(x)) and g(f (x)). Determine whether the composition of the functions is commutative. f (x) = 2x + 1 g(x) = 3 - x

**Solution**

Let’s begin by substituting g(x) into f (x).

f (g(x)) = 2(3 - x) + 1

= 6 - 2x + 1

= 7 - 2x Now we can substitute f (x) into g(x).

g(f (x)) = 3 - (2x + 1)

= 3 - 2x - 1

= - 2x + 2 We find that g(f (x)) ≠  f (g(x)), so the operation of function composition is not commutative.

---
### 📐 **Example  3**: Interpreting Composite Functions

The function c(s) gives the number of calories burned completing s sit-ups, and s(t) gives the number of sit-ups a person can complete in t minutes. Interpret c(s(3)).

**Solution**

The inside expression in the composition is s(3). Because the input to the s-function is time, t = 3 represents 3 minutes, and s(3) is the number of sit-ups completed in 3 minutes. Using s(3) as the input to the function c(s) gives us the number of calories burned during the number of sit-ups that can be completed in 3 minutes, or simply the number of calories burned in 3 minutes (by doing sit-ups).

---
### 📐 **Example  4**: Investigating the Order of Function Composition

Suppose f (x) gives miles that can be driven in x hours and g(y) gives the gallons of gas used in driving y miles. Which of these expressions is meaningful: f (g(y)) or g(f (x))?

**Solution**

The function y = f (x) is a function whose output is the number of miles driven corresponding to the number of hours driven. number of miles = f (number of hours) The function g(y) is a function whose output is the number of gallons used corresponding to the number of miles driven. This means: number of gallons = g (number of miles) The expression g(y) takes miles as the input and a number of gallons as the output. The function f (x) requires a number of hours as the input. Trying to input a number of gallons does not make sense. The expression f (g(y)) is meaningless. The expression f (x) takes hours as input and a number of miles driven as the output. The function g(y) requires a number of miles as the input. Using f (x) (miles driven) as an input value for g(y), where gallons of gas depends on miles driven, does make sense. The expression g(f (x)) makes sense, and will yield the number of gallons of gas used, g, driving a certain number of miles, f (x), in x hours. Are there any situations where f (g(y)) and g(f (x)) would both be meaningful or useful expressions ? Yes. For many pure mathematical functions, both compositions make sense, even though they usually produce different new functions. In real-world problems, functions whose inputs and outputs have the same units also may give compositions that are meaningful in either order.

---
### ✏️ **Try It #2**
The gravitational force on a planet a distance r from the sun is given by the function G(r). The acceleration of a planet subjected to any force F is given by the function a(F). Form a meaningful composition of these two functions, and explain what it means.

### Evaluating Composite Functions

Once we compose a new function from two existing functions, we need to be able to evaluate it for any input in its domain. We will do this with specific numerical inputs for functions expressed as tables, graphs, and formulas and with variables as inputs to functions expressed as formulas. In each case, we evaluate the inner function using the starting input and then use the inner function’s output as the input for the outer function. Evaluating Composite Functions Using Tables When working with functions given as tables, we read input and output values from the table entries and always work from the inside to the outside. We evaluate the inside function first and then use the output of the inside function as the input to the outside function.

---
### 📐 **Example  5**
Using a Table to Evaluate a Composite Function Using Table 1, evaluate f (g(3)) and g(f (3)). x f (x) g(x)

**Solution**

To evaluate f (g(3)), we start from the inside with the input value 3. We then evaluate the inside expression g(3) using the table that defines the function g: g(3) = 2. We can then use that result as the input to the function f, so g(3) is replaced by 2 and we get f (2). Then, using the table that defines the function f, we find that f (2) = 8.

g(3) = 2 f (g(3)) = f (2) = 8 To evaluate g(f (3)), we first evaluate the inside expression f (3) using the first table: f (3) = 3. Then, using the table for g, we can evaluate g(f (3)) = g(3) = 2 x g(x) f (g(x)) f (x) g(f (x))

---
### ✏️ **Try It #3**
Using Table 1, evaluate f (g(1)) and g(f (4)). Evaluating Composite Functions Using Graphs When we are given individual functions as graphs, the procedure for evaluating composite functions is similar to the process we use for evaluating tables. We read the input and output values, but this time, from the x- and y-axes of the graphs.

---
### 💡 **How To…**
Given a composite function and graphs of its individual functions, evaluate it using the information provided by the graphs. 1. Locate the given input to the inner function on the x-axis of its graph. 2. Read off the output of the inner function from the y-axis of its graph. 3. Locate the inner function output on the x-axis of the graph of the outer function. 4. Read the output of the outer function from the y-axis of its graph. This is the output of the composite function.

---
### 📐 **Example  6**
Using a Graph to Evaluate a Composite Function Using Figure 1, evaluate f (g(1)). x g(x) (a) x f(x) (b)

**Solution**

To evaluate f (g(1)), we start with the inside evaluation. See Figure 2. x g(x) x f (x) g(1) = 3 f (3) = 6 We evaluate g(1) using the graph of g(x), finding the input of 1 on the x-axis and finding the output value of the graph at that input. Here, g(1) = 3. We use this value as the input to the function f. f (g(1)) = f (3) We can then evaluate the composite function by looking to the graph of f (x), finding the input of 3 on the x-axis and reading the output value of the graph at this input. Here, f (3) = 6, so f ( g(1)) = 6.

**Analysis**
x g(x) x f(x)

---
### ✏️ **Try It #4**
Using Figure 1, evaluate g(f (2)). Evaluating Composite Functions Using Formulas When evaluating a composite function where we have either created or been given formulas, the rule of working from the inside out remains the same. The input value to the outer function will be the output of the inner function, which may be a numerical value, a variable name, or a more complicated expression. While we can compose the functions for each individual input value, it is sometimes helpful to find a single formula that will calculate the result of a composition f ( g(x)). To do this, we will extend our idea of function evaluation. Recall that, when we evaluate a function like f (t) = t² - t, we substitute the value inside the parentheses into the formula wherever we see the input variable.

---
### 💡 **How To…**
Given a formula for a composite function, evaluate the function. 1. Evaluate the inside function using the input value or variable provided. 2. Use the resulting output as the input to the outside function.

---
### 📐 **Example  7**
Evaluating a Composition of Functions Expressed as Formulas with a Numerical Input Given f (t) = t² - t and h(x) = 3x + 2, evaluate f (h(1)).

**Solution**

Because the inside expression is h(1), we start by evaluating h(x) at 1.

h(1) = 3(1) + 2

h(1) = 5 Then f (h(1)) = f (5), so we evaluate f (t) at an input of 5.

f (h(1)) = f (5)

f (h(1)) = 52 - 5

f (h(1)) = 20 Analysis It makes no difference what the input variables t and x were called in this problem because we evaluated for specific numerical values.

---
### ✏️ **Try It #5**
Given f (t) = t 2 - t and h(x) = 3x + 2, evaluate a. h(f (2)) b. h(f (-2)) Finding the Domain of a Composite Function As we discussed previously, the domain of a composite function such as f ∘ g is dependent on the domain of g and the domain of f. It is important to know when we can apply a composite function and when we cannot, that is, to know the domain of a function such as f ∘ g. Let us assume we know the domains of the functions f and g separately. If we write the composite function for an input x as f (g(x)), we can see right away that x must be a member of the domain of g in order for the expression to be meaningful, because otherwise we cannot complete the inner function evaluation. However, we also see that g(x) must be a member of the domain of f, otherwise the second function evaluation in f (g(x)) cannot be completed, and the expression is still undefined. Thus the domain of f ∘ g consists of only those inputs in the domain of g that produce outputs from g belonging to the domain of f. Note that the domain of f composed with g is the set of all x such that x is in the domain of g and g(x) is in the domain of f. domain of a composite function The domain of a composite function f (g(x)) is the set of those inputs x in the domain of g for which g(x) is in the domain of f.

---
### 💡 **How To…**
Given a function composition f (g(x)), determine its domain. 1. Find the domain of g. 2. Find the domain of f. 3. Find those inputs x in the domain of g for which g(x) is in the domain of f. That is, exclude those inputs x from the domain of g for which g(x) is not in the domain of f. The resulting set is the domain of f ∘ g.

---
### 📐 **Example  8**: Finding the Domain of a Composite Function

Find the domain of (f ∘ g)(x) where f (x) =  5 ____ x - 1  and g(x) =  _____ 3x - 2

**Solution**

The domain of g(x) consists of all real numbers except x =  2/3 , since that input value would cause us to divide by 0. Likewise, the domain of f consists of all real numbers except 1. So we need to exclude from the domain of g(x) that value of x for which g(x) = 1.

 _____ 3x - 2  = 1

4 = 3x - 2

6 = 3x

x = 2 So the domain of f ∘ g is the set of all real numbers except  2/3  and 2. This means that x ≠   2/3  or x ≠  2 We can write this in interval notation as ( - ∞ ,  2/3  ) ∪ (  2/3 , 2 ) ∪ (2, ∞ )

Finding the Domain of a Composite Function Involving Radicals Find the domain of (f ∘ g)(x) where f (x) = √x + 2  and g(x) = √3 - x

**Solution**

Because we cannot take the square root of a negative number, the domain of g is (-∞ , 3]. Now we check the domain of the composite function (f ∘ g)(x) = √___________ √3 - x +2  For (f ∘ g)(x) = √___________ √3 - x +2  , √3 - x +2 ≥  0, since the radicand of a square root must be positive. Since the square roots are positive, √3 - x  ≥  0, 3 - x ≥  0, which gives a domain of (-∞ , 3]. Analysis This example shows that knowledge of the range of functions (specifically the inner function) can also be helpful in finding the domain of a composite function. It also shows that the domain of f ∘ g can contain values that are not in the domain of f, though they must be in the domain of g.

---
### ✏️ **Try It #6**
Find the domain of (f ∘ g)(x) where f (x) =  1 ____ x - 2  and g(x) = √x + 4  Decomposing a Composite Function into its Component Functions In some cases, it is necessary to decompose a complicated function. In other words, we can write it as a composition of two simpler functions. There may be more than one way to decompose a composite function, so we may choose the decomposition that appears to be most expedient.

---
### 📐 **Example  9**: Decomposing a Function

Write f (x) = √5 - x 2  as the composition of two functions.

**Solution**

We are looking for two functions, g and h, so f (x) = g(h(x)). To do this, we look for a function inside a function in the formula for f (x). As one possibility, we might notice that the expression 5 - x² is the inside of the square root. We could then decompose the function as h(x) = 5 - x² and g(x) = √x  We can check our answer by recomposing the functions. g(h(x)) = g(5 - x²) = √5 - x² 

---
### ✏️ **Try It #7**
Write f (x) =  __

3 - √4 + x²   as the composition of two functions. Access these online resources for additional instruction and practice with composite functions. • Composite Functions (http://openstaxcollege.org/l/compfunction) • Composite Function Notation Application (http://openstaxcollege.org/l/compfuncnot) • Composite Functions Using Graphs (http://openstaxcollege.org/l/compfuncgraph) • Decompose Functions (http://openstaxcollege.org/l/decompfunction) • Composite Function Values (http://openstaxcollege.org/l/compfuncvalue)

### 1.4 section EXERCISES

Verbal 1. How does one find the domain of the quotient of two functions,  (f)/(g) ? 2. What is the composition of two functions, f ∘ g ? 3. If the order is reversed when composing two functions, can the result ever be the same as the answer in the original order of the composition ? If yes, give an example. If no, explain why not. 4. How do you find the domain for the composition of two functions, f ∘ g ? Algebraic 5. Given f (x) = x 2 + 2x and g(x) = 6 - x 2, find f + g, f - g, fg, and  (f)/(g) . Determine the domain for each function in interval notation. 6. Given f (x) = -3x² + x and g(x) = 5, find f + g, f - g, fg, and  (f)/(g) . Determine the domain for each function in interval notation. 7. Given f (x) = 2x 2 + 4x and g(x) =  1/2x , find f + g, f - g, fg, and  (f)/(g) . Determine the domain for each function in interval notation. 8. Given f (x) =  _ x - 4 and g(x) =  1/6 - x , find f + g, f - g, fg, and  (f)/(g) . Determine the domain for each function in interval notation. 9. Given f (x) = 3x 2 and g(x) = √x - 5 , find f + g, f - g, fg, and  (f)/(g) . Determine the domain for each function in interval notation. 10. Given f (x) = √x  and g(x) = |x - 3|, find  (g)/(f) . Determine the domain for each function in interval notation. 11. Given f (x) = 2x 2 + 1 and g(x) = 3x - 5, find the following: a. f ( g(2)) b. f ( g(x)) c. g( f (x)) d. ( g ∘ g)(x) e. ( f ∘ f )(-2) For the following exercises, use each pair of functions to find f (g(x)) and g(f (x)). Simplify your answers. 12. f (x) = x 2 + 1, g(x) = √x + 2  13. f (x) = √x  + 2, g(x) = x 2 + 3 14. f (x) = |x|, g(x) = 5x + 1 15. f (x) =  √x , g(x) =  x + 1/x³  16. f (x) =  1/x - 6 , g(x) =  7/x  + 6 17. f (x) =  1 ___ x-4 , g(x) =  2/x  + 4 For the following exercises, use each set of functions to find f (g(h(x))). Simplify your answers. 18. f (x) = x  4 + 6, g(x) = x - 6, and h(x) = √x  19. f (x) = x 2 + 1, g(x) =  1/x  , and h(x) = x + 3 20. Given f (x) =  1/x , and g(x) = x - 3, find the following: a. ( f ∘ g)(x) b. the domain of ( f ∘ g)(x) in interval notation c. ( g ∘ f )(x) d. the domain of ( g ∘ f )(x) e. (  (f)/(g)  )x 21. Given f (x) = √2 - 4x  and g(x) = - 3/x , find the following: a. ( g ∘ f )(x) b. the domain of ( g ∘ f )(x) in interval notation

## 1.4 Section Exercises

---
22. Given the functions f (x) =  1 - (x)/(x)  and g(x) =  _ 1 + x² , find the following: a. ( g ∘ f )(x) b. ( g ∘ f )(2) 23. Given functions p(x) =  1 _ √x   and m(x) = x 2 - 4, state the domain of each of the following functions using interval notation: a.  p(x) _ m(x)  b. p(m(x)) c. m(p(x)) 24. Given functions q(x) =  1 _ √x   and h(x) = x 2 - 9, state the domain of each of the following functions using interval notation. a.  q(x) _ h(x)  b. q(h(x)) c. h(q(x)) 25. For f (x) =  1/x  and g(x) = √x - 1 , write the domain of ( f ∘ g)(x) in interval notation. For the following exercises, find functions f (x) and g(x) so the given function can be expressed as h(x) = f (g(x)). 26. h(x) = (x + 2)² 27. h(x) = (x - 5)³ 28. h(x) =  3/x - 5  29. h(x) =  _______ (x + 2)²  30. h(x) = 4 +  √x  31. h(x) = √_______  ______ 2x - 3   32. h(x) =  _ (3x 2 - 4)-3  33. h(x) = √_______  3x - 2 ______ x + 5   34. h(x) = (  8 + x 3/8 - x 3  ) 35. h(x) = √2x + 6  36. h(x) = (5x - 1)³ 37. h(x) =  √x - 1  38. h(x) = |x 2 + 7| 39. h(x) =  _ (x - 2)³  40. h(x) = (  _ 2x - 3  ) 41. h(x) = √_______  2x - 1/3x + 4   Graphical For the following exercises, use the graphs of f, shown in Figure 4, and g, shown in Figure 5, to evaluate the expressions. f(x) x f f(x) x g 42. f ( g(3)) 43. f ( g(1)) 44. g( f (1)) 45. g( f (0)) 46. f ( f (5)) 47. f ( f (4)) 48. g( g(2)) 49. g( g(0))

For the following exercises, use graphs of f (x), shown in Figure 6, g(x), shown in Figure 7, and h(x), shown in Figure 8, to evaluate the expressions. f(x) x f(x) g(x) x f(x) h(x) x f(x) 50. g( f (1)) 51. g( f (2)) 52. f ( g(4)) 53. f ( g(1)) 54. f (h(2)) 55. h( f (2)) 56. f ( g(h(4))) 57. f ( g( f (-2))) Numeric For the following exercises, use the function values for f and g shown in Table 3 to evaluate each expression. x f (x) g(x) 58. f ( g(8)) 59. f ( g(5)) 60. g( f (5)) 61. g( f (3)) 62. f ( f (4)) 63. f ( f (1)) 64. g( g(2)) 65. g( g(6)) For the following exercises, use the function values for f and g shown in Table 4 to evaluate the expressions. x -3 -2 -1 f (x) -1 g(x) -8 -3 -3 -8 66. ( f ∘ g)(1) 67. ( f ∘ g)(2) 68. ( g ∘ f )(2) 69. ( g ∘ f )(3) 70. ( g ∘ g )(1) 71. ( f ∘ f )(3) For the following exercises, use each pair of functions to find f (g(0)) and g(f (0)). 72. f (x) = 4x + 8, g(x) = 7 - x² 73. f (x) = 5x + 7, g(x) = 4 - 2x² 74. f (x) = √x + 4 , g(x) = 12 - x³ 75. f (x) =  1/x + 2 , g(x) = 4x + 3 For the following exercises, use the functions f (x) = 2x² + 1 and g(x) = 3x + 5 to evaluate or find the composite function as indicated. 76. f ( g(2)) 77. f ( g(x)) 78. g( f ( - 3)) 79. ( g ∘ g )(x)

Extensions For the following exercises, use f (x) = x³ + 1 and g(x) =  √x - 1 . 80. Find ( f ∘ g)(x) and ( g ∘ f )(x). Compare the two answers. 81. Find ( f ∘ g)(2) and ( g ∘ f )(2). 82. What is the domain of ( g ∘ f )(x) ? 83. What is the domain of ( f ∘ g)(x) ? 84. Let f (x) =  1/x . a. Find ( f ∘ f )(x). b. Is ( f ∘ f )(x) for any function f the same result as the answer to part (a) for any function ? Explain. For the following exercises, let F (x) = (x + 1)⁵, f (x) = x⁵, and g(x) = x + 1. 85. True or False: ( g ∘ f )(x) = F (x). 86. True or False: ( f ∘ g )(x) = F (x). For the following exercises, find the composition when f (x) = x² + 2 for all x ≥  0 and g(x) = √x - 2 . 87. ( f ∘ g)(6) ; ( g ∘ f )(6) 88. ( g ∘ f )(a) ; ( f ∘ g )(a) 89. ( f ∘ g )(11) ; (g ∘ f )(11) Real-World Applications 90. The function D(p) gives the number of items that will be demanded when the price is p. The production cost C(x) is the cost of producing x items. To determine the cost of production when the price is $6, you would do which of the following ? a. Evaluate D(C(6)). b. Evaluate C(D(6)). c. Solve D(C(x)) = 6. d. Solve C(D(p)) = 6. 91. The function A(d) gives the pain level on a scale of 0 to 10 experienced by a patient with d milligrams of a pain- reducing drug in her system. The milligrams of the drug in the patient’s system after t minutes is modeled by m(t). Which of the following would you do in order to determine when the patient will be at a pain level of 4 ? a. Evaluate A(m(4)). b. Evaluate m(A(4)). c. Solve A(m(t)) = 4. d. Solve m(A(d)) = 4. 92. A store offers customers a 30 % discount on the price x of selected items. Then, the store takes off an additional 15 % at the cash register. Write a price function P(x) that computes the final price of the item in terms of the original price x. (Hint: Use function composition to find your answer.) 93. A rain drop hitting a lake makes a circular ripple. If the radius, in inches, grows as a function of time in minutes according to r(t) = 25 

√t + 2 , find the area of the ripple as a function of time. Find the area of the ripple at t = 2. 94. A forest fire leaves behind an area of grass burned in an expanding circular pattern. If the radius of the circle of burning grass is increasing with time according to the formula r(t) = 2t + 1, express the area burned as a function of time, t (minutes). 95. Use the function you found in the previous exercise to find the total area burned after 5 minutes. 96. The radius r, in inches, of a spherical balloon is related to the volume, V, by r(V) = 3√___

 3V ___ 4π   . Air is pumped into the balloon, so the volume after t seconds is given by V(t) = 10 + 20t. a. Find the composite function r(V(t)). b. Find the exact time when the radius reaches 10 inches. 97. The number of bacteria in a refrigerated food product is given by N(T) = 23T 2 - 56T + 1, 3 < T < 33, where T is the temperature of the food. When the food is removed from the refrigerator, the temperature is given by T(t) = 5t + 1.5, where t is the time in hours. a. Find the composite function N(T(t)). b. Find the time (round to two decimal places) when the bacteria count reaches 6,752.

1. 5 Transformation of Functions We all know that a flat mirror enables us to see an accurate image of ourselves and whatever is behind us. When we tilt the mirror, the images we see may shift horizontally or vertically. But what happens when we bend a flexible mirror? Like a carnival funhouse mirror, it presents us with a distorted image of ourselves, stretched or compressed horizontally or vertically. In a similar way, we can distort or transform mathematical functions to better adapt them to describing objects or processes in the real world. In this section, we will take a look at several kinds of transformations. Graphing Functions Using Vertical and Horizontal Shifts Often when given a problem, we try to model the scenario using mathematics in the form of words, tables, graphs, and equations. One method we can employ is to adapt the basic graphs of the toolkit functions to build new models for a given scenario. There are systematic ways to alter functions to construct appropriate models for the problems we are trying to solve. Identifying Vertical Shifts One simple kind of transformation involves shifting the entire graph of a function up, down, right, or left. The simplest shift is a vertical shift, moving the graph up or down, because this transformation involves adding a positive or negative constant to the function. In other words, we add the same constant to the output value of the function regardless of the input. For a function g (x) = f (x) + k, the function f (x) is shifted vertically k units. See Figure 2 for an example. Learning Objectives
In this section, you will:
• Graph functions using vertical and horizontal shifts.
• Graph functions using reflections about the x-axis and the y-axis.
• Determine whether a function is even, odd, or neither from its graph.
• Graph functions using compressions and stretches.
• Combine transformations.
