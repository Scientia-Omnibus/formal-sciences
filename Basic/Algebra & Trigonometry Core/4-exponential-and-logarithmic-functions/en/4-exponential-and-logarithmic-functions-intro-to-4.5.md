# Exponential and Logarithmic Functions

## Introduction

---
Focus in on a square centimeter of your skin. Look closer. Closer still. If you could look closely enough, you would see hundreds of thousands of microscopic organisms. They are bacteria, and they are not only on your skin, but in your mouth, nose, and even your intestines. In fact, the bacterial cells in your body at any given moment outnumber your own cells. But that is no reason to feel bad about yourself. While some bacteria can cause illness, many are healthy and even essential to the body. Bacteria commonly reproduce through a process called binary fission, during which one bacterial cell splits into two. When conditions are right, bacteria can reproduce very quickly. Unlike humans and other complex organisms, the time required to form a new generation of bacteria is often a matter of minutes or hours, as opposed to days or years.[16] For simplicity’s sake, suppose we begin with a culture of one bacterial cell that can divide every hour. Table 1 shows the number of bacterial cells at the end of each subsequent hour. We see that the single bacterial cell leads to over one thousand bacterial cells in just ten hours! And if we were to extrapolate the table to twenty-four hours, we would have over 16 million! Hour Bacteria In this chapter, we will explore exponential functions, which can be used for, among other things, modeling growth patterns such as those found in bacteria. We will also investigate logarithmic functions, which are closely related to exponential functions. Both types of functions have numerous real-world applications when it comes to modeling and interpreting data. 16. Todar, PhD, Kenneth. Todar’s Online Te xtbook of Bacteriology. http://te xtbookofbacteriology.net/growth_3.html. Exponential and ­Logarithmic Functions

Learning Objectives
In this section, you will:
• Evaluate exponential functions.
• Find the equation of an exponential function.
• Use compound interest formulas.
• Evaluate exponential functions with base e.

## 4.1 Exponential Functions

---
India is the second most populous country in the world with a population of about 1.25 billion people in 2013. The population is growing at a rate of about 1.2% each year[17]. If this rate continues, the population of India will e xceed China’s population by the year 2031. When populations grow rapidly, we often say that the growth is “exponential,” meaning that something is growing very rapidly. To a mathematician, however, the term exponential growth has a very specific meaning. In this section, we will take a look at exponential functions, which model this kind of rapid growth. Identifying Exponential Functions When exploring linear growth, we observed a constant rate of change—a constant number by which the output increased for each unit increase in input. For example, in the equation f (x) = 3x + 4, the slope tells us the output increases by 3 each time the input increases by 1. The scenario in the India population example is different because we have a percent change per unit time (rather than a constant change) in the number of people. Defining an Exponential Function A study found that the percent of the population who are vegans in the United States doubled from 2009 to 2011. In 2011, 2.5% of the population was vegan, adhering to a diet that does not include any animal products—no meat, poultry, fish, dairy, or eggs. If this rate continues, vegans will make up 10% of the U.S. population in 2015, 40% in 2019, and What exactly does it mean to grow exponentially? What does the word double have in common with percent increase? People toss these words around errantly. Are these words used correctly? The words certainly appear frequently in the media. • Percent change refers to a change based on a percent of the original amount. • Exponential growth refers to an increase based on a constant multiplicative rate of change over equal increments of time, that is, a percent increase of the original amount over time. • Exponential decay refers to a decrease based on a constant multiplicative rate of change over equal increments of time, that is, a percent decrease of the original amount over time. For us to gain a clear understanding of exponential growth, let us contrast exponential growth with linear growth. We will construct two functions. The first function is exponential. We will start with an input of 0, and increase each input by 1. We will double the corresponding consecutive outputs. The second function is linear. We will start with an input of 0, and increase each input by 1. We will add 2 to the corresponding consecutive outputs. See Table 1. x f (x) = 2x g(x) = 2x 17. http://www.worldometers.info/world-population/. Accessed February 24, 2014.

From Table 1 we can infer that for these two functions, exponential growth dwarfs linear growth. • Exponential growth refers to the original value from the range increases by the same percentage over equal increments found in the domain. • Linear growth refers to the original value from the range increases by the same amount over equal increments found in the domain. Apparently, the difference between “the same percentage” and “the same amount” is quite significant. For exponential growth, over equal increments, the constant multiplicative rate of change resulted in doubling the output whenever the input increased by one. For linear growth, the constant additive rate of change over equal increments resulted in adding 2 to the output whenever the input was increased by one. The general form of the exponential function is f (x) = ab x, where a is any nonzero number, b is a positive real number not equal to 1. • If b > 1, the function grows at a rate proportional to its size. • If 0 < b < 1, the function decays at a rate proportional to its size. Let’s look at the function f (x) = 2x from our example. We will create a table (Table 2) to determine the corresponding outputs over an interval in the domain from -3 to 3. x -3 -2 -1 f (x) = 2x 2-3 =  1/8  2-2 =  1/4  2-1 =  1/2  Let us examine the graph of f by plotting the ordered pairs we observe on the table in Figure 1, and then make a few observations. f(x) = 2x y = 0 x y 2) Let’s define the behavior of the graph of the exponential function f (x) = 2x and highlight some its key characteristics. • the domain is (-∞ , ∞ ), • the range is (0, ∞ ), • as x → ∞ , f (x) → ∞ , • as x → -∞ , f (x) → 0, • f (x) is always increasing, • the graph of f (x) will never touch the x-axis because base two raised to any exponent never has the result of zero. • y = 0 is the horizontal asymptote. • the y-intercept is 1.

exponential function For any real number x, an exponential function is a function with the form f (x) = ab x where • a is the a non-zero real number called the initial value and • b is any positive real number such that b ≠  1. • The domain of f is all real numbers. • The range of f is all positive real numbers if a > 0. • The range of f is all negative real numbers if a < 0. • The y-intercept is (0, a), and the horizontal asymptote is y = 0.

---
### 📐 **Example  1**: Identifying Exponential Functions

Which of the following equations are not exponential functions? f (x) = 43(x - 2) g (x) = x³ h (x) = (  1/3  ) x j (x) = (-2)x

**Solution**

B y definition, an exponential function has a constant as a base and an independent variable as an exponent. Thus, g(x) = x³ does not represent an exponential function because the base is an independent variable. In fact, g(x) = x³ is a power function. Recall that the base b of an exponential function is always a positive constant, and b ≠  1. Thus, j(x) = (-2)x does not represent an exponential function because the base, -2, is less than 0.

---
### ✏️ **Try It #1**
Which of the following equations represent exponential functions? • f (x) = 2x² - 3x + 1 • g(x) = 0.875x • h(x) = 1.75x + 2 Evaluating Exponential Functions Recall that the base of an exponential function must be a positive real number other than 1. Why do we limit the base b to positive values? To ensure that the outputs will be real numbers. Observe what happens if the base is not positive: • Let b = -9 and x =  1/2 . Then f (x) = f (  1/2  ) = (-9)  1/2  = √-9 , which is not a real number. Why do we limit the base to positive values other than 1? Because base 1 results in the constant function. Observe what happens if the base is 1: • Let b = 1. Then f (x) = 1x = 1 for any value of x. To evaluate an exponential function with the form f (x) = b x, we simply substitute x with the given value, and calculate the resulting power. For example: Let f (x) = 2x. What is f (3)?

f (x) = 2x

f (3) = 23 Substitute x = 3.

= 8 Evaluate the power. To evaluate an exponential function with a form other than the basic form, it is important to follow the order of operations.

For example: Let f (x) = 30(2)x. What is f (3)?

f (x) = 30(2)x

Substitute x = 3.

Simplify the power first.

= 240 Multiply. Note that if the order of operations were not followed, the result would be incorrect:

---
### 📐 **Example  2**: Evaluating Exponential Functions

Let f (x) = 5(3)x + 1. Evaluate f (2) without using a calculator.

**Solution**

Follow the order of operations. Be sure to pay attention to the parentheses.

f (x) = 5(3)x + 1

f (2) = 5(3)² + 1 Substitute x = 2.

Add the exponents.

Simplify the power.

= 135 Multiply.

---
### ✏️ **Try It #2**
Let f (x) = 8(1.2)x - 5. Evaluate f (3) using a calculator. Round to four decimal places. Defining Exponential Growth Because the output of exponential functions increases very rapidly, the term “exponential growth” is often used in everyday language to describe anything that grows or increases rapidly. However, exponential growth can be defined more precisely in a mathematical sense. If the growth rate is proportional to the amount present, the function models exponential growth. exponential growth A function that models exponential growth grows by a rate proportional to the amount present. For any real number x and any positive real numbers a and b such that b ≠  1, an exponential growth function has the form f (x) = ab x where • a is the initial or starting value of the function. • b is the growth factor or growth multiplier per unit x. In more general terms, we have an exponential function, in which a constant base is raised to a variable exponent. To differentiate between linear and exponential functions, let’s consider two companies, A and B. Company A has 100 stores and expands by opening 50 new stores a year, so its growth can be represented by the function A(x) = 100 + 50x. Company B has 100 stores and expands by increasing the number of stores by 50% each year, so its growth can be represented by the function B(x) = 100(1 + 0.5)x. A few years of growth for these companies are illustrated in Table 3. Year, x Stores, Company A Stores, Company B x A(x) = 100 + 50x B(x) = 100(1 + 0.5)x

The graphs comparing the number of stores for each company over a five-year period are shown in Figure 2. We can see that, with exponential growth, the number of stores increases much more rapidly than with linear growth. Years Number of Stores x y B(x) = 100(1 + 0.5)x A(x) = 100 + 50x Notice that the domain for both functions is [0, ∞ ), and the range for both functions is [100, ∞ ). After year 1, Company B always has more stores than Company A. Now we will turn our attention to the function representing the number of stores for Company B, B(x) = 100(1 + 0.5)x. In this exponential function, 100 represents the initial number of stores, 0.50 represents the growth rate, and 1 + 0.5 = 1.5 represents the growth factor. Generalizing further, we can write this function as B(x) = 100(1.5)x, where 100 is the initial value, 1.5 is called the base, and x is called the exponent.

---
### 📐 **Example  3**: Evaluating a Real-World Exponential Model

At the beginning of this section, we learned that the population of India was about 1.25 billion in the year 2013, with an annual growth rate of about 1.2%. This situation is represented by the growth function P(t) = 1.25(1.012)t, where t is the number of years since 2013. To the nearest thousandth, what will the population of India be in 2031?

**Solution**

To estimate the population in 2031, we evaluate the models for t = 18, because 2031 is 18 years after 2013. Rounding to the nearest thousandth, There will be about 1.549 billion people in India in the year 2031.

---
### ✏️ **Try It #3**
The population of China was about 1.39 billion in the year 2013, with an annual growth rate of about 0.6%. This situation is represented by the growth function P(t) = 1.39(1.006)t, where t is the number of years since 2013. To the nearest thousandth, what will the population of China be for the year 2031? How does this compare to the population prediction we made for India in Example 3? Finding Equations of Exponential Functions In the previous examples, we were given an exponential function, which we then evaluated for a given input. Sometimes we are given information about an exponential function without knowing the function explicitly. We must use the information to first write the form of the function, then determine the constants a and b, and evaluate the function.

---
### 💡 **How To…**
Given two data points, write an exponential model. 1. If one of the data points has the form (0, a), then a is the initial value. Using a, substitute the second point into the equation f (x) = a(b)x, and solve for b. 2. If neither of the data points have the form (0, a), substitute both points into two equations with the form f (x) = a(b)x. Solve the resulting system of two equations in two unknowns to find a and b. 3. Using the a and b found in the steps above, write the exponential function in the form f (x) = a(b)x.

---
### 📐 **Example  4**: Writing an Exponential Model When the Initial Value Is Known

In 2006, 80 deer were introduced into a wildlife refuge. By 2012, the population had grown to 180 deer. The population was growing exponentially. Write an algebraic function N(t) representing the population (N) of deer over time t.

**Solution**

We let our independent variable t be the number of years after 2006. Thus, the information given in the problem can be written as input-output pairs: (0, 80) and (6, 180). Notice that by choosing our input variable to be measured as years after 2006, we have given ourselves the initial value for the function, a = 80. We can now substitute the second point into the equation N(t) = 80bt to find b:

N(t) = 80b t

Substitute using point (6, 180).

 9/4  = b 6 Divide and write in lowest terms.

b = (  9/4  )  1/6  Isolate b using properties of exponents.

Round to 4 decimal places. NOTE: Unless otherwise stated, do not round any intermediate calculations. Then round the final answer to four places for the remainder of this section. The exponential model for the population of deer is N(t) = 80(1.1447)t. (Note that this exponential function models short-term growth. As the inputs gets large, the output will get increasingly larger, so much so that the model may not be useful in the long term.) We can graph our model to observe the population growth of deer in the refuge over time. Notice that the graph in for the function is [0, ∞ ), and the range for the function is [80, ∞ ). Years Deer Population t N(t)

---
### ✏️ **Try It #4**
A wolf population is growing exponentially. In 2011, 129 wolves were counted. By 2013, the population had reached 236 wolves. What two points can be used to derive an exponential equation modeling this situation? Write the equation representing the population N of wolves over time t.

---
### 📐 **Example  5**: Writing an Exponential Model When the Initial Value is Not Known

Find an exponential function that passes through the points (-2, 6) and (2, 1).

**Solution**

Because we don’t have the initial value, we substitute both points into an equation of the form f (x) = ab x, and then solve the system for a and b. • Substituting (-2, 6) gives 6 = ab-2 • Substituting (2, 1) gives 1 = ab²

Use the first equation to solve for a in terms of b:

6 = ab-2

 6/b-2  = a Divide.

a = 6b 2 Use properties of exponents to rewrite the denominator. Substitute a in the second equation, and solve for b:

1 = ab 2

1 = 6b 2b 2 = 6b 4 Substitute a.

b = (  1/6  )  1/4  Use properties of exponents to isolate b.

Round 4 decimal places. Use the value of b in the first equation to solve for the value of a:

Thus, the equation is f (x) = 2.4492(0.6389)x. We can graph our model to check our work. Notice that the graph in Figure 4 passes through the initial points given in the problem, (-2, 6) and (2, 1). The graph is an example of an exponential decay function. x f(x)

---
### ✏️ **Try It #5**
Given the two points (1, 3) and (2, 4.5), find the equation of the exponential function that passes through these two points. Do two points always determine a unique exponential function? Yes, provided the two points are either both above the x-axis or both below the x-axis and have different x-coordinates. But keep in mind that we also need to know that the graph is, in fact, an exponential function. Not every graph that looks exponential really is exponential. We need to know the graph is based on a model that shows the same percent growth with each unit increase in x, which in many real world cases involves time.

---
### 💡 **How To…**
Given the graph of an exponential function, write its equation. 1. First, identify two points on the graph. Choose the y-intercept as one of the two points whenever possible. Try to choose points that are as far apart as possible to reduce round-off error. 2. If one of the data points is the y-intercept (0, a), then a is the initial value. Using a, substitute the second point into the equation f (x) = a(b)x, and solve for b. 3. If neither of the data points have the form (0, a), substitute both points into two equations with the form f (x) = a(b)x. Solve the resulting system of two equations in two unknowns to find a and b. 4. Write the exponential function, f (x) = a(b)x.

---
### 📐 **Example  6**: Writing an Exponential Function Given Its Graph

