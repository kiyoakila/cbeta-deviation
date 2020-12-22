import os


def SCAN(name):
    Files = open(str(name),'r')
    content = Files.read()
    content = content.split(' The following ModRedundant input section has been read:')[-1]
    content = content.split('\n')[1:3]
    if content[1] == ' ':
        ScanA = content[0].split()
        if ScanA[0] == 'A':
            BA = ScanA[0] + '(' + ScanA[1] + ',' + ScanA[2] + ',' + ScanA[3] + ')'
            return BA
        if ScanA[0] == 'D':
            DA = ScanA[0] + '(' + ScanA[1] + ',' + ScanA[2] + ',' + ScanA[3] + ',' + ScanA[4] + ')'
            return DA
    if content[1] != ' ':
        ScanA1 = content[0].split()
        if ScanA1[0] == 'A':
            BA1 = ScanA1[0] + '(' + ScanA1[1] + ',' + ScanA1[2] + ',' + ScanA1[3] + ')'
            ScanA2 = content[1].split()
            if ScanA2[0] == 'A':
                BA2 = ScanA2[0] + '(' + ScanA2[1] + ',' + ScanA2[2] + ',' + ScanA2[3] + ')'
                return BA1,BA2
            if ScanA2[0] == 'D':
                DA2 = ScanA2[0] + '(' + ScanA2[1] + ',' + ScanA2[2] + ',' + ScanA2[3] + ',' + ScanA2[4] + ')'
                return BA1,DA2
        if ScanA1[0] == 'D':
            DA1 = ScanA1[0] + '(' + ScanA1[1] + ',' + ScanA1[2] + ',' + ScanA1[3] + ',' + ScanA1[4] + ')'
            ScanA2 = content[1].split()
            if ScanA2[0] == 'A':
                BA2 = ScanA2[0] + '(' + ScanA2[1] + ',' + ScanA2[2] + ',' + ScanA2[3] + ')'
                return DA1,BA2
            if ScanA2[0] == 'D':
                DA2 = ScanA2[0] + '(' + ScanA2[1] + ',' + ScanA2[2] + ',' + ScanA2[3] + ',' + ScanA2[4] + ')'
                return DA1,DA2
                           
def separate(name):
    Files = open(str(name),'r')
    content = Files.read()
    content = content.split(' ! Name  Definition              Value          Derivative Info.                !')[-1]
    content = content.split(' --------------------------------------------------------------------------------')[1]
    content = content.split('\n')[1:-1]
    DN = content[-1].split()[1]
    DA = content[-1].split()[2]
    return ' ' + '! ' +  DN + '   ' + DA


def parameter(name):
    files = open(str(name),'r')
    cont = files.read()
    stepcont = cont.split(separate(name))
    for step  in stepcont[1:-1]:
        Name = ''
        if len(SCAN(name)) == 2:
            OBJ1 = '%.0f' % float(step.split(SCAN(name)[0])[-1].split()[0])
            OBJ2 = '%.0f' % float(step.split(SCAN(name)[1])[-1].split()[0])
            Name = Name + 'Psi_' + str(OBJ1) + '_Phi_' + str(OBJ2)
        if len(SCAN(name)) != 2:
            OBJ = '%.0f' % float(step.split(SCAN(name))[-1].split()[0])
            Name = Name + 'OBJ_' + str(OBJ)
        coordinate = step.split("Standard orientation")[-1]
        coordinate = coordinate.split("Rotational constants")[0]
        coordinate = coordinate.split("\n")[5:-2]
        PDB = open('tmp.pdb','r')
        PDBcontent = PDB.read()
        n = 0
        for At in coordinate:
            n = n + 1
            att = ''
            At = At.split()
            if At[3][0]== '-':
                att = att + '%.3f' % float(At[3])+ '  '
            elif At[3][0] != '-':
                att = att + ' ' + '%.3f' % float(At[3]) + '  '
            pass
            if At[4][0] == "-":
                att = att + '%.3f' % float(At[4]) + '  '
            elif At[4][0] != "-":
                att = att + ' ' + '%.3f' % float(At[4]) + '  '
            pass
            if At[5][0 ]== "-":
                att = att + '%.3f' % float(At[5]) + '  '
            elif At[5][0] != "-":
                att = att + ' ' + '%.3f' % float(At[5]) + '  '
            pass
            if At[1]=="6":
                att = att + "                     " + "C"
            elif At[1]=="8":
                att = att + "                     " + "O"
            elif At[1]=="7":
                att = att + "                     " + "N" 
            elif At[1]=="1":
                att = att + "                     " + "H"
            pass
            PDBcontent = PDBcontent.replace('AT' + str(n) + '_' , att)
        PDBfiles = open(str(name.split('.')[0]) + '/' + Name + '.pdb', 'w' )
        PDBfiles.write(PDBcontent)
        PDBfiles.close()
            

if __name__=='__main__':
    name = ['MeAlaNH2L_scan_alpha.log']
    for i in name:
        SCAN(i)
        separate(i)
        parameter(i)