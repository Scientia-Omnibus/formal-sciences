Formal Sciences — open textbook collection
============================================

Repository structure:

  Basic/
    Arithmetic & Algebra Basics    — pre-algebra, 11 chapters
    Algebra & Trigonometry Core    — high-school algebra & trig, 12 chapters

Each course is split into chapters, and chapters into individual lessons.
The material is adapted from open educational resources.
Math notation uses a custom inline HTML format (span/div with math classes).

Language subdirectories (en/, etc.) are meant to support multiple translations
down the line. Currently only English is available.

  ├── LICENSE                 GPLv3
  ├── .gitignore
  └── Basic/
      ├── Arithmetic & Algebra Basics/
      │   ├── 1-whole-numbers/
      │   ├── 2-the-language-of-algebra/
      │   ├── 3-integers/
      │   ├── 4-fractions/
      │   ├── 5-decimals/
      │   ├── 6-percents/
      │   ├── 7-the-properties-of-real-numbers/
      │   ├── 8-solving-linear-equations/
      │   ├── 9-math-models-and-geometry/
      │   ├── 10-polynomials/
      │   └── 11-graphs/
      └── Algebra & Trigonometry Core/
          ├── 1-functions/
          ├── 2-linear-functions/
          ├── 3-polynomial-and-rational-functions/
          ├── 4-exponential-and-logarithmic-functions/
          ├── 5-trigonometric-functions/
          ├── 6-periodic-functions/
          ├── 7-trigonometric-identities-and-equations/
          ├── 8-further-applications-of-trigonometry/
          ├── 9-systems-of-equations-and-inequalities/
          ├── 10-analytic-geometry/
          ├── 11-sequences-probability-and-counting-theory/
          └── 12-introduction-to-calculus/


Advanced (planned)
------------------

The following areas are not yet populated but are on the roadmap:

  • Logic                — propositional & predicate logic, proofs
  • Discrete Mathematics — set theory, combinatorics, graph theory, algorithms
  • Statistics & Probability Theory

The naming and structure will follow the same pattern as Basic/:
one directory per broad domain, split into courses, chapters, and lessons,
with language subdirectories for future translations.
