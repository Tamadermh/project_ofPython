
class Game:
    def __init__(self):
        while True:
            print ('''welcom
             we have many game
                 to dvid list to even and odd enter 1
                 to print sentence with out duplicate enter 2
                 to print numbers ending in spcific number enter 3
                 to test how many number devid on second number enter 4
                 to find number can devid on your numbers enter 5
                 ''')

            inp=int(input())

            if inp ==1:
                self.evenorodd()
            elif inp==2:
                self.no_duplicate()
            elif inp==3:
                self.print_numbers()
            elif inp==4:
                self.test_dvied()
            elif inp==5:
                self.test_dvied_both()
            x_or_y=input("to continue enter y or x to exit :")
            if x_or_y=='x':
                print ('thank you , bey bey')
                break
        
                
    def evenorodd(self):
        lists=[]
        length=int(input('enter the size of list: '))
        print('enter the number of list :')
        for n in range(length):
            nu=int(input('numbers of list : '))
            lists.append(nu)
        print(f"the list ={lists}")
        even=[]
        odd=[]
        for num in lists:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        print(f"the even list ={even}")
        print(f"the odd list ={odd}")

    def no_duplicate(self):
        sentence=input("enter the sentence plase\n")
        new_sent=sentence.split(' ')
        s_no=[]
        for word in new_sent:
            if word not in s_no:
                s_no.append(word)
        sentence2=" ".join(s_no)
        leng=len(new_sent)-len(s_no)
        print(f"the sentence with out duplicate :\n {sentence2}")
        print(f"the number of duplicate : {leng}")


    def print_numbers(self):
        number=int(input('enter the number : '))
        number +=1
        for i in range(number):
            print(i)


    def test_dvied(self):
        x=int(input('enter first number : '))
        y=int(input('enter second number : '))
        x+=1
        for i in range(x):
            if i%y==0:
                print(i)

                
    def test_dvied_both(self):
        num1=int(input('enter first number : '))
        num2=int(input('enter second number : '))
        for i in range(101):
            if i%num1==0 and i%num2==0:
                print (i)

               
g =Game()

    

