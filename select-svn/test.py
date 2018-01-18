from ftplib import FTP

ftp_ip = '112.74.133.133'
ftp_port = 21

ftp_user = 'com_dc_baopintao'
ftp_password = '564&sfgsk'

with FTP(ftp_ip) as ftp:

    ftp.set_debuglevel(2)
    # ftp.connect(ftp_ip, ftp_port)

    ftp.login(ftp_user, ftp_password)

    print (ftp.dir())
