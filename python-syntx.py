			print("Hello, World!")
			print("Number is ", n)
			print(i,end = ' ')//end tells what to end with after printing,(in this case a space)
			a="Hello",b=60;
			print("%s  %d ,How are ya?" % (a,b) );  





			Taking Input
			n = int(input())
			x, y = map(int,input().split())
			lis = list(map(int,input().split()))




			Data Types
			//Standard DT
			Numbers 
						x=69
			
			String 		
						str = "Hello"
						str = 'Hello'
			
			List
						l  = [0, "arjit", 2]

			Tuple
						t  = (0, "arjit", 2)  
			
			Dictionary
						d = {1:'arjit', 2:'Anik', 3:'Jam', 4:'Milli'};   

			




			Operators
			+,-,*,/,//(Floor Division),%(remainder),**(exponential)
			==,!=,<=,>=,<,>
			&,|,^,~,<<,>>
			Logical - and,or,not
			Membership op- in,not in
			Identify op - is,is not

			


			Control Structure
			if n % 2 == 1:
				print("Weird")
			elif n % 2 == 0 and 2 <= n <= 5:
				print("Not Weird")
			elif n % 2 == 0 and 6 <= n <= 20:
				print("Weird")
			else:
				print("Not Weird")

			//Shorthand
			print("a") if a>b else print("b")


			Looping

			for i in range(0,5):  
				print(i,end = ' ')//Ouput: 0 1 2 3 4 5  


			//if for runs completely then will come to else ...if doesnt run completely wont come to else
			for i in range(0,n):  
				if(condition):
					----  
			else:
				----  
			
			while conditon:
				body


			
			
			Usefull features for looping
			
			break;
			continue;
			pass;//Null operation,does nothing just used when empty block is there

			
			

			Functions

			def is_leap(year):
				return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

			

			Strings 

			//Multiline string
			a = ''' Hello
					Multiline
					String '''

			// strings are arrays
			a = "Hello, World!"
			print(a[1]) //e

			//Slicing
			a[2:5] //llo
			a[-5:-2] //orl
			a[-1::-1] //Reversing(last parameter shows updation) !dlroW ,olleH
			
			
			//Splitting and Joining
			a = "my name is arjit"
			a.split(" ") //['my','name','is','arjit']
			a="-".join(a) //my-name-is-arjit

			//Check a substring in string
			txt = " Rain in Spain"
			x = "ain" in txt
			y = "ain" not in txt

			//String Formatting
			
			//concatenation
			txt = "My name is "+ name
			
			//format()
			x = "{} is {} years old."
			print(x.format("Arjit",18))
		
			//Escape Charachters
			\\' \\t \\n \\b \\ooo \\xhh

			
			//Change an element in String(Cant do str[5]="x" as non mutable)
			//Method 1 : Change to list then to string using join()
			str = "arjit"
			l = list(str) //['a','r','j','i','t']
			l[2] = 'p'//['a','r','p','i','t'] 
			str = ''.join(l) // arpit
			
			//Method 2 : use Slicing
			str = str[:2] + "p" + string[3:] // arpit


			//Other Utility methods
			a.lower(), a.upper(), capitalize(), title(), swapcase() ,a.strip() 
			a.replace("H","J"), count(), find()
			isalpha(),isdigit(),isalnum(),isnumeric()
			





			Lists

			a = ["1",2,3,4]

			//Accesing elements in list
			a[1] // 2
			a[-1] // 4
			a[1:] // 2,3,4

			//Loop through
			for i in a:
				print(i)
			
			for i in range(len(a)):
				print(a[i])

			//Check a item in list
			if "Boy" in a:
				print("Yes")

			//Adding items
			a.append("newItem")
			a.insert(index,"newItem")//Inserts item at specified index

			//Removing items
			a.remove("newItem")
			a.pop() //last item will be removed
			a.pop(3) //item at index 3 will be removed

			//Reversing a list
			a.reverse()

			//Sorting
			a.sort()
			a.sort(reverse = True) //sorts in reverse order

			//Join 2 lists
			l3 = l1 + l2
			l1.extend(l2)


			//Other utility functions
			len(a)
			min(a),max(a)
			a.count(1) // counts frequency of 1 in a


			//List Comprehension
