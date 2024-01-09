with open('source.txt') as f:
    lines = f.readlines()

file_obj = open("result.xml", "w")

for line in lines:
    x = line.strip().split("=")
    file_obj.write(f"<entry key=\"{x[0]}\">\n\t<int>{x[1].strip()}</int>\n\t<uat>{x[1].strip()}</uat>\n\t<prod>{x[1].strip()}</prod>\n</entry>\n")

file_obj.close()

# source=source1
# yukarıdaki formatı aşağıdaki hale çeviren script
# <entry key="source">
#     <int>source1</int>
#     <uat>source1</uat>
#     <prod>source1</prod>
# </entry>
     