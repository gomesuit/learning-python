import ssl
import OpenSSL

cert = ssl.get_server_certificate(('www.google.com', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)

print(u'start:', x509.get_notBefore())
print(u'end:', x509.get_notAfter())

components = x509.get_subject().get_components()
for component in components:
    print(component)
