
## With using 're' librery

#import re

#with open("catch_me.txt", 'r') as f:

#    for line in f:
#        list_ = re.findall("catch me", str(line))
#        if list_ != []:
#            print(len(list_))
#        else:
#            continue


# --------------------------------------------------------------------
# Without using 're' librery

with open("catch_me.txt", 'r') as f:
    list_ = []
    for line in f:
        while True:
            try:

                ## will catch string even it is uppercase
                # pos = line.lower().index("catch me")
                
                pos = line.index("catch me")
                
                list_.append(line[pos:pos+8])
                line = line[:pos] + line[pos+8:]
                
            except ValueError:
                break
            except Exception as err:
                raise err

    print(len(list_))


