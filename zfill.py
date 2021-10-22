class FillText:

   @classmethod
   def my_fill(cls, txt: str, length: int, direction: str):

       """An Implementation for xfill() python method
          It'll add 0 to left or right depending on your third argument
          For example
          
          print(FillText.my_fill("hello", 8, "right")) 
          output: hello000
    
          print(FillText.my_fill("hello", 8, "left"))
          output: 000hello
       """

       direction = direction.lower()
       zeros = '0' * (length - len(txt))
 
       directions = {
         "right": txt + zeros,
         "left": zeros + txt
       }
       if direction in directions:
           return directions[direction]
       else:
           return "Valid Options are: right, left"


test = [FillText.my_fill(str(i), 3, "left") for i in range(10)]

print(test) # ['000', '001', '002', '003', '004', '005', '006', '007', '008', '009']

print(FillText.my_fill("1", 3, "right")) # 100
