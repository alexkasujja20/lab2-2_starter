# lab2-2_Top 5 attacler Ips and export.py

LOGFILE = "sample_auth_small.log" 
from collections import defaultdict # change filename if needed
import time
start = time.time()
List_ips=[]
lines_read =0
Unique_list_ips=[]

counts = defaultdict(int) 
def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

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
    
print("\nTop 5 attackers Ips:")   
    
final_list =top_n(counts, 5)
num = 0
for i in final_list:
    num +=1
    print(num, ".", i[0], "--" ,i[1])
        
        

# run counting
end = time.time()
with open("Wrorte failed_counts.txt", "w") as f:
        print(f"Wrote failed_counts.txt")
print("Elapsed:", end-start, "seconds")    