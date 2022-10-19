from OpenSSL import crypto

private_cert_file = open("root_privkey.pem")
private_cert = crypto.load_privatekey(crypto.FILETYPE_PEM, private_cert_file.read())
private_cert_file.close()

start_line = b'-----BEGIN CERTIFICATE-----'

def read_all_certs(pem_bytes):
    result = []
    cert_slots = pem_bytes.split(start_line)
    for single_pem_cert in cert_slots[1:]:
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, start_line+single_pem_cert)
        result.append(cert.get_subject())
        result.append(cert.get_notBefore())
    return result

chain_cert_file = open("root_fullchain.pem", "rb")
print(read_all_certs(chain_cert_file.read()))
chain_cert_file.close()