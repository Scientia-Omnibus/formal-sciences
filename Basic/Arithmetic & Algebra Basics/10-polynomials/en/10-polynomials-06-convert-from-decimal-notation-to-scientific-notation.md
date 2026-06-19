<style>
.math-inline {
    font-style: italic;
    padding: 2px 6px;
    border-radius: 4px;
    background: #f8f9fa;
    font-family: Georgia, serif;
}
.math-display {
    background: #f8f9fa;
    border-left: 4px solid #4a90d9;
    padding: 16px 20px;
    margin: 16px 0;
    border-radius: 6px;
    font-size: 1.15em;
    font-family: Georgia, serif;
    text-align: center;
    line-height: 2;
    overflow-x: auto;
}
.example-box, .example {
    background: #f0f8ff;
    border-left: 4px solid #2e86de;
    padding: 12px 20px;
    margin: 16px 0;
    border-radius: 6px;
}
.tryit-box, .tryit {
    background: #f0fff4;
    border-left: 4px solid #27ae60;
    padding: 12px 20px;
    margin: 16px 0;
    border-radius: 6px;
}
.solution-box, .solution {
    background: #fef9e7;
    border-left: 4px solid #f39c12;
    padding: 12px 20px;
    margin: 12px 0;
    border-radius: 6px;
}
.check-box, .check {
    background: #fef9e7;
    border-left: 4px solid #f39c12;
    padding: 12px 20px;
    margin: 12px 0;
    border-radius: 6px;
}
.prep-quiz {
    background: #fff3cd;
    border: 1px solid #ffc107;
    padding: 12px 20px;
    margin: 16px 0;
    border-radius: 6px;
}
.def-label, .definition-label {
    font-weight: bold;
    font-size: 1.1em;
    margin: 20px 0 8px 0;
    color: #2c3e50;
    display: block;
}
.math-display sup, .math-inline sup { font-size: 0.75em; line-height: 0; }
.math-display sub, .math-inline sub { font-size: 0.75em; line-height: 0; }
</style>


---


---

## Convert from Decimal Notation to Scientific Notation


Remember working with place value for whole numbers and decimals? Our number system is based on powers of <span class="math-inline">10.</span> We use tens, hundreds, thousands, and so on. Our decimal numbers are also based on powers of tens—tenths, hundredths, thousandths, and so on.

Consider the numbers <span class="math-inline">4000</span> and <span class="math-inline">0.004.</span> We know that <span class="math-inline">4000</span> means <span class="math-inline">4 ×  1000</span> and <span class="math-inline">0.004</span> means <span class="math-inline">4 ×  <sup>1</sup>∕<sub>1000</sub>.</span> If we write the <span class="math-inline">1000</span> as a power of ten in exponential form, we can rewrite these numbers in this way:


<div class="math-display">
4000 &  &  & 0.004 \\
4 ×  1000 &  &  & 4 ×  <sup>1</sup>∕<sub>1000</sub> \\
4 ×  10<sup>3</sup> &  &  & 4 ×  <sup>1</sup>∕<sub>10<sup>3</sup></sub> \\
 &  &  & 4 ×  10<sup>−3</sup>
</div>


When a number is written as a product of two numbers, where the first factor is a number greater than or equal to one but less than <span class="math-inline">10,</span> and the second factor is a power of <span class="math-inline">10</span> written in exponential form, it is said to be in *scientific notation.*


<div class="definition-label">**Scientific Notation**</div>


A number is expressed in **scientific notation** when it is of the form


<div class="math-display">
a ×  10<sup>n</sup>
</div>


where <span class="math-inline">a≥ 1</span> and <span class="math-inline">a<10</span> and <span class="math-inline">n</span> is an integer.

It is customary in scientific notation to use <span class="math-inline">×</span> as the multiplication sign, even though we avoid using this sign elsewhere in algebra.

Scientific notation is a useful way of writing very large or very small numbers. It is used often in the sciences to make calculations easier.

If we look at what happened to the decimal point, we can see a method to easily convert from decimal notation to scientific notation.

