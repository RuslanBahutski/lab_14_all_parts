"""
grade.py
=====
Translate a numeric grade to a letter grade.
1. Ask the user for a numeric grade.
2. Use the table below to calculate the corresponding letter:
    90-100 - A
    80-89  - B
    70-79  - C
    60-69  - D
     0-59  - F
3. Print out both the number and letter grade.
4. If the value is not numeric, allow the error to happen.
5. However, if the number is not within the ranges specified in the table, output:
    "Could not translate %s into a letter grade" where %s is the numeric grade"

Example Output (consider text after the ">" user input):

Run 1:
-----
What grade did you get?
> 59
Number Grade: 59
Letter Grade: F

Run 2:
-----
What grade did you get?
> 89
Number Grade: 89
Letter Grade: B

Run 3:
-----
What grade did you get?
> 90
Number Grade: 90
Letter Grade: A

Run 4:
-----
What grade did you get?
> -12
Couldn't translate -12 into a letter grade
"""
Grade = raw_input ('enter a numeric grade ')

Grade = int (Grade)
if (Grade) > 90 and (Grade) < 100:
    print('A')

    print('90 - 100')
if (Grade) > 80 and (Grade) < 89:
    print('B')

    print('80 - 89')
if (Grade) > 70 and (Grade) < 79:
    print('C')

    print('70 - 79')        
if (Grade) > 60 and (Grade) < 69:
    print('D')

    print('60 - 69')
if (Grade) > 0 and (Grade) < 59:
    print('F')

    print('0 - 59')            