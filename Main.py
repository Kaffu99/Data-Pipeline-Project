import csv
with open("expenses.txt", "r") as file:
    List_of_Prices=[]
    List_of_Error_id=[]
    Missing_Prices=[]
    Negative_product_price=[]
    List_of_The_Filtered_Data=[]

    for line in file:
            try:
                line=line.strip()
                product_details=line.split(",")
                Length_of_the_Data=len(product_details)
                if Length_of_the_Data==3:
                    ID=int(product_details[0])
                    product_name=product_details[1].strip()
                    if product_name=='' or product_name==None :
                        List_of_Error_id.append(ID)
                        continue



                    product_price=(product_details[2])
                    if product_details[2]=='' :
                            Missing_Prices.append(ID)
                            continue
                    try:
                        product_prices=int(product_price)
                        if product_prices<0:
                            Negative_product_price.append([ID,product_price])
                            continue
                    except(ValueError):
                        Missing_Prices.append(ID)
                        continue
                    else:
                        product_prices=int(product_price)


                    print(f"{product_name} : {product_price}")
                    List_of_Prices.append(product_prices)


                    List_of_The_Filtered_Data.append([ID,product_name,product_prices])



                else:
                    print("Something is Missing Must be the Price or Name of The Product")
                    continue



            except(ValueError):
                print(f"Invalid Input: {product_name}")



    Sum=sum(List_of_Prices)
    print("*** This are The Sum of Prices ***")
    print(f"Sum of Prices: {Sum}\n")

    print("*** This are The List of Prices ***")
    print(f"List of prices: {List_of_Prices}\n")

    print("*** This are The Id Where Product Name are Missing ***")
    print(f"{List_of_Error_id}\n")

    print("*** This are The Id Where Product Prices are Missing ***")
    print(f"{Missing_Prices}\n")

    print("*** Negative Product Prices")
    print(f"{Negative_product_price}\n")

    print("*** This are The Filtered Data ***")
    print(List_of_The_Filtered_Data)



with open("Filtered_data.csv",mode="w",newline="",encoding="utf-8") as file:
     writer=csv.writer(file)
     writer.writerow(["ID","Product_name","Product_Price"])
     for Data in List_of_The_Filtered_Data:
        writer.writerow(Data)

with open("Negative_product_prices.csv","w",newline="") as file:
     writer=csv.writer(file)
     writer.writerow(["ID","Product_Price"])
     for Datas in Negative_product_price:
        writer.writerow(Datas)
