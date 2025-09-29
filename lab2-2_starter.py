# lab2-2_starter.py

LOGFILE = "sample_auth_small.log"  # change filename if needed
List_ips=[]
count=0
Unique_list_ips=[]

def simple_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            List_ips.append(port.strip()) 
           
                        # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":

    with open(LOGFILE, "r") as f:
        for line in f:
            (simple_parser(line.strip()))
            count+=1
    Unique_list_ips=set(List_ips) #This is turn them into a list of the same element.
    sorted_list= sorted(Unique_list_ips)
    print("Lines Read is= ", count)
    print("The Unique Ips= ", len(Unique_list_ips))
    print(sorted_list[0:10])
    