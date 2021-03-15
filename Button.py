from autotrade import*
from tkinter import*

window = Tk()

#현재 보유하고 있는 주식을 전체 매도한 후 프로그램 종료
b1 = Button(window, text="전체 매도", command=sell_all)
b1.pack()

#slack으로 현재 주식 매입상황을 전송
b2 = Button(window, text="현재 매입상황", command=get_stock_balance(ALL))
b2.pack()

window.mainloop()
