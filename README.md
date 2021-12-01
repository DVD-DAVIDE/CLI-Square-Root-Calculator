# CLI-Square-Root-Calculator
It's a simple square root calculator.

## Files
 - `squareroot.py`: main file with the square root function
   - Running:
     - With `$python squareroot.py <number>`:
       - <number> is the number whose square root has to be extracted
     - With `$python squareroot.py`:
       - Will be asked for the number to extract
 - `testsquareroot.py`: testing file executing the same code as `squareroot.py` repeatedly with random parameters, outputting only the results different from the other function (`math.sqrt()` by default)
   - Running:
     - With `$python testsquareroot.py <iters>`:
       - <iters> is the number of times the squareroot will be calculated with random parameters
     - With `$python testsquareroot.py`:
       - <iters> parameter is default (100)