Find an equation for the exponential function graphed in Figure 5. x f(x) 0.5 1.5 2.5 3.5

**Solution**

We can choose the y-intercept of the graph, (0, 3), as our first point. This gives us the initial value, a = 3. Next, choose a point on the curve some distance away from (0, 3) that has integer coordinates. One such point is (2, 12).

y = ab x Write the general form of an exponential equation.

y = 3b x Substitute the initial value 3 for a.

Substitute in 12 for y and 2 for x.

4 = b² Divide by 3.

b = ± 2 Take the square root. Because we restrict ourselves to positive values of b, we will use b = 2. Substitute a and b into the standard form to yield the equation f (x) = 3(2)x.

---
### ✏️ **Try It #6**
Find an equation for the exponential function graphed in Figure 6. x f(x)

---
### 💡 **How To…**
Given two points on the curve of an exponential function, use a graphing calculator to find the equation. 1. Press [STAT]. 2. Clear any existing entries in columns L¹ or L². 3. In L¹, enter the x-coordinates given. 4. In L², enter the corresponding y-coordinates. 5. Press [STAT] again. Cursor right to CALC, scroll down to ExpReg (Exponential Regression), and press [ENTER]. 6. The screen displays the values of a and b in the exponential equation y = a ⋅ b x

---
### 📐 **Example  7**
Using a Graphing Calculator to Find an Exponential Function Use a graphing calculator to find the exponential equation that includes the points (2, 24.8) and (5, 198.4).

**Solution**

Follow the guidelines above. First press [STAT], [EDIT], [1: Edit...], and clear the lists L¹ and L². Next, in the L¹ column, enter the x-coordinates, 2 and 5. Do the same in the L² column for the y-coordinates, 24.8 and 198.4. Now press [STAT], [CALC], [0: ExpReg] and press [ENTER]. The values a = 6.2 and b = 2 will be displayed. The exponential equation is y = 6.2 ⋅ 2x.

---
### ✏️ **Try It #7**
Use a graphing calculator to find the exponential equation that includes the points (3, 75.98) and (6, 481.07).

### Applying the Compound-Interest Formula

Savings instruments in which earnings are continually reinvested, such as mutual funds and retirement accounts, use compound interest. The term compounding refers to interest earned not only on the original value, but on the accumulated value of the account. The annual percentage rate (APR) of an account, also called the nominal rate, is the yearly interest rate earned by an investment account. The term nominal is used when the compounding occurs a number of times other than once per year. In fact, when interest is compounded more than once a year, the effective interest rate ends up being greater than the nominal rate! This is a powerful tool for investing. We can calculate the compound interest using the compound interest formula, which is an exponential function of the variables time t, principal P, APR r, and number of compounding periods in a year n: A(t) = P ( 1 +  (r)/(n)  ) nt For example, observe Table 4, which shows the result of investing $1,000 at 10% for one year. Notice how the value of the account increases as the compounding frequency increases. Frequency Value after 1 year Annually $1100 Semiannually Quarterly Monthly Daily the compound interest formula Compound interest can be calculated using the formula A(t) = P ( 1 +  (r)/(n)  ) nt where • A(t) is the account value, • t is measured in years, • P is the starting amount of the account, often called the principal, or more generally present value, • r is the annual percentage rate (APR) expressed as a decimal, and • n is the number of compounding periods in one year.

---
### 📐 **Example  8**: Calculating Compound Interest

If we invest $3,000 in an investment account paying 3% interest compounded quarterly, how much will the account be worth in 10 years?

**Solution**

Because we are starting with $3,000, P = 3000. Our interest rate is 3%, so r = 0.03. Because we are compounding quarterly, we are compounding 4 times per year, so n = 4. We want to know the value of the account in 10 years, so we are looking for A(10), the value when t = 10.

A(t) = P ( 1 +  (r)/(n)  ) nt

Use the compound interest formula.

____ 4  ) Substitute using given values.

Round to two decimal places. The account will be worth about $4,045.05 in 10 years.

---
### ✏️ **Try It #8**
An initial investment of $100,000 at 12% interest is compounded weekly (use 52 weeks in a year). What will the investment be worth in 30 years?

---
### 📐 **Example  9**
Using the Compound Interest Formula to Solve for the Principal A 529 Plan is a college-savings plan that allows relatives to invest money to pay for a child’s future college tuition; the account grows tax-free. Lily wants to set up a 529 account for her new granddaughter and wants the account to grow to $40,000 over 18 years. She believes the account will earn 6% compounded semi-annually (twice a year). To the nearest dollar, how much will Lily need to invest in the account now?

**Solution**

The nominal interest rate is 6%, so r = 0.06. Interest is compounded twice a year, so n = 2. We want to find the initial investment, P, needed so that the value of the account will be worth $40,000 in 18 years. Substitute the given values into the compound interest formula, and solve for P.

A(t) = P ( 1 +  (r)/(n)  ) nt Use the compound interest formula.

____ 2  ) 2(18)

Substitute using given values A, r, n, and t.

Simplify.

______

Isolate P.

Divide and round to the nearest dollar. Lily will need to invest $13,801 to have $40,000 in 18 years.

