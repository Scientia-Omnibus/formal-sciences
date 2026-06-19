# Exponential and Logarithmic Functions

## Introduction
Focus in on a square centimeter of your skin. Look closer. Closer still. If you could look closely enough, you would see hundreds of thousands of microscopic organisms. They are bacteria, and they are not only on your skin, but in your mouth, nose, and even your intestines. In fact, the bacterial cells in your body at any given moment outnumber your own cells. But that is no reason to feel bad about yourself. While some bacteria can cause illness, many are healthy and even essential to the body. Bacteria commonly reproduce through a process called binary fission, during which one bacterial cell splits into two. When conditions are right, bacteria can reproduce very quickly. Unlike humans and other complex organisms, the time required to form a new generation of bacteria is often a matter of minutes or hours, as opposed to days or years.[16] For simplicity’s sake, suppose we begin with a culture of one bacterial cell that can divide every hour. Table 1 shows the number of bacterial cells at the end of each subsequent hour. We see that the single bacterial cell leads to over one thousand bacterial cells in just ten hours! And if we were to extrapolate the table to twenty-four hours, we would have over 16 million! Hour Bacteria In this chapter, we will explore exponential functions, which can be used for, among other things, modeling growth patterns such as those found in bacteria. We will also investigate logarithmic functions, which are closely related to exponential functions. Both types of functions have numerous real-world applications when it comes to modeling and interpreting data. 16. Todar, PhD, Kenneth. Todar’s Online Te xtbook of Bacteriology. http://te xtbookofbacteriology.net/growth_3.html. Exponential and ­Logarithmic Functions

Learning Objectives
In this section, you will:
• Evaluate exponential functions.
• Find the equation of an exponential function.
• Use compound interest formulas.
• Evaluate exponential functions with base e.

## 4.1 Exponential Functions
India is the second most populous country in the world with a population of about 1.25 billion people in 2013. The population is growing at a rate of about 1.2% each year[17]. If this rate continues, the population of India will e xceed China’s population by the year 2031. When populations grow rapidly, we often say that the growth is “exponential,” meaning that something is growing very rapidly. To a mathematician, however, the term exponential growth has a very specific meaning. In this section, we will take a look at exponential functions, which model this kind of rapid growth. Identifying Exponential Functions When exploring linear growth, we observed a constant rate of change—a constant number by which the output increased for each unit increase in input. For example, in the equation f (x) = 3x + 4, the slope tells us the output increases by 3 each time the input increases by 1. The scenario in the India population example is different because we have a percent change per unit time (rather than a constant change) in the number of people. Defining an Exponential Function A study found that the percent of the population who are vegans in the United States doubled from 2009 to 2011. In 2011, 2.5% of the population was vegan, adhering to a diet that does not include any animal products—no meat, poultry, fish, dairy, or eggs. If this rate continues, vegans will make up 10% of the U.S. population in 2015, 40% in 2019, and What exactly does it mean to grow exponentially? What does the word double have in common with percent increase? People toss these words around errantly. Are these words used correctly? The words certainly appear frequently in the media. • Percent change refers to a change based on a percent of the original amount. • Exponential growth refers to an increase based on a constant multiplicative rate of change over equal increments of time, that is, a percent increase of the original amount over time. • Exponential decay refers to a decrease based on a constant multiplicative rate of change over equal increments of time, that is, a percent decrease of the original amount over time. For us to gain a clear understanding of exponential growth, let us contrast exponential growth with linear growth. We will construct two functions. The first function is exponential. We will start with an input of 0, and increase each input by 1. We will double the corresponding consecutive outputs. The second function is linear. We will start with an input of 0, and increase each input by 1. We will add 2 to the corresponding consecutive outputs. See Table 1. x f (x) = 2x g(x) = 2x 17. http://www.worldometers.info/world-population/. Accessed February 24, 2014.

From Table 1 we can infer that for these two functions, exponential growth dwarfs linear growth. • Exponential growth refers to the original value from the range increases by the same percentage over equal increments found in the domain. • Linear growth refers to the original value from the range increases by the same amount over equal increments found in the domain. Apparently, the difference between “the same percentage” and “the same amount” is quite significant. For exponential growth, over equal increments, the constant multiplicative rate of change resulted in doubling the output whenever the input increased by one. For linear growth, the constant additive rate of change over equal increments resulted in adding 2 to the output whenever the input was increased by one. The general form of the exponential function is f (x) = ab x, where a is any nonzero number, b is a positive real number not equal to 1. • If b > 1, the function grows at a rate proportional to its size. • If 0 < b < 1, the function decays at a rate proportional to its size. Let’s look at the function f (x) = 2x from our example. We will create a table (Table 2) to determine the corresponding outputs over an interval in the domain from -3 to 3. x -3 -2 -1 f (x) = 2x 2-3 =  1 _ 8  2-2 =  1 _ 4  2-1 =  1 _ 2  Let us examine the graph of f by plotting the ordered pairs we observe on the table in Figure 1, and then make a few observations. f(x) = 2x y = 0 x y 2) Let’s define the behavior of the graph of the exponential function f (x) = 2x and highlight some its key characteristics. • the domain is (-\infty , \infty ), • the range is (0, \infty ), • as x → \infty , f (x) → \infty , • as x → -\infty , f (x) → 0, • f (x) is always increasing, • the graph of f (x) will never touch the x-axis because base two raised to any exponent never has the result of zero. • y = 0 is the horizontal asymptote. • the y-intercept is 1.

exponential function For any real number x, an exponential function is a function with the form f (x) = ab x where • a is the a non-zero real number called the initial value and • b is any positive real number such that b \neq  1. • The domain of f is all real numbers. • The range of f is all positive real numbers if a > 0. • The range of f is all negative real numbers if a < 0. • The y-intercept is (0, a), and the horizontal asymptote is y = 0.

**Example  1**

### Identifying Exponential Functions
Which of the following equations are not exponential functions? f (x) = 43(x - 2) g (x) = x^{3} h (x) =   1 _ 3   x j (x) = (-2)x

**Solution**
B y definition, an exponential function has a constant as a base and an independent variable as an exponent. Thus, g(x) = x^{3} does not represent an exponential function because the base is an independent variable. In fact, g(x) = x^{3} is a power function. Recall that the base b of an exponential function is always a positive constant, and b \neq  1. Thus, j(x) = (-2)x does not represent an exponential function because the base, -2, is less than 0.

**Try It #1**
Which of the following equations represent exponential functions? • f (x) = 2x^{2} - 3x + 1 • g(x) = 0.875x • h(x) = 1.75x + 2 Evaluating Exponential Functions Recall that the base of an exponential function must be a positive real number other than 1. Why do we limit the base b to positive values? To ensure that the outputs will be real numbers. Observe what happens if the base is not positive: • Let b = -9 and x =  1 _ 2 . Then f (x) = f   1 _ 2   = (-9)  1 __ 2  = \sqrt{-9} , which is not a real number. Why do we limit the base to positive values other than 1? Because base 1 results in the constant function. Observe what happens if the base is 1: • Let b = 1. Then f (x) = 1x = 1 for any value of x. To evaluate an exponential function with the form f (x) = b x, we simply substitute x with the given value, and calculate the resulting power. For example: Let f (x) = 2x. What is f (3)?

f (x) = 2x

f (3) = 23 Substitute x = 3.

= 8 Evaluate the power. To evaluate an exponential function with a form other than the basic form, it is important to follow the order of operations.

For example: Let f (x) = 30(2)x. What is f (3)?

f (x) = 30(2)x

Substitute x = 3.

Simplify the power first.

= 240 Multiply. Note that if the order of operations were not followed, the result would be incorrect:

**Example  2**

### Evaluating Exponential Functions
Let f (x) = 5(3)x + 1. Evaluate f (2) without using a calculator. Solution Follow the order of operations. Be sure to pay attention to the parentheses.

f (x) = 5(3)x + 1

f (2) = 5(3)^{2} + 1 Substitute x = 2.

Add the exponents.

Simplify the power.

= 135 Multiply.

**Try It #2**
Let f (x) = 8(1.2)x - 5. Evaluate f (3) using a calculator. Round to four decimal places. Defining Exponential Growth Because the output of exponential functions increases very rapidly, the term “exponential growth” is often used in everyday language to describe anything that grows or increases rapidly. However, exponential growth can be defined more precisely in a mathematical sense. If the growth rate is proportional to the amount present, the function models exponential growth. exponential growth A function that models exponential growth grows by a rate proportional to the amount present. For any real number x and any positive real numbers a and b such that b \neq  1, an exponential growth function has the form f (x) = ab x where • a is the initial or starting value of the function. • b is the growth factor or growth multiplier per unit x. In more general terms, we have an exponential function, in which a constant base is raised to a variable exponent. To differentiate between linear and exponential functions, let’s consider two companies, A and B. Company A has 100 stores and expands by opening 50 new stores a year, so its growth can be represented by the function A(x) = 100 + 50x. Company B has 100 stores and expands by increasing the number of stores by 50% each year, so its growth can be represented by the function B(x) = 100(1 + 0.5)x. A few years of growth for these companies are illustrated in Table 3. Year, x Stores, Company A Stores, Company B x A(x) = 100 + 50x B(x) = 100(1 + 0.5)x

The graphs comparing the number of stores for each company over a five-year period are shown in Figure 2. We can see that, with exponential growth, the number of stores increases much more rapidly than with linear growth. Years Number of Stores x y B(x) = 100(1 + 0.5)x A(x) = 100 + 50x Notice that the domain for both functions is [0, \infty ), and the range for both functions is [100, \infty ). After year 1, Company B always has more stores than Company A. Now we will turn our attention to the function representing the number of stores for Company B, B(x) = 100(1 + 0.5)x. In this exponential function, 100 represents the initial number of stores, 0.50 represents the growth rate, and 1 + 0.5 = 1.5 represents the growth factor. Generalizing further, we can write this function as B(x) = 100(1.5)x, where 100 is the initial value, 1.5 is called the base, and x is called the exponent.

**Example  3**

### Evaluating a Real-World Exponential Model
At the beginning of this section, we learned that the population of India was about 1.25 billion in the year 2013, with an annual growth rate of about 1.2%. This situation is represented by the growth function P(t) = 1.25(1.012)t, where t is the number of years since 2013. To the nearest thousandth, what will the population of India be in 2031?

**Solution**
To estimate the population in 2031, we evaluate the models for t = 18, because 2031 is 18 years after 2013. Rounding to the nearest thousandth, There will be about 1.549 billion people in India in the year 2031.

**Try It #3**
The population of China was about 1.39 billion in the year 2013, with an annual growth rate of about 0.6%. This situation is represented by the growth function P(t) = 1.39(1.006)t, where t is the number of years since 2013. To the nearest thousandth, what will the population of China be for the year 2031? How does this compare to the population prediction we made for India in Example 3? Finding Equations of Exponential Functions In the previous examples, we were given an exponential function, which we then evaluated for a given input. Sometimes we are given information about an exponential function without knowing the function explicitly. We must use the information to first write the form of the function, then determine the constants a and b, and evaluate the function.

**How To…**
Given two data points, write an exponential model. 1. If one of the data points has the form (0, a), then a is the initial value. Using a, substitute the second point into the equation f (x) = a(b)x, and solve for b. 2. If neither of the data points have the form (0, a), substitute both points into two equations with the form f (x) = a(b)x. Solve the resulting system of two equations in two unknowns to find a and b. 3. Using the a and b found in the steps above, write the exponential function in the form f (x) = a(b)x.


**Example  4**

### Writing an Exponential Model When the Initial Value Is Known
In 2006, 80 deer were introduced into a wildlife refuge. By 2012, the population had grown to 180 deer. The population was growing exponentially. Write an algebraic function N(t) representing the population (N) of deer over time t. Solution We let our independent variable t be the number of years after 2006. Thus, the information given in the problem can be written as input-output pairs: (0, 80) and (6, 180). Notice that by choosing our input variable to be measured as years after 2006, we have given ourselves the initial value for the function, a = 80. We can now substitute the second point into the equation N(t) = 80bt to find b:

N(t) = 80b t

Substitute using point (6, 180).

 9 __ 4  = b 6 Divide and write in lowest terms.

b =   9 __ 4    1 __ 6  Isolate b using properties of exponents.

Round to 4 decimal places. NOTE: Unless otherwise stated, do not round any intermediate calculations. Then round the final answer to four places for the remainder of this section. The exponential model for the population of deer is N(t) = 80(1.1447)t. (Note that this exponential function models short-term growth. As the inputs gets large, the output will get increasingly larger, so much so that the model may not be useful in the long term.) We can graph our model to observe the population growth of deer in the refuge over time. Notice that the graph in for the function is [0, \infty ), and the range for the function is [80, \infty ). Years Deer Population t N(t)

**Try It #4**
A wolf population is growing exponentially. In 2011, 129 wolves were counted. By 2013, the population had reached 236 wolves. What two points can be used to derive an exponential equation modeling this situation? Write the equation representing the population N of wolves over time t.

**Example  5**

### Writing an Exponential Model When the Initial Value is Not Known
Find an exponential function that passes through the points (-2, 6) and (2, 1). Solution Because we don’t have the initial value, we substitute both points into an equation of the form f (x) = ab x, and then solve the system for a and b. • Substituting (-2, 6) gives 6 = ab-2 • Substituting (2, 1) gives 1 = ab^{2}

Use the first equation to solve for a in terms of b:

6 = ab-2

 6 _ b-2  = a Divide.

a = 6b 2 Use properties of exponents to rewrite the denominator. Substitute a in the second equation, and solve for b:

1 = ab 2

1 = 6b 2b 2 = 6b 4 Substitute a.

b =   1 _ 6    1 __ 4  Use properties of exponents to isolate b.

Round 4 decimal places. Use the value of b in the first equation to solve for the value of a:

Thus, the equation is f (x) = 2.4492(0.6389)x. We can graph our model to check our work. Notice that the graph in Figure 4 passes through the initial points given in the problem, (-2, 6) and (2, 1). The graph is an example of an exponential decay function. x f(x)

**Try It #5**
Given the two points (1, 3) and (2, 4.5), find the equation of the exponential function that passes through these two points. Do two points always determine a unique exponential function? Yes, provided the two points are either both above the x-axis or both below the x-axis and have different x-coordinates. But keep in mind that we also need to know that the graph is, in fact, an exponential function. Not every graph that looks exponential really is exponential. We need to know the graph is based on a model that shows the same percent growth with each unit increase in x, which in many real world cases involves time.

**How To…**
Given the graph of an exponential function, write its equation. 1. First, identify two points on the graph. Choose the y-intercept as one of the two points whenever possible. Try to choose points that are as far apart as possible to reduce round-off error. 2. If one of the data points is the y-intercept (0, a), then a is the initial value. Using a, substitute the second point into the equation f (x) = a(b)x, and solve for b. 3. If neither of the data points have the form (0, a), substitute both points into two equations with the form f (x) = a(b)x. Solve the resulting system of two equations in two unknowns to find a and b. 4. Write the exponential function, f (x) = a(b)x.


**Example  6**

### Writing an Exponential Function Given Its Graph
Find an equation for the exponential function graphed in Figure 5. x f(x) 0.5 1.5 2.5 3.5 Solution We can choose the y-intercept of the graph, (0, 3), as our first point. This gives us the initial value, a = 3. Next, choose a point on the curve some distance away from (0, 3) that has integer coordinates. One such point is (2, 12).

y = ab x Write the general form of an exponential equation.

y = 3b x Substitute the initial value 3 for a.

Substitute in 12 for y and 2 for x.

4 = b^{2} Divide by 3.

b = \pm 2 Take the square root. Because we restrict ourselves to positive values of b, we will use b = 2. Substitute a and b into the standard form to yield the equation f (x) = 3(2)x.

**Try It #6**
Find an equation for the exponential function graphed in Figure 6. x f(x)

**How To…**
Given two points on the curve of an exponential function, use a graphing calculator to find the equation. 1. Press [STAT]. 2. Clear any existing entries in columns L^{1} or L^{2}. 3. In L^{1}, enter the x-coordinates given. 4. In L^{2}, enter the corresponding y-coordinates. 5. Press [STAT] again. Cursor right to CALC, scroll down to ExpReg (Exponential Regression), and press [ENTER]. 6. The screen displays the values of a and b in the exponential equation y = a ⋅ b x

**Example  7**
Using a Graphing Calculator to Find an Exponential Function Use a graphing calculator to find the exponential equation that includes the points (2, 24.8) and (5, 198.4). Solution Follow the guidelines above. First press [STAT], [EDIT], [1: Edit...], and clear the lists L^{1} and L^{2}. Next, in the L^{1} column, enter the x-coordinates, 2 and 5. Do the same in the L^{2} column for the y-coordinates, 24.8 and 198.4. Now press [STAT], [CALC], [0: ExpReg] and press [ENTER]. The values a = 6.2 and b = 2 will be displayed. The exponential equation is y = 6.2 ⋅ 2x.

**Try It #7**
Use a graphing calculator to find the exponential equation that includes the points (3, 75.98) and (6, 481.07).


### Applying the Compound-Interest Formula
Savings instruments in which earnings are continually reinvested, such as mutual funds and retirement accounts, use compound interest. The term compounding refers to interest earned not only on the original value, but on the accumulated value of the account. The annual percentage rate (APR) of an account, also called the nominal rate, is the yearly interest rate earned by an investment account. The term nominal is used when the compounding occurs a number of times other than once per year. In fact, when interest is compounded more than once a year, the effective interest rate ends up being greater than the nominal rate! This is a powerful tool for investing. We can calculate the compound interest using the compound interest formula, which is an exponential function of the variables time t, principal P, APR r, and number of compounding periods in a year n: A(t) = P  1 +  r _ n   nt For example, observe Table 4, which shows the result of investing $1,000 at 10% for one year. Notice how the value of the account increases as the compounding frequency increases. Frequency Value after 1 year Annually $1100 Semiannually Quarterly Monthly Daily the compound interest formula Compound interest can be calculated using the formula A(t) = P  1 +  r _ n   nt where • A(t) is the account value, • t is measured in years, • P is the starting amount of the account, often called the principal, or more generally present value, • r is the annual percentage rate (APR) expressed as a decimal, and • n is the number of compounding periods in one year.

**Example  8**

### Calculating Compound Interest
If we invest $3,000 in an investment account paying 3% interest compounded quarterly, how much will the account be worth in 10 years? Solution Because we are starting with $3,000, P = 3000. Our interest rate is 3%, so r = 0.03. Because we are compounding quarterly, we are compounding 4 times per year, so n = 4. We want to know the value of the account in 10 years, so we are looking for A(10), the value when t = 10.

A(t) = P  1 +  r _ n   nt

Use the compound interest formula.

____ 4   Substitute using given values.

Round to two decimal places. The account will be worth about $4,045.05 in 10 years.

**Try It #8**
An initial investment of $100,000 at 12% interest is compounded weekly (use 52 weeks in a year). What will the investment be worth in 30 years?


**Example  9**
Using the Compound Interest Formula to Solve for the Principal A 529 Plan is a college-savings plan that allows relatives to invest money to pay for a child’s future college tuition; the account grows tax-free. Lily wants to set up a 529 account for her new granddaughter and wants the account to grow to $40,000 over 18 years. She believes the account will earn 6% compounded semi-annually (twice a year). To the nearest dollar, how much will Lily need to invest in the account now? Solution The nominal interest rate is 6%, so r = 0.06. Interest is compounded twice a year, so n = 2. We want to find the initial investment, P, needed so that the value of the account will be worth $40,000 in 18 years. Substitute the given values into the compound interest formula, and solve for P.

A(t) = P  1 +  r _ n   nt Use the compound interest formula.

____ 2   2(18)

Substitute using given values A, r, n, and t.

Simplify.

______

Isolate P.

Divide and round to the nearest dollar. Lily will need to invest $13,801 to have $40,000 in 18 years.

**Try It #9**
Refer to Example 9. To the nearest dollar, how much would Lily need to invest if the account is compounded quarterly? Evaluating Functions with Base e As we saw earlier, the amount earned on an account increases as the compounding frequency increases. Table 5 shows that the increase from annual to semi-annual compounding is larger than the increase from monthly to daily compounding. This might lead us to ask whether this pattern will continue. Examine the value of $1 invested at 100% interest for 1 year, compounded at various frequencies, listed in Table 5. Frequency A(t) =  1 +  1 _ n   n Value Annually  1 +  1 _ 1   $2 Semiannually  1 +  1 _ 2   $2.25 Quarterly  1 +  1 _ 4   Monthly  1 +  1 _ 12   Daily  1 +  1 _ Hourly  1 +  1 _ Once per minute  1 +  _ Once per second  1 +  ________

These values appear to be approaching a limit as n increases without bound. In fact, as n gets larger and larger, the expression  1 +  1 _ n   n approaches a number used so frequently in mathematics that it has its own name: the letter e. This value is an irrational number, which means that its decimal expansion goes on forever without repeating. Its approximation to six decimal places is shown below. the number e The letter e represents the irrational number  1 +  1 __ n   n , as n increases without bound The letter e is used as a base for many real-world exponential models. To work with base e, we use the approximation, e ≈ 2.718282. The constant was named by the Swiss mathematician Leonhard Euler (1707–1783) who first investigated and discovered many of its properties.

**Example  10**
Using a Calculator to Find Powers of e Calculate e^{3}.14. Round to five decimal places. Solution On a calculator, press the button labeled [e x]. The window shows [e^(]. Type 3.14 and then close parenthesis, [)]. Press [ENTER]. Rounding to 5 decimal places, e 3.14 ≈ 23.10387. Caution: Many scientific calculators have an “Exp” button, which is used to enter numbers in scientific notation. It is not used to find powers of e.

**Try It #10**
Use a calculator to find e -0.5. Round to five decimal places. Investigating Continuous Growth So far we have worked with rational bases for exponential functions. For most real-world phenomena, however, e is used as the base for exponential functions. Exponential models that use e as the base are called continuous growth or decay models. We see these models in finance, computer science, and most of the sciences, such as physics, toxicology, and fluid dynamics. the continuous growth/decay formula For all real numbers t, and all positive numbers a and r, continuous growth or decay is represented by the formula A(t) = aert where • a is the initial value, • r is the continuous growth rate per unit time, • and t is the elapsed time. If r > 0, then the formula represents continuous growth. If r < 0, then the formula represents continuous decay. For business applications, the continuous growth formula is called the continuous compounding formula and takes the form A(t) = Pert where • P is the principal or the initial invested, • r is the growth or interest rate per unit time, • and t is the period or term of the investment.


**How To…**
Given the initial value, rate of growth or decay, and time t, solve a continuous growth or decay function. 1. Use the information in the problem to determine a, the initial value of the function. 2. Use the information in the problem to determine the growth rate r. a. If the problem refers to continuous growth, then r > 0. b. If the problem refers to continuous decay, then r < 0. 3. Use the information in the problem to determine the time t. 4. Substitute the given information into the continuous growth formula and solve for A(t).

**Example  11**

### Calculating Continuous Growth
A person invested $1,000 in an account earning a nominal 10% per year compounded continuously. How much was in the account at the end of one year? Solution Since the account is growing in value, this is a continuous compounding problem with growth rate r = 0.10. The initial investment was $1,000, so P = 1000. We use the continuous compounding formula to find the value after t = 1 year:

A(t) = Pert Use the continuous compounding formula.

Substitute known values for P, r, and t.

Use a calculator to approximate. The account is worth $1,105.17 after one year.

**Try It #11**
A person invests $100,000 at a nominal 12% interest per year compounded continuously. What will be the value of the investment in 30 years?

**Example  12**

### Calculating Continuous Decay
Radon-222 decays at a continuous rate of 17.3% per day. How much will 100 mg of Radon-222 decay to in 3 days? Solution Since the substance is decaying, the rate, 17.3%, is negative. So, r = -0.173. The initial amount of radon- 222 was 100 mg, so a = 100. We use the continuous decay formula to find the value after t = 3 days:

A(t) = aert Use the continuous growth formula.

Substitute known values for a, r, and t.

Use a calculator to approximate. So 59.5115 mg of radon-222 will remain.

