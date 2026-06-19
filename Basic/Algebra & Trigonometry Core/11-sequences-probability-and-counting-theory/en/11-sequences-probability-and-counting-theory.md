# Sequences, Probability, and Counting Theory

## Introduction
A lottery winner has some big decisions to make regarding what to do with the winnings. Buy a villa in Saint Barthélemy? A luxury convertible? A cruise around the world? The likelihood of winning the lottery is slim, but we all love to fantasize about what we could buy with the winnings. One of the first things a lottery winner has to decide is whether to take the winnings in the form of a lump sum or as a series of regular payments, called an annuity, over the next 30 years or so. This decision is often based on many factors, such as tax implications, interest rates, and investment strategies. There are also personal reasons to consider when making the choice, and one can make many arguments for either decision. However, most lottery winners opt for the lump sum. In this chapter, we will explore the mathematics behind situations such as these. We will take an in-depth look at annuities. We will also look at the branch of mathematics that would allow us to calculate the number of ways to choose lottery numbers and the probability of winning. Sequences, Probability and Counting Theory

Learning Objectives
In this section, you will:
• Write the terms of a sequence defined by an explicit formula.
• Write the terms of a sequence defined by a recursive formula.
• Use factorial notation.

## 11.1 Sequences and Their Notations
A video game company launches an exciting new advertising campaign. They predict the number of online visits to their website, or hits, will double each day. The model they are using shows 2 hits the first day, 4 hits the second day, 8 hits the third day, and so on. See Table 1. Day Hits If their model continues, how many hits will there be at the end of the month? To answer this question, we’ll first need to know how to determine a list of numbers written in a specific order. In this section, we will explore these kinds of ordered lists. Writing the Terms of a Sequence Defined by an Explicit Formula One way to describe an ordered list of numbers is as a sequence. A sequence is a function whose domain is a subset of the counting numbers. The sequence established by the number of hits on the website is The ellipsis (...) indicates that the sequence continues indefinitely. Each number in the sequence is called a term. The first five terms of this sequence are 2, 4, 8, 16, and 32. Listing all of the terms for a sequence can be cumbersome. For example, finding the number of hits on the website at the end of the month would require listing out as many as 31 terms. A more efficient way to determine a specific term is by writing a formula to define the sequence. One type of formula is an explicit formula, which defines the terms of a sequence using their position in the sequence. Explicit formulas are helpful if we want to find a specific term of a sequence without finding all of the previous terms. We can use the formula to find the nth term of the sequence, where n is any positive number. In our example, each number in the sequence is double the previous number, so we can use powers of 2 to write a formula for the nth term.

↓ ↓ ↓ ↓ ↓ ↓

The first term of the sequence is 21 = 2, the second term is 22 = 4, the third term is 23 = 8, and so on. The nth term of the sequence can be found by raising 2 to the nth power. An explicit formula for a sequence is named by a lower case letter a, b, c... with the subscript n. The explicit formula for this sequence is

an = 2n . Now that we have a formula for the nth term of the sequence, we can answer the question posed at the beginning of this section. We were asked to find the number of hits at the end of the month, which we will take to be 31 days. To find the number of hits on the last day of the month, we need to find the 31st term of the sequence. We will substitute 31 for n in the formula.

If the doubling trend continues, the company will get 2,147,483,648 hits on the last day of the month. That is over 2.1 billion hits! The huge number is probably a little unrealistic because it does not take consumer interest and competition into account. It does, however, give the company a starting point from which to consider business decisions. Another way to represent the sequence is by using a table. The first five terms of the sequence and the nth term of the sequence are shown in Table 2. n n nth term of the sequence, an 2n Graphing provides a visual representation of the sequence as a set of distinct points. We can see from the graph in Figure 1 that the number of hits is rising at an exponential rate. This particular sequence forms an exponential function. n an Lastly, we can write this particular sequence as A sequence that continues indefinitely is called an infinite sequence. The domain of an infinite sequence is the set of counting numbers. If we consider only the first 10 terms of the sequence, we could write This sequence is called a finite sequence because it does not continue indefinitely. sequence A sequence is a function whose domain is the set of positive integers. A finite sequence is a sequence whose domain consists of only the first n positive integers. The numbers in a sequence are called terms. The variable a with a number subscript is used to represent the terms in a sequence and to indicate the position of the term in the sequence. We call a^{1} the first term of the sequence, a^{2} the second term of the sequence, a^{3} the third term of the sequence, and so on. The term an is called the nth term of the sequence, or the general term of the sequence. An explicit formula defines the nth term of a sequence using the position of the term. A sequence that continues indefinitely is an infinite sequence. Does a sequence always have to begin with a^{1}? No. In certain problems, it may be useful to define the initial term as a^{0} instead of a^{1}. In these problems, the domain of the function includes 0.


**How To…**
Given an explicit formula, write the first n terms of a sequence. 1. Substitute each value of n into the formula. Begin with n = 1 to find the first term, a^{1}. 2. To find the second term, a^{2}, use n = 2. 3. Continue in the same manner until you have identified all n terms.

**Example  1**

### Writing the Terms of a Sequence Defined by an Explicit Formula
Write the first five terms of the sequence defined by the explicit formula an = -3n + 8. Solution Substitute n = 1 into the formula. Repeat with values 2 through 5 for n.

n = 1 a^{1} = -3(1) + 8 = 5

n = 2 a^{2} = -3(2) + 8 = 2

n = 3 a^{3} = -3(3) + 8 = -1

n = 4 a^{4} = -3(4) + 8 = -4

n = 5 a^{5} = -3(5) + 8 = -7 The first five terms are {5, 2, -1, -4, -7}. Analysis The sequence values can be listed in a table. A table, such as Table 3, is a convenient way to input the function into a graphing utility. n an -1 -4 -7 A graph can be made from this table of values. From the graph in Figure 2, we can see that this sequence represents a linear function, but notice the graph is not continuous because the domain is over the positive integers only. an n

**Try It #1**
Write the first five terms of the sequence defined by the explicit formula tn = 5n - 4.


### Investigating Alternating Sequences
Sometimes sequences have terms that are alternate. In fact, the terms may actually alternate in sign. The steps to finding terms of the sequence are the same as if the signs did not alternate. However, the resulting terms will not show increase or decrease as n increases. Let’s take a look at the following sequence. Notice the first term is greater than the second term, the second term is less than the third term, and the third term is greater than the fourth term. This trend continues forever. Do not rearrange the terms in numerical order to interpret the sequence.

**How To…**
Given an explicit formula with alternating terms, write the first n terms of a sequence. 1. Substitute each value of n into the formula. Begin with n = 1 to find the first term, a^{1}. The sign of the term is given by the (-1)n in the explicit formula. 2. To find the second term, a^{2}, use n = 2. 3. Continue in the same manner until you have identified all n terms.

**Example  2**

### Writing the Terms of an Alternating Sequence Defined by an Explicit Formula
Write the first five terms of the sequence.

an =  (-1)n n 2 _______ n + 1  Solution Substitute n = 1, n = 2, and so on in the formula.

n = 1 a^{1} =  (-1)^{1} 12 _______ 1 + 1  = - 1 __ 2 

n = 2 a^{2} =  (-1)^{2} 22 _______ 2 + 1  =  4 __ 3 

n = 3 a^{3} =  (-1)^{3} 32 _______ 3 + 1  = - 9 __ 4 

n = 4 a^{4} =  (-1)^{4} 42 _______ 4 + 1  =  16 __ 5 

n = 5 a^{5} =  (-1)^{5} 52 _______ 5 + 1  = - 25 ___ 6  The first five terms are  - 1 __ 2 ,  4 __ 3 , - 9 __ 4 ,  16 ___ ___ 6   Analysis The graph of this function, shown in Figure 3, looks different from the ones we have seen previously in this section because the terms of the sequence alternate between positive and negative values. an n

In Example 2, does the (-1) to the power of n account for the oscillations of signs? Yes, the power might be n, n + 1, n - 1, and so on, but any odd powers will result in a negative term, and any even power will result in a positive term.

**Try It #2**
Write the first five terms of the sequence. an =  4n _____ (-2)n  Investigating Piecewise Explicit Formulas We’ve learned that sequences are functions whose domain is over the positive integers. This is true for other types of functions, including some piecewise functions. Recall that a piecewise function is a function defined by multiple subsections. A different formula might represent each individual subsection.

**How To…**
Given an explicit formula for a piecewise function, write the first n terms of a sequence 1. Identify the formula to which n = 1 applies. 2. To find the first term, a^{1}, use n = 1 in the appropriate formula. 3. Identify the formula to which n = 2 applies. 4. To find the second term, a^{2}, use n = 2 in the appropriate formula. 5. Continue in the same manner until you have identified all n terms.

**Example  3**

### Writing the Terms of a Sequence Defined by a Piecewise Explicit Formula
Write the first six terms of the sequence.

