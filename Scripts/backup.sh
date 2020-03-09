
cd ~

echo "Replace all (y) or one by one (n)"

read choice
echo $choice

cd ~ && cd Documents/Programming/Emacs/
sudo rm -r .emacs.d/
sudo rm .emacs
mkdir .emacs.d/

cd ~

if [ $choice == 'y' ]; then
    sudo cp -a .emacs Documents/Programming/Emacs/
    sudo cp -a .emacs.dCopy/. Documents/Programming/Emacs/.emacs.d/
else
    sudo cp -ai .emacs.dCopy/. Documents/Programming/Emacs/.emacs.d/
    sudo cp -ai .emacs.dCopy/. Documents/Programming/Emacs/.emacs.d/
fi



