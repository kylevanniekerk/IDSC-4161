def assign_grade(exam, lab, quiz, challenge, presentation, assesment):
    gradetot = int(exam + lab + quiz + challenge + presentation + assesment)
    if exam <= 250 and quiz <= 240 and lab <= 240 and challenge <= 120 and presentation <= 100 and assesment <= 50: 
        if gradetot >= 930:
            letgrade = 'A'
            
        elif gradetot >= 900 and gradetot < 930:
            letgrade = 'A-'
            
        elif gradetot >= 870 and gradetot < 900:
            letgrade = 'B+'
        
        elif gradetot >= 830 and gradetot < 870:
            letgrade = 'B'
            
        elif gradetot >= 800 and gradetot < 830:
            letgrade = 'B-'
            
        elif gradetot >= 770 and gradetot < 800:
            letgrade = 'C+'
            
        elif gradetot >= 730 and gradetot < 770:
            letgrade = 'C'
            
        elif gradetot >= 700 and gradetot < 730:
            letgrade = 'C-'
        
        elif gradetot >= 670 and gradetot < 700:
            letgrade = 'D+'
            
        elif gradetot >= 600 and gradetot < 670:
            letgrade = 'D'
            
        elif gradetot <= 599:
            letgrade = 'F'
    else:
        letgrade = 'NR'
        
    return letgrade

print('{0}'.format(assign_grade(260,238,230,112,99,45)))
        
    

