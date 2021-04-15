def main():
    #to see is married or not
    tax_type = input("Married enter 1, Single/Separated/Divorced/Widowed enter 2 :")
    
    #not married
    if tax_type == "2":
        while True:
            try:
                income = eval(input("Please enter your income:"))
                if income < 0:
                    print("Your input value is invalid!")
                elif income >= 0:
                    print("--------------------------------------")
                    #calculat MPF
                    MPF = (income * .05)
                    if MPF > 18000:
                        MPF = 18000 
                    print("Your MPF is", MPF)
                    print("---------------")
                    
                    Less_basic_allowance = 132000
                    
                    #calculat MPF net income after allowance adn MPF
                    net_chargeable_income = (income - Less_basic_allowance - MPF)
                    if net_chargeable_income <= 0:
                        net_chargeable_income =0
                    
                    tax = 0.0
                    #Progressive
                    if income >=0:
                         
                        if net_chargeable_income >= 200000 :  
                            tax = ((net_chargeable_income - 200000) * 0.17)+(16000)
                        # 4th levl
                        elif net_chargeable_income >= 150000 :
                            tax = ((net_chargeable_income - 150000) * 0.14) +(9000)
                        # 3rd levle 
                        elif net_chargeable_income >= 100000 :
                            tax = ((net_chargeable_income - 100000) * 0.10) +(4000)
                        # 2nd levl  
                        elif net_chargeable_income >= 50000 :
                            tax = ((net_chargeable_income - 50000) * 0.06) +(1000)
                        # first levle   
                        else:
                            tax = (net_chargeable_income * .02)
                        
                        print("Total progressive tax payable : $",'%.2f'%tax)
                    
                    else:
                        #enter wrong number 
                        print("Please enter a valid income of more than $0")
                        
                    #standard
                    standard_tax = ((income - MPF) * .15)
                    print("Total standard tax payable : $",'%.2f'% standard_tax)
                    
                    print("---------------")
                    #compare standard and progressive
                    if standard_tax > tax:
                        print("Progressive tax rate is better.")
                        print("You should pay : $",'%.2f'% tax)
                    elif standard_tax < tax:
                        print("Standard tax rate is better.")
                        print("You should pay : $",'%.2f'% standard_tax)
                
                else:
                    print("Wrong income, incoem must be a positive number.")
                    
            except NameError:
                print("Wrong enter, please enter integer!")
    # married 
    elif tax_type == "1":
        while True:
            try:
                income_self = eval(input("Please enter yourself income:"))
                income_spouse = eval(input("Please enter your spouse income:"))
                
                if income_self < 0 or income_spouse <0:
                    print("Your input value is invalid!")
                
                elif income_self >=0 & income_spouse >= 0:
                    #calculat MPF of self
                    MPF_self = (income_self * .05)
                    if MPF_self > 18000:
                        MPF_self = 18000 
                    
                    
                    #calculat MPF of spouse
                    MPF_spouse = (income_spouse * .05)
                    if MPF_spouse > 18000:
                        MPF_spouse = 18000 
                    
                        
                    total_MPF = MPF_self + MPF_spouse
                    
                    Less_basic_allowance = 132000
                    
                    # net income of self after allowance and MPF
                    net_chargeable_income_self = (income_self - Less_basic_allowance - MPF_self)
                    if net_chargeable_income_self <= 0:
                        net_chargeable_income_self =0
                       
                    # net income of spouse after allowance and MPF 
                    net_chargeable_income_spouse = (income_spouse - Less_basic_allowance - MPF_spouse)
                    if net_chargeable_income_spouse <= 0:
                        net_chargeable_income_spouse =0
                    
                    tax_self = 0.0
                    tax_spouse = 0.0
                    tax_join = 0.0
                    
                    print("--------------------------------------")
                    print("Under separate assessment")
                    #under separate taxation
                    
                    print("Your MPF is : $", MPF_self)
                    print("Your spouse MPF is : $", MPF_spouse)
                    print("---------------")
                    
                    # Progressive tax of self
                    if income_self >=0:
                        #remained
                        if net_chargeable_income_self > 200000 :  
                            tax_self = ((net_chargeable_income_self - 200000) * 0.17)+(16000)
                        # 4th levl
                        elif net_chargeable_income_self > 150000 :                    
                            tax_self = ((net_chargeable_income_self - 150000) * 0.14) +(9000)
                        # 3rdt levl     
                        elif net_chargeable_income_self > 100000 :
                            tax_self = ((net_chargeable_income_self - 100000) * 0.10) +(4000)
                        # 2nd levle       
                        elif net_chargeable_income_self > 50000 :
                            tax_self = ((net_chargeable_income_self - 50000) * 0.06) +(1000)
                        # first levle        
                        else:
                            tax_self = (net_chargeable_income_self * .02)
                            
                    else:
                        #enter wrong number
                        print("Please enter a valid self income of more than $0")
                    
                    #Progressive tax of spouse
                    if income_spouse >=0:
                        #remained
                        if net_chargeable_income_spouse > 200000 :  
                            tax_spouse = ((net_chargeable_income_spouse - 200000) * 0.17)+(16000)
                        # 4th levl
                        elif net_chargeable_income_spouse > 150000 :                    
                            tax_spouse = ((net_chargeable_income_spouse - 150000) * 0.14) +(9000)
                        # 3rdt levl    
                        elif net_chargeable_income_spouse > 100000 :
                            tax_spouse = ((net_chargeable_income_spouse - 100000) * 0.10) +(4000)
                        # 2nd levl   
                        elif net_chargeable_income_spouse > 50000 :
                            tax_spouse = ((net_chargeable_income_spouse - 50000) * 0.06) +(1000)
                        # first levl          
                        else:
                            tax_spouse = (net_chargeable_income_spouse * .02)
                            
                    else:
                        #enter wrong number
                        print("Please enter a valid spouse income of more than $0")
            
                    #standard tax of self
                    standard_tax_self = ((income_self - MPF_self) * .15)
                    
                    #standard tax of spouse
                    standard_tax_spouse = ((income_spouse - MPF_spouse)* .15)
                    
                    # chose standard or progressive for you
                    if standard_tax_self < tax_self:
                        separate_tax_self= standard_tax_self
                        print("Standard tax payable is lower for you")
                    elif standard_tax_self > tax_self:
                        separate_tax_self= tax_self
                        print("Progressive tax payable is lower for you")
                    print("The tax payable of you is : $", '%.2f'% separate_tax_self)
                        
                    # chose standard or progressive for your spouse
                    if standard_tax_spouse < tax_spouse :
                        separate_tax_spouse= standard_tax_spouse
                        print("Standard tax payable is lower for your spouse")
                    elif standard_tax_spouse > tax_spouse:
                        separate_tax_spouse= tax_spouse
                        print("Progressive tax payable is lower for your spouse")
                    print("The tax payable of your spouse is : $", '%.2f'% separate_tax_spouse)
                    
                    #total tax
                    print("----------------")
                    total_separate_assessment = separate_tax_self + separate_tax_spouse
                    print("Total tax : $", '%.2f'% total_separate_assessment)
                    
                    #under join assessment
                    total_income = income_self + income_spouse
                    
                    total_net_income = total_income - MPF_self - MPF_spouse - (Less_basic_allowance * 2)
                    
                    #remained
                    if total_net_income >= 200000:
                        tax_join = ((total_net_income - 200000) * 0.17)+(16000)
                    # 4th levl
                    elif total_net_income >= 150000:
                        tax_join = ((total_net_income - 150000) * 0.14)+(9000)
                    # 3rdt levl
                    elif total_net_income >= 100000:
                        tax_join = ((total_net_income - 100000) * 0.10)+(4000)
                    # 2nd levl
                    elif total_net_income >= 50000:
                        tax_join = ((total_net_income - 50000) * 0.06)+(1000)
                    # first levl 
                    elif total_net_income >= 0:
                        tax_join = (total_net_income * 0.02)
                    
                    else:
                        tax_join = 0
                    
                    print("--------------------------------------")
                    print("Under join assessment")
                    print("Total MPF is : $", total_MPF)
                    
                    #standard tax of join
                    standard_tax_join = ((total_income - total_MPF) * .15)
                    
                    #compare standard and progressive
                    if standard_tax_join > tax_join:
                        print("Progressive tax rate is lower.")
                        Under_Joint_Assessment = tax_join
                    elif standard_tax_join < tax_join:
                        print("Standard tax rate is lower.")
                        Under_Joint_Assessment = standard_tax_join
                    print("Total tax : $", '%.2f'% Under_Joint_Assessment)
                    
                    print("--------------------------------------")
                    #compare two tax calculation
                    if total_separate_assessment < Under_Joint_Assessment:
                        print("Under Separate Taxation is better.")
                        print("You and your spouse should pay : $",'%.2f'% total_separate_assessment)
                    elif total_separate_assessment > Under_Joint_Assessment:
                        print("Under join assessment is better.")
                        print("You and your spouse should pay : $",'%.2f'% Under_Joint_Assessment)
                    else:
                        print("Two tax payable is the same, you can choose either one of them.")
            except NameError:
                print("Wrong enter, please enter integer!")   
        else:
            print("Wrong income, incoem must be a positive number.")
          
    else:
        print("Wrong or empty entry")
        main()
    
    print("--------------------------------------")
    again=input("Do you want to try again?(Y/N)")
    
    if again == "Y":
        main()
    else:
        pass

main()
        