**Try It #12**
Using the data in Example 12, how much radon-222 will remain after one year? Access these online resources for additional instruction and practice with exponential functions. • Exponential Growth Function (http://openstaxcollege.org/l/expgrowth) • Compound Interest (http://openstaxcollege.org/l/compoundint)


### 4.1 section EXERCISES
Verbal 1. Explain why the values of an increasing exponential function will eventually overtake the values of an increasing linear function. 2. Given a formula for an exponential function, is it possible to determine whether the function grows or decays exponentially just by looking at the formula? Explain. 3. The Oxford Dictionary defines the word nominal as a value that is “stated or expressed but not necessarily corresponding exactly to the real value.”[18] Develop a reasonable argument for why the term nominal rate is used to describe the annual percentage rate of an investment account that compounds interest. Algebraic For the following exercises, identify whether the statement represents an exponential function. Explain. 4. The average annual population increase of a pack of wolves is 25. 5. A population of bacteria decreases by a factor of  1 __ 8  every 24 hours. 6. The value of a coin collection has increased by 3.25% annually over the last 20 years. 7. For each training session, a personal trainer charges his clients $5 less than the previous training session. 8. The height of a projectile at time t is represented by the function h(t) = -4.9t 2 + 18t + 40. For the following exercises, consider this scenario: For each year t, the population of a forest of trees is represented by the function A(t) = 115(1.025)t. In a neighboring forest, the population of the same type of tree is represented by the function B(t) = 82(1.029)t. (Round answers to the nearest whole number.) 9. Which forest’s population is growing at a faster rate? 10. Which forest had a greater number of trees initially? By how many? 11. Assuming the population growth models continue to represent the growth of the forests, which forest will have a greater number of trees after 20 years? By how many? 12. Assuming the population growth models continue to represent the growth of the forests, which forest will have a greater number of trees after 100 years? By how many? 13. Discuss the above results from the previous four exercises. Assuming the population growth models continue to represent the growth of the forests, which forest will have the greater number of trees in the long run? Why? What are some factors that might influence the long-term validity of the exponential growth model? For the following exercises, determine whether the equation represents exponential growth, exponential decay, or neither. Explain. _ x  For the following exercises, find the formula for an exponential function that passes through the two points given. _ 2   and (3, 24) 18. Oxford Dictionary. http://oxforddictionaries.com/us/definition/american_english/nominal.


## 4.1 Section Exercises
For the following exercises, determine whether the table could represent a function that is linear, exponential, or neither. If it appears to be exponential, find a function that passes through the points. x f (x) -20

x h(x) 34.3 24.01

x m (x) 42.9 25.61

x f (x)

x g (x) -3.25 7.25 12.5 For the following exercises, use the compound interest formula, A(t) = P  1 +  r _ n   nt. 28. After a certain number of years, the value of an investment account is represented by the equation ____ 12   120. What is the value of the account? 29. What was the initial deposit made to the account in the previous exercise? 30. How many years had the account from the previous exercise been accumulating interest? 31. An account is opened with an initial deposit of $6,500 and earns 3.6% interest compounded semi-annually. What will the account be worth in 20 years? 32. How much more would the account in the previous exercise have been worth if the interest were compounding weekly? 33. Solve the compound interest formula for the principal, P. 34. Use the formula found in Exercise #31 to calculate the initial deposit of an account that is worth $14,472.74 after earning 5.5% interest compounded monthly for 5 years. (Round to the nearest dollar.) 35. How much more would the account in Exercises #31 and #34 be worth if it were earning interest for 5 more years? 36. Use properties of rational exponents to solve the compound interest formula for the interest rate, r. 37. Use the formula found in the previous exercise to calculate the interest rate for an account that was compounded semi-annually, had an initial deposit of $9,000 and was worth $13,373.53 after 10 years. 38. Use the formula found in the previous exercise to calculate the interest rate for an account that was compounded monthly, had an initial deposit of $5,500, and was worth $38,455 after 30 years. For the following exercises, determine whether the equation represents continuous growth, continuous decay, or neither. Explain. _ t  42. Suppose an investment account is opened with an initial deposit of $12,000 earning 7.2% interest compounded continuously. How much will the account be worth after 30 years? 43. How much less would the account from Exercise 42 be worth after 30 years if it were compounded monthly instead? Numeric For the following exercises, evaluate each function. Round answers to four decimal places, if necessary. 44. f (x) = 2(5)x, for f (-3) 45. f (x) = -42x + 3, for f (-1) 46. f (x) = e x, for f (3) 47. f (x) = -2e x - 1, for f (-1) 48. f (x) = 2.7(4)-x + 1 + 1.5, for f (-2) 49. f (x) = 1.2e^{2}x - 0.3, for f (3) 50. f (x) = - 3 _ 2 (3)-x +  3 _ 2 , for f (2)

Technology For the following exercises, use a graphing calculator to find the equation of an exponential function given the points on the curve. Extensions 56. The annual percentage yield (APY) of an investment account is a representation of the actual interest rate earned on a compounding account. It is based on a compounding period of one year. Show that the APY of an account that compounds monthly can be found with the formula APY =  1 +  r __ 12   57. Repeat the previous exercise to find the formula for the APY of an account that compounds daily. Use the results from this and the previous exercise to develop a function I(n) for the APY of any account that compounds n times per year. 58. Recall that an exponential function is any equation written in the form f (x) = a . b x such that a and b are positive numbers and b \neq  1. Any positive number b can be written as b = en for some value of n. Use this fact to rewrite the formula for an exponential function that uses the number e as a base. 59. In an exponential decay function, the base of the exponent is a value between 0 and 1. Thus, for some number b > 1, the exponential decay function can be written as f (x) = a .   1 _ b   x . Use this formula, along with the fact that b = e n, to show that an exponential decay function takes the form f (x) = a(e)-nx for some positive number n. 60. The formula for the amount A in an investment account with a nominal interest rate r at any time t is given by A(t) = a(e)rt, where a is the amount of principal initially deposited into an account that compounds continuously. Prove that the percentage of interest earned to principal at any time t can be calculated with the formula I(t) = e rt - 1. Real-World Applications 61. The fox population in a certain region has an annual growth rate of 9% per year. In the year 2012, there were 23,900 fox counted in the area. What is the fox population predicted to be in the year 2020? 62. A scientist begins with 100 milligrams of a radioactive substance that decays exponentially. After 35 hours, 50 mg of the substance remains. How many milligrams will remain after 54 hours? 63. In the year 1985, a house was valued at $110,000. By the year 2005, the value had appreciated to $145,000. What was the annual growth rate between 1985 and 2005? Assume that the value continued to grow by the same percentage. What was the value of the house in the year 2010? 64. A car was valued at $38,000 in the year 2007. By 2013, the value had depreciated to $11,000 If the car’s value continues to drop by the same percentage, what will it be worth by 2017? 65. Jamal wants to save $54,000 for a down payment on a home. How much will he need to invest in an account with 8.2% APR, compounding daily, in order to reach his goal in 5 years? 66. Kyoko has $10,000 that she wants to invest. Her bank has several investment accounts to choose from, all compounding daily. Her goal is to have $15,000 by the time she finishes graduate school in 6 years. To the nearest hundredth of a percent, what should her minimum annual interest rate be in order to reach her goal? (Hint : solve the compound interest formula for the interest rate.) 67. Alyssa opened a retirement account with 7.25% APR in the year 2000. Her initial deposit was $13,500. How much will the account be worth in 2025 if interest compounds monthly? How much more would she make if interest compounded continuously? 68. An investment account with an annual interest rate of 7% was opened with an initial deposit of $4,000 Compare the values of the account after 9 years when the interest is compounded annually, quarterly, monthly, and continuously.


## 4.2 Graphs of Exponential Functions
Learning Objectives
In this section, you will:
• Graph exponential functions.
• Graph exponential functions using transformations.
As we discussed in the previous section, exponential functions are used for many real-world applications such as finance, forensics, computer science, and most of the life sciences. Working with an equation that describes a real- world situation gives us a method for making predictions. Most of the time, however, the equation itself is not enough. We learn a lot about things by seeing their pictorial representations, and that is exactly why graphing exponential equations is a powerful tool. It gives us another layer of insight for predicting future events. Graphing Exponential Functions Before we begin graphing, it is helpful to review the behavior of exponential growth. Recall the table of values for a function of the form f (x) = b x whose base is greater than one. We’ll use the function f (x) = 2x. Observe how the output values in Table 1 change as the input increases by 1. x -3 -2 -1 f (x) = 2x  1 _ 8   1 _ 4   1 _ 2  Each output value is the product of the previous output and the base, 2. We call the base 2 the constant ratio. In fact, for any exponential function with the form f (x) = ab x, b is the constant ratio of the function. This means that as the input increases by 1, the output value will be the product of the base and the previous output, regardless of the value of a. Notice from the table that • the output values are positive for all values of x; • as x increases, the output values increase without bound; and • as x decreases, the output values grow smaller, approaching zero. Te x-axis is an asymptote. f (x) = 2x -3, -2, -1, x f(x) The domain of f (x) = 2x is all real numbers, the range is (0, \infty ), and the horizontal asymptote is y = 0. To get a sense of the behavior of exponential decay, we can create a table of values for a function of the form f (x) = b x whose base is between zero and one. We’ll use the function g(x) =   1 _ 2   x . Observe how the output values in Table 2 change as the input increases by 1.

x -3 -2 -1 g(x) =   1 __ 2   x  1 _ 2   1 _ 4   1 _ 8  Again, because the input is increasing by 1, each output value is the product of the previous output and the base, or constant ratio  1 _ 2 . Notice from the table that • the output values are positive for all values of x; • as x increases, the output values grow smaller, approaching zero; and • as x decreases, the output values grow without bound. _ 2   x . g(x) = 1 x Te x-axis is an asymptote. x g(x) The domain of g(x) =   1 _ 2   x  is all real numbers, the range is (0, \infty ), and the horizontal asymptote is y = 0. characteristics of the graph of the parent function f (x) = b x An exponential function with the form f (x) = b x, b > 0, b \neq  1, has these characteristics: • one-to-one function • horizontal asymptote: y = 0 • domain: (–\infty , \infty ) • range: (0, \infty ) • x-intercept: none • y-intercept: (0, 1) • increasing if b > 1 • decreasing if b < 1 growth and decay functions. (1, b) (1, b) x x f(x) f (x) = bx b > 1 f (x) = bx 0 < b < 1 f(x)

**How To…**
Given an exponential function of the form f (x) = b x, graph the function. 1. Create a table of points. 2. Plot at least 3 point from the table, including the y-intercept (0, 1). 3. Draw a smooth curve through the points. 4. State the domain, (-\infty , \infty ), the range, (0, \infty ), and the horizontal asymptote, y = 0.


**Example  1**

### Sketching the Graph of an Exponential Function of the Form f (x) = b x
Sketch a graph of f (x) = 0.25x. State the domain, range, and asymptote. Solution Before graphing, identify the behavior and create a table of points for the graph. • Since b = 0.25 is between zero and one, we know the function is decreasing. The left tail of the graph will increase without bound, and the right tail will approach the asymptote y = 0. • Create a table of points as in Table 3. x -3 -2 -1 f (x) = 0.25x 0.25 • Plot the y-intercept, (0, 1), along with two other points. We can use (-1, 4) and (1, 0.25). Draw a smooth curve connecting the points as in Figure 4. f(x) = 0.25x x f(x) The domain is (-\infty , \infty ); the range is (0, \infty ); the horizontal asymptote is y = 0.

**Try It #1**
Sketch the graph of f (x) = 4x. State the domain, range, and asymptote. Graphing Transformations of Exponential Functions Transformations of exponential graphs behave similarly to those of other functions. Just as with other parent functions, we can apply the four types of transformations—shifts, reflections, stretches, and compressions—to the parent function f (x) = b x without loss of shape. For instance, just as the quadratic function maintains its parabolic shape when shifted, reflected, stretched, or compressed, the exponential function also maintains its general shape regardless of the transformations applied. Graphing a Vertical Shift The first transformation occurs when we add a constant d to the parent function f (x) = b x, giving us a vertical shift d units in the same direction as the sign. For example, if we begin by graphing a parent function, f (x) = 2x, we can then graph two vertical shifts alongside it, using d = 3: the upward shift, g(x) = 2x + 3 and the downward shift, h(x) = 2x - 3. Both vertical shifts are shown in Figure 5. g(x) = 2x + 3 f (x) = 2x h(x) = 2x - 3 y = 3 y = -3 y = 0 x y

Observe the results of shifting f (x) = 2x vertically: • The domain, (-\infty , \infty ) remains unchanged. • When the function is shifted up 3 units to g(x) = 2x + 3: ◦ ◦The y-intercept shifts up 3 units to (0, 4). ◦ ◦The asymptote shifts up 3 units to y = 3. ◦ ◦The range becomes (3, \infty ). • When the function is shifted down 3 units to h(x) = 2x - 3: ◦ ◦The y-intercept shifts down 3 units to (0, -2). ◦ ◦The asymptote also shifts down 3 units to y = -3. ◦ ◦The range becomes (-3, \infty ). Graphing a Horizontal Shift The next transformation occurs when we add a constant c to the input of the parent function f (x) = b x, giving us a horizontal shift c units in the opposite direction of the sign. For example, if we begin by graphing the parent function f (x) = 2x, we can then graph two horizontal shifts alongside it, using c = 3: the shift left, g(x) = 2x + 3, and the shift right, h (x) = 2x - 3. Both horizontal shifts are shown in Figure 6. x y g(x) = 2x + 3 f (x) = 2x h(x) = 2x - 3 y = 0 Observe the results of shifting f (x) = 2x horizontally: • The domain, (-\infty , \infty ), remains unchanged. • The asymptote, y = 0, remains unchanged. • The y-intercept shifts such that: ◦ ◦When the function is shifted left 3 units to g(x) = 2x + 3, the y-intercept becomes (0, 8). This is because 2x + 3 = (8)^{2}x, so the initial value of the function is 8. ◦ ◦When the function is shifted right 3 units to h(x) = 2x - 3, the y-intercept becomes  0,  1 _ 8  . Again, see that 2x - 3 =   1 _ 8  2x, so the initial value of the function is  1 _ 8 . shifts of the parent function f (x) = b x For any constants c and d, the function f (x) = b x + c + d shifts the parent function f (x) = b x • vertically d units, in the same direction of the sign of d. • horizontally c units, in the opposite direction of the sign of c. • The y-intercept becomes (0, bc + d). • The horizontal asymptote becomes y = d. • The range becomes (d, \infty ). • The domain, (-\infty , \infty ), remains unchanged.


**How To…**
Given an exponential function with the form f (x) = b x + c + d, graph the translation. 1. Draw the horizontal asymptote y = d. 2. Identify the shift as (-c, d). Shift the graph of f (x) = b x left c units if c is positive, and right c units if c is negative. 3. Shift the graph of f (x) = b x up d units if d is positive, and down d units if d is negative. 4. State the domain, (-\infty , \infty ), the range, (d, \infty ), and the horizontal asymptote y = d.

**Example  2**

### Graphing a Shift of an Exponential Function
Graph f (x) = 2x + 1 - 3. State the domain, range, and asymptote. Solution We have an exponential equation of the form f (x) = b x + c + d, with b = 2, c = 1, and d = -3. Draw the horizontal asymptote y = d, so draw y = -3. Identify the shift as (-c, d), so the shift is (-1, -3). Shift the graph of f (x) = b x left 1 units and down 3 units. x f (x) f (x) = 2x + 1 - 3 y = -3 The domain is (-\infty , \infty ); the range is (-3, \infty ); the horizontal asymptote is y = -3.

**Try It #2**
Graph f (x) = 2x - 1 + 3. State domain, range, and asymptote.

**How To…**
Given an equation of the form f (x) = b x + c + d for x, use a graphing calculator to approximate the solution. 1. Press [Y=]. Enter the given exponential equation in the line headed “Y^{1}=”. 2. Enter the given value for f (x) in the line headed “Y^{2}=”. 3. Press [WINDOW]. Adjust the y-axis so that it includes the value entered for “Y^{2}=”. 4. Press [GRAPH] to observe the graph of the exponential function along with the line for the specified value of f (x). 5. To find the value of x, we compute the point of intersection. Press [2ND] then [CALC]. Select “intersect” and press [ENTER] three times. The point of intersection gives the value of x for the indicated value of the function.

**Example  3**
Approximating the Solution of an Exponential Equation Solve 42 = 1.2(5)x + 2.8 graphically. Round to the nearest thousandth. Solution Press [Y=] and enter 1.2(5)x + 2.8 next to Y^{1}=. Then enter 42 next to Y^{2}=. For a window, use the values -3 to 3 for x and -5 to 55 for y. Press [GRAPH]. The graphs should intersect somewhere near x = 2. For a better approximation, press [2ND] then [CALC]. Select [5: intersect] and press [ENTER] three times. The x-coordinate of the point of intersection is displayed as 2.1661943. (Your answer may be different if you use a different window or use a different value for Guess?) To the nearest thousandth, x ≈ 2.166.


**Try It #3**
Solve 4 = 7.85(1.15)x - 2.27 graphically. Round to the nearest thousandth. Graphing a Stretch or Compression While horizontal and vertical shifts involve adding constants to the input or to the function itself, a stretch or compression occurs when we multiply the parent function f (x) = b x by a constant ∣ a ∣ > 0. For example, if we begin by graphing the parent function f (x) = 2x, we can then graph the stretch, using a = 3, to get g(x) = 3(2)x as shown on the left in Figure 8, and the compression, using a =  1 _ 3 , to get h(x) =  1 _ 3 (2)x as shown on the right in Figure 8. x y Vertical stretch Vertical compression (a) (b) x y g(x) = 3(2)x f (x) = 2x f (x) = 2x y = 0 y = 0 h(x) = (2)x (b) h(x) =  1 __ 3 (2)x compresses the graph of f (x) = 2x vertically by a factor of  1 __ 3 . stretches and compressions of the parent function f ( x ) = b x For any factor a > 0, the function f (x) = a(b)x • is stretched vertically by a factor of a if ∣ a ∣ > 1. • is compressed vertically by a factor of a if ∣ a ∣ < 1. • has a y-intercept of (0, a). • has a horizontal asymptote at y = 0, a range of (0, \infty ), and a domain of (-\infty , \infty ), which are unchanged from the parent function.

**Example  4**

### Graphing the Stretch of an Exponential Function
Sketch a graph of f (x) = 4   1 _ 2   x. State the domain, range, and asymptote. Solution Before graphing, identify the behavior and key points on the graph. • Since b =  1 _ 2  is between zero and one, the left tail of the graph will increase without bound as x decreases, and the right tail will approach the x-axis as x increases. • Since a = 4, the graph of f (x) =   1 _ 2   x will be stretched by a factor of 4. • Create a table of points as shown in Table 4. x -3 -2 -1 f (x) = 4  1 __ 2   x 0.5 • Plot the y-intercept, (0, 4), along with two other points. We can use (-1, 8) and (1, 2).

Draw a smooth curve connecting the points, as shown in Figure 9. x f(x) y = 0 f (x) = 4 1 x The domain is (-\infty , \infty ); the range is (0, \infty ); the horizontal asymptote is y = 0.

**Try It #4**
Sketch the graph of f (x) =  1 _ 2 (4)x. State the domain, range, and asymptote. Graphing Reflections In addition to shifting, compressing, and stretching a graph, we can also reflect it about the x-axis or the y-axis. When we multiply the parent function f (x) = b x by -1, we get a reflection about the x-axis. When we multiply the input by -1, we get a reflection about the y-axis. For example, if we begin by graphing the parent function f (x) = 2x, we can then graph the two reflections alongside it. The reflection about the x-axis, g(x) = -2x, is shown on the left side of Figure 10, and the reflection about the y-axis h(x) = 2-x, is shown on the right side of Figure 10. x y Reflection about the x-axis Reflection about the y-axis x y f (x) = 2x f (x) = 2x h(x) = 2-x g(x) = -2x y = 0 y = 0 reflections of the parent function f (x) = b x The function f (x) = -b x • reflects the parent function f (x) = b x about the x-axis. • has a y-intercept of (0, -1). • has a range of (-\infty , 0). • has a horizontal asymptote at y = 0 and domain of (-\infty , \infty ), which are unchanged from the parent function. The function f (x) = b-x • reflects the parent function f (x) = b x about the y-axis. • has a y-intercept of (0, 1), a horizontal asymptote at y = 0, a range of (0, \infty ), and a domain of (-\infty , \infty ), which are unchanged from the parent function.


**Example  5**

### Writing and Graphing the Reflection of an Exponential Function
Find and graph the equation for a function, g (x), that reflects f (x) =   1 _ 4   x about the x-axis. State its domain, range, and asymptote. Solution Since we want to reflect the parent function f (x) =   1 _ 4   x about the x-axis, we multiply f (x) by -1 to get, g (x) = -  1 _ 4   x . Next we create a table of points as in Table 5. x -3 -2 -1 g(x) = -   1 __ 4   x -64 -16 -4 -1 -0.25 Plot the y-intercept, (0, -1), along with two other points. We can use (-1, -4) and (1, -0.25). Draw a smooth curve connecting the points: x g(x) y = 0 g(x) = -1 x The domain is (-\infty , \infty ); the range is (-\infty , 0); the horizontal asymptote is y = 0.

**Try It #5**
Find and graph the equation for a function, g(x), that reflects f (x) = 1.25 x about the y-axis. State its domain, range, and asymptote. Summarizing Translations of the Exponential Function Now that we have worked with each type of translation for the exponential function, we can summarize them in Table 6 to arrive at the general equation for translating exponential functions. Translations of the Parent Function f (x) = b x Translation Form Shift • Horizontally c units to the left • Vertically d units up f (x) = b x + c + d Stretch and Compress • Stretch if | a | > 1 • Compression if 0 < | a | < 1 f (x) = ab x Reflect about the x-axis f (x) = -b x Reflect about the y-axis f (x) = b-x =   1 _ b   x General equation for all translations f (x) = ab x + c + d

translations of exponential functions A translation of an exponential function has the form f (x) = ab x + c + d Where the parent function, y = b x, b > 1, is • shifted horizontally c units to the left. • stretched vertically by a factor of ∣ a ∣ if ∣ a ∣ > 0. • compressed vertically by a factor of ∣ a ∣ if 0 < ∣ a ∣ < 1. • shifted vertically d units. • reflected about the x-axis when a < 0. Note the order of the shifts, transformations, and reflections follow the order of operations.

**Example  6**

### Writing a Function from a Description
Write the equation for the function described below. Give the horizontal asymptote, the domain, and the range. • f (x) = e x is vertically stretched by a factor of 2, reflected across the y-axis, and then shifted up 4 units. Solution We want to find an equation of the general form f (x) = ab x + c + d. We use the description provided to find a, b, c, and d. • We are given the parent function f (x) = e x, so b = e. • The function is stretched by a factor of 2, so a = 2. • The function is reflected about the y-axis. We replace x with -x to get: e-x. • The graph is shifted vertically 4 units, so d = 4. Substituting in the general form we get, f (x) = ab x + c + d

= 2e-x + 0 + 4

= 2e-x + 4 The domain is (-\infty , \infty ); the range is (4, \infty ); the horizontal asymptote is y = 4.

**Try It #6**
Write the equation for function described below. Give the horizontal asymptote, the domain, and the range. • f (x) = e x is compressed vertically by a factor of  1 _ 3 , reflected across the x-axis and then shifted down 2 units.

> Access this online resource for additional instruction and practice with graphing exponential functions. • Graph Exponential Functions (http://openstaxcollege.org/l/graphexpfunc)

4.2 Section EXERCISES Verbal 1. What role does the horizontal asymptote of an exponential function play in telling us about the end behavior of the graph? 2. What is the advantage of knowing how to recognize transformations of the graph of a parent function algebraically? Algebraic 3. The graph of f (x) = 3x is reflected about the y-axis and stretched vertically by a factor of 4. What is the equation of the new function, g(x)? State its y-intercept, domain, and range. 4. The graph of f (x) =   1 _ 2   -x is reflected about the y-axis and compressed vertically by a factor of  1 _ 5 . What is the equation of the new function, g(x)? State its y-intercept, domain, and range. 5. The graph of f (x) = 10x is reflected about the x-axis and shifted upward 7 units. What is the equation of the new function, g(x)? State its y-intercept, domain, and range. 6. The graph of f (x) = (1.68)x is shifted right 3 units, stretched vertically by a factor of 2, reflected about the x-axis, and then shifted downward 3 units. What is the equation of the new function, g(x)? State its y-intercept (to the nearest thousandth), domain, and range. 7. The graph of f (x) = - 1 _ 2   1 _ 4   x - 2+ 4 is shifted downward 4 units, and then shifted left 2 units, stretched vertically by a factor of 4, and reflected about the x-axis. What is the equation of the new function, g(x)? State its y-intercept, domain, and range. Graphical For the following exercises, graph the function and its reflection about the y-axis on the same axes, and give the y-intercept. 8. f (x) = 3  1 _ 2   x 9. g(x) = -2(0.25)x For the following exercises, graph each set of functions on the same axes. 11. f (x) = 3  1 _ 4   x , g(x) = 3(2)x, and h(x) = 3(4)x 12. f (x) =  1 _ 4 (3)x, g(x) = 2(3)x, and h(x) = 4(3)x For the following exercises, match each function with one of the graphs in Figure 12. A B C D E F


## 4.2 Section Exercises
For the following exercises, use the graphs shown in Figure 13. All have the form f (x) = ab x. y x A B C D E F 19. Which graph has the largest value for b? 20. Which graph has the smallest value for b? 21. Which graph has the largest value for a? 22. Which graph has the smallest value for a? For the following exercises, graph the function and its reflection about the x-axis on the same axes. 23. f (x) =  1 _ 2 (4)x 25. f (x) = -4(2)x + 2 For the following exercises, graph the transformation of f (x) = 2x. Give the horizontal asymptote, the domain, and the range. 26. f (x) = 2-x 27. h(x) = 2x + 3 28. f (x) = 2x - 2 For the following exercises, describe the end behavior of the graphs of the functions. 29. f (x) = -5(4)x - 1 30. f (x) = 3   1 _ 2   x - 2 31. f (x) = 3(4)-x + 2 For the following exercises, start with the graph of f (x) = 4x. Then write a function that results from the given transformation. 32. Shift f (x) 4 units upward 33. Shift f (x) 3 units downward 34. Shift f (x) 2 units left 35. Shift f (x) 5 units right 36. Reflect f (x) about the x-axis 37. Reflect f (x) about the y-axis For the following exercises, each graph is a transformation of y = 2x. Write an equation describing the transformation. x y x y x y

For the following exercises, find an exponential equation for the graph. x y x y Numeric For the following exercises, evaluate the exponential functions for the indicated value of x. 43. g (x) =  1 _ 3 (7)x - 2 for g(6). 44. f (x) = 4(2)x - 1 - 2 for f (5). 45. h(x) = - 1 _ 2   1 _ 2   x + 6 for h(-7). Technology For the following exercises, use a graphing calculator to approximate the solutions of the equation. Round to the nearest thousandth. f (x) = ab x + d. 46. -50 = -  1 _ 2   -x _ 4   1 _ 8   x _ 2   x - 1 - 2 Extensions 51. Explore and discuss the graphs of f (x) = (b)x and g(x) =   1 _ b   x . Then make a conjecture about the relationship between the graphs of the functions b x and   1 _ b   x  for any real number b > 0. 52. Prove the conjecture made in the previous exercise. 53. Explore and discuss the graphs of f (x) = 4x, g(x) = 4x - 2, and h(x) =   1 _ 16  4x. Then make a conjecture about the relationship between the graphs of the functions b x and   1 _ bn  b x for any real number n and real number b > 0. 54. Prove the conjecture made in the previous exercise.


## 4.3 Logarithmic Functions
Learning Objectives
In this section, you will:
• Convert from logarithmic to exponential form.
• Convert from exponential to logarithmic form.
• Evaluate logarithms.
• Use common logarithms.
• Use natural logarithms.
In 2010, a major earthquake struck Haiti, destroying or damaging over 285,000 homes[19]. One year later, another, stronger earthquake devastated Honshu, Japan, destroying or damaging over 332,000 buildings,[20] like those shown in earthquake in Haiti. How do we know? The magnitudes of earthquakes are measured on a scale known as the Richter Scale. The Haitian earthquake registered a 7.0 on the Richter Scale[21] whereas the Japanese earthquake registered a 9.0.[22] The Richter Scale is a base-ten logarithmic scale. In other words, an earthquake of magnitude 8 is not twice as great as an earthquake of magnitude 4. It is 108 - 4 = 104 = 10,000 times as great! In this lesson, we will investigate the nature of the Richter Scale and the base-ten function upon which it depends. Converting from Logarithmic to Exponential Form In order to analyze the magnitude of earthquakes or compare the magnitudes of two different earthquakes, we need to be able to convert between logarithmic and exponential form. For example, suppose the amount of energy released from one earthquake were 500 times greater than the amount of energy released from another. We want to calculate the difference in magnitude. The equation that represents this problem is 10x = 500, where x represents the difference in magnitudes on the Richter Scale. How would we solve for x? We have not yet learned a method for solving exponential equations. None of the algebraic tools discussed so far is sufficient to solve 10x = 500. We know that 102 = 100 and 103 = 1000, so it is clear that x must be some value between 2 and 3, since y = 10x is increasing. We can examine a graph, as in Figure 2, to better estimate the solution. x y = 10x y 19 http://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us^{2}010rja^{6}/#summary. Accessed 3/4/2013. 20 http://earthquake.usgs.gov/earthquakes/eqinthenews/2011/usc^{0}01xgp/#summary. Accessed 3/4/2013. 21 http://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us^{2}010rja^{6}/. Accessed 3/4/2013. 22 http://earthquake.usgs.gov/earthquakes/eqinthenews/2011/usc^{0}01xgp/#details. Accessed 3/4/2013.

Estimating from a graph, however, is imprecise. To find an algebraic solution, we must introduce a new function. Observe that the graph in Figure 2 passes the horizontal line test. The exponential function y = b x is one-to-one, so its inverse, x = b y is also a function. As is the case with all inverse functions, we simply interchange x and y and solve for y to find the inverse function. To represent y as a function of x, we use a logarithmic function of the form y = logb(x). The base b logarithm of a number is the exponent by which we must raise b to get that number. We read a logarithmic expression as, “The logarithm with base b of x is equal to y,” or, simplified, “log base b of x is y.” We can also say, “b raised to the power of y is x,” because logs are exponents. For example, the base 2 logarithm of 32 is 5, because 5 is the exponent we must apply to 2 to get 32. Since 25 = 32, we can write log^{2} 32 = 5. We read this as “log base 2 of 32 is 5.” We can express the relationship between logarithmic form and its corresponding exponential form as follows: logb(x) = y ⇔ b y = x, b > 0, b \neq  1 Note that the base b is always positive. logb(x) = y Think b to the y = x =

to Because logarithm is a function, it is most correctly written as logb(x), using parentheses to denote function evaluation, just as we would with f (x). However, when the input is a single variable or number, it is common to see the parentheses dropped and the expression written without parentheses, as logb x. Note that many calculators require parentheses around the x. We can illustrate the notation of logarithms as follows:

logb(c) = a means ba = c =

to Notice that, comparing the logarithm function and the exponential function, the input and the output are switched. This means y = logb (x) and y = b x are inverse functions. definition of the logarithmic function A logarithm base b of a positive number x satisfies the following definition. For x > 0, b > 0, b \neq  1, y = logb(x) is equivalent to b y = x where, • we read logb (x) as, “the logarithm with base b of x” or the “log base b of x.” • the logarithm y is the exponent to which b must be raised to get x. Also, since the logarithmic and exponential functions switch the x and y values, the domain and range of the exponential function are interchanged for the logarithmic function. Therefore, • the domain of the logarithm function with base b is (0, \infty ). • the range of the logarithm function with base b is ( -\infty , \infty ). Can we take the logarithm of a negative number? No. Because the base of an exponential function is always positive, no power of that base can ever be negative. We can never take the logarithm of a negative number. Also, we cannot take the logarithm of zero. Calculators may output a log of a negative number when in complex mode, but the log of a negative number is not a real number.

**How To…**
Given an equation in logarithmic form logb(x) = y, convert it to exponential form. 1. Examine the equation y = logb(x) and identify b, y, and x. 2. Rewrite logb(x) = y as b y = x.


**Example  1**
Converting from Logarithmic Form to Exponential Form Write the following logarithmic equations in exponential form. a. log^{6}(\sqrt{6} ) =  1 _ 2  b. log^{3}(9) = 2 Solution First, identify the values of b, y, and x. Then, write the equation in the form b y = x. a. log^{6}(\sqrt{6} ) =  1 _ 2  Here, b = 6, y =  1 _ 2 , and x = \sqrt{6} . Therefore, the equation log^{6}(\sqrt{6} ) =  1 _ 2  is equivalent to 6  1 __ 2  = \sqrt{6} . b. log^{3}(9) = 2 Here, b = 3, y = 2, and x = 9. Therefore, the equation log^{3}(9) = 2 is equivalent to 32 = 9.

**Try It #1**
Write the following logarithmic equations in exponential form. Converting From Exponential to Logarithmic Form To convert from exponents to logarithms, we follow the same steps in reverse. We identify the base b, exponent x, and output y. Then we write x = logb(y).

**Example  2**
Converting from Exponential Form to Logarithmic Form Write the following exponential equations in logarithmic form. a. 23 = 8 b. 52 = 25 c. 10-4 =  ______ Solution First, identify the values of b, y, and x. Then, write the equation in the form x = logb(y). Here, b = 2, x = 3, and y = 8. Therefore, the equation 23 = 8 is equivalent to log^{2}(8) = 3. Here, b = 5, x = 2, and y = 25. Therefore, the equation 52 = 25 is equivalent to log^{5}(25) = 2. c. 10-4 =  ______ Here, b = 10, x = -4, and y =  _ 10,000 . Therefore, the equation 10-4 =  _ 10,000  is equivalent to log^{1}0   _

**Try It #20**
Write the following exponential equations in logarithmic form. a. 32 = 9 b. 53 = 125 c. 2-1 =  1 __ 2  Evaluating Logarithms Knowing the squares, cubes, and roots of numbers allows us to evaluate many logarithms mentally. For example, consider log^{2}(8). We ask, “To what exponent must 2 be raised in order to get 8?” Because we already know 23 = 8, it follows that log^{2}(8) = 3. Now consider solving log^{7}(49) and log^{3}(27) mentally. • We ask, “To what exponent must 7 be raised in order to get 49?” We know 72 = 49. Therefore, log^{7}(49) = 2 • We ask, “To what exponent must 3 be raised in order to get 27?” We know 33 = 27. Therefore, log^{3}(27) = 3 Even some seemingly more complicated logarithms can be evaluated without a calculator. For example, let’s evaluate log 2 _ 3    4 _ 9   mentally. • We ask, “To what exponent must  2 _ 3  be raised in order to get  4 _ 9 ?” We know 22 = 4 and 32 = 9, so   2 _ 3   =  4 _ 9 . Therefore, log 2 _ 3    4 _ 9   = 2.


**How To…**
Given a logarithm of the form y = logb(x), evaluate it mentally. 1. Rewrite the argument x as a power of b : b y = x. 2. Use previous knowledge of powers of b identify y by asking, “To what exponent should b be raised in order to get x?”

**Example  3**

### Solving Logarithms Mentally
Solve y = log^{4}(64) without using a calculator. Solution First we rewrite the logarithm in exponential form: 4y = 64. Next, we ask, “To what exponent must 4 be raised in order to get 64?” We know 43 = 64 therefore, log^{4}(64) = 3.

**Try It #3**
Solve y = log^{1}21(11) without using a calculator.

**Example  4**

### Evaluating the Logarithm of a Reciprocal
Evaluate y = log^{3}   1 _ 27   without using a calculator. Solution First we rewrite the logarithm in exponential form: 3 y =  1 _ 27 . Next, we ask, “To what exponent must 3 be raised in order to get  1 _ 27  ?” We know 33 = 27, but what must we do to get the reciprocal,  1 _ 27 ? Recall from working with exponents that b-a =  1 _ ba . We use this information to write

3-3 =  1 __ 33 

=  1 __ 27  Therefore, log^{3}   1 _ 27   = -3.

**Try It #4**
Evaluate y = log^{2}   1 _ 32   without using a calculator. Using Common Logarithms Sometimes we may see a logarithm written without a base. In this case, we assume that the base is 10. In other words, the expression log(x) means log^{1}0(x). We call a base-10 logarithm a common logarithm. Common logarithms are used to measure the Richter Scale mentioned at the beginning of the section. Scales for measuring the brightness of stars and the pH of acids and bases also use common logarithms. definition of the common logarithm A common logarithm is a logarithm with base 10. We write log^{1}0(x) simply as log(x). The common logarithm of a positive number x satisfies the following definition. For x > 0, y = log(x) is equivalent to 10 y = x We read log(x) as, “the logarithm with base 10 of x” or “log base 10 of x.” The logarithm y is the exponent to which 10 must be raised to get x.


**How To…**
Given a common logarithm of the form y = log(x), evaluate it mentally. 1. Rewrite the argument x as a power of 10: 10 y = x. 2. Use previous knowledge of powers of 10 to identify y by asking, “To what exponent must 10 be raised in order to get x?”

**Example  5**

### Finding the Value of a Common Logarithm Mentally
Evaluate y = log(1,000) without using a calculator. Solution First we rewrite the logarithm in exponential form: 10y = 1,000. Next, we ask, “To what exponent must 10 be raised in order to get 1,000?” We know 103 = 1,000 therefore, log(1,000) = 3.

**Try It #5**

**How To…**
Given a common logarithm with the form y = log(x), evaluate it using a calculator. 1. Press [LOG]. 2. Enter the value given for x, followed by [ ) ]. 3. Press [ENTER].

**Example  6**

### Finding the Value of a Common Logarithm Using a Calculator
Evaluate y = log(321) to four decimal places using a calculator.

**Solution**
• Press [LOG]. • Enter 321, followed by [ ) ]. • Press [ENTER]. Rounding to four decimal places, log(321) ≈ 2.5065. Analysis Note that 102 = 100 and that 103 = 1000. Since 321 is between 100 and 1000, we know that log(321) must be between log(100) and log(1000). This gives us the following:


