t=int(input())
q1=int(input())
q2=int(input())
q3=int(input())

p_price=45
price1=p_price*q1
price2=p_price*q2
price3=p_price*q3
gst=(45*(18/100))
gst_price1=q1*(45*(18/100))
gst_price2=q2*(45*(18/100))
gst_price3=q3*(45*(18/100))
print(price1+gst_price1)
print(price2+gst_price2)
print(price3+gst_price3)