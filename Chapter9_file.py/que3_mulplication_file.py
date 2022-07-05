for j in range(2,21):
    with open(f"Tables/multipication_table_of_{j}.txt","w") as f:
        f.write("multiplication table of "+ str(j)+"\n\n")
        for i in range(1,11):
            f.write(str(str(j)+ "x"+str(i)+"="+str(j*i)))
            if i!=10:
                f.write("\n")
print("success")