In both cases, the decimal was moved <span class="math-inline">3</span> places to get the first factor, <span class="math-inline">4,</span> by itself.

- The power of <span class="math-inline">10</span> is positive when the number is larger than <span class="math-inline">1: 4000=4 ×  10<sup>3</sup>.</span>

- The power of <span class="math-inline">10</span> is negative when the number is between <span class="math-inline">0</span> and <span class="math-inline">1: 0.004=4 ×  10<sup>-3</sup>.</span>


<div class="example">
**Example**


Write <span class="math-inline">37,000</span> in scientific notation.


<div class="solution">
<span class="def-label">Solution</span>


*Step 1*: Move the decimal point so that the first factor is greater than or equal to 1 but less than 10.


*Step 2*: Count the number of decimal places, <span class="math-inline">n</span>, that the decimal point was moved.
3.70000
4 places


*Step 3*: Write the number as a product with a power of 10.

<span class="math-inline">3.7× 10<sup>4</sup></span>


If the original number is:

  - greater than 1, the power of 10 will be <span class="math-inline">10<sup>n</sup></span>.
  - between 0 and 1, the power of 10 will be <span class="math-inline">10<sup>−n</sup></span>


*Step 4*: Check.


<span class="math-inline">10<sup>4</sup></span> is 10,000 and 10,000 times 3.7 will be 37,000.


<span class="math-inline">37,000=3.7× 10<sup>4</sup></span>


<div class="tryit">
**Try It**


Write in scientific notation: <span class="math-inline">96,000.</span>


9.6 × 104


<div class="tryit">
**Try It**


Write in scientific notation: <span class="math-inline">48,300.</span>


4.83 × 104


<div class="definition-label">**Convert from decimal notation to scientific notation.**</div>


- Move the decimal point so that the first factor is greater than or equal to <span class="math-inline">1</span> but less than <span class="math-inline">10.</span>

- Count the number of decimal places, <span class="math-inline">n,</span> that the decimal point was moved.

- Write the number as a product with a power of <span class="math-inline">10.</span>

  - If the original number is:

  - greater than <span class="math-inline">1,</span> the power of <span class="math-inline">10</span> will be <span class="math-inline">10<sup>n</sup>.</span>
  - between <span class="math-inline">0</span> and <span class="math-inline">1,</span> the power of <span class="math-inline">10</span> will be <span class="math-inline">10<sup>-n</sup>.</span>

- Check.


<div class="example">
**Example**


Write in scientific notation: <span class="math-inline">0.0052.</span>


<div class="solution">
<span class="def-label">Solution</span>


0.0052


Move the decimal point to get 5.2, a number between 1 and 10.


Count the number of decimal places the point was moved.
3 places


Write as a product with a power of 10.
<span class="math-inline">5.2× 10<sup>−3</sup></span>


<div class="check-box">
**Check your answer:
\(5.2 \times  10^{−3} \\
5.2 \times  \frac{1}{10^3} \\
 \\
 \\
 \\
 \\
0.0052\)**


<span class="math-inline">0.0052=5.2 ×  10<sup>−3</sup></span>


<div class="tryit">
**Try It**


Write in scientific notation: <span class="math-inline">0.0078.</span>


7.8 × 10−3


<div class="tryit">
**Try It**


Write in scientific notation: <span class="math-inline">0.0129.</span>


1.29 × 10−2


---


---

## Convert Scientific Notation to Decimal Form


How can we convert from scientific notation to decimal form? Let’s look at two numbers written in scientific notation and see.


<div class="math-display">
9.12 ×  10<sup>4</sup> &  &  & 9.12 ×  10<sup>−4</sup> \\
9.12 ×  10,000 &  &  & 9.12 ×  0.0001 \\
91,200 &  &  & 0.000912
</div>


If we look at the location of the decimal point, we can see an easy method to convert a number from scientific notation to decimal form.

In both cases the decimal point moved 4 places. When the exponent was positive, the decimal moved to the right. When the exponent was negative, the decimal point moved to the left.


<div class="example">
**Example**