---
### ✏️ **Try It #9**
Refer to Example 9. To the nearest dollar, how much would Lily need to invest if the account is compounded quarterly? Evaluating Functions with Base e As we saw earlier, the amount earned on an account increases as the compounding frequency increases. Table 5 shows that the increase from annual to semi-annual compounding is larger than the increase from monthly to daily compounding. This might lead us to ask whether this pattern will continue. Examine the value of $1 invested at 100% interest for 1 year, compounded at various frequencies, listed in Table 5. Frequency A(t) = ( 1 +  1/n  ) n Value Annually ( 1 +  1/1  ) $2 Semiannually ( 1 +  1/2  ) $2.25 Quarterly ( 1 +  1/4  ) Monthly ( 1 +  1/12  ) Daily ( 1 +  1/Hourly ( 1 +  1/Once per minute ( 1 +  _ Once per second ( 1 +  ________

These values appear to be approaching a limit as n increases without bound. In fact, as n gets larger and larger, the expression ( 1 +  1/n  ) n approaches a number used so frequently in mathematics that it has its own name: the letter e. This value is an irrational number, which means that its decimal expansion goes on forever without repeating. Its approximation to six decimal places is shown below. the number e The letter e represents the irrational number ( 1 +  1/n  ) n , as n increases without bound The letter e is used as a base for many real-world exponential models. To work with base e, we use the approximation, e ≈ 2.718282. The constant was named by the Swiss mathematician Leonhard Euler (1707–1783) who first investigated and discovered many of its properties.

---
### 📐 **Example  10**
Using a Calculator to Find Powers of e Calculate e³.14. Round to five decimal places.

**Solution**

On a calculator, press the button labeled [e x]. The window shows [e^(]. Type 3.14 and then close parenthesis, [)]. Press [ENTER]. Rounding to 5 decimal places, e 3.14 ≈ 23.10387. Caution: Many scientific calculators have an “Exp” button, which is used to enter numbers in scientific notation. It is not used to find powers of e.

---
### ✏️ **Try It #10**
Use a calculator to find e -0.5. Round to five decimal places. Investigating Continuous Growth So far we have worked with rational bases for exponential functions. For most real-world phenomena, however, e is used as the base for exponential functions. Exponential models that use e as the base are called continuous growth or decay models. We see these models in finance, computer science, and most of the sciences, such as physics, toxicology, and fluid dynamics. the continuous growth/decay formula For all real numbers t, and all positive numbers a and r, continuous growth or decay is represented by the formula A(t) = aert where • a is the initial value, • r is the continuous growth rate per unit time, • and t is the elapsed time. If r > 0, then the formula represents continuous growth. If r < 0, then the formula represents continuous decay. For business applications, the continuous growth formula is called the continuous compounding formula and takes the form A(t) = Pert where • P is the principal or the initial invested, • r is the growth or interest rate per unit time, • and t is the period or term of the investment.

---
### 💡 **How To…**
Given the initial value, rate of growth or decay, and time t, solve a continuous growth or decay function. 1. Use the information in the problem to determine a, the initial value of the function. 2. Use the information in the problem to determine the growth rate r. a. If the problem refers to continuous growth, then r > 0. b. If the problem refers to continuous decay, then r < 0. 3. Use the information in the problem to determine the time t. 4. Substitute the given information into the continuous growth formula and solve for A(t).

---
### 📐 **Example  11**: Calculating Continuous Growth

A person invested $1,000 in an account earning a nominal 10% per year compounded continuously. How much was in the account at the end of one year?

**Solution**

Since the account is growing in value, this is a continuous compounding problem with growth rate r = 0.10. The initial investment was $1,000, so P = 1000. We use the continuous compounding formula to find the value after t = 1 year:

A(t) = Pert Use the continuous compounding formula.

Substitute known values for P, r, and t.

Use a calculator to approximate. The account is worth $1,105.17 after one year.

---
### ✏️ **Try It #11**
A person invests $100,000 at a nominal 12% interest per year compounded continuously. What will be the value of the investment in 30 years?

---
### 📐 **Example  12**: Calculating Continuous Decay

Radon-222 decays at a continuous rate of 17.3% per day. How much will 100 mg of Radon-222 decay to in 3 days?

**Solution**

Since the substance is decaying, the rate, 17.3%, is negative. So, r = -0.173. The initial amount of radon- 222 was 100 mg, so a = 100. We use the continuous decay formula to find the value after t = 3 days:

A(t) = aert Use the continuous growth formula.

Substitute known values for a, r, and t.

Use a calculator to approximate. So 59.5115 mg of radon-222 will remain.

---
### ✏️ **Try It #12**
Using the data in Example 12, how much radon-222 will remain after one year? Access these online resources for additional instruction and practice with exponential functions. • Exponential Growth Function (http://openstaxcollege.org/l/expgrowth) • Compound Interest (http://openstaxcollege.org/l/compoundint)

### 4.1 section EXERCISES

Verbal 1. Explain why the values of an increasing exponential function will eventually overtake the values of an increasing linear function. 2. Given a formula for an exponential function, is it possible to determine whether the function grows or decays exponentially just by looking at the formula? Explain. 3. The Oxford Dictionary defines the word nominal as a value that is “stated or expressed but not necessarily corresponding exactly to the real value.”[18] Develop a reasonable argument for why the term nominal rate is used to describe the annual percentage rate of an investment account that compounds interest. Algebraic For the following exercises, identify whether the statement represents an exponential function. Explain. 4. The average annual population increase of a pack of wolves is 25. 5. A population of bacteria decreases by a factor of  1/8  every 24 hours. 6. The value of a coin collection has increased by 3.25% annually over the last 20 years. 7. For each training session, a personal trainer charges his clients $5 less than the previous training session. 8. The height of a projectile at time t is represented by the function h(t) = -4.9t 2 + 18t + 40. For the following exercises, consider this scenario: For each year t, the population of a forest of trees is represented by the function A(t) = 115(1.025)t. In a neighboring forest, the population of the same type of tree is represented by the function B(t) = 82(1.029)t. (Round answers to the nearest whole number.) 9. Which forest’s population is growing at a faster rate? 10. Which forest had a greater number of trees initially? By how many? 11. Assuming the population growth models continue to represent the growth of the forests, which forest will have a greater number of trees after 20 years? By how many? 12. Assuming the population growth models continue to represent the growth of the forests, which forest will have a greater number of trees after 100 years? By how many? 13. Discuss the above results from the previous four exercises. Assuming the population growth models continue to represent the growth of the forests, which forest will have the greater number of trees in the long run? Why? What are some factors that might influence the long-term validity of the exponential growth model? For the following exercises, determine whether the equation represents exponential growth, exponential decay, or neither. Explain. _ x  For the following exercises, find the formula for an exponential function that passes through the two points given. _ 2  ) and (3, 24) 18. Oxford Dictionary. http://oxforddictionaries.com/us/definition/american_english/nominal.

## 4.1 Section Exercises

---
For the following exercises, determine whether the table could represent a function that is linear, exponential, or neither. If it appears to be exponential, find a function that passes through the points. x f (x) -20

x h(x) 34.3 24.01

x m (x) 42.9 25.61

x f (x)

x g (x) -3.25 7.25 12.5 For the following exercises, use the compound interest formula, A(t) = P ( 1 +  (r)/(n)  ) nt. 28. After a certain number of years, the value of an investment account is represented by the equation ____ 12  ) 120. What is the value of the account? 29. What was the initial deposit made to the account in the previous exercise? 30. How many years had the account from the previous exercise been accumulating interest? 31. An account is opened with an initial deposit of $6,500 and earns 3.6% interest compounded semi-annually. What will the account be worth in 20 years? 32. How much more would the account in the previous exercise have been worth if the interest were compounding weekly? 33. Solve the compound interest formula for the principal, P. 34. Use the formula found in Exercise #31 to calculate the initial deposit of an account that is worth $14,472.74 after earning 5.5% interest compounded monthly for 5 years. (Round to the nearest dollar.) 35. How much more would the account in Exercises #31 and #34 be worth if it were earning interest for 5 more years? 36. Use properties of rational exponents to solve the compound interest formula for the interest rate, r. 37. Use the formula found in the previous exercise to calculate the interest rate for an account that was compounded semi-annually, had an initial deposit of $9,000 and was worth $13,373.53 after 10 years. 38. Use the formula found in the previous exercise to calculate the interest rate for an account that was compounded monthly, had an initial deposit of $5,500, and was worth $38,455 after 30 years. For the following exercises, determine whether the equation represents continuous growth, continuous decay, or neither. Explain. _ t  42. Suppose an investment account is opened with an initial deposit of $12,000 earning 7.2% interest compounded continuously. How much will the account be worth after 30 years? 43. How much less would the account from Exercise 42 be worth after 30 years if it were compounded monthly instead? Numeric For the following exercises, evaluate each function. Round answers to four decimal places, if necessary. 44. f (x) = 2(5)x, for f (-3) 45. f (x) = -42x + 3, for f (-1) 46. f (x) = e x, for f (3) 47. f (x) = -2e x - 1, for f (-1) 48. f (x) = 2.7(4)-x + 1 + 1.5, for f (-2) 49. f (x) = 1.2e²x - 0.3, for f (3) 50. f (x) = - 3/2 (3)-x +  3/2 , for f (2)

Technology For the following exercises, use a graphing calculator to find the equation of an exponential function given the points on the curve. Extensions 56. The annual percentage yield (APY) of an investment account is a representation of the actual interest rate earned on a compounding account. It is based on a compounding period of one year. Show that the APY of an account that compounds monthly can be found with the formula APY = ( 1 +  r/12  ) 57. Repeat the previous exercise to find the formula for the APY of an account that compounds daily. Use the results from this and the previous exercise to develop a function I(n) for the APY of any account that compounds n times per year. 58. Recall that an exponential function is any equation written in the form f (x) = a . b x such that a and b are positive numbers and b ≠  1. Any positive number b can be written as b = en for some value of n. Use this fact to rewrite the formula for an exponential function that uses the number e as a base. 59. In an exponential decay function, the base of the exponent is a value between 0 and 1. Thus, for some number b > 1, the exponential decay function can be written as f (x) = a . (  1/b  ) x . Use this formula, along with the fact that b = e n, to show that an exponential decay function takes the form f (x) = a(e)-nx for some positive number n. 60. The formula for the amount A in an investment account with a nominal interest rate r at any time t is given by A(t) = a(e)rt, where a is the amount of principal initially deposited into an account that compounds continuously. Prove that the percentage of interest earned to principal at any time t can be calculated with the formula I(t) = e rt - 1. Real-World Applications 61. The fox population in a certain region has an annual growth rate of 9% per year. In the year 2012, there were 23,900 fox counted in the area. What is the fox population predicted to be in the year 2020? 62. A scientist begins with 100 milligrams of a radioactive substance that decays exponentially. After 35 hours, 50 mg of the substance remains. How many milligrams will remain after 54 hours? 63. In the year 1985, a house was valued at $110,000. By the year 2005, the value had appreciated to $145,000. What was the annual growth rate between 1985 and 2005? Assume that the value continued to grow by the same percentage. What was the value of the house in the year 2010? 64. A car was valued at $38,000 in the year 2007. By 2013, the value had depreciated to $11,000 If the car’s value continues to drop by the same percentage, what will it be worth by 2017? 65. Jamal wants to save $54,000 for a down payment on a home. How much will he need to invest in an account with 8.2% APR, compounding daily, in order to reach his goal in 5 years? 66. Kyoko has $10,000 that she wants to invest. Her bank has several investment accounts to choose from, all compounding daily. Her goal is to have $15,000 by the time she finishes graduate school in 6 years. To the nearest hundredth of a percent, what should her minimum annual interest rate be in order to reach her goal? (Hint : solve the compound interest formula for the interest rate.) 67. Alyssa opened a retirement account with 7.25% APR in the year 2000. Her initial deposit was $13,500. How much will the account be worth in 2025 if interest compounds monthly? How much more would she make if interest compounded continuously? 68. An investment account with an annual interest rate of 7% was opened with an initial deposit of $4,000 Compare the values of the account after 9 years when the interest is compounded annually, quarterly, monthly, and continuously.

## 4.2 Graphs of Exponential Functions

---
Learning Objectives
In this section, you will:
• Graph exponential functions.
• Graph exponential functions using transformations.
As we discussed in the previous section, exponential functions are used for many real-world applications such as finance, forensics, computer science, and most of the life sciences. Working with an equation that describes a real- world situation gives us a method for making predictions. Most of the time, however, the equation itself is not enough. We learn a lot about things by seeing their pictorial representations, and that is exactly why graphing exponential equations is a powerful tool. It gives us another layer of insight for predicting future events. Graphing Exponential Functions Before we begin graphing, it is helpful to review the behavior of exponential growth. Recall the table of values for a function of the form f (x) = b x whose base is greater than one. We’ll use the function f (x) = 2x. Observe how the output values in Table 1 change as the input increases by 1. x -3 -2 -1 f (x) = 2x  1/8   1/4   1/2  Each output value is the product of the previous output and the base, 2. We call the base 2 the constant ratio. In fact, for any exponential function with the form f (x) = ab x, b is the constant ratio of the function. This means that as the input increases by 1, the output value will be the product of the base and the previous output, regardless of the value of a. Notice from the table that • the output values are positive for all values of x; • as x increases, the output values increase without bound; and • as x decreases, the output values grow smaller, approaching zero. Te x-axis is an asymptote. f (x) = 2x -3, -2, -1, x f(x) The domain of f (x) = 2x is all real numbers, the range is (0, ∞ ), and the horizontal asymptote is y = 0. To get a sense of the behavior of exponential decay, we can create a table of values for a function of the form f (x) = b x whose base is between zero and one. We’ll use the function g(x) = (  1/2  ) x . Observe how the output values in Table 2 change as the input increases by 1.

x -3 -2 -1 g(x) = (  1/2  ) x  1/2   1/4   1/8  Again, because the input is increasing by 1, each output value is the product of the previous output and the base, or constant ratio  1/2 . Notice from the table that • the output values are positive for all values of x; • as x increases, the output values grow smaller, approaching zero; and • as x decreases, the output values grow without bound. _ 2  ) x . g(x) = 1 x Te x-axis is an asymptote. x g(x) The domain of g(x) = (  1/2  ) x  is all real numbers, the range is (0, ∞ ), and the horizontal asymptote is y = 0. characteristics of the graph of the parent function f (x) = b x An exponential function with the form f (x) = b x, b > 0, b ≠  1, has these characteristics: • one-to-one function • horizontal asymptote: y = 0 • domain: (–∞ , ∞ ) • range: (0, ∞ ) • x-intercept: none • y-intercept: (0, 1) • increasing if b > 1 • decreasing if b < 1 growth and decay functions. (1, b) (1, b) x x f(x) f (x) = bx b > 1 f (x) = bx 0 < b < 1 f(x)

---
### 💡 **How To…**
Given an exponential function of the form f (x) = b x, graph the function. 1. Create a table of points. 2. Plot at least 3 point from the table, including the y-intercept (0, 1). 3. Draw a smooth curve through the points. 4. State the domain, (-∞ , ∞ ), the range, (0, ∞ ), and the horizontal asymptote, y = 0.

---
### 📐 **Example  1**: Sketching the Graph of an Exponential Function of the Form f (x) = b x

Sketch a graph of f (x) = 0.25x. State the domain, range, and asymptote.

**Solution**

Before graphing, identify the behavior and create a table of points for the graph. • Since b = 0.25 is between zero and one, we know the function is decreasing. The left tail of the graph will increase without bound, and the right tail will approach the asymptote y = 0. • Create a table of points as in Table 3. x -3 -2 -1 f (x) = 0.25x 0.25 • Plot the y-intercept, (0, 1), along with two other points. We can use (-1, 4) and (1, 0.25). Draw a smooth curve connecting the points as in Figure 4. f(x) = 0.25x x f(x) The domain is (-∞ , ∞ ); the range is (0, ∞ ); the horizontal asymptote is y = 0.

---
### ✏️ **Try It #1**
Sketch the graph of f (x) = 4x. State the domain, range, and asymptote. Graphing Transformations of Exponential Functions Transformations of exponential graphs behave similarly to those of other functions. Just as with other parent functions, we can apply the four types of transformations—shifts, reflections, stretches, and compressions—to the parent function f (x) = b x without loss of shape. For instance, just as the quadratic function maintains its parabolic shape when shifted, reflected, stretched, or compressed, the exponential function also maintains its general shape regardless of the transformations applied. Graphing a Vertical Shift The first transformation occurs when we add a constant d to the parent function f (x) = b x, giving us a vertical shift d units in the same direction as the sign. For example, if we begin by graphing a parent function, f (x) = 2x, we can then graph two vertical shifts alongside it, using d = 3: the upward shift, g(x) = 2x + 3 and the downward shift, h(x) = 2x - 3. Both vertical shifts are shown in Figure 5. g(x) = 2x + 3 f (x) = 2x h(x) = 2x - 3 y = 3 y = -3 y = 0 x y

Observe the results of shifting f (x) = 2x vertically: • The domain, (-∞ , ∞ ) remains unchanged. • When the function is shifted up 3 units to g(x) = 2x + 3: ◦ ◦The y-intercept shifts up 3 units to (0, 4). ◦ ◦The asymptote shifts up 3 units to y = 3. ◦ ◦The range becomes (3, ∞ ). • When the function is shifted down 3 units to h(x) = 2x - 3: ◦ ◦The y-intercept shifts down 3 units to (0, -2). ◦ ◦The asymptote also shifts down 3 units to y = -3. ◦ ◦The range becomes (-3, ∞ ). Graphing a Horizontal Shift The next transformation occurs when we add a constant c to the input of the parent function f (x) = b x, giving us a horizontal shift c units in the opposite direction of the sign. For example, if we begin by graphing the parent function f (x) = 2x, we can then graph two horizontal shifts alongside it, using c = 3: the shift left, g(x) = 2x + 3, and the shift right, h (x) = 2x - 3. Both horizontal shifts are shown in Figure 6. x y g(x) = 2x + 3 f (x) = 2x h(x) = 2x - 3 y = 0 Observe the results of shifting f (x) = 2x horizontally: • The domain, (-∞ , ∞ ), remains unchanged. • The asymptote, y = 0, remains unchanged. • The y-intercept shifts such that: ◦ ◦When the function is shifted left 3 units to g(x) = 2x + 3, the y-intercept becomes (0, 8). This is because 2x + 3 = (8)²x, so the initial value of the function is 8. ◦ ◦When the function is shifted right 3 units to h(x) = 2x - 3, the y-intercept becomes ( 0,  1/8  ). Again, see that 2x - 3 = (  1/8  )2x, so the initial value of the function is  1/8 . shifts of the parent function f (x) = b x For any constants c and d, the function f (x) = b x + c + d shifts the parent function f (x) = b x • vertically d units, in the same direction of the sign of d. • horizontally c units, in the opposite direction of the sign of c. • The y-intercept becomes (0, bc + d). • The horizontal asymptote becomes y = d. • The range becomes (d, ∞ ). • The domain, (-∞ , ∞ ), remains unchanged.

---
### 💡 **How To…**
Given an exponential function with the form f (x) = b x + c + d, graph the translation. 1. Draw the horizontal asymptote y = d. 2. Identify the shift as (-c, d). Shift the graph of f (x) = b x left c units if c is positive, and right c units if c is negative. 3. Shift the graph of f (x) = b x up d units if d is positive, and down d units if d is negative. 4. State the domain, (-∞ , ∞ ), the range, (d, ∞ ), and the horizontal asymptote y = d.

---
### 📐 **Example  2**: Graphing a Shift of an Exponential Function

Graph f (x) = 2x + 1 - 3. State the domain, range, and asymptote.

**Solution**

We have an exponential equation of the form f (x) = b x + c + d, with b = 2, c = 1, and d = -3. Draw the horizontal asymptote y = d, so draw y = -3. Identify the shift as (-c, d), so the shift is (-1, -3). Shift the graph of f (x) = b x left 1 units and down 3 units. x f (x) f (x) = 2x + 1 - 3 y = -3 The domain is (-∞ , ∞ ); the range is (-3, ∞ ); the horizontal asymptote is y = -3.

---
### ✏️ **Try It #2**
Graph f (x) = 2x - 1 + 3. State domain, range, and asymptote.

---
### 💡 **How To…**
Given an equation of the form f (x) = b x + c + d for x, use a graphing calculator to approximate the solution. 1. Press [Y=]. Enter the given exponential equation in the line headed “Y¹=”. 2. Enter the given value for f (x) in the line headed “Y²=”. 3. Press [WINDOW]. Adjust the y-axis so that it includes the value entered for “Y²=”. 4. Press [GRAPH] to observe the graph of the exponential function along with the line for the specified value of f (x). 5. To find the value of x, we compute the point of intersection. Press [2ND] then [CALC]. Select “intersect” and press [ENTER] three times. The point of intersection gives the value of x for the indicated value of the function.

---
### 📐 **Example  3**
Approximating the

**Solution**

of an Exponential Equation Solve 42 = 1.2(5)x + 2.8 graphically. Round to the nearest thousandth.

**Solution**

Press [Y=] and enter 1.2(5)x + 2.8 next to Y¹=. Then enter 42 next to Y²=. For a window, use the values -3 to 3 for x and -5 to 55 for y. Press [GRAPH]. The graphs should intersect somewhere near x = 2. For a better approximation, press [2ND] then [CALC]. Select [5: intersect] and press [ENTER] three times. The x-coordinate of the point of intersection is displayed as 2.1661943. (Your answer may be different if you use a different window or use a different value for Guess?) To the nearest thousandth, x ≈ 2.166.

---
### ✏️ **Try It #3**
Solve 4 = 7.85(1.15)x - 2.27 graphically. Round to the nearest thousandth. Graphing a Stretch or Compression While horizontal and vertical shifts involve adding constants to the input or to the function itself, a stretch or compression occurs when we multiply the parent function f (x) = b x by a constant ∣ a ∣ > 0. For example, if we begin by graphing the parent function f (x) = 2x, we can then graph the stretch, using a = 3, to get g(x) = 3(2)x as shown on the left in Figure 8, and the compression, using a =  1/3 , to get h(x) =  1/3 (2)x as shown on the right in Figure 8. x y Vertical stretch Vertical compression (a) (b) x y g(x) = 3(2)x f (x) = 2x f (x) = 2x y = 0 y = 0 h(x) = (2)x (b) h(x) =  1/3 (2)x compresses the graph of f (x) = 2x vertically by a factor of  1/3 . stretches and compressions of the parent function f ( x ) = b x For any factor a > 0, the function f (x) = a(b)x • is stretched vertically by a factor of a if ∣ a ∣ > 1. • is compressed vertically by a factor of a if ∣ a ∣ < 1. • has a y-intercept of (0, a). • has a horizontal asymptote at y = 0, a range of (0, ∞ ), and a domain of (-∞ , ∞ ), which are unchanged from the parent function.

---
### 📐 **Example  4**: Graphing the Stretch of an Exponential Function

Sketch a graph of f (x) = 4 (  1/2  ) x. State the domain, range, and asymptote.

**Solution**

Before graphing, identify the behavior and key points on the graph. • Since b =  1/2  is between zero and one, the left tail of the graph will increase without bound as x decreases, and the right tail will approach the x-axis as x increases. • Since a = 4, the graph of f (x) = (  1/2  ) x will be stretched by a factor of 4. • Create a table of points as shown in Table 4. x -3 -2 -1 f (x) = 4(  1/2  ) x 0.5 • Plot the y-intercept, (0, 4), along with two other points. We can use (-1, 8) and (1, 2).

Draw a smooth curve connecting the points, as shown in Figure 9. x f(x) y = 0 f (x) = 4 1 x The domain is (-∞ , ∞ ); the range is (0, ∞ ); the horizontal asymptote is y = 0.

---
### ✏️ **Try It #4**
Sketch the graph of f (x) =  1/2 (4)x. State the domain, range, and asymptote. Graphing Reflections In addition to shifting, compressing, and stretching a graph, we can also reflect it about the x-axis or the y-axis. When we multiply the parent function f (x) = b x by -1, we get a reflection about the x-axis. When we multiply the input by -1, we get a reflection about the y-axis. For example, if we begin by graphing the parent function f (x) = 2x, we can then graph the two reflections alongside it. The reflection about the x-axis, g(x) = -2x, is shown on the left side of Figure 10, and the reflection about the y-axis h(x) = 2-x, is shown on the right side of Figure 10. x y Reflection about the x-axis Reflection about the y-axis x y f (x) = 2x f (x) = 2x h(x) = 2-x g(x) = -2x y = 0 y = 0 reflections of the parent function f (x) = b x The function f (x) = -b x • reflects the parent function f (x) = b x about the x-axis. • has a y-intercept of (0, -1). • has a range of (-∞ , 0). • has a horizontal asymptote at y = 0 and domain of (-∞ , ∞ ), which are unchanged from the parent function. The function f (x) = b-x • reflects the parent function f (x) = b x about the y-axis. • has a y-intercept of (0, 1), a horizontal asymptote at y = 0, a range of (0, ∞ ), and a domain of (-∞ , ∞ ), which are unchanged from the parent function.

---
### 📐 **Example  5**: Writing and Graphing the Reflection of an Exponential Function

Find and graph the equation for a function, g (x), that reflects f (x) = (  1/4  ) x about the x-axis. State its domain, range, and asymptote.

**Solution**

Since we want to reflect the parent function f (x) = (  1/4  ) x about the x-axis, we multiply f (x) by -1 to get, g (x) = -(  1/4  ) x . Next we create a table of points as in Table 5. x -3 -2 -1 g(x) = - (  1/4  ) x -64 -16 -4 -1 -0.25 Plot the y-intercept, (0, -1), along with two other points. We can use (-1, -4) and (1, -0.25). Draw a smooth curve connecting the points: x g(x) y = 0 g(x) = -1 x The domain is (-∞ , ∞ ); the range is (-∞ , 0); the horizontal asymptote is y = 0.

---
### ✏️ **Try It #5**
Find and graph the equation for a function, g(x), that reflects f (x) = 1.25 x about the y-axis. State its domain, range, and asymptote. Summarizing Translations of the Exponential Function Now that we have worked with each type of translation for the exponential function, we can summarize them in Table 6 to arrive at the general equation for translating exponential functions. Translations of the Parent Function f (x) = b x Translation Form Shift • Horizontally c units to the left • Vertically d units up f (x) = b x + c + d Stretch and Compress • Stretch if | a | > 1 • Compression if 0 < | a | < 1 f (x) = ab x Reflect about the x-axis f (x) = -b x Reflect about the y-axis f (x) = b-x = (  1/b  ) x General equation for all translations f (x) = ab x + c + d

translations of exponential functions A translation of an exponential function has the form f (x) = ab x + c + d Where the parent function, y = b x, b > 1, is • shifted horizontally c units to the left. • stretched vertically by a factor of ∣ a ∣ if ∣ a ∣ > 0. • compressed vertically by a factor of ∣ a ∣ if 0 < ∣ a ∣ < 1. • shifted vertically d units. • reflected about the x-axis when a < 0. Note the order of the shifts, transformations, and reflections follow the order of operations.

---
### 📐 **Example  6**: Writing a Function from a Description

Write the equation for the function described below. Give the horizontal asymptote, the domain, and the range. • f (x) = e x is vertically stretched by a factor of 2, reflected across the y-axis, and then shifted up 4 units.

**Solution**

We want to find an equation of the general form f (x) = ab x + c + d. We use the description provided to find a, b, c, and d. • We are given the parent function f (x) = e x, so b = e. • The function is stretched by a factor of 2, so a = 2. • The function is reflected about the y-axis. We replace x with -x to get: e-x. • The graph is shifted vertically 4 units, so d = 4. Substituting in the general form we get, f (x) = ab x + c + d

= 2e-x + 0 + 4

= 2e-x + 4 The domain is (-∞ , ∞ ); the range is (4, ∞ ); the horizontal asymptote is y = 4.

---
### ✏️ **Try It #6**
Write the equation for function described below. Give the horizontal asymptote, the domain, and the range. • f (x) = e x is compressed vertically by a factor of  1/3 , reflected across the x-axis and then shifted down 2 units.

> Access this online resource for additional instruction and practice with graphing exponential functions. • Graph Exponential Functions (http://openstaxcollege.org/l/graphexpfunc)

4.2 Section EXERCISES Verbal 1. What role does the horizontal asymptote of an exponential function play in telling us about the end behavior of the graph? 2. What is the advantage of knowing how to recognize transformations of the graph of a parent function algebraically? Algebraic 3. The graph of f (x) = 3x is reflected about the y-axis and stretched vertically by a factor of 4. What is the equation of the new function, g(x)? State its y-intercept, domain, and range. 4. The graph of f (x) = (  1/2  ) -x is reflected about the y-axis and compressed vertically by a factor of  1/5 . What is the equation of the new function, g(x)? State its y-intercept, domain, and range. 5. The graph of f (x) = 10x is reflected about the x-axis and shifted upward 7 units. What is the equation of the new function, g(x)? State its y-intercept, domain, and range. 6. The graph of f (x) = (1.68)x is shifted right 3 units, stretched vertically by a factor of 2, reflected about the x-axis, and then shifted downward 3 units. What is the equation of the new function, g(x)? State its y-intercept (to the nearest thousandth), domain, and range. 7. The graph of f (x) = - 1/2 (  1/4  ) x - 2+ 4 is shifted downward 4 units, and then shifted left 2 units, stretched vertically by a factor of 4, and reflected about the x-axis. What is the equation of the new function, g(x)? State its y-intercept, domain, and range. Graphical For the following exercises, graph the function and its reflection about the y-axis on the same axes, and give the y-intercept. 8. f (x) = 3(  1/2  ) x 9. g(x) = -2(0.25)x For the following exercises, graph each set of functions on the same axes. 11. f (x) = 3(  1/4  ) x , g(x) = 3(2)x, and h(x) = 3(4)x 12. f (x) =  1/4 (3)x, g(x) = 2(3)x, and h(x) = 4(3)x For the following exercises, match each function with one of the graphs in Figure 12. A B C D E F

## 4.2 Section Exercises

---
For the following exercises, use the graphs shown in Figure 13. All have the form f (x) = ab x. y x A B C D E F 19. Which graph has the largest value for b? 20. Which graph has the smallest value for b? 21. Which graph has the largest value for a? 22. Which graph has the smallest value for a? For the following exercises, graph the function and its reflection about the x-axis on the same axes. 23. f (x) =  1/2 (4)x 25. f (x) = -4(2)x + 2 For the following exercises, graph the transformation of f (x) = 2x. Give the horizontal asymptote, the domain, and the range. 26. f (x) = 2-x 27. h(x) = 2x + 3 28. f (x) = 2x - 2 For the following exercises, describe the end behavior of the graphs of the functions. 29. f (x) = -5(4)x - 1 30. f (x) = 3 (  1/2  ) x - 2 31. f (x) = 3(4)-x + 2 For the following exercises, start with the graph of f (x) = 4x. Then write a function that results from the given transformation. 32. Shift f (x) 4 units upward 33. Shift f (x) 3 units downward 34. Shift f (x) 2 units left 35. Shift f (x) 5 units right 36. Reflect f (x) about the x-axis 37. Reflect f (x) about the y-axis For the following exercises, each graph is a transformation of y = 2x. Write an equation describing the transformation. x y x y x y

For the following exercises, find an exponential equation for the graph. x y x y Numeric For the following exercises, evaluate the exponential functions for the indicated value of x. 43. g (x) =  1/3 (7)x - 2 for g(6). 44. f (x) = 4(2)x - 1 - 2 for f (5). 45. h(x) = - 1/2 (  1/2  ) x + 6 for h(-7). Technology For the following exercises, use a graphing calculator to approximate the solutions of the equation. Round to the nearest thousandth. f (x) = ab x + d. 46. -50 = -(  1/2  ) -x/4 (  1/8  ) x/2  ) x - 1 - 2 Extensions 51. Explore and discuss the graphs of f (x) = (b)x and g(x) = (  1/b  ) x . Then make a conjecture about the relationship between the graphs of the functions b x and (  1/b  ) x  for any real number b > 0. 52. Prove the conjecture made in the previous exercise. 53. Explore and discuss the graphs of f (x) = 4x, g(x) = 4x - 2, and h(x) = (  1/16  )4x. Then make a conjecture about the relationship between the graphs of the functions b x and (  1/bn  )b x for any real number n and real number b > 0. 54. Prove the conjecture made in the previous exercise.

## 4.3 Logarithmic Functions

---
Learning Objectives
In this section, you will:
• Convert from logarithmic to exponential form.
• Convert from exponential to logarithmic form.
• Evaluate logarithms.
• Use common logarithms.
• Use natural logarithms.
In 2010, a major earthquake struck Haiti, destroying or damaging over 285,000 homes[19]. One year later, another, stronger earthquake devastated Honshu, Japan, destroying or damaging over 332,000 buildings,[20] like those shown in earthquake in Haiti. How do we know? The magnitudes of earthquakes are measured on a scale known as the Richter Scale. The Haitian earthquake registered a 7.0 on the Richter Scale[21] whereas the Japanese earthquake registered a 9.0.[22] The Richter Scale is a base-ten logarithmic scale. In other words, an earthquake of magnitude 8 is not twice as great as an earthquake of magnitude 4. It is 108 - 4 = 104 = 10,000 times as great! In this lesson, we will investigate the nature of the Richter Scale and the base-ten function upon which it depends. Converting from Logarithmic to Exponential Form In order to analyze the magnitude of earthquakes or compare the magnitudes of two different earthquakes, we need to be able to convert between logarithmic and exponential form. For example, suppose the amount of energy released from one earthquake were 500 times greater than the amount of energy released from another. We want to calculate the difference in magnitude. The equation that represents this problem is 10x = 500, where x represents the difference in magnitudes on the Richter Scale. How would we solve for x? We have not yet learned a method for solving exponential equations. None of the algebraic tools discussed so far is sufficient to solve 10x = 500. We know that 102 = 100 and 103 = 1000, so it is clear that x must be some value between 2 and 3, since y = 10x is increasing. We can examine a graph, as in Figure 2, to better estimate the solution. x y = 10x y 19 http://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us²010rja⁶/#summary. Accessed 3/4/2013. 20 http://earthquake.usgs.gov/earthquakes/eqinthenews/2011/usc⁰01xgp/#summary. Accessed 3/4/2013. 21 http://earthquake.usgs.gov/earthquakes/eqinthenews/2010/us²010rja⁶/. Accessed 3/4/2013. 22 http://earthquake.usgs.gov/earthquakes/eqinthenews/2011/usc⁰01xgp/#details. Accessed 3/4/2013.

Estimating from a graph, however, is imprecise. To find an algebraic solution, we must introduce a new function. Observe that the graph in Figure 2 passes the horizontal line test. The exponential function y = b x is one-to-one, so its inverse, x = b y is also a function. As is the case with all inverse functions, we simply interchange x and y and solve for y to find the inverse function. To represent y as a function of x, we use a logarithmic function of the form y = logb(x). The base b logarithm of a number is the exponent by which we must raise b to get that number. We read a logarithmic expression as, “The logarithm with base b of x is equal to y,” or, simplified, “log base b of x is y.” We can also say, “b raised to the power of y is x,” because logs are exponents. For example, the base 2 logarithm of 32 is 5, because 5 is the exponent we must apply to 2 to get 32. Since 25 = 32, we can write log² 32 = 5. We read this as “log base 2 of 32 is 5.” We can express the relationship between logarithmic form and its corresponding exponential form as follows: logb(x) = y ⇔ b y = x, b > 0, b ≠  1 Note that the base b is always positive. logb(x) = y Think b to the y = x =

to Because logarithm is a function, it is most correctly written as logb(x), using parentheses to denote function evaluation, just as we would with f (x). However, when the input is a single variable or number, it is common to see the parentheses dropped and the expression written without parentheses, as logb x. Note that many calculators require parentheses around the x. We can illustrate the notation of logarithms as follows:

logb(c) = a means ba = c =

to Notice that, comparing the logarithm function and the exponential function, the input and the output are switched. This means y = logb (x) and y = b x are inverse functions. definition of the logarithmic function A logarithm base b of a positive number x satisfies the following definition. For x > 0, b > 0, b ≠  1, y = logb(x) is equivalent to b y = x where, • we read logb (x) as, “the logarithm with base b of x” or the “log base b of x.” • the logarithm y is the exponent to which b must be raised to get x. Also, since the logarithmic and exponential functions switch the x and y values, the domain and range of the exponential function are interchanged for the logarithmic function. Therefore, • the domain of the logarithm function with base b is (0, ∞ ). • the range of the logarithm function with base b is ( -∞ , ∞ ). Can we take the logarithm of a negative number? No. Because the base of an exponential function is always positive, no power of that base can ever be negative. We can never take the logarithm of a negative number. Also, we cannot take the logarithm of zero. Calculators may output a log of a negative number when in complex mode, but the log of a negative number is not a real number.

---
### 💡 **How To…**
Given an equation in logarithmic form logb(x) = y, convert it to exponential form. 1. Examine the equation y = logb(x) and identify b, y, and x. 2. Rewrite logb(x) = y as b y = x.

---
### 📐 **Example  1**
Converting from Logarithmic Form to Exponential Form Write the following logarithmic equations in exponential form. a. log⁶(√6 ) =  1/2  b. log³(9) = 2

**Solution**

First, identify the values of b, y, and x. Then, write the equation in the form b y = x. a. log⁶(√6 ) =  1/2  Here, b = 6, y =  1/2 , and x = √6 . Therefore, the equation log⁶(√6 ) =  1/2  is equivalent to 6  1/2  = √6 . b. log³(9) = 2 Here, b = 3, y = 2, and x = 9. Therefore, the equation log³(9) = 2 is equivalent to 32 = 9.

---
### ✏️ **Try It #1**
Write the following logarithmic equations in exponential form. Converting From Exponential to Logarithmic Form To convert from exponents to logarithms, we follow the same steps in reverse. We identify the base b, exponent x, and output y. Then we write x = logb(y).

---
### 📐 **Example  2**
Converting from Exponential Form to Logarithmic Form Write the following exponential equations in logarithmic form. a. 23 = 8 b. 52 = 25 c. 10-4 =  ______

**Solution**

First, identify the values of b, y, and x. Then, write the equation in the form x = logb(y). Here, b = 2, x = 3, and y = 8. Therefore, the equation 23 = 8 is equivalent to log²(8) = 3. Here, b = 5, x = 2, and y = 25. Therefore, the equation 52 = 25 is equivalent to log⁵(25) = 2. c. 10-4 =  ______ Here, b = 10, x = -4, and y =  _ 10,000 . Therefore, the equation 10-4 =  _ 10,000  is equivalent to log¹0 (  _

---
### ✏️ **Try It #20**
Write the following exponential equations in logarithmic form. a. 32 = 9 b. 53 = 125 c. 2-1 =  1/2  Evaluating Logarithms Knowing the squares, cubes, and roots of numbers allows us to evaluate many logarithms mentally. For example, consider log²(8). We ask, “To what exponent must 2 be raised in order to get 8?” Because we already know 23 = 8, it follows that log²(8) = 3. Now consider solving log⁷(49) and log³(27) mentally. • We ask, “To what exponent must 7 be raised in order to get 49?” We know 72 = 49. Therefore, log⁷(49) = 2 • We ask, “To what exponent must 3 be raised in order to get 27?” We know 33 = 27. Therefore, log³(27) = 3 Even some seemingly more complicated logarithms can be evaluated without a calculator. For example, let’s evaluate log 2/3  (  4/9  ) mentally. • We ask, “To what exponent must  2/3  be raised in order to get  4/9 ?” We know 22 = 4 and 32 = 9, so (  2/3  ) =  4/9 . Therefore, log 2/3  (  4/9  ) = 2.

---
### 💡 **How To…**
Given a logarithm of the form y = logb(x), evaluate it mentally. 1. Rewrite the argument x as a power of b : b y = x. 2. Use previous knowledge of powers of b identify y by asking, “To what exponent should b be raised in order to get x?”

---
### 📐 **Example  3**: Solving Logarithms Mentally

Solve y = log⁴(64) without using a calculator.

**Solution**

First we rewrite the logarithm in exponential form: 4y = 64. Next, we ask, “To what exponent must 4 be raised in order to get 64?” We know 43 = 64 therefore, log⁴(64) = 3.

---
### ✏️ **Try It #3**
Solve y = log¹21(11) without using a calculator.

---
### 📐 **Example  4**: Evaluating the Logarithm of a Reciprocal

Evaluate y = log³ (  1/27  ) without using a calculator.

**Solution**

First we rewrite the logarithm in exponential form: 3 y =  1/27 . Next, we ask, “To what exponent must 3 be raised in order to get  1/27  ?” We know 33 = 27, but what must we do to get the reciprocal,  1/27 ? Recall from working with exponents that b-a =  1/ba . We use this information to write

3-3 =  1/33 

=  1/27  Therefore, log³ (  1/27  ) = -3.

---
### ✏️ **Try It #4**
Evaluate y = log² (  1/32  ) without using a calculator. Using Common Logarithms Sometimes we may see a logarithm written without a base. In this case, we assume that the base is 10. In other words, the expression log(x) means log¹0(x). We call a base-10 logarithm a common logarithm. Common logarithms are used to measure the Richter Scale mentioned at the beginning of the section. Scales for measuring the brightness of stars and the pH of acids and bases also use common logarithms. definition of the common logarithm A common logarithm is a logarithm with base 10. We write log¹0(x) simply as log(x). The common logarithm of a positive number x satisfies the following definition. For x > 0, y = log(x) is equivalent to 10 y = x We read log(x) as, “the logarithm with base 10 of x” or “log base 10 of x.” The logarithm y is the exponent to which 10 must be raised to get x.

---
### 💡 **How To…**
Given a common logarithm of the form y = log(x), evaluate it mentally. 1. Rewrite the argument x as a power of 10: 10 y = x. 2. Use previous knowledge of powers of 10 to identify y by asking, “To what exponent must 10 be raised in order to get x?”

---
### 📐 **Example  5**: Finding the Value of a Common Logarithm Mentally

Evaluate y = log(1,000) without using a calculator.

**Solution**

First we rewrite the logarithm in exponential form: 10y = 1,000. Next, we ask, “To what exponent must 10 be raised in order to get 1,000?” We know 103 = 1,000 therefore, log(1,000) = 3.

---
### ✏️ **Try It #5**

---
### 💡 **How To…**
Given a common logarithm with the form y = log(x), evaluate it using a calculator. 1. Press [LOG]. 2. Enter the value given for x, followed by [ ) ]. 3. Press [ENTER].

---
### 📐 **Example  6**: Finding the Value of a Common Logarithm Using a Calculator

Evaluate y = log(321) to four decimal places using a calculator.

**Solution**

• Press [LOG]. • Enter 321, followed by [ ) ]. • Press [ENTER]. Rounding to four decimal places, log(321) ≈ 2.5065. Analysis Note that 102 = 100 and that 103 = 1000. Since 321 is between 100 and 1000, we know that log(321) must be between log(100) and log(1000). This gives us the following:

---
### ✏️ **Try It #6**
Evaluate y = log(123) to four decimal places using a calculator.

---
### 📐 **Example  7**
Rewriting and Solving a Real-World Exponential Model The amount of energy released from one earthquake was 500 times greater than the amount of energy released from another. The equation 10x = 500 represents this situation, where x is the difference in magnitudes on the Richter Scale. To the nearest thousandth, what was the difference in magnitudes?

**Solution**

We begin by rewriting the exponential equation in logarithmic form.

log(500) = x Use the definition of the common log.

Next we evaluate the logarithm using a calculator: • Press [LOG]. • Enter 500, followed by [ ) ]. • Press [ENTER]. • To the nearest thousandth, log(500) ≈ 2.699. The difference in magnitudes was about 2.699.

