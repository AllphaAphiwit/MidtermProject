import tkinter
def save(event): 
    n = button_name.get()
    t = button_tel.get()
    datauser = open("D:\\user.txt","w")
    datauser.write("%s:%s"%(n,t))
    gui.quit()
def ui(): #การจัดารหน้าล็อกอิน
    global button_name
    global button_tel
    global gui
    gui = tkinter.Tk()
    gui.geometry("350x240")
    gui.option_add("*Font","consolas 14")
    gui.title("LOGIN")
    title = tkinter.Label(text = "LOGIN",font = "consolas 40 bold")
    title.grid(row = 0,column = 3)
    #title.pack()
    title_name = tkinter.Label(text = "NAME")
    title_name.grid(row = 1,column = 2)
    button_name = tkinter.Entry(width = 25)
    button_name.grid(row = 1,column = 3)
    #button_name.pack()
    title_tel = tkinter.Label(text = "\nTEL\n")
    title_tel.grid(row = 2,column = 2)
    button_tel = tkinter.Entry(width = 25)
    button_tel.grid(row = 2,column = 3)
    #button_tel.pack()
    button_save = tkinter.Button(text = "Submit")
    button_save.grid(row = 3,column = 3)
    button_save.bind("<Button-1>",save)
    #button_save.pack()
    gui.mainloop()
def start_menu(): #เมนูหลัก
    global choice
    print("\n{0:=<120}\n{1:<50}{2:}\n{3:<57}{4:}\n{5:<57}{6:}\n{7:<57}{8:}\n{9:=<120}".format("","","MENU : (1) Select-Menu","","(2) Cancle-Order","","(3) Confirm-Order","","(4) Exit Program",""))
    choice = str(input("\t\t\t\t\t\t  Please Select Menu : "))
def start_menu1(re): #เมนูรอง
    while True:
        print("\n{0:=<120}\n{1:<50}{2:<5}{3:}".format("","","Menu :"," (r) Repeat"))
        print("{0:<57}{1:}\n{2:=<120}".format("","(e) Exit",""))
        re = input("\t\t\t\t\t\t  Please Select Menu : ")   
        if re == "r" or re == "e":
            break
        else: 
            print("\n\t\t\t\t!!!!! Please select menu |(r)Repeat or (e)Exit !!!!!\n")
    return re
def show_order():#โชว์รายการอาหารและออเดอร์และราคา
    print("\n{0:-<120}\n{1:<14}{2:<30}{3:<15}{4:<13}{5:<16}{6:<19}{7:}\n{8:-<120}".format("","NO.","MENU NAME","NORMAL(n)","EXTRA(e)","ORDER(NORMAL)","ORDER(EXTRA)","TOTAL",""))
    print("{0:<45}{1:<15}{2:<17}{3:<16}{4:<16}{5:<6}{6:}".format("[1] Steamed Chicken with Rice","40 Baht","45 Baht",order_n[0],order_e[0],total[0],"Baht"))
    print("{0:<45}{1:<15}{2:<17}{3:<16}{4:<16}{5:<6}{6:}".format("[2] Roasted Duck on Rice","50 Baht","55 Baht",order_n[1],order_e[1],total[1],"Baht"))
    print("{0:<45}{1:<15}{2:<17}{3:<16}{4:<16}{5:<6}{6:}".format("[3] Barbecued Red Pork in Sauce with Rice","65 Baht","70 Baht",order_n[2],order_e[2],total[2],"Baht"))
    print("{0:<45}{1:<15}{2:<17}{3:<16}{4:<16}{5:<6}{6:}".format("[4] Rice Crispy Pork","40 Baht","45 Baht",order_n[3],order_e[3],total[3],"Baht"))
    print("{0:<45}{1:<15}{2:<17}{3:<16}{4:<16}{5:<6}{6:}\n{7:-<120}".format("[5] Charcoal-Boiled Pork Neck","40 Bath","45 Baht",order_n[4],order_e[4],total[4],"Baht",""))
def cal_price(): #คำนวณออเดอร์
    if (menu >= 1 and menu <= 5) and (select == "n" or select == "normal") and (num > 0):
        if choice == "1":
            if order_n[menu-1] >= 0:
                order_n[menu-1] += num
                total[menu-1] += price[menu-1]*num
        elif choice == "2":
            if order_n[menu-1] == 0:
                order_n[menu-1] -= order_n[menu-1]
                total[menu-1] = price[menu-1]*order_n[menu-1]
            elif order_n[menu-1] > 0:
                if order_n[menu-1] > num:
                    order_n[menu-1] -= num
                    total[menu-1] -= price[menu-1]*num
                elif order_n[menu-1] <= num:
                    total[menu-1] -= (price[menu-1])*order_n[menu-1]
                    order_n[menu-1] -= order_n[menu-1]
    elif (menu >= 1 and menu <= 5) and (select == "e" or select == "extra") and (num > 0):
        if choice == "1":
            if order_e[menu-1] >= 0:
                order_e[menu-1] += num
                total[menu-1] += (price[menu-1]+5)*num
        elif choice == "2":
            if order_e[menu-1] == 0:
                order_e[menu-1] -= order_e[menu-1]
                total[menu-1] = (price[menu-1]+5)*order_e[menu-1]
            elif order_e[menu-1] > 0:
                if order_e[menu-1] > num:
                    order_e[menu-1] -= num
                    total[menu-1] -= (price[menu-1]+5)*num
                elif order_e[menu-1] <= num:
                    total[menu-1] -= (price[menu-1]+5)*order_e[menu-1]
                    order_e[menu-1] -= order_e[menu-1]              
    else:
        print("\n{0:!<56}{1:}{2:!<56}\n".format(""," ERROR. ",""))
