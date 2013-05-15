"""
go_for_gold.py
=====
Translate an athlete's finishing placement (1st, 2nd and 3rd) into its Olympic medal value: 1 for gold, 2 for silver, 3 for bronze and anything else means no medal.  Do this by asking for user input.  For example:

What number should I translate into a medal?
>1
gold

What number should I translate into a medal?
>3
bronze

What number should I translate into a medal?
>23
no medal for you!

"""
medalraw_imput('what number should i translate into a medal?\n> ')

if (medal) < 1 or (medal) >3:
	print('not valid placement')
elif medal == 1:
	print('gold')
elif medal == 3:
	print('bronze')
elif medal == 2:
	print('silver')
else:
	print('no medal for you')