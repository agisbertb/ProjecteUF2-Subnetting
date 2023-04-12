# ============ SECCIÓ DE FUNCIONS ============

# Funció per limitar l'entrada per teclat a la màscara cdir

def limit_input_masc(text):
    if len(text) > 2:
        return False
    return True

# Funció per limitar l'entrada per teclat a l'adreça ip

def limit_input_ip(text):
    if len(text) > 15:
        return False
    return True

# Funció per calcular la mascara decimal a partir de la màscara cidr

def cidr_a_decimal(cidr):
    global decimal_mask
    mask_bin = ''.join(['1' if i < cidr else '0' for i in range(32)])
    octets_bin = [mask_bin[i:i+8] for i in range(0, len(mask_bin), 8)]
    octets_decimal = [str(int(octet_bin, 2)) for octet_bin in octets_bin]
    decimal_mask = '.'.join(octets_decimal)
    return decimal_mask

# Funció per calcular la mascara decimal a partir de la màscara binaria

def decimal_a_binari(decimal):
    octets = decimal.split('.')
    octets_bin = [bin(int(octet))[2:].zfill(8) for octet in octets]
    mask_bin = '.'.join(octets_bin)
    return mask_bin

# Funció per calcular la mascara wildcard a partir de la màscara decimal

def decimal_a_wildcard(decimal):
    octets = decimal.split('.')
    octets_wildcard = [str(255 - int(octet)) for octet in octets]
    wildcard_mask = '.'.join(octets_wildcard)
    return wildcard_mask

# Funció per calcular la adreça de xarxa a partir de l'adreça ip i la màscara

def ip_de_xarxa(ip,mask):
    ip_octets = ip.split('.')
    mask_octets = mask.split('.')
    network_octets = [str(int(ip_octet) & int(mask_octet)) for ip_octet, mask_octet in zip(ip_octets, mask_octets)]
    network_address = '.'.join(network_octets)
    return network_address

# Funció per calcular la adreça de broadcast de la xarxa a partir de l'adreça ip i la màscara

def broadcast_address(ip_address, subnet_mask):
    ip_octets = ip_address.split('.')
    mask_octets = subnet_mask.split('.')
    broadcast_octets = []
    for i in range(4):
        broadcast_octets.append(str(int(ip_octets[i]) | (255 - int(mask_octets[i]))))
    broadcast_address = '.'.join(broadcast_octets)
    return broadcast_address

# Funció per calcular el primer host de la xarxa

def primer_host(ip_address, subnet_mask):
    ip_octets = ip_address.split('.')
    mask_octets = subnet_mask.split('.')
    network_octets = [str(int(ip_octets[i]) & int(mask_octets[i])) for i in range(4)]
    network_address = '.'.join(network_octets)
    ip_octets = network_address.split('.')
    ip_octets[3] = str(int(ip_octets[3]) + 1)
    primer_host = '.'.join(ip_octets)
    return primer_host

# Funció per calcular l'ultim host de la xarxa

def ultim_host(ip_address, subnet_mask):
    ip_octets = ip_address.split('.')
    mask_octets = subnet_mask.split('.')
    broadcast_octets = []
    for i in range(4):
        broadcast_octets.append(str(int(ip_octets[i]) | (255 - int(mask_octets[i]))))
    broadcast_address = '.'.join(broadcast_octets)
    ip_octets = broadcast_address.split('.')
    ip_octets[3] = str(int(ip_octets[3]) - 1)
    ultim_host = '.'.join(ip_octets)
    return ultim_host

# Funció per calcular el total de hosts de la xarxa

def total_hosts(decimal):
    octets = decimal.split('.')
    octets_bin = [bin(int(octet))[2:].zfill(8) for octet in octets]
    mask_bin = ''.join(octets_bin)
    total_hosts = 2 ** mask_bin.count('0') - 2
    return total_hosts

# Funció per trobar classe de l'adreça ip

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

# Funció per trobar si la adreça ip és privada o pública

def tipus_ip(adreçaip):
    octets = adreçaip.split('.')
    if len(octets) != 4:
        return False
    if octets[0] == '10':
        return 'Privada'
    elif octets[0] == '172' and 16 <= int(octets[1]) <= 31:
        return 'Privada'
    elif octets[0] == '192' and octets[1] == '168':
        return 'Privada'
    else:
        return 'Publica'
    
    