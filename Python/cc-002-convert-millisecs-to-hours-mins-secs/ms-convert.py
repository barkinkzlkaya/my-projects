print('''
    ###  This program converts milliseconds into hours, minutes, and seconds ###
    (To exit the program, please type "exit")
    ''')  

while True:
    ms = input('Please enter the milliseconds (should be greater than zero) : ')
    if (ms.lower()) == 'exit':
        print ('"Exiting the program... Good Bye"')
        exit()
    else :
        
        try:
            ms = int(ms)
            
        
                
                
        except ValueError:
            print ('"Not Valid Input !!!"')
            continue 
        if ms < 1:
                
                print('"Not Valid Input !!!"')
                
        else :

            def convert(ms):
                hr=ms//3600000
                minute=(ms%3600000)//60000
                sec=(ms%60000)//1000
                
                if hr > 0:
                    h=f'{hr} hour/s'
                else :
                    h=''
                        
                if minute > 0:
                    m=f'{minute} minute/s'
                else :
                    m=''
                    
                if sec > 0:
                    s=f'{sec} second/s'        
                else :
                    s=''
                if sec < 1 and ms < 1000 :  
                    ms = f'just {ms} millisecond/s'     
                else :
                    ms = ''
                
                return h + ' ' + m + ' ' + s + ' ' + ms      
                        
                
            print(convert(ms))



            
        
       
                          