**Try It #6**
Evaluate y = log(123) to four decimal places using a calculator.

**Example  7**
Rewriting and Solving a Real-World Exponential Model The amount of energy released from one earthquake was 500 times greater than the amount of energy released from another. The equation 10x = 500 represents this situation, where x is the difference in magnitudes on the Richter Scale. To the nearest thousandth, what was the difference in magnitudes? Solution We begin by rewriting the exponential equation in logarithmic form.

log(500) = x Use the definition of the common log.

Next we evaluate the logarithm using a calculator: • Press [LOG]. • Enter 500, followed by [ ) ]. • Press [ENTER]. • To the nearest thousandth, log(500) ≈ 2.699. The difference in magnitudes was about 2.699.

**Try It #7**
The amount of energy released from one earthquake was 8,500 times greater than the amount of energy released from another. The equation 10x = 8500 represents this situation, where x is the difference in magnitudes on the Richter Scale. To the nearest thousandth, what was the difference in magnitudes? Using Natural Logarithms The most frequently used base for logarithms is e. Base e logarithms are important in calculus and some scientific applications; they are called natural logarithms. The base e logarithm, loge(x), has its own notation, ln(x). Most values of ln(x) can be found only using a calculator. The major exception is that, because the logarithm of 1 is always 0 in any base, ln(1) = 0. For other natural logarithms, we can use the ln key that can be found on most scientific calculators. We can also find the natural logarithm of any power of e using the inverse property of logarithms. definition of the natural logarithm A natural logarithm is a logarithm with base e. We write loge(x) simply as ln(x). The natural logarithm of a positive number x satisfies the following definition. For x > 0, y = ln(x) is equivalent to e y = x We read ln(x) as, “the logarithm with base e of x” or “the natural logarithm of x.” The logarithm y is the exponent to which e must be raised to get x. Since the functions y = e and y = ln(x) are inverse functions, ln(e x) = x for all x and e = x for x > 0.

**How To…**
Given a natural logarithm with the form y = ln(x), evaluate it using a calculator. 1. Press [LN]. 2. Enter the value given for x, followed by [ ) ]. 3. Press [ENTER].

**Example  8**

### Evaluating a Natural Logarithm Using a Calculator
Evaluate y = ln(500) to four decimal places using a calculator.

**Solution**
• Press [LN]. • Enter 500, followed by [ ) ]. • Press [ENTER]. Rounding to four decimal places, ln(500) ≈ 6.2146

