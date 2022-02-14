echo "This Programm Work for Debian Distro!"
echo -n "Do you have a Target Mac Address? (y|n): "
read question

if [[ $question == "y" || $question == "yes" ]]; then
  echo -n "Enter Target Ip Address: "
  read ip
  echo -n "Enter Target Mac Address: "
  read mac
  sudo arp -s $ip $mac
  echo "[+]Arp Table Set Successfuly!"
  sudo arp -a
fi

if [[ $question == "n" || "no" ]]; then
  echo -n "Do you have nmap: (y|n)"
  read nmap
  if [[ $nmap == "y" ]]; then
    echo -n "Enter Target Ip Address: "
    read search
    sudo nmap $search
    echo "The Nmap can find Mac at The end of Scan!"
  elif [[ $nmap == "n" ]]; then
    sudo apt-get install nmap
    echo "After The Installation Run Programm again for seting arp Table!"
  fi
fi
