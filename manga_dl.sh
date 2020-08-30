#!/bin/bash
myself=`basename "$0"`
echo "komikmanga.com downloader"

# respon input kosong
if [ -z "$1" ]; then
	clear
	echo
	echo "usage: ./"$myself" <link> <directory> <makecbz>"
	echo $myself " https://komikmanga.com/manga/uzumaki-spiral-into-horror/01 uzumaki/chapter1 makecbz"
	echo
	echo "untuk sementara command harus berurutan hhhh :>"
    exit 1
fi


# oks
if [[ ${1} != *"https://komikmanga.com/manga/"* ]];
then
    echo "link salah"
else
	clear
	echo "downloading......"
	echo
	judul="$(sed -r 's/https:\/\/komikmanga\.com\/manga\/([^"]+)\/([^"]+)/\1/' <<< "${1}")"
	chapter="$(sed -r 's/https:\/\/komikmanga\.com\/manga\/([^"]+)\/([^"]+)/\2/' <<< "${1}")"
	echo "judul: $judul"
	echo "chapter: $chapter"
	echo
		for donlot in 'https://komikmanga.com/uploads/manga/'$judul'/chapters/'$chapter'/'{01..99}'.jpg'
			do
				wget -c -nc "$donlot" -P "$2" || break	
			done
			
		for donlot2 in 'https://komikmanga.com/uploads/manga/'$judul'/chapters/'$chapter'/'{02..99}'.png'
			do
				wget -c -nc "$donlot2" -P "$2" || break	
			done
	echo
	echo "selesai donlot > $(pwd)/$2"
	echo
	if [[ $3 = "makecbz" ]];
				then zip ${judul}_chapter_$chapter.cbz -r $2 -i *.jpg *.jpeg *.png
				echo
				echo "selesai compress cbz > $(pwd)/${judul}_chapter_$chapter.cbz"
				echo "hapus directory.........."
				rm "$(pwd)/$2" -rf -v
				echo
	fi			
	echo "tugas beres."
	exit
fi


			

