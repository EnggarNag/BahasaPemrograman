# Dokumentasi instalasi Tools

dimulai dari install WSL hingga Push Github.
step/langkah yang diperlukan selama instalasi hingga push github :

# Langkah 1 : Install terminal dan VSCode

Sebelum menginstall WSL. Install Windows Terminal melalui microsoft store untuk membantu membuka lebih dari 1 tab tools command yang berbeda dalam 1 aplikasi dan juga install Visual Studio Code sebagai media dalam membuat codingan yang nantinya akan di push ke Github.

# Langkah 2 : cek versi dan persyaratan instalasi

Untuk menjalankan WSL diperlukan persyaratan tertentu. check terlebih dahulu versi Windows Laptop kita.
• Untuk sistem x64: Versi 1903 atau yang lebih baru, dengan Build 18362 atau yang lebih baru.
• Untuk sistem ARM64: Versi 2004 atau yang lebih baru, dengan Build 19041 atau yang lebih baru.
• atau Windows 11.
Untuk memeriksa versi Windows dan nomor build nya , pakai shortcut Windows + R , ketik winver , pilih OK .

kita bisa memperbarui ke versi Windows terbaru dengan memilih Mulai > Pengaturan > Pembaruan Windows > Periksa pembaruan .

# Langkah 3 : Aktifkan fitur Subsistem Windowns dan Komputer virtual

Cari Windows Powershell -> Run as administrator lalu Aktifkan Subsistem Windows untuk Linux dengan ketik command.

    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

dan aktifkan fitur Komputer Virtual dengan ketik command

    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

lalu restart Laptop

# Langkah 4 : Install Ubuntu dan konfigurasi

Setelah direstart, Buka windows Powershell dengan run as administrator. Install ubuntu dengan command
wsl --install -d Ubuntu-20.04

Tunggu penginstallan selesai.
Setelah penginstallan selesai maka akan otomatis launch/membuka Ubuntu.
Dan akan muncul Registrasi Akun UNIX dengan memasukkan Username UNIX baru dan Password (sistem Linux membuat input password tidak terlihat). Lalu Retype Password sebagai konfirmasi.

Setelah itu akan muncul beberapa baris teks yang berisi informasi yang menandakan penginstallan dan registrasi akun berhasil. Lalu Tutup Ubuntu. Dan buka kembali Ubuntu melalui Windows Terminal.
Klik Navbar (panah bawah) pilih Ubuntu. Atau bisa atur di pengaturan dengan mengubah default profile menjadi Ubuntu agar setiap membuka Windows Terminal akan otomatis membuka Ubuntu (opsional)

Ketik Command di Windows Powershell

    ubuntu2004.exe config --default-user root

setelah itu tutup Ubuntu di windows terminal dan buka kembali Ubuntu untuk merefresh.

# Langkah 5 : Install ZSH dan Pluginnya

Install ZSH di Ubuntu dengan command

    apt install zsh

continue dengan Y.
cari “ohmyzsh” di mesin pencarian Google, klik website nya dan copy-paste command

    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

continue dengan y

Jika muncul gambar seperti itu maka menandakan ohmyzsh sudah terinstall.

Ubah Configurasi ZSH dengan ketik nano ~/.zshrc . didalam nano pengkonfigurasian dilakukan dengan menggunakan panah pada keyboard (tidak bisa menggunakan mouse).
Ubah ZSH theme (misal “agnoster”). Untuk save config ctrl+X -> Y -> Enter.
Ketik command source ~/.zshrc untuk merefresh hasil config. (selalu refresh setiap ada perubahan)
Download font di google search (FiraCode Nerd Font) dan gunakan font untuk di terminal ubuntu (opsional)
Pasang Plugin untuk zshnya
Cari di google “oh my zsh autosuggestions” -> pilih yang di github(zsh-users) copy-paste

    git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

    source ~/.zshrc

Ubah config plugin dengan masuk nano nano ~/.zshrc , tambahkan zsh-autosuggestions pada plugin setelah (git) => (git zsh-autosuggestions). save config ctrl+X -> Y -> Enter.

    source ~/.zshrc

buka juga “oh my zsh syntax-highlighting” di akun github yang sama (zsh-users) dan copy-paste

    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

    source ~/.zshrc.

Ubah config plugin dengan masuk nano nano ~/.zshrc , tambahkan zsh-syntax-highlighting pada plugin setelah (git zsh-autosuggestions) => (git zsh-autosuggestions zsh-syntax-highlighting). save config ctrl+X -> Y -> Enter.
source ~/.zshrc.

Penginstallan WSL dan zsh telah selesai

# Langkah 6 : Penginstallan bahasa pemrograman yang akan digunakan

Selanjutnya penginstallan bahasa pemrograman yang akan digunakan. Pada perkuliahan kali ini menggunakan python. Ketik command

    apt install python3

Download extension Python dan extension code runner di VSCode, ubah beberapa pengaturan (checkbox) dan buka executor map edit in settings.json. dan ubah extensionnya python menjadi python3.
Tes Python

# Langkah 7 : Connect WSL Laptop dengan github

Buka Github, jika belum mempunyai akun github buat akun terlebih dahulu. Lalu buat SSH keys baru

Settings => Access => SSH and GPG keys => New SSH keys
Input command di Ubuntu (misal)

    ssh-keygen -t ed25519 -C "enggarlanang@gmail.com"

Wsl akan menggenerate public/private key pair. Masukkan passphrase 2x (yang kedua untuk konfirmasi) . lalu akan muncul pemberitahuan bahwa identifikasi berhasil bersamaan dengan key fingerprint.
Selanjutnya input command pada baris yang bertuliskan
Enter file in which to save the key (/root/.ssh/id*####) dengan format cat ~/.ssh/id*##.pub
Lalu akan muncul key dan copy key tsb ke kolom SSH github.
Buka Developer Settings Github => Personal Access Token => Generate new Token
Ubah exp jadi “no Expiration”, Ceklis semua box dan generate. Copy token dan simpan dalam sebuah note. (jangan sampai hilang)

# Langkah 8 : init project -> push Github

Inisialisasi Project di folder yang memuat keseluruhan project dalam hal ini saya inisialisasi di folder BahasaPemrograman

• Masuk Directory BahasaPemrograman di windows terminal(Ubuntu), kemudian buka VSC
code .

• mulai coding, save codingan ctrl+s dan run code ctrl+alt+n
otomatis membuka terminal di bagian bawah VSC,

• jika terminal belum muncul maka ke tab terminal > new terminal > dibawah kanan ada powershell biasanya dan ada panah bawah di samping tanda +, diklik lalu pilih ubuntu (wsl) / gitbash yang ada aja salah satunya. setelah semua sudah di save dan ready to deploy to github

• inisialisasi project di direktori yang memuat keseluruhan project
git init
• add keseluruhan project yang ada di direktori tsb
git add .
• commit
git commit –m “push”
• ubah konfigurasi akun
git config –global –edit
ubah username dengan username github dan email dengan email github
• set branch dengan nama main
git branch –m Main
• membuat repository
curl -u 'EnggarNag' https://api.github.com/user/repos -d '{"name":"BahasaPemrograman","private":false}'
enter host password (token github)

• arahkan untuk push ke dalam repository yang sudah dibuat tadi
git remote add origin git@github.com:EnggarNag/BahasaPemrograman.git

• Push
git push –u origin main
