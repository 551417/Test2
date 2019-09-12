def safe_pawns(pawns: set) -> int:
   count=0
   temp=0
   ls=list(pawns)
   move=ls[count]
   print(move[1])
   while count<len(pawns):
       move=ls[count]
       var1=move[0]
       var2=move[1]
       if var2==1:
           print("Not a valid location of pawn")
       elif var1.isalpha():
           nextchar=chr(ord(var1)+1)
           print("next char is ",nextchar)
           nextval=int(var2)-int(1)
           print("next val is ",nextval)
           finalnext=str(nextchar)+str(nextval)
           print("finalnext",finalnext)
           previourschar=chr(ord(var1)-1)
           print("previous char is ",previourschar)
           prevval=int(var2)-int(1)
           print("previous value is ",prevval)
           finalprevval=str(previourschar)+str(prevval)
           print("previous value:" ,finalprevval)
           if(finalnext in ls or finalprevval in ls):
               temp+=1
       else:
            print("Not present")
       count+=1

   print("temp is:",temp)

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})


    
   




#    while count<len(pawns):

#        move=ls[count]
#        var1=move[0]
#        var2=move[1]

#        if var2==1:
#            print("Not a valid location of pawn")
#        elif str(var1.ischar()):
#              nextchar=chr(ord(ch))+1
#              nextval=var2+1
#              finalnext=str(nextchar)+str(nextval)
#              previourschar=char(ord(ch))+1
#              prevval=var2-1
#              finalprevval=str(previourschar)+str(prevval)
#              if(finalnext in ls or finalprevval in ls):
#                  temp+=1
#        else:
#             print("Not present")
#     count+=1