Convert to decimal form: <span class="math-inline">6.2 ×  10<sup>3</sup>.</span>


<div class="solution">
<span class="def-label">Solution</span>


*Step 1*: Determine the exponent, <span class="math-inline">n</span>, on the factor 10.
<span class="math-inline">6.2× 10<sup>3</sup></span>


*Step 2*: Move the decimal point <span class="math-inline">n</span> places, adding zeros if needed.


  - If the exponent is positive, move the decimal point <span class="math-inline">n</span> places to the right.
  - If the exponent is negative, move the decimal point <span class="math-inline">|n|</span> places to the left.
6,200


*Step 3*: Check to see if your answer makes sense.


<span class="math-inline">10<sup>3</sup></span> is 1000 and 1000 times 6.2 will be 6,200.


<span class="math-inline">6.2× 10<sup>3</sup>=6,200</span>


<div class="tryit">
**Try It**


Convert to decimal form: <span class="math-inline">1.3 ×  10<sup>3</sup>.</span>


1,300


<div class="tryit">
**Try It**


Convert to decimal form: <span class="math-inline">9.25 ×  10<sup>4</sup>.</span>


92,500


<div class="definition-label">**Convert scientific notation to decimal form.**</div>


- Determine the exponent, <span class="math-inline">n,</span> on the factor <span class="math-inline">10.</span>

- Move the decimal <span class="math-inline">n</span> places, adding zeros if needed.

  - If the exponent is positive, move the decimal point <span class="math-inline">n</span> places to the right.
  - If the exponent is negative, move the decimal point <span class="math-inline">|n|</span> places to the left.


- Check.


<div class="example">
**Example**


Convert to decimal form: <span class="math-inline">8.9 ×  10<sup>−2</sup>.</span>


<div class="solution">
<span class="def-label">Solution</span>


<span class="math-inline">8.9× 10<sup>−2</sup></span>


Determine the exponent <span class="math-inline">n</span>, on the factor 10.
The exponent is −2.


Move the decimal point 2 places to the left.


Add zeros as needed for placeholders.
0.089


<span class="math-inline">8.9× 10<sup>−2</sup>=0.089</span>


The Check is left to you.


<div class="tryit">
**Try It**


Convert to decimal form: <span class="math-inline">1.2 ×  10<sup>−4</sup>.</span>


0.00012


<div class="tryit">
**Try It**


Convert to decimal form: <span class="math-inline">7.5 ×  10<sup>−2</sup>.</span>


0.075


---


---

## Multiply and Divide Using Scientific Notation


We use the Properties of Exponents to multiply and divide numbers in scientific notation.


<div class="example">
**Example**


Multiply. Write answers in decimal form: <span class="math-inline">(4 ×  10<sup>5</sup>)(2 ×  10<sup>−7</sup>).</span>


<div class="solution">
<span class="def-label">Solution</span>


<span class="math-inline">(4 ×  10<sup>5</sup>)(2 ×  10<sup>−7</sup>)</span>


Use the Commutative Property to rearrange the factors.
<span class="math-inline">4· 2· 10<sup>5</sup>· 10<sup>−7</sup></span>


Multiply 4 by 2 and use the Product Property to multiply <span class="math-inline">10<sup>5</sup></span> by <span class="math-inline">10<sup>−7</sup></span>.
<span class="math-inline">8 ×  10<sup>−2</sup></span>


Change to decimal form by moving the decimal two places left.
<span class="math-inline">0.08</span>


<div class="tryit">
**Try It**


Multiply. Write answers in decimal form: <span class="math-inline">(3 ×  10<sup>6</sup>)(2 ×  10<sup>−8</sup>).</span>


0.06


<div class="tryit">
**Try It**


Multiply. Write answers in decimal form: <span class="math-inline">(3 ×  10<sup>−2</sup>)(3 ×  10<sup>−1</sup>).</span>


0.009


<div class="example">
**Example**


Divide. Write answers in decimal form: <span class="math-inline"><sup>9 ×  10<sup>3</sup></sup>∕<sub>3 ×  10<sup>−2</sub></sup>.</span>


