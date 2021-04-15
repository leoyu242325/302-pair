def test():
    income = eval(input("Please enter your income:"))
    if income < 0:
        print("Wrong income, incoem must be a positive number.")
    elif income >= 0:
        #calculat MPF
        MPF = (income * .05)
        if MPF > 18000:
            MPF = 18000 
        
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

        
        else:
            #enter wrong number 
            print("Please enter a valid income of more than $0")
            
        #standard
        standard_tax = ((income - MPF) * .15)

        #compare standard and progressive
        if standard_tax > tax:
            return int(tax)
        elif standard_tax < tax:
            return int(standard_tax)
    else:
        print("Wrong income, incoem must be a positive number.")
