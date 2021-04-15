def test():
    income_self = eval(input("Please enter yourself income:"))
    income_spouse = eval(input("Please enter your spouse income:"))
    
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
    elif standard_tax_self > tax_self:
        separate_tax_self= tax_self
        
    # chose standard or progressive for your spouse
    if standard_tax_spouse < tax_spouse :
        separate_tax_spouse= standard_tax_spouse
    elif standard_tax_spouse > tax_spouse:
        separate_tax_spouse= tax_spouse
    
    #total tax
    total_separate_assessment = separate_tax_self + separate_tax_spouse
    
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

    #standard tax of join
    standard_tax_join = ((total_income - total_MPF) * .15)
    
    #compare standard and progressive
    if standard_tax_join > tax_join:
        Under_Joint_Assessment = tax_join
    elif standard_tax_join < tax_join:
        Under_Joint_Assessment = standard_tax_join
    
    #compare two tax calculation
    if total_separate_assessment < Under_Joint_Assessment:
        return int(total_separate_assessment)
    elif total_separate_assessment > Under_Joint_Assessment:
        return int(Under_Joint_Assessment)