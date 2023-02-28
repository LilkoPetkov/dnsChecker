from flask import request, render_template
from d_checker import app
from d_checker.functions import funcs


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/dns_check", methods=["GET", "POST"])
def dns_check():
    domain = request.form.get("domain")

    mx_len = funcs.len_check(funcs.dns_check_mx(domain))
    mx_result = funcs.mx_formatting(funcs.dns_check_mx(domain))

    txt_result = funcs.txt_formatting(funcs.dns_check_txt(domain))

    ns_result = funcs.dns_check_ns(domain).split()
    a_cname_result = funcs.dns_check_a(domain).split()
    dnssec_result = funcs.dns_check_dnssec(domain).split()

    return render_template("dns_check.html", ns=ns_result, a=a_cname_result, mx=mx_result, txt=txt_result,
                           dnssec=dnssec_result, domain=domain, mx_len=mx_len)