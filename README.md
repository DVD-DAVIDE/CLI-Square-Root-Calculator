# CLI-Square-Root-Calculator

A simple square root calculator.

---

## Files

> NOTE: file extensions aren't specified due to the various languages used. Still, the sintax is the same, besides the language.

> NOTE: `<engine>` is the eventual program running the code (e.g. 'java', 'python', etc.)

- `squareroot`: main file with square root function
  - Running:  
    - With `$<engine> squareroot <number>`:
      > \<number\> is the number whose square root has to be extracted. If not provided, user is prompted by default.

- `testsquareroot`: testing file executing the same code as `squareroot` repeatedly with random parameters, outputting only the results different from the other function defined (by default from the `math` library, or equivalent)
  - Running:
    - With `$<engine> testsquareroot <iters>`:
      > \<iters\> is the number of times the squareroot will be calculated with random parameter. If not provided, default is 100.

## License

This project is licensed under the terms of the MIT license.
