#Mascara Cidr a decimal
def cidr_a_decimal(cidr):
    global decimal_mask
    mask_bin = ''.join(['1' if i < cidr else '0' for i in range(32)])
    octets_bin = [mask_bin[i:i+8] for i in range(0, len(mask_bin), 8)]
    octets_decimal = [str(int(octet_bin, 2)) for octet_bin in octets_bin]
    decimal_mask = '.'.join(octets_decimal)
    return decimal_mask

#Mascara de red decimal a binario
def decimal_a_binari(decimal):
    octets = decimal.split('.')
    octets_bin = [bin(int(octet))[2:].zfill(8) for octet in octets]
    mask_bin = '.'.join(octets_bin)
    return mask_bin

#Mascara decimal a wildcard
def decimal_a_wildcard(decimal):
    octets = decimal.split('.')
    octets_wildcard = [str(255 - int(octet)) for octet in octets]
    wildcard_mask = '.'.join(octets_wildcard)
    return wildcard_mask

#Ip de red a partir de ip y mascara
def ip_de_xarxa(ip,mask):
    ip_octets = ip.split('.')
    mask_octets = mask.split('.')
    network_octets = [str(int(ip_octet) & int(mask_octet)) for ip_octet, mask_octet in zip(ip_octets, mask_octets)]
    network_address = '.'.join(network_octets)
    return network_address

#Ip de broadcast a partir de ip y mascara
def broadcast_address(ip_address, subnet_mask):
    ip_octets = ip_address.split('.')
    mask_octets = subnet_mask.split('.')
    broadcast_octets = []
    for i in range(4):
        broadcast_octets.append(str(int(ip_octets[i]) | (255 - int(mask_octets[i]))))
    broadcast_address = '.'.join(broadcast_octets)
    return broadcast_address

#Ultim host de la xarxa
def ultim_host(ip_address, subnet_mask):
    ip_octets = ip_address.split('.')
    mask_octets = subnet_mask.split('.')
    broadcast_octets = []
    for i in range(4):
        broadcast_octets.append(str(int(ip_octets[i]) | (255 - int(mask_octets[i]))))
    broadcast_address = '.'.join(broadcast_octets)
    ip_octets = broadcast_address.split('.')
    ip_octets[3] = str(int(ip_octets[3]) - 1)
    ultimo_host = '.'.join(ip_octets)
    return ultimo_host

#Primer host de la xarxa
def primer_host(ip_address, subnet_mask):
    ip_octets = ip_address.split('.')
    mask_octets = subnet_mask.split('.')
    network_octets = [str(int(ip_octets[i]) & int(mask_octets[i])) for i in range(4)]
    network_address = '.'.join(network_octets)
    ip_octets = network_address.split('.')
    ip_octets[3] = str(int(ip_octets[3]) + 1)
    primer_host = '.'.join(ip_octets)
    return primer_host

#Hosts de la xarxa
def total_hosts(decimal):
    octets = decimal.split('.')
    octets_bin = [bin(int(octet))[2:].zfill(8) for octet in octets]
    mask_bin = ''.join(octets_bin)
    total_hosts = 2 ** mask_bin.count('0') - 2
    return total_hosts

#Funcio per trobar classe de la ip
def classe_ip(adreçaip):
    ip_octets = adreçaip.split('.')
    if int(ip_octets[0]) <= 127:
        return 'A'
    elif int(ip_octets[0]) <= 191:
        return 'B'
    elif int(ip_octets[0]) <= 223:
        return 'C'
    elif int(ip_octets[0]) <= 239:
        return 'D'
    elif int(ip_octets[0]) <= 255:
        return 'E'
    else:
        return 'Error'

#Funcio per trobar el tipus de la ip

def tipus_ip(adreçaip):
    """
    Determina si una dirección IP es privada o no.
    """
    octetos = adreçaip.split('.')
    if len(octetos) != 4:
        return False
    if octetos[0] == '10':
        return 'Privada'
    elif octetos[0] == '172' and 16 <= int(octetos[1]) <= 31:
        return 'Privada'
    elif octetos[0] == '192' and octetos[1] == '168':
        return 'Privada'
    else:
        return 'Publica'
    
    