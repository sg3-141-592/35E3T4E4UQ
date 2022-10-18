import dns.resolver

CERT_TYPES = [dns.rdatatype.A, dns.rdatatype.AAAA, dns.rdatatype.CNAME]
DOMAIN = 'dishy.dev'

print(f"Checking {DOMAIN} ...")
# Get A records and AAAA records
for CERT in CERT_TYPES:
    try:
        answers = dns.resolver.resolve(DOMAIN, CERT)
        for rdata in answers:
            print("{} - {}".format(dns.rdatatype.to_text(CERT), rdata.to_text()))
    except dns.resolver.NoAnswer:
        print(f'{DOMAIN}: No answer for {dns.rdatatype.to_text(CERT)}')
