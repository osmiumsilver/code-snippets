ports = set("21,22,23,25,53,80,443,135,137,138,139,445,587,993,995,1080,1433,1701,1723,3306,5432,8000,8080,11211,2179,3389,5975,7680,8090,47001,49600-49700,7890,5040,5050,5000,7000,5985,3702".split(","))

ports_int = []
for port in ports:
    try: ports_int.append(int(port))
    except ValueError: ports_int.append(port)

def __sort(port):
    if isinstance(port, int):
        return (0,port)
    if isinstance(port, str):
        return (1, port)
ports_int.sort(key=__sort)
print(ports_int,sep=',',end='',flush=True)