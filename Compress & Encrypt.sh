#!/bin/bash

clear
cat << EOF
Please Select:

1. Compress and Encrypt Directory
2. Decrypt Directory
0. Quit

EOF

echo -n 'Enter Selection [0-2]: '
read -r option

case $option in
        0) echo "Program Terminated.";;
        1) echo -n 'Enter directory: '
           read pathEn
           echo -n 'Enter archive: '
           read nameEn
           tar -czvf $nameEn.tar.gz --absolute-names $pathEn
           echo tar -czvf $nameEn.tar.gz --absolute-names $pathEn
           gpg -c $nameEn.tar.gz
           rm -rf $nameEn.tar.gz;;
        2) echo -n 'Enter directory to decrypt: '
           read pathDe
           gpg $pathDe.tar.gz.gpg;;

        *)
           echo "Invalid Entry.">&2
           exit 1
esac