<div class="solution">
<span class="def-label">Solution</span>


<span class="math-inline"><sup>9 ×  10<sup>3</sup></sup>∕<sub>3 ×  10<sup>−2</sub></sup></span>


Separate the factors.
<span class="math-inline"><sup>9</sup>∕<sub>3</sub> ×  <sup>10<sup>3</sup></sup>∕<sub>10<sup>−2</sub></sup></span>


Divide 9 by 3 and use the Quotient Property to divide <span class="math-inline">10<sup>3</sup></span> by <span class="math-inline">10<sup>−2</sup></span>.
<span class="math-inline">3 ×  10<sup>5</sup></span>


Change to decimal form by moving the decimal five places right.
<span class="math-inline">300,000</span>


<div class="tryit">
**Try It**


Divide. Write answers in decimal form: <span class="math-inline"><sup>8 ×  10<sup>4</sup></sup>∕<sub>2 ×  10<sup>−1</sub></sup>.</span>


400,000


<div class="tryit">
**Try It**


Divide. Write answers in decimal form: <span class="math-inline"><sup>8 ×  10<sup>2</sup></sup>∕<sub>4 ×  10<sup>−2</sub></sup>.</span>


20,000


<div class="definition-label">**ACCESS ADDITIONAL ONLINE RESOURCES**</div>


- Negative Exponents

- Examples of Simplifying Expressions with Negative Exponents

- Scientific Notation


---


---

## Key Concepts


- *Summary of Exponent Properties*

  - If <span class="math-inline">a,b</span> are real numbers and <span class="math-inline">m,n</span> are integers, then
\(Product Property &  &  & a^m\cdot a^n=a^{m+n} \\
Power Property &  &  & (a^m)^n=a^{m\cdot n} \\
Product to a Power Property &  &  & (ab)^m=a^mb^m \\
Quotient Property &  &  & \frac{a^m}{a^n}=a^{m-n}, a\ne 0 \\
Zero Exponent Property &  &  & a^0=1, \\
Quotient to a Power Property &  &  & (\frac{a}{b})^m=\frac{a^m}{b^m}, b\ne 0 \\
Definition of Negative Exponent &  &  & a^{-n}=\frac{1}{a^n}\)


- *Convert from Decimal Notation to Scientific Notation:* To convert a decimal to scientific notation:

  - Move the decimal point so that the first factor is greater than or equal to 1 but less than 10.
  - Count the number of decimal places, <span class="math-inline">n</span>, that the decimal point was moved.
  - Write the number as a product with a power of 10.
  - If the original number is greater than 1, the power of 10 will be <span class="math-inline">10<sup>n</sup></span>.
  - If the original number is between 0 and 1, the power of 10 will be <span class="math-inline">10<sup>-n</sup></span>.
  - Check.


- *Convert Scientific Notation to Decimal Form:* To convert scientific notation to decimal form:

  - Determine the exponent, <span class="math-inline">n</span>, on the factor 10.
  - Move the decimal <span class="math-inline">n</span> places, adding zeros if needed.

  - If the exponent is positive, move the decimal point <span class="math-inline">n</span>  places to the right.
  - If the exponent is negative, move the decimal point <span class="math-inline">|n|</span>  places to the left.
  - Check.


### Practice Makes Perfect

*Use the Definition of a Negative Exponent*

In the following exercises, simplify.


<span class="math-inline">5<sup>−3</sup></span>


<span class="math-inline">8<sup>−2</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>64</sub></span>


<span class="math-inline">3<sup>−4</sup></span>


<span class="math-inline">2<sup>−5</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>32</sub></span>


<span class="math-inline">7<sup>−1</sup></span>


<span class="math-inline">10<sup>−1</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>10</sub></span>


<span class="math-inline">2<sup>−3</sup>+2<sup>−2</sup></span>


<span class="math-inline">3<sup>−2</sup>+3<sup>−1</sup></span>


<span class="math-inline"><sup>4</sup>∕<sub>9</sub></span>


