while 5>0:
    p = int(input('marks of english = '))
    q = int(input('marks of Nepali = '))
    r = int(input('marks of Account = '))
    s = int(input('marks of Economics = '))
    t = int(input('marks of Computer science = '))
    a = p+q+r+s+t
    if(150<=a<=200):
        print('Passed in individual Subjects')
    print('Total = ',a)
    #b= 'total full marks'/100 
    b= 500/100
    percent = a / b
    print('Percentage =',percent,'%')
    if(((p >= 40)and(q >= 40)and(r >= 40)and(s >= 40)and(t >= 40))or((p >= 30)and(q >= 30)and(r >= 30)and(s >= 30)and(t >= 30)and(a>=150))):
        print('Remarks: ','Congratulations! Bro, You have successfylly passed the exam.')
    else:
        print('Remarks:','Sorry Bro! Your symbol Number is not in list.You are supposed to give equal emphasis for all the subjects.')