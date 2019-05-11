import ssl
import OpenSSL
from IPython import embed

def get_certificate_san(x509cert):
    san = ''
    ext_count = x509cert.get_extension_count()
    for i in range(0, ext_count):
        ext = x509cert.get_extension(i)
        if 'subjectAltName' in str(ext.get_short_name()):
            san = ext.__str__()
    return san

def main():
    cert = ssl.get_server_certificate(('www.google.com', 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    # embed()

    print(u'start:', x509.get_notBefore())
    print(u'end:', x509.get_notAfter())

    components = x509.get_subject().get_components()
    for component in components:
        print(component)

    print(get_certificate_san(x509))

if __name__ == "__main__":
    main()