<span class="math-inline">3<sup>−1</sup>+4<sup>−1</sup></span>


<span class="math-inline">10<sup>−1</sup>+2<sup>−1</sup></span>


<span class="math-inline"><sup>3</sup>∕<sub>5</sub></span>


<span class="math-inline">10<sup>0</sup>-10<sup>−1</sup>+10<sup>−2</sup></span>


<span class="math-inline">2<sup>0</sup>-2<sup>−1</sup>+2<sup>−2</sup></span>


<span class="math-inline"><sup>3</sup>∕<sub>4</sub></span>


  - ⓐ <span class="math-inline">(−6)<sup>−2</sup></span>
  - ⓑ <span class="math-inline">-6<sup>−2</sup></span>


  - ⓐ <span class="math-inline">(−8)<sup>−2</sup></span>
  - ⓑ <span class="math-inline">-8<sup>−2</sup></span>


  - ⓐ <span class="math-inline"><sup>1</sup>∕<sub>64</sub></span>
  - ⓑ <span class="math-inline">-<sup>1</sup>∕<sub>64</sub></span>


  - ⓐ <span class="math-inline">(−10)<sup>−4</sup></span>
  - ⓑ <span class="math-inline">-10<sup>−4</sup></span>


  - ⓐ <span class="math-inline">(−4)<sup>−6</sup></span>
  - ⓑ <span class="math-inline">-4<sup>−6</sup></span>


  - ⓐ <span class="math-inline"><sup>1</sup>∕<sub>4096</sub></span>
  - ⓑ <span class="math-inline">-<sup>1</sup>∕<sub>4096</sub></span>


  - ⓐ <span class="math-inline">5· 2<sup>−1</sup></span>
  - ⓑ <span class="math-inline">(5· 2)<sup>−1</sup></span>


  - ⓐ <span class="math-inline">10· 3<sup>−1</sup></span>
  - ⓑ <span class="math-inline">(10· 3)<sup>−1</sup></span>


  - ⓐ <span class="math-inline"><sup>10</sup>∕<sub>3</sub></span>
  - ⓑ <span class="math-inline"><sup>1</sup>∕<sub>30</sub></span>


  - ⓐ <span class="math-inline">4· 10<sup>−3</sup></span>
  - ⓑ <span class="math-inline">(4· 10)<sup>−3</sup></span>


  - ⓐ <span class="math-inline">3· 5<sup>−2</sup></span>
  - ⓑ <span class="math-inline">(3· 5)<sup>−2</sup></span>


  - ⓐ <span class="math-inline"><sup>3</sup>∕<sub>25</sub></span>
  - ⓑ <span class="math-inline"><sup>1</sup>∕<sub>225</sub></span>


<span class="math-inline">n<sup>−4</sup></span>


<span class="math-inline">p<sup>−3</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>p<sup>3</sup></sub></span>


<span class="math-inline">c<sup>−10</sup></span>


<span class="math-inline">m<sup>−5</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>m<sup>5</sup></sub></span>


  - ⓐ <span class="math-inline">4x<sup>−1</sup></span>
  - ⓑ <span class="math-inline">(4x)<sup>−1</sup></span>
  - ⓒ <span class="math-inline">(−4x)<sup>−1</sup></span>


  - ⓐ <span class="math-inline">3q<sup>−1</sup></span>
  - ⓑ <span class="math-inline">(3q)<sup>−1</sup></span>
  - ⓒ <span class="math-inline">(−3q)<sup>−1</sup></span>


  - ⓐ <span class="math-inline"><sup>3</sup>∕<sub>q</sub></span>
  - ⓑ <span class="math-inline"><sup>1</sup>∕<sub>3q</sub></span>
  - ⓒ <span class="math-inline">-<sup>1</sup>∕<sub>3q</sub></span>


  - ⓐ <span class="math-inline">6m<sup>−1</sup></span>
  - ⓑ <span class="math-inline">(6m)<sup>−1</sup></span>
  - ⓒ <span class="math-inline">(−6m)<sup>−1</sup></span>


  - ⓐ <span class="math-inline">10k<sup>−1</sup></span>
  - ⓑ <span class="math-inline">(10k)<sup>−1</sup></span>
  - ⓒ <span class="math-inline">(−10k)<sup>−1</sup></span>


  - ⓐ <span class="math-inline"><sup>10</sup>∕<sub>k</sub></span>
  - ⓑ <span class="math-inline"><sup>1</sup>∕<sub>10k</sub></span>
  - ⓒ <span class="math-inline">-<sup>1</sup>∕<sub>10k</sub></span>

