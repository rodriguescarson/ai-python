# def pour(jug1, jug2, step):
#     max1, max2, fill = 3, 10, 2  # Change maximum capacity and final capacity max1<max2
#     print("%d\t%d\t" % (jug1, jug2), end=step+"\n")
#     if jug2 == fill:
#         return
#     elif jug2 == max2:
#         pour(0, jug1, "step 1")
#     elif jug1 != 0 and jug2 == 0:
#         pour(0, jug1, "step 2")
#     elif jug1 < max1:
#         pour(max1, jug2, "step 3")
#     elif jug1 < (max2-jug2):
#         pour(0, (jug1+jug2), "step 4")
#     else:
#         pour(jug1-(max2-jug2), max2, "step 5")


# print("JUG1\tJUG2")
# pour(0, 0, "step 0")
def pour(jug1, jug2):
    max1, max2, fill = 4, 5, 2
    print(jug1, jug2)

    if(jug2 == fill):
        return
    elif(jug2 == max2):
        pour(0, jug1)
    elif(jug1 != 0 and jug2 == 0):
        pour(0, jug1)
    elif(jug1 < max1):
        pour(max1, jug2)
    elif(jug1 < max2-jug2):
        pour(0, jug2+jug1)
    else:
        pour(jug1-(max2-jug2), max2)


pour(0, 0)