---
### ✏️ **Try It #7**
The amount of energy released from one earthquake was 8,500 times greater than the amount of energy released from another. The equation 10x = 8500 represents this situation, where x is the difference in magnitudes on the Richter Scale. To the nearest thousandth, what was the difference in magnitudes? Using Natural Logarithms The most frequently used base for logarithms is e. Base e logarithms are important in calculus and some scientific applications; they are called natural logarithms. The base e logarithm, loge(x), has its own notation, ln(x). Most values of ln(x) can be found only using a calculator. The major exception is that, because the logarithm of 1 is always 0 in any base, ln(1) = 0. For other natural logarithms, we can use the ln key that can be found on most scientific calculators. We can also find the natural logarithm of any power of e using the inverse property of logarithms. definition of the natural logarithm A natural logarithm is a logarithm with base e. We write loge(x) simply as ln(x). The natural logarithm of a positive number x satisfies the following definition. For x > 0, y = ln(x) is equivalent to e y = x We read ln(x) as, “the logarithm with base e of x” or “the natural logarithm of x.” The logarithm y is the exponent to which e must be raised to get x. Since the functions y = e and y = ln(x) are inverse functions, ln(e x) = x for all x and e = x for x > 0.

---
### 💡 **How To…**
Given a natural logarithm with the form y = ln(x), evaluate it using a calculator. 1. Press [LN]. 2. Enter the value given for x, followed by [ ) ]. 3. Press [ENTER].