*Simplify Expressions with Integer Exponents*

In the following exercises, simplify*.*


<span class="math-inline">p<sup>−4</sup>· p<sup>8</sup></span>


<span class="math-inline">r<sup>−2</sup>· r<sup>5</sup></span>


*r*3


<span class="math-inline">n<sup>−10</sup>· n<sup>2</sup></span>


<span class="math-inline">q<sup>−8</sup>· q<sup>3</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>q<sup>5</sup></sub></span>


<span class="math-inline">k<sup>−3</sup>· k<sup>−2</sup></span>


<span class="math-inline">z<sup>−6</sup>· z<sup>−2</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>z<sup>8</sup></sub></span>


<span class="math-inline">a· a<sup>−4</sup></span>


<span class="math-inline">m· m<sup>−2</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>m</sub></span>


<span class="math-inline">p<sup>5</sup>· p<sup>−2</sup>· p<sup>−4</sup></span>


<span class="math-inline">x<sup>4</sup>· x<sup>−2</sup>· x<sup>−3</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>x</sub></span>


<span class="math-inline">a<sup>3</sup>b<sup>−3</sup></span>


<span class="math-inline">u<sup>2</sup>v<sup>−2</sup></span>


<span class="math-inline"><sup>u<sup>2</sup></sup>∕<sub>v<sup>2</sup></sub></span>


<span class="math-inline">(x<sup>5</sup>y<sup>−1</sup>)(x<sup>−10</sup>y<sup>−3</sup>)</span>


<span class="math-inline">(a<sup>3</sup>b<sup>−3</sup>)(a<sup>−5</sup>b<sup>−1</sup>)</span>


<span class="math-inline"><sup>1</sup>∕<sub>a<sup>2</sup>b<sup>4</sup></sub></span>


<span class="math-inline">(uv<sup>−2</sup>)(u<sup>−5</sup>v<sup>−4</sup>)</span>


<span class="math-inline">(pq<sup>−4</sup>)(p<sup>−6</sup>q<sup>−3</sup>)</span>


<span class="math-inline"><sup>1</sup>∕<sub>p<sup>5</sup>q<sup>7</sup></sub></span>


<span class="math-inline">(−2r<sup>−3</sup>s<sup>9</sup>)(6r<sup>4</sup>s<sup>−5</sup>)</span>


<span class="math-inline">(−3p<sup>−5</sup>q<sup>8</sup>)(7p<sup>2</sup>q<sup>−3</sup>)</span>


<span class="math-inline">-<sup>21q<sup>5</sup></sup>∕<sub>p<sup>3</sup></sub></span>


<span class="math-inline">(−6m<sup>−8</sup>n<sup>−5</sup>)(−9m<sup>4</sup>n<sup>2</sup>)</span>


<span class="math-inline">(−8a<sup>−5</sup>b<sup>−4</sup>)(−4a<sup>2</sup>b<sup>3</sup>)</span>


<span class="math-inline"><sup>32</sup>∕<sub>a<sup>3</sup>b</sub></span>


<span class="math-inline">(a<sup>3</sup>)<sup>−3</sup></span>


<span class="math-inline">(q<sup>10</sup>)<sup>−10</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>q<sup>100</sub></sup></span>


<span class="math-inline">(n<sup>2</sup>)<sup>−1</sup></span>


<span class="math-inline">(x<sup>4</sup>)<sup>−1</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>x<sup>4</sup></sub></span>


<span class="math-inline">(y<sup>−5</sup>)<sup>4</sup></span>


