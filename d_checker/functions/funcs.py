import os
from re import findall


def dns_check_ns(domain):
    return os.popen(f"dig +short NS {domain}").read()


def dns_check_a(domain):
    return os.popen(
        f"dig +short A {domain}; dig +short A www.{domain}; dig +short cName www.{domain}; dig +short AAAA {domain}").read()


def dns_check_mx(domain):
    return os.popen(f"dig +short MX {domain}").read()


def dns_check_txt(domain):
    return os.popen(f"nslookup -type=TXT {domain}").read()


def dns_check_dnssec(domain):
    return os.popen(f"whois {domain} | grep -i dnssec").read()


def len_check(func):
    mx_len = len(func.split())

    return mx_len


def mx_formatting(func):
    mx_len = len(func.split())

    if mx_len <= 2:
        mx_result = f"Priority: {func.split()[0]} - Value: {func.split()[1]}"

        return mx_result
    else:
        as_list = func.split()
        result = []

        for idx in range(0, len(as_list), 2):
            result.append(f"Priority: {as_list[idx]} - Value: {as_list[idx + 1]}")

        mx_result = result

        return mx_result


def txt_formatting(func):
    value = func

    pattern = r'\"(.*?)\"'
    result = findall(pattern, value)

    return result