**Try It #8**
Evaluate ln(-500). > Access this online resource for additional instruction and practice with logarithms. • Introduction to Logarithms (http://openstaxcollege.org/l/intrologarithms)


## 4.3 Section Exercises
4.3 SECTION EXERCISES Verbal 1. What is a base b logarithm? Discuss the meaning by interpreting each part of the equivalent equations b y = x and logb(x) = y for b > 0, b \neq  1. 2. How is the logarithmic function f (x) = logb(x) related to the exponential function g(x) = b x ? What is the result of composing these two functions? 3. How can the logarithmic equation logb x = y be solved for x using the properties of exponents? 4. Discuss the meaning of the common logarithm. What is its relationship to a logarithm with base b, and how does the notation differ? 5. Discuss the meaning of the natural logarithm. What is its relationship to a logarithm with base b, and how does the notation differ? Algebraic For the following exercises, rewrite each equation in exponential form. 6. log^{4}(q) = m 7. loga(b) = c 8. log^{1}6(y) = x 9. logx(64) = y 10. logy(x) = -11 11. log^{1}5(a) = b 12. logy(137) = x 14. log(v) = t 15. ln(w) = n For the following exercises, rewrite each equation in logarithmic form. 17. c d = k 18. m-7 = n __ 13  = y _ 5   m  = n _ 100  25. e k = h For the following exercises, solve for x by converting the logarithmic equation to exponential form. 26. log^{3}(x) = 2 27. log^{2}(x) = -3 28. log^{5}(x) = 2 29. log^{3}(x) = 3 30. log^{2}(x) = 6 31. log^{9}(x) =  1 _ 2  33. log^{6}(x) = -3 34. log(x) = 3 35. ln(x) = 2 For the following exercises, use the definition of common and natural logarithms to simplify. Numeric For the following exercises, evaluate the base b logarithmic expression without using a calculator. 42. log^{3}   1 _ 27   43. log^{6}(\sqrt{6} ) 44. log^{2}   1 _ 8   + 4 For the following exercises, evaluate the common logarithmic expression without using a calculator. 48. log(1) + 7

For the following exercises, evaluate the natural logarithmic expression without using a calculator. 50. ln e  1 __ 3    2 __ 5   Technology For the following exercises, evaluate each expression using a calculator. Round to the nearest thousandth. 56. ln  4 _ 5   57. log(\sqrt{2} ) 58. ln(\sqrt{2} ) Extensions 59. Is x = 0 in the domain of the function f (x) = log(x)? If so, what is the value of the function when x = 0? Verify the result. 60. Is f (x) = 0 in the range of the function f (x) = log(x)? If so, for what value of x? Verify the result. 61. Is there a number x such that ln x = 2? If so, what is that number? Verify the result. 62. Is the following true:  _ log^{4}   1 _ 64    = -1? Verify the result. 63. Is the following true:  ln(e^{1}.725) _ ln(1)  = 1.725? Verify the result. Real-World Applications 64. The exposure index EI for a 35 millimeter camera is a measurement of the amount of light that hits the film. It is determined by the equation EI = log^{2}  f 2

_ t  , where f is the “f-stop” setting on the camera, and t is the exposure time in seconds. Suppose the f-stop setting is 8 and the desired exposure time is 2 seconds. What will the resulting exposure index be? 65. Refer to the previous exercise. Suppose the light meter on a camera indicates an EI of -2, and the desired exposure time is 16 seconds. What should the f-stop setting be? 66. The intensity levels I of two earthquakes measured on a seismograph can be compared by the formula log  I^{1} _ I^{2}  = M^{1} - M^{2} where M is the magnitude given by the Richter Scale. In August 2009, an earthquake of magnitude 6.1 hit Honshu, Japan. In March 2011, that same region experienced yet another, more devastating earthquake, this time with a magnitude of 9.0.[23] How many times greater was the intensity of the 2011 earthquake? Round to the nearest whole number. 23 http://earthquake.usgs.gov/earthquakes/world/historical.php. Accessed 3/4/2014.


## 4.4 Graphs of Logarithmic Functions
Learning Objectives
In this section, you will:
• Identify the domain of a logarithmic function.
• Graph logarithmic functions.
In Graphs of Exponential Functions, we saw how creating a graphical representation of an exponential model gives us another layer of insight for predicting future events. How do logarithmic graphs give us insight into situations? Because every logarithmic function is the inverse function of an exponential function, we can think of every output on a logarithmic graph as the input for the corresponding inverse exponential equation. In other words, logarithms give the cause for an effect. To illustrate, suppose we invest $2,500 in an account that offers an annual interest rate of 5%, compounded continuously. We already know that the balance in our account for any year t can be found with the equation A = 2500e^{0}.05t. But what if we wanted to know the year for any balance? We would need to create a corresponding new function by interchanging the input and the output; thus we would need to create a logarithmic model for this situation. By graphing the model, we can see the output (year) for any input (account balance). For instance, what if we wanted to know how many years it would take for our initial investment to double? Figure 1 shows this point on the logarithmic graph. Logarithmic Model Showing Years as a Function of the Balance in the Account Account balance Te balance reaches Years In this section we will discuss the values for which a logarithmic function is defined, and then turn our attention to graphing the family of logarithmic functions. Finding the Domain of a Logarithmic Function Before working with graphs, we will take a look at the domain (the set of input values) for which the logarithmic function is defined. Recall that the exponential function is defined as y = b x for any real number x and constant b > 0, b \neq  1, where • The domain of y is (-\infty , \infty ). • The range of y is (0, \infty ). In the last section we learned that the logarithmic function y = logb(x) is the inverse of the exponential function y = b x. So, as inverse functions: • The domain of y = logb(x) is the range of y = b x : (0, \infty ). • The range of y = logb(x) is the domain of y = b x : (-\infty , \infty ).

Transformations of the parent function y = logb(x) behave similarly to those of other functions. Just as with other parent functions, we can apply the four types of transformations—shifts, stretches, compressions, and reflections—to the parent function without loss of shape. In Graphs of Exponential Functions we saw that certain transformations can change the range of y = b x. Similarly, applying transformations to the parent function y = logb(x) can change the domain. When finding the domain of a logarithmic function, therefore, it is important to remember that the domain consists only of positive real numbers. That is, the argument of the logarithmic function must be greater than zero. For example, consider f (x) = log^{4}(2x - 3). This function is defined for any values of x such that the argument, in this case 2x - 3, is greater than zero. To find the domain, we set up an inequality and solve for x :

2x - 3 > 0 Show the argument greater than zero.

2x > 3 Add 3.

Divide by 2. In interval notation, the domain of f (x) = log^{4}(2x - 3) is (1.5, \infty ).

**How To…**
Given a logarithmic function, identify the domain. 1. Set up an inequality showing the argument greater than zero. 2. Solve for x. 3. Write the domain in interval notation.

**Example  1**

### Identifying the Domain of a Logarithmic Shift
What is the domain of f (x) = log^{2}(x + 3)? Solution The logarithmic function is defined only when the input is positive, so this function is defined when x + 3 > 0. Solving this inequality,

x + 3 > 0 The input must be positive.

x > -3 Subtract 3. The domain of f (x) = log^{2}(x + 3) is (-3, \infty ).

**Try It #1**
What is the domain of f (x) = log^{5}(x - 2) + 1?

**Example  2**

### Identifying the Domain of a Logarithmic Shift and Reflection
What is the domain of f (x) = log(5 - 2x)? Solution The logarithmic function is defined only when the input is positive, so this function is defined when Solving this inequality,

5 - 2x > 0 The input must be positive.

-2x > -5 Subtract 5.

x <  5 __ 2  Divide by -2 and switch the inequality. The domain of f (x) = log(5 - 2x) is  –\infty ,  5 _ 2  .


**Try It #2**
What is the domain of f (x) = log(x - 5) + 2? Graphing Logarithmic Functions Now that we have a feel for the set of values for which a logarithmic function is defined, we move on to graphing logarithmic functions. The family of logarithmic functions includes the parent function y = logb(x) along with all its transformations: shifts, stretches, compressions, and reflections. We begin with the parent function y = logb(x). Because every logarithmic function of this form is the inverse of an exponential function with the form y = b x, their graphs will be reflections of each other across the line y = x. To illustrate this, we can observe the relationship between the input and output values of y = 2x and its equivalent x = log^{2}(y) in Table 1. x -3 -2 -1 2x = y  1 _ 8   1 _ 4   1 _ 2  log^{2}(y) = x -3 -2 -1 Using the inputs and outputs from Table 1, we can build another table to observe the relationship between points on the graphs of the inverse functions f (x) = 2x and g(x) = log^{2}(x). See Table 2. f (x) = 2x  -3,  1 _ 8    -2,  1 _ 4    -1,  1 _ 2   g(x) = log^{2}(x)   1 _ 8 , -3    1 _ 4 , -2    1 _ 2 , -1  As we’d expect, the x- and y-coordinates are reversed for the inverse functions. Figure 2 shows the graph of f and g. x y y = x g(x) = log^{2}(x) f (x) = 2x Observe the following from the graph: • f (x) = 2x has a y-intercept at (0, 1) and g(x) = log^{2}(x) has an x-intercept at (1, 0). • The domain of f (x) = 2x, (-\infty , \infty ), is the same as the range of g(x) = log^{2}(x). • The range of f (x) = 2x, (0, \infty ), is the same as the domain of g(x) = log^{2}(x).

characteristics of the graph of the parent function, f (x) = logb(x) For any real number x and constant b > 0, b \neq  1, we can see the following characteristics in the graph of f (x) = logb(x): • one-to-one function • vertical asymptote: x = 0 • domain: (0, \infty ) • range: (-\infty , \infty ) • x-intercept: (1, 0) and key point (b, 1) • y-intercept: none • increasing if b > 1 • decreasing if 0 < b < 1 See Figure 3. the graphs. Observe that the graphs compress vertically as the value of the base increases. (Note: recall that the function ln(x) has base x y log^{2}(x) ln(x) log(x) x = 0 functions with different bases, all greater than 1. f(x) x (b, 1) x = 0 f(x) = logb(x) b > 1 f(x) x (b, 1) x = 0 f (x) = logb(x) 0 < b < 1

**How To…**
Given a logarithmic function with the form f (x) = logb(x), graph the function. 1. Draw and label the vertical asymptote, x = 0. 2. Plot the x-intercept, (1, 0). 3. Plot the key point (b, 1). 4. Draw a smooth curve through the points. 5. State the domain, (0, \infty ), the range, (-\infty , \infty ), and the vertical asymptote, x = 0.

**Example  3**

### Graphing a Logarithmic Function with the Form f ( x) = logb( x).
Graph f (x) = log^{5}(x). State the domain, range, and asymptote. Solution Before graphing, identify the behavior and key points for the graph. • Since b = 5 is greater than one, we know the function is increasing. The left tail of the graph will approach the vertical asymptote x = 0, and the right tail will increase slowly without bound. • The x-intercept is (1, 0). • The key point (5, 1) is on the graph. • We draw and label the asymptote, plot and label the points, and draw a smooth curve through the points (see

x f (x) f (x) = log^{5}(x) x = 0 The domain is (0, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = 0.

**Try It #3**
Graph f (x) = log 1 _ 5 (x). State the domain, range, and asymptote. Graphing Transformations of Logarithmic Functions As we mentioned in the beginning of the section, transformations of logarithmic graphs behave similarly to those of other parent functions. We can shift, stretch, compress, and reflect the parent function y = logb(x) without loss of shape. Graphing a Horizontal Shift of f (x ) = logb(x ) When a constant c is added to the input of the parent function f (x) = logb(x), the result is a horizontal shift c units in the opposite direction of the sign on c. To visualize horizontal shifts, we can observe the general graph of the parent function f (x) = logb(x) and for c > 0 alongside the shift left, g(x ) = logb(x + c), and the shift right, h(x) = logb(x - c). See Figure 6. Shift left g (x) = logb(x + c) Shift right h(x) = logb(x - c) (b, 1) (1 - c, 0) (b - c, 1) f (x) = logb(x) x = 0 x y g(x) = logb(x + c) x = –c • The asymptote changes to x = -c. • The domain changes to (-c, \infty ). • The range remains (-\infty , \infty ). x = 0 y (1 + c, 0) (b + c, 1) (b, 1) h(x) = logb(x - c) f (x) = logb(x) x x = c • The asymptote changes to x = c. • The domain changes to (c, \infty ). • The range remains (-\infty , \infty ). horizontal shifts of the parent function y = logb(x) For any constant c, the function f (x) = logb (x + c) • shifts the parent function y = logb(x) left c units if c > 0. • shifts the parent function y = logb(x) right c units if c < 0. • has the vertical asymptote x = -c. • has domain (-c, \infty ). • has range (-\infty , \infty ).


**How To…**
Given a logarithmic function with the form f (x) = logb(x + c), graph the translation. 1. Identify the horizontal shift: a. If c > 0, shift the graph of f (x) = logb(x) left c units. b. If c < 0, shift the graph of f (x) = logb(x) right c units. 2. Draw the vertical asymptote x = -c. 3. Identify three key points from the parent function. Find new coordinates for the shifted functions by subtracting c from the x coordinate. 4. Label the three points. 5. The domain is (-c, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = -c.

**Example  4**

### Graphing a Horizontal Shift of the Parent Function y = logb( x)
Sketch the horizontal shift f (x) = log^{3}(x - 2) alongside its parent function. Include the key points and asymptotes on the graph. State the domain, range, and asymptote. Solution Since the function is f (x) = log^{3}(x - 2), we notice x + (-2) = x - 2. Thus c = -2, so c < 0. This means we will shift the function f (x) = log^{3}(x) right 2 units. The vertical asymptote is x = -(-2) or x = 2. Consider the three key points from the parent function,   1 The new coordinates are found by adding 2 to the x coordinates. Label the points   7 The domain is (2, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = 2. f (x) = log^{3}(x - 2) y = log^{3}(x) x = 0 x = 2 x y

**Try It #4**
Sketch a graph of f (x) = log^{3}(x + 4) alongside its parent function. Include the key points and asymptotes on the graph. State the domain, range, and asymptote. Graphing a Vertical Shift of y = logb(x ) When a constant d is added to the parent function f (x) = logb(x), the result is a vertical shift d units in the direction of the sign on d. To visualize vertical shifts, we can observe the general graph of the parent function f (x) = logb(x) alongside the shift up, g (x) = logb(x) + d and the shift down, h(x) = logb(x) - d. See Figure 8.

Shift up g (x) = logb(x) + d Shift down h(x) = logb(x) - d (b, 1) (b^{1} - d, 1) (b-d, 0) g(x) = logb(x) + d f (x) = logb(x) x = 0 y x (b, 1) (b^{1}+d, 1) (bd, 0) h(x) = logb(x) - d f (x) = logb(x) x = 0 y x • The asymptote remains x = 0. • The domain remains to (0, \infty ). • The range remains (-\infty , \infty ). • The asymptote remains x = 0. • The domain remains to (0, \infty ). • The range remains (-\infty , \infty ). vertical shifts of the parent function y = logb(x) For any constant d, the function f (x) = logb(x) + d • shifts the parent function y = logb(x) up d units if d > 0. • shifts the parent function y = logb(x) down d units if d < 0. • has the vertical asymptote x = 0. • has domain (0, \infty ). • has range (-\infty , \infty ).

**How To…**
Given a logarithmic function with the form f (x) = logb(x) + d, graph the translation. 1. Identify the vertical shift: a. If d > 0, shift the graph of f (x) = logb(x) up d units. b. If d < 0, shift the graph of f (x) = logb(x) down d units. 2. Draw the vertical asymptote x = 0. 3. Identify three key points from the parent function. Find new coordinates for the shifted functions by adding d to the y coordinate. 4. Label the three points. 5. The domain is (0, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = 0.

**Example  5**

### Graphing a Vertical Shift of the Parent Function y = logb(x)
Sketch a graph of f (x) = log^{3}(x) - 2 alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote. Solution Since the function is f (x) = log^{3}(x) - 2, we will notice d = -2. Thus d < 0. This means we will shift the function f (x) = log^{3}(x) down 2 units. The vertical asymptote is x = 0.

Consider the three key points from the parent function,   1 The new coordinates are found by subtracting 2 from the y coordinates. Label the points   1 _ 3 , -3 , (1, -2), and (3, -1). The domain is (0, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = 0. f (x) = log^{3}(x - 2) y = log^{3}(x) x = 0 x y The domain is (0, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = 0.

**Try It #5**
Sketch a graph of f (x) = log^{2}(x) + 2 alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote. Graphing Stretches and Compressions of y = logb(x ) When the parent function f (x) = logb(x) is multiplied by a constant a > 0, the result is a vertical stretch or compression of the original graph. To visualize stretches and compressions, we set a > 1 and observe the general graph of the parent function f (x) = logb(x) alongside the vertical stretch, g (x) = alogb(x) and the vertical compression, h(x) =  1 _ a logb(x). See Figure 10. Vertical Stretch g (x) = alogb(x), a > 1 Vertical Compression h(x) =  1 _ a logb(x), a > 1 (b, 1) g(x) = alogb(x) f(x) = logb(x) x = 0 x y (b , 1) 1/a • The asymptote remains x = 0. • The x-intercept remains (1, 0). • The domain remains (0, \infty ). • The range remains (-\infty , \infty ). (b, 1) f(x) = logb(x) x = 0 x y (ba, 1) h(x) = logb(x) 1a • The asymptote remains x = 0. • The x-intercept remains (1, 0). • The domain remains (0, \infty ). • The range remains (-\infty , \infty ).

vertical stretches and compressions of the parent function y = logb(x) For any constant a > 1, the function f (x) = alogb(x) • stretches the parent function y = logb(x) vertically by a factor of a if a > 1. • compresses the parent function y = logb(x) vertically by a factor of a if 0 < a < 1. • has the vertical asymptote x = 0. • has the x-intercept (1, 0). • has domain (0, \infty ). • has range (-\infty , \infty ).

**How To…**
Given a logarithmic function with the form f (x) = alogb(x), a > 0, graph the translation. 1. Identify the vertical stretch or compressions: a. If ∣ a ∣ > 1, the graph of f (x) = logb(x) is stretched by a factor of a units. b. If ∣ a ∣ < 1, the graph of f (x) = logb(x) is compressed by a factor of a units. 2. Draw the vertical asymptote x = 0. 3. Identify three key points from the parent function. Find new coordinates for the shifted functions by multiplying the y coordinates by a. 4. Label the three points. 5. The domain is (0, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = 0.

**Example  6**

### Graphing a Stretch or Compression of the Parent Function y = logb( x )
Sketch a graph of f (x) = 2log^{4}(x) alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote. Solution Since the function is f (x) = 2log^{4}(x), we will notice a = 2. This means we will stretch the function f (x) = log^{4}(x) by a factor of 2. The vertical asymptote is x = 0. Consider the three key points from the parent function,   1 The new coordinates are found by multiplying the y coordinates by 2. Label the points   1 The domain is (0, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = 0. See Figure 11. f (x) = 2log^{4}(x) y = log^{4}(x) x = 0 x y


**Try It #6**
Sketch a graph of f (x) =  1 _ 2 log^{4}(x) alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote.

**Example  7**

### Combining a Shift and a Stretch
Sketch a graph of f (x) = 5log(x + 2). State the domain, range, and asymptote. Solution Remember: what happens inside parentheses happens first. First, we move the graph left 2 units, then stretch the function vertically by a factor of 5, as in Figure 12. The vertical asymptote will be shifted to x = -2. The x-intercept will be (-1, 0). The domain will be (-2, \infty ). Two points will help give the shape of the graph: (-1, 0) and (8, 5). We chose x = 8 as the x-coordinate of one point to graph because when x = 8, x + 2 = 10, the base of the common logarithm. x y y = 5 log(x + 2) y = log(x + 2) y = log(x) x = -2 The domain is (-2, \infty ), the range is (-\infty , \infty ), and the vertical asymptote is x = -2.

**Try It #7**
Sketch a graph of the function f (x) = 3log(x - 2) + 1. State the domain, range, and asymptote. Graphing Reflections of f (x ) = logb(x ) When the parent function f (x) = logb(x) is multiplied by -1, the result is a reflection about the x-axis. When the input is multiplied by -1, the result is a reflection about the y-axis. To visualize reflections, we restrict b > 1, and observe the general graph of the parent function f (x) = logb(x) alongside the reflection about the x-axis, g(x) = -logb(x) and the reflection about the y-axis, h(x) = logb(-x). Reflection about the x-axis g (x) = logb(x), b > 1 Reflection about the y-axis h(x) = logb(-x), b > 1 (b, 1) f (x) = logb(x) g(x) = -logb(x) x = 0 x y (b -1, 1) • The reflected function is decreasing as x moves from zero to infinity. • The asymptote remains x = 0. • The x-intercept remains (1, 0). • The key point changes to (b - 1, 1). • The domain remains (0, \infty ). • The range remains (-\infty , \infty ). (b, 1) (-b, 1) f (x) = logb(x) h(x) = logb(-x) x = 0 x y • The reflected function is decreasing as x moves from infinity to zero. • The asymptote remains x = 0. • The x-intercept remains (-1, 0). • The key point changes to (-b, 1). • The domain changes to (-\infty , 0). • The range remains (-\infty , \infty ).

reflections of the parent function y = logb(x) The function f (x) = -logb(x) • reflects the parent function y = logb(x) about the x-axis. • has domain, (0, \infty ), range, (-\infty , \infty ), and vertical asymptote, x = 0, which are unchanged from the parent function. The function f (x) = logb(-x) • reflects the parent function y = logb(x) about the y-axis. • has domain (-\infty , 0). • has range, (-\infty , \infty ), and vertical asymptote, x = 0, which are unchanged from the parent function.

**How To…**
Given a logarithmic function with the parent function f (x) = logb(x), graph a translation. If f (x) = -logb(x) If f (x) = logb(-x) 1. Draw the vertical asymptote, x = 0. 1. Draw the vertical asymptote, x = 0. 2. Plot the x-intercept, (1, 0). 2. Plot the x-intercept, (1, 0). 3. Reflect the graph of the parent function f (x) = logb(x) about the x-axis. 3. Reflect the graph of the parent function f (x) = logb(x) about the y-axis. 4. Draw a smooth curve through the points. 4. Draw a smooth curve through the points. 5. State the domain, (0, \infty ), the range, (-\infty , \infty ), and the vertical asymptote x = 0. 5. State the domain, (-\infty , 0), the range, (-\infty , \infty ), and the vertical asymptote x = 0.

**Example  8**

### Graphing a Reflection of a Logarithmic Function
Sketch a graph of f (x) = log(-x) alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote. Solution Before graphing f (x) = log(-x), identify the behavior and key points for the graph. • Since b = 10 is greater than one, we know that the parent function is increasing. Since the input value is multiplied by -1, f is a reflection of the parent graph about the y-axis. Thus, f (x) = log(-x) will be decreasing as x moves from negative infinity to zero, and the right tail of the graph will approach the vertical asymptote x = 0. • The x-intercept is (-1, 0). • We draw and label the asymptote, plot and label the points, and draw a smooth curve through the points. f (x) = log(-x) y = log(x) x = 0 x y The domain is (-\infty , 0), the range is (-\infty , \infty ), and the vertical asymptote is x = 0.

**Try It #8**
Graph f (x) = -log(-x). State the domain, range, and asymptote.


**How To…**
Given a logarithmic equation, use a graphing calculator to approximate solutions. 1. Press [Y=]. Enter the given logarithm equation or equations as Y^{1}= and, if needed, Y^{2}=. 2. Press [GRAPH] to observe the graphs of the curves and use [WINDOW] to find an appropriate view of the graphs, including their point(s) of intersection. 3. To find the value of x, we compute the point of intersection. Press [2ND] then [CALC]. Select “intersect” and press [ENTER] three times. The point of intersection gives the value of x, for the point(s) of intersection.

**Example  9**
Approximating the Solution of a Logarithmic Equation Solve 4ln(x) + 1 = -2ln(x - 1) graphically. Round to the nearest thousandth. Solution Press [Y=] and enter 4ln(x) + 1 next to Y^{1}=. Then enter -2ln(x - 1) next to Y^{2}=. For a window, use the values 0 to 5 for x and –10 to 10 for y. Press [GRAPH]. The graphs should intersect somewhere a little to right of x = 1. For a better approximation, press [2ND] then [CALC]. Select [5: intersect] and press [ENTER] three times. The x-coordinate of the point of intersection is displayed as 1.3385297. (Your answer may be different if you use a different window or use a different value for Guess?) So, to the nearest thousandth, x ≈ 1.339.

**Try It #9**
Solve 5log(x + 2) = 4 - log(x) graphically. Round to the nearest thousandth. Summarizing Translations of the Logarithmic Function Now that we have worked with each type of translation for the logarithmic function, we can summarize each in Table 4 to arrive at the general equation for translating exponential functions. Translations of the Parent Function y = logb(x) Translation Form Shift • Horizontally c units to the left • Vertically d units up y = logb (x + c) + d Stretch and Compress • Stretch if ∣ a ∣ > 1 • Compression if ∣ a ∣ < 1 y = alogb(x) Reflect about the x-axis y = -logb(x) Reflect about the y-axis y = logb(-x) General equation for all translations y = alogb(x + c) + d translations of logarithmic functions All translations of the parent logarithmic function, y = logb(x), have the form f (x) = alogb(x + c) + d where the parent function, y = logb(x), b > 1, is • shifted vertically up d units. • shifted horizontally to the left c units. • stretched vertically by a factor of ∣ a ∣ if ∣ a ∣ > 0. • compressed vertically by a factor of ∣ a ∣ if 0 < ∣ a ∣ < 1. • reflected about the x-axis when a < 0. For f (x) = log(-x), the graph of the parent function is reflected about the y-axis.


**Example  10**
Finding the Vertical Asymptote of a Logarithm Graph What is the vertical asymptote of f (x) = -2log^{3}(x + 4) + 5? Solution The vertical asymptote is at x = -4. Analysis The coefficient, the base, and the upward translation do not affect the asymptote. The shift of the curve 4 units to the left shifts the vertical asymptote to x = -4.

**Try It #10**
What is the vertical asymptote of f (x) = 3 + ln(x - 1)?

**Example  11**
Finding the Equation from a Graph Find a possible equation for the common logarithmic function graphed in Figure 15. x f(x) Solution This graph has a vertical asymptote at x = -2 and has been vertically reflected. We do not know yet the vertical shift or the vertical stretch. We know so far that the equation will have form: f (x) = -alog(x + 2) + k It appears the graph passes through the points (-1, 1) and (2, -1). Substituting (-1, 1),

1 = -alog(-1 + 2) + k Substitute (-1, 1).

1 = -alog(1) + k Arithmetic.

1 = k log(1) = 0. Next, substituting in (2, –1),

-1 = -alog(2 + 2) + 1 Plug in (2, -1).

-2 = -alog(4) Arithmetic.

a =  _____ log(4)  Solve for a. This gives us the equation f (x) = - _ log(4) log(x + 2) + 1. Analysis can verify this answer by comparing the function values in Table 5 with the points on the graph in Figure 15. x -1 f (x) -1 x f (x) -2


**Try It #11**
Give the equation of the natural logarithm graphed in Figure 16. x f(x) Is it possible to tell the domain and range and describe the end behavior of a function just by looking at the graph? Yes, if we know the function is a general logarithmic function. For example, look at the graph in Figure 16. The graph approaches x = -3 (or thereabouts) more and more closely, so x = -3 is, or is very close to, the vertical asymptote. It approaches from the right, so the domain is all points to the right, {x | x > -3}. The range, as with all general logarithmic functions, is all real numbers. And we can see the end behavior because the graph goes down as it goes left and up as it goes right. The end behavior is that as x → -3+, f (x) → -\infty  and as x → \infty , f (x) → \infty .

Access these online resources for additional instruction and practice with graphing logarithms. • Graph an Exponential Function and Logarithmic Function (http://openstaxcollege.org/l/graphexplog) • Match Graphs with Exponential and Logarithmic Functions (http://openstaxcollege.org/l/matchexplog) • Find the Domain of Logarithmic Functions (http://openstaxcollege.org/l/domainlog)


## 4.4 Section Exercises
4.4 Section ExERCISES Verbal 1. The inverse of every logarithmic function is an exponential function and vice-versa. What does this tell us about the relationship between the coordinates of the points on the graphs of each? 2. What type(s) of translation(s), if any, affect the range of a logarithmic function? 3. What type(s) of translation(s), if any, affect the domain of a logarithmic function? 4. Consider the general logarithmic function f (x) = logb(x). Why can’t x be zero? 5. Does the graph of a general logarithmic function have a horizontal asymptote? Explain. Algebraic For the following exercises, state the domain and range of the function. 6. f (x) = log^{3}(x + 4) 7. h(x) = ln   1 _ 2  - x  8. g(x) = log^{5}(2x + 9) - 2 9. h(x) = ln(4x + 17) - 5 10. f (x) = log^{2}(12 - 3x) - 3 For the following exercises, state the domain and the vertical asymptote of the function. 11. f (x) = logb(x - 5) 12. g(x) = ln(3 - x) 13. f (x) = log(3x + 1) 14. f (x) = 3log(-x) + 2 15. g(x) = -ln(3x + 9) - 7 For the following exercises, state the domain, vertical asymptote, and end behavior of the function. 16. f (x) = ln(2 - x) 17. f (x) = log  x - 3 _ 7   18. h(x) = -log(3x - 4) + 3 19. g(x) = ln(2x + 6) - 5 20. f (x) = log^{3}(15 - 5x) + 6 For the following exercises, state the domain, range, and x- and y-intercepts, if they exist. If they do not exist, write DNE. 21. h(x) = log^{4}(x - 1) + 1 22. f (x) = log(5x + 10) + 3 23. g(x) = ln(-x) - 2 24. f (x) = log^{2}(x + 2) - 5 25. h(x) = 3ln(x) - 9 Graphical For the following exercises, match each function in Figure 17 with the letter corresponding to its graph. A B C D E x y 26. d(x) = log(x) 27. f (x) = ln(x) 28. g(x) = log^{2}(x) 29. h(x) = log^{5}(x) 30. j(x) = log^{2}5(x)

For the following exercises, match each function in Figure 18 with the letter corresponding to its graph. x y A B C 31. f (x) = log  1 _ 3 (x) 32. g(x) = log^{2}(x) 33. h(x) = log  3 _ 4 (x) For the following exercises, sketch the graphs of each pair of functions on the same axis. 34. f (x) = log(x) and g(x) = 10x 35. f (x) = log(x) and g(x) = log  1 _ 2 (x) 36. f (x) = log^{4}(x) and g(x) = ln(x) 37. f (x) = e x and g(x) = ln(x) For the following exercises, match each function in Figure 19 with the letter corresponding to its graph. x y A B C 38. f (x) = log^{4}(-x + 2) 39. g(x) = -log^{4}(x + 2) 40. h(x) = log^{4}(x + 2) For the following exercises, sketch the graph of the indicated function. 41. f (x) = log^{2}(x + 2) 42. f (x) = 2log(x) 43. f (x) = ln(-x) 44. g(x) = log(4x + 16) + 4 45. g(x) = log(6 - 3x) + 1 46. h(x) = - 1 _ 2  ln(x + 1) - 3 For the following exercises, write a logarithmic equation corresponding to the graph shown. 47. Use y = log^{2}(x) as the parent function. x y 48. Use f (x) = log^{3}(x) as the parent function. x y

49. Use f (x) = log^{4}(x) as the parent function. x y 50. Use f (x) = log^{5}(x) as the parent function. x y Technology For the following exercises, use a graphing calculator to find approximate solutions to each equation. 51. log(x - 1) + 2 = ln(x - 1) + 2 52. log(2x - 3) + 2 = -log(2x - 3) + 5 53. ln(x - 2) = -ln(x + 1) 54. 2ln(5x + 1) = 1 _ 2 ln(-5x) + 1 _ 3 log(1 - x) = log(x + 1) +  1 _ 3  Extensions 56. Let b be any positive real number such that b \neq  1. What must logb^{1} be equal to? Verify the result. 57. Explore and discuss the graphs of f (x) = log  1 _ 2 (x) and g(x) = -log^{2}(x). Make a conjecture based on the result. 58. Prove the conjecture made in the previous exercise. 59. What is the domain of the function f (x) = ln   x + 2 _ x - 4  ? Discuss the result. 60. Use properties of exponents to find the x-intercepts of the function f (x) = log(x 2 + 4x + 4) algebraically. Show the steps for solving, and then verify the result by graphing the function.

Learning Objectives
In this section, you will:
• Use the product rule for logarithms.
• Use the quotient rule for logarithms.
• Use the power rule for logarithms.
• Expand logarithmic expressions.
• Condense logarithmic expressions.
• Use the change-of-base formula for logarithms.

## 4.5 Logarithmic Properties
In chemistry, pH is used as a measure of the acidity or alkalinity of a substance. The pH scale runs from 0 to 14. Substances with a pH less than 7 are considered acidic, and substances with a pH greater than 7 are said to be alkaline. Our bodies, for instance, must maintain a pH close to 7.35 in order for enzymes to work properly. To get a feel for what is acidic and what is alkaline, consider the following pH levels of some common substances: • Battery acid: 0.8 • Stomach acid: 2.7 • Orange juice: 3.3 • Pure water: 7 (at 25° C) • Human blood: 7.35 • Fresh coconut: 7.8 • Sodium hydroxide (lye): 14 To determine whether a solution is acidic or alkaline, we find its pH, which is a measure of the number of active positive hydrogen ions in the solution. The pH is defined by the following formula, where a is the concentration of hydrogen ion in the solution

pH = -log([H+])

= log   _____ ([H+]   The equivalence of -log ([H+]) and log   1 _ [H+]   is one of the logarithm properties we will examine in this section. Using the Product Rule for Logarithms Recall that the logarithmic and exponential functions “undo” each other. This means that logarithms have similar properties to exponents. Some important properties of logarithms are given here. First, the following properties are easy to prove.

logb(1) = 0

logb(b) = 1 For example, log^{5} 1 = 0 since 50 = 1. And log^{5} 5 = 1 since 51 = 5.

Next, we have the inverse property.

logb(b x) = x

b logb(x) = x, x > 0 For example, to evaluate log(100), we can rewrite the logarithm as log^{1}0(102), and then apply the inverse property logb (b x) = x to get log^{1}0(102) = 2. To evaluate e ln(7), we can rewrite the logarithm as eloge(7), and then apply the inverse property b logb (x) = x to get eloge(7) = 7. Finally, we have the one-to-one property.

logbM = logbN if and only if M = N We can use the one-to-one property to solve the equation log^{3}(3x) = log^{3}(2x + 5) for x. Since the bases are the same, we can apply the one-to-one property by setting the arguments equal and solving for x :

3x = 2x + 5 Set the arguments equal.

x = 5 Subtract 2x. But what about the equation log^{3}(3x) + log^{3}(2x + 5) = 2? The one-to-one property does not help us in this instance. Before we can solve an equation like this, we need a method for combining terms on the left side of the equation. Recall that we use the product rule of exponents to combine the product of exponents by adding: x a xb = x a + b. We have a similar property for logarithms, called the product rule for logarithms, which says that the logarithm of a product is equal to a sum of logarithms. Because logs are exponents, and we multiply like bases, we can add the exponents. We will use the inverse property to derive the product rule below. Given any real number x and positive real numbers M, N, and b, where b \neq  1, we will show

logb(MN) = logb(M) + logb(N). Let m = logb(M) and n = logb(N). In exponential form, these equations are b m = M and b n = N. It follows that

logb(MN) = logb(b mb n) Substitute for M and N.

= logb(b m + n) Apply the product rule for exponents.

= m + n Apply the inverse property of logs.

= logb(M) + logb(N) Substitute for m and n. Note that repeated applications of the product rule for logarithms allow us to simplify the logarithm of the product of any number of factors. For example, consider logb(wxyz). Using the product rule for logarithms, we can rewrite this logarithm of a product as the sum of logarithms of its factors:

logb(wxyz) = logb(w) + logb(x) + logb(y) + logb(z) the product rule for logarithms The product rule for logarithms can be used to simplify a logarithm of a product by rewriting it as a sum of individual logarithms. logb(MN) = logb(M) + logb(N) for b > 0

**How To…**
Given the logarithm of a product, use the product rule of logarithms to write an equivalent sum of logarithms. 1. Factor the argument completely, expressing each whole number factor as a product of primes. 2. Write the equivalent expression by summing the logarithms of each factor.


**Example  1**
Using the Product Rule for Logarithms Expand log^{3}(30x(3x + 4)). Solution We begin by factoring the argument completely, expressing 30 as a product of primes.

log^{3}(30x(3x + 4)) = log^{3}(2 \cdot  3 \cdot  5 \cdot  x \cdot  (3x +4)) Next we write the equivalent equation by summing the logarithms of each factor.

log^{3}(30x(3x + 4)) = log^{3}(2) + log^{3}(3) + log^{3}(5) + log^{3}(x) + log^{3}(3x + 4)

**Try It #1**
Expand logb(8k). Using the Quotient Rule for Logarithms For quotients, we have a similar rule for logarithms. Recall that we use the quotient rule of exponents to combine the quotient of exponents by subtracting: x  a __ b  = x a-b. The quotient rule for logarithms says that the logarithm of a quotient is equal to a difference of logarithms. Just as with the product rule, we can use the inverse property to derive the quotient rule. Given any real number x and positive real numbers M, N, and b, where b \neq  1, we will show

logb   M __ N   = logb(M) - logb(N). Let m = logb(M) and n = logb(N). In exponential form, these equations are bm = M and bn = N. It follows that

logb   M __ N   = logb   bm __ bn   Substitute for M and N.

= logb(b m - n) Apply the quotient rule for exponents.

= m - n Apply the inverse property of logs.

= logb(M) - logb(N) Substitute for m and n. For example, to expand log   2x^{2} + 6x _ 3x + 9  , we must first express the quotient in lowest terms. Factoring and canceling we get,

log   2x^{2} + 6x _______ 3x + 9  = log   2x(x + 3) ________ 3(x + 3)   Factor the numerator and denominator.

= log   2x __ 3   Cancel the common factors. Next we apply the quotient rule by subtracting the logarithm of the denominator from the logarithm of the numerator. Then we apply the product rule.

log   2x __ 3   = log(2x) - log(3)

= log(2) + log(x) - log(3) the quotient rule for logarithms The quotient rule for logarithms can be used to simplify a logarithm or a quotient by rewriting it as the difference of individual logarithms. logb   M __ N   = logb(M) - logb(N)

**How To…**
Given the logarithm of a quotient, use the quotient rule of logarithms to write an equivalent difference of logarithms. 1. Express the argument in lowest terms by factoring the numerator and denominator and canceling common terms. 2. Write the equivalent expression by subtracting the logarithm of the denominator from the logarithm of the numerator. 3. Check to see that each term is fully expanded. If not, apply the product rule for logarithms to expand completely.


**Example  2**
Using the Quotient Rule for Logarithms Expand log^{2}   15x(x - 1) __

(3x + 4)(2 - x)  . Solution First we note that the quotient is factored and in lowest terms, so we apply the quotient rule. log^{2}   15x(x - 1) __

(3x + 4)(2 - x)   = log^{2}(15x(x-1))- log^{2}((3x + 4)(2 - x)) Notice that the resulting terms are logarithms of products. To expand completely, we apply the product rule, noting that the prime factors of the factor 15 are 3 and 5. log^{2}(15x(x - 1)) - log^{2}((3x + 4)(2 - x)) = [log^{2}(3) + log^{2}(5) + log^{2}(x) + log^{2}(x - 1)] - [log^{2}(3x + 4) + log^{2}(2 - x)]

= log^{2}(3) + log^{2}(5) + log^{2}(x) + log^{2}(x - 1) - log^{2}(3x + 4) - log^{2}(2 - x) Analysis There are exceptions to consider in this and later examples. First, because denominators must never be zero, this expression is not defined for x = - 4 _ 3  and x = 2. Also, since the argument of a logarithm must be positive, we note as we observe the expanded logarithm, that x > 0, x > 1, x > - 4 _ 3 , and x < 2. Combining these conditions is beyond the scope of this section, and we will not consider them here or in subsequent exercises.

**Try It #2**
Expand log^{3}   __

7x(x - 1)(x - 2)  . Using the Power Rule for Logarithms We’ve explored the product rule and the quotient rule, but how can we take the logarithm of a power, such as x^{2}? One method is as follows:

logb(x^{2}) = logb(x ⋅ x)

= logb (x) + logb (x)

= 2log b (x) Notice that we used the product rule for logarithms to find a solution for the example above. By doing so, we have derived the power rule for logarithms, which says that the log of a power is equal to the exponent times the log of the base. Keep in mind that, although the input to a logarithm may not be written as a power, we may be able to change it to a power. For example, 3  = 3  1 __ 2   1 _ e  = e-1 the power rule for logarithms The power rule for logarithms can be used to simplify the logarithm of a power by rewriting it as the product of the exponent times the logarithm of the base. logb(Mn) = nlogb(M)

**How To…**
Given the logarithm of a power, use the power rule of logarithms to write an equivalent product of a factor and a logarithm. 1. Express the argument as a power, if needed. 2. Write the equivalent expression by multiplying the exponent times the logarithm of the base.


**Example  3**
Expanding a Logarithm with Powers Expand log^{2}(x^{5}). Solution The argument is already written as a power, so we identify the exponent, 5, and the base, x, and rewrite the equivalent expression by multiplying the exponent times the logarithm of the base.

log^{2}(x 5) = 5log^{2}(x)

**Try It #3**
Expand ln(x^{2}).

**Example  4**
Rewriting an Expression as a Power before Using the Power Rule Expand log^{3}(25) using the power rule for logs. Solution Expressing the argument as a power, we get log^{3}(25) = log^{3}(52). Next we identify the exponent, 2, and the base, 5, and rewrite the equivalent expression by multiplying the exponent times the logarithm of the base.

log^{3}(5 2) = 2log^{3}(5)

**Try It #4**
Expand ln   1 _ x^{2}  .

**Example  5**
Using the Power Rule in Reverse Rewrite 4ln(x) using the power rule for logs to a single logarithm with a leading coefficient of 1. Solution Because the logarithm of a power is the product of the exponent times the logarithm of the base, it follows that the product of a number and a logarithm can be written as a power. For the expression 4ln(x), we identify the factor, 4, as the exponent and the argument, x, as the base, and rewrite the product as a logarithm of a power: 4ln(x) = ln(x^{4}).

**Try It #5**
Rewrite 2log^{3}(4) using the power rule for logs to a single logarithm with a leading coefficient of 1. Expanding Logarithmic Expressions Taken together, the product rule, quotient rule, and power rule are often called “laws of logs.” Sometimes we apply more than one rule in order to simplify an expression. For example:

logb   6x _ y   = logb(6x) - logb(y)

= logb(6) + logb(x) - logb(y) We can use the power rule to expand logarithmic expressions involving negative and fractional exponents. Here is an alternate proof of the quotient rule for logarithms using the fact that a reciprocal is a negative power:

logb   A __ C   = logb(AC -1)

= logb(A) + logb(C -1)

= logb(A) + (-1)logb(C)

= logb(A) - logb(C) We can also apply the product rule to express a sum or difference of logarithms as the logarithm of a product. With practice, we can look at a logarithmic expression and expand it mentally, writing the final answer. Remember, however, that we can only do this with products, quotients, powers, and roots—never with addition or subtraction inside the argument of the logarithm.


**Example  6**
Expanding Logarithms Using Product, Quotient, and Power Rules Rewrite ln   x 4 y _ 7   as a sum or difference of logs. Solution First, because we have a quotient of two expressions, we can use the quotient rule:

ln   x 4y ___ 7   = ln(x 4y)- ln(7) Then seeing the product in the first term, we use the product rule:

ln(x 4y) - ln(7) = ln(x 4) + ln(y) - ln(7) Finally, we use the power rule on the first term:

ln(x^{4})+ ln(y) - ln(7) = 4ln(x) + ln(y) - ln(7)

**Try It #6**
Expand log   x^{2} y^{3} _ z^{4}  .

**Example  7**
Using the Power Rule for Logarithms to Simplify the Logarithm of a Radical Expression Expand log(\sqrt{x} ).

**Solution**

log(\sqrt{x} ) = log(x)  1 __ 2 

=  1 __ 2  log(x)

**Try It #7**
Expand ln( \sqrt{x^{2}} ). Can we expand ln(x^{2} + y^{2})? No. There is no way to expand the logarithm of a sum or difference inside the argument of the logarithm.

**Example  8**
Expanding Complex Logarithmic Expressions Expand log^{6}   64x^{3} (4x + 1) __ (2x - 1)  . Solution We can expand by applying the Product and Quotient Rules. log^{6}   64x^{3}(4x + 1) __ (2x - 1)   = log^{6}(64) + log^{6}(x^{3}) + log^{6}(4x + 1) - log^{6}(2x - 1) Apply the Quotient Rule.

= log^{6}(26) + log^{6}(x^{3}) + log^{6}(4x + 1) - log^{6}(2x - 1) Simplify by writing 64 as 26.

= 6log^{6}(2) + 3log^{6}(x) + log^{6}(4x + 1) - log^{6}(2x - 1) Apply the Power Rule.

**Try It #8**
Expand ln    \sqrt{(x} - 1)(2x + 1)^{2} 

__ x 2 - 9  . Condensing Logarithmic Expressions We can use the rules of logarithms we just learned to condense sums, differences, and products with the same base as a single logarithm. It is important to remember that the logarithms must have the same base to be combined. We will learn later how to change the base of any logarithm before condensing.


**How To…**
Given a sum, difference, or product of logarithms with the same base, write an equivalent expression as a single logarithm. 1. Apply the power property first. Identify terms that are products of factors and a logarithm, and rewrite each as the logarithm of a power. 2. Next apply the product property. Rewrite sums of logarithms as the logarithm of a product. 3. Apply the quotient property last. Rewrite differences of logarithms as the logarithm of a quotient.

**Example  9**
Using the Product and Quotient Rules to Combine Logarithms Write log^{3}(5) + log^{3}(8) - log^{3}(2) as a single logarithm. Solution Using the product and quotient rules log^{3}(5) + log^{3}(8) = log^{3}(5 \cdot  8) = log^{3}(40) This reduces our original expression to log^{3}(40) - log^{3}(2) Then, using the quotient rule log^{3}(40) - log^{3}(2) = log^{3}   40 __ 2   = log^{3}(20)

**Try It #9**
Condense log(3) - log(4) + log(5) - log(6).

**Example  10**
Condensing Complex Logarithmic Expressions Condense log^{2}(x 2) +  1 __ 2 log^{2}(x - 1) - 3log^{2}((x + 3)^{2}). Solution We apply the power rule first:

log^{2}(x 2) +  1 __ 2 log^{2}(x - 1) - 3log^{2}((x + 3)^{2}) = log^{2}(x^{2}) + log^{2}(\sqrt{x} - 1 ) - log^{2}((x + 3)^{6}) Next we apply the product rule to the sum:

log^{2}(x 2) + log^{2}(\sqrt{x} - 1 ) - log^{2}((x + 3)^{6}) = log^{2}(x^{2}\sqrt{x} - 1 ) - log^{2}((x + 3)^{6}) Finally, we apply the quotient rule to the difference:

log^{2}(x 2\sqrt{x} - 1 )- log^{2}((x + 3)^{6}) = log^{2}  x^{2}\sqrt{x} - 1  ________ (x + 3)^{6}  

**Try It #10**
Rewrite log(5) + 0.5log(x) - log(7x - 1) + 3log(x - 1) as a single logarithm.

**Example  11**
Rewriting as a Single Logarithm Rewrite 2log(x) - 4log(x + 5) +  1 _ x log(3x + 5) as a single logarithm. Solution We apply the power rule first:

2log(x) - 4log(x + 5) +  1 _ x log(3x + 5) = log(x^{2}) - log((x + 5)^{4}) + log (3x + 5)x -1  Next we apply the product rule to the sum:

log(x^{2})- log((x + 5)^{4}) + log (3x + 5)x -1  = log(x^{2})- log (x + 5)^{4}(3x + 5)x -1  Finally, we apply the quotient rule to the difference:

log(x^{2}) - log (x + 5)^{4}(3x + 5)x -1  = log  x 2 __

(x + 5)^{4}(3x + 5)x -1  


**Try It #11**
Condense 4(3log(x) + log(x + 5) - log(2x + 3)).

**Example  12**

### Applying of the Laws of Logs
Recall that, in chemistry, pH = -log[H+]. If the concentration of hydrogen ions in a liquid is doubled, what is the effect on pH? Solution Suppose C is the original concentration of hydrogen ions, and P is the original pH of the liquid. Then P = -log(C). If the concentration is doubled, the new concentration is 2C. Then the pH of the new liquid is

pH = -log(2C) Using the product rule of logs pH = -log(2C) = -(log(2) + log(C)) = -log(2) - log(C) Since P = -log(C), the new pH is

pH = P - log(2) ≈ P - 0.301 When the concentration of hydrogen ions is doubled, the pH decreases by about 0.301.

**Try It #12**
How does the pH change when the concentration of positive hydrogen ions is decreased by half? Using the Change-of-Base Formula for Logarithms Most calculators can evaluate only common and natural logs. In order to evaluate logarithms with a base other than 10 or e, we use the change-of-base formula to rewrite the logarithm as the quotient of logarithms of any other base; when using a calculator, we would change them to common or natural logs. To derive the change-of-base formula, we use the one-to-one property and power rule for logarithms. Given any positive real numbers M, b, and n, where n \neq  1 and b \neq  1, we show

logb(M) =  logn(M) _ logn(b)  Let y = logb(M). By taking the log base n of both sides of the equation, we arrive at an exponential form, namely b y = M. It follows that

logn(b y) = logn(M) Apply the one-to-one property.

ylogn(b) = logn(M) Apply the power rule for logarithms.

y =  logn(M) _ logn(b)  Isolate y.

logb(M) =  logn(M) _ logn(b)  Substitute for y. For example, to evaluate log^{5}(36) using a calculator, we must first rewrite the expression as a quotient of common or natural logs. We will use the common log.

log^{5}(36) =  log(36) _ log(5)  Apply the change of base formula using base 10.

Use a calculator to evaluate to 4 decimal places.

the change-of-base formula The change-of-base formula can be used to evaluate a logarithm with any base. For any positive real numbers M, b, and n, where n \neq  1 and b \neq  1, logb(M) =  logn(M) _ logn(b) . It follows that the change-of-base formula can be used to rewrite a logarithm with any base as the quotient of common or natural logs. logb(M) =  ln(M) _ ln(b)  and logb(M) =  logn(M) _ logn(b) 

**How To…**
Given a logarithm with the form logb(M), use the change-of-base formula to rewrite it as a quotient of logs with any positive base n, where n \neq  1. 1. Determine the new base n, remembering that the common log, log(x), has base 10, and the natural log, ln(x), has base e. 2. Rewrite the log as a quotient using the change-of-base formula a. The numerator of the quotient will be a logarithm with base n and argument M. b. The denominator of the quotient will be a logarithm with base n and argument b.

**Example  13**
Changing Logarithmic Expressions to Expressions Involving Only Natural Logs Change log^{5}(3) to a quotient of natural logarithms. Solution Because we will be expressing log^{5}(3) as a quotient of natural logarithms, the new base, n = e. We rewrite the log as a quotient using the change-of-base formula. The numerator of the quotient will be the natural log with argument 3. The denominator of the quotient will be the natural log with argument 5. logb(M) =  ln(M) _ ln(b)  log^{5}(3) =  ln(3) _ ln(5) 

**Try It #13**
Change log^{0}.5(8) to a quotient of natural logarithms. Can we change common logarithms to natural logarithms? Yes. Remember that log(9) means log^{1}0(9). So, log(9) =  ln(9) _ ln(10) .

**Example  14**
Using the Change-of-Base Formula with a Calculator Evaluate log^{2}(10) using the change-of-base formula with a calculator. Solution According to the change-of-base formula, we can rewrite the log base 2 as a logarithm of any other base. Since our calculators can evaluate the natural log, we might choose to use the natural logarithm, which is the log base e. log^{2}(10) =  ln(10) _ ln(2)  Apply the change of base formula using base e.

Use a calculator to evaluate to 4 decimal places.

**Try It #14**
Evaluate log^{5}(100) using the change-of-base formula. > Access this online resource for additional instruction and practice with laws of logarithms. • The Properties of Logarithms (http://openstaxcollege.org/l/proplog) • Expand Logarithmic Expressions (http://openstaxcollege.org/l/expandlog) • Evaluate a Natural Logarithmic Expression (http://openstaxcollege.org/l/evaluatelog)


## 4.5 Section Exercises

### 4.5 section EXERCISES
Verbal 1. How does the power rule for logarithms help when solving logarithms with the form logb( n \sqrt{x} )? 2. What does the change-of-base formula do? Why is it useful when using a calculator? Algebraic For the following exercises, expand each logarithm as much as possible. Rewrite each expression as a sum, difference, or product of logs. 3. logb(7x \cdot  2y) 4. ln(3ab \cdot  5c) 5. logb   13 _ 17   6. log^{4}    x __ z 

_ w   7. ln   1 _ 4k   8. log^{2}(yx) For the following exercises, condense to a single logarithm if possible. 9. ln(7) + ln(x) + ln(y) 10. log^{3}(2) + log^{3}(a) + log^{3}(11) + log^{3}(b) 11. logb(28) - logb(7) 12. ln(a) - ln(d) - ln(c) 13. -logb  1 _ 7   _ 3 ln(8) For the following exercises, use the properties of logarithms to expand each logarithm as much as possible. Rewrite each expression as a sum, difference, or product of logs. 15. log   x^{1}5 y^{1}3 _ z^{1}9   16. ln   a-2 _ b-4 c^{5}   17. log(\sqrt{x^{3}} y-4 ) 18. ln  y\sqrt{_____}

 y _ 1 - y    19. log(x 2 y 3  \sqrt{x^{2}} y^{5} ) For the following exercises, condense each expression to a single logarithm using the properties of logarithms. 20. log(2x^{4}) + log(3x^{5}) 21. ln(6x^{9}) - ln(3x^{2}) 22. 2log(x) + 3log(x + 1) 23. log(x) - 1 _ 2 log(y) + 3log(z) 24. 4log^{7} (c) +  log^{7}(a) _  +  log^{7}(b) _  For the following exercises, rewrite each expression as an equivalent ratio of logs using the indicated base. 25. log^{7}(15) to base e For the following exercises, suppose log^{5} (6) = a and log^{5} (11) = b. Use the change-of-base formula along with properties of logarithms to rewrite each expression in terms of a and b. Show the steps for solving. _ 11   Numeric For the following exercises, use properties of logarithms to evaluate without using a calculator. 30. log^{3}   1 _ 9   - 3log^{3} (3) _ 3log^{8}(4)  32. 2log^{9}(3) - 4log^{9}(3) + log^{9}   1 _ For the following exercises, use the change-of-base formula to evaluate each expression as a quotient of natural logs. Use a calculator to approximate each to five decimal places. _ 2   37. log  1 Extensions 38. Use the product rule for logarithms to find all x values such that log^{1}2(2x + 6) + log^{1}2(x + 2) = 2. Show the steps for solving. 39. Use the quotient rule for logarithms to find all x values such that log^{6}(x + 2) - log^{6} (x - 3) = 1. Show the steps for solving. 40. Can the power property of logarithms be derived from the power property of exponents using the equation b x = m? If not, explain why. If so, show the derivation. 41. Prove that logb (n) =  _ logn(b)  for any positive integers b > 1 and n > 1. 42. Does log^{8}1(2401) = log^{3}(7)? Verify the claim algebraically.

Learning Objectives
In this section, you will:
• Use like bases to solve exponential equations.
• Use logarithms to solve exponential equations.
• Use the definition of a logarithm to solve logarithmic equations.
• Use the one-to-one property of logarithms to solve logarithmic equations.
• Solve applied problems involving exponential and logarithmic equations.

## 4.6 Exponential and Logarithmic Equations
In 1859, an Australian landowner named Thomas Austin released 24 rabbits into the wild for hunting. Because Australia had few predators and ample food, the rabbit population exploded. In fewer than ten years, the rabbit population numbered in the millions. Uncontrolled population growth, as in the wild rabbits in Australia, can be modeled with exponential functions. Equations resulting from those exponential functions can be solved to analyze and make predictions about exponential growth. In this section, we will learn techniques for solving exponential functions. Using Like Bases to Solve Exponential Equations The first technique involves two functions with like bases. Recall that the one-to-one property of exponential functions tells us that, for any real numbers b, S, and T, where b > 0, b \neq  1, bS = bT if and only if S = T. In other words, when an exponential equation has the same base on each side, the exponents must be equal. This also applies when the exponents are algebraic expressions. Therefore, we can solve many exponential equations by using the rules of exponents to rewrite each side as a power with the same base. Then, we use the fact that exponential functions are one-to-one to set the exponents equal to one another, and solve for the unknown. For example, consider the equation 34x - 7 =  32x _ 3 . To solve for x, we use the division property of exponents to rewrite the right side so that both sides have the common base, 3. Then we apply the one-to-one property of exponents by setting the exponents equal to one another and solving for x :

34x - 7 =  32x ___ 3 

34x - 7 =  32x ___ 31  Rewrite 3 as 31.

Use the division property of exponents.

4x - 7 = 2x - 1 Apply the one-to-one property of exponents.

2x = 6 Subtract 2x and add 7 to both sides.

x = 3 Divide by 3.

using the one-to-one property of exponential functions to solve exponential equations For any algebraic expressions S and T, and any positive real number b \neq  1, bS = bT if and only if S = T

**How To…**
Given an exponential equation with the form bS = bT, where S and T are algebraic expressions with an unknown, solve for the unknown. 1. Use the rules of exponents to simplify, if necessary, so that the resulting equation has the form bS = bT. 2. Use the one-to-one property to set the exponents equal. 3. Solve the resulting equation, S = T, for the unknown.

**Example  1**

### Solving an Exponential Equation with a Common Base
Solve 2x - 1 = 22x - 4.

**Solution**
2x - 1 = 22x - 4 The common base is 2.

x - 1 = 2x - 4 By the one-to-one property the exponents must be equal.

x = 3 Solve for x.

**Try It #1**
Solve 52x = 53x + 2. Rewriting Equations So All Powers Have the Same Base Sometimes the common base for an exponential equation is not explicitly shown. In these cases, we simply rewrite the terms in the equation as powers with a common base, and solve using the one-to-one property. For example, consider the equation 256 = 4x - 5. We can rewrite both sides of this equation as a power of 2. Then we apply the rules of exponents, along with the one-to-one property, to solve for x :

Rewrite each side as a power with base 2.

Use the one-to-one property of exponents.

Apply the one-to-one property of exponents.

Add 10 to both sides.

x = 9 Divide by 2.

**How To…**
Given an exponential equation with unlike bases, use the one-to-one property to solve it. 1. Rewrite each side in the equation as a power with a common base. 2. Use the rules of exponents to simplify, if necessary, so that the resulting equation has the form bS = bT. 3. Use the one-to-one property to set the exponents equal. 4. Solve the resulting equation, S = T, for the unknown.

**Example  2**

### Solving Equations by Rewriting Them to Have a Common Base
Solve 8x + 2 = 16x + 1.

**Solution**
8x + 2 = 16x + 1

(23)x + 2 = (24)x + 1 Write 8 and 16 as powers of 2.

To take a power of a power, multiply exponents .

3x + 6 = 4x + 4 Use the one-to-one property to set the exponents equal.

x = 2 Solve for x.


**Try It #2**
Solve 52x = 253x + 2.

**Example  3**
Solving Equations by Rewriting Roots with Fractional Exponents to Have a Common Base Solve 25x = \sqrt{2} .

**Solution**
25x = 2  1 __ 2  Write the square root of 2 as a power of 2.

5x =  1 __ 2  Use the one-to-one property.

x =  1 __ 10  Solve for x.

**Try It #3**
Solve 5x = \sqrt{5} . Do all exponential equations have a solution? If not, how can we tell if there is a solution during the problem- solving process? No. Recall that the range of an exponential function is always positive. While solving the equation, we may obtain an expression that is undefined.

**Example  4**

### Solving an Equation with Positive and Negative Powers
Solve 3x + 1 = -2. Solution This equation has no solution. There is no real value of x that will make the equation a true statement because any power of a positive number is positive. Analysis Figure 2 shows that the two graphs do not cross so the left side is never equal to the right side. Thus the equation has no solution. x y Tey do not cross. y = -2 y = 3x + 1

**Try It #4**
Solve 2x = -100. Solving Exponential Equations Using Logarithms Sometimes the terms of an exponential equation cannot be rewritten with a common base. In these cases, we solve by taking the logarithm of each side. Recall, since log(a) = log(b) is equivalent to a = b, we may apply logarithms with the same base on both sides of an exponential equation.


**How To…**
Given an exponential equation in which a common base cannot be found, solve for the unknown. 1. Apply the logarithm of both sides of the equation. a. If one of the terms in the equation has base 10, use the common logarithm. b. If none of the terms in the equation has base 10, use the natural logarithm. 2. Use the rules of logarithms to solve for the unknown.

**Example  5**

### Solving an Equation Containing Powers of Different Bases
Solve 5x + 2 = 4x.

**Solution**
5x + 2 = 4x There is no easy way to get the powers to have the same base .

ln(5x + 2) = ln(4x) Take ln of both sides.

(x + 2)ln(5) = xln(4) Use laws of logs.

xln(5) + 2ln(5) = xln(4) Use the distributive law.

xln(5) - xln(4) = - 2ln(5) Get terms containing x on one side, terms without x on the other.

x(ln(5) - ln(4)) = - 2ln(5) On the left hand side, factor out an x.

xln   5 __ 4   = ln   1 __ 25   Use the laws of logs.

x =  ln  1 __ 25   _ ln  5 __ 4    Divide by the coefficient of x.

**Try It #5**
Solve 2x = 3x + 1. Is there any way to solve 2x = 3x? Yes. The solution is 0. Equations Containing e One common type of exponential equations are those with base e. This constant occurs again and again in nature, in mathematics, in science, in engineering, and in finance. When we have an equation with a base e on either side, we can use the natural logarithm to solve it.

**How To…**
Given an equation of the form y = Aekt, solve for t. 1. Divide both sides of the equation by A. 2. Apply the natural logarithm of both sides of the equation. 3. Divide both sides of the equation by k.

**Example  6**
Solve an Equation of the Form y = Ae k t

**Solution**

5 = e 2t Divide by the coefficient of the power .

ln(5) = 2t Take ln of both sides. Use the fact that ln(x) and e x are inverse functions.

t =  ln(5) ___ 2  Divide by the coefficient of t.

Analysis Using laws of logs, we can also write this answer in the form t = ln\sqrt{5} . If we want a decimal approximation of the answer, we use a calculator.

**Try It #6**
Does every equation of the form y = Aekt have a solution? No. There is a solution when k \neq  0, and when y and A are either both 0 or neither 0, and they have the same sign. An example of an equation with this form that has no solution is 2 = -3et.

**Example  7**

### Solving an Equation That Can Be Simplified to the Form y = Ae k t
Solve 4e^{2}x + 5 = 12.

**Solution**

Combine like terms.

e^{2}x =  7 __ 4  Divide by the coefficient of the power.

2x = ln   7 __ 4   Take ln of both sides.

x =  1 __ 2  ln   7 __ 4   Solve for x.

**Try It #7**
Solve 3 + e^{2}t = 7e^{2}t. Extraneous Solutions Sometimes the methods used to solve an equation introduce an extraneous solution, which is a solution that is correct algebraically but does not satisfy the conditions of the original equation. One such situation arises in solving when the logarithm is taken on both sides of the equation. In such cases, remember that the argument of the logarithm must be positive. If the number we are evaluating in a logarithm function is negative, there is no output.

**Example  8**

### Solving Exponential Functions in Quadratic Form
Solve e^{2}x - e x = 56.

**Solution**

e 2x - e x = 56

e 2x - e x - 56 = 0 Get one side of the equation equal to zero.

(e x + 7)(e x - 8) = 0 Factor by the FOIL method.

e x + 7 = 0 or e x - 8 = 0 If a product is zero, then one factor must be zero.

e x = -7 or e x = 8 Isolate the exponentials.

e x = 8 Reject the equation in which the power equals a negative number.

x = ln(8) Solve the equation in which the power equals a positive number. Analysis When we plan to use factoring to solve a problem, we always get zero on one side of the equation, because zero has the unique property that when a product is zero, one or both of the factors must be zero. We reject the equation e x = -7 because a positive number never equals a negative number. The solution ln(-7) is not a real number, and in the real number system this solution is rejected as an extraneous solution.


**Try It #8**
Solve e^{2}x = e x + 2. Does every logarithmic equation have a solution? No. Keep in mind that we can only apply the logarithm to a positive number. Always check for extraneous solutions. Using the Definition of a Logarithm to Solve Logarithmic Equations We have already seen that every logarithmic equation logb(x) = y is equivalent to the exponential equation b y = x. We can use this fact, along with the rules of logarithms, to solve logarithmic equations where the argument is an algebraic expression. For example, consider the equation log^{2}(2) + log^{2}(3x - 5) = 3. To solve this equation, we can use rules of logarithms to rewrite the left side in compact form and then apply the definition of logs to solve for x:

log^{2}(2) + log^{2}(3x - 5) = 3

log^{2}(2(3x - 5)) = 3 Apply the product rule of logarithms.

log^{2}(6x - 10) = 3 Distribute.

Apply the definition of a logarithm.

Calculate 23.

Add 10 to both sides.

x = 3 Divide by 6. using the definition of a logarithm to solve logarithmic equations For any algebraic expression S and real numbers b and c, where b > 0, b \neq  1, logb(S) = c if and only if b c = S

**Example  9**
Using Algebra to Solve a Logarithmic Equation Solve 2ln(x) + 3 = 7.

**Solution**
2ln(x) + 3 = 7

2ln(x) = 4 Subtract 3.

ln(x) = 2 Divide by 2.

x = e^{2} Rewrite in exponential form.

**Try It #9**
Solve 6 + ln(x) = 10.

**Example  10**
Using Algebra Before and After Using the Definition of the Natural Logarithm Solve 2ln(6x) = 7.

**Solution**
2ln(6x) = 7

ln(6x) =  7 __ 2  Divide by 2.

6x = e  7 __ 2  Use the definition of ln.

x = 1 __ 6 e  7 __ 2  Divide by 6.


**Try It #10**
Solve 2ln(x + 1) = 10.

**Example  11**
Using a Graph to Understand the Solution to a Logarithmic Equation Solve ln(x) = 3.

**Solution**
ln(x) = 3

x = e 3 Use the definition of the natural logarithm. intersect is close to 20. In other words e^{3} ≈ 20. A calculator gives a better approximation: e^{3} ≈ 20.0855. x y y = 3 y = 1n(x)

**Try It #11**
Use a graphing calculator to estimate the approximate solution to the logarithmic equation 2x = 1000 to 2 decimal places. Using the One-to-One Property of Logarithms to Solve Logarithmic Equations As with exponential equations, we can use the one-to-one property to solve logarithmic equations. The one-to-one property of logarithmic functions tells us that, for any real numbers x > 0, S > 0, T > 0 and any positive real number b, where b \neq  1, logb(S) = logb(T) if and only if S = T. For example, If log^{2}(x - 1) = log^{2}(8), then x - 1 = 8. So, if x - 1 = 8, then we can solve for x, and we get x = 9. To check, we can substitute x = 9 into the original equation: log^{2}(9 - 1) = log^{2}(8) = 3. In other words, when a logarithmic equation has the same base on each side, the arguments must be equal. This also applies when the arguments are algebraic expressions. Therefore, when given an equation with logs of the same base on each side, we can use rules of logarithms to rewrite each side as a single logarithm. Then we use the fact that logarithmic functions are one-to-one to set the arguments equal to one another and solve for the unknown. For example, consider the equation log(3x - 2) - log(2) = log(x + 4). To solve this equation, we can use the rules of logarithms to rewrite the left side as a single logarithm, and then apply the one-to-one property to solve for x:

log(3x - 2) - log(2) = log(x + 4)

log   3x - 2 ______   = log(x + 4) Apply the quotient rule of logarithms.

 3x - 2 ______  = x + 4 Apply the one to one property of a logarithm.

3x - 2 = 2x + 8 Multiply both sides of the equation by 2.

x = 10 Subtract 2x and add 2.

To check the result, substitute x = 10 into log(3x - 2) - log(2) = log(x + 4).

log(3(10) - 2) - log(2) = log((10) + 4)

log(28) - log(2) = log(14)

log   28 __ 2   = log(14) The solution checks. using the one-to-one property of logarithms to solve logarithmic equations For any algebraic expressions S and T and any positive real number b, where b \neq  1, logb(S) = logb(T) if and only if S = T Note, when solving an equation involving logarithms, always check to see if the answer is correct or if it is an extraneous solution.

**How To…**
Given an equation containing logarithms, solve it using the one-to-one property. 1. Use the rules of logarithms to combine like terms, if necessary, so that the resulting equation has the form logbS = logbT. 2. Use the one-to-one property to set the arguments equal. 3. Solve the resulting equation, S = T, for the unknown.

**Example  12**

### Solving an Equation Using the One-to-One Property of Logarithms
Solve ln(x^{2}) = ln(2x + 3).

**Solution**

ln(x^{2}) = ln(2x + 3)

x^{2} = 2x + 3 Use the one-to-one property of the logarithm.

x^{2} - 2x - 3 = 0 Get zero on one side before factoring.

(x - 3)(x + 1) = 0 Factor using FOIL.

x - 3 = 0 or x + 1 = 0 If a product is zero, one of the factors must be zero.

x = 3 or x = -1 Solve for x. Analysis There are two solutions: 3 or -1. The solution -1 is negative, but it checks when substituted into the original equation because the argument of the logarithm functions is still positive.

**Try It #12**
Solve ln(x^{2}) = ln(1). Solving Applied Problems Using Exponential and Logarithmic Equations In previous sections, we learned the properties and rules for both exponential and logarithmic functions. We have seen that any exponential function can be written as a logarithmic function and vice versa. We have used exponents to solve logarithmic equations and logarithms to solve exponential equations. We are now ready to combine our skills to solve equations that model real-world situations, whether the unknown is in an exponent or in the argument of a logarithm. One such application is in science, in calculating the time it takes for half of the unstable material in a sample of a radioactive substance to decay, called its half-life. Table 1 lists the half-life for several of the more common radioactive substances.

Substance Use Half-life gallium-67 nuclear medicine 80 hours cobalt-60 manufacturing 5.3 years technetium-99m nuclear medicine 6 hours americium-241 construction 432 years carbon-14 archeological dating uranium-235 atomic power We can see how widely the half-lives for these substances vary. Knowing the half-life of a substance allows us to calculate the amount remaining after a specified time. We can use the formula for radioactive decay:

A(t) = A^{0}e  ln(0.5) _____ T t

A(t) = A^{0}e ln(0.5)  t __ T  

A(t) = A^{0}(e ln(0.5))  t _ T 

A(t) = A^{0}  1 __ 2    t _ T  where • A^{0} is the amount initially present • T is the half-life of the substance • t is the time period over which the substance is studied • y is the amount of the substance present after time t

**Example  13**
Using the Formula for Radioactive Decay to Find the Quantity of a Substance How long will it take for ten percent of a 1,000-gram sample of uranium-235 to decay?

**Solution**
y = 1000e   __________

 __________ After 10% decays, 900 grams are left.

0.9 = e   __________ Divide by 1000.

ln(0.9) = ln  e   __________ Take ln of both sides.

ln(0.9) =  __ ln(eM) = M

_ ln(0.5) years Solve for t.

Analysis Ten percent of 1,000 grams is 100 grams. If 100 grams decay, the amount of uranium-235 remaining is 900 grams.

**Try It #13**
How long will it take before twenty percent of our 1,000-gram sample of uranium-235 has decayed? Access these online resources for additional instruction and practice with exponential and logarithmic equations. • Solving Logarithmic Equations (http://openstaxcollege.org/l/solvelogeq) • Solving Exponential Equations with Logarithms (http://openstaxcollege.org/l/solveexplog)


## 4.6 Section Exercises
4.6 Section EXERCISES Verbal 1. How can an exponential equation be solved? 2. When does an extraneous solution occur? How can an extraneous solution be recognized? 3. When can the one-to-one property of logarithms be used to solve an equation? When can it not be used? Algebraic For the following exercises, use like bases to solve the exponential equation. _ 4  = 2n + 2 _ _ 64   3n For the following exercises, use logarithms to solve. 21. e 2x - e x - 132 = 0 27. e 2x - e x - 6 = 0 For the following exercises, use the definition of a logarithm to rewrite the equation as an exponential equation. 29. log   1 _ 100   = -2 _ 2  For the following exercises, use the definition of a logarithm to solve the equation. 33. 4 + log^{2}(9k) = 2 For the following exercises, use the one-to-one property of logarithms to solve. 36. ln(10 - 3x) = ln(-4x) 37. log^{1}3(5n - 2) = log^{1}3(8 - 5n) 38. log(x + 3) - log(x) = log(74) 39. ln(-3x) = ln(x^{2} - 6x) 40. log^{4}(6 - m) = log^{4}3(m) 41. ln(x - 2) - ln(x) = ln(54) 42. log^{9}(2n^{2} - 14n)= log^{9}(-45 + n^{2}) 43. ln(x^{2} - 10) + ln(9) = ln(10) For the following exercises, solve each equation for x. 44. log(x + 12) = log(x) + log(12) 45. ln(x) + ln(x - 3) = ln(7x) 46. log^{2}(7x + 6) = 3 47. ln(7) + ln(2 - 4x^{2}) = ln(14) 48. log^{8}(x + 6) - log^{8}(x) = log^{8}(58) 49. ln(3) - ln(3 - 3x) = ln(4) 50. log^{3}(3x) - log^{3}(6) = log^{3}(77) GRAPHICAL For the following exercises, solve the equation for x, if there is a solution. Then graph both sides of the equation, and observe the point of intersection (if it exists) to verify the solution. 51. log^{9}(x) - 5 = -4 52. log^{3}(x) + 3 = 2 53. ln(3x) = 2 54. ln(x - 5) = 1 55. log(4) + log(-5x) = 2 56. -7 + log^{3} (4 - x) = -6 57. ln(4x - 10) - 6 = -5 58. log(4 - 2x) = log(-4x) 59. log^{1}1(-2x^{2} - 7x) = log^{1}1(x - 2) 60. ln(2x + 9) = ln(-5x) 61. log^{9}(3 - x) = log^{9}(4x - 8) 62. log(x^{2} + 13) = log(7x + 3) 63.  _ log^{2}(10)  - log(x - 9) = log(44) 64. ln(x) - ln(x + 3) = ln(6)

For the following exercises, solve for the indicated value, and graph the situation showing the solution point. 65. An account with an initial deposit of $6,500 earns 7.25% annual interest, compounded continuously. How much will the account be worth after 20 years? 66. The formula for measuring sound intensity in decibels D is defined by the equation D = 10 log   I __ I^{0}  , where I is the intensity of the sound in watts per square meter and I^{0} = 10-12 is the lowest level of sound that the average person can hear. How many decibels are emitted from a jet plane with a sound intensity of 8.3 ⋅ 102 watts per square meter? 67. The population of a small town is modeled by the equation P = 1650e^{0}.5t where t is measured in years. In approximately how many years will the town’s population reach 20,000? Technology For the following exercises, solve each equation by rewriting the exponential expression using the indicated logarithm. Then use a calculator to approximate the variable to 3 decimal places. 69. e^{5}x = 17 using the natural log 70. 3(1.04)^{3}t = 8 using the common log 71. 34x - 5 = 38 using the common log 72. 50e-0.12t = 10 using the natural log For the following exercises, use a calculator to solve the equation. Unless indicated otherwise, round all answers to the nearest ten-thousandth.

75. log(-0.7x - 9) = 1 + 5log(5) 76. Atmospheric pressure P in pounds per square inch is represented by the formula P = 14.7e-0.21x, where x is the number of miles above sea level. To the nearest foot, how high is the peak of a mountain with an atmospheric pressure of 8.369 pounds per square inch? (Hint: there are 5,280 feet in a mile) 77. The magnitude M of an earthquake is represented by the equation M =  2 _ 3  log   E __ E^{0}   where E is the amount of energy released by the earthquake in joules and E^{0} = 104.4 is the assigned minimal measure released by an earthquake. To the nearest hundredth, what would the magnitude be of an earthquake releasing 1.4 \cdot  1013 joules of energy? Extensions 78. Use the definition of a logarithm along with the one- to-one property of logarithms to prove that blogb x = x. 79. Recall the formula for continually compounding interest, y = Ae kt. Use the definition of a logarithm along with properties of logarithms to solve the formula for time t such that t is equal to a single logarithm. 80. Recall the compound interest formula A = a  1 +  r _ k   kt. Use the definition of a logarithm along with properties of logarithms to solve the formula for time t. 81. Newton’s Law of Cooling states that the temperature T of an object at any time t can be described by the equation T = Ts + (T^{0} - Ts)e-kt, where Ts is the temperature of the surrounding environment, T^{0} is the initial temperature of the object, and k is the cooling rate. Use the definition of a logarithm along with properties of logarithms to solve the formula for time t such that t is equal to a single logarithm.


## 4.7 Exponential and Logarithmic Models
Learning Objectives
In this section, you will:
• Model exponential growth and decay.
• Use Newton’s Law of Cooling.
• Use logistic-growth models.
• Choose an appropriate model for data.
• Express an exponential model in base e.
We have already explored some basic applications of exponential and logarithmic functions. In this section, we explore some important applications in more depth, including radioactive isotopes and Newton’s Law of Cooling. Modeling Exponential Growth and Decay In real-world applications, we need to model the behavior of a function. In mathematical modeling, we choose a familiar general function with properties that suggest that it will model the real-world phenomenon we wish to analyze. In the case of rapid growth, we may choose the exponential growth function: y = A^{0}e kt where A^{0} is equal to the value at time zero, e is Euler’s constant, and k is a positive constant that determines the rate (percentage) of growth. We may use the exponential growth function in applications involving doubling time, the time it takes for a quantity to double. Such phenomena as wildlife populations, financial investments, biological samples, and natural resources may exhibit growth based on a doubling time. In some applications, however, as we will see when we discuss the logistic equation, the logistic model sometimes fits the data better than the exponential model. On the other hand, if a quantity is falling rapidly toward zero, without ever reaching zero, then we should probably choose the exponential decay model. Again, we have the form y = A^{0}e kt where A^{0} is the starting value, and e is Euler’s constant. Now k is a negative constant that determines the rate of decay. We may use the exponential decay model when we are calculating half-life, or the time it takes for a substance to exponentially decay to half of its original quantity. We use half-life in applications involving radioactive isotopes.

In our choice of a function to serve as a mathematical model, we often use data points gathered by careful observation and measurement to construct points on a graph and hope we can recognize the shape of the graph. Exponential growth and decay graphs have a distinctive shape, as we can see in Figure 2 and Figure 3. It is important to remember that, although parts of each of the two graphs seem to lie on the x-axis, they are really a tiny distance above the x-axis. y = 2e^{3}x x y -1 e 3 2e y = 0 growth. The equation is y = 2e 3x. x y -1 2 3e y = 3e-2x y = 0 e decay. The equation is y = 3e -2x. Exponential growth and decay often involve very large or very small numbers. To describe these numbers, we often use orders of magnitude. The order of magnitude is the power of ten, when the number is expressed in scientific notation, with one digit to the left of the decimal. For example, the distance to the nearest star, Proxima Centauri, measured in kilometers, is 40,113,497,200,000 kilometers. Expressed in scientific notation, this is 4.01134972 \times  1013. So, we could describe this number as having order of magnitude 1013. characteristics of the exponential function, y = A^{0}e kt An exponential function with the form y = A^{0}e kt has the following characteristics: • one-to-one function • horizontal asymptote: y = 0 • domain: ( –\infty , \infty ) • range: (0, \infty ) • x-intercept: none • y-intercept: (0, A^{0}) • increasing if k > 0 (see Figure 4) • decreasing if k < 0 (see Figure 4) t t y y y = 0 y = 0 y = A^{0}ekt k > 0 y = A^{0}ekt k < 0 ( ) k , A^{0}e ( ) k , A^{0}e ( ) k A^{0} e ( ) k A^{0} e when k > 0 and exponential decay when k < 0.

**Example  1**

### Graphing Exponential Growth
A population of bacteria doubles every hour. If the culture started with 10 bacteria, graph the population as a function of time. Solution When an amount grows at a fixed percent per unit time, the growth is exponential. To find A^{0} we use the fact that A^{0} is the amount at time zero, so A^{0} = 10. To find k, use the fact that after one hour (t = 1) the population doubles from 10 to 20. The formula is derived as follows

2 = e k Divide by 10

ln^{2} = k Take the natural logarithm so k = ln(2). Thus the equation we want to graph is y = 10e(ln^{2})t = 10(eln^{2})t = 10 \cdot  2t. The graph is shown in Figure 5.

t y y = 10e(ln 2)t Analysis The population of bacteria after ten hours is 10,240. We could describe this amount is being of the order of magnitude 104. The population of bacteria after twenty hours is 10,485,760 which is of the order of magnitude 10 7, so we could say that the population has increased by three orders of magnitude in ten hours. Half-Life We now turn to exponential decay. One of the common terms associated with exponential decay, as stated above, is half-life, the length of time it takes an exponentially decaying quantity to decrease to half its original amount. Every radioactive isotope has a half-life, and the process describing the exponential decay of an isotope is called radioactive decay. To find the half-life of a function describing exponential decay, solve the following equation:  1 __ 2 A^{0} = A^{0}e kt We find that the half-life depends only on the constant k and not on the starting quantity A^{0}. The formula is derived as follows

 1 __ 2 A^{0} = A^{0}e kt

 1 __ 2  = e kt Divide by A^{0}.

ln 1 __ 2  = kt Take the natural log.

- ln(2) = kt Apply laws of logarithms.

-  ln(2) ____ k  = t Divide by k. Since t, the time, is positive, k must, as expected, be negative. This gives us the half-life formula

t = -  ln(2) ____ k 

**How To…**
Given the half-life, find the decay rate. 1. Write A = A^{0} ekt. 2. Replace A by  1 _ 2 A^{0} and replace t by the given half-life. 3. Solve to find k. Express k as an exact value (do not round). Note: It is also possible to find the decay rate using k = -  ln(2) _ t .


**Example  2**
Finding the Function that Describes Radioactive Decay The half-life of carbon-14 is 5,730 years. Express the amount of carbon-14 remaining as a function of time, t. Solution This formula is derived as follows.

A = A^{0}e kt The continuous growth formula.

Substitute the half-life for t and 0.5A^{0} for f(t).

Divide by A^{0}.

Take the natural log of both sides.

k =  ln(0.5) ______ Divide by the coefficient of k.

A = A^{0}e    ln(0.5) ______ 5730  t Substitute for k in the continuous growth formula. The function that describes this continuous decay is f(t) = A^{0}e    ln(0.5) ______ 5730  t. We observe that the coefficient of t,  ln(0.5) _ 5730  ≈ -1.2097 is negative, as expected in the case of exponential decay.

**Try It #14**
The half-life of plutonium-244 is 80,000,000 years. Find function gives the amount of carbon-14 remaining as a function of time, measured in years. Radiocarbon Dating The formula for radioactive decay is important in radiocarbon dating, which is used to calculate the approximate date a plant or animal died. Radiocarbon dating was discovered in 1949 by Willard Libb y, who won a Nobel Prize for his discovery. It compares the difference between the ratio of two isotopes of carbon in an organic artifact or fossil to the ratio of those two isotopes in the air. It is believed to be accurate to within about 1% error for plants or animals that died within the last 60,000 years. Carbon-14 is a radioactive isotope of carbon that has a half-life of 5,730 years. It occurs in small quantities in the carbon dioxide in the air we breathe. Most of the carbon on earth is carbon-12, which has an atomic weight of 12 and is not radioactive. Scientists have determined the ratio of carbon-14 to carbon-12 in the air for the last 60,000 years, using tree rings and other organic samples of known dates—although the ratio has changed slightly over the centuries. As long as a plant or animal is alive, the ratio of the two isotopes of carbon in its body is close to the ratio in the atmosphere. When it dies, the carbon-14 in its body decays and is not replaced. By comparing the ratio of carbon-14 to carbon-12 in a decaying sample to the known ratio in the atmosphere, the date the plant or animal died can be approximated. Since the half-life of carbon-14 is 5,730 years, the formula for the amount of carbon-14 remaining after t years is

A ≈ A^{0}e    ln(0.5) ______ 5730  t where • A is the amount of carbon-14 remaining • A^{0} is the amount of carbon-14 when the plant or animal began decaying. This formula is derived as follows:

A = A^{0}e kt The continuous growth formula.

Substitute the half-life for t and 0.5A^{0} for f (t).

Divide by A^{0}.

Take the natural log of both sides.

k =  ln(0.5) ______ Divide by the coefficient of k.

A = A^{0}e    ln(0.5) ______ 5730  t Substitute for r in the continuous growth formula. To find the age of an object, we solve this equation for t:

t =  ln  A _ A^{0}   _

Out of necessity, we neglect here the many details that a scientist takes into consideration when doing carbon-14 dating, and we only look at the basic formula. The ratio of carbon-14 to carbon-12 in the atmosphere is approximately 0.0000000001%. Let r be the ratio of carbon-14 to carbon-12 in the organic artifact or fossil to be dated, determined by a method called liquid scintillation. From the equation A ≈ A^{0}e-0.000121t we know the ratio of the percentage of carbon-14 in the object we are dating to the percentage of carbon-14 in the atmosphere is r =  A __ A^{0} this equation for t, to get

t =  ln(r) _

**How To…**
Given the percentage of carbon-14 in an object, determine its age. 1. Express the given percentage of carbon-14 as an equivalent decimal, k. 2. Substitute for k in the equation t =  ln(r) _________ -0.000121  and solve for the age, t.

**Example  3**
Finding the Age of a Bone A bone fragment is found that contains 20% of its original carbon-14. To the nearest year, how old is the bone? Solution We substitute 20% = 0.20 for k in the equation and solve for t :

t =  ln(r) _ Use the general form of the equation.

=  ln(0.20) _ Substitute for r.

Round to the nearest year. The bone fragment is about 13,301 years old. Analysis The instruments that measure the percentage of carbon-14 are extremely sensitive and, as we mention above, a scientist will need to do much more work than we did in order to be satisfied. Even so, carbon dating is only accurate to about 1%, so this age should be given as 13,301 years \pm  1% or 13,301 years \pm  133 years.

**Try It #15**
Cesium-137 has a half-life of about 30 years. If we begin with 200 mg of cesium-137, will it take more or less than 230 years until only 1 milligram remains? Calculating Doubling Time For decaying quantities, we determined how long it took for half of a substance to decay. For growing quantities, we might want to find out how long it takes for a quantity to double. As we mentioned above, the time it takes for a quantity to double is called the doubling time. Given the basic exponential growth equation A = A^{0}e kt, doubling time can be found by solving for when the original quantity has doubled, that is, by solving 2A^{0} = A^{0}e kt. The formula is derived as follows:

2A^{0} = A^{0}e kt

2 = e kt Divide by A^{0}.

ln(2) = kt Take the natural logarithm.

t =  ln(2) _ k  Divide by the coefficient of t. Thus the doubling time is

t =  ln(2) _ k 


**Example  4**
Finding a Function That Describes Exponential Growth According to Moore’s Law, the doubling time for the number of transistors that can be put on a computer chip is approximately two years. Give a function that describes this behavior. Solution The formula is derived as follows:

t =  ln(2) ___ k  The doubling time formula.

2 =  ln(2) ___ k  Use a doubling time of two years.

k =  ln(2) ___ 2  Multiply by k and divide by 2.

A = A^{0}e  ln(2) _____ 2 t Substitute k into the continuous growth formula. The function is A^{0}e  ln(2) _____ 2 t.

**Try It #16**
Recent data suggests that, as of 2013, the rate of growth predicted by Moore’s Law no longer holds. Growth has slowed to a doubling time of approximately three years. Find the new function that takes that longer doubling time into account. Using Newton’s Law of Cooling Exponential decay can also be applied to temperature. When a hot object is left in surrounding air that is at a lower temperature, the object’s temperature will decrease exponentially, leveling off as it approaches the surrounding air temperature. On a graph of the temperature function, the leveling off will correspond to a horizontal asymptote at the temperature of the surrounding air. Unless the room temperature is zero, this will correspond to a vertical shift of the generic exponential decay function. This translation leads to Newton’s Law of Cooling, the scientific formula for temperature as a function of time as an object’s temperature is equalized with the ambient temperature

T(t) = Ae kt + Ts This formula is derived as follows:

T(t) = Ab ct + Ts

T(t) = Ae ln(bct) + Ts Laws of logarithms.

T(t) = Ae ctln(b) + Ts Laws of logarithms.

T(t) = Ae kt + Ts Rename the constant cln(b), calling it k. Newton’s law of cooling The temperature of an object, T, in surrounding air with temperature Ts will behave according to the formula T(t) = Ae kt + Ts where • t is time • A is the difference between the initial temperature of the object and the surroundings • k is a constant, the continuous rate of cooling of the object

**How To…**
Given a set of conditions, apply Newton’s Law of Cooling. 1. Set Ts equal to the y-coordinate of the horizontal asymptote (usually the ambient temperature). 2. Substitute the given values into the continuous growth formula T(t) = Ae kt + Ts to find the parameters A and k. 3. Substitute in the desired time to find the temperature or the desired temperature to find the time.


**Example  5**
Using Newton’s Law of Cooling A cheesecake is taken out of the oven with an ideal internal temperature of 165°F, and is placed into a 35°F refrigerator. After 10 minutes, the cheesecake has cooled to 150°F. If we must wait until the cheesecake has cooled to 70°F before we eat it, how long will we have to wait? Solution Because the surrounding air temperature in the refrigerator is 35 degrees, the cheesecake’s temperature will decay exponentially toward 35, following the equation T(t) = Ae kt + 35 We know the initial temperature was 165, so T(0) = 165.

Substitute (0, 165).

Solve for A. We were given another data point, T(10) = 150, which we can use to solve for k.

Substitute (10, 150).

Subtract 35.

 115 ___ Divide by 130.

ln  115 ___ Take the natural log of both sides.

k =  ln  115 ___ _  ≈ -0.0123 Divide by the coefficient of k. This gives us the equation for the cooling of the cheesecake: T(t) = 130e -0.0123t + 35. Now we can solve for the time it will take for the temperature to cool to 70 degrees.

Substitute in 70 for T(t).

Subtract 35.

 35 ___ Divide by 130.

ln  35 ___ Take the natural log of both sides

t =  ln  35 ___ _ Divide by the coefficient of t. It will take about 107 minutes, or one hour and 47 minutes, for the cheesecake to cool to 70°F.

**Try It #17**
A pitcher of water at 40 degrees Fahrenheit is placed into a 70 degree room. One hour later, the temperature has risen to 45 degrees. How long will it take for the temperature to rise to 60 degrees? Using Logistic Growth Models Exponential growth cannot continue forever. Exponential models, while they may be useful in the short term, tend to fall apart the longer they continue. Consider an aspiring writer who writes a single line on day one and plans to double the number of lines she writes each day for a month. By the end of the month, she must write over 17 billion lines, or one-half-billion pages. It is impractical, if not impossible, for anyone to write that much in such a short period of time. Eventually, an exponential model must begin to approach some limiting value, and then the growth is forced to slow. For this reason, it is often better to use a model with an upper bound instead of an exponential growth model, though the exponential growth model is still useful over a short term, before approaching the limiting value.

The logistic growth model is approximately exponential at first, but it has a reduced rate of growth as the output approaches the model’s upper bound, called the carrying capacity. For constants a, b, and c, the logistic growth of a population over time x is represented by the model f (x) =  c _______ 1 + ae-b x  The graph in Figure 6 shows how the growth rate changes over time. The graph increases from left to right, but the growth rate only increases until it reaches its point of maximum growth rate, at which point the rate of increase decreases. x Initial value of population Point of maximum growth Carrying capacity f (x) f (x) = y = c ( ) c 1+a c 1 + ae–bx ( ) c ln(a) b , logistic growth The logistic growth model is f (x) =  c _ 1 + ae-b x  where •  c _____ 1 + a  is the initial value • c is the carrying capacity, or limiting value • b is a constant determined by the rate of growth.

**Example  6**
Using the Logistic-Growth Model An influenza epidemic spreads through a population rapidly, at a rate that depends on two factors: The more people who have the flu, the more rapidly it spreads, and also the more uninfected people there are, the more rapidly it spreads. These two factors make the logistic model a good one to study the spread of communicable diseases. And, clearly, there is a maximum value for the number of people infected: the entire population. For example, at time t = 0 there is one person in a community of 1,000 people who has the flu. So, in that community, at most 1,000 people can have the flu. Researchers find that for this particular strain of the flu, the logistic growth constant is b = 0.6030. Estimate the number of people in this community who will have had this flu after ten days. Predict how many people in this community will have had this flu after a long period of time has passed. Solution We substitute the given data into the logistic growth model f (x) =  c _______ 1 + ae-b x  Because at most 1,000 people, the entire population of the community, can get the flu, we know the limiting value is c = 1000. To find a, we use the formula that the number of cases at time t = 0 is  c _ 1 + a  = 1, from which it follows that a = 999. This model predicts that, after ten days, the number of people who have had the flu is f (x) =  ____________

the actual number must be a whole number (a person has either had the flu or not) we round to 294. In the long term, the number of people who will contract the flu is the limiting value, c = 1000. Analysis Remember that, because we are dealing with a virus, we cannot predict with certainty the number of people infected. The model only approximates the number of people infected and will not give us exact or actual values. The graph in

20 cases on day 5 1 case on day 0 294 cases on day 10 1,000 cases on day 21 Days Cases __


**Try It #18**
Using the model in Example 6, estimate the number of cases of flu on day 15. Choosing an Appropriate Model for Data Now that we have discussed various mathematical models, we need to learn how to choose the appropriate model for the raw data we have. Many factors influence the choice of a mathematical model, among which are experience, scientific laws, and patterns in the data itself. Not all data can be described by elementary functions. Sometimes, a function is chosen that approximates the data over a given interval. For instance, suppose data were gathered on the number of homes bought in the United States from the years 1960 to 2013. After plotting these data in a scatter plot, we notice that the shape of the data from the years 2000 to 2013 follow a logarithmic curve. We could restrict the interval from 2000 to 2010, apply regression analysis using a logarithmic model, and use it to predict the number of home buyers for the year 2015. Three kinds of functions that are often useful in mathematical models are linear functions, exponential functions, and logarithmic functions. If the data lies on a straight line, or seems to lie approximately along a straight line, a linear model may be best. If the data is non-linear, we often consider an exponential or logarithmic model, though other models, such as quadratic models, may also be considered. In choosing between an exponential model and a logarithmic model, we look at the way the data curves. This is called the concavity. If we draw a line between two data points, and all (or most) of the data between those two points lies above that line, we say the curve is concave down. We can think of it as a bowl that bends downward and therefore cannot hold water. If all (or most) of the data between those two points lies below the line, we say the curve is concave up. In this case, we can think of a bowl that bends upward and can therefore hold water. An exponential curve, whether rising or falling, whether representing growth or decay, is always concave up away from its horizontal asymptote. A logarithmic curve is always concave away from its vertical asymptote. In the case of positive data, which is the most common case, an exponential curve is always concave up, and a logarithmic curve always concave down. A logistic curve changes concavity. It starts out concave up and then changes to concave down beyond a certain point, called a point of inflection. After using the graph to help us choose a type of function to use as a model, we substitute points, and solve to find the parameters. We reduce round-off error by choosing points as far apart as possible.


**Example  7**
Choosing a Mathematical Model Does a linear, exponential, logarithmic, or logistic model best fit the values listed in Table 1? Find the model, and use a graph to check your choice. x y 1.386 2.197 2.773 3.219 3.584 3.892 4.159 4.394 Solution First, plot the data on a graph as in Figure 8. For the purpose of graphing, round the data to two significant digits. 0.5 1.5 2.5 3.5 4.5 5.5 y x Clearly, the points do not lie on a straight line, so we reject a linear model. If we draw a line between any two of the points, most or all of the points between those two points lie above the line, so the graph is concave down, suggesting a logarithmic model. We can try y = aln(b x). Plugging in the first point, (1,0), gives 0 = alnb. We reject the case that a = 0 (if it were, all outputs would be 0), so we know ln(b) = 0. Thus b = 1 and y = aln(x). Next we can use the point (9,4.394) to solve for a:

y = aln(x)

_____ ln(9)  Because a =  4.394 _ ln(9)  ≈ 2, an appropriate model for the data is y = 2ln(x). To check the accuracy of the model, we graph the function together with the given points as in Figure 9. 0.5 1.5 2.5 3.5 4.5 5.5 y x x = 0 y = 2 ln(x) We can conclude that the model is a good fit to the data. Compare Figure 9 to the graph of y = ln(x^{2}) shown in Figure 10.

0.5 1.5 2.5 3.5 4.5 5.5 y x x = 0 y = ln(x^{2}) The graphs appear to be identical when x > 0. A quick check confirms this conclusion: y = ln(x 2) = 2ln(x) for x > 0. However, if x < 0, the graph of y = ln(x 2) includes a “extra” branch, as shown in Figure 11. This occurs because, while y = 2ln(x) cannot have negative values in the domain (as such values would force the argument to be negative), the function y = ln(x 2) can have negative domain values. x y y = ln(x^{2})

**Try It #19**
Does a linear, exponential, or logarithmic model best fit the data in Table 2? Find the model. x y 3.297 5.437 8.963 Expressing an Exponential Model in Base e While powers and logarithms of any base can be used in modeling, the two most common bases are 10 and e. In science and mathematics, the base e is often preferred. We can use laws of exponents and laws of logarithms to change any base to base e.

**How To…**
Given a model with the form y = ab x, change it to the form y = A^{0}e kx. 1. Rewrite y = ab x as y = aeln(b x). 2. Use the power rule of logarithms to rewrite y as y = ae xln(b) = aeln(b)x. 3. Note that a = A^{0} and k = ln(b) in the equation y = A^{0}e kx.


**Example  8**
Changing to base e Change the function y = 2.5(3.1)x so that this same function is written in the form y = A^{0}e kx.

**Solution**
The formula is derived as follows

Insert exponential and its inverse.

Laws of logs.

Commutative law of multiplication

**Try It #20**
Change the function y = 3(0.5)x to one having e as the base.

Access these online resources for additional instruction and practice with exponential and logarithmic models. • Logarithm Application – pH (http://openstaxcollege.org/l/logph) • Exponential Model – Age Using Half-Life (http://openstaxcollege.org/l/expmodelhalf) • Newton’s Law of Cooling (http://openstaxcollege.org/l/newtoncooling) • Exponential Growth Given Doubling Time (http://openstaxcollege.org/l/expgrowthdbl) • Exponential Growth – Find Initial Amount Given Doubling Time (http://openstaxcollege.org/l/initialdouble)


## 4.7 Section Exercises

### 4.7 section EXERCISES
Verbal 1. With what kind of exponential model would half-life be associated? What role does half-life play in these models? 2. What is carbon dating? Why does it work? Give an example in which carbon dating would be useful. 3. With what kind of exponential model would doubling time be associated? What role does doubling time play in these models? 4. Define Newton’s Law of Cooling. Then name at least three real-world situations where Newton’s Law of Cooling would be applied. 5. What is an order of magnitude? Why are orders of magnitude useful? Give an example to explain. Numeric 6. The temperature of an object in degrees Fahrenheit after t minutes is represented by the equation T(t) = 68e-0.0174t + 72. To the nearest degree, what is the temperature of the object after one and a half hours? For the following exercises, use the logistic growth model f (x) =  _ 1 + 8e-2x . 7. Find and interpret f (0). Round to the nearest tenth. 8. Find and interpret f (4). Round to the nearest tenth. 9. Find the carrying capacity. 10. Graph the model. 11. Determine whether the data from the table could best be represented as a function that is linear, exponential, or logarithmic. Then write a formula for a model that represents the data. x 1.2 12. Rewrite f (x) = 1.68(0.65)x as an exponential equation with base e to five significant digits. Technology For the following exercises, enter the data from each table into a graphing calculator and graph the resulting scatter plots. Determine whether the data from the table could represent a function that is linear, exponential, or logarithmic. x f (x) 4.079 5.296 6.159 6.828 7.375 7.838 8.238 8.592 8.908 x f (x) 2.4 2.88 3.456 4.147 4.977 5.972 7.166 8.6 10.32 x f (x) 9.429 9.972 10.79 x 1.25 2.25 3.56 4.2 5.65 6.75 7.25 8.6 9.25 10.5 f (x) 5.75 8.75 12.68 14.6 18.95 22.25 23.75 27.8 29.75 33.5 For the following exercises, use a graphing calculator and this scenario: the population of a fish farm in t years is modeled by the equation P(t) =  _ 17. Graph the function. 18. What is the initial population of fish? 19. To the nearest tenth, what is the doubling time for the fish population? 20. To the nearest whole number, what will the fish population be after 2 years? 21. To the nearest tenth, how long will it take for the population to reach 900? 22. What is the carrying capacity for the fish population? Justify your answer using the graph of P.

Extensions 23. A substance has a half-life of 2.045 minutes. If the initial amount of the substance was 132.8 grams, how many half-lives will have passed before the substance decays to 8.3 grams? What is the total time of decay? 24. The formula for an increasing population is given by P(t) = P^{0}e rt where P^{0} is the initial population and r > 0. Derive a general formula for the time t it takes for the population to increase by a factor of M. 25. Recall the formula for calculating the magnitude of an earthquake, M =  2 _ 3 log   S __ S^{0}  . Show each step for solving this equation algebraically for the seismic moment S. 26. What is the y-intercept of the logistic growth model y =  c ________ 1 + ae-rx ? Show the steps for calculation. What does this point tell us about the population? 27. Prove that b x = e xln(b) for positive b \neq  1. Real-World Applications For the following exercises, use this scenario: A doctor prescribes 125 milligrams of a therapeutic drug that decays by about 30% each hour. 28. To the nearest hour, what is the half-life of the drug? 29. Write an exponential model representing the amount of the drug remaining in the patient’s system after t hours. Then use the formula to find the amount of the drug that would remain in the patient’s system after 3 hours. Round to the nearest milligram. 30. Using the model found in the previous exercise, find f (10) and interpret the result. Round to the nearest hundredth. For the following exercises, use this scenario: A tumor is injected with 0.5 grams of Iodine-125, which has a decay rate of 1.15% per day. 31. To the nearest day, how long will it take for half of the Iodine-125 to decay? 32. Write an exponential model representing the amount of Iodine-125 remaining in the tumor after t days. Then use the formula to find the amount of Iodine-125 that would remain in the tumor after 60 days. Round to the nearest tenth of a gram. 33. A scientist begins with 250 grams of a radioactive substance. After 250 minutes, the sample has decayed to 32 grams. Rounding to five significant digits, write an exponential equation representing this situation. To the nearest minute, what is the half-life of this substance? 34. The half-life of Radium-226 is 1590 years. What is the annual decay rate? Express the decimal result to four significant digits and the percentage to two significant digits. 35. The half-life of Erbium-165 is 10.4 hours. What is the hourly decay rate? Express the decimal result to four significant digits and the percentage to two significant digits. 36. A wooden artifact from an archeological dig contains 60 percent of the carbon-14 that is present in living trees. To the nearest year, about how many years old is the artifact? (The half-life of carbon-14 is 37. A research student is working with a culture of bacteria that doubles in size every twenty minutes. The initial population count was 1350 bacteria. Rounding to five significant digits, write an exponential equation representing this situation. To the nearest whole number, what is the population size after 3 hours?

For the following exercises, use this scenario: A biologist recorded a count of 360 bacteria present in a culture after 5 minutes and 1,000 bacteria present after 20 minutes. 38. To the nearest whole number, what was the initial population in the culture? 39. Rounding to six significant digits, write an exponential equation representing this situation. To the nearest minute, how long did it take the population to double? For the following exercises, use this scenario: A pot of boiling soup with an internal temperature of 100° Fahrenheit was taken off the stove to cool in a 69° F room. After fifteen minutes, the internal temperature of the soup was 95° F. 40. Use Newton’s Law of Cooling to write a formula that models this situation. 41. To the nearest minute, how long will it take the soup to cool to 80° F? 42. To the nearest degree, what will the temperature be after 2 and a half hours? For the following exercises, use this scenario: A turkey is taken out of the oven with an internal temperature of 165° Fahrenheit and is allowed to cool in a 75° F room. After half an hour, the internal temperature of the turkey is 145° F. 43. Write a formula that models this situation. 44. To the nearest degree, what will the temperature be after 50 minutes? 45. To the nearest minute, how long will it take the turkey to cool to 110° F? For the following exercises, find the value of the number shown on each logarithmic scale. Round all answers to the nearest thousandth. log (x) log (x) 48. Plot each set of approximate values of intensity of sounds on a logarithmic scale: Whisper: 10-10 W ___ m^{2} , Vacuum: 10-4 W ___ m^{2} , Jet: 102 W ___ m^{2}  49. Recall the formula for calculating the magnitude of an earthquake, M =  2 __ 3 log   S __ S^{0}  . One earthquake has magnitude 3.9 on the MMS scale. If a second earthquake has 750 times as much energy as the first, find the magnitude of the second quake. Round to the nearest hundredth. For the following exercises, use this scenario: The equation N(t) =  _ 1 + 49e-0.7t  models the number of people in a town who have heard a rumor after t days. 50. How many people started the rumor? 51. To the nearest whole number, how many people will have heard the rumor after 3 days? 52. As t increases without bound, what value does N(t) approach? Interpret your answer. For the following exercise, choose the correct answer choice. 53. A doctor and injects a patient with 13 milligrams of radioactive dye that decays exponentially. After 12 minutes, there are 4.75 milligrams of dye remaining in the patient’s system. Which is an appropriate model for this situation?

a. f (t) = 13(0.0805)t b. f (t) = 13e^{0}.9195t c. f (t) = 13e(-0.0839t) d. f (t) =  4.75 __________

Learning Objectives
In this section, you will:
• Build an exponential model from data.
• Build a logarithmic model from data.
• Build a logistic model from data.

## 4.8 Fitting Exponential Models to Data
In previous sections of this chapter, we were either given a function explicitly to graph or evaluate, or we were given a set of points that were guaranteed to lie on the curve. Then we used algebra to find the equation that fit the points exactly. In this section, we use a modeling technique called regression analysis to find a curve that models data collected from real-world observations. With regression analysis, we don’t expect all the points to lie perfectly on the curve. The idea is to find a model that best fits the data. Then we use the model to make predictions about future events. Do not be confused by the word model. In mathematics, we often use the terms function, equation, and model interchangeably, even though they each have their own formal definition. The term model is typically used to indicate that the equation or function approximates a real-world situation. We will concentrate on three types of regression models in this section: exponential, logarithmic, and logistic. Having already worked with each of these functions gives us an advantage. Knowing their formal definitions, the behavior of their graphs, and some of their real-world applications gives us the opportunity to deepen our understanding. As each regression model is presented, key features and definitions of its associated function are included for review. Take a moment to rethink each of these functions, reflect on the work we’ve done so far, and then explore the ways regression is used to model real-world phenomena. Building an Exponential Model from Data As we’ve learned, there are a multitude of situations that can be modeled by exponential functions, such as investment growth, radioactive decay, atmospheric pressure changes, and temperatures of a cooling object. What do these phenomena have in common? For one thing, all the models either increase or decrease as time moves forward. But that’s not the whole story. It’s the way data increase or decrease that helps us determine whether it is best modeled by an exponential equation. Knowing the behavior of exponential functions in general allows us to recognize when to use exponential regression, so let’s review exponential growth and decay. Recall that exponential functions have the form y = ab x or y = A^{0}e kx. When performing regression analysis, we use the form most commonly used on graphing utilities, y = ab x. Take a moment to reflect on the characteristics we’ve already learned about the exponential function y = ab x (assume a > 0): • b must be greater than zero and not equal to one. • The initial value of the model is y = a. • If b > 1, the function models exponential growth. As x increases, the outputs of the model increase slowly at first, but then increase more and more rapidly, without bound. • If 0 < b < 1, the function models exponential decay. As x increases, the outputs for the model decrease rapidly at first and then level off to become asymptotic to the x-axis. In other words, the outputs never become equal to or less than zero. As part of the results, your calculator will display a number known as the correlation coefficient, labeled by the variable r, or r 2. (You may have to change the calculator’s settings for these to be shown.) The values are an indication of the “goodness of fit” of the regression equation to the data. We more commonly use the value of r 2 instead of r, but the closer either value is to 1, the better the regression equation approximates the data.

exponential regression Exponential regression is used to model situations in which growth begins slowly and then accelerates rapidly without bound, or where decay begins rapidly and then slows down to get closer and closer to zero. We use the command “ExpReg” on a graphing utility to fit an exponential function to a set of data points. This returns an equation of the form, y = ab x Note that: • b must be non-negative. • when b > 1, we have an exponential growth model. • when 0 < b < 1, we have an exponential decay model.

**How To…**
Given a set of data, perform exponential regression using a graphing utility. 1. Use the STAT then EDIT menu to enter given data. a. Clear any existing data from the lists. b. List the input values in the L^{1} column. c. List the output values in the L^{2} column. 2. Graph and observe a scatter plot of the data using the STATPLOT feature. a. Use ZOOM [9] to adjust axes to fit the data. b. Verify the data follow an exponential pattern. 3. Find the equation that models the data. a. Select “ExpReg” from the STAT then CALC menu. b. Use the values returned for a and b to record the model, y = ab x. 4. Graph the model in the same window as the scatterplot to verify it is a good fit for the data.

**Example  1**
Using Exponential Regression to Fit a Model to Data In 2007, a university study was published investigating the crash risk of alcohol impaired driving. Data from 2,871 crashes were used to measure the association of a person’s blood alcohol level (BAC) with the risk of being in an accident. crash. So, for example, a person with a BAC of 0.09 is 3.54 times as likely to crash as a person who has not been drinking alcohol. BAC 0.01 0.03 0.05 0.07 0.09 Relative Risk of Crashing 1.03 1.06 1.38 2.09 3.54 BAC 0.11 0.13 0.15 0.17 0.19 0.21 Relative Risk of Crashing 6.41 12.6 22.1 39.05 65.32 99.78 a. Let x represent the BAC level, and let y represent the corresponding relative risk. Use exponential regression to fit a model to these data. b. After 6 drinks, a person weighing 160 pounds will have a BAC of about 0.16. How many times more likely is a person with this weight to crash if they drive after having a 6-pack of beer? Round to the nearest hundredth. 24 Source: Indiana University Center for Studies of Law in Action, 2007


**Solution**
a. Using the STAT then EDIT menu on a graphing utility, list the BAC values in L^{1} and the relative risk values in L^{2}. Then use the STATPLOT feature to verify that the scatterplot follows the exponential pattern shown in Figure 1: x y Use the “ExpReg” command from the STAT then CALC menu to obtain the exponential model, Converting from scientific notation, we have: Notice that r 2 ≈ 0.97 which indicates the model is a good fit to the data. To see this, graph the model in the same window as the scatterplot to verify it is a good fit as shown in Figure 2: x y b. Use the model to estimate the risk associated with a BAC of 0.16. Substitute 0.16 for x in the model and solve for y.

Use the regression model found in part (a).

Round to the nearest hundredth. If a 160-pound person drives after having 6 drinks, he or she is about 26.35 times more likely to crash than if driving while sober.


**Try It #1**
Month Debt ($) a. Use exponential regression to fit a model to these data. b. If spending continues at this rate, what will the graduate’s credit card debt be one year after graduating? Is it reasonable to assume that an exponential regression model will represent a situation indefinitely? No. Remember that models are formed by real-world data gathered for regression. It is usually reasonable to make estimates within the interval of original observation (interpolation). However, when a model is used to make predictions, it is important to use reasoning skills to determine whether the model makes sense for inputs far beyond the original observation interval (extrapolation). Building a Logarithmic Model from Data Just as with exponential functions, there are many real-world applications for logarithmic functions: intensity of sound, pH levels of solutions, yields of chemical reactions, production of goods, and growth of infants. As with exponential models, data modeled by logarithmic functions are either always increasing or always decreasing as time moves forward. Again, it is the way they increase or decrease that helps us determine whether a logarithmic model is best. Recall that logarithmic functions increase or decrease rapidly at first, but then steadily slow as time moves on. By reflecting on the characteristics we’ve already learned about this function, we can better analyze real world situations that reflect this type of growth or decay. When performing logarithmic regression analysis, we use the form of the logarithmic function most commonly used on graphing utilities, y = a + bln(x). For this function • All input values, x, must be greater than zero. • The point (1, a) is on the graph of the model. • If b > 0, the model is increasing. Growth increases rapidly at first and then steadily slows over time. • If b < 0, the model is decreasing. Decay occurs rapidly at first and then steadily slows over time. logarithmic regression Logarithmic regression is used to model situations where growth or decay accelerates rapidly at first and then slows over time. We use the command “LnReg” on a graphing utility to fit a logarithmic function to a set of data points. This returns an equation of the form, y = a + bln(x) Note that: • all input values, x, must be non-negative. • when b > 0, the model is increasing. • when b < 0, the model is decreasing.

**How To…**
Given a set of data, perform logarithmic regression using a graphing utility. 1. Use the STAT then EDIT menu to enter given data. a. Clear any existing data from the lists. b. List the input values in the L^{1} column.

c. List the output values in the L^{2} column. 2. Graph and observe a scatter plot of the data using the STATPLOT feature. a. Use ZOOM [9] to adjust axes to fit the data. b. Verify the data follow a logarithmic pattern. 3. Find the equation that models the data. a. Select “LnReg” from the STAT then CALC menu. b. Use the values returned for a and b to record the model, y = a + bln(x). 4. Graph the model in the same window as the scatterplot to verify it is a good fit for the data.

**Example  2**
Using Logarithmic Regression to Fit a Model to Data Due to advances in medicine and higher standards of living, life expectancy has been increasing in most developed countries since the beginning of the 20th century. Year Life Expectancy (Years) 47.3 50.0 54.1 59.7 62.9 68.2 Year Life Expectancy (Years) 69.7 70.8 73.7 75.4 76.8 78.7 a. Let x represent time in decades starting with x = 1 for the year 1900, x = 2 for the year 1910, and so on. Let y represent the corresponding life expectancy. Use logarithmic regression to fit a model to these data. b. Use the model to predict the average American life expectancy for the year 2030.

**Solution**
a. Using the STAT then EDIT menu on a graphing utility, list the years using values 1–12 in L^{1} and the corresponding life expectancy in L^{2}. Then use the STATPLOT feature to verify that the scatterplot follows a logarithmic pattern as shown in Figure 3: x y Use the “LnReg” command from the STAT then CALC menu to obtain the logarithmic model, Next, graph the model in the same window as the scatterplot to verify it is a good fit as shown in Figure 4: 25 Source: Center for Disease Control and Prevention, 2013

x y b. To predict the life expectancy of an American in the year 2030, substitute x = 14 for the in the model and solve for y:

y = 42.52722583 + 13.85752327ln(x) Use the regression model found in part ( a).

Round to the nearest tenth If life expectancy continues to increase at this pace, the average life expectancy of an American will be 79.1 by

**Try It #2**
Sales of a video game released in the year 2000 took off at first, but then steadily slowed as time moved on. Table 4 shows the number of games sold, in thousands, from the years 2000–2010. Year Number Sold (Thousands) a. Let x represent time in years starting with x = 1 for the year 2000. Let y represent the number of games sold in thousands. Use logarithmic regression to fit a model to these data. b. If games continue to sell at this rate, how many games will sell in 2015? Round to the nearest thousand.

Building a Logistic Model from Data Like exponential and logarithmic growth, logistic growth increases over time. One of the most notable differences with logistic growth models is that, at a certain point, growth steadily slows and the function approaches an upper bound, or limiting value. Because of this, logistic regression is best for modeling phenomena where there are limits in expansion, such as availability of living space or nutrients. It is worth pointing out that logistic functions actually model resource-limited exponential growth. There are many examples of this type of growth in real-world situations, including population growth and spread of disease, rumors, and even stains in fabric. When performing logistic regression analysis, we use the form most commonly used on graphing utilities: y =  c _______ 1 + ae-b x  Recall that: •  c _____ 1 + a  is the initial value of the model. • when b > 0, the model increases rapidly at first until it reaches its point of maximum growth rate,   ln(a) _ b ,  c _ 2  . At that point, growth steadily slows and the function becomes asymptotic to the upper bound y = c. • c is the limiting value, sometimes called the carrying capacity, of the model. logistic regression Logistic regression is used to model situations where growth accelerates rapidly at first and then steadily slows to an upper limit. We use the command “Logistic” on a graphing utility to fit a logistic function to a set of data points. This returns an equation of the form y =  c _______ 1 + ae-b x  Note that • The initial value of the model is  c _ 1 + a . • Output values for the model grow closer and closer to y = c as time increases.

**How To…**
Given a set of data, perform logistic regression using a graphing utility. 1. Use the STAT then EDIT menu to enter given data. a. Clear any existing data from the lists. b. List the input values in the L^{1} column. c. List the output values in the L^{2} column. 2. Graph and observe a scatter plot of the data using the STATPLOT feature. a. Use ZOOM [9] to adjust axes to fit the data. b. Verify the data follow a logistic pattern. 3. Find the equation that models the data. a. Select “Logistic” from the STAT then CALC menu. b. Use the values returned for a, b, and c to record the model, y =  c _ 1 + ae-b x . 4. Graph the model in the same window as the scatterplot to verify it is a good fit for the data.

**Example  3**
Using Logistic Regression to Fit a Model to Data Mobile telephone service has increased rapidly in America since the mid 1990s. Today, almost all residents have cellular service. Table 5 shows the percentage of Americans with cellular service between the years 1995 and 2012[26]. 26 Source: The World Bankn, 2013

Year Americans with Cellular Service (%) Year Americans with Cellular Service (%)

12.69

16.35 68.63

20.29 76.64

25.08 82.47

30.81 85.68

38.75 89.14

45.00 91.86

49.16 95.28

55.15 98.17 a. Let x represent time in years starting with x = 0 for the year 1995. Let y represent the corresponding percentage of residents with cellular service. Use logistic regression to fit a model to these data. b. Use the model to calculate the percentage of Americans with cell service in the year 2013. Round to the nearest tenth of a percent. c. Discuss the value returned for the upper limit c. What does this tell you about the model? What would the limiting value be if the model were exact?

**Solution**
a. Using the STAT then EDIT menu on a graphing utility, list the years using values 0–15 in L^{1} and the corresponding percentage in L^{2}. Then use the STATPLOT feature to verify that the scatterplot follows a logistic pattern as shown in Figure 5: x y Use the “Logistic” command from the STAT then CALC menu to obtain the logistic model, y = 

___________________

Next, graph the model in the same window as shown in Figure 6 the scatterplot to verify it is a good fit: x y

b. To approximate the percentage of Americans with cellular service in the year 2013, substitute x = 18 for the in the model and solve for y:

y = 

____________________

Use the regression model found in part ( a).

= 

_____________________

Round to the nearest tenth According to the model, about 99.3% of Americans had cellular service in 2013. c. The model gives a limiting value of about 105. This means that the maximum possible percentage of Americans with cellular service would be 105%, which is impossible. (How could over 100% of a population have cellular service?) If the model were exact, the limiting value would be c = 100 and the model’s outputs would get very close to, but never actually reach 100%. After all, there will always be someone out there without cellular service!

**Try It #3**
Year Seal Population (Thousands) Year Seal Population (Thousands)

3.493

5.282

6.357

9.201

a. Let x represent time in years starting with x = 0 for the year 1997. Let y represent the number of seals in thousands. Use logistic regression to fit a model to these data. b. Use the model to predict the seal population for the year 2020. c. To the nearest whole number, what is the limiting value of this model? > Access this online resource for additional instruction and practice with exponential function models. • Exponential Regression on a Calculator (http://openstaxcollege.org/l/pregresscalc)


## 4.8 Section Exercises

### 4.8 Section Exercises
Verbal 1. What situations are best modeled by a logistic equation? Give an example, and state a case for why the example is a good fit. 2. What is a carrying capacity? What kind of model has a carrying capacity built into its formula? Why does this make sense? 3. What is regression analysis? Describe the process of performing regression analysis on a graphing utility. 4. What might a scatterplot of data points look like if it were best described by a logarithmic model? 5. What does the y-intercept on the graph of a logistic equation correspond to for a population modeled by that equation? Graphical For the following exercises, match the given function of best fit with the appropriate scatterplot in Figure 7 through y x (a) y x (b) y x (c) y x (d) y x (e) 10. y =  __________

Numeric 11. To the nearest whole number, what is the initial value of a population modeled by the logistic equation P(t) =  ____________

1 + 6.995e-0.68t ? What is the carrying capacity? 12. Rewrite the exponential model A(t) = 1550(1.085)x as an equivalent model with base e. Express the exponent to four significant digits. 13. A logarithmic model is given by the equation h(p) = 67.682 - 5.792ln(p). To the nearest hundredth, for what value of p does h(p) = 62? 14. A logistic model is given by the equation P(t) =  ________ 1 + 5e-0.42t . To the nearest hundredth, for what value of t does P(t) = 45? 15. What is the y-intercept on the graph of the logistic model given in the previous exercise? Technology For the following exercises, use this scenario: The population P of a koi pond over x months is modeled by the function P(x) =  __ 16. Graph the population model to show the population over a span of 3 years. 17. What was the initial population of koi? 18. How many koi will the pond have after one and a half years? 19. How many months will it take before there are 20 koi in the pond? 20. Use the intersect feature to approximate the number of months it will take before the population of the pond reaches half its carrying capacity. For the following exercises, use this scenario: The population P of an endangered species habitat for wolves is modeled by the function P(x) =  __

1 + 54.8e-0.462x  , where x is given in years. 21. Graph the population model to show the population over a span of 10 years. 22. What was the initial population of wolves transported to the habitat? 23. How many wolves will the habitat have after 3 years? 24. How many years will it take before there are 100 wolves in the habitat? 25. Use the intersect feature to approximate the number of years it will take before the population of the habitat reaches half its carrying capacity. For the following exercises, refer to Table 7. x f (x) 26. Use a graphing calculator to create a scatter diagram of the data. 27. Use the regression feature to find an exponential function that best fits the data in the table. 28. Write the exponential function as an exponential equation with base e. 29. Graph the exponential equation on the scatter diagram. 30. Use the intersect feature to find the value of x for which f (x) = 4000.

For the following exercises, refer to Table 8. x f (x) 31. Use a graphing calculator to create a scatter diagram of the data. 32. Use the regression feature to find an exponential function that best fits the data in the table. 33. Write the exponential function as an exponential equation with base e. 34. Graph the exponential equation on the scatter diagram. 35. Use the intersect feature to find the value of x for which f (x) = 250. For the following exercises, refer to Table 9. x f (x) 5.1 6.3 7.3 7.7 8.1 8.6 36. Use a graphing calculator to create a scatter diagram of the data. 37. Use the LOGarithm option of the REGression feature to find a logarithmic function of the form y = a + bln(x) that best fits the data in the table. 38. Use the logarithmic function to find the value of the function when x = 10. 39. Graph the logarithmic equation on the scatter diagram. 40. Use the intersect feature to find the value of x for which f (x) = 7. For the following exercises, refer to Table 10. x f (x) 7.5 5.2 4.3 3.9 3.4 3.1 2.9 41. Use a graphing calculator to create a scatter diagram of the data. 42. Use the LOGarithm option of the REGression feature to find a logarithmic function of the form y = a + bln(x) that best fits the data in the table. 43. Use the logarithmic function to find the value of the function when x = 10. 44. Graph the logarithmic equation on the scatter diagram. 45. Use the intersect feature to find the value of x for which f (x) = 8. For the following exercises, refer to Table 11. x f (x) 8.7 12.3 15.4 18.5 20.7 22.5 23.3 24.6 24.8 46. Use a graphing calculator to create a scatter diagram of the data. 47. Use the LOGISTIC regression option to find a logistic growth model of the form y =  c _ 1 + ae-b x  that best fits the data in the table.

48. Graph the logistic equation on the scatter diagram. 49. To the nearest whole number, what is the predicted carrying capacity of the model? 50. Use the intersect feature to find the value of x for which the model reaches half its carrying capacity. For the following exercises, refer to Table 12. x f (x) 28.6 52.8 70.3 99.9 51. Use a graphing calculator to create a scatter diagram of the data. 52. Use the LOGISTIC regression option to find a logistic growth model of the form y =  c ________ 1 + ae-b x  that best fits the data in the table. 53. Graph the logistic equation on the scatter diagram. 54. To the nearest whole number, what is the predicted carrying capacity of the model? 55. Use the intersect feature to find the value of x for which the model reaches half its carrying capacity. extensions 56. Recall that the general form of a logistic equation for a population is given by P(t) =  c _ 1 + ae-bt  , such that the initial population at time t = 0 is P(0) = P^{0}. Show algebraically that  c - P(t) _ P(t)  =  c - P^{0} _ P^{0} e-bt. 57. Use a graphing utility to find an exponential regression formula f (x) and a logarithmic regression formula g(x) for the points (1.5, 1.5) and (8.5, 8.5). Round all numbers to 6 decimal places. Graph the points and both formulas along with the line y = x on the same axis. Make a conjecture about the relationship of the regression formulas. 58. Verify the conjecture made in the previous exercise. Round all numbers to six decimal places when necessary. 59. Find the inverse function f -1 (x) for the logistic function f (x) =  c _ 1 + ae-b x . Show all steps. 60. Use the result from the previous exercise to graph the logistic model P(t) =  ________ 1 + 4e-0.5t  along with its inverse on the same axis. What are the intercepts and asymptotes of each function?


### Key Terms
annual percentage rate (APR) the yearly interest rate earned by an investment account, also called nominal rate carrying capacity in a logistic model, the limiting value of the output change-of-base formula a formula for converting a logarithm with any base to a quotient of logarithms with any other base. common logarithm the exponent to which 10 must be raised to get x; log^{1}0(x) is written simply as log(x). compound interest interest earned on the total balance, not just the principal doubling time the time it takes for a quantity to double exponential growth a model that grows by a rate proportional to the amount present extraneous solution a solution introduced while solving an equation that does not satisfy the conditions of the original equation half-life the length of time it takes for a substance to exponentially decay to half of its original quantity logarithm the exponent to which b must be raised to get x; written y = logb(x) logistic growth model a function of the form f (x) =  c ________ 1+ ae-b x  where  c _ 1 + a  is the initial value, c is the carrying capacity, or limiting value, and b is a constant determined by the rate of growth natural logarithm the exponent to which the number e must be raised to get x; loge(x) is written as ln(x). Newton’s Law of Cooling the scientific formula for temperature as a function of time as an object’s temperature is equalized with the ambient temperature nominal rate the yearly interest rate earned by an investment account, also called annual percentage rate order of magnitude the power of ten, when a number is expressed in scientific notation, with one non-zero digit to the left of the decimal power rule for logarithms a rule of logarithms that states that the log of a power is equal to the product of the exponent and the log of its base product rule for logarithms a rule of logarithms that states that the log of a product is equal to a sum of logarithms quotient rule for logarithms a rule of logarithms that states that the log of a quotient is equal to a difference of logarithms Key Equations definition of the exponential function f (x) = b x, where b > 0, b \neq  1 definition of exponential growth f (x) = ab x, where a > 0, b > 0, b \neq  1 compound interest formula A(t) = P  1 +  r _ n   nt, where

A(t) is the account value at time t

t is the number of years

P is the initial investment, often called the principal

r is the annual percentage rate (APR), or nominal rate

n is the number of compounding periods in one year continuous growth formula A(t) = ae rt, where

t is the number of unit time periods of growth

a is the starting amount (in the continuous compounding formula a is replaced with P, the principal) e is the mathematical constant, e ≈ 2.718282 General Form for the Translation of the f (x) = ab x + c + d Parent Function f (x) = b x Definition of the logarithmic function For x > 0, b > 0, b \neq  1, y = logb(x) if and only if b y = x. Definition of the common logarithm For x > 0, y = log(x) if and only if 10y = x.

Definition of the natural logarithm For x > 0, y = ln(x) if and only if ey = x. General Form for the Translation of the f (x) = alogb(x + c) + d Parent Logarithmic Function f (x) = logb(x) The Product Rule for Logarithms logb(MN) = logb(M) + logb(N) The Quotient Rule for Logarithms logb  M __ N   = logbM - logbN The Power Rule for Logarithms logb(Mn) = nlogbM The Change-of-Base Formula logbM =  lognM _ lognb  n > 0, n \neq  1, b \neq  1 One-to-one property for exponential functions

For any algebraic expressions S and T and any positive real number b, where bS = bT if and only if S = T. Definition of a logarithm For any algebraic expression S and positive real numbers b and c, where b \neq  1,

logb(S) = c if and only if bc = S. One-to-one property for logarithmic functions

For any algebraic expressions S and T and any positive real number b, where b \neq  1,

logbS = logbT if and only if S = T. Half-life formula If A = A^{0}e kt, k < 0, the half-life is t = - ln(2) _ k . t =  ln  A _ A^{0}   _ Carbon-14 dating A^{0} is the amount of carbon-14 when the plant or animal died, A is the amount of carbon-14 remaining today, t is the age of the fossil in years Doubling time formula If A = A^{0}e kt, k > 0, the doubling time is t =  ln(2) ___ k  Newton’s Law of Cooling T(t) = Ae kt + Ts, where Ts is the ambient temperature, A = T(0) - Ts, and k is the continuous rate of cooling.

### Key Concepts
• An exponential function is defined as a function with a positive constant other than 1 raised to a variable exponent. See Example 1. • A function is evaluated by solving at a specific value. See Example 2 and Example 3. • An exponential model can be found when the growth rate and initial value are known. See Example 4. • An exponential model can be found when the two data points from the model are known. See Example 5. • An exponential model can be found using two data points from the graph of the model. See Example 6. • An exponential model can be found using two data points from the graph and a calculator. See Example 7. • The value of an account at any time t can be calculated using the compound interest formula when the principal, annual interest rate, and compounding periods are known. See Example 8. • The initial investment of an account can be found using the compound interest formula when the value of the account, annual interest rate, compounding periods, and life span of the account are known. See Example 9. • The number e is a mathematical constant often used as the base of real world exponential growth and decay models. Its decimal approximation is e ≈ 2.718282. • Scientific and graphing calculators have the key [e x] or [e xp(x)] for calculating powers of e. See Example 10. • Continuous growth or decay models are exponential models that use e as the base. Continuous growth and decay models can be found when the initial value and growth or decay rate are known. See Example 11 and Example 12.

• The graph of the function f (x) = b x has a y-intercept at (0, 1), domain (-\infty , \infty ), range (0, \infty ), and horizontal asymptote y = 0. See Example 1. • If b > 1, the function is increasing. The left tail of the graph will approach the asymptote y = 0, and the right tail will increase without bound. • If 0 < b < 1, the function is decreasing. The left tail of the graph will increase without bound, and the right tail will approach the asymptote y = 0. • The equation f (x) = b x + d represents a vertical shift of the parent function f (x) = b x. • The equation f (x) = b x + c represents a horizontal shift of the parent function f (x) = b x. See Example 2. • Approximate solutions of the equation f (x) = b x + c + d can be found using a graphing calculator. See Example 3. • The equation f (x) = ab x, where a > 0, represents a vertical stretch if ∣ a ∣ > 1 or compression if 0 < ∣ a ∣ < 1 of the parent function f (x) = b x. See Example 4. • When the parent function f (x) = b x is multiplied by -1, the result, f (x) = -b x, is a reflection about the x-axis. When the input is multiplied by -1, the result, f (x) = b-x, is a reflection about the y-axis. See Example 5. • All translations of the exponential function can be summarized by the general equation f (x) = ab x + c + d. See • Using the general equation f (x) = ab x + c + d, we can write the equation of a function given its description. See

**Example 6** — .
• The inverse of an exponential function is a logarithmic function, and the inverse of a logarithmic function is an exponential function. • Logarithmic equations can be written in an equivalent exponential form, using the definition of a logarithm. See Example 1. • Exponential equations can be written in their equivalent logarithmic form using the definition of a logarithm See Example 2. • Logarithmic functions with base b can be evaluated mentally using previous knowledge of powers of b. See

**Example 3** — and Example 4.
• Common logarithms can be evaluated mentally using previous knowledge of powers of 10. See Example 5. • When common logarithms cannot be evaluated mentally, a calculator can be used. See Example 6. • Real-world exponential problems with base 10 can be rewritten as a common logarithm and then evaluated using a calculator. See Example 7. • Natural logarithms can be evaluated using a calculator Example 8. 4.4 Graphs of Logarithmic Functions • To find the domain of a logarithmic function, set up an inequality showing the argument greater than zero, and solve for x. See Example 1 and Example 2 • The graph of the parent function f (x) = logb(x) has an x-intercept at (1, 0), domain (0, \infty ), range (-\infty , \infty ), vertical asymptote x = 0, and • if b > 1, the function is increasing. • if 0 < b < 1, the function is decreasing. See Example 3. • The equation f (x) = logb(x + c) shifts the parent function y = logb(x) horizontally • left c units if c > 0. • right c units if c < 0. See Example 4. • The equation f (x) = logb(x) + d shifts the parent function y = logb(x) vertically • up d units if d > 0. • down d units if d < 0. See Example 5.

• For any constant a > 0, the equation f (x) = alogb(x) • stretches the parent function y = logb(x) vertically by a factor of a if ∣ a ∣ > 1. • compresses the parent function y = logb(x) vertically by a factor of a if ∣ a ∣ < 1. See Example 6 and Example 7. • When the parent function y = logb(x) is multiplied by -1, the result is a reflection about the x-axis. When the input is multiplied by -1, the result is a reflection about the y-axis. • The equation f (x) = -logb(x) represents a reflection of the parent function about the x-axis. • The equation f (x) = logb(-x) represents a reflection of the parent function about the y-axis. See Example 8. • A graphing calculator may be used to approximate solutions to some logarithmic equations See Example 9. • All translations of the logarithmic function can be summarized by the general equation f (x) = alogb(x + c) + d. See Table 4. • Given an equation with the general form f (x) = alogb(x + c) + d, we can identify the vertical asymptote x = -c for the transformation. See Example 10. • Using the general equation f (x) = alogb(x + c) + d, we can write the equation of a logarithmic function given its graph. See Example 11. 4.5 Logarithmic Properties • We can use the product rule of logarithms to rewrite the log of a product as a sum of logarithms. See

**Example 1** — .
• We can use the quotient rule of logarithms to rewrite the log of a quotient as a difference of logarithms. See

**Example 2** — .
• We can use the power rule for logarithms to rewrite the log of a power as the product of the exponent and the log of its base. See Example 3, Example 4, and Example 5. • We can use the product rule, the quotient rule, and the power rule together to combine or expand a logarithm with a complex input. See Example 6, Example 7, and Example 8. • The rules of logarithms can also be used to condense sums, differences, and products with the same base as a single logarithm. See Example 9, Example 10, Example 11, and Example 12. • We can convert a logarithm with any base to a quotient of logarithms with any other base using the change-of- base formula. See Example 13. • The change-of-base formula is often used to rewrite a logarithm with a base other than 10 and e as the quotient of natural or common logs. That way a calculator can be used to evaluate. See Example 14. 4.6 Exponential and Logarithmic Equations • We can solve many exponential equations by using the rules of exponents to rewrite each side as a power with the same base. Then we use the fact that exponential functions are one-to-one to set the exponents equal to one another and solve for the unknown. • When we are given an exponential equation where the bases are explicitly shown as being equal, set the exponents equal to one another and solve for the unknown. See Example 1. • When we are given an exponential equation where the bases are not explicitly shown as being equal, rewrite each side of the equation as powers of the same base, then set the exponents equal to one another and solve for the unknown. See Example 2, Example 3, and Example 4. • When an exponential equation cannot be rewritten with a common base, solve by taking the logarithm of each side. See Example 5. • We can solve exponential equations with base e, by applying the natural logarithm of both sides because exponential and logarithmic functions are inverses of each other. See Example 6 and Example 7. • After solving an exponential equation, check each solution in the original equation to find and eliminate any extraneous solutions. See Example 8.

• When given an equation of the form logb(S) = c, where S is an algebraic expression, we can use the definition of a logarithm to rewrite the equation as the equivalent exponential equation bc = S, and solve for the unknown. See Example 9 and Example 10. • We can also use graphing to solve equations with the form logb(S) = c. We graph both equations y = logb(S) and y = c on the same coordinate plane and identify the solution as the x-value of the intersecting point. See Example 11. • When given an equation of the form logbS = logbT, where S and T are algebraic expressions, we can use the one- to-one property of logarithms to solve the equation S = T for the unknown. See Example 12. • Combining the skills learned in this and previous sections, we can solve equations that model real world situations, whether the unknown is in an exponent or in the argument of a logarithm. See Example 13. 4.7 Exponential and Logarithmic Models • The basic exponential function is f (x) = ab x. If b > 1, we have exponential growth; if 0 < b < 1, we have exponential decay. • We can also write this formula in terms of continuous growth as A = A^{0}e kx, where A^{0} is the starting value. If A^{0} is positive, then we have exponential growth when k > 0 and exponential decay when k < 0. See Example 1. • In general, we solve problems involving exponential growth or decay in two steps. First, we set up a model and use the model to find the parameters. Then we use the formula with these parameters to predict growth and decay. See Example 2. • We can find the age, t, of an organic artifact by measuring the amount, k, of carbon-14 remaining in the artifact and using the formula t =  ln(k) _ -0.000121  to solve for t. See Example 3. • Given a substance’s doubling time or half-life we can find a function that represents its exponential growth or decay. See Example 4. • We can use Newton’s Law of Cooling to find how long it will take for a cooling object to reach a desired temperature, or to find what temperature an object will be after a given time. See Example 5. • We can use logistic growth functions to model real-world situations where the rate of growth changes over time, such as population growth, spread of disease, and spread of rumors. See Example 6. • We can use real-world data gathered over time to observe trends. Knowledge of linear, exponential, logarithmic, and logistic graphs help us to develop models that best fit our data. See Example 7. • Any exponential function with the form y = ab x can be rewritten as an equivalent exponential function with the form y = A^{0}e kx where k = lnb. See Example 8. 4.8 Fitting Exponential Models to Data • Exponential regression is used to model situations where growth begins slowly and then accelerates rapidly without bound, or where decay begins rapidly and then slows down to get closer and closer to zero. • We use the command “ExpReg” on a graphing utility to fit function of the form y = ab x to a set of data points. See Example 1. • Logarithmic regression is used to model situations where growth or decay accelerates rapidly at first and then slows over time. • We use the command “LnReg” on a graphing utility to fit a function of the form y = a + bln(x) to a set of data points. See Example 2. • Logistic regression is used to model situations where growth accelerates rapidly at first and then steadily slows as the function approaches an upper limit. • We use the command “Logistic” on a graphing utility to fit a function of the form y =  c _________ 1 + ae-b x  to a set of data points. See Example 3.

Exponential Functions 1. Determine whether the function y = 156(0.825)t represents exponential growth, exponential decay, or neither. Explain 2. The population of a herd of deer is represented by the function A(t) = 205(1.13)t, where t is given in years. To the nearest whole number, what will the herd population be after 6 years? 3. Find an exponential equation that passes through the points (2, 2.25) and (5, 60.75). 4. Determine whether Table 1 could represent a function that is linear, exponential, or neither. If it appears to be exponential, find a function that passes through the points. x f (x) 0.9 0.27 0.081 5. A retirement account is opened with an initial deposit of $8,500 and earns 8.12% interest compounded monthly. What will the account be worth in 20 years? 6. Hsu-Mei wants to save $5,000 for a down payment on a car. To the nearest dollar, how much will she need to invest in an account now with 7.5% APR, compounded daily, in order to reach her goal in 3 years? 7. Does the equation y = 2.294e-0.654t represent continuous growth, continuous decay, or neither? Explain. 8. Suppose an investment account is opened with an initial deposit of $10,500 earning 6.25% interest, compounded continuously. How much will the account be worth after 25 years? Graphs of Exponential Functions 9. Graph the function f (x) = 3.5(2)x. State the domain and range and give the y-intercept. 10. Graph the function f (x) = 4  1 __ 8   x and its reflection about the y-axis on the same axes, and give the y-intercept. 11. The graph of f (x) = 6.5x is reflected about the y-axis and stretched vertically by a factor of 7. What is the equation of the new function, g (x) ? State its y-intercept, domain, and range. 12. The graph here shows transformations of the graph of f (x) = 2x. What is the equation for the transformation? x y Logarithmic Functions 13. Rewrite log^{1}7(4913) = x as an equivalent exponential equation. 14. Rewrite ln(s) = t as an equivalent exponential equation. 15. Rewrite a - 2 __ 5  = b as an equivalent logarithmic equation. 16. Rewrite e-3.5 = h as an equivalent logarithmic equation. 17. Solve for xlog^{6}4(x) =   1 _ 3   to exponential form. 18. Evaluate log^{5}  1 _ 125   without using a calculator. 19. Evaluate log(0.000001) without using a calculator. 20. Evaluate log(4.005) using a calculator. Round to the nearest thousandth.

21. Evaluate ln(e-0.8648) without using a calculator. 22. Evaluate ln  \sqrt{18}   using a calculator. Round to the nearest thousandth. Graphs of Logarithmic Functions 23. Graph the function g(x) = log(7x + 21) - 4. 24. Graph the function h(x) = 2ln(9 - 3x) + 1. 25. State the domain, vertical asymptote, and end behavior of the function g (x) = ln(4x + 20) - 17. Logarithmic Properties 26. Rewrite ln(7r \cdot  11st) in expanded form. 27. Rewrite log^{8}(x) + log^{8}(5) + log^{8}(y) + log^{8}(13) in compact form. 28. Rewrite logm  67 ___ 83   in expanded form. 29. Rewrite ln(z) – ln(x) – ln(y) in compact form. 30. Rewrite ln   1 __ x^{5}   as a product. 31. Rewrite -logy  1 __ 12   as a single logarithm. 32. Use properties of logarithms to expand log  r 2s^{1}1 _ t^{1}4  . 33. Use properties of logarithms to expand ln 2b\sqrt{______}

 b + 1 _____ b - 1   . 34. Condense the expression 5ln(b) + ln(c) +  ln(4 - a) _  to a single logarithm. 35. Condense the expression 3log^{7}v + 6log^{7}w -  log 7 u _ 3  to a single logarithm. 36. Rewrite log^{3}(12.75) to base e. 37. Rewrite 512x - 17 = 125 as a logarithm. Then apply the change of base formula to solve for x using the common log. Round to the nearest thousandth. Exponential and Logarithmic Equations 38. Solve 2163x \cdot  216x = 363x + 2 by rewriting each side with a common base. 39. Solve  __   1 _ -x - 3  = 53 by rewriting each side with a common base. 40. Use logarithms to find the exact solution for 7 \cdot  17-9x - 7 = 49. If there is no solution, write no solution. 41. Use logarithms to find the exact solution for 3e^{6}n - 2 + 1 = -60. If there is no solution, write no solution. 42. Find the exact solution for 5e^{3}x - 4 = 6 . If there is no solution, write no solution. 43. Find the exact solution for 2e^{5}x - 2 - 9 = -56. If there is no solution, write no solution. 44. Find the exact solution for 52x - 3 = 7x + 1. If there is no solution, write no solution. 45. Find the exact solution for e 2x - e x - 110 = 0. If there is no solution, write no solution. 46. Use the definition of a logarithm to solve. 47. Use the definition of a logarithm to find the exact solution for 9 + 6ln(a + 3) = 33. 48. Use the one-to-one property of logarithms to find an exact solution for log^{8}(7) + log^{8}(-4x) = log^{8}(5). If there is no solution, write no solution. 49. Use the one-to-one property of logarithms to find an exact solution for ln(5) + ln(5x^{2} - 5) = ln(56). If there is no solution, write no solution. 50. The formula for measuring sound intensity in decibels D is defined by the equation D = 10log   I _ I^{0}   , where I is the intensity of the sound in watts per square meter and I^{0} = 10-12 is the lowest level of sound that the average person can hear. How many decibels are emitted from a large orchestra with a sound intensity of 6.3 \cdot  10-3 watts per square meter? 51. The population of a city is modeled by the equation P(t) = 256, 114e^{0}.25t where t is measured in years. If the city continues to grow at this rate, how many years will it take for the population to reach one million? 52. Find the inverse function f -1 for the exponential function f (x) = 2 \cdot  e x + 1 - 5. 53. Find the inverse function f -1 for the logarithmic function f (x) = 0.25 \cdot  log^{2}(x^{3} + 1).

Exponential and Logarithmic Models For the following exercises, use this scenario: A doctor prescribes 300 milligrams of a therapeutic drug that decays by about 17% each hour. 54. To the nearest minute, what is the half-life of the drug? 55. Write an exponential model representing the amount of the drug remaining in the patient’s system after t hours. Then use the formula to find the amount of the drug that would remain in the patient’s system after 24 hours. Round to the nearest hundredth of a gram. For the following exercises, use this scenario: A soup with an internal temperature of 350° Fahrenheit was taken off the stove to cool in a 71°F room. After fifteen minutes, the internal temperature of the soup was 175°F. 56. Use Newton’s Law of Cooling to write a formula that models this situation. 57. How many minutes will it take the soup to cool to 85°F? For the following exercises, use this scenario: The equation N(t) =  __

1 + 199e-0.625t  models the number of people in a school who have heard a rumor after t days. 58. How many people started the rumor? 59. To the nearest tenth, how many days will it be before the rumor spreads to half the carrying capacity? 60. What is the carrying capacity? For the following exercises, enter the data from each table into a graphing calculator and graph the resulting scatter plots. Determine whether the data from the table would likely represent a function that is linear, exponential, or logarithmic. x f (x) 3.05 4.42 6.4 9.28 13.46 19.52 28.3 41.04 59.5 86.28 x 0.5 f (x) 18.05 15.33 14.55 14.04 13.5 13.22 13.1 12.88 12.69 12.45 63. Find a formula for an exponential equation that goes through the points (-2, 100) and (0, 4). Then express the formula as an equivalent equation with base e. Fitting Exponential Models to Data 64. What is the carrying capacity for a population modeled by the logistic equation P(t) =  250, 000 ___________ 1 + 499e-0.45t ? What is the initial population for the model? 65. The population of a culture of bacteria is modeled by the logistic equation P(t) =  14, 250 __ 1 + 29e-0.62t , where t is in days. To the nearest tenth, how many days will it take the culture to reach 75% of its carrying capacity? For the following exercises, use a graphing utility to create a scatter diagram of the data given in the table. Observe the shape of the scatter diagram to determine whether the data is best described by an exponential, logarithmic, or logistic model. Then use the appropriate regression feature to find an equation that models the data. When necessary, round values to five decimal places. x f (x) 409.4 260.7 170.4 110.6 44.7 32.4 19.5 12.7 8.1 x 0.15 0.25 0.5 0.75 1.5 2.25 2.75 3.5 f (x) 36.21 28.88 24.39 18.28 16.5 12.99 9.91 8.57 7.23 5.99 4.81 x f (x) 22.6 44.2 62.1 96.9 113.4 133.4 137.6 148.4 149.3

1. The population of a pod of bottlenose dolphins is modeled by the function A(t) = 8(1.17)t, where t is given in years. To the nearest whole number, what will the pod population be after 3 years? 2. Find an exponential equation that passes through the points (0, 4) and (2, 9). 3. Drew wants to save $2,500 to go to the next World Cup. To the nearest dollar, how much will he need to invest in an account now with 6.25% APR, compounding daily, in order to reach his goal in 4 years? 4. An investment account was opened with an initial deposit of $9,600 and earns 7.4% interest, compounded continuously. How much will the account be worth after 15 years? 5. Graph the function f (x) = 5(0.5)-x and its reflection across the y-axis on the same axes, and give the y-intercept. 6. The graph below shows transformations of the graph of f (x) =   1 __ 2   x. What is the equation for the transformation? x y 7. Rewrite log^{8}.5(614.125) = a as an equivalent exponential equation. 8. Rewrite e  1 __ 2  = m as an equivalent logarithmic equation. 9. Solve for x by converting the logarithmic equation log  1 _ 7 (x) = 2 to exponential form. 10. Evaluate log(10,000,000) without using a calculator. 11. Evaluate ln(0.716) using a calculator. Round to the nearest thousandth. 12. Graph the function g (x) = log(12 - 6x) + 3. 13. State the domain, vertical asymptote, and end behavior of the function f (x) = log^{5}(39 - 13x) + 7. 14. Rewrite log(17a \cdot  2b) as a sum. 15. Rewrite logt(96) - logt(8) in compact form. 16. Rewrite log^{8} a  1 __ b   as a product. 17. Use properties of logarithm to expand ln (y 3z 2 \cdot   \sqrt{x} - 4 ). 18. Condense the expression 4ln(c) + ln(d) +  ln(a) _ 3  +  ln(b + 3) _  to a single logarithm. 19. Rewrite 163x - 5 = 1000 as a logarithm. Then apply the change of base formula to solve for x using the natural log. Round to the nearest thousandth. 20. Solve   1 _ 81   x  \cdot   1 _ 243  =   1 _ 9   -3x - 1 by rewriting each side with a common base. 21. Use logarithms to find the exact solution for -9e^{1}0a - 8 -5 = -41. If there is no solution, write no solution. 22. Find the exact solution for 10e 4x + 2 + 5 = 56. If there is no solution, write no solution. 23. Find the exact solution for -5e-4x - 1 - 4 = 64. If there is no solution, write no solution. 24. Find the exact solution for 2x - 3 = 62x - 1. If there is no solution, write no solution. 25. Find the exact solution for e^{2}x - e x - 72 = 0. If there is no solution, write no solution. 26. Use the definition of a logarithm to find the exact solution for 4log(2n) - 7 = -11.

27. Use the one-to-one property of logarithms to find an exact solution for log(4x^{2} - 10) + log(3) = log(51) If there is no solution, write no solution. 28. The formula for measuring sound intensity in decibels D is defined by the equation D = 10log   I __ I^{0}   where I is the intensity of the sound in watts per square meter and I^{0} = 10-12 is the lowest level of sound that the average person can hear. How many decibels are emitted from a rock concert with a sound intensity of 4.7 \cdot  10-1 watts per square meter? 29. A radiation safety officer is working with 112 grams of a radioactive substance. After 17 days, the sample has decayed to 80 grams. Rounding to five significant digits, write an exponential equation representing this situation. To the nearest day, what is the half-life of this substance? 30. Write the formula found in the previous exercise as an equivalent equation with base e. Express the exponent to five significant digits. 31. A bottle of soda with a temperature of 71° Fahrenheit was taken off a shelf and placed in a refrigerator with an internal temperature of 35° F. After ten minutes, the internal temperature of the soda was 63° F. Use Newton’s Law of Cooling to write a formula that models this situation. To the nearest degree, what will the temperature of the soda be after one hour? 32. The population of a wildlife habitat is modeled by the equation P(t) =  __ 1 + 6.2e-0.35t , where t is given in years. How many animals were originally transported to the habitat? How many years will it take before the habitat reaches half its capacity? 33. Enter the data from Table 2 into a graphing calculator and graph the resulting scatter plot. Determine whether the data from the table would likely represent a function that is linear, exponential, or logarithmic. x f (x) 8.55 11.79 14.09 15.88 17.33 18.57 19.64 20.58 21.42 34. The population of a lake of fish is modeled by the logistic equation P(t) =  16, 120 __ 1 + 25e-0.75t , where t is time in years. To the nearest hundredth, how many years will it take the lake to reach 80% of its carrying capacity? For the following exercises, use a graphing utility to create a scatter diagram of the data given in the table. Observe the shape of the scatter diagram to determine whether the data is best described by an exponential, logarithmic, or logistic model. Then use the appropriate regression feature to find an equation that models the data. When necessary, round values to five decimal places. x f (x) 21.6 29.2 36.4 46.6 55.7 72.6 87.1 107.2 138.1 x f (x) 13.98 17.84 20.01 22.7 24.1 26.15 27.37 28.38 29.97 31.07 31.43 x 0.5 1.5 f (x) 2.2 2.9 3.9 4.8 6.4 9.3 12.3 16.2 17.3 17.9