<span class="math-inline">(p<sup>−3</sup>)<sup>2</sup></span>


<span class="math-inline"><sup>1</sup>∕<sub>p<sup>6</sup></sub></span>


<span class="math-inline">(q<sup>−5</sup>)<sup>−2</sup></span>


<span class="math-inline">(m<sup>−2</sup>)<sup>−3</sup></span>


*m*6


<span class="math-inline">(4y<sup>−3</sup>)<sup>2</sup></span>


<span class="math-inline">(3q<sup>−5</sup>)<sup>2</sup></span>


<span class="math-inline"><sup>9</sup>∕<sub>q<sup>10</sub></sup></span>


<span class="math-inline">(10p<sup>−2</sup>)<sup>−5</sup></span>


<span class="math-inline">(2n<sup>−3</sup>)<sup>−6</sup></span>


<span class="math-inline">\frac{n<sup>18</sup>{64}</span>


<span class="math-inline"><sup>u<sup>9</sup></sup>∕<sub>u<sup>−2</sub></sup></span>


<span class="math-inline"><sup>b<sup>5</sup></sup>∕<sub>b<sup>−3</sub></sup></span>


*b*8


<span class="math-inline">\frac{x<sup>−6</sup>{x<sup>4</sup></span>


<span class="math-inline"><sup>m<sup>5</sup></sup>∕<sub>m<sup>−2</sub></sup></span>


*m*7


<span class="math-inline"><sup>q<sup>3</sup></sup>∕<sub>q<sup>12</sub></sup></span>


<span class="math-inline"><sup>r<sup>6</sup></sup>∕<sub>r<sup>9</sup></sub></span>


<span class="math-inline"><sup>1</sup>∕<sub>r<sup>3</sup></sub></span>


<span class="math-inline">\frac{n<sup>−4</sup>{n<sup>−10</sup></span>


<span class="math-inline">\frac{p<sup>−3</sup>{p<sup>−6</sup></span>


*p*3


*Convert from Decimal Notation to Scientific Notation*

In the following exercises, write each number in scientific notation.


45,000


280,000


2.8 × 105


8,750,000


1,290,000


1.29 × 106


0.036


0.041


4.1 × 10−2


0.00000924


0.0000103


1.03 × 10−5


The population of the United States on July 4, 2010 was almost <span class="math-inline">310,000,000.</span>


The population of the world on July 4, 2010 was more than <span class="math-inline">6,850,000,000.</span>


6.85 × 109


The average width of a human hair is <span class="math-inline">0.0018</span> centimeters.


The probability of winning the <span class="math-inline">2010</span> Megamillions lottery is about <span class="math-inline">0.0000000057.</span>


5.7 × 10−9


*Convert Scientific Notation to Decimal Form*

In the following exercises, convert each number to decimal form.


<span class="math-inline">4.1 ×  10<sup>2</sup></span>


<span class="math-inline">8.3 ×  10<sup>2</sup></span>


830


<span class="math-inline">5.5 ×  10<sup>8</sup></span>


<span class="math-inline">1.6 ×  10<sup>10</sup></span>


16,000,000,000


<span class="math-inline">3.5 ×  10<sup>−2</sup></span>


<span class="math-inline">2.8 ×  10<sup>−2</sup></span>


0.028


<span class="math-inline">1.93 ×  10<sup>−5</sup></span>


<span class="math-inline">6.15 ×  10<sup>−8</sup></span>


0.0000000615


In 2010, the number of Facebook users each day who changed their status to ‘engaged’ was <span class="math-inline">2 ×  10<sup>4</sup>.</span>


At the start of 2012, the US federal budget had a deficit of more than <span class="math-inline">$1.5 ×  10<sup>13</sup>.</span>


$15,000,000,000,000


The concentration of carbon dioxide in the atmosphere is <span class="math-inline">3.9 ×  10<sup>−4</sup>.</span>


The width of a proton is <span class="math-inline">1 ×  10<sup>−5</sup></span> of the width of an atom.


0.00001


*Multiply and Divide Using Scientific Notation*

In the following exercises, multiply or divide and write your answer in decimal form.


<span class="math-inline">(2 ×  10<sup>5</sup>)(2 ×  10<sup>−9</sup>)</span>


<span class="math-inline">(3 ×  10<sup>2</sup>)(1 ×  10<sup>−5</sup>)</span>


0.003


<span class="math-inline">(1.6 ×  10<sup>−2</sup>)(5.2 ×  10<sup>−6</sup>)</span>


<span class="math-inline">(2.1 ×  10<sup>−4</sup>)(3.5 ×  10<sup>−2</sup>)</span>


0.00000735


<span class="math-inline"><sup>6 ×  10<sup>4</sup></sup>∕<sub>3 ×  10<sup>−2</sub></sup></span>


<span class="math-inline"><sup>8 ×  10<sup>6</sup></sup>∕<sub>4 ×  10<sup>−1</sub></sup></span>


20,000,000


<span class="math-inline">\frac{7 ×  10<sup>−2</sup>{1 ×  10<sup>−8</sup></span>


<span class="math-inline">\frac{5 ×  10<sup>−3</sup>{1 ×  10<sup>−10</sup></span>


50,000,000


### Everyday Math


*Calories* In May 2010 the Food and Beverage Manufacturers pledged to reduce their products by <span class="math-inline">1.5</span> trillion calories by the end of 2015.

  - ⓐ Write <span class="math-inline">1.5</span> trillion in decimal notation.
  - ⓑ Write <span class="math-inline">1.5</span> trillion in scientific notation.


*Length of a year* The difference between the calendar year and the astronomical year is <span class="math-inline">0.000125</span> day.

  - ⓐ Write this number in scientific notation.
  - ⓑ How many years does it take for the difference to become 1 day?


  - ⓐ 1.25 × 10−4
  - ⓐ 8,000


*Calculator display* Many calculators automatically show answers in scientific notation if there are more digits than can fit in the calculator’s display. To find the probability of getting a particular 5-card hand from a deck of cards, Mario divided <span class="math-inline">1</span> by <span class="math-inline">2,598,960</span> and saw the answer <span class="math-inline">3.848 ×  10<sup>−7</sup>.</span> Write the number in decimal notation.


*Calculator display* Many calculators automatically show answers in scientific notation if there are more digits than can fit in the calculator’s display. To find the number of ways Barbara could make a collage with <span class="math-inline">6</span> of her <span class="math-inline">50</span> favorite photographs, she multiplied <span class="math-inline">50· 49· 48· 47· 46· 45.</span> Her calculator gave the answer <span class="math-inline">1.1441304 ×  10<sup>10</sup>.</span> Write the number in decimal notation.


11,441,304,000


### Writing Exercises


  - ⓐ Explain the meaning of the exponent in the expression <span class="math-inline">2<sup>3</sup>.</span>
  - ⓑ Explain the meaning of the exponent in the expression <span class="math-inline">2<sup>−3</sup></span>


When you convert a number from decimal notation to scientific notation, how do you know if the exponent will be positive or negative?


Answers will vary.


### Self Check

ⓐ After completing the exercises, use this checklist to evaluate your mastery of the objectives of this section.


ⓑ After looking at the checklist, do you think you are well prepared for the next section? Why or why not?


<div class="prep-quiz">
**Be Prepared!**


Before you get started, take this readiness quiz.


Factor <span class="math-inline">56</span> into primes.

If you missed this problem, review .


<span class="math-inline">2· 2· 2· 7</span>


<div class="prep-quiz">
**Be Prepared!**


Multiply: <span class="math-inline">−3(6a+11).</span>

If you missed this problem, review .


<span class="math-inline">-18a-33</span>


<div class="prep-quiz">
**Be Prepared!**


Multiply: <span class="math-inline">4x<sup>2</sup>(x<sup>2</sup>+3x-1).</span>

If you missed this problem, review .


<span class="math-inline">4x<sup>4</sup>+12x<sup>3</sup>-4x<sup>2</sup></span>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>
