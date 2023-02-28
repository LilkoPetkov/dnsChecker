import os


def dns_check_ns(domain):
    return "NS records: " + "\n" + "\n" + os.popen(f"dig +short NS {domain}").read()


def dns_check_a(domain):
    return "A and cName records: " + "\n" + "\n" + os.popen(
        f"dig +short A {domain}; dig +short A www.{domain}; dig +short cName www.{domain}; dig +short AAAA {domain}").read()


def dns_check_mx(domain):
    return "MX records: " + "\n" + "\n" + os.popen(f"dig +short MX {domain}").read()


def dns_check_txt(domain):
    return "TXT records: " + "\n" + "\n" + os.popen(f"dig +short TXT {domain}").read()


def dns_check_dnssec(domain):
    return "DNSSEC records: " + "\n" + "\n" + os.popen(f"whois {domain} | grep -i dnssec").read()