order_e,order_n,total,price,count,ans = [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[40,50,65,45,40],0,""
print("\n\t\t\t\t\t >>>> Welcome to High-tech Restaurant <<<<")
ui()
while True:
    data_all = open("D:\\Data.txt","r")
    txt = data_all.read()
    data = txt.split(",")
    count = int(len(data))-1
    start_menu()
    if choice == "1":
        while True:
            try:
                alltotal = total[0]+total[1]+total[2]+total[3]+total[4]
                show_order()
                print("{0:<93}{1:<16}{2:<6}{3:}\n{4:-<120}".format("","TOTAL PRICE",alltotal,"Baht",""))
                print("\nAdd Menu >> NO.(1)(2)(3)(4)(5) - ORDER - NORMAL(n) or EXTRA(e)")
                menu,num,select = input("Add Menu >> ").split("-")
                num = int(num)
                menu = int(menu)
                cal_price()   
                alltotal = total[0]+total[1]+total[2]+total[3]+total[4] 
                show_order()
                print("{0:<93}{1:<16}{2:<6}{3:}\n{4:-<120}".format("","TOTAL PRICE",alltotal,"Baht",""))
                break
            except ValueError:
                print("\n{0:!<49}{1:}{2:!<49}\n".format(""," Please input 3 data. ",""))
    elif choice == "2":
        while True:
            try:
                alltotal = total[0]+total[1]+total[2]+total[3]+total[4]
                show_order()
                print("{0:<93}{1:<16}{2:<6}{3:}\n{4:-<120}".format("","TOTAL PRICE",alltotal,"Baht",""))
                print("\nCancle Menu >> NO.(1)(2)(3)(4)(5) - ORDER - NORMAL(n) or EXTRA(e)")
                menu,num,select = input("Cancel Menu >> ").split("-")
                num = int(num)
                menu = int(menu)
                cal_price()
                alltotal = total[0]+total[1]+total[2]+total[3]+total[4]
                show_order()
                print("{0:<93}{1:<16}{2:<6}{3:}\n{4:-<120}".format("","TOTAL PRICE",alltotal,"Baht",""))
                break
            except ValueError:
                print("\n{0:!<49}{1:}{2:!<49}\n".format(""," Please input 3 data. ",""))
    elif choice == "3": 
        count += 1      
        show_order()
        alltotal = total[0] + total[1] + total[2] + total[3] + total[4]
        allorder_n = order_n[0] + order_n[1] + order_n[2] + order_n[3] + order_n[4]
        allorder_e = order_e[0] + order_e[1] + order_e[2] + order_e[3] + order_e[4]
        allorder = allorder_n + allorder_e #การรวมออเดอร์
        datauser = open("D:\\user.txt","r")
        data = datauser.read()
        name,tel = data.split(":")
        data_all = open("D:\\Data.txt","a")
        data_all.write("[%d] %s %s : %s %s : %s %s %s : %s %s %s,\n"%(count,"NAME",name,"TEL.",tel,"AMOUNT",allorder,"order","TOTAL PRICE",alltotal,"Baht"))
        print("NAME: {0:<25}{1:<1}{2:<25}{3:<8}{4:<4}{5:<22}{6:<15}{7:<6}{8:}\n{9:-<120}".format(name,"TEL.",tel,"AMOUNT:",allorder,"order","TOTAL PRICE",alltotal,"Baht",""))
        ans = start_menu1(ans)
        if ans == "r":
            print("\n\t\t\t\t\t >>>> Welcome to High-tech Restaurant <<<<")
            ui()
            order_e,order_n,total,price,b = [0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[40,50,65,45,40],0
        elif ans == "e":
            print("\n\n\n\n\n\t\t\t\t\t\t   >>>>> Thank you <<<<<")
            break
    elif choice == "4":
        print("\n\n\n\n\n\t\t\t\t\t\t   >>>>> Thank you <<<<<")
        break
    else:
        print("\n{0:!<56}{1:}{2:!<56}\n".format(""," ERROR. ",""))