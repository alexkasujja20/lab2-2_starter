# Lab2-2 COunt failed login attempts prt Ip.
LOGFILE = "sample_auth_small.log" 
from collections import defaultdict # change filename if needed
List_ips=[]
lines_read =0
Unique_list_ips=[]

counts = defaultdict(int) 

def ip_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            ip= parts[anchor+1]          # the port value will be next token, anchor+1
            return ip.strip()
           
                        # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":

    with open("sample_auth_small.log") as f:
        for line in f:
            if "Failed password" in line or "Invalid user" in line:
            # extract ip
                ip = ip_parser(line)
                if ip:
                    counts[ip] += 1
    print(counts)