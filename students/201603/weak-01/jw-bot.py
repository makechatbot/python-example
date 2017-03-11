def chatbot(request):
   if request.count("안녕") > 0:
       print("봇 : 안녕하세요!!!")
   elif request.lower() == "hi":
       print("봇 : HI~!!!")
   else:
       print("봇 : 몰라!!!")


X = ""

while  X != "end":
   sInput = input("나 : ")

   if sInput == "/end":
       X = "end"
   else:
       chatbot(sInput)
