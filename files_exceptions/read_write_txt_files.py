# Chapter 10: Files and Exceptions

# with open('filepath') as aliasNameForTheFile:
#     line1 = aliasNameForTheFile.readline()
#     line2 = aliasNameForTheFile.readline()
#     line3 = aliasNameForTheFile.readline()
#
#     all_lines = aliasNameForTheFile.readline() # the result will be list of values
#
#     file_content = aliasNameForTheFile.read()
#
#     # aliasNameForTheFile.close() # !! no need to close when you read a fike starting 'WITH' !!!!


filepath = '../data/products.txt'
filepath2 = '../data/sample.txt'
# filepath1 = 'c:/dev/basics/data/products.txt'



print("******************* READ FILE **********************")
with open(filepath) as prod_list:
    contents = prod_list.read()
    print("contents of the file: \n", contents)

with open(filepath) as prod_list:
    print("now we are trying to loop through the contents")
    all_lines = prod_list.readlines()
    print(all_lines)

print('printing the line1:', all_lines[0])

for line in all_lines:
        print(line)

print("******************* WRITE FILE **********************")

print("******************* WRITE FILE appending new content **********************")
with open(filepath, "a") as prod_list:
    prod_list.write('playstation 5\n')
    prod_list.write('learning python book\n')
    prod_list.write('first head to selenium book\n')
    # check the file content

print("******************* WRITE FILE deleting old content **********************")

with open(filepath, "w") as prod_list:
    prod_list.write('spiderman jacket\n')
    prod_list.write('batman mask\n')
    prod_list.write('smart tv samsung 70\n')
    # check the file content



# H/W: 10-3, 10-4,

