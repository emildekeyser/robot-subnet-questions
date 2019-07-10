# A Gegeven netwerk (\d*\.\d*\.\d*\.\d*/\d*), geef het (\d*)e subnet waarin je minstens (\d*) hosts uniek kan adresseren.
# B Gegeven netwerk (\d*\.\d*\.\d*\.\d*/\d*), bereken het netmask.
# C Gegeven netwerk (\d*\.\d*\.\d*\.\d*/\d*), bereken het maximaal aantal hosts dat een uniek IP-adres binnen dit netwerk kunnen krijgen.
# D Gegeven een subnet (\d*\.\d*\.\d*\.\d*/\d*), bereken de volgende adressen.

def A(args):
    print(args)
    hostbits = hostbits_from_host_amount(args[6])
    slash = "/" + str(32-hostbits)
    ip_bitfield = pad_zeroes(bitfield(args[0]))
    ip_bitfield += pad_zeroes(bitfield(args[1]))
    ip_bitfield += pad_zeroes(bitfield(args[2]))
    ip_bitfield += pad_zeroes(bitfield(args[3]))
    nth_subnet = bitfield(int(args[5])-1)

    print(ip_bitfield)
    nth_subnet.reverse()
    print(nth_subnet)

    start = 32 - 1 - hostbits
    for i in range(len(nth_subnet)):
        ip_bitfield[start - i] = nth_subnet[i]

    print(slash)
    print(ip_bitfield)
    print('----')
    ip = bitfield_to_ip(ip_bitfield) + slash
    print(ip)
    return ip

def B(args):
    print(args)
    networkbits = int(args[4])
    hostbits = 32-networkbits
    netpart = [1] * networkbits
    hostpart = [0] * hostbits
    return bitfield_to_ip(netpart + hostpart)

def C(args):
    print(args)
    exponent = 32-int(args[4])
    return (2**exponent)-2

def D(args):
    print(args)
    # slash = "/" + args[4]
    netw_address = ".".join(args[:4])

    first_address = list(args).copy()
    first_address[3] = str(int(first_address[3])+1)
    first_address = ".".join(first_address[:4]) 

    broadcast_address = pad_zeroes(bitfield(args[0]))
    broadcast_address += pad_zeroes(bitfield(args[1]))
    broadcast_address += pad_zeroes(bitfield(args[2]))
    broadcast_address += pad_zeroes(bitfield(args[3]))
    hostbits = 32-int(args[4])
    hostpart = [1] * hostbits
    broadcast_address = broadcast_address[:-hostbits] + hostpart
    print(broadcast_address)
    broadcast_address = bitfield_to_ip(broadcast_address)
    print(broadcast_address)

    last_address = broadcast_address.split('.')
    decremented = str(int(last_address[3])-1)
    last_address = last_address[:3] + [decremented]
    last_address = ".".join(last_address)
    print(last_address)

    return [netw_address, first_address, last_address, broadcast_address]

def hostbits_from_host_amount(hosts):
    hosts = int(hosts)
    hosts += 2
    for i in range(8):
        if 2**i >= hosts:
            return i

def bitfield(n):
    return [1 if digit=='1' else 0 for digit in bin(int(n))[2:]]

def pad_zeroes(field):
    while len(field) < 8: field.insert(0, 0)
    return field

def bitfield_to_ip(bits):
    bits = [str(b) for b in bits]
    print(bits)
    octets = [\
        "".join(bits[0:8]),\
        "".join(bits[8:16]),\
        "".join(bits[16:24]),\
        "".join(bits[24:32]),\
    ]
    print(octets)
    octets = [str(int(octet, 2)) for octet in octets]
    return ".".join(octets)


