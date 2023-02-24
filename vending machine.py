class Some:

    def name (self):

        import playsound as ps
        import pyttsx3
        engine = pyttsx3.init()


        print("WELCOME TO VENDING MACHINE 250")
        engine.say("WELCOME TO VENDING MACHINE")
        engine.runAndWait()

        # taking mioney from the user
        engine.say("enter the number of tens you want to insert")
        engine.runAndWait()
        while (True):
            try:
                Money_tens = int(input("Enter the number of ten's you want to insert : "))
                if (Money_tens >= 0):
                    break
                while (Money_tens <= 0):
                    Money_tens = int(input("please enter the right amount :"))
                    engine.say("please enter the amount greater than zero ")
                    engine.runAndWait()
                    break
            except:
                print("Enter the money is int format")
                engine.say("please enter in correct format ")
                engine.runAndWait()
        engine.say("enter the number of twentys you want to insert")
        engine.runAndWait()
        while (True):
            try:
                Money_twentys = int(input("Enter the number of twenty's you want to insert : "))
                if (Money_twentys >= 0):
                    break
                while (Money_twentys < 0):
                    Money_twentys = int(input("please enter the right amount :"))
                    engine.say("please enter the amount greater than zero ")
                    engine.runAndWait()
                    break
            except:
                print("Enter the money is int format")
                engine.say("please enter in correct format ")
                engine.runAndWait()
        engine.say("enter the number of fiftys you want to insert")
        engine.runAndWait()
        while (True):
            try:
                Money_fiftys = int(input("Enter the number of fifty's you want to insert : "))
                if (Money_fiftys >= 0):
                    break
                while (Money_fiftys < 0):
                    Money_fiftys = int(input("please enter the right amount :"))
                    engine.say("please enter the amount greater than zero ")
                    engine.runAndWait()
                    break
            except:
                print("Enter the money is int format")
                engine.say("please enter in correct format ")
                engine.runAndWait()

        engine.say("enter the number of hundreds you want to insert")
        engine.runAndWait()
        while (True):
            try:
                Money_hundred = int(input("Enter the nummber of hundred's you want to insert : "))
                if (Money_hundred >= 0):
                    break
                while (Money_hundred < 0):
                    Money_hundred = int(input("please enter the amount greater than zero :"))
                    engine.say("please enter in correct format ")
                    engine.runAndWait()
                    break
            except:
                print("Enter the money is int format")
                engine.say("please enter in correct format ")
                engine.runAndWait()
        # Dispaying the total amount
        print("10  : ", Money_tens, "\n20  : ", Money_twentys, "\n50  : ", Money_fiftys, "\n100 : ", Money_hundred)
        Total_amount = Money_tens * 10 + Money_twentys * 20 + Money_fiftys * 50 + Money_hundred * 100
        print("The amount you had instred in the vending machine : ", Total_amount, "₹ only")

        # showing the list avl
        print("These are the itmes available")
        Pro1_name, pro1_price = "Fanta 200-ml", 20
        Pro2_name, pro2_price = "Maza 200-ml", 20
        Pro3_name, pro3_price = "Coke 200-ml", 20
        Pro4_name, pro4_price = "Tumbs-up 200-ml", 20
        print(Pro1_name, pro1_price)
        print(Pro2_name, pro2_price)
        print(Pro3_name, pro3_price)
        print(Pro4_name, pro4_price)
        F_pro = 0
        M_pro = 0
        C_pro = 0
        T_pro = 0
        # if your choose fanta
        while (True):
            # giving choice to user
            engine.say("select of your choice      press n if you want to exit")
            engine.runAndWait()
            Choice_user = (input("Choose of your choice (If you want to exit press n): "))
            if Choice_user == "fanta" and Total_amount >= pro1_price:
                print("You had choosed fanta")
                Total_amount = Total_amount - pro1_price
                print("This is you total balance : ", Total_amount)
                F_pro = F_pro + 1
                engine.say("fanta")
                engine.runAndWait()


            elif Choice_user == "maza" and Total_amount >= pro2_price:
                print("You had chossed Maza")
                Total_amount = Total_amount - pro2_price
                print("This is you total balance : ", Total_amount)
                M_pro = M_pro + 1
                engine.say("maza")
                engine.runAndWait()
            elif Choice_user == "coke" and Total_amount >= pro3_price:
                print("you had choosed coke")
                Total_amount = Total_amount - pro3_price
                print("This is you total balance : ", Total_amount)
                C_pro = C_pro + 1
                engine.say("coke")
                engine.runAndWait()
            elif Choice_user == "tumbsup" and Total_amount >= pro4_price:
                print("you had choosed Tumbsup")
                Total_amount = Total_amount - pro4_price
                print("This is you total balance : ", Total_amount)
                T_pro = T_pro + 1
                engine.say("tumbsup0")
                engine.runAndWait()

            elif Choice_user == "n":

                ps.playsound("C:\\Users\\NAGAR\Downloads\\salamisound-8930906-big-ratchet-half-turn.mp3")

                print("==================================")
                print("no of itmes you had perchased :")
                print(Pro1_name, "    : ", F_pro)
                print(Pro2_name, "     : ", M_pro)
                print(Pro3_name, "     : ", C_pro)
                print(Pro4_name, " : ", T_pro)
                print("==================================")
                print("Your total balance is ", Total_amount)
                engine.say("your total balance is")
                engine.runAndWait()
                print("==================================")

                engine.say("thank you")
                engine.runAndWait()
                break

            else:
                ps.playsound("C:\\Users\\NAGAR\Downloads\\salamisound-8930906-big-ratchet-half-turn.mp3")
                print("==================================")
                print("Insufficient balance balance")
                engine.say("sorry you your total balance is zero ")
                engine.runAndWait()
                print("==================================")
                print("no of itmes you had perchased :")
                print(Pro1_name, "    : ", F_pro)
                print(Pro2_name, "     : ", M_pro)
                print(Pro3_name, "     : ", C_pro)
                print(Pro4_name, " : ", T_pro)
                print("==================================")
                print("Your total balance is ", Total_amount)
                engine.say("your total balance is")
                print("==================================")

                engine.say("thank you")
                engine.runAndWait()

                break


p1=Some()
p1.name()