an = { n^{2} if n is not divisible by 3

 n __ 3  if n is divisible by 3

  Solution Substitute n = 1, n = 2, and so on in the appropriate formula. Use n^{2} when n is not a multiple of 3. Use  n _ 3  when n is a multiple of 3.

1 is not a multiple of 3. Use n^{2}.

2 is not a multiple of 3. Use n^{2}.

a^{3} =  3 __ 3  = 1 3 is a multiple of 3. Use  n __ 3 .

4 is not a multiple of 3. Use n^{2}.

5 is not a multiple of 3. Use n^{2}.

a^{6} =  6 __ 3  = 2 6 is a multiple of 3. Use  n __ 3 . The first six terms are {1, 4, 1, 16, 25, 2}. Analysis Every third point on the graph shown in Figure 4 stands out from the two nearby points. This occurs because the sequence was defined by a piecewise function. an n


**Try It #3**
Write the first six terms of the sequence. an = { 2n^{3} if n is odd

 5n ___ 2  if n is even   Finding an Explicit Formula Thus far, we have been given the explicit formula and asked to find a number of terms of the sequence. Sometimes, the explicit formula for the nth term of a sequence is not given. Instead, we are given several terms from the sequence. When this happens, we can work in reverse to find an explicit formula from the first few terms of a sequence. The key to finding an explicit formula is to look for a pattern in the terms. Keep in mind that the pattern may involve alternating terms, formulas for numerators, formulas for denominators, exponents, or bases.

**How To…**
Given the first few terms of a sequence, find an explicit formula for the sequence. 1. Look for a pattern among the terms. 2. If the terms are fractions, look for a separate pattern among the numerators and denominators. 3. Look for a pattern among the signs of the terms. 4. Write a formula for an in terms of n. Test your formula for n = 1, n = 2, and n = 3.

**Example  4**

### Writing an Explicit Formula for the nth Term of a Sequence
Write an explicit formula for the nth term of each sequence. a.  - 2 ___ ___ ___ ___ ___ b.  - 2 ___ ___ ___ _____ ______ Solution Look for the pattern in each sequence. a. The terms alternate between positive and negative. We can use (-1)n to make the terms alternate. The numerator can be represented by n + 1. The denominator can be represented by 2n + 9.

an =  (-1)n (n + 1) ___________ 2n + 9  b. The terms are all negative.

 - 2 ___ ___ ___ _____ ______ The numerator is 2

 - 2 __ __ __ __ __ __ __ 5n   The denominators are increasing powers of 5 So we know that the fraction is negative, the numerator is 2, and the denominator can be represented by 5 n + 1.

an = - 2 ______ 5 n + 1  c. The terms are powers of e. For n = 1, the first term is e 4 so the exponent must be n + 3. an = e n + 3

**Try It #4**
Write an explicit formula for the nth term of the sequence.


**Try It #5**
Write an explicit formula for the nth term of the sequence.  - 3 __ 4 , - 9 __ 8 , - 27 ___ ___ ___

**Try It #6**
Write an explicit formula for the nth term of the sequence.   1 __ e^{2} ,  1 _ e , 1, e, e 2, ...  Writing the Terms of a Sequence Defined by a Recursive Formula Sequences occur naturally in the growth patterns of nautilus shells, pinecones, tree branches, and many other natural structures. We may see the sequence in the leaf or branch arrangement, the number of petals of a flower, or the pattern of the chambers in a nautilus shell. Their growth follows the Fibonacci sequence, a famous sequence in which each term can be found by adding the preceding two terms. The numbers in the sequence are 1, 1, 2, 3, 5, 8, 13, 21, 34,.... Other examples from the natural world that exhibit the Fibonacci sequence are the Calla Lily, which has just one petal, the Black-Eyed Susan with 13 petals, and different varieties of daisies that may have 21 or 34 petals. Each term of the Fibonacci sequence depends on the terms that come before it. The Fibonacci sequence cannot easily be written using an explicit formula. Instead, we describe the sequence using a recursive formula, a formula that defines the terms of a sequence using previous terms. A recursive formula always has two parts: the value of an initial term (or terms), and an equation defining an in terms of preceding terms. For example, suppose we know the following:

a^{1} = 3

an = 2an - 1 - 1, for n \ge  2 We can find the subsequent terms of the sequence using the first term.

a^{1} = 3

a^{2} = 2a^{1} - 1 = 2(3) - 1 = 5

a^{3} = 2a^{2} - 1 = 2(5) - 1 = 9

a^{4} = 2a^{3} - 1 = 2(9) - 1 = 17 So the first four terms of the sequence are {3, 5, 9, 17} . The recursive formula for the Fibonacci sequence states the first two terms and defines each successive term as the sum of the preceding two terms.

a^{1} = 1

a^{2} = 1

an = an - 1 + an - 2 for n \ge  3 To find the tenth term of the sequence, for example, we would need to add the eighth and ninth terms. We were told previously that the eighth and ninth terms are 21 and 34, so

recursive formula A recursive formula is a formula that defines each term of a sequence using preceding term(s ). Recursive formulas must always state the initial term, or terms, of the sequence.

Must the first two terms always be given in a recursive formula? No. The Fibonacci sequence defines each term using the two preceding terms, but many recursive formulas define each term using only one preceding term. These sequences need only the first term to be defined.

**How To…**
Given a recursive formula with only the first term provided, write the first n terms of a sequence. 1. Identify the initial term, a^{1}, which is given as part of the formula. This is the first term. 2. To find the second term, a^{2}, substitute the initial term into the formula for an - 1. Solve. 3. To find the third term, a^{3}, substitute the second term into the formula. Solve. 4. Repeat until you have solved for the nth term.

**Example  5**

### Writing the Terms of a Sequence Defined by a Recursive Formula
Write the first five terms of the sequence defined by the recursive formula.

a^{1} = 9

an = 3an - 1 - 20, for n \ge  2 Solution The first term is given in the formula. For each subsequent term, we replace an - 1 with the value of the preceding term.

n = 1 a^{1} = 9

n = 2

n = 3

n = 4 a^{4} = 3a^{3} - 20 = 3(1) - 20 = 3 - 20 = -17

n = 5 The first five terms are {9, 7, 1, – 17, – 71}. See Figure 5. -20 -40 -60 n an -1 -80

**Try It #7**
Write the first five terms of the sequence defined by the recursive formula.

a^{1} = 2

an = 2an - 1 + 1, for n \ge  2

**How To…**
Given a recursive formula with two initial terms, write the first n terms of a sequence. 1. Identify the initial term, a^{1}, which is given as part of the formula. 2. Identify the second term, a^{2}, which is given as part of the formula. 3. To find the third term, substitute the initial term and the second term into the formula. Evaluate. 4. Repeat until you have evaluated the nth term.


**Example  6**

### Writing the Terms of a Sequence Defined by a Recursive Formula
Write the first six terms of the sequence defined by the recursive formula.

a^{1} = 1

a^{2} = 2

an = 3an - 1 + 4an - 2, for n \ge  3 Solution The first two terms are given. For each subsequent term, we replace an - 1 and an - 2 with the values of the two preceding terms.

n = 3 a^{3} = 3a^{2} + 4a^{1} = 3(2) + 4(1) = 10

n = 4

n = 5

n = 6 The first six terms are {1, 2, 10, 38, 154, 614}. See Figure 6. n an

**Try It #8**
Write the first 8 terms of the sequence defined by the recursive formula.

a^{1} = 0

a^{2} = 1

a^{3} = 1

an =  an - 1 _____ an - 2  + an - 3, for n \ge  4 Using Factorial Notation The formulas for some sequences include products of consecutive positive integers. n factorial, written as n!, is the product of the positive integers from 1 to n. For example,

4! = 4 ⋅ 3 ⋅ 2 ⋅ 1 = 24

5! = 5 ⋅ 4 ⋅ 3 ⋅ 2 ⋅ 1 = 120 An example of formula containing a factorial is an = (n + 1)!. The sixth term of the sequence can be found by substituting 6 for n.

a^{6} = (6 + 1)! = 7! = 7 \cdot  6 \cdot  5 \cdot  4 \cdot  3 \cdot  2 \cdot  1 = 5,040 The factorial of any whole number n is n(n - 1)! We can therefore also think of 5! as 5 ⋅ 4!.

n factorial n factorial is a mathematical operation that can be defined using a recursive formula. The factorial of n, denoted n!, is defined for a positive integer n as:

0! = 1

1! = 1

n ! = n(n - 1)(n - 2) ⋯ (2)(1), for n \ge  2 The special case 0! is defined as 0! = 1. Can factorials always be found using a calculator? No. Factorials get large very quickly—faster than even exponential functions! When the output gets too large for the calculator, it will not be able to calculate the factorial.

**Example  7**

### Writing the Terms of a Sequence Using Factorials
Write the first five terms of the sequence defined by the explicit formula an =  5n _______ (n + 2)! . Solution Substitute n = 1, n = 2, and so on in the formula.

n = 1 a^{1} =  5(1) _______ (1 + 2)!  =  5 __ 3!  =  ______ 3 \cdot  2 \cdot  1  =  5 __ 6 

n = 2 a^{2} =  5(2) _______ (2 + 2)!  =  10 ___ 4!  =  _________ 4 \cdot  3 \cdot  2 \cdot  1  =  5 ___ 12 

n = 3 a^{3} =  5(3) _______ (3 + 2)!  =  15 ___ 5!  =  ___________ 5 \cdot  4 \cdot  3 \cdot  2 \cdot  1  =  1 __ 8 

n = 4 a^{4} =  5(4) _______ (4 + 2)!  =  20 ___ 6!  =  _____________

6 \cdot  5 \cdot  4 \cdot  3 \cdot  2 \cdot  1  =  1 ___ 36 

n = 5 a^{5} =  5(5) _______ (5 + 2)!  =  25 ___ 7!  =  _______________

7 \cdot  6 \cdot  5 \cdot  4 \cdot  3 \cdot  2 \cdot  1  =  5 _____ The first five terms are   5 __ 6 ,  5 ___ __ 8 ,  1 ___ _____ Analysis Figure 7 shows the graph of the sequence. Notice that, since factorials grow very quickly, the presence of the factorial term in the denominator results in the denominator becoming much larger than the numerator as n increases. This means the quotient gets smaller and, as the plot of the terms shows, the terms are decreasing and nearing zero. n an

**Try It #9**
Write the first five terms of the sequence defined by the explicit formula an =  (n + 1)! _______ 2n . > Access this online resource for additional instruction and practice with sequences. • Finding Terms in a Sequence (http://openstaxcollege.org/l/findingterms)


### 11.1 Section Exercises
Verbal 1. Discuss the meaning of a sequence. If a finite sequence is defined by a formula, what is its domain? What about an infinite sequence? 2. Describe three ways that a sequence can be defined. 3. Is the ordered set of even numbers an infinite sequence? What about the ordered set of odd numbers? Explain why or why not. 4. What happens to the terms an of a sequence when there is a negative factor in the formula that is raised to a power that includes n? What is the term used to describe this phenomenon? 5. What is a factorial, and how is it denoted? Use an example to illustrate how factorial notation can be beneficial. Algebraic For the following exercises, write the first four terms of the sequence. 6. an = 2n - 2 7. an = - 16 _____ n + 1  8. an = -(-5)n - 1 9. an =  2n

__ n^{3}  10. an =  2n + 1 ______ n^{3}  12. an = -4 ⋅ (-6)n - 1 13. an =  n^{2} ______ 2n + 1  14. an = (-10)n + 1 15. an = -  4 ⋅ (-5)n - 1 __________    For the following exercises, write the first eight terms of the piecewise sequence. 16. an = { (-2)n - 2 if n is even (3)n - 1 if n is odd 17. an = {  n^{2} _ 2n + 1  if n \le  5 n^{2} - 5 if n > 5 18. an = { (2n + 1)^{2} if n is divisible by 4  2 _ n  if n is not divisible by 4 19. an = { -0.6 ⋅ 5n - 1 if n is prime or 1 2.5 ⋅ (-2)n - 1 if n is composite 20. an = { 4(n^{2} - 2) if n \le  3 or n > 6  n^{2} - 2 _  if 3 < n \le  6 For the following exercises, write an explicit formula for each sequence. ___ _____ 1 + e^{2} ,  1 - e^{2} _____ 1 + e^{3} ,  1 - e^{3} ______ 1 + e^{4} ,  1 - e^{4} ______ __ 2 ,  1 __ 4 , - 1 __ 8 ,  1 ___ For the following exercises, write the first five terms of the sequence. 26. a^{1} = 9, an = an - 1 + n 27. a^{1} = 3, an = (-3)an - 1 28. a^{1} = -4, an =  an - 1 + 2n _ an - 1 - 1  29. a^{1} = -1, an =  (-3)n - 1 _ an - 1 - 2  30. a^{1} = -30, an = (2 + an - 1)  1 __ 2    n  For the following exercises, write the first eight terms of the sequence. ___ 24 , a^{2} = 1, an = (2an - 2)(3an - 1) 32. a^{1} = -1, a^{2} = 5, an = an - 2(3 - an -1) 2(an -1 + 2) __ an - 2 


## 11.1 Section Exercises
For the following exercises, write a recursive formula for each sequence. __ 5 ,  3 ___ ___ For the following exercises, evaluate the factorial. ___ 6   ! ___ 6!  ____ 99!  For the following exercises, write the first four terms of the sequence. 43. an =  n! __ n^{2}  44. an =  3 ⋅ n ! _____ 4 ⋅ n !  45. an =  n ! _________ n^{2} - n - 1  46. an =  100 ⋅ n ________ n(n - 1)!  Graphical For the following exercises, graph the first five terms of the indicated sequence 47. an =  (-1)n _____ n  + n 48. an = {  4 + n _ 2n  if n in even 3 + n if n is odd 49. a^{1} = 2, an = (-an - 1 + 1)^{2} 50. an = 1, an = an - 1 + 8 51. an =  (n + 1)! _______ (n - 1)!  For the following exercises, write an explicit formula for the sequence using the first five points shown on the graph. n an n an n an For the following exercises, write a recursive formula for the sequence using the first five points shown on the graph. n an n an

Technology Follow these steps to evaluate a sequence defined recursively using a graphing calculator: • On the home screen, key in the value for the initial term a^{1} and press [ENTER]. • Enter the recursive formula by keying in all numerical values given in the formula, along with the key strokes [2ND] ANS for the previous term an - 1. Press [ENTER]. • Continue pressing [ENTER] to calculate the values for each successive term. For the following exercises, use the steps above to find the indicated term or terms for the sequence. 57. Find the first five terms of the sequence a^{1} =  87 ___ an =  4 __ 3 an - 1 +  12 ___ 37 . Use the >Frac feature to give fractional results. 58. Find the 15th term of the sequence 59. Find the first five terms of the sequence a^{1} = 2, an = 2[(an - 1) - 1] + 1. 60. Find the first ten terms of the sequence a^{1} = 8, an =  (an - 1 + 1)! _ an - 1!  . 61. Find the tenth term of the sequence a^{1} = 2, an = nan - 1 Follow these steps to evaluate a finite sequence defined by an explicit formula. Using a TI-84, do the following. • In the home screen, press [2ND] LIST. • Scroll over to OPS and choose “seq(” from the dropdown list. Press [ENTER]. • In the line headed “Expr:” type in the explicit formula, using the [X,T, \theta , n] button for n • In the line headed “Variable:” type in the variable used on the previous step. • In the line headed “start:” key in the value of n that begins the sequence. • In the line headed “end:” key in the value of n that ends the sequence. • Press [ENTER] 3 times to return to the home screen. You will see the sequence syntax on the screen. Press [ENTER] to see the list of terms for the finite sequence defined. Use the right arrow key to scroll through the list of terms. Using a TI-83, do the following. • In the home screen, press [2ND] LIST. • Scroll over to OPS and choose “seq(” from the dropdown list. Press [ENTER]. • Enter the items in the order “Expr”, “Variable”, “start”, “end” separated by commas. See the instructions above for the description of each item. • Press [ENTER] to see the list of terms for the finite sequence defined. Use the right arrow key to scroll through the list of terms. For the following exercises, use the steps above to find the indicated terms for the sequence. Round to the nearest thousandth when necessary. 62. List the first five terms of the sequence. an = - 28 ___ 9 n +  5 _ 3  63. List the first six terms of the sequence.

___________________

2.4n  64. List the first five terms of the sequence. an =  15n ⋅ (-2)n - 1

____________  65. List the first four terms of the sequence. 66. List the first six terms of the sequence an =  n! __ n . Extensions 67. Consider the sequence defined by an = -6 - 8n. Is an = -421 a term in the sequence? Verify the result. 68. What term in the sequence an =  n^{2} + 4n + 4 __________ 2(n + 2)  has the value 41? Verify the result. 69. Find a recursive formula for the sequence (Hint: find a pattern for an based on the first two terms.) 70. Calculate the first eight terms of the sequences an =  (n + 2)! _______ (n - 1)!  and bn = n^{3} + 3n^{2} + 2n, and then make a conjecture about the relationship between these two sequences. 71. Prove the conjecture made in the preceding exercise.


## 11.2 Arithmetic Sequences
Learning Objectives
In this section, you will:
• Find the common difference for an arithmetic sequence.
• Write terms of an arithmetic sequence.
• Use a recursive formula for an arithmetic sequence.
• Use an explicit formula for an arithmetic sequence.
Companies often make large purchases, such as computers and vehicles, for business use. The book-value of these supplies decreases each year for tax purposes. This decrease in value is called depreciation. One method of calculating depreciation is straight-line depreciation, in which the value of the asset decreases by the same amount each year. As an example, consider a woman who starts a small contracting business. She purchases a new truck for $25,000. After five years, she estimates that she will be able to sell the truck for $8,000. The loss in value of the truck will therefore be $17,000, which is $3,400 per year for five years. The truck will be worth $21,600 after the first year; $18,200 after two years; $14,800 after three years; $11,400 after four years; and $8,000 at the end of five years. In this section, we will consider specific kinds of sequences that will allow us to calculate depreciation, such as the truck’s value. Finding Common Differences The values of the truck in the example are said to form an arithmetic sequence because they change by a constant amount each year. Each term increases or decreases by the same constant value called the common difference of the sequence. For this sequence, the common difference is -3,400. 8000} The sequence below is another example of an arithmetic sequence. In this case, the constant difference is 3. You can choose any term of the sequence, and add 3 to find the subsequent term. {3, +3 +3 +3 +3 arithmetic sequence An arithmetic sequence is a sequence that has the property that the difference between any two consecutive terms is a constant. This constant is called the common difference. If a^{1} is the first term of an arithmetic sequence and d is the common difference, the sequence will be: {an} = {a^{1}, a^{1} + d, a^{1} + 2d, a^{1} + 3d,...}

**Example  1**
Finding Common Differences Is each sequence arithmetic? If so, find the common difference. Solution Subtract each term from the subsequent term to determine whether a common difference exists. a. The sequence is not arithmetic because there is no common difference. 2 - 1 = 1 4 - 2 = 2 8 - 4 = 4 b. The sequence is arithmetic because there is a common difference. The common difference is 4. 1 - (-3) = 4 5 - 1 = 4 9 - 5 = 4

Analysis The graph of each of these sequences is shown in Figure 1. We can see from the graphs that, although both sequences show growth, a is not linear whereas b is linear. Arithmetic sequences have a constant rate of change so their graphs will always be points on a line. -4 n an -4 (b) (a) n an If we are told that a sequence is arithmetic, do we have to subtract every term from the following term to find the common difference? No. If we know that the sequence is arithmetic, we can choose any one term in the sequence, and subtract it from the subsequent term to find the common difference.

**Try It #1**
Is the given sequence arithmetic? If so, find the common difference.

**Try It #2**
Is the given sequence arithmetic? If so, find the common difference. Writing Terms of Arithmetic Sequences Now that we can recognize an arithmetic sequence, we will find the terms if we are given the first term and the common difference. The terms can be found by beginning with the first term and adding the common difference repeatedly. In addition, any term can also be found by plugging in the values of n and d into formula below. an = a^{1} + (n - 1)d

**How To…**
Given the first term and the common difference of an arithmetic sequence, find the first several terms. 1. Add the common difference to the first term to find the second term. 2. Add the common difference to the second term to find the third term. 3. Continue until all of the desired terms are identified. 4. Write the terms separated by commas within brackets.

**Example  2**

### Writing Terms of Arithmetic Sequences
Write the first five terms of the arithmetic sequence with a^{1} = 17 and d = -3. Solution Adding -3 is the same as subtracting 3. Beginning with the first term, subtract 3 from each term to find the next term. The first five terms are {17, 14, 11, 8, 5}

Analysis As expected, the graph of the sequence consists of points on a line as shown in Figure 2. n an

**Try It #3**
List the first five terms of the arithmetic sequence with a^{1} = 1 and d = 5.

**How To…**
Given any first term and any other term in an arithmetic sequence, find a given term. 1. Substitute the values given for a^{1}, an, n into the formula an = a^{1} + (n - 1)d to solve for d. 2. Find a given term by substituting the appropriate values for a^{1}, n, and d into the formula an = a^{1} + (n - 1)d.

**Example  3**

### Writing Terms of Arithmetic Sequences
Given a^{1} = 8 and a^{4} = 14, find a^{5}. Solution The sequence can be written in terms of the initial term 8 and the common difference d.

{8, 8 + d, 8 + 2d, 8 + 3d} We know the fourth term equals 14; we know the fourth term has the form a^{1} + 3d = 8 + 3d. We can find the common difference d.

an = a^{1} + (n - 1)d

a^{4} = a^{1} + 3d

a^{4} = 8 + 3d Write the fourth term of the sequence in terms of a^{1} and d.

Substitute 14 for a^{4}.

d = 2 Solve for the common difference. Find the fifth term by adding the common difference to the fourth term.

a^{5} = a^{4} + 2 = 16 Analysis Notice that the common difference is added to the first term once to find the second term, twice to find the third term, three times to find the fourth term, and so on. The tenth term could be found by adding the common difference to the first term nine times or by using the equation an = a^{1} + (n - 1)d.

**Try It #4**
Given a^{3} = 7 and a^{5} = 17, find a^{2}. Using Recursive Formulas for Arithmetic Sequences Some arithmetic sequences are defined in terms of the previous term using a recursive formula. The formula provides an algebraic rule for determining the terms of the sequence. A recursive formula allows us to find any term of an arithmetic sequence using a function of the preceding term. Each term is the sum of the previous term and the

common difference. For example, if the common difference is 5, then each term is the previous term plus 5. As with any recursive formula, the first term must be given. an = an - 1 + d n \ge  2 recursive formula for an arithmetic sequence The recursive formula for an arithmetic sequence with common difference d is: an = an - 1 + d n \ge  2

**How To…**
Given an arithmetic sequence, write its recursive formula. 1. Subtract any term from the subsequent term to find the common difference. 2. State the initial term and substitute the common difference into the recursive formula for arithmetic sequences.

**Example  4**

### Writing a Recursive Formula for an Arithmetic Sequence
Write a recursive formula for the arithmetic sequence. Solution The first term is given as -18. The common difference can be found by subtracting the first term from the second term. d = -7 - (-18) = 11 Substitute the initial term and the common difference into the recursive formula for arithmetic sequences.

an = an - 1 + 11, for n \ge  2 Analysis We see that the common difference is the slope of the line formed when we graph the terms of the sequence, as shown in Figure 3. The growth pattern of the sequence shows the constant difference of 11 units. -20 -10 n an Do we have to subtract the first term from the second term to find the common difference? No. We can subtract any term in the sequence from the subsequent term. It is, however, most common to subtract the first term from the second term because it is often the easiest method of finding the common difference.

**Try It #5**
Write a recursive formula for the arithmetic sequence.

Using Explicit Formulas for Arithmetic Sequences We can think of an arithmetic sequence as a function on the domain of the natural numbers; it is a linear function because it has a constant rate of change. The common difference is the constant rate of change, or the slope of the function. We can construct the linear function if we know the slope and the vertical intercept. an = a^{1} + d(n - 1) To find the y-intercept of the function, we can subtract the common difference from the first term of the sequence. Consider the following sequence. {200, -50 -50 -50 -50 The common difference is -50, so the sequence represents a linear function with a slope of -50. To find the y-intercept, we subtract -50 from 200: 200 - ( -50) = 200 + 50 = 250. You can also find the y -intercept by graphing the function and determining where a line that connects the points would intersect the vertical axis. The graph is shown in Figure 4. n an Recall the slope-intercept form of a line is y = mx + b. When dealing with sequences, we use an in place of y and n in place of x. If we know the slope and vertical intercept of the function, we can substitute them for m and b in the slope- intercept form of a line. Substituting - 50 for the slope and 250 for the vertical intercept, we get the following equation: an = -50n + 250 We do not need to find the vertical intercept to write an explicit formula for an arithmetic sequence. Another explicit formula for this sequence is an = 200 - 50(n - 1), which simplifies to an = -50n + 250. explicit formula for an arithmetic sequence An explicit formula for the nth term of an arithmetic sequence is given by an = a^{1} + d (n - 1)

**How To…**
Given the first several terms for an arithmetic sequence, write an explicit formula. 1. Find the common difference, a^{2} - a^{1}. 2. Substitute the common difference and the first term into an = a^{1} + d(n - 1).

**Example  5**

### Writing the nth Term Explicit Formula for an Arithmetic Sequence
Write an explicit formula for the arithmetic sequence.

Solution The common difference can be found by subtracting the first term from the second term.

d = a^{2} - a^{1}

= 10 The common difference is 10. Substitute the common difference and the first term of the sequence into the formula and simplify.

an = 2 + 10(n - 1)

an = 10n - 8 Analysis The graph of this sequence, represented in Figure 5, shows a slope of 10 and a vertical intercept of -8. n an

**Try It #6**
Write an explicit formula for the following arithmetic sequence. Finding the Number of Terms in a Finite Arithmetic Sequence Explicit formulas can be used to determine the number of terms in a finite arithmetic sequence. We need to find the common difference, and then determine how many times the common difference must be added to the first term to obtain the final term of the sequence.

**How To…**
Given the first three terms and the last term of a finite arithmetic sequence, find the total number of terms. 1. Find the common difference d. 2. Substitute the common difference and the first term into an = a^{1} + d(n - 1). 3. Substitute the last term for an and solve for n.

**Example  6**
Finding the Number of Terms in a Finite Arithmetic Sequence Find the number of terms in the finite arithmetic sequence. Solution The common difference can be found by subtracting the first term from the second term.

1 - 8 = -7

The common difference is -7. Substitute the common difference and the initial term of the sequence into the nth term formula and simplify.

an = a^{1} + d(n - 1)

an = 8 + (-7)(n - 1)

an = 15 - 7n Substitute -41 for an and solve for n

8 = n There are eight terms in the sequence.

**Try It #7**
Find the number of terms in the finite arithmetic sequence. Solving Application Problems with Arithmetic Sequences In many application problems, it often makes sense to use an initial term of a^{0} instead of a^{1}. In these problems, we alter the explicit formula slightly to account for the difference in initial terms. We use the following formula:

an = a^{0} + dn

**Example  7**

### Solving Application Problems with Arithmetic Sequences
A five-year old child receives an allowance of $1 each week. His parents promise him an annual increase of $2 per week. a. Write a formula for the child’s weekly allowance in a given year. b. What will the child’s allowance be when he is 16 years old?

**Solution**
a. The situation can be modeled by an arithmetic sequence with an initial term of 1 and a common difference of 2. Let A be the amount of the allowance and n be the number of years after age 5. Using the altered explicit formula for an arithmetic sequence we get:

An = 1 + 2n b. We can find the number of years since age 5 by subtracting.

We are looking for the child’s allowance after 11 years. Substitute 11 into the formula to find the child’s allowance at age 16.

The child’s allowance at age 16 will be $23 per week.

**Try It #8**
A woman decides to go for a 10-minute run every day this week and plans to increase the time of her daily run by 4 minutes each week. Write a formula for the time of her run after n weeks. How long will her daily run be 8 weeks from today? > Access this online resource for additional instruction and practice with arithmetic sequences. • Arithmetic Sequences (http://openstaxcollege.org/l/arithmeticseq)


### 11.2 Section Exercises
Verbal 1. What is an arithmetic sequence? 2. How is the common difference of an arithmetic sequence found? 3. How do we determine whether a sequence is arithmetic? 4. What are the main differences between using a recursive formula and using an explicit formula to describe an arithmetic sequence? 5. Describe how linear functions and arithmetic sequences are similar. How are they different? Algebraic For the following exercises, find the common difference for the arithmetic sequence provided. For the following exercises, determine whether the sequence is arithmetic. If so find the common difference. For the following exercises, write the first five terms of the arithmetic sequence given the first term and common difference. __ 3  For the following exercises, write the first five terms of the arithmetic series given two terms. For the following exercises, find the specified term for the arithmetic sequence given the first term and common difference. 14. First term is 3, common difference is 4, find the 5th term. 15. First term is 4, common difference is 5, find the 4th term. 16. First term is 5, common difference is 6, find the 8th term. 17. First term is 6, common difference is 7, find the 6th term. 18. First term is 7, common difference is 8, find the 7th term. For the following exercises, find the first term given two terms from an arithmetic sequence. 19. Find the first term or a^{1} of an arithmetic sequence if 20. Find the first term or a^{1} of an arithmetic sequence if 21. Find the first term or a^{1} of an arithmetic sequence if 22. Find the first term or a^{1} of an arithmetic sequence if 23. Find the first term or a^{1} of an arithmetic sequence if For the following exercises, find the specified term given two terms from an arithmetic sequence. For the following exercises, use the recursive formula to write the first five terms of the arithmetic sequence. 26. a^{1} = 39; an = an - 1 -3 27. a^{1} = -19; an = an - 1 -1.4


## 11.2 Section Exercises
For the following exercises, write a recursive formula for each arithmetic sequence. 35. a =   1 __ 5 ,  9 ___ ___ 36. a =  -  1 __ 2 , -  5 37. a =   1 __ 6 , - 11 ___ For the following exercises, use the recursive formula to write the first five terms of the arithmetic sequence. 38. a = {7, 4, 1, ... }; Find the 17th term. For the following exercises, use the recursive formula to write the first five terms of the arithmetic sequence. __ 2 n -  1 __ 2  For the following exercises, write an explicit formula for each arithmetic sequence. 50. a =   1 __ 3 , - 4 __ 3 ,  2 52. a =  -5, -  10 ___ 3 , - 5 For the following exercises, find the number of terms in the given finite arithmetic sequence. 55. a =   1 Graphical For the following exercises, determine whether the graph shown represents an arithmetic sequence. 0.5 -0.5 -0.5 -1.5 -3 -4 -5 -2.5 -3.5 -4.5 -5.5 -1 -2 0.5 1.5 2.5 3.5 4.5 5.5 n 1.5 2.5 3.5 4.5 5.5 an 0.5 -0.5 -0.5 0.5 1.5 2.5 3.5 4.5 5.5 1.5 2.5 3.5 4.5 5.5 6.5 7.5 8.5 n an

For the following exercises, use the information provided to graph the first 5 terms of the arithmetic sequence. 59. a^{1} = 9; an = an - 1 - 10 Technology For the following exercises, follow the steps to work with the arithmetic sequence an = 3n - 2 using a graphing calculator: • Press [MODE] ›› Select [SEQ] in the fourth line ›› Select [DOT] in the fifth line ›› Press [ENTER] • Press [Y=] ›› nMin is the first counting number for the sequence. Set nMin = 1 ›› u(n) is the pattern for the sequence. Set u(n) = 3n - 2 ›› u(nMin) is the first number in the sequence. Set u(nMin) = 1 • Press [2ND] then [WINDOW] to go to TBLSET ›› Set TblStart = 1 ›› Set \Delta Tbl = 1 ›› Set Indpnt: Auto and Depend: Auto • Press [2ND] then [GRAPH] to go to the [TABLE] 61. What are the first seven terms shown in the column with the heading u(n)? 62. Use the scroll-down arrow to scroll to n = 50. What value is given for u(n)? 63. Press [WINDOW]. Set nMin = 1, nMax = 5, xMin = 0, xMax = 6, yMin = -1, and yMax = 14. Then press [GRAPH]. Graph the sequence as it appears on the graphing calculator. For the following exercises, follow the steps given above to work with the arithmetic sequence an =  1 __ 2 n + 5 using a graphing calculator. 64. What are the first seven terms shown in the column with the heading u(n) in the [TABLE] feature? 65. Graph the sequence as it appears on the graphing calculator. Be sure to adjust the [WINDOW] settings as needed. Extensions 66. Give two examples of arithmetic sequences whose 4th terms are 9. 67. Give two examples of arithmetic sequences whose 10th terms are 206. 68. Find the 5th term of the arithmetic sequence 69. Find the 11th term of the arithmetic sequence {3a - 2b, a + 2b, -a + 6b, ... }. 70. At which term does the sequence {5.4, 14.5, 23.6, ...} exceed 151? 71. At which term does the sequence   17 _ _ _ begin to have negative values? 72. For which terms does the finite arithmetic sequence    5 _ ___ 8 ,  9 _ _ 8   have integer values? 73. Write an arithmetic sequence using a recursive formula. Show the first 4 terms, and then find the 31st term. 74. Write an arithmetic sequence using an explicit formula. Show the first 4 terms, and then find the 28th term.


## 11.3 Geometric Sequences
Learning Objectives
In this section, you will:
• Find the common ratio for a geometric sequence.
• List the terms of a geometric sequence.
• Use a recursive formula for a geometric sequence.
• Use an explicit formula for a geometric sequence.
Many jobs offer an annual cost-of-living increase to keep salaries consistent with inflation. Suppose, for example, a recent college graduate finds a position as a sales manager earning an annual salary of $26,000. He is promised a 2% cost of living increase each year. His annual salary in any given year can be found by multiplying his salary from the previous year by 102%. His salary will be $26,520 after one year; $27,050.40 after two years; $27,591.41 after three years; and so on. When a salary increases by a constant rate each year, the salary grows by a constant factor. In this section, we will review sequences that grow in this way. Finding Common Ratios The yearly salary values described form a geometric sequence because they change by a constant factor each year. Each term of a geometric sequence increases or decreases by a constant factor called the common ratio. The sequence below is an example of a geometric sequence because each term increases by a constant factor of 6. Multiplying any term of the sequence by the common ratio 6 generates the subsequent term. {1, \times 6 \times 6 \times 6 \times 6 definition of a geometric sequence A geometric sequence is one in which any term divided by the previous term is a constant. This constant is called the common ratio of the sequence. The common ratio can be found by dividing any term in the sequence by the previous term. If a^{1} is the initial term of a geometric sequence and r is the common ratio, the sequence will be


**How To…**
Given a set of numbers, determine if they represent a geometric sequence. 1. Divide each term by the previous term. 2. Compare the quotients. If they are the same, a common ratio exists and the sequence is geometric.

**Example  1**
Finding Common Ratios Is the sequence geometric? If so, find the common ratio. Solution Divide each term by the previous term to determine whether a common ratio exists. a.  2 _ 1  = 2  4 _ 2 = 2  8 _ 4  = 2  16 _ 8  = 2 The sequence is geometric because there is a common ratio. The common ratio is 2. _ 48  =  1 __ 4   4 _ 12  =  1 _ 3   2 _ 4  =  1 _ 2  The sequence is not geometric because there is not a common ratio.

Analysis The graph of each sequence is shown in Figure 1. It seems from the graphs that both (a) and (b) appear have the form of the graph of an exponential function in this viewing window. However, we know that (a) is geometric and so this interpretation holds, but (b) is not. an an n n (a) (b) If you are told that a sequence is geometric, do you have to divide every term by the previous term to find the common ratio? No. If you know that the sequence is geometric, you can choose any one term in the sequence and divide it by the previous term to find the common ratio.

**Try It #1**
Is the sequence geometric? If so, find the common ratio.

**Try It #2**
Is the sequence geometric? If so, find the common ratio. __ Writing Terms of Geometric Sequences Now that we can identify a geometric sequence, we will learn how to find the terms of a geometric sequence if we are given the first term and the common ratio. The terms of a geometric sequence can be found by beginning with the first term and multiplying by the common ratio repeatedly. For instance, if the first term of a geometric sequence is a^{1} = -2 and the common ratio is r = 4, we can find subsequent terms by multiplying -2 ⋅ 4 to get -8 then multiplying the result -8 ⋅ 4 to get -32 and so on.

a^{1} = -2

a^{2} = (-2 ⋅ 4) = -8

a^{3} = (-8 ⋅ 4) = -32

a^{4} = (-32 ⋅ 4) = -128 The first four terms are {-2, -8, -32, -128}.

**How To…**
Given the first term and the common factor, find the first four terms of a geometric sequence. 1. Multiply the initial term, a^{1}, by the common ratio to find the next term, a^{2}. 2. Repeat the process, using an = a^{2} to find a^{3} and then a^{3} to find a^{4}, until all four terms have been identified. 3. Write the terms separated by commons within brackets.


**Example  2**

### Writing the Terms of a Geometric Sequence
List the first four terms of the geometric sequence with a^{1} = 5 and r = -2. Solution Multiply a^{1} by -2 to find a^{2}. Repeat the process, using a^{2} to find a^{3}, and so on.

a^{1} = 5

a^{2} = -2a^{1} = -10

a^{4} = -2a^{3} = -40 The first four terms are {5, -10, 20, -40}.

**Try It #3**
List the first five terms of the geometric sequence with a^{1} = 18 and r =  1 __ 3 . Using Recursive Formulas for Geometric Sequences A recursive formula allows us to find any term of a geometric sequence by using the previous term. Each term is the product of the common ratio and the previous term. For example, suppose the common ratio is 9. Then each term is nine times the previous term. As with any recursive formula, the initial term must be given. recursive formula for a geometric sequence The recursive formula for a geometric sequence with common ratio r and first term a^{1} is an = r an - 1, n \ge  2

**How To…**
Given the first several terms of a geometric sequence, write its recursive formula. 1. State the initial term. 2. Find the common ratio by dividing any term by the preceding term. 3. Substitute the common ratio into the recursive formula for a geometric sequence.

**Example  3**
Using Recursive Formulas for Geometric Sequences Write a recursive formula for the following geometric sequence.

Solution The first term is given as 6. The common ratio can be found by dividing the second term by the first term.

r =  9 _ Substitute the common ratio into the recursive formula for geometric sequences and define a^{1}.

an = ran - 1

an = 1.5an - 1 for n \ge  2

a^{1} = 6 Analysis The sequence of data points follows an exponential pattern. The common ratio is also the base of an exponential function as shown in Figure 2. an n

Do we have to divide the second term by the first term to find the common ratio? No. We can divide any term in the sequence by the previous term. It is, however, most common to divide the second term by the first term because it is often the easiest method of finding the common ratio.

**Try It #4**
Write a recursive formula for the following geometric sequence.  2,  4 _ _ _ Using Explicit Formulas for Geometric Sequences Because a geometric sequence is an exponential function whose domain is the set of positive integers, and the common ratio is the base of the function, we can write explicit formulas that allow us to find particular terms. an = a^{1} r n - 1 Let’s take a look at the sequence {18, 36, 72, 144, 288,...}. This is a geometric sequence with a common ratio of 2 and an exponential function with a base of 2. An explicit formula for this sequence is an = 18 \cdot  2n - 1 The graph of the sequence is shown in Figure 3. n an explicit formula for a geometric sequence The nth term of a geometric sequence is given by the explicit formula: an = a^{1} r n - 1

**Example  4**

### Writing Terms of Geometric Sequences Using the Explicit Formula
Given a geometric sequence with a^{1} = 3 and a^{4} = 24, find a^{2}. Solution The sequence can be written in terms of the initial term and the common ratio r.

Find the common ratio using the given fourth term.

an = a^{1}r n - 1

a^{4} = 3r 3 Write the fourth term of sequence in terms of a^{1} and r

Substitute 24 for a^{4}

8 = r 3 Divide

r = 2 Solve for the common ratio Find the second term by multiplying the first term by the common ratio.

= 2(3)

= 6 Analysis The common ratio is multiplied by the first term once to find the second term, twice to find the third term, three times to find the fourth term, and so on. The tenth term could be found by multiplying the first term by the common ratio nine times or by multiplying by the common ratio raised to the ninth power.

**Try It #5**
Given a geometric sequence with a^{2} = 4 and a^{3} = 32, find a^{6}.

**Example  5**

### Writing an Explicit Formula for the nth Term of a Geometric Sequence
Write an explicit formula for the nth term of the following geometric sequence. Solution The first term is 2. The common ratio can be found by dividing the second term by the first term.

 10 ___ 2  = 5 The common ratio is 5. Substitute the common ratio and the first term of the sequence into the formula.

an = a^{1}r (n - 1)

an = 2 ⋅ 5n - 1 The graph of this sequence in Figure 4 shows an exponential pattern. an n

**Try It #6**
Write an explicit formula for the following geometric sequence.


### Solving Application Problems with Geometric Sequences
In real-world scenarios involving arithmetic sequences, we may need to use an initial term of a^{0} instead of a^{1}. In these problems, we can alter the explicit formula slightly by using the following formula: an = a^{0} r n

**Example  6**

### Solving Application Problems with Geometric Sequences
In 2013, the number of students in a small school is 284. It is estimated that the student population will increase by 4% each year. a. Write a formula for the student population. b. Estimate the student population in 2020.

**Solution**
a. The situation can be modeled by a geometric sequence with an initial term of 284. The student population will be 104% of the prior year, so the common ratio is 1.04. Let P be the student population and n be the number of years after 2013. Using the explicit formula for a geometric sequence we get

b. We can find the number of years since 2013 by subtracting.

We are looking for the population after 7 years. We can substitute 7 for n to estimate the population in 2020.

The student population will be about 374 in 2020.

**Try It #7**
A business starts a new website. Initially the number of hits is 293 due to the curiosity factor. The business estimates the number of hits will increase by 2.6% per week. a. Write a formula for the number of hits. b. Estimate the number of hits in 5 weeks. Access these online resources for additional instruction and practice with geometric sequences. • Geometric Sequences (http://openstaxcollege.org/l/geometricseq) • Determine the Type of Sequence (http://openstaxcollege.org/l/sequencetype) • Find the Formula for a Sequence (http://openstaxcollege.org/l/sequenceformula)


## 11.3 Section Exercises

### 11.3 Section Exercises
Verbal 1. What is a geometric sequence? 2. How is the common ratio of a geometric sequence found? 3. What is the procedure for determining whether a sequence is geometric? 4. What is the difference between an arithmetic sequence and a geometric sequence? 5. Describe how exponential functions and geometric sequences are similar. How are they different? Algebraic For the following exercises, find the common ratio for the geometric sequence. ___ 2 , - 1 ___ 8 , - 1 ___ ___ For the following exercises, determine whether the sequence is geometric. If so, find the common ratio. __ 2 , - 1 ___ 4 ,  1 __ 8 , - 1 ___ For the following exercises, write the first five terms of the geometric sequence, given the first term and common ratio. __ 5  For the following exercises, write the first five terms of the geometric sequence, given any two terms. For the following exercises, find the specified term for the geometric sequence, given the first term and common ratio. 18. The first term is 2, and the common ratio is 3. Find the 5th term. 19. The first term is 16 and the common ratio is - 1 ___ 3 . Find the 4th term. For the following exercises, find the specified term for the geometric sequence, given the first four terms. 21. an =  -2,  2 __ 3 , - 2 __ 9 ,  2 ___ For the following exercises, write the first five terms of the geometric sequence. ___ 3 an - 1 For the following exercises, write a recursive formula for each geometric sequence. 29. an =   3 __ 5 ,  1 ___ ___ ___ 30. an =  -2,  4 __ 3 , - 8 __ 9 ,  16 ___ 31. an =   1 ___ ___ ___ ___ 8 , ...  For the following exercises, write the first five terms of the geometric sequence. 32. an = -4 ⋅ 5n - 1 33. an = 12 ⋅  - 1 ___ 2    n - 1

For the following exercises, write an explicit formula for each geometric sequence. 39. an =  -1, -  4 __ 5 , - 16 ___ ___ 40. an =  2,  1 __ 3 ,  1 ___ ___ __ 3 , - 1 For the following exercises, find the specified term for the geometric sequence given. 42. Let a^{1} = 4, an = -3an - 1. Find a^{8}. 43. Let an = - - 1 __ 3    n - 1. Find a^{1}2. For the following exercises, find the number of terms in the given finite geometric sequence. ____ Graphical For the following exercises, determine whether the graph shown represents a geometric sequence. 3.5 n an -1 -2 -3 -4 -0.5 1.5 5.5 3.5 n an 4.5 3.5 2.5 1.5 0.5 -0.5 -1 -0.5 1.5 For the following exercises, use the information provided to graph the first five terms of the geometric sequence. __ 2  49. a^{1} = 3, an = 2an - 1 Extensions 51. Use recursive formulas to give two examples of geometric sequences whose 3rd terms are 200. 52. Use explicit formulas to give two examples of geometric sequences whose 7th terms are 1024. 53. Find the 5th term of the geometric sequence 54. Find the 7th term of the geometric sequence 55. At which term does the sequence 56. At which term does the sequence   1 ____ ___ ___ ___ 81 ...  begin to have integer values? 57. For which term does the geometric sequence an = -36   2 __ 3    n - 1 first have a non-integer value? 58. Use the recursive formula to write a geometric sequence whose common ratio is an integer. Show the first four terms, and then find the 10th term. 59. Use the explicit formula to write a geometric sequence whose common ratio is a decimal number between 0 and 1. Show the first 4 terms, and then find the 8th term. 60. Is it possible for a sequence to be both arithmetic and geometric? If so, give an example.


## 11.4 Series and their notations
Learning Objectives
In this section, you will:
• Use summation notation.
• Use the formula for the sum of the first n terms of an arithmetic series.
• Use the formula for the sum of the first n terms of a geometric series.
• Use the formula for the sum of an infinite geometric series.
• Solve annuity problems.
A couple decides to start a college fund for their daughter. They plan to invest $50 in the fund each month. The fund pays 6% annual interest, compounded monthly. How much money will they have saved when their daughter is ready to start college in 6 years? In this section, we will learn how to answer this question. To do so, we need to consider the amount of money invested and the amount of interest earned. Using Summation Notation To find the total amount of money in the college fund and the sum of the amounts deposited, we need to add the amounts deposited each month and the amounts earned monthly. The sum of the terms of a sequence is called a series. Consider, for example, the following series.

The nth partial sum of a series is the sum of a finite number of consecutive terms beginning with the first term. The notation Sn represents the partial sum.

S^{1} = 3

S^{2} = 3 + 7 = 10

S^{3} = 3 + 7 + 11 = 21

Summation notation is used to represent series. Summation notation is often known as sigma notation because it uses the Greek capital letter sigma, \sum , to represent the sum. Summation notation includes an explicit formula and specifies the first and last terms in the series. An explicit formula for each term of the series is given to the right of the sigma. A variable called the index of summation is written below the sigma. The index of summation is set equal to the lower limit of summation, which is the number used to generate the first term in the series. The number above the sigma, called the upper limit of summation, is the number used to generate the last term in a series. Upper limit of summation → ← Explicit formula for kth term of series Index of summation → ← Lower limit of summation ∑ k = 1   2k If we interpret the given notation, we see that it asks us to find the sum of the terms in the series ak = 2k for k = 1 through k = 5. We can begin by substituting the terms for k and listing out the terms of this series.

a^{1} = 2(1) = 2

a^{2} = 2(2) = 4

a^{3} = 2(3) = 6

a^{4} = 2(4) = 8

We can find the sum of the series by adding the terms:

∑ k = 1   2k = 2 + 4 + 6 + 8 + 10 = 30

summation notation The sum of the first n terms of a series can be expressed in summation notation as follows: ∑ k = 1 n ak This notation tells us to find the sum of ak from k = 1 to k = n. k is called the index of summation, 1 is the lower limit of summation, and n is the upper limit of summation. Does the lower limit of summation have to be 1? No. The lower limit of summation can be any number, but 1 is frequently used. We will look at examples with lower limits of summation other than 1.

**How To…**
Given summation notation for a series, evaluate the value. 1. Identify the lower limit of summation. 2. Identify the upper limit of summation. 3. Substitute each value of k from the lower limit to the upper limit into the formula. 4. Add to find the sum.

**Example  1**
Using Summation Notation Evaluate ∑ k = 3   k^{2}. Solution According to the notation, the lower limit of summation is 3 and the upper limit is 7. So we need to find the sum of k 2 from k = 3 to k = 7. We find the terms of the series by substituting k = 3, 4, 5, 6, and 7 into the function k 2. We add the terms to find the sum.

∑ k = 3   k 2 = 32 + 42 + 52 + 62 + 72

= 135

**Try It #1**
Evaluate ∑ k = 2   (3k - 1). Using the Formula for Arithmetic Series Just as we studied special types of sequences, we will look at special types of series. Recall that an arithmetic sequence is a sequence in which the difference between any two consecutive terms is the common difference, d. The sum of the terms of an arithmetic sequence is called an arithmetic series. We can write the sum of the first n terms of an arithmetic series as:

Sn = a^{1} + (a^{1} + d) + (a^{1} + 2d) + ... + (an - d) + an. We can also reverse the order of the terms and write the sum as

Sn = an + (an - d) + (an - 2d) + ... + (a^{1} + d) + a^{1}. If we add these two expressions for the sum of the first n terms of an arithmetic series, we can derive a formula for the sum of the first n terms of any arithmetic series.

Sn = a^{1} + (a^{1} + d) + (a^{1} + 2d) + ... + (an - d) + an

+ Sn = an + (an - d) + (an - 2d) + ... + (a^{1} + d) + a^{1}

2Sn = (a^{1} + an) + (a^{1} + an) + ... + (a^{1} + an) Because there are n terms in the series, we can simplify this sum to

2Sn = n(a^{1} + an). We divide by 2 to find the formula for the sum of the first n terms of an arithmetic series.

Sn =  n(a^{1} + an) __________  formula for the sum of the first n terms of an arithmetic series An arithmetic series is the sum of the terms of an arithmetic sequence. The formula for the sum of the first n terms of an arithmetic sequence is Sn =  n(a^{1} + an) __________ 

**How To…**
Given terms of an arithmetic series, find the sum of the first n terms. 1. Identify a^{1} and an. 2. Determine n. 3. Substitute values for a^{1}, an, and n into the formula Sn =  n(a^{1} + an) _ . 4. Simplify to find Sn.

**Example  2**
Finding the First n Terms of an Arithmetic Series Find the sum of each arithmetic series. c. ∑ k = 1   3k - 8

**Solution**
a. We are given a^{1} = 5 and an = 32. Count the number of terms in the sequence to find n = 10. Substitute values for a^{1}, an, and n into the formula and simplify.

Sn =  n(a^{1} + an) __________ 

_________ b. We are given a^{1} = 20 and an = -50. Use the formula for the general term of an arithmetic sequence to find n.

an = a^{1} + (n - 1)d

-50 = 20 + (n - 1)( -5)

-70 = (n - 1)( -5)

14 = n - 1

15 = n Substitute values for a^{1}, an, n into the formula and simplify.

Sn =  n(a^{1} + an) __________ 

__________

c. To find a^{1}, substitute k = 1 into the given explicit formula.

ak = 3k - 8

a^{1} = 3(1) - 8 = -5 We are given that n = 12. To find a^{1}2, substitute k = 12 into the given explicit formula.

ak = 3k - 8

Substitute values for a^{1}, an, and n into the formula and simplify.

Sn =  n(a^{1} + an) _ 

S^{1}2 =  12( -5 + 28) __

**Try It #2**
Use the formula to find the sum of the arithmetic series.

**Try It #3**
Use the formula to find the sum of the arithmetic series.

**Try It #4**
Use the formula to find the sum of the arithmetic series. ∑ k = 1   5 - 6k

**Example  3**

### Solving Application Problems with Arithmetic Series
On the Sunday after a minor surgery, a woman is able to walk a half-mile. Each Sunday, she walks an additional quarter-mile. After 8 weeks, what will be the total number of miles she has walked? Solution This problem can be modeled by an arithmetic series with a^{1} =  1 __ 2  and d =  1 __ 4 . We are looking for the total number of miles walked after 8 weeks, so we know that n = 8, and we are looking for S^{8}. To find a^{8}, we can use the explicit formula for an arithmetic sequence.

an = a^{1} + d(n - 1)

a^{8} =  1 __ 2  +  1 __ 4 (8 - 1) =  9 __ 4  We can now use the formula for arithmetic series.

Sn =  n(a^{1} + an) _ 

S^{8} =  8  1 __ 2  +  9 __ 4    __  = 11 She will have walked a total of 11 miles.

**Try It #5**
A man earns $100 in the first week of June. Each week, he earns $12.50 more than the previous week. After 12 weeks, how much has he earned?

Using the Formula for Geometric Series Just as the sum of the terms of an arithmetic sequence is called an arithmetic series, the sum of the terms in a geometric sequence is called a geometric series. Recall that a geometric sequence is a sequence in which the ratio of any two consecutive terms is the common ratio, r. We can write the sum of the first n terms of a geometric series as

Sn = a^{1} + ra^{1} + r^{2}a^{1} + ... + rn – 1a^{1}. Just as with arithmetic series, we can do some algebraic manipulation to derive a formula for the sum of the first n terms of a geometric series. We will begin by multiplying both sides of the equation by r.

rSn = ra^{1} + r 2a^{1} + r 3a^{1} + ... + r na^{1} Next, we subtract this equation from the original equation.

Sn = a^{1} + ra^{1} + r 2a^{1} + ... + r n – 1 a^{1}.

-rSn = -(ra^{1} + r 2a^{1} + r 3a^{1} + ... + r na^{1})

(1 - r)Sn = a^{1} - r n a^{1} Notice that when we subtract, all but the first term of the top equation and the last term of the bottom equation cancel out. To obtain a formula for Sn, divide both sides by (1 - r).

Sn =  a^{1}(1 - rn) _________ 1 - r  r \neq  1 formula for the sum of the first n terms of a geometric series A geometric series is the sum of the terms in a geometric sequence. The formula for the sum of the first n terms of a geometric sequence is represented as Sn =  a^{1}(1 - r n) _________ 1 - r  r \neq  1

**How To…**
Given a geometric series, find the sum of the first n terms. 1. Identify a^{1}, r, and n. 2. Substitute values for a^{1}, r, and n into the formula Sn =  a^{1}(1 - r n) _________ 1 - r . 3. Simplify to find Sn.

**Example  4**
Finding the First n Terms of a Geometric Series Use the formula to find the indicated partial sum of each geometric series. a. S^{1}1 for the series 8 + (-4) + 2 + ... b. ∑ k = 1   3 ⋅ 2k

**Solution**
a. a^{1} = 8, and we are given that n = 11. We can find r by dividing the second term of the series by the first. r =  -4 ___ 8  = - 1 ___ 2  Substitute values for a^{1}, r, and n into the formula and simplify.

Sn =  a^{1}(1 - rn) _ 1 - r 

S^{1}1 =  8  1 -  - 1 __ 2    11  

__

1 -  - 1 __ 2   

b. Find a^{1} by substituting k = 1 into the given explicit formula.

a^{1} = 3 ⋅ 21 = 6 We can see from the given explicit formula that r = 2. The upper limit of summation is 6, so n = 6. Substitute values for a^{1}, r, and n into the formula, and simplify.

Sn =  a^{1}(1 - r n) _________ 1 - r 

S^{6} =  6(1 - 26) ________

**Try It #6**
Use the formula to find the indicated partial sum of each geometric series.

**Try It #7**
Use the formula to find the indicated partial sum of each geometric series. ∑ k = 1   3k

**Example  5**

### Solving an Application Problem with a Geometric Series
At a new job, an employee’s starting salary is $26,750. He receives a 1.6% annual raise. Find his total earnings at the end of 5 years. Solution The problem can be represented by a geometric series with a^{1} = 26, 750; n = 5; and r = 1.016. Substitute values for a^{1}, r, and n into the formula and simplify to find the total amount earned at the end of 5 years.

Sn =  a^{1}(1 - rn) _________ 1 - r 

________________

He will have earned a total of $138,099.03 by the end of 5 years.

**Try It #8**
At a new job, an employee’s starting salary is $32,100. She receives a 2% annual raise. How much will she have earned by the end of 8 years? Using the Formula for the Sum of an Infinite Geometric Series Thus far, we have looked only at finite series. Sometimes, however, we are interested in the sum of the terms of an infinite sequence rather than the sum of only the first n terms. An infinite series is the sum of the terms of an infinite sequence. An example of an infinite series is 2 + 4 + 6 + 8 + ... This series can also be written in summation notation as ∑ k = 1  \infty   2k, where the upper limit of summation is infinity. Because the terms are not tending to zero, the sum of the series increases without bound as we add more terms. Therefore, the sum of this infinite series is not defined. When the sum is not a real number, we say the series diverges. Determining Whether the Sum of an Infinite Geometric Series is Defined If the terms of an infinite geometric series approach 0, the sum of an infinite geometric series can be defined. The terms in this series approach 0:

The common ratio r = 0.2. As n gets very large, the values of rn get very small and approach 0. Each successive term affects the sum less than the preceding term. As each succeeding term gets closer to 0, the sum of the terms approaches a finite value. The terms of any infinite geometric series with -1 < r < 1 approach 0; the sum of a geometric series is defined when -1 < r < 1. determining whether the sum of an infinite geometric series is defined The sum of an infinite series is defined if the series is geometric and -1 < r < 1.

**How To…**
Given the first several terms of an infinite series, determine if the sum of the series exists. 1. Find the ratio of the second term to the first term. 2. Find the ratio of the third term to the second term. 3. Continue this process to ensure the ratio of a term to the preceding term is constant throughout. If so, the series is geometric. 4. If a common ratio, r, was found in step 3, check to see if -1 < r < 1 . If so, the sum is defined. If not, the sum is not defined.

**Example  6**

### Determining Whether the Sum of an Infinite Series is Defined
Determine whether the sum of each infinite series is defined. a. 12 + 8 + 4 + ... b.  3 __ 4  +  1 __ 2  +  1 __ 3  + ... c. ∑ k = 1  \infty   27 ⋅   1 __ 3    k d. ∑ k = 1  \infty   5k

**Solution**
a. The ratio of the second term to the first is  2 __ 3 , which is not the same as the ratio of the third term to the second,  1 __ 2 . The series is not geometric. b. The ratio of the second term to the first is the same as the ratio of the third term to the second. The series is geometric with a common ratio of  2 __ 3 . The sum of the infinite series is defined. c. The given formula is exponential with a base of  1 __ 3 ; the series is geometric with a common ratio of  1 __ 3 . The sum of the infinite series is defined. d. The given formula is not exponential; the series is not geometric because the terms are increasing, and so cannot yield a finite sum.

**Try It #9**
Determine whether the sum of the infinite series is defined.  1 __ 3  +  1 __ 2  +  3 __ 4  +  9 __ 8  + ...

**Try It #10**
Determine whether the sum of the infinite series is defined. 24 + (-12) + 6 + (-3) + ...

**Try It #11**
Determine whether the sum of the infinite series is defined. ∑ k = 1  \infty   15 ⋅ (-0.3)k Finding Sums of Infinite Series When the sum of an infinite geometric series exists, we can calculate the sum. The formula for the sum of an infinite series is related to the formula for the sum of the first n terms of a geometric series.

Sn =  a^{1}(1 - r n) _________ 1 - r 

We will examine an infinite series with r =  1 __ 2 . What happens to r n as n increases?

  1 _ 2    2 =  1 __ 4 

  1 _ 2    3 =  1 __ 8 

  1 _ 2    4 =  1 ___ 16  The value of rn decreases rapidly. What happens for greater values of n?

  1 _ 2    10 =  1 _____

  1 _ 2    20 =  ________

  1 _ 2    30 =  ____________

As n gets very large, r n gets very small. We say that, as n increases without bound, r n approaches 0. As r n approaches 0, 1 - r n approaches 1. When this happens, the numerator approaches a^{1}. This give us a formula for the sum of an infinite geometric series. formula for the sum of an infinite geometric series The formula for the sum of an infinite geometric series with -1 < r < 1 is S =  a^{1} _ 1 - r 

**How To…**
Given an infinite geometric series, find its sum. 1. Identify a^{1} and r. 2. Confirm that -1 < r < 1. 3. Substitute values for a^{1} and r into the formula, S =  a^{1} _ 1 - r . 4. Simplify to find S.

**Example  7**
Finding the Sum of an Infinite Geometric Series Find the sum, if it exists, for the following: k = 1  \infty  __ 3    k - 1 d. ∑ k = 1  \infty    1 __ 9  ⋅   4 __ 3    k

**Solution**
a. There is not a constant ratio; the series is not geometric. b. There is a constant ratio; the series is geometric. a^{1} = 248.6 and r =  99.44 _____ 248.6  = 0.4, so the sum exists. Substitute a^{1} = 248.6 and r = 0.4 into the formula and simplify to find the sum: S =  a^{1} _ 1 - r 

_ _ 3 c. The formula is exponential, so the series is geometric with r = - 1 __ 3 . Find a^{1} by substituting k = 1 into the given explicit formula:

a^{1} = 4,374 ⋅  - 1 __ 3   

Substitute a^{1} = 4,374 and r = - 1 __ 3  into the formula, and simplify to find the sum:

S =  a^{1} _ 1 - r 

S =  __ 1 -  - 1 __ 3    d. The formula is exponential, so the series is geometric, but r > 1. The sum does not exist.

**Example  8**
Finding an Equivalent Fraction for a Repeating Decimal Find an equivalent fraction for the repeating decimal 0. _ 3 Solution We notice the repeating decimal 0. _ 3 = 0.333... so we can rewrite the repeating decimal as a sum of terms.

0. _ Looking for a pattern, we rewrite the sum, noticing that we see the first term multiplied to 0.1 in the second term, and the second term multiplied to 0.1 in the third term.

0. _

First Term Second Term Notice the pattern; we multiply each consecutive term by a common ratio of 0.1 starting with the first term of 0.3. So, substituting into our formula for an infinite geometric sum, we have

S =  a^{1} _ 1 - r  =  0.3 ______ ___ ___ 3 .

**Try It #12**
Find the sum, if it exists. 2 +  2 __ 3  +  2 __ 9  + ...

**Try It #13**
Find the sum, if it exists. ∑ k = 1  \infty 

**Try It #14**
Find the sum, if it exists. ∑ k = 1  \infty    - 3 __ 8    k Solving Annuity Problems At the beginning of the section, we looked at a problem in which a couple invested a set amount of money each month into a college fund for six years. An annuity is an investment in which the purchaser makes a sequence of periodic, equal payments. To find the amount of an annuity, we need to find the sum of all the payments and the interest earned. In the example, the couple invests $50 each month. This is the value of the initial deposit. The account paid 6% annual interest, compounded monthly. To find the interest rate per payment period, we need to divide the 6% annual percentage interest (APR) rate by 12. So the monthly interest rate is 0.5%. We can multiply the amount in the account each month by 100.5% to find the value of the account after interest has been added. We can find the value of the annuity right after the last deposit by using a geometric series with a^{1} = 50 and r = 100.5% = 1.005. After the first deposit, the value of the annuity will be $50. Let us see if we can determine the amount in the college fund and the interest earned. We can find the value of the annuity after n deposits using the formula for the sum of the first n terms of a geometric series. In 6 years, there are 72 months, so n = 72. We can substitute a^{1} = 50, r = 1.005, and n = 72 into the formula, and simplify to find the value of the annuity after 6 years.

_____________ After the last deposit, the couple will have a total of $4,320.44 in the account. Notice, the couple made 72 payments of $50 each for a total of 72(50) = $3,600. This means that because of the annuity, the couple earned $720.44 interest in their college fund. }


**How To…**
Given an initial deposit and an interest rate, find the value of an annuity. 1. Determine a^{1}, the value of the initial deposit. 2. Determine n, the number of deposits. 3. Determine r. a. Divide the annual interest rate by the number of times per year that interest is compounded. b. Add 1 to this amount to find r. 4. Substitute values for a^{1}, r, and n into the formula for the sum of the first n terms of a geometric series, Sn =  a^{1}(1 – rn) _ 1 – r  . 5. Simplify to find Sn, the value of the annuity after n deposits.

**Example  9**

### Solving an Annuity Problem
A deposit of $100 is placed into a college fund at the beginning of every month for 10 years. The fund earns 9% annual interest, compounded monthly, and paid at the end of the month. How much is in the account right after the last deposit? Solution The value of the initial deposit is $100, so a^{1} = 100. A total of 120 monthly deposits are made in the 10 years, so n = 120. To find r, divide the annual interest rate by 12 to find the monthly interest rate and add 1 to represent the new monthly deposit.

____ Substitute a^{1} = 100, r = 1.0075, and n = 120 into the formula for the sum of the first n terms of a geometric series, and simplify to find the value of the annuity.

_______________

So the account has $19,351.43 after the last deposit is made.

**Try It #15**
At the beginning of each month, $200 is deposited into a retirement fund. The fund earns 6% annual interest, compounded monthly, and paid into the account at the end of the month. How much is in the account if deposits are made for 10 years? Access these online resources for additional instruction and practice with series. • Arithmetic Series (http://openstaxcollege.org/l/arithmeticser) • Geometric Series (http://openstaxcollege.org/l/geometricser) • Summation Notation (http://openstaxcollege.org/l/sumnotation)


## 11.4 Section Exercises

### 11.4 Section Exercises
Verbal 1. What is an nth partial sum? 2. What is the difference between an arithmetic sequence and an arithmetic series? 3. What is a geometric series? 4. How is finding the sum of an infinite geometric series different from finding the nth partial sum? 5. What is an annuity? Algebraic For the following exercises, express each description of a sum using summation notation. 6. The sum of terms m^{2} + 3m from m = 1 to m = 5 7. The sum from of n = 0 to n = 4 of 5n 8. The sum of 6k - 5 from k = -2 to k = 1 9. The sum that results from adding the number 4 five times For the following exercises, express each arithmetic sum using summation notation. __ 2  + 1 + 3 ___ 2  + 2 + ... + 4 For the following exercises, use the formula for the sum of the first n terms of each arithmetic sequence. __ 2  + 2 +  5 __ 2  + 3 +  7 __ 2  For the following exercises, express each geometric sum using summation notation. __ 6  +  1 ___ 12  -  1 ___ ___ 768  For the following exercises, use the formula for the sum of the first n terms of each geometric sequence, and then state the indicated sum. _ 3  +  1 _ 9  n = 1   5 ⋅ 2n - 1 a = 1  For the following exercises, determine whether the infinite series has a sum. If so, write the formula for the sum. If not, state the reason. m = 1  \infty   4m - 1 k = 1  \infty   - - 1 __ 2    k - 1

Graphical For the following exercises, use the following scenario. Javier makes monthly deposits into a savings account. He opened the account with an initial deposit of $50. Each month thereafter he increased the previous deposit amount 26. Graph the arithmetic sequence showing one year of Javier’s deposits. 27. Graph the arithmetic series showing the monthly sums of one year of Javier’s deposits. For the following exercises, use the geometric series ∑ k = 1  \infty      1 __ 2    k. 28. Graph the first 7 partial sums of the series. 29. What number does Sn seem to be approaching in the graph? Find the sum to explain why this makes sense. Numeric For the following exercises, find the indicated sum. a = 1   a n = 1   n(n - 2) k = 1   k^{2} k = 1   2k For the following exercises, use the formula for the sum of the first n terms of an arithmetic series to find the sum. ___ 2  + 9 +  21 ___ 2  + 12 +  27 ___ 2  + 15 k = 1     k __ 2  -  1 __ 2    For the following exercises, use the formula for the sum of the first n terms of a geometric series to find the partial sum. 38. S^{6} for the series -2 - 10 - 50 - 250 ... 39. S^{7} for the series 0.4 - 2 + 10 - 50 ... k = 1  2k - 1 n = 1  -2 ⋅   1 __ 2    n - 1 For the following exercises, find the sum of the infinite geometric series. __ 4  -  1 ___ 16  -  1 ___ \infty  k = 1 3 ⋅   1 __ 4    k - 1 n = 1 \infty  For the following exercises, determine the value of the annuity for the indicated monthly deposit amount, the number of deposits, and the interest rate. 46. Deposit amount: $50; total deposits: 60; interest rate: 5%, compounded monthly 47. Deposit amount: $150; total deposits: 24; interest rate: 3%, compounded monthly 48. Deposit amount: $450; total deposits: 60; interest rate: 4.5%, compounded quarterly 49. Deposit amount: $100; total deposits: 120; interest rate: 10%, compounded semi-annually Extensions 50. The sum of terms 50 - k 2 from k = x through 7 is 115. What is x? 51. Write an explicit formula for ak such that ∑ k = 0   ak = 189. Assume this is an arithmetic series. 52. Find the smallest value of n such that ∑ k = 1  n  (3k - 5) > 100. 53. How many terms must be added before the series -1 - 3 - 5 - 7.... has a sum less than -75?

65 as an infinite geometric series using summation notation. Then use the formula for finding the sum of an infinite geometric series to convert 0.65 to a fraction. 55. The sum of an infinite geometric series is five times the value of the first term. What is the common ratio of the series? 56. To get the best loan rates available, the Riches want to save enough money to place 20% down on a $160,000 home. They plan to make monthly deposits of $125 in an investment account that offers 8.5% annual interest compounded semi- annually. Will the Riches have enough for a 20% down payment after five years of saving? How much money will they have saved? 57. Karl has two years to save $10,000 to buy a used car when he graduates. To the nearest dollar, what would his monthly deposits need to be if he invests in an account offering a 4.2% annual interest rate that compounds monthly? Real-World Applications 58. Keisha devised a week-long study plan to prepare for finals. On the first day, she plans to study for 1 hour, and each successive day she will increase her study time by 30 minutes. How many hours will Keisha have studied after one week? 59. A boulder rolled down a mountain, traveling 6 feet in the first second. Each successive second, its distance increased by 8 feet. How far did the boulder travel after 10 seconds? 60. A scientist places 50 cells in a petri dish. Every hour, the population increases by 1.5%. What will the cell count be after 1 day? 61. A pendulum travels a distance of 3 feet on its first swing. On each successive swing, it travels  3 __ 4  the distance of the previous swing. What is the total distance traveled by the pendulum when it stops swinging? 62. Rachael deposits $1,500 into a retirement fund each year. The fund earns 8.2% annual interest, compounded monthly. If she opened her account when she was 19 years old, how much will she have by the time she is 55? How much of that amount will be interest earned?

Learning Objectives
In this section, you will:
• Solve counting problems using the Addition Principle.
• Solve counting problems using the Multiplication Principle.
• Solve counting problems using permutations involving n distinct objects.
• Solve counting problems using combinations.
• Find the number of subsets of a given set.
• Solve counting problems using permutations involving n non-distinct objects.
Counting Principles A new company sells customizable cases for tablets and smartphones. Each case comes in a variety of colors and can be personalized for an additional fee with images or a monogram. A customer can choose not to personalize or could choose to have one, two, or three images or a monogram. The customer can choose the order of the images and the letters in the monogram. The company is working with an agency to develop a marketing campaign with a focus on the huge number of options they offer. Counting the possibilities is challenging! We encounter a wide variety of counting problems every day. There is a branch of mathematics devoted to the study of counting problems such as this one. Other applications of counting include secure passwords, horse racing outcomes, and college scheduling choices. We will examine this type of mathematics in this section. Using the Addition Principle The company that sells customizable cases offers cases for tablets and smartphones. There are 3 supported tablet models and 5 supported smartphone models. The Addition Principle tells us that we can add the number of tablet options to the number of smartphone options to find the total number of options. By the Addition Principle, there are 8 total options, as we can see in Figure 1. the Addition Principle According to the Addition Principle, if one event can occur in m ways and a second event with no common outcomes can occur in n ways, then the first or second event can occur in m + n ways.

**Example  1**
Using the Addition Principle There are 2 vegetarian entrée options and 5 meat entrée options on a dinner menu. What is the total number of entrée options?


## 11.5 Counting Principles
Solution We can add the number of vegetarian options to the number of meat options to find the total number of entrée options. Vegetarian + Vegetarian + Meat + Meat + Meat + Meat + Meat ↓ ↓ ↓ ↓ ↓ ↓ ↓ Option 1 + Option 2 + Option 3 + Option 4 + Option 5 + Option 6 + Option 7 There are 7 total options.

**Try It #1**
A student is shopping for a new computer. He is deciding among 3 desktop computers and 4 laptop computers. What is the total number of computer options? Using the Multiplication Principle The Multiplication Principle applies when we are making more than one selection. Suppose we are choosing an appetizer, an entrée, and a dessert. If there are 2 appetizer options, 3 entrée options, and 2 dessert options on a fixed- price dinner menu, there are a total of 12 possible choices of one each as shown in the tree diagram in Figure 2. Soup Chicken Chicken Fish Fish Steak Steak Cake Cake Cake Cake Cake Cake Pudding Pudding Pudding Pudding Pudding Pudding Salad (Appetizers) (Entress) (Dessert) The possible choices are: 1. soup, chicken, cake 2. soup, chicken, pudding 3. soup, fish, cake 4. soup, fish, pudding 5. soup, steak, cake 6. soup, steak, pudding 7. salad, chicken, cake 8. salad, chicken, pudding 9. salad, fish, cake 10. salad, fish, pudding 11. salad, steak, cake 12. salad, steak, pudding We can also find the total number of possible dinners by multiplying. We could also conclude that there are 12 possible dinner choices simply by applying the Multiplication Principle. # of appetizer options \times  # of entree options \times  # of dessert options

\times  \times  = 12

the Multiplication Principle According to the Multiplication Principle, if one event can occur in m ways and a second event can occur in n ways after the first event has occurred, then the two events can occur in m \times  n ways. This is also known as the Fundamental Counting Principle.

**Example  2**
Using the Multiplication Principle Diane packed 2 skirts, 4 blouses, and a sweater for her business trip. She will need to choose a skirt and a blouse for each outfit and decide whether to wear the sweater. Use the Multiplication Principle to find the total number of possible outfits. Solution To find the total number of outfits, find the product of the number of skirt options, the number of blouse options, and the number of sweater options. # of skirt options \times  # of blouse options \times  # of sweater options

\times  \times  = 16 There are 16 possible outfits.

**Try It #2**
A restaurant offers a breakfast special that includes a breakfast sandwich, a side dish, and a beverage. There are 3 types of breakfast sandwiches, 4 side dish options, and 5 beverage choices. Find the total number of possible breakfast specials. Finding the Number of Permutations of n Distinct Objects The Multiplication Principle can be used to solve a variety of problem types. One type of problem involves placing objects in order. We arrange letters into words and digits into numbers, line up for photographs, decorate rooms, and more. An ordering of objects is called a permutation. Finding the Number of Permutations of n Distinct Objects Using the Multiplication Principle To solve permutation problems, it is often helpful to draw line segments for each option. That enables us to determine the number of each option so we can multiply. For instance, suppose we have four paintings, and we want to find the number of ways we can hang three of the paintings in order on the wall. We can draw three lines to represent the three places on the wall.

\times  \times  There are four options for the first place, so we write a 4 on the first line.

\times  \times  After the first place has been filled, there are three options for the second place so we write a 3 on the second line.

\times  \times  After the second place has been filled, there are two options for the third place so we write a 2 on the third line. Finally, we find the product.

\times  \times  = 24 There are 24 possible permutations of the paintings.

**How To…**
Given n distinct options, determine how many permutations there are. 1. Determine how many options there are for the first situation. 2. Determine how many options are left for the second situation. 3. Continue until all of the spots are filled. 4. Multiply the numbers together.


**Example  3**
Finding the Number of Permutations Using the Multiplication Principle At a swimming competition, nine swimmers compete in a race. a. How many ways can they place first, second, and third? b. How many ways can they place first, second, and third if a swimmer named Ariel wins first place? (Assume there is only one contestant named Ariel.) c. How many ways can all nine swimmers line up for a photo?

**Solution**
a. Draw lines for each place. \times  \times  There are 9 options for first place. Once someone has won first place, there are 8 remaining options for second place. Once first and second place have been won, there are 7 remaining options for third place.

\times  \times  = 504 Multiply to find that there are 504 ways for the swimmers to place. b. Draw lines for describing each place. \times  \times  We know Ariel must win first place, so there is only 1 option for first place. There are 8 remaining options for second place, and then 7 remaining options for third place.

\times  \times  = 56 Multiply to find that there are 56 ways for the swimmers to place if Ariel wins first. c. Draw lines for describing each place in the photo. \times  \times  \times  \times  \times  \times  \times  \times  There are 9 choices for the first spot, then 8 for the second, 7 for the third, 6 for the fourth, and so on until only 1 person remains for the last spot. \times  \times  \times  \times  \times  \times  \times  \times  There are 362,880 possible permutations for the swimmers to line up. Analysis Note that in part c, we found there were 9! ways for 9 people to line up. The number of permutations of n distinct objects can always be found by n!.

**Try It #3**
A family of five is having portraits taken. Use the Multiplication Principle to find how many ways the family can line up for the portrait.

**Try It #4**
A family of five is having portraits taken. Use the Multiplication Principle to find how many ways the photographer can line up 3 of the family members.

**Try It #5**
A family of five is having portraits taken. Use the Multiplication Principle to find how many ways the family can line up for the portrait if the parents are required to stand on each end. options for 1st place options for 2nd place options for 3rd place options for 1st place options for 2nd place options for 3rd place

Finding the Number of Permutations of n Distinct Objects Using a Formula For some permutation problems, it is inconvenient to use the Multiplication Principle because there are so many numbers to multiply. Fortunately, we can solve these problems using a formula. Before we learn the formula, let’s look at two common notations for permutations. If we have a set of n objects and we want to choose r objects from the set in order, we write P (n, r). Another way to write this is nPr, a notation commonly seen on computers and calculators. To calculate P(n, r), we begin by finding n!, the number of ways to line up all n objects. We then divide by (n - r)! to cancel out the (n - r) items that we do not wish to line up. Let’s see how this works with a simple example. Imagine a club of six people. They need to elect a president, a vice president, and a treasurer. Six people can be elected president, any one of the five remaining people can be elected vice president, and any of the remaining four people could be elected treasurer. The number of ways this may be done is 6 \times  5 \times  4 = 120. Using factorials, we get the same result.  6! __ 3!  =  6 \cdot  5 \cdot  4 \cdot  3! _________ 3!  = 6 \cdot  5 \cdot  4 = 120 There are 120 ways to select 3 officers in order from a club with 6 members. We refer to this as a permutation of 6 taken 3 at a time. The general formula is as follows. P(n, r) =  n! _______ (n - r)!  Note that the formula stills works if we are choosing all n objects and placing them in order. In that case we would be dividing by (n - n)! or 0!, which we said earlier is equal to 1. So the number of permutations of n objects taken n at a time is  n! __ 1  or just n!. formula for permutations of n distinct objects Given n distinct objects, the number of ways to select r objects from the set in order is P(n, r) =  n! _______ (n - r)! 

**How To…**
Given a word problem, evaluate the possible permutations. 1. Identify n from the given information. 2. Identify r from the given information. 3. Replace n and r in the formula with the given values. 4. Evaluate.

**Example  4**
Finding the Number of Permutations Using the Formula A professor is creating an exam of 9 questions from a test bank of 12 questions. How many ways can she select and arrange the questions? Solution Substitute n = 12 and r = 9 into the permutation formula and simplify.

P(n, r) =  n! _______ (n - r)! 

P(12, 9) =  12! ________ (12 - 9)!  =  12! ___ There are 79,833,600 possible permutations of exam questions! Analysis We can also use a calculator to find permutations. For this problem, we would enter 15, press the [nPr function], enter [12], and then press the equal sign. The [nPr function] may be located under the [MATH] menu with probability commands. Could we have solved Example 4 using the Multiplication Principle? Yes. We could have multiplied 15 ⋅ 14 ⋅ 13 ⋅ 12 ⋅ 11 ⋅ 10 ⋅ 9 ⋅ 8 ⋅ 7 ⋅ 6 ⋅ 5 ⋅ 4 to find the same answer.


**Try It #6**
A play has a cast of 7 actors preparing to make their curtain call. Use the permutation formula to find how many ways the 7 actors can line up.

**Try It #7**
A play has a cast of 7 actors preparing to make their curtain call. Use the permutation formula to find how many ways 5 of the 7 actors can be chosen to line up. Find the Number of Combinations Using the Formula So far, we have looked at problems asking us to put objects in order. There are many problems in which we want to select a few objects from a group of objects, but we do not care about the order. When we are selecting objects and the order does not matter, we are dealing with combinations. A selection of r objects from a set of n objects where the order does not matter can be written as C (n, r). Just as with permutations, C(n, r) can also be written as nCr. In this case, the general formula is as follows. C (n, r) =  n! _________ r!(n - r)!  An earlier problem considered choosing 3 of 4 possible paintings to hang on a wall. We found that there were 24 ways to select 3 of the 4 paintings in order. But what if we did not care about the order? We would expect a smaller number because selecting paintings 1, 2, 3 would be the same as selecting paintings 2, 3, 1. To find the number of ways to select 3 of the 4 paintings, disregarding the order of the paintings, divide the number of permutations by the number of ways to order 3 paintings. There are 3! = 3 \cdot  2 \cdot  1 = 6 ways to order 3 paintings. There are  24 ___ 6  , or 4 ways to select 3 of the 4 paintings. This number makes sense because every time we are selecting 3 paintings, we are not selecting 1 painting. There are 4 paintings we could choose not to select, so there are 4 ways to select 3 of the 4 paintings. formula for combinations of n distinct objects Given n distinct objects, the number of ways to select r objects from the set is C (n, r) =  n! _________ r!(n - r)! 

**How To…**
Given a number of options, determine the possible number of combinations. 1. Identify n from the given information. 2. Identify r from the given information. 3. Replace n and r in the formula with the given values. 4. Evaluate.

**Example  5**
Finding the Number of Combinations Using the Formula A fast food restaurant offers five side dish options. Your meal comes with two side dishes. a. How many ways can you select your side dishes? b. How many ways can you select 3 side dishes?

**Solution**
a. We want to choose 2 side dishes from 5 options.

C(5, 2) =  5! ________ 2!(5 - 2)!  = 10 b. We want to choose 3 side dishes from 5 options.

C(5, 3) =  5! ________ 3!(5 - 3)!  = 10

Analysis We can also use a graphing calculator to find combinations. Enter 5, then press nCr, enter 3, and then press the equal sign. The nCr function may be located under the MATH menu with probability commands. Is it a coincidence that parts ( a) and ( b) in Example 5 have the same answers? No. When we choose r objects from n objects, we are not choosing (n - r) objects. Therefore, C(n, r) = C(n, n - r).

**Try It #8**
An ice cream shop offers 10 flavors of ice cream. How many ways are there to choose 3 flavors for a banana split? Finding the Number of Subsets of a Set We have looked only at combination problems in which we chose exactly r objects. In some problems, we want to consider choosing every possible number of objects. Consider, for example, a pizza restaurant that offers 5 toppings. Any number of toppings can be ordered. How many different pizzas are possible? To answer this question, we need to consider pizzas with any number of toppings. There is C(5, 0) = 1 way to order a pizza with no toppings. There are C(5, 1) = 5 ways to order a pizza with exactly one topping. If we continue this process, we get C(5, 0) + C(5, 1) + C(5, 2) + C(5, 3) + C(5, 4) + C(5, 5) = 32 There are 32 possible pizzas. This result is equal to 25. We are presented with a sequence of choices. For each of the n objects we have two choices: include it in the subset or not. So for the whole subset we have made n choices, each with two options. So there are a total of 2 \cdot  2 \cdot  2 \cdot  ... \cdot  2 possible resulting subsets, all the way from the empty subset, which we obtain when we say “no” each time, to the original set itself, which we obtain when we say “yes” each time. formula for the number of subsets of a set A set containing n distinct objects has 2n subsets.

**Example  6**
Finding the Number of Subsets of a Set A restaurant offers butter, cheese, chives, and sour cream as toppings for a baked potato. How many different ways are there to order a potato? Solution We are looking for the number of subsets of a set with 4 objects. Substitute n = 4 into the formula.

= 16 There are 16 possible ways to order a potato.

**Try It #9**
A sundae bar at a wedding has 6 toppings to choose from. Any number of toppings can be chosen. How many different sundaes are possible? Finding the Number of Permutations of n Non-Distinct Objects We have studied permutations where all of the objects involved were distinct. What happens if some of the objects are indistinguishable? For example, suppose there is a sheet of 12 stickers. If all of the stickers were distinct, there would be 12! ways to order the stickers. However, 4 of the stickers are identical stars, and 3 are identical moons. Because all of the objects are not distinct, many of the 12! permutations we counted are duplicates. The general formula for this situation is as follows.

 n! __________ r^{1}! r^{2} ! ... rk !  In this example, we need to divide by the number of ways to order the 4 stars and the ways to order the 3 moons to find the number of unique permutations of the stickers. There are 4! ways to order the stars and 3! ways to order the moon.  12! ____ There are 3,326,400 ways to order the sheet of stickers. formula for finding the number of permutations of n non-distinct objects If there are n elements in a set and r^{1} are alike, r^{2} are alike, r^{3} are alike, and so on through rk , the number of permutations can be found by  n! __________ r^{1}! r^{2}! ... rk ! 

**Example  7**
Finding the Number of Permutations of n Non-Distinct Objects Find the number of rearrangements of the letters in the word DISTINCT. Solution There are 8 letters. Both I and T are repeated 2 times. Substitute n = 8, r^{1} = 2, and r^{2} = 2 into the formula.  8! ____ There are 10,080 arrangements.

**Try It #10**
Find the number of rearrangements of the letters in the word CARRIER. Access these online resources for additional instruction and practice with combinations and permutations. • Combinations (http://openstaxcollege.org/l/combinations) • Permutations (http://openstaxcollege.org/l/permutations)


### 11.5 Section Exercises
Verbal For the following exercises, assume that there are n ways an event A can happen, m ways an event B can happen, and that A and B are non-overlapping. 1. Use the Addition Principle of counting to explain how many ways event A or B can occur. 2. Use the Multiplication Principle of counting to explain how many ways event A and B can occur. Answer the following questions. 3. When given two separate events, how do we know whether to apply the Addition Principle or the Multiplication Principle when calculating possible outcomes? What conjunctions may help to determine which operations to use? 4. Describe how the permutation of n objects differs from the permutation of choosing r objects from a set of n objects. Include how each is calculated. 5. What is the term for the arrangement that selects r objects from a set of n objects when the order of the r objects is not important? What is the formula for calculating the number of possible outcomes for this type of arrangement? Numeric For the following exercises, determine whether to use the Addition Principle or the Multiplication Principle. Then perform the calculations. 6. Let the set A = { -5, -3, -1, 2, 3, 4, 5, 6}. How many ways are there to choose a negative or an even number from A? How many ways are there to choose a positive or an odd number from A? 8. How many ways are there to pick a red ace or a club from a standard card playing deck? 9. How many ways are there to pick a paint color from 5 shades of green, 4 shades of blue, or 7 shades of yellow? 10. How many outcomes are possible from tossing a pair of coins? 11. How many outcomes are possible from tossing a coin and rolling a 6-sided die? 12. How many two-letter strings—the first letter from A and the second letter from B—can be formed from the sets A = {b, c, d } and B = {a, e, i, o, u}? 13. How many ways are there to construct a string of 3 digits if numbers can be repeated? 14. How many ways are there to construct a string of 3 digits if numbers cannot be repeated? For the following exercises, compute the value of the expression. For the following exercises, find the number of subsets in each given set. 27. A set containing 5 distinct numbers, 4 distinct letters, and 3 distinct symbols 28. The set of even numbers from 2 to 28 29. The set of two-digit numbers between 1 and 100 containing the digit 0 For the following exercises, find the distinct number of arrangements. 30. The letters in the word “juggernaut” 31. The letters in the word “academia” 32. The letters in the word “academia” that begin and end in “a” 33. The symbols in the string #,#,#,@,@,$,$,$,%,%,%,% 34. The symbols in the string #,#,#,@,@,$,$,$,%,%,%,% that begin and end with “%”


## 11.5 Section Exercises
Extensions 35. The set, S consists of 900,000,000 whole numbers, each being the same number of digits long. How many digits long is a number from S? (Hint: use the fact that a whole number cannot start with the digit 0.) 36. The number of 5-element subsets from a set containing n elements is equal to the number of 6-element subsets from the same set. What is the value of n? (Hint: the order in which the elements for the subsets are chosen is not important.) 37. Can C(n, r) ever equal P(n, r)? Explain. 38. Suppose a set A has 2,048 subsets. How many distinct objects are contained in A? 39. How many arrangements can be made from the letters of the word “mountains” if all the vowels must form a string? Real-World Applications 40. A family consisting of 2 parents and 3 children is to pose for a picture with 2 family members in the front and 3 in the back. a. How many arrangements are possible with no restrictions? b. How many arrangements are possible if the parents must sit in the front? c. How many arrangements are possible if the parents must be next to each other? 41. A cell phone company offers 6 different voice packages and 8 different data packages. Of those, 3 packages include both voice and data. How many ways are there to choose either voice or data, but not both? 42. In horse racing, a “trifecta” occurs when a bettor wins by selecting the first three finishers in the exact order (1st place, 2nd place, and 3rd place). How many different trifectas are possible if there are 14 horses in a race? 43. A wholesale T-shirt company offers sizes small, medium, large, and extra-large in organic or non- organic cotton and colors white, black, gray, blue, and red. How many different T-shirts are there to choose from? 44. Hector wants to place billboard advertisements throughout the county for his new business. How many ways can Hector choose 15 neighborhoods to advertise in if there are 30 neighborhoods in the county? 45. An art store has 4 brands of paint pens in 12 different colors and 3 types of ink. How many paint pens are there to choose from? 46. How many ways can a committee of 3 freshmen and 4 juniors be formed from a group of 8 freshmen and 11 juniors? 47. How many ways can a baseball coach arrange the order of 9 batters if there are 15 players on the team? 48. A conductor needs 5 cellists and 5 violinists to play at a diplomatic event. To do this, he ranks the orchestra’s 10 cellists and 16 violinists in order of musical proficiency. What is the ratio of the total cellist rankings possible to the total violinist rankings possible? 49. A motorcycle shop has 10 choppers, 6 bobbers, and 5 café racers—different types of vintage motorcycles. How many ways can the shop choose 3 choppers, 5 bobbers, and 2 café racers for a weekend showcase? 50. A skateboard shop stocks 10 types of board decks, 3 types of trucks, and 4 types of wheels. How many different skateboards can be constructed? 51. Just-For-Kicks Sneaker Company offers an online customizing service. How many ways are there to design a custom pair of Just-For-Kicks sneakers if a customer can choose from a basic shoe up to 11 customizable options? 52. A car wash offers the following optional services to the basic wash: clear coat wax, triple foam polish, undercarriage wash, rust inhibitor, wheel brightener, air freshener, and interior shampoo. How many washes are possible if any number of options can be added to the basic wash? 53. Susan bought 20 plants to arrange along the border of her garden. How many distinct arrangements can she make if the plants are comprised of 6 tulips, 6 roses, and 8 daisies? 54. How many unique ways can a string of Christmas lights be arranged from 9 red, 10 green, 6 white, and 12 gold color bulbs?

Learning Objectives
In this section, you will:
• Apply the Binomial Theorem.
Binomial Theorem A polynomial with two terms is called a binomial. We have already learned to multiply binomials and to raise binomials to powers, but raising a binomial to a high power can be tedious and time-consuming. In this section, we will discuss a shortcut that will allow us to find (x + y)n without multiplying the binomial by itself n times. Identifying Binomial Coefficients In Counting Principles, we studied combinations. In the shortcut to finding (x + y)n, we will need to use combinations to find the coefficients that will appear in the expansion of the binomial. In this case, we use the notation   n _ r   instead of C(n, r), but it can be calculated in the same way. So   n _ r   = C(n, r) =  n! ________ r!(n - r)!  The combination   n _ r   is called a binomial coefficient. An example of a binomial coefficient is   5 __ 2   = C(5, 2) = 10. binomial coefficients If n and r are integers greater than or equal to 0 with n \ge  r, then the binomial coefficient is   n _ r   = C(n, r) =  n! ________ r!(n - r)!  Is a binomial coefficient always a whole number? Yes. Just as the number of combinations must always be a whole number, a binomial coefficient will always be a whole number.

**Example  1**
Finding Binomial Coefficients Find each binomial coefficient. a.   5 __ 3   b.   9 __ 2   c.   9 __ 7  

**Solution**
Use the formula to calculate each binomial coefficient. You can also use the nCr function on your calculator.   n _ r   = C(n, r) =  n! ________ r!(n - r)!  a.   5 __ 3   =  5! ________ 3!(5 - 3)!  =  5 ⋅ 4 ⋅ 3! _______ 3!2!  = 10 b.   9 __ 2   =  9! ________ 2!(9 - 2)!  =  9 ⋅ 8 ⋅ 7! _______ 2!7!  = 36 c.   9 __ 7   =  9! ________ 7!(9 - 7)!  =  9 ⋅ 8 ⋅ 7! _______ 7!2!  = 36 Analysis Notice that we obtained the same result for parts (b) and (c). If you look closely at the solution for these two parts, you will see that you end up with the same two factorials in the denominator, but the order is reversed, just as with combinations.   n _ r   =   n _ n - r  


## 11.6 Binomial Theorem

**Try It #1**
Find each binomial coefficient. a.   7 __ 3   b.   11 __ 4   Using the Binomial Theorem When we expand (x + y)n by multiplying, the result is called a binomial expansion, and it includes binomial coefficients. If we wanted to expand (x + y)^{5}2, we might multiply (x + y) by itself fifty-two times. This could take hours! If we examine some simple binomial expansions, we can find patterns that will lead us to a shortcut for finding more complicated binomial expansions.

(x + y)^{2} = x 2 + 2xy + y 2

(x + y)^{3} = x 3 + 3x 2 y + 3xy 2 + y 3

(x + y)^{4} = x 4 + 4x 3 y + 6x 2 y 2 + 4xy 3 + y 4 First, let’s examine the exponents. With each successive term, the exponent for x decreases and the exponent for y increases. The sum of the two exponents is n for each term. Next, let’s examine the coefficients. Notice that the coefficients increase and then decrease in a symmetrical pattern. The coefficients follow a pattern:   n _ 0  ,   n _ 1  ,   n _ 2  , ...,   n _ n  . These patterns lead us to the Binomial Theorem, which can be used to expand any binomial.

(x + y)n = ∑ k = 0  n    n _ k   xn - kyk

= xn +   n _ 1  xn - 1 y +   n _ 2  xn - 2 y 2 + ... +   n _ n - 1  xy n - 1 + yn Another way to see the coefficients is to examine the expansion of a binomial in general form, x + y, to successive

(x + y)^{1} = x + y

(x + y)^{2} = x^{2} + 2xy + y^{2}

(x + y)^{3} = x^{3} + 3x^{2} y + 3xy^{2} + y^{3}

(x + y)^{4} = x^{4} + 4x^{3} y + 6x^{2} y^{2} + 4xy^{3} + y^{4} Can you guess the next expansion for the binomial (x + y)^{5}? Exponent sum: Exponents on x: Exponents on y: 1 + 1 2 + 1 3 + 1 4 + 1 4+0 n + 1 n + 1 n (x + y)^{1} = x + y Exponent Pascal’s Triangle Pattern # of Terms (x + y)^{2} = x^{2} + 2xy + y^{2} (x + y)^{3} = x^{3} + 3x^{2}y + 3xy^{2} + y^{3} xy 3+1 xy 2+2 xy 1+3 xy 0+4 xy (x + y)^{4} = x^{4} + 4x^{3}y + 6x^{2}y^{2} + 4xy^{3} + y^{4}

See Figure 1, which illustrates the following: • There are n + 1 terms in the expansion of (x + y)n. • The degree (or sum of the exponents) for each term is n. • The powers on x begin with n and decrease to 0. • The powers on y begin with 0 and increase to n. • The coefficients are symmetric. To determine the expansion on (x + y)^{5}, we see n = 5, thus, there will be 5 + 1 = 6 terms. Each term has a combined degree of 5. In descending order for powers of x, the pattern is as follows: • Introduce x 5, and then for each successive term reduce the exponent on x by 1 until x 0 = 1 is reached. • Introduce y 0 = 1, and then increase the exponent on y by 1 until y 5 is reached. The next expansion would be (x + y)^{5} = x^{5} + 5x 4y + 10x 3y^{2} + 10x 2y 3 + 5xy 4 + y 5. But where do those coefficients come from? The binomial coefficients are symmetric. We can see these coefficients in an array known as Pascal's Triangle, shown in Figure 2. Pascal’s Triangle 1 + 2 = 3 To generate Pascal’s Triangle, we start by writing a 1. In the row below, row 2, we write two 1’s. In the 3rd row, flank the ends of the rows with 1’s, and add 1 + 1 to find the middle number, 2. In the nth row, flank the ends of the row with 1’s. Each element in the triangle is the sum of the two elements immediately above it. To see the connection between Pascal’s Triangle and binomial coefficients, let us revisit the expansion of the binomials in general form. 1 → (x + y)^{0} = 1 1 → (x + y)^{1} = x + y 1 → (x + y)^{2} = x 2 + 2xy + y 2 1 → (x + y)^{3} = x 3 + 3x 2y + 3xy^{2} + y 3 1 → (x + y)^{4} = x^{4} + 4x 3y + 6x 2y 2 + 4xy 3 + y 4 1 → (x + y)^{5} = x 5 + 5x 4y + 10x 3y 2 + 10x 2 y 3 + 5xy 4 + y 5 the Binomial Theorem The Binomial Theorem is a formula that can be used to expand any binomial.

(x + y)n = ∑ k = 0  n    n k   x n - k yk

= x n +   n _ 1  x n - 1 y +   n _ 2  x n - 2y 2 + ... +   n _ n - 1  xy n - 1 + y n


**How To…**
Given a binomial, write it in expanded form. 1. Determine the value of n according to the exponent. 2. Evaluate the k = 0 through k = n using the Binomial Theorem formula. 3. Simplify.

**Example  2**
Expanding a Binomial Write in expanded form. a. (x + y)^{5} b. (3x - y)^{4}

**Solution**
a. Substitute n = 5 into the formula. Evaluate the k = 0 through k = 5 terms. Simplify.

(x + y)^{5} =   5 _ 0  x 5y 0 +   5 _ 1  x 4y^{1} +   5 _ 2  x 3y 2 +   5 _ 3  x 2y 3 +   5 _ 4  x^{1}y 4 +   5 _ 5  x 0y 5

(x + y)^{5} = x 5 + 5x 4y + 10x 3y 2 + 10x 2y 3 + 5xy 4 + y 5 b. Substitute n = 4 into the formula. Evaluate the k = 0 through k = 4 terms. Notice that 3x is in the place that was occupied by x and that -y is in the place that was occupied by y. So we substitute them. Simplify.

(3x - y)^{4} =   4 _ 0  (3x)^{4}(-y)^{0} +   4 _ 1  (3x)^{3}(-y)^{1} +   4 _ 2  (3x)^{2}(-y)^{2} +   4 _ 3  (3x)^{1}(-y)^{3} +  4 _ 4  (3x)^{0}(-y)^{4}

(3x - y)^{4} = 81x 4 - 108x 3y + 54x 2y 2 - 12xy 3 + y 4 Analysis Notice the alternating signs in part b. This happens because (-y) raised to odd powers is negative, but (-y) raised to even powers is positive. This will occur whenever the binomial contains a subtraction sign.

**Try It #2**
Write in expanded form. a. (x - y)^{5} b. (2x + 5y)^{3} Using the Binomial Theorem to Find a Single Term Expanding a binomial with a high exponent such as (x + 2y)^{1}6 can be a lengthy process. Sometimes we are interested only in a certain term of a binomial expansion. We do not need to fully expand a binomial to find a single specific term. Note the pattern of coefficients in the expansion of (x + y)^{5}. (x + y)^{5} = x 5 +   5 _ 1  x 4y +   5 _ 2  x^{3}y^{2} +   5 _ 3  x 2y 3 +   5 _ 4  xy 4 + y 5 The second term is   5 _ 1  x 4y. The third term is   5 _ 2  x 3y 2. We can generalize this result.   n _ r  xn - ry r the (r + 1)th term of a binomial expansion The (r + 1)th term of the binomial expansion of (x + y)n is:   n _ r  x n - ry r


**How To…**
Given a binomial, write a specific term without fully expanding. 1. Determine the value of n according to the exponent. 2. Determine (r + 1). 3. Determine r. 4. Replace r in the formula for the (r + 1)th term of the binomial expansion.

**Example  3**

### Writing a Given Term of a Binomial Expansion
Find the tenth term of (x + 2y)^{1}6 without fully expanding the binomial. Solution Because we are looking for the tenth term, r + 1 = 10, we will use r = 9 in our calculations.   n _ r  xn - r yr   16 _

**Try It #3**
Find the sixth term of (3x - y)^{9} without fully expanding the binomial. Access these online resources for additional instruction and practice with binomial expansion. • The Binomial Theorem (http://openstaxcollege.org/l/binomialtheorem) • Binomial Theorem Example (http://openstaxcollege.org/l/btexample)


## 11.6 Section Exercises

### 11.6 Section Exercises
Verbal 1. What is a binomial coefficient, and how it is calculated? 2. What role do binomial coefficients play in a binomial expansion? Are they restricted to any type of number? 3. What is the Binomial Theorem and what is its use? 4. When is it an advantage to use the Binomial Theorem? Explain. Algebraic For the following exercises, evaluate the binomial coefficient. 5.   6 _ 2   6.   5 _ 3   7.   7 _ 4   8.   9 _ 7   _ 9   _ 11   _ 6   _ For the following exercises, use the Binomial Theorem to expand each binomial. _ x  + 3y   5 x  - \sqrt{y} )^{5} For the following exercises, use the Binomial Theorem to write the first three terms of each binomial. 29. (x^{3} - \sqrt{y} )^{8} For the following exercises, find the indicated term of each binomial without fully expanding the binomial. 30. The fourth term of (2x - 3y)^{4} 31. The fourth term of (3x - 2y)^{5} 32. The third term of (6x - 3y)^{7} 33. The eighth term of (7 + 5y)^{1}4 34. The seventh term of (a + b)^{1}1 35. The fifth term of (x - y)^{7} 36. The tenth term of (x - 1)^{1}2 37. The ninth term of (a - 3b 2)^{1}1 38. The fourth term of  x 3 -  1 __ 2     39. The eighth term of   y _ 2  +  2 _ x     Graphical For the following exercises, use the Binomial Theorem to expand the binomial f (x) = (x + 3)^{4}. Then find and graph each indicated sum on one set of axes. 40. Find and graph f^{1}(x), such that f^{1}(x) is the first term of the expansion. 41. Find and graph f^{2}(x), such that f^{2}(x) is the sum of the first two terms of the expansion. 42. Find and graph f^{3}(x), such that f^{3}(x) is the sum of the first three terms of the expansion. 43. Find and graph f^{4}(x), such that f^{4}(x) is the sum of the first four terms of the expansion. 44. Find and graph f^{5}(x), such that f^{5}(x) is the sum of the first five terms of the expansion.

Extensions 45. In the expansion of (5x + 3y)n, each term has the form   n _ k  an - kbk, where k successively takes on the value 0, 1, 2, ..., n. If   n _ k   =   7 _ 2  , what is the corresponding term? 46. In the expansion of (a + b)n, the coefficient of a n - kbk is the same as the coefficient of which other term? 47. Consider the expansion of (x + b)^{4}0. What is the exponent of b in the kth term? 48. Find   n _ k - 1   +   n _ k   and write the answer as a binomial coefficient in the form   n _ k  . Prove it. Hint: Use the fact that, for any integer p, such that p \ge  1, p! = p(p - 1)!. 49. Which expression cannot be expanded using the Binomial Theorem? Explain. a. (x 2 - 2x + 1) b. (\sqrt{a}  + 4\sqrt{a}  - 5) c. (x 3 + 2y 2 - z)^{5} d. (3x 2 - \sqrt{2y} 3 )


## 11.7 Probability
Learning Objectives
In this section, you will:
• Construct probability models.
• Compute probabilities of equally likely outcomes.
• Compute probabilities of the union of two events.
• Use the complement rule to find probabilities.
• Compute probability using counting theory.
Residents of the Southeastern United States are all too familiar with charts, known as spaghetti models, such as the one in Figure 1. They combine a collection of weather data to predict the most likely path of a hurricane. Each colored line represents one possible path. The group of squiggly lines can begin to resemble strands of spaghetti, hence the name. In this section, we will investigate methods for making these types of predictions. Constructing Probability Models Suppose we roll a six-sided number cube. Rolling a number cube is an example of an experiment, or an activity with an observable result. The numbers on the cube are possible results, or outcomes, of this experiment. The set of all possible outcomes of an experiment is called the sample space of the experiment. The sample space for this experiment is {1, 2, 3, 4, 5, 6}. An event is any subset of a sample space. The likelihood of an event is known as probability. The probability of an event p is a number that always satisfies 0 \le  p \le  1, where 0 indicates an impossible event and 1 indicates a certain event. A probability model is a mathematical description of an experiment listing all possible outcomes and their associated probabilities. For instance, if there is a 1% chance of winning a raffle and a 99% chance of losing the raffle, a probability model would look much like Table 1. Outcome Probability Winning the raffle 1% Losing the raffle 99% The sum of the probabilities listed in a probability model must equal 1, or 100%. 34 The figure is for illustrative purposes only and does not model any particular storm.


**How To…**
Given a probability event where each event is equally likely, construct a probability model. 1. Identify every outcome. 2. Determine the total number of possible outcomes. 3. Compare each outcome to the total number of possible outcomes.

**Example  1**
Constructing a Probability Model Construct a probability model for rolling a single, fair die, with the event being the number shown on the die. Solution Begin by making a list of all possible outcomes for the experiment. The possible outcomes are the numbers that can be rolled: 1, 2, 3, 4, 5, and 6. There are six possible outcomes that make up the sample space. Assign probabilities to each outcome in the sample space by determining a ratio of the outcome to the number of possible outcomes. There is one of each of the six numbers on the cube, and there is no reason to think that any particular face is more likely to show up than any other one, so the probability of rolling any number is  1 __ 6 . Outcome Roll of 1 Roll of 2 Roll of 3 Roll of 4 Roll of 5 Roll of 6 Probability  1 __ 6   1 __ 6   1 __ 6   1 __ 6   1 __ 6   1 __ 6  Do probabilities always have to be expressed as fractions? No. Probabilities can be expressed as fractions, decimals, or percents. Probability must always be a number between 0 and 1, inclusive of 0 and 1.

**Try It #1**
Construct a probability model for tossing a fair coin. Computing Probabilities of Equally Likely Outcomes Let S be a sample space for an experiment. When investigating probability, an event is any subset of S. When the outcomes of an experiment are all equally likely, we can find the probability of an event by dividing the number of outcomes in the event by the total number of outcomes in S. Suppose a number cube is rolled, and we are interested in finding the probability of the event “rolling a number less than or equal to 4.” There are 4 possible outcomes in the event and 6 possible outcomes in S, so the probability of the event is  4 __ 6  =  2 __ 3 . computing the probability of an event with equally likely outcomes The probability of an event E in an experiment with sample space S with equally likely outcomes is given by P(E) =  number of elements in E

____________________

number of elements in S  =  n(E) ____ n(S)  E is a subset of S, so it is always true that 0 \le  P(E) \le  1.

**Example  2**

### Computing the Probability of an Event with Equally Likely Outcomes
A six-sided number cube is rolled. Find the probability of rolling an odd number. Solution The event “rolling an odd number” contains three outcomes. There are 6 equally likely outcomes in the sample space. Divide to find the probability of the event. P(E) =  3 __ 6  =  1 __ 2 


**Try It #2**
A six-sided number cube is rolled. Find the probability of rolling a number greater than 2. Computing the Probability of the Union of Two Events We are often interested in finding the probability that one of multiple events occurs. Suppose we are playing a card game, and we will win if the next card drawn is either a heart or a king. We would be interested in finding the probability of the next card being a heart or a king. The union of two events E and F, written E ∪ F, is the event that occurs if either or both events occur. P(E ∪ F) = P(E) + P(F) - P(E ∩ F) Suppose the spinner in Figure 2 is spun. We want to find the probability of spinning orange or spinning a b. a a b b c d There are a total of 6 sections, and 3 of them are orange. So the probability of spinning orange is  3 __ 6  =  1 __ 2 . There are a total of 6 sections, and 2 of them have a b. So the probability of spinning a b is  2 __ 6  =  1 __ 3 . If we added these two probabilities, we would be counting the sector that is both orange and a b twice. To find the probability of spinning an orange or a b, we need to subtract the probability that the sector is both orange and has a b.  1 __ 2  +  1 __ 3  -  1 __ 6  =  2 __ 3  The probability of spinning orange or a b is  2 __ 3 . probability of the union of two events The probability of the union of two events E and F (written E ∪ F) equals the sum of the probability of E and the probability of F minus the probability of E and F occurring together (which is called the intersection of E and F and is written as E ∩ F).

P(E ∪ F) = P(E) + P(F) - P(E ∩ F)

**Example  3**

### Computing the Probability of the Union of Two Events
A card is drawn from a standard deck. Find the probability of drawing a heart or a 7. Solution A standard deck contains an equal number of hearts, diamonds, clubs, and spades. So the probability of drawing a heart is  1 __ 4 . There are four 7s in a standard deck, and there are a total of 52 cards. So the probability of drawing a 7 is  1 ___ 13 . The only card in the deck that is both a heart and a 7 is the 7 of hearts, so the probability of drawing both a heart and a 7 is  1 ___ 52 . Substitute P(H) =  1 __ 4 , P(7) =  1 ___ 13 , and P(H ∩ 7) =  1 ___ 52  into the formula.

P(E ∪ F) = P(E) + P(F) - P(E ∩ F)

=  1 __ 4  +  1 ___ 13  -  1 ___ 52 

=  4 ___ 13  The probability of drawing a heart or a 7 is  4 ___ 13 .


**Try It #3**
A card is drawn from a standard deck. Find the probability of drawing a red card or an ace. Computing the Probability of Mutually Exclusive Events Suppose the spinner in Figure 2 is spun again, but this time we are interested in the probability of spinning an orange or a d. There are no sectors that are both orange and contain a d, so these two events have no outcomes in common. Events are said to be mutually exclusive events when they have no outcomes in common. Because there is no overlap, there is nothing to subtract, so the general formula is

P(E ∪ F) = P(E) + P(F) Notice that with mutually exclusive events, the intersection of E and F is the empty set. The probability of spinning an orange is  3 __ 6  =  1 __ 2  and the probability of spinning a d is  1 __ 6 . We can find the probability of spinning an orange or a d simply by adding the two probabilities.

P(E ∪ F) = P(E) + P(F)

=  1 __ 2  +  1 __ 6 

=  2 __ 3  The probability of spinning an orange or a d is  2 __ 3 . probability of the union of mutually exclusive events The probability of the union of two mutually exclusive events E and F is given by P(E ∪ F) = P(E) + P(F)

**How To…**
Given a set of events, compute the probability of the union of mutually exclusive events. 1. Determine the total number of outcomes for the first event. 2. Find the probability of the first event. 3. Determine the total number of outcomes for the second event. 4. Find the probability of the second event. 5. Add the probabilities.

**Example  4**

### Computing the Probability of the Union of Mutually Exclusive Events
A card is drawn from a standard deck. Find the probability of drawing a heart or a spade. Solution The events “drawing a heart” and “drawing a spade” are mutually exclusive because they cannot occur at the same time. The probability of drawing a heart is  1 __ 4 , and the probability of drawing a spade is also  1 __ 4 , so the probability of drawing a heart or a spade is

 1 __ 4  +  1 __ 4  =  1 __ 2 

**Try It #4**
A card is drawn from a standard deck. Find the probability of drawing an ace or a king.

Using the Complement Rule to Compute Probabilities We have discussed how to calculate the probability that an event will happen. Sometimes, we are interested in finding the probability that an event will not happen. The complement of an event E, denoted E′, is the set of outcomes in the sample space that are not in E. For example, suppose we are interested in the probability that a horse will lose a race. If event W is the horse winning the race, then the complement of event W is the horse losing the race. To find the probability that the horse loses the race, we need to use the fact that the sum of all probabilities in a probability model must be 1.

P(E′) = 1 - P(E) The probability of the horse winning added to the probability of the horse losing must be equal to 1. Therefore, if the probability of the horse winning the race is  1 __ 9 , the probability of the horse losing the race is simply

1 -  1 __ 9  =  8 __ 9  the complement rule The probability that the complement of an event will occur is given by P(E′) = 1 - P(E)

**Example  5**
Using the Complement Rule to Calculate Probabilities Two six-sided number cubes are rolled. a. Find the probability that the sum of the numbers rolled is less than or equal to 3. b. Find the probability that the sum of the numbers rolled is greater than 3. Solution The first step is to identify the sample space, which consists of all the possible outcomes. There are two number cubes, and each number cube has six possible outcomes. Using the Multiplication Principle, we find that there are 6 \times  6, or 36 total possible outcomes. So, for example, 1-1 represents a 1 rolled on each number cube. a. We need to count the number of ways to roll a sum of 3 or less. These would include the following outcomes: 1-1, 1-2, and 2-1. So there are only three ways to roll a sum of 3 or less. The probability is

 3 ___ 36  =  1 ___ 12  b. Rather than listing all the possibilities, we can use the Complement Rule. Because we have already found the probability of the complement of this event, we can simply subtract that probability from 1 to find the probability that the sum of the numbers rolled is greater than 3.

P(E′) = 1 - P(E)

= 1 -  1 ___ 12 

=  11 ___ 12 

**Try It #5**
Two number cubes are rolled. Use the Complement Rule to find the probability that the sum is less than 10.


### Computing Probability Using Counting Theory
Many interesting probability problems involve counting principles, permutations, and combinations. In these problems, we will use permutations and combinations to find the number of elements in events and sample spaces. These problems can be complicated, but they can be made easier by breaking them down into smaller counting problems. Assume, for example, that a store has 8 cellular phones and that 3 of those are defective. We might want to find the probability that a couple purchasing 2 phones receives 2 phones that are not defective. To solve this problem, we need to calculate all of the ways to select 2 phones that are not defective as well as all of the ways to select 2 phones. There are 5 phones that are not defective, so there are C(5, 2) ways to select 2 phones that are not defective. There are 8 phones, so there are C(8, 2) ways to select 2 phones. The probability of selecting 2 phones that are not defective is:

 ways to select 2 phones that are not defective

____

ways to select 2 phones  =  C(5, 2) _ C(8, 2) 

=  10 ___ 28 

=  5 ___ 14 

**Example  6**

### Computing Probability Using Counting Theory
A child randomly selects 5 toys from a bin containing 3 bunnies, 5 dogs, and 6 bears. a. Find the probability that only bears are chosen. b. Find the probability that 2 bears and 3 dogs are chosen. c. Find the probability that at least 2 dogs are chosen.

**Solution**
a. We need to count the number of ways to choose only bears and the total number of possible ways to select 5 toys. There are 6 bears, so there are C(6, 5) ways to choose 5 bears. There are 14 toys, so there are C(14, 5) ways to choose any 5 toys.

 C(6, 5) _______ C(14, 5)  =  6 _____ _____ b. We need to count the number of ways to choose 2 bears and 3 dogs and the total number of possible ways to select 5 toys. There are 6 bears, so there are C(6, 2) ways to choose 2 bears. There are 5 dogs, so there are C(5, 3) ways to choose 3 dogs. Since we are choosing both bears and dogs at the same time, we will use the Multiplication Principle. There are C(6, 2) ⋅ C(5, 3) ways to choose 2 bears and 3 dogs. We can use this result to find the probability.

____________  =  15 ⋅ 10 ______ _____ c. It is often easiest to solve “at least” problems using the Complement Rule. We will begin by finding the probability that fewer than 2 dogs are chosen. If less than 2 dogs are chosen, then either no dogs could be chosen, or 1 dog could be chosen. When no dogs are chosen, all 5 toys come from the 9 toys that are not dogs. There are C(9, 5) ways to choose toys from the 9 toys that are not dogs. Since there are 14 toys, there are C(14, 5) ways to choose the 5 toys from all of the toys.

 C(9, 5) _______ _____ If there is 1 dog chosen, then 4 toys must come from the 9 toys that are not dogs, and 1 must come from the 5 dogs. Since we are choosing both dogs and other toys at the same time, we will use the Multiplication Principle. There are C(5, 1) ⋅ C(9, 4) ways to choose 1 dog and 1 other toy.

____________  =  5 ⋅ 126 ______ _____

Because these events would not occur together and are therefore mutually exclusive, we add the probabilities to find the probability that fewer than 2 dogs are chosen.

 63 _____ _____ _____ We then subtract that probability from 1 to find the probability that at least 2 dogs are chosen.

_____ _____

**Try It #6**
A child randomly selects 3 gumballs from a container holding 4 purple gumballs, 8 yellow gumballs, and 2 green gumballs. a. Find the probability that all 3 gumballs selected are purple. b. Find the probability that no yellow gumballs are selected. c. Find the probability that at least 1 yellow gumball is selected. Access these online resources for additional instruction and practice with probability. • Introduction to Probability (http://openstaxcollege.org/l/introprob) • Determining Probability (http://openstaxcollege.org/l/determineprob)


### 11.7 Section Exercises
Verbal 1. What term is used to express the likelihood of an event occurring? Are there restrictions on its values? If so, what are they? If not, explain. 2. What is a sample space? 3. What is an experiment? 4. What is the difference between events and outcomes? Give an example of both using the sample space of tossing a coin 50 times. 5. The union of two sets is defined as a set of elements that are present in at least one of the sets. How is this similar to the definition used for the union of two events from a probability model? How is it different? Numeric For the following exercises, use the spinner shown in Figure 3 to find the probabilities indicated. A B C D E F I O 6. Landing on red 7. Landing on a vowel 8. Not landing on blue 9. Landing on purple or a vowel 10. Landing on blue or a vowel 11. Landing on green or blue 12. Landing on yellow or a consonant 13. Not landing on yellow or a consonant For the following exercises, two coins are tossed. 14. What is the sample space? 15. Find the probability of tossing two heads. 16. Find the probability of tossing exactly one tail. 17. Find the probability of tossing at least one tail. For the following exercises, four coins are tossed. 18. What is the sample space? 19. Find the probability of tossing exactly two heads. 20. Find the probability of tossing exactly three heads. 21. Find the probability of tossing four heads or four tails. 22. Find the probability of tossing all tails. 23. Find the probability of tossing not all tails. 24. Find the probability of tossing exactly two heads or at least two tails. 25. Find the probability of tossing either two heads or three heads. For the following exercises, one card is drawn from a standard deck of 52 cards. Find the probability of drawing the following: 26. A club 27. A two 28. Six or seven 29. Red six 30. An ace or a diamond 31. A non-ace 32. A heart or a non-jack For the following exercises, two dice are rolled, and the results are summed. 33. Construct a table showing the sample space of outcomes and sums. 34. Find the probability of rolling a sum of 3.


## 11.7 Section Exercises
35. Find the probability of rolling at least one four or a sum of 8. 36. Find the probability of rolling an odd sum less than 9. 37. Find the probability of rolling a sum greater than or equal to 15. 38. Find the probability of rolling a sum less than 15. 39. Find the probability of rolling a sum less than 6 or greater than 9. 40. Find the probability of rolling a sum between 6 and 9, inclusive. 41. Find the probability of rolling a sum of 5 or 6. 42. Find the probability of rolling any sum other than 5 or 6. For the following exercises, a coin is tossed, and a card is pulled from a standard deck. Find the probability of the following: 43. A head on the coin or a club 44. A tail on the coin or red ace 45. A head on the coin or a face card 46. No aces For the following exercises, use this scenario: a bag of M&Ms contains 12 blue, 6 brown, 10 orange, 8 yellow, 8 red, and 4 green M&Ms. Reaching into the bag, a person grabs 5 M&Ms. 47. What is the probability of getting all blue M&Ms? 48. What is the probability of getting 4 blue M&Ms? 49. What is the probability of getting 3 blue M&Ms? 50. What is the probability of getting no brown M&Ms? Extensions Use the following scenario for the exercises that follow: In the game of Keno, a player starts by selecting 20 numbers from the numbers 1 to 80. After the player makes his selections, 20 winning numbers are randomly selected from numbers 1 to 80. A win occurs if the player has correctly selected 3, 4, or 5 of the 20 winning numbers. (Round all answers to the nearest hundredth of a percent.) 51. What is the percent chance that a player selects exactly 3 winning numbers? 52. What is the percent chance that a player selects exactly 4 winning numbers? 53. What is the percent chance that a player selects all 5 winning numbers? 54. What is the percent chance of winning? 55. How much less is a player’s chance of selecting 3 winning numbers than the chance of selecting either 4 or 5 winning numbers? Real-World Applications Use this data for the exercises that follow: In 2013, there were roughly 317 million citizens in the United States, and about 40 million were elderly (aged 65 and over).[35] 56. If you meet a U.S. citizen, what is the percent chance that the person is elderly? (Round to the nearest tenth of a percent.) 57. If you meet five U.S. citizens, what is the percent chance that exactly one is elderly? (Round to the nearest tenth of a percent.) 58. If you meet five U.S. citizens, what is the percent chance that three are elderly? (Round to the nearest tenth of a percent.) 59. If you meet five U.S. citizens, what is the percent chance that four are elderly? (Round to the nearest thousandth of a percent.) 60. It is predicted that by 2030, one in five U.S. citizens will be elderly. How much greater will the chances of meeting an elderly person be at that time? What policy changes do you foresee if these statistics hold true? 35 United States Census Bureau. http://www.census.gov


### Key Terms
Addition Principle if one event can occur in m ways and a second event with no common outcomes can occur in n ways, then the first or second event can occur in m + n ways annuity an investment in which the purchaser makes a sequence of periodic, equal payments arithmetic sequence a sequence in which the difference between any two consecutive terms is a constant arithmetic series the sum of the terms in an arithmetic sequence binomial coefficient the number of ways to choose r objects from n objects where order does not matter; equivalent to C(n, r), denoted   n _ r   binomial expansion the result of expanding (x + y)n by multiplying Binomial Theorem a formula that can be used to expand any binomial combination a selection of objects in which order does not matter common difference the difference between any two consecutive terms in an arithmetic sequence common ratio the ratio between any two consecutive terms in a geometric sequence complement of an event the set of outcomes in the sample space that are not in the event E diverge a series is said to diverge if the sum is not a real number event any subset of a sample space experiment an activity with an observable result explicit formula a formula that defines each term of a sequence in terms of its position in the sequence finite sequence a function whose domain consists of a finite subset of the positive integers {1, 2, ... n} for some positive integer n Fundamental Counting Principle if one event can occur in m ways and a second event can occur in n ways after the first event has occurred, then the two events can occur in m \times  n ways; also known as the Multiplication Principle geometric sequence a sequence in which the ratio of a term to a previous term is a constant geometric series the sum of the terms in a geometric sequence index of summation in summation notation, the variable used in the explicit formula for the terms of a series and written below the sigma with the lower limit of summation infinite sequence a function whose domain is the set of positive integers infinite series the sum of the terms in an infinite sequence lower limit of summation the number used in the explicit formula to find the first term in a series Multiplication Principle if one event can occur in m ways and a second event can occur in n ways after the first event has occurred, then the two events can occur in m \times  n ways; also known as the Fundamental Counting Principle mutually exclusive events events that have no outcomes in common n factorial the product of all the positive integers from 1 to n nth partial sum the sum of the first n terms of a sequence nth term of a sequence a formula for the general term of a sequence outcomes the possible results of an experiment permutation a selection of objects in which order matters probability a number from 0 to 1 indicating the likelihood of an event probability model a mathematical description of an experiment listing all possible outcomes and their associated probabilities

recursive formula a formula that defines each term of a sequence using previous term(s ) sample space the set of all possible outcomes of an experiment sequence a function whose domain is a subset of the positive integers series the sum of the terms in a sequence summation notation a notation for series using the Greek letter sigma; it includes an explicit formula and specifies the first and last terms in the series term a number in a sequence union of two events the event that occurs if either or both events occur upper limit of summation the number used in the explicit formula to find the last term in a series Key Equations

0! = 1 Formula for a factorial 1! = 1

n!= n(n - 1)(n - 2) ⋯ (2)(1), for n \ge  2 recursive formula for nth term of an arithmetic sequence an = an -1 + d; n \ge  2 explicit formula for nth term of an arithmetic sequence an = a^{1} + d(n - 1) recursive formula for nth term of a geometric sequence an = ran - 1, n \ge  2 explicit formula for nth term of a geometric sequence an = a^{1}r n -1 sum of the first n terms of an arithmetic series Sn =  n(a^{1}+ an) _  sum of the first n terms of a geometric series Sn =  a^{1}(1 - rn) _________ 1 - r , r \neq 1 sum of an infinite geometric series with -1 < r < 1 Sn =  a^{1} _ 1 - r , r \neq  1 number of permutations of n distinct objects taken r at a time P(n, r) =  n! _ (n - r)!  number of combinations of n distinct objects taken r at a time C(n, r) =  n! _ r!(n - r)!  number of permutations of n non-distinct objects  n! _ r^{1}!r^{2}! ... rk!  Binomial Theorem (x + y)n = ∑ k – 0 n    n _ k    x n - ky k (r + 1)th term of a binomial expansion   n _ r  xn - ryr probability of an event with equally likely outcomes P(E)=  n(E) ____ n(S)  probability of the union of two events P(E ∪ F) = P(E) + P(F) - P(E ∩ F) probability of the union of mutually exclusive events P(E ∪ F) = P(E) + P(F) probability of the complement of an event P(E') = 1 - P(E)


### Key Concepts
• A sequence is a list of numbers, called terms, written in a specific order. • Explicit formulas define each term of a sequence using the position of the term. See Example 1, Example 2, and

**Example 3** — .
• An explicit formula for the nth term of a sequence can be written by analyzing the pattern of several terms. See Example 4. • Recursive formulas define each term of a sequence using previous terms. • Recursive formulas must state the initial term, or terms, of a sequence. • A set of terms can be written by using a recursive formula. See Example 5 and Example 6. • A factorial is a mathematical operation that can be defined recursively. • The factorial of n is the product of all integers from 1 to n See Example 7. 11.2 Arithmetic Sequences • An arithmetic sequence is a sequence where the difference between any two consecutive terms is a constant. • The constant between two consecutive terms is called the common difference. • The common difference is the number added to any one term of an arithmetic sequence that generates the subsequent term. See Example 1. • The terms of an arithmetic sequence can be found by beginning with the initial term and adding the common difference repeatedly. See Example 2 and Example 3. • A recursive formula for an arithmetic sequence with common difference d is given by an = an - 1 + d, n \ge  2. See

**Example 4** — .
• As with any recursive formula, the initial term of the sequence must be given. • An explicit formula for an arithmetic sequence with common difference d is given by an = a^{1} + d(n - 1). See Example 5. • An explicit formula can be used to find the number of terms in a sequence. See Example 6. • In application problems, we sometimes alter the explicit formula slightly to an = a^{0} + dn. See Example 7. 11.3 Geometric Sequences • A geometric sequence is a sequence in which the ratio between any two consecutive terms is a constant. • The constant ratio between two consecutive terms is called the common ratio. • The common ratio can be found by dividing any term in the sequence by the previous term. See Example 1. • The terms of a geometric sequence can be found by beginning with the first term and multiplying by the common ratio repeatedly. See Example 2 and Example 4. • A recursive formula for a geometric sequence with common ratio r is given by an = ran - 1 for n \ge  2 . • As with any recursive formula, the initial term of the sequence must be given. See Example 3. • An explicit formula for a geometric sequence with common ratio r is given by an = a^{1}r n - 1. See Example 5. • In application problems, we sometimes alter the explicit formula slightly to an = a^{0}r n. See Example 6. 11.4 Series and Their Notations • The sum of the terms in a sequence is called a series. • A common notation for series is called summation notation, which uses the Greek letter sigma to represent the sum. See Example 1. • The sum of the terms in an arithmetic sequence is called an arithmetic series. • The sum of the first n terms of an arithmetic series can be found using a formula. See Example 2 and Example 3. • The sum of the terms in a geometric sequence is called a geometric series. • The sum of the first n terms of a geometric series can be found using a formula. See Example 4 and Example 5. • The sum of an infinite series exists if the series is geometric with -1 < r < 1.

• If the sum of an infinite series exists, it can be found using a formula. See Example 6, Example 7, and Example 8. • An annuity is an account into which the investor makes a series of regularly scheduled payments. The value of an annuity can be found using geometric series. See Example 9. 11.5 Counting Principles • If one event can occur in m ways and a second event with no common outcomes can occur in n ways, then the first or second event can occur in m + n ways. See Example 1. • If one event can occur in m ways and a second event can occur in n ways after the first event has occurred, then the two events can occur in m \times  n ways. See Example 2. • A permutation is an ordering of n objects. • If we have a set of n objects and we want to choose r objects from the set in order, we write P(n, r). • Permutation problems can be solved using the Multiplication Principle or the formula for P(n, r). See Example 3 and

**Example 4** — .
• A selection of objects where the order does not matter is a combination. • Given n distinct objects, the number of ways to select r objects from the set is C (n, r) and can be found using a formula. See Example 5. • A set containing n distinct objects has 2n subsets. See Example 6. • For counting problems involving non-distinct objects, we need to divide to avoid counting duplicate permutations. See Example 7. 11.6 Binomial Theorem •   n _ r   is called a binomial coefficient and is equal to C (n, r). See Example 1. • The Binomial Theorem allows us to expand binomials without multiplying. See Example 2. • We can find a given term of a binomial expansion without fully expanding the binomial. See Example 3. 11.7 Probability • Probability is always a number between 0 and 1, where 0 means an event is impossible and 1 means an event is certain. • The probabilities in a probability model must sum to 1. See Example 1. • When the outcomes of an experiment are all equally likely, we can find the probability of an event by dividing the number of outcomes in the event by the total number of outcomes in the sample space for the experiment. See

**Example 2** — .
• To find the probability of the union of two events, we add the probabilities of the two events and subtract the probability that both events occur simultaneously. See Example 3. • To find the probability of the union of two mutually exclusive events, we add the probabilities of each of the events. See Example 4. • The probability of the complement of an event is the difference between 1 and the probability that the event occurs. See Example 5. • In some probability problems, we need to use permutations and combinations to find the number of elements in events and sample spaces. See Example 6.

Sequences and Their Notation 1. Write the first four terms of the sequence defined by the recursive formula a^{1} = 2, an = an - 1 + n. 2. Evaluate  6! ________ (5 - 3)!3! . 3. Write the first four terms of the sequence defined by the explicit formula an = 10n + 3. 4. Write the first four terms of the sequence defined by the explicit formula an =  n! ________ n(n + 1).  Arithmetic Sequences 5. Is the sequence  4 _ _ _ _ 7 , ... arithmetic? If so, find the common difference. 6. Is the sequence 2, 4, 8, 16, ... arithmetic? If so, find the common difference. 7. An arithmetic sequence has the first term a^{1} = 18 and common difference d = -8. What are the first five terms? 8. An arithmetic sequence has terms a^{3} = 11.7 and a^{8} = -14.6. What is the first term? 9. Write a recursive formula for the arithmetic 10. Write a recursive formula for the arithmetic sequence _ _ 2 , ... , and then find the 31st term. 11. Write an explicit formula for the arithmetic sequence  7 _ _ _ _ 12. How many terms are in the finite arithmetic Geometric Sequences 13. Find the common ratio for the geometric sequence 14. Is the sequence 4, 16, 28, 40, ... geometric? If so find the common ratio. If not, explain why. 15. A geometric sequence has terms a^{7} = 16,384 and a^{9} = 262,144. What are the first five terms? 16. A geometric sequence has the first term a^{1} = -3 and common ratio r =  1 _ 2 . What is the 8th term? 17. What are the first five terms of the geometric sequence a^{1} = 3, an = 4 ⋅ an - 1? 18. Write a recursive formula for the geometric sequence 1,  1 _ _ _ 19. Write an explicit formula for the geometric sequence - 1 _ 5 , - 1 _ _ _ 20. How many terms are in the finite geometric sequence -5, - 5 _ 3 , - 5 _ ______ Series and Their Notation 21. Use summation notation to write the sum of terms  1 _ 2 m + 5 from m = 0 to m = 5. 22. Use summation notation to write the sum that results from adding the number 13 twenty times. 23. Use the formula for the sum of the first n terms of an arithmetic series to find the sum of the first eleven terms of the arithmetic series 2.5, 4, 5.5, ... . 24. A ladder has 15 tapered rungs, the lengths of which increase by a common difference. The first rung is 5 inches long, and the last rung is 20 inches long. What is the sum of the lengths of the rungs?

25. Use the formula for the sum of the first n terms of a geometric series to find S^{9} for the series 12, 6, 3,  3 26. The fees for the first three years of a hunting club membership are given in Table 1. If fees continue to rise at the same rate, how much will the total cost be for the first ten years of membership? Year Membership Fees $1500 $1950 $2535 27. Find the sum of the infinite geometric series  ∑ k -1  \infty   45 ⋅  - 1 __ 3    k = 1 . 28. A ball has a bounce-back ratio  3 _ 5  of the height of the previous bounce. Write a series representing the total distance traveled by the ball, assuming it was initially dropped from a height of 5 feet. What is the total distance? (Hint: the total distance the ball travels on each bounce is the sum of the heights of the rise and the fall.) 29. Alejandro deposits $80 of his monthly earnings into an annuity that earns 6.25% annual interest, compounded monthly. How much money will he have saved after 5 years? 30. The twins Sarah and Scott both opened retirement accounts on their 21st birthday. Sarah deposits $4,800.00 each year, earning 5.5% annual interest, compounded monthly. Scott deposits $3,600.00 each year, earning 8.5% annual interest, compounded monthly. Which twin will earn the most interest by the time they are 55 years old? How much more? Counting Principles 31. How many ways are there to choose a number divisible by either 4 or 6? 32. In a group of 20 musicians, 12 play piano, 7 play trumpet, and 2 play both piano and trumpet. How many musicians play either piano or trumpet? 33. How many ways are there to construct a 4-digit code if numbers can be repeated? 34. A palette of water color paints has 3 shades of green, 3 shades of blue, 2 shades of red, 2 shades of yellow, and 1 shade of black. How many ways are there to choose one shade of each color? 35. Calculate P(18, 4). 36. In a group of 5 freshman, 10 sophomores, 3 juniors, and 2 seniors, how many ways can a president, vice president, and treasurer be elected? 37. Calculate C(15, 6). 38. A coffee shop has 7 Guatemalan roasts, 4 Cuban roasts, and 10 Costa Rican roasts. How many ways can the shop choose 2 Guatemalan, 2 Cuban, and 3 Costa Rican roasts for a coffee tasting event? 39. How many subsets does the set {1, 3, 5, ... , 99} have? 40. A day spa charges a basic day rate that includes use of a sauna, pool, and showers. For an extra charge, guests can choose from the following additional services: massage, body scrub, manicure, pedicure, facial, and straight-razor shave. How many ways are there to order additional services at the day spa? 41. How many distinct ways can the word DEADWOOD be arranged? 42. How many distinct rearrangements of the letters of the word DEADWOOD are there if the arrangement must begin and end with the letter D?

Binomial Theorem 43. Evaluate the binomial coefficient   23 _ 8   . 44. Use the Binomial Theorem to expand  3x +  1 _ 2 y   6. 45. Use the Binomial Theorem to write the first three terms of (2a + b)^{1}7. 46. Find the fourth term of (3a 2 - 2b)^{1}1 without fully expanding the binomial. Probability For the following exercises, assume two die are rolled. 47. Construct a table showing the sample space. 48. What is the probability that a roll includes a 2? 49. What is the probability of rolling a pair? 50. What is the probability that a roll includes a 2 or results in a pair? 51. What is the probability that a roll doesn’t include a 2 or result in a pair? 52. What is the probability of rolling a 5 or a 6? 53. What is the probability that a roll includes neither a 5 nor a 6? For the following exercises, use the following data: An elementary school survey found that 350 of the 500 students preferred soda to milk. Suppose 8 children from the school are attending a birthday party. (Show calculations and round to the nearest tenth of a percent.) 54. What is the percent chance that all the children attending the party prefer soda? 55. What is the percent chance that at least one of the children attending the party prefers milk? 56. What is the percent chance that exactly 3 of the children attending the party prefer soda? 57. What is the percent chance that exactly 3 of the children attending the party prefer milk?

1. Write the first four terms of the sequence defined by the recursive formula a = -14, an =  2 + an – 1 ________  . 2. Write the first four terms of the sequence defined by the explicit formula an =  n^{2} - n - 1 ________ n! . 3. Is the sequence 0.3, 1.2, 2.1, 3, ... arithmetic? If so find the common difference. 4. An arithmetic sequence has the first term a^{1} = -4 and common difference d = - 4 _ 3 . What is the 6th term? 5. Write a recursive formula for the arithmetic sequence -2, -  7 _ _ 2  , ... and then find the 22nd term. 6. Write an explicit formula for the arithmetic sequence 7. Is the sequence - 2, - 1, -  1 _ 2 , -  1 _ 4 , ... geometric? If so find the common ratio. If not, explain why. 8. What is the 11th term of the geometric 9. Write a recursive formula for the geometric sequence 1, -  1 _ _ 4 , -  1 _ 10. Write an explicit formula for the geometric sequence _ _ 9 , -  4 _ 11. Use summation notation to write the sum of terms 3k 2 -  5 __ 6  k from k = -3 to k = 15. 12. A community baseball stadium has 10 seats in the first row, 13 seats in the second row, 16 seats in the third row, and so on. There are 56 rows in all. What is the seating capacity of the stadium? 13. Use the formula for the sum of the first n terms of a geometric series to find ∑ k = 1   -0.2 ⋅ (-5)k - 1. 14. Find the sum of the infinite geometric series.  ∑ k = 1  \infty    1 _ 3  ⋅  - 1 _ 5    k - 1 15. Rachael deposits $3,600 into a retirement fund each year. The fund earns 7.5% annual interest, compounded monthly. If she opened her account when she was 20 years old, how much will she have by the time she’s 55? How much of that amount was interest earned? 16. In a competition of 50 professional ballroom dancers, 22 compete in the fox-trot competition, 18 compete in the tango competition, and 6 compete in both the fox-trot and tango competitions. How many dancers compete in the foxtrot or tango competitions? 17. A buyer of a new sedan can custom order the car by choosing from 5 different exterior colors, 3 different interior colors, 2 sound systems, 3 motor designs, and either manual or automatic transmission. How many choices does the buyer have? 18. To allocate annual bonuses, a manager must choose his top four employees and rank them first to fourth. In how many ways can he create the “Top-Four” list out of the 32 employees? 19. A rock group needs to choose 3 songs to play at the annual Battle of the Bands. How many ways can they choose their set if have 15 songs to pick from? 20. A self-serve frozen yogurt shop has 8 candy toppings and 4 fruit toppings to choose from. How many ways are there to top a frozen yogurt? 21. How many distinct ways can the word EVANESCENCE be arranged if the anagram must end with the letter E? 22. Use the Binomial Theorem to expand   3 _ 2 x -  1 _ 2 y   5. 23. Find the seventh term of  x^{2} -  1 __ 2    without fully expanding the binomial.

For the following exercises, use the spinner in Figure 1. 24. Construct a probability model showing each possible outcome and its associated probability. (Use the first letter for colors.) 25. What is the probability of landing on an odd number? 26. What is the probability of landing on blue? 27. What is the probability of landing on blue or an odd number? 28. What is the probability of landing on anything other than blue or an odd number? 29. A bowl of candy holds 16 peppermint, 14 butterscotch, and 10 strawberry flavored candies. Suppose a person grabs a handful of 7 candies. What is the percent chance that exactly 3 are butterscotch? (Show calculations and round to the nearest tenth of a percent.)