---
### 📐 **Example  8**: Evaluating a Natural Logarithm Using a Calculator

Evaluate y = ln(500) to four decimal places using a calculator.

**Solution**

• Press [LN]. • Enter 500, followed by [ ) ]. • Press [ENTER]. Rounding to four decimal places, ln(500) ≈ 6.2146

---
### ✏️ **Try It #8**
Evaluate ln(-500). > Access this online resource for additional instruction and practice with logarithms. • Introduction to Logarithms (http://openstaxcollege.org/l/intrologarithms)

## 4.3 Section Exercises

---
4.3 SECTION EXERCISES Verbal 1. What is a base b logarithm? Discuss the meaning by interpreting each part of the equivalent equations b y = x and logb(x) = y for b > 0, b ≠  1. 2. How is the logarithmic function f (x) = logb(x) related to the exponential function g(x) = b x ? What is the result of composing these two functions? 3. How can the logarithmic equation logb x = y be solved for x using the properties of exponents? 4. Discuss the meaning of the common logarithm. What is its relationship to a logarithm with base b, and how does the notation differ? 5. Discuss the meaning of the natural logarithm. What is its relationship to a logarithm with base b, and how does the notation differ? Algebraic For the following exercises, rewrite each equation in exponential form. 6. log⁴(q) = m 7. loga(b) = c 8. log¹6(y) = x 9. logx(64) = y 10. logy(x) = -11 11. log¹5(a) = b 12. logy(137) = x 14. log(v) = t 15. ln(w) = n For the following exercises, rewrite each equation in logarithmic form. 17. c d = k 18. m-7 = n/13  = y/5  ) m  = n/100  25. e k = h For the following exercises, solve for x by converting the logarithmic equation to exponential form. 26. log³(x) = 2 27. log²(x) = -3 28. log⁵(x) = 2 29. log³(x) = 3 30. log²(x) = 6 31. log⁹(x) =  1/2  33. log⁶(x) = -3 34. log(x) = 3 35. ln(x) = 2 For the following exercises, use the definition of common and natural logarithms to simplify. Numeric For the following exercises, evaluate the base b logarithmic expression without using a calculator. 42. log³ (  1/27  ) 43. log⁶(√6 ) 44. log² (  1/8  ) + 4 For the following exercises, evaluate the common logarithmic expression without using a calculator. 48. log(1) + 7

For the following exercises, evaluate the natural logarithmic expression without using a calculator. 50. ln( e  1/3  )  2/5  ) Technology For the following exercises, evaluate each expression using a calculator. Round to the nearest thousandth. 56. ln(  4/5  ) 57. log(√2 ) 58. ln(√2 ) Extensions 59. Is x = 0 in the domain of the function f (x) = log(x)? If so, what is the value of the function when x = 0? Verify the result. 60. Is f (x) = 0 in the range of the function f (x) = log(x)? If so, for what value of x? Verify the result. 61. Is there a number x such that ln x = 2? If so, what is that number? Verify the result. 62. Is the following true:  _ log⁴ (  1/64  )  = -1? Verify the result. 63. Is the following true:  ln(e¹.725) _ ln(1)  = 1.725? Verify the result. Real-World Applications 64. The exposure index EI for a 35 millimeter camera is a measurement of the amount of light that hits the film. It is determined by the equation EI = log²(  f 2/t  ), where f is the “f-stop” setting on the camera, and t is the exposure time in seconds. Suppose the f-stop setting is 8 and the desired exposure time is 2 seconds. What will the resulting exposure index be? 65. Refer to the previous exercise. Suppose the light meter on a camera indicates an EI of -2, and the desired exposure time is 16 seconds. What should the f-stop setting be? 66. The intensity levels I of two earthquakes measured on a seismograph can be compared by the formula log  I¹ _ I²  = M¹ - M² where M is the magnitude given by the Richter Scale. In August 2009, an earthquake of magnitude 6.1 hit Honshu, Japan. In March 2011, that same region experienced yet another, more devastating earthquake, this time with a magnitude of 9.0.[23] How many times greater was the intensity of the 2011 earthquake? Round to the nearest whole number. 23 http://earthquake.usgs.gov/earthquakes/world/historical.php. Accessed 3/4/2014.

## 4.4 Graphs of Logarithmic Functions

---
Learning Objectives
In this section, you will:
• Identify the domain of a logarithmic function.
• Graph logarithmic functions.
In Graphs of Exponential Functions, we saw how creating a graphical representation of an exponential model gives us another layer of insight for predicting future events. How do logarithmic graphs give us insight into situations? Because every logarithmic function is the inverse function of an exponential function, we can think of every output on a logarithmic graph as the input for the corresponding inverse exponential equation. In other words, logarithms give the cause for an effect. To illustrate, suppose we invest $2,500 in an account that offers an annual interest rate of 5%, compounded continuously. We already know that the balance in our account for any year t can be found with the equation A = 2500e⁰.05t. But what if we wanted to know the year for any balance? We would need to create a corresponding new function by interchanging the input and the output; thus we would need to create a logarithmic model for this situation. By graphing the model, we can see the output (year) for any input (account balance). For instance, what if we wanted to know how many years it would take for our initial investment to double? Figure 1 shows this point on the logarithmic graph. Logarithmic Model Showing Years as a Function of the Balance in the Account Account balance Te balance reaches Years In this section we will discuss the values for which a logarithmic function is defined, and then turn our attention to graphing the family of logarithmic functions. Finding the Domain of a Logarithmic Function Before working with graphs, we will take a look at the domain (the set of input values) for which the logarithmic function is defined. Recall that the exponential function is defined as y = b x for any real number x and constant b > 0, b ≠  1, where • The domain of y is (-∞ , ∞ ). • The range of y is (0, ∞ ). In the last section we learned that the logarithmic function y = logb(x) is the inverse of the exponential function y = b x. So, as inverse functions: • The domain of y = logb(x) is the range of y = b x : (0, ∞ ). • The range of y = logb(x) is the domain of y = b x : (-∞ , ∞ ).

Transformations of the parent function y = logb(x) behave similarly to those of other functions. Just as with other parent functions, we can apply the four types of transformations—shifts, stretches, compressions, and reflections—to the parent function without loss of shape. In Graphs of Exponential Functions we saw that certain transformations can change the range of y = b x. Similarly, applying transformations to the parent function y = logb(x) can change the domain. When finding the domain of a logarithmic function, therefore, it is important to remember that the domain consists only of positive real numbers. That is, the argument of the logarithmic function must be greater than zero. For example, consider f (x) = log⁴(2x - 3). This function is defined for any values of x such that the argument, in this case 2x - 3, is greater than zero. To find the domain, we set up an inequality and solve for x :

2x - 3 > 0 Show the argument greater than zero.

2x > 3 Add 3.

Divide by 2. In interval notation, the domain of f (x) = log⁴(2x - 3) is (1.5, ∞ ).

---
### 💡 **How To…**
Given a logarithmic function, identify the domain. 1. Set up an inequality showing the argument greater than zero. 2. Solve for x. 3. Write the domain in interval notation.

---
### 📐 **Example  1**: Identifying the Domain of a Logarithmic Shift

What is the domain of f (x) = log²(x + 3)?

**Solution**

The logarithmic function is defined only when the input is positive, so this function is defined when x + 3 > 0. Solving this inequality,

x + 3 > 0 The input must be positive.

x > -3 Subtract 3. The domain of f (x) = log²(x + 3) is (-3, ∞ ).

---
### ✏️ **Try It #1**
What is the domain of f (x) = log⁵(x - 2) + 1?

---
### 📐 **Example  2**: Identifying the Domain of a Logarithmic Shift and Reflection

What is the domain of f (x) = log(5 - 2x)?

**Solution**

The logarithmic function is defined only when the input is positive, so this function is defined when Solving this inequality,

5 - 2x > 0 The input must be positive.

-2x > -5 Subtract 5.

x <  5/2  Divide by -2 and switch the inequality. The domain of f (x) = log(5 - 2x) is ( –∞ ,  5/2  ).

---
### ✏️ **Try It #2**
What is the domain of f (x) = log(x - 5) + 2? Graphing Logarithmic Functions Now that we have a feel for the set of values for which a logarithmic function is defined, we move on to graphing logarithmic functions. The family of logarithmic functions includes the parent function y = logb(x) along with all its transformations: shifts, stretches, compressions, and reflections. We begin with the parent function y = logb(x). Because every logarithmic function of this form is the inverse of an exponential function with the form y = b x, their graphs will be reflections of each other across the line y = x. To illustrate this, we can observe the relationship between the input and output values of y = 2x and its equivalent x = log²(y) in Table 1. x -3 -2 -1 2x = y  1/8   1/4   1/2  log²(y) = x -3 -2 -1 Using the inputs and outputs from Table 1, we can build another table to observe the relationship between points on the graphs of the inverse functions f (x) = 2x and g(x) = log²(x). See Table 2. f (x) = 2x ( -3,  1/8  ) ( -2,  1/4  ) ( -1,  1/2  ) g(x) = log²(x) (  1/8 , -3 ) (  1/4 , -2 ) (  1/2 , -1 ) As we’d expect, the x- and y-coordinates are reversed for the inverse functions. Figure 2 shows the graph of f and g. x y y = x g(x) = log²(x) f (x) = 2x Observe the following from the graph: • f (x) = 2x has a y-intercept at (0, 1) and g(x) = log²(x) has an x-intercept at (1, 0). • The domain of f (x) = 2x, (-∞ , ∞ ), is the same as the range of g(x) = log²(x). • The range of f (x) = 2x, (0, ∞ ), is the same as the domain of g(x) = log²(x).

characteristics of the graph of the parent function, f (x) = logb(x) For any real number x and constant b > 0, b ≠  1, we can see the following characteristics in the graph of f (x) = logb(x): • one-to-one function • vertical asymptote: x = 0 • domain: (0, ∞ ) • range: (-∞ , ∞ ) • x-intercept: (1, 0) and key point (b, 1) • y-intercept: none • increasing if b > 1 • decreasing if 0 < b < 1 See Figure 3. the graphs. Observe that the graphs compress vertically as the value of the base increases. (Note: recall that the function ln(x) has base x y log²(x) ln(x) log(x) x = 0 functions with different bases, all greater than 1. f(x) x (b, 1) x = 0 f(x) = logb(x) b > 1 f(x) x (b, 1) x = 0 f (x) = logb(x) 0 < b < 1

---
### 💡 **How To…**
Given a logarithmic function with the form f (x) = logb(x), graph the function. 1. Draw and label the vertical asymptote, x = 0. 2. Plot the x-intercept, (1, 0). 3. Plot the key point (b, 1). 4. Draw a smooth curve through the points. 5. State the domain, (0, ∞ ), the range, (-∞ , ∞ ), and the vertical asymptote, x = 0.

---
### 📐 **Example  3**: Graphing a Logarithmic Function with the Form f ( x) = logb( x).

Graph f (x) = log⁵(x). State the domain, range, and asymptote.

**Solution**

Before graphing, identify the behavior and key points for the graph. • Since b = 5 is greater than one, we know the function is increasing. The left tail of the graph will approach the vertical asymptote x = 0, and the right tail will increase slowly without bound. • The x-intercept is (1, 0). • The key point (5, 1) is on the graph. • We draw and label the asymptote, plot and label the points, and draw a smooth curve through the points (see

x f (x) f (x) = log⁵(x) x = 0 The domain is (0, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = 0.

---
### ✏️ **Try It #3**
Graph f (x) = log 1/5 (x). State the domain, range, and asymptote. Graphing Transformations of Logarithmic Functions As we mentioned in the beginning of the section, transformations of logarithmic graphs behave similarly to those of other parent functions. We can shift, stretch, compress, and reflect the parent function y = logb(x) without loss of shape. Graphing a Horizontal Shift of f (x ) = logb(x ) When a constant c is added to the input of the parent function f (x) = logb(x), the result is a horizontal shift c units in the opposite direction of the sign on c. To visualize horizontal shifts, we can observe the general graph of the parent function f (x) = logb(x) and for c > 0 alongside the shift left, g(x ) = logb(x + c), and the shift right, h(x) = logb(x - c). See Figure 6. Shift left g (x) = logb(x + c) Shift right h(x) = logb(x - c) (b, 1) (1 - c, 0) (b - c, 1) f (x) = logb(x) x = 0 x y g(x) = logb(x + c) x = –c • The asymptote changes to x = -c. • The domain changes to (-c, ∞ ). • The range remains (-∞ , ∞ ). x = 0 y (1 + c, 0) (b + c, 1) (b, 1) h(x) = logb(x - c) f (x) = logb(x) x x = c • The asymptote changes to x = c. • The domain changes to (c, ∞ ). • The range remains (-∞ , ∞ ). horizontal shifts of the parent function y = logb(x) For any constant c, the function f (x) = logb (x + c) • shifts the parent function y = logb(x) left c units if c > 0. • shifts the parent function y = logb(x) right c units if c < 0. • has the vertical asymptote x = -c. • has domain (-c, ∞ ). • has range (-∞ , ∞ ).

---
### 💡 **How To…**
Given a logarithmic function with the form f (x) = logb(x + c), graph the translation. 1. Identify the horizontal shift: a. If c > 0, shift the graph of f (x) = logb(x) left c units. b. If c < 0, shift the graph of f (x) = logb(x) right c units. 2. Draw the vertical asymptote x = -c. 3. Identify three key points from the parent function. Find new coordinates for the shifted functions by subtracting c from the x coordinate. 4. Label the three points. 5. The domain is (-c, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = -c.

---
### 📐 **Example  4**: Graphing a Horizontal Shift of the Parent Function y = logb( x)

Sketch the horizontal shift f (x) = log³(x - 2) alongside its parent function. Include the key points and asymptotes on the graph. State the domain, range, and asymptote.

**Solution**

Since the function is f (x) = log³(x - 2), we notice x + (-2) = x - 2. Thus c = -2, so c < 0. This means we will shift the function f (x) = log³(x) right 2 units. The vertical asymptote is x = -(-2) or x = 2. Consider the three key points from the parent function, (  1 The new coordinates are found by adding 2 to the x coordinates. Label the points (  7 The domain is (2, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = 2. f (x) = log³(x - 2) y = log³(x) x = 0 x = 2 x y

---
### ✏️ **Try It #4**
Sketch a graph of f (x) = log³(x + 4) alongside its parent function. Include the key points and asymptotes on the graph. State the domain, range, and asymptote. Graphing a Vertical Shift of y = logb(x ) When a constant d is added to the parent function f (x) = logb(x), the result is a vertical shift d units in the direction of the sign on d. To visualize vertical shifts, we can observe the general graph of the parent function f (x) = logb(x) alongside the shift up, g (x) = logb(x) + d and the shift down, h(x) = logb(x) - d. See Figure 8.

Shift up g (x) = logb(x) + d Shift down h(x) = logb(x) - d (b, 1) (b¹ - d, 1) (b-d, 0) g(x) = logb(x) + d f (x) = logb(x) x = 0 y x (b, 1) (b¹+d, 1) (bd, 0) h(x) = logb(x) - d f (x) = logb(x) x = 0 y x • The asymptote remains x = 0. • The domain remains to (0, ∞ ). • The range remains (-∞ , ∞ ). • The asymptote remains x = 0. • The domain remains to (0, ∞ ). • The range remains (-∞ , ∞ ). vertical shifts of the parent function y = logb(x) For any constant d, the function f (x) = logb(x) + d • shifts the parent function y = logb(x) up d units if d > 0. • shifts the parent function y = logb(x) down d units if d < 0. • has the vertical asymptote x = 0. • has domain (0, ∞ ). • has range (-∞ , ∞ ).

---
### 💡 **How To…**
Given a logarithmic function with the form f (x) = logb(x) + d, graph the translation. 1. Identify the vertical shift: a. If d > 0, shift the graph of f (x) = logb(x) up d units. b. If d < 0, shift the graph of f (x) = logb(x) down d units. 2. Draw the vertical asymptote x = 0. 3. Identify three key points from the parent function. Find new coordinates for the shifted functions by adding d to the y coordinate. 4. Label the three points. 5. The domain is (0, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = 0.

---
### 📐 **Example  5**: Graphing a Vertical Shift of the Parent Function y = logb(x)

Sketch a graph of f (x) = log³(x) - 2 alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote.

**Solution**

Since the function is f (x) = log³(x) - 2, we will notice d = -2. Thus d < 0. This means we will shift the function f (x) = log³(x) down 2 units. The vertical asymptote is x = 0.

Consider the three key points from the parent function, (  1 The new coordinates are found by subtracting 2 from the y coordinates. Label the points (  1/3 , -3 ), (1, -2), and (3, -1). The domain is (0, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = 0. f (x) = log³(x - 2) y = log³(x) x = 0 x y The domain is (0, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = 0.

---
### ✏️ **Try It #5**
Sketch a graph of f (x) = log²(x) + 2 alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote. Graphing Stretches and Compressions of y = logb(x ) When the parent function f (x) = logb(x) is multiplied by a constant a > 0, the result is a vertical stretch or compression of the original graph. To visualize stretches and compressions, we set a > 1 and observe the general graph of the parent function f (x) = logb(x) alongside the vertical stretch, g (x) = alogb(x) and the vertical compression, h(x) =  1/a logb(x). See Figure 10. Vertical Stretch g (x) = alogb(x), a > 1 Vertical Compression h(x) =  1/a logb(x), a > 1 (b, 1) g(x) = alogb(x) f(x) = logb(x) x = 0 x y (b , 1) 1/a • The asymptote remains x = 0. • The x-intercept remains (1, 0). • The domain remains (0, ∞ ). • The range remains (-∞ , ∞ ). (b, 1) f(x) = logb(x) x = 0 x y (ba, 1) h(x) = logb(x) 1a • The asymptote remains x = 0. • The x-intercept remains (1, 0). • The domain remains (0, ∞ ). • The range remains (-∞ , ∞ ).

vertical stretches and compressions of the parent function y = logb(x) For any constant a > 1, the function f (x) = alogb(x) • stretches the parent function y = logb(x) vertically by a factor of a if a > 1. • compresses the parent function y = logb(x) vertically by a factor of a if 0 < a < 1. • has the vertical asymptote x = 0. • has the x-intercept (1, 0). • has domain (0, ∞ ). • has range (-∞ , ∞ ).

---
### 💡 **How To…**
Given a logarithmic function with the form f (x) = alogb(x), a > 0, graph the translation. 1. Identify the vertical stretch or compressions: a. If ∣ a ∣ > 1, the graph of f (x) = logb(x) is stretched by a factor of a units. b. If ∣ a ∣ < 1, the graph of f (x) = logb(x) is compressed by a factor of a units. 2. Draw the vertical asymptote x = 0. 3. Identify three key points from the parent function. Find new coordinates for the shifted functions by multiplying the y coordinates by a. 4. Label the three points. 5. The domain is (0, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = 0.

---
### 📐 **Example  6**: Graphing a Stretch or Compression of the Parent Function y = logb( x )

Sketch a graph of f (x) = 2log⁴(x) alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote.

**Solution**

Since the function is f (x) = 2log⁴(x), we will notice a = 2. This means we will stretch the function f (x) = log⁴(x) by a factor of 2. The vertical asymptote is x = 0. Consider the three key points from the parent function, (  1 The new coordinates are found by multiplying the y coordinates by 2. Label the points (  1 The domain is (0, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = 0. See Figure 11. f (x) = 2log⁴(x) y = log⁴(x) x = 0 x y

---
### ✏️ **Try It #6**
Sketch a graph of f (x) =  1/2 log⁴(x) alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote.

---
### 📐 **Example  7**: Combining a Shift and a Stretch

Sketch a graph of f (x) = 5log(x + 2). State the domain, range, and asymptote.

**Solution**

Remember: what happens inside parentheses happens first. First, we move the graph left 2 units, then stretch the function vertically by a factor of 5, as in Figure 12. The vertical asymptote will be shifted to x = -2. The x-intercept will be (-1, 0). The domain will be (-2, ∞ ). Two points will help give the shape of the graph: (-1, 0) and (8, 5). We chose x = 8 as the x-coordinate of one point to graph because when x = 8, x + 2 = 10, the base of the common logarithm. x y y = 5 log(x + 2) y = log(x + 2) y = log(x) x = -2 The domain is (-2, ∞ ), the range is (-∞ , ∞ ), and the vertical asymptote is x = -2.

---
### ✏️ **Try It #7**
Sketch a graph of the function f (x) = 3log(x - 2) + 1. State the domain, range, and asymptote. Graphing Reflections of f (x ) = logb(x ) When the parent function f (x) = logb(x) is multiplied by -1, the result is a reflection about the x-axis. When the input is multiplied by -1, the result is a reflection about the y-axis. To visualize reflections, we restrict b > 1, and observe the general graph of the parent function f (x) = logb(x) alongside the reflection about the x-axis, g(x) = -logb(x) and the reflection about the y-axis, h(x) = logb(-x). Reflection about the x-axis g (x) = logb(x), b > 1 Reflection about the y-axis h(x) = logb(-x), b > 1 (b, 1) f (x) = logb(x) g(x) = -logb(x) x = 0 x y (b -1, 1) • The reflected function is decreasing as x moves from zero to infinity. • The asymptote remains x = 0. • The x-intercept remains (1, 0). • The key point changes to (b - 1, 1). • The domain remains (0, ∞ ). • The range remains (-∞ , ∞ ). (b, 1) (-b, 1) f (x) = logb(x) h(x) = logb(-x) x = 0 x y • The reflected function is decreasing as x moves from infinity to zero. • The asymptote remains x = 0. • The x-intercept remains (-1, 0). • The key point changes to (-b, 1). • The domain changes to (-∞ , 0). • The range remains (-∞ , ∞ ).

reflections of the parent function y = logb(x) The function f (x) = -logb(x) • reflects the parent function y = logb(x) about the x-axis. • has domain, (0, ∞ ), range, (-∞ , ∞ ), and vertical asymptote, x = 0, which are unchanged from the parent function. The function f (x) = logb(-x) • reflects the parent function y = logb(x) about the y-axis. • has domain (-∞ , 0). • has range, (-∞ , ∞ ), and vertical asymptote, x = 0, which are unchanged from the parent function.

---
### 💡 **How To…**
Given a logarithmic function with the parent function f (x) = logb(x), graph a translation. If f (x) = -logb(x) If f (x) = logb(-x) 1. Draw the vertical asymptote, x = 0. 1. Draw the vertical asymptote, x = 0. 2. Plot the x-intercept, (1, 0). 2. Plot the x-intercept, (1, 0). 3. Reflect the graph of the parent function f (x) = logb(x) about the x-axis. 3. Reflect the graph of the parent function f (x) = logb(x) about the y-axis. 4. Draw a smooth curve through the points. 4. Draw a smooth curve through the points. 5. State the domain, (0, ∞ ), the range, (-∞ , ∞ ), and the vertical asymptote x = 0. 5. State the domain, (-∞ , 0), the range, (-∞ , ∞ ), and the vertical asymptote x = 0.

---
### 📐 **Example  8**: Graphing a Reflection of a Logarithmic Function

Sketch a graph of f (x) = log(-x) alongside its parent function. Include the key points and asymptote on the graph. State the domain, range, and asymptote.

**Solution**

Before graphing f (x) = log(-x), identify the behavior and key points for the graph. • Since b = 10 is greater than one, we know that the parent function is increasing. Since the input value is multiplied by -1, f is a reflection of the parent graph about the y-axis. Thus, f (x) = log(-x) will be decreasing as x moves from negative infinity to zero, and the right tail of the graph will approach the vertical asymptote x = 0. • The x-intercept is (-1, 0). • We draw and label the asymptote, plot and label the points, and draw a smooth curve through the points. f (x) = log(-x) y = log(x) x = 0 x y The domain is (-∞ , 0), the range is (-∞ , ∞ ), and the vertical asymptote is x = 0.

---
### ✏️ **Try It #8**
Graph f (x) = -log(-x). State the domain, range, and asymptote.

---
### 💡 **How To…**
Given a logarithmic equation, use a graphing calculator to approximate solutions. 1. Press [Y=]. Enter the given logarithm equation or equations as Y¹= and, if needed, Y²=. 2. Press [GRAPH] to observe the graphs of the curves and use [WINDOW] to find an appropriate view of the graphs, including their point(s) of intersection. 3. To find the value of x, we compute the point of intersection. Press [2ND] then [CALC]. Select “intersect” and press [ENTER] three times. The point of intersection gives the value of x, for the point(s) of intersection.

---
### 📐 **Example  9**
Approximating the

**Solution**

of a Logarithmic Equation Solve 4ln(x) + 1 = -2ln(x - 1) graphically. Round to the nearest thousandth.

**Solution**

Press [Y=] and enter 4ln(x) + 1 next to Y¹=. Then enter -2ln(x - 1) next to Y²=. For a window, use the values 0 to 5 for x and –10 to 10 for y. Press [GRAPH]. The graphs should intersect somewhere a little to right of x = 1. For a better approximation, press [2ND] then [CALC]. Select [5: intersect] and press [ENTER] three times. The x-coordinate of the point of intersection is displayed as 1.3385297. (Your answer may be different if you use a different window or use a different value for Guess?) So, to the nearest thousandth, x ≈ 1.339.

---
### ✏️ **Try It #9**
Solve 5log(x + 2) = 4 - log(x) graphically. Round to the nearest thousandth. Summarizing Translations of the Logarithmic Function Now that we have worked with each type of translation for the logarithmic function, we can summarize each in Table 4 to arrive at the general equation for translating exponential functions. Translations of the Parent Function y = logb(x) Translation Form Shift • Horizontally c units to the left • Vertically d units up y = logb (x + c) + d Stretch and Compress • Stretch if ∣ a ∣ > 1 • Compression if ∣ a ∣ < 1 y = alogb(x) Reflect about the x-axis y = -logb(x) Reflect about the y-axis y = logb(-x) General equation for all translations y = alogb(x + c) + d translations of logarithmic functions All translations of the parent logarithmic function, y = logb(x), have the form f (x) = alogb(x + c) + d where the parent function, y = logb(x), b > 1, is • shifted vertically up d units. • shifted horizontally to the left c units. • stretched vertically by a factor of ∣ a ∣ if ∣ a ∣ > 0. • compressed vertically by a factor of ∣ a ∣ if 0 < ∣ a ∣ < 1. • reflected about the x-axis when a < 0. For f (x) = log(-x), the graph of the parent function is reflected about the y-axis.

---
### 📐 **Example  10**
Finding the Vertical Asymptote of a Logarithm Graph What is the vertical asymptote of f (x) = -2log³(x + 4) + 5?

**Solution**

The vertical asymptote is at x = -4. Analysis The coefficient, the base, and the upward translation do not affect the asymptote. The shift of the curve 4 units to the left shifts the vertical asymptote to x = -4.

---
### ✏️ **Try It #10**
What is the vertical asymptote of f (x) = 3 + ln(x - 1)?

---
### 📐 **Example  11**
Finding the Equation from a Graph Find a possible equation for the common logarithmic function graphed in Figure 15. x f(x)

**Solution**

This graph has a vertical asymptote at x = -2 and has been vertically reflected. We do not know yet the vertical shift or the vertical stretch. We know so far that the equation will have form: f (x) = -alog(x + 2) + k It appears the graph passes through the points (-1, 1) and (2, -1). Substituting (-1, 1),

1 = -alog(-1 + 2) + k Substitute (-1, 1).

1 = -alog(1) + k Arithmetic.

1 = k log(1) = 0. Next, substituting in (2, –1),

-1 = -alog(2 + 2) + 1 Plug in (2, -1).

-2 = -alog(4) Arithmetic.

a =  _____ log(4)  Solve for a. This gives us the equation f (x) = - _ log(4) log(x + 2) + 1. Analysis can verify this answer by comparing the function values in Table 5 with the points on the graph in Figure 15. x -1 f (x) -1 x f (x) -2

---
### ✏️ **Try It #11**
Give the equation of the natural logarithm graphed in Figure 16. x f(x) Is it possible to tell the domain and range and describe the end behavior of a function just by looking at the graph? Yes, if we know the function is a general logarithmic function. For example, look at the graph in Figure 16. The graph approaches x = -3 (or thereabouts) more and more closely, so x = -3 is, or is very close to, the vertical asymptote. It approaches from the right, so the domain is all points to the right, {x | x > -3}. The range, as with all general logarithmic functions, is all real numbers. And we can see the end behavior because the graph goes down as it goes left and up as it goes right. The end behavior is that as x → -3+, f (x) → -∞  and as x → ∞ , f (x) → ∞ .

Access these online resources for additional instruction and practice with graphing logarithms. • Graph an Exponential Function and Logarithmic Function (http://openstaxcollege.org/l/graphexplog) • Match Graphs with Exponential and Logarithmic Functions (http://openstaxcollege.org/l/matchexplog) • Find the Domain of Logarithmic Functions (http://openstaxcollege.org/l/domainlog)

## 4.4 Section Exercises

---
4.4 Section ExERCISES Verbal 1. The inverse of every logarithmic function is an exponential function and vice-versa. What does this tell us about the relationship between the coordinates of the points on the graphs of each? 2. What type(s) of translation(s), if any, affect the range of a logarithmic function? 3. What type(s) of translation(s), if any, affect the domain of a logarithmic function? 4. Consider the general logarithmic function f (x) = logb(x). Why can’t x be zero? 5. Does the graph of a general logarithmic function have a horizontal asymptote? Explain. Algebraic For the following exercises, state the domain and range of the function. 6. f (x) = log³(x + 4) 7. h(x) = ln (  1/2  - x ) 8. g(x) = log⁵(2x + 9) - 2 9. h(x) = ln(4x + 17) - 5 10. f (x) = log²(12 - 3x) - 3 For the following exercises, state the domain and the vertical asymptote of the function. 11. f (x) = logb(x - 5) 12. g(x) = ln(3 - x) 13. f (x) = log(3x + 1) 14. f (x) = 3log(-x) + 2 15. g(x) = -ln(3x + 9) - 7 For the following exercises, state the domain, vertical asymptote, and end behavior of the function. 16. f (x) = ln(2 - x) 17. f (x) = log ( x - 3/7  ) 18. h(x) = -log(3x - 4) + 3 19. g(x) = ln(2x + 6) - 5 20. f (x) = log³(15 - 5x) + 6 For the following exercises, state the domain, range, and x- and y-intercepts, if they exist. If they do not exist, write DNE. 21. h(x) = log⁴(x - 1) + 1 22. f (x) = log(5x + 10) + 3 23. g(x) = ln(-x) - 2 24. f (x) = log²(x + 2) - 5 25. h(x) = 3ln(x) - 9 Graphical For the following exercises, match each function in Figure 17 with the letter corresponding to its graph. A B C D E x y 26. d(x) = log(x) 27. f (x) = ln(x) 28. g(x) = log²(x) 29. h(x) = log⁵(x) 30. j(x) = log²5(x)

For the following exercises, match each function in Figure 18 with the letter corresponding to its graph. x y A B C 31. f (x) = log  1/3 (x) 32. g(x) = log²(x) 33. h(x) = log  3/4 (x) For the following exercises, sketch the graphs of each pair of functions on the same axis. 34. f (x) = log(x) and g(x) = 10x 35. f (x) = log(x) and g(x) = log  1/2 (x) 36. f (x) = log⁴(x) and g(x) = ln(x) 37. f (x) = e x and g(x) = ln(x) For the following exercises, match each function in Figure 19 with the letter corresponding to its graph. x y A B C 38. f (x) = log⁴(-x + 2) 39. g(x) = -log⁴(x + 2) 40. h(x) = log⁴(x + 2) For the following exercises, sketch the graph of the indicated function. 41. f (x) = log²(x + 2) 42. f (x) = 2log(x) 43. f (x) = ln(-x) 44. g(x) = log(4x + 16) + 4 45. g(x) = log(6 - 3x) + 1 46. h(x) = - 1/2  ln(x + 1) - 3 For the following exercises, write a logarithmic equation corresponding to the graph shown. 47. Use y = log²(x) as the parent function. x y 48. Use f (x) = log³(x) as the parent function. x y

49. Use f (x) = log⁴(x) as the parent function. x y 50. Use f (x) = log⁵(x) as the parent function. x y Technology For the following exercises, use a graphing calculator to find approximate solutions to each equation. 51. log(x - 1) + 2 = ln(x - 1) + 2 52. log(2x - 3) + 2 = -log(2x - 3) + 5 53. ln(x - 2) = -ln(x + 1) 54. 2ln(5x + 1) = 1/2 ln(-5x) + 1/3 log(1 - x) = log(x + 1) +  1/3  Extensions 56. Let b be any positive real number such that b ≠  1. What must logb¹ be equal to? Verify the result. 57. Explore and discuss the graphs of f (x) = log  1/2 (x) and g(x) = -log²(x). Make a conjecture based on the result. 58. Prove the conjecture made in the previous exercise. 59. What is the domain of the function f (x) = ln (  x + 2/x - 4  )? Discuss the result. 60. Use properties of exponents to find the x-intercepts of the function f (x) = log(x 2 + 4x + 4) algebraically. Show the steps for solving, and then verify the result by graphing the function.

Learning Objectives
In this section, you will:
• Use the product rule for logarithms.
• Use the quotient rule for logarithms.
• Use the power rule for logarithms.
• Expand logarithmic expressions.
• Condense logarithmic expressions.
• Use the change-of-base formula for logarithms.

## 4.5 Logarithmic Properties

---
In chemistry, pH is used as a measure of the acidity or alkalinity of a substance. The pH scale runs from 0 to 14. Substances with a pH less than 7 are considered acidic, and substances with a pH greater than 7 are said to be alkaline. Our bodies, for instance, must maintain a pH close to 7.35 in order for enzymes to work properly. To get a feel for what is acidic and what is alkaline, consider the following pH levels of some common substances: • Battery acid: 0.8 • Stomach acid: 2.7 • Orange juice: 3.3 • Pure water: 7 (at 25° C) • Human blood: 7.35 • Fresh coconut: 7.8 • Sodium hydroxide (lye): 14 To determine whether a solution is acidic or alkaline, we find its pH, which is a measure of the number of active positive hydrogen ions in the solution. The pH is defined by the following formula, where a is the concentration of hydrogen ion in the solution

pH = -log([H+])

= log (  _____ ([H+]  ) The equivalence of -log ([H+]) and log (  1 _ [H+]  ) is one of the logarithm properties we will examine in this section. Using the Product Rule for Logarithms Recall that the logarithmic and exponential functions “undo” each other. This means that logarithms have similar properties to exponents. Some important properties of logarithms are given here. First, the following properties are easy to prove.

logb(1) = 0

logb(b) = 1 For example, log⁵ 1 = 0 since 50 = 1. And log⁵ 5 = 1 since 51 = 5.

Next, we have the inverse property.

logb(b x) = x

b logb(x) = x, x > 0 For example, to evaluate log(100), we can rewrite the logarithm as log¹0(102), and then apply the inverse property logb (b x) = x to get log¹0(102) = 2. To evaluate e ln(7), we can rewrite the logarithm as eloge(7), and then apply the inverse property b logb (x) = x to get eloge(7) = 7. Finally, we have the one-to-one property.

logbM = logbN if and only if M = N We can use the one-to-one property to solve the equation log³(3x) = log³(2x + 5) for x. Since the bases are the same, we can apply the one-to-one property by setting the arguments equal and solving for x :

3x = 2x + 5 Set the arguments equal.

x = 5 Subtract 2x. But what about the equation log³(3x) + log³(2x + 5) = 2? The one-to-one property does not help us in this instance. Before we can solve an equation like this, we need a method for combining terms on the left side of the equation. Recall that we use the product rule of exponents to combine the product of exponents by adding: x a xb = x a + b. We have a similar property for logarithms, called the product rule for logarithms, which says that the logarithm of a product is equal to a sum of logarithms. Because logs are exponents, and we multiply like bases, we can add the exponents. We will use the inverse property to derive the product rule below. Given any real number x and positive real numbers M, N, and b, where b ≠  1, we will show

logb(MN) = logb(M) + logb(N). Let m = logb(M) and n = logb(N). In exponential form, these equations are b m = M and b n = N. It follows that

logb(MN) = logb(b mb n) Substitute for M and N.

= logb(b m + n) Apply the product rule for exponents.

= m + n Apply the inverse property of logs.

= logb(M) + logb(N) Substitute for m and n. Note that repeated applications of the product rule for logarithms allow us to simplify the logarithm of the product of any number of factors. For example, consider logb(wxyz). Using the product rule for logarithms, we can rewrite this logarithm of a product as the sum of logarithms of its factors:

logb(wxyz) = logb(w) + logb(x) + logb(y) + logb(z) the product rule for logarithms The product rule for logarithms can be used to simplify a logarithm of a product by rewriting it as a sum of individual logarithms. logb(MN) = logb(M) + logb(N) for b > 0

---
### 💡 **How To…**
Given the logarithm of a product, use the product rule of logarithms to write an equivalent sum of logarithms. 1. Factor the argument completely, expressing each whole number factor as a product of primes. 2. Write the equivalent expression by summing the logarithms of each factor.

---
### 📐 **Example  1**
Using the Product Rule for Logarithms Expand log³(30x(3x + 4)).

**Solution**

We begin by factoring the argument completely, expressing 30 as a product of primes.

log³(30x(3x + 4)) = log³(2 ·  3 ·  5 ·  x ·  (3x +4)) Next we write the equivalent equation by summing the logarithms of each factor.

log³(30x(3x + 4)) = log³(2) + log³(3) + log³(5) + log³(x) + log³(3x + 4)

---
### ✏️ **Try It #1**
Expand logb(8k). Using the Quotient Rule for Logarithms For quotients, we have a similar rule for logarithms. Recall that we use the quotient rule of exponents to combine the quotient of exponents by subtracting: x  (a)/(b)  = x a-b. The quotient rule for logarithms says that the logarithm of a quotient is equal to a difference of logarithms. Just as with the product rule, we can use the inverse property to derive the quotient rule. Given any real number x and positive real numbers M, N, and b, where b ≠  1, we will show

logb (  (M)/(N)  ) = logb(M) - logb(N). Let m = logb(M) and n = logb(N). In exponential form, these equations are bm = M and bn = N. It follows that

logb (  (M)/(N)  ) = logb (  b(m)/(b)n  ) Substitute for M and N.

= logb(b m - n) Apply the quotient rule for exponents.

= m - n Apply the inverse property of logs.

= logb(M) - logb(N) Substitute for m and n. For example, to expand log (  2x² + 6x/3x + 9  ), we must first express the quotient in lowest terms. Factoring and canceling we get,

log (  2x² + 6x _______ 3x + 9  )= log (  2x(x + 3) ________ 3(x + 3)  ) Factor the numerator and denominator.

= log (  2x/3  ) Cancel the common factors. Next we apply the quotient rule by subtracting the logarithm of the denominator from the logarithm of the numerator. Then we apply the product rule.

log (  2x/3  ) = log(2x) - log(3)

= log(2) + log(x) - log(3) the quotient rule for logarithms The quotient rule for logarithms can be used to simplify a logarithm or a quotient by rewriting it as the difference of individual logarithms. logb (  (M)/(N)  ) = logb(M) - logb(N)

---
### 💡 **How To…**
Given the logarithm of a quotient, use the quotient rule of logarithms to write an equivalent difference of logarithms. 1. Express the argument in lowest terms by factoring the numerator and denominator and canceling common terms. 2. Write the equivalent expression by subtracting the logarithm of the denominator from the logarithm of the numerator. 3. Check to see that each term is fully expanded. If not, apply the product rule for logarithms to expand completely.

---
### 📐 **Example  2**
Using the Quotient Rule for Logarithms Expand log² (  15x(x - 1) __

(3x + 4)(2 - x)  ).

**Solution**

First we note that the quotient is factored and in lowest terms, so we apply the quotient rule. log² (  15x(x - 1) __

(3x + 4)(2 - x)  ) = log²(15x(x-1))- log²((3x + 4)(2 - x)) Notice that the resulting terms are logarithms of products. To expand completely, we apply the product rule, noting that the prime factors of the factor 15 are 3 and 5. log²(15x(x - 1)) - log²((3x + 4)(2 - x)) = [log²(3) + log²(5) + log²(x) + log²(x - 1)] - [log²(3x + 4) + log²(2 - x)]

= log²(3) + log²(5) + log²(x) + log²(x - 1) - log²(3x + 4) - log²(2 - x) Analysis There are exceptions to consider in this and later examples. First, because denominators must never be zero, this expression is not defined for x = - 4/3  and x = 2. Also, since the argument of a logarithm must be positive, we note as we observe the expanded logarithm, that x > 0, x > 1, x > - 4/3 , and x < 2. Combining these conditions is beyond the scope of this section, and we will not consider them here or in subsequent exercises.

---
### ✏️ **Try It #2**
Expand log³ (  __

7x(x - 1)(x - 2)  ). Using the Power Rule for Logarithms We’ve explored the product rule and the quotient rule, but how can we take the logarithm of a power, such as x²? One method is as follows:

logb(x²) = logb(x ⋅ x)

= logb (x) + logb (x)

= 2log b (x) Notice that we used the product rule for logarithms to find a solution for the example above. By doing so, we have derived the power rule for logarithms, which says that the log of a power is equal to the exponent times the log of the base. Keep in mind that, although the input to a logarithm may not be written as a power, we may be able to change it to a power. For example, 3  = 3  1/2   1/e  = e-1 the power rule for logarithms The power rule for logarithms can be used to simplify the logarithm of a power by rewriting it as the product of the exponent times the logarithm of the base. logb(Mn) = nlogb(M)

---
### 💡 **How To…**
Given the logarithm of a power, use the power rule of logarithms to write an equivalent product of a factor and a logarithm. 1. Express the argument as a power, if needed. 2. Write the equivalent expression by multiplying the exponent times the logarithm of the base.

---
### 📐 **Example  3**
Expanding a Logarithm with Powers Expand log²(x⁵).

**Solution**

The argument is already written as a power, so we identify the exponent, 5, and the base, x, and rewrite the equivalent expression by multiplying the exponent times the logarithm of the base.

log²(x 5) = 5log²(x)

---
### ✏️ **Try It #3**
Expand ln(x²).

---
### 📐 **Example  4**
Rewriting an Expression as a Power before Using the Power Rule Expand log³(25) using the power rule for logs.

**Solution**

Expressing the argument as a power, we get log³(25) = log³(52). Next we identify the exponent, 2, and the base, 5, and rewrite the equivalent expression by multiplying the exponent times the logarithm of the base.

log³(5 2) = 2log³(5)

---
### ✏️ **Try It #4**
Expand ln (  1/x²  ).

---
### 📐 **Example  5**
Using the Power Rule in Reverse Rewrite 4ln(x) using the power rule for logs to a single logarithm with a leading coefficient of 1.

**Solution**

Because the logarithm of a power is the product of the exponent times the logarithm of the base, it follows that the product of a number and a logarithm can be written as a power. For the expression 4ln(x), we identify the factor, 4, as the exponent and the argument, x, as the base, and rewrite the product as a logarithm of a power: 4ln(x) = ln(x⁴).

---
### ✏️ **Try It #5**
Rewrite 2log³(4) using the power rule for logs to a single logarithm with a leading coefficient of 1. Expanding Logarithmic Expressions Taken together, the product rule, quotient rule, and power rule are often called “laws of logs.” Sometimes we apply more than one rule in order to simplify an expression. For example:

logb (  6(x)/(y)  ) = logb(6x) - logb(y)

= logb(6) + logb(x) - logb(y) We can use the power rule to expand logarithmic expressions involving negative and fractional exponents. Here is an alternate proof of the quotient rule for logarithms using the fact that a reciprocal is a negative power:

logb (  (A)/(C)  ) = logb(AC -1)

= logb(A) + logb(C -1)

= logb(A) + (-1)logb(C)

= logb(A) - logb(C) We can also apply the product rule to express a sum or difference of logarithms as the logarithm of a product. With practice, we can look at a logarithmic expression and expand it mentally, writing the final answer. Remember, however, that we can only do this with products, quotients, powers, and roots—never with addition or subtraction inside the argument of the logarithm.

---
### 📐 **Example  6**
Expanding Logarithms Using Product, Quotient, and Power Rules Rewrite ln (  x 4 y/7  ) as a sum or difference of logs.

**Solution**

First, because we have a quotient of two expressions, we can use the quotient rule:

ln (  x 4y ___ 7  ) = ln(x 4y)- ln(7) Then seeing the product in the first term, we use the product rule:

ln(x 4y) - ln(7) = ln(x 4) + ln(y) - ln(7) Finally, we use the power rule on the first term:

ln(x⁴)+ ln(y) - ln(7) = 4ln(x) + ln(y) - ln(7)

---
### ✏️ **Try It #6**
Expand log (  x² y³ _ z⁴  ).

---
### 📐 **Example  7**
Using the Power Rule for Logarithms to Simplify the Logarithm of a Radical Expression Expand log(√x ).

**Solution**

log(√x ) = log(x)  1/2 

=  1/2  log(x)

---
### ✏️ **Try It #7**
Expand ln( √x² ). Can we expand ln(x² + y²)? No. There is no way to expand the logarithm of a sum or difference inside the argument of the logarithm.

---
### 📐 **Example  8**
Expanding Complex Logarithmic Expressions Expand log⁶ (  64x³ (4x + 1) __ (2x - 1)  ).

**Solution**

We can expand by applying the Product and Quotient Rules. log⁶ (  64x³(4x + 1) __ (2x - 1)  ) = log⁶(64) + log⁶(x³) + log⁶(4x + 1) - log⁶(2x - 1) Apply the Quotient Rule.

= log⁶(26) + log⁶(x³) + log⁶(4x + 1) - log⁶(2x - 1) Simplify by writing 64 as 26.

= 6log⁶(2) + 3log⁶(x) + log⁶(4x + 1) - log⁶(2x - 1) Apply the Power Rule.

---
### ✏️ **Try It #8**
Expand ln (   √(x - 1)(2x + 1)² 

__ x 2 - 9  ). Condensing Logarithmic Expressions We can use the rules of logarithms we just learned to condense sums, differences, and products with the same base as a single logarithm. It is important to remember that the logarithms must have the same base to be combined. We will learn later how to change the base of any logarithm before condensing.

---
### 💡 **How To…**
Given a sum, difference, or product of logarithms with the same base, write an equivalent expression as a single logarithm. 1. Apply the power property first. Identify terms that are products of factors and a logarithm, and rewrite each as the logarithm of a power. 2. Next apply the product property. Rewrite sums of logarithms as the logarithm of a product. 3. Apply the quotient property last. Rewrite differences of logarithms as the logarithm of a quotient.

---
### 📐 **Example  9**
Using the Product and Quotient Rules to Combine Logarithms Write log³(5) + log³(8) - log³(2) as a single logarithm.

**Solution**

Using the product and quotient rules log³(5) + log³(8) = log³(5 ·  8) = log³(40) This reduces our original expression to log³(40) - log³(2) Then, using the quotient rule log³(40) - log³(2) = log³ (  40/2  ) = log³(20)

---
### ✏️ **Try It #9**
Condense log(3) - log(4) + log(5) - log(6).

---
### 📐 **Example  10**
Condensing Complex Logarithmic Expressions Condense log²(x 2) +  1/2 log²(x - 1) - 3log²((x + 3)²).

**Solution**

We apply the power rule first:

log²(x 2) +  1/2 log²(x - 1) - 3log²((x + 3)²) = log²(x²) + log²(√x - 1 ) - log²((x + 3)⁶) Next we apply the product rule to the sum:

log²(x 2) + log²(√x - 1 ) - log²((x + 3)⁶) = log²(x²√x - 1 ) - log²((x + 3)⁶) Finally, we apply the quotient rule to the difference:

log²(x 2√x - 1 )- log²((x + 3)⁶) = log²(  x²√x - 1  ________ (x + 3)⁶  )

---
### ✏️ **Try It #10**
Rewrite log(5) + 0.5log(x) - log(7x - 1) + 3log(x - 1) as a single logarithm.

---
### 📐 **Example  11**
Rewriting as a Single Logarithm Rewrite 2log(x) - 4log(x + 5) +  1/x log(3x + 5) as a single logarithm.

**Solution**

We apply the power rule first:

2log(x) - 4log(x + 5) +  1/x log(3x + 5) = log(x²) - log((x + 5)⁴) + log( (3x + 5)x -1 ) Next we apply the product rule to the sum:

log(x²)- log((x + 5)⁴) + log( (3x + 5)x -1 ) = log(x²)- log( (x + 5)⁴(3x + 5)x -1 ) Finally, we apply the quotient rule to the difference:

log(x²) - log( (x + 5)⁴(3x + 5)x -1 ) = log(  x 2 __

(x + 5)⁴(3x + 5)x -1  )

---
### ✏️ **Try It #11**
Condense 4(3log(x) + log(x + 5) - log(2x + 3)).

---
### 📐 **Example  12**: Applying of the Laws of Logs

Recall that, in chemistry, pH = -log[H+]. If the concentration of hydrogen ions in a liquid is doubled, what is the effect on pH?

**Solution**

Suppose C is the original concentration of hydrogen ions, and P is the original pH of the liquid. Then P = -log(C). If the concentration is doubled, the new concentration is 2C. Then the pH of the new liquid is

pH = -log(2C) Using the product rule of logs pH = -log(2C) = -(log(2) + log(C)) = -log(2) - log(C) Since P = -log(C), the new pH is

pH = P - log(2) ≈ P - 0.301 When the concentration of hydrogen ions is doubled, the pH decreases by about 0.301.

---
### ✏️ **Try It #12**
How does the pH change when the concentration of positive hydrogen ions is decreased by half? Using the Change-of-Base Formula for Logarithms Most calculators can evaluate only common and natural logs. In order to evaluate logarithms with a base other than 10 or e, we use the change-of-base formula to rewrite the logarithm as the quotient of logarithms of any other base; when using a calculator, we would change them to common or natural logs. To derive the change-of-base formula, we use the one-to-one property and power rule for logarithms. Given any positive real numbers M, b, and n, where n ≠  1 and b ≠  1, we show

logb(M) =  logn(M) _ logn(b)  Let y = logb(M). By taking the log base n of both sides of the equation, we arrive at an exponential form, namely b y = M. It follows that

logn(b y) = logn(M) Apply the one-to-one property.

ylogn(b) = logn(M) Apply the power rule for logarithms.

y =  logn(M) _ logn(b)  Isolate y.

logb(M) =  logn(M) _ logn(b)  Substitute for y. For example, to evaluate log⁵(36) using a calculator, we must first rewrite the expression as a quotient of common or natural logs. We will use the common log.

log⁵(36) =  log(36) _ log(5)  Apply the change of base formula using base 10.

Use a calculator to evaluate to 4 decimal places.

the change-of-base formula The change-of-base formula can be used to evaluate a logarithm with any base. For any positive real numbers M, b, and n, where n ≠  1 and b ≠  1, logb(M) =  logn(M) _ logn(b) . It follows that the change-of-base formula can be used to rewrite a logarithm with any base as the quotient of common or natural logs. logb(M) =  ln(M) _ ln(b)  and logb(M) =  logn(M) _ logn(b) 

---
### 💡 **How To…**
Given a logarithm with the form logb(M), use the change-of-base formula to rewrite it as a quotient of logs with any positive base n, where n ≠  1. 1. Determine the new base n, remembering that the common log, log(x), has base 10, and the natural log, ln(x), has base e. 2. Rewrite the log as a quotient using the change-of-base formula a. The numerator of the quotient will be a logarithm with base n and argument M. b. The denominator of the quotient will be a logarithm with base n and argument b.

---
### 📐 **Example  13**
Changing Logarithmic Expressions to Expressions Involving Only Natural Logs Change log⁵(3) to a quotient of natural logarithms.

**Solution**

Because we will be expressing log⁵(3) as a quotient of natural logarithms, the new base, n = e. We rewrite the log as a quotient using the change-of-base formula. The numerator of the quotient will be the natural log with argument 3. The denominator of the quotient will be the natural log with argument 5. logb(M) =  ln(M) _ ln(b)  log⁵(3) =  ln(3) _ ln(5) 

---
### ✏️ **Try It #13**
Change log⁰.5(8) to a quotient of natural logarithms. Can we change common logarithms to natural logarithms? Yes. Remember that log(9) means log¹0(9). So, log(9) =  ln(9) _ ln(10) .

---
### 📐 **Example  14**
Using the Change-of-Base Formula with a Calculator Evaluate log²(10) using the change-of-base formula with a calculator.

**Solution**

According to the change-of-base formula, we can rewrite the log base 2 as a logarithm of any other base. Since our calculators can evaluate the natural log, we might choose to use the natural logarithm, which is the log base e. log²(10) =  ln(10) _ ln(2)  Apply the change of base formula using base e.

Use a calculator to evaluate to 4 decimal places.

---
### ✏️ **Try It #14**
Evaluate log⁵(100) using the change-of-base formula. > Access this online resource for additional instruction and practice with laws of logarithms. • The Properties of Logarithms (http://openstaxcollege.org/l/proplog) • Expand Logarithmic Expressions (http://openstaxcollege.org/l/expandlog) • Evaluate a Natural Logarithmic Expression (http://openstaxcollege.org/l/evaluatelog)

## 4.5 Section Exercises

---
### 4.5 section EXERCISES

Verbal 1. How does the power rule for logarithms help when solving logarithms with the form logb( n √x )? 2. What does the change-of-base formula do? Why is it useful when using a calculator? Algebraic For the following exercises, expand each logarithm as much as possible. Rewrite each expression as a sum, difference, or product of logs. 3. logb(7x ·  2y) 4. ln(3ab ·  5c) 5. logb (  13/17  ) 6. log⁴ (   (x)/(z) 

_ w  ) 7. ln (  1/4k  ) 8. log²(yx) For the following exercises, condense to a single logarithm if possible. 9. ln(7) + ln(x) + ln(y) 10. log³(2) + log³(a) + log³(11) + log³(b) 11. logb(28) - logb(7) 12. ln(a) - ln(d) - ln(c) 13. -logb(  1/7  ) _ 3 ln(8) For the following exercises, use the properties of logarithms to expand each logarithm as much as possible. Rewrite each expression as a sum, difference, or product of logs. 15. log (  x¹5 y¹3/z¹9  ) 16. ln (  a-2/b-4 c⁵  ) 17. log(√x³ y-4 ) 18. ln ( y√_____

 y/1 - y   ) 19. log(x 2 y 3  √x² y⁵ ) For the following exercises, condense each expression to a single logarithm using the properties of logarithms. 20. log(2x⁴) + log(3x⁵) 21. ln(6x⁹) - ln(3x²) 22. 2log(x) + 3log(x + 1) 23. log(x) - 1/2 log(y) + 3log(z) 24. 4log⁷ (c) +  log⁷(a) _  +  log⁷(b) _  For the following exercises, rewrite each expression as an equivalent ratio of logs using the indicated base. 25. log⁷(15) to base e For the following exercises, suppose log⁵ (6) = a and log⁵ (11) = b. Use the change-of-base formula along with properties of logarithms to rewrite each expression in terms of a and b. Show the steps for solving. _ 11  ) Numeric For the following exercises, use properties of logarithms to evaluate without using a calculator. 30. log³ (  1/9  ) - 3log³ (3) _ 3log⁸(4)  32. 2log⁹(3) - 4log⁹(3) + log⁹ (  1/For the following exercises, use the change-of-base formula to evaluate each expression as a quotient of natural logs. Use a calculator to approximate each to five decimal places. _ 2  ) 37. log  1 Extensions 38. Use the product rule for logarithms to find all x values such that log¹2(2x + 6) + log¹2(x + 2) = 2. Show the steps for solving. 39. Use the quotient rule for logarithms to find all x values such that log⁶(x + 2) - log⁶ (x - 3) = 1. Show the steps for solving. 40. Can the power property of logarithms be derived from the power property of exponents using the equation b x = m? If not, explain why. If so, show the derivation. 41. Prove that logb (n) =  _ logn(b)  for any positive integers b > 1 and n > 1. 42. Does log⁸1(2401) = log³(7)? Verify the claim algebraically.

Learning Objectives
In this section, you will:
• Use like bases to solve exponential equations.
• Use logarithms to solve exponential equations.
• Use the definition of a logarithm to solve logarithmic equations.
• Use the one-to-one property of logarithms to solve logarithmic equations.
• Solve applied problems involving exponential and logarithmic equations.
