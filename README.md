# 🤖 LinkedIn Auto-Connector Bot

Este bot automatiza el envío de solicitudes de conexión en LinkedIn usando Python + Selenium.

📌 Va directamente a la página de sugerencias de contactos  
📌 Hace scroll automático  
📌 Encuentra y hace clic en los botones de "Conectar"  
📌 Permite configurar un máximo de conexiones por sesión  

---

## ⚙️ Requisitos

- Python 3.8 o superior
- Google Chrome
- [Chromedriver incluido con `undetected-chromedriver`]

---

## 🚀 Instalación y uso

### 1. Clonar el repositorio

### 2. Crear entorno virtual

## En cmd o PowerShell

python -m venv venv
venv\Scripts\activate


## en bash

python -m venv venv
source venv/Scripts/activate

### 3. Instalar dependencias

pip install selenium undetected-chromedriver python-dotenv

### 4. Configurar env

USERNAME=""
PASSWORD=""


### 5. Ejecutar script

python linkedin_script.py


Hice este script para automatizar la tarea aburrida. Automatizar interacciones en plataformas como LinkedIn puede violar sus términos de uso. Usalo con precaución y bajo tu propia responsabilidad.
Se recomienda limitar la cantidad de conexiones diarias.

c::::clc::::cccccc:::loddlccoxoodk00Okdocc:::::::;;::::;::;:::ldkO00KXNNWWWWWWWNNNNNNNNXXXXXXXXKKKKK
;:::::cc:::::clodollooxOxlllldocllc:::::::::;;;;;;;;;;;;;;;;::::::coxOKNWWWNNNNNNNNNNNNNNNXXXXXXXKKK
;;;::::::;:::coddddxxdxkdlodl:::::::;::;;;;;;;;;;;;;;;;;;;;;;,,,;;::cccoxkkkOOOOOOOOO0KXXNNNXXXXXXKK
::::::::::::::cllloxO0000kool:;;;;;;;;;;;;;,;;;;,''''',,,'......',;;;;:::clx0000XXXXK0OOOOKXNNXXXXXX
:::;:::::clcc::::clodOKXXOl:;,',;;;;;;;,,;;;;,'.......','........,;;;;;;::::clllxKWWWWWNX0OO0XNXXXXX
:::::::lllol:;:::clllxkxoc:,',;;;;;;;,,,;;,,.....''''',;;,,'......,;;;;;;;:::::cco0NWWWWWNNX000XNXXX
::::::ccc:ccc:;;:ccoddoc::,.;l:;;;;,,,,;;,'..',,,,,,,,,;,,,,,'.....,;;;;;;:;;:::ccoONWWWWWNNNNK0KXXX
:::::cccc:::c::::::clllc;',lolc;,;,,,;;,'..',,,,,,,,',,;;;;,,,,''...';;;;;;;;;;:c:co0NWWWWWNNNXK000K
::::::::::::::ccc::::cc,,coxxo;.,;::;;,''',,,,,,,,,'',,;;;;;,,,,,,'..';;;;;;;;,,clccx0NWWWNXXXKKKKK0
dlc::::::::::cccc::;:c;:cclxd;.,;cc:;,'',,,,,,.',,'.',;;;;;;,,,,,,;,..',,,;;;;,',loclk0NWWNNXKKKXXK0
ddlcc:::::::::::cc:;:cc:;coo;..,cl:;,''''.','..';'..',;;,;:::;,;;,,:;..,,',;;;;,',lxldO0NWNNXKKXK0O0
ccllc::clcccccccllc:c:;;:cc;..':c:;,......,....,,....,;;,,:lc;',;:,;ll,','.,;;;;,',oxxkOKNNNXXXXK0Ok
cllcccldkOOOxdoolc::;;;;::,...,::;,......'.....,'....';;'';cl;'';::,:dd;,,..';;;;;,;lxOOOKNNNNNXXXKK
clodollldkOOkoc::;;;;;;;;,...';;;,.............'..'...,;'.':c;.';::,,lxo;,,..,;;;;;;;lxkkO0XNNNNNNNN
ccloolllllc:::;;;;;;;;;;;'...,;,,.......'.........,,..';,..;:,..,;,..;ldl,,'.';;;;;;;:cdxxk0XNNNNNNN
ccc:::::;;:ccc;;;;;;;,,;,....,;,'.....,;...,.....';,...,'..,:,..',...,:cl:,;'.,;;;;,,;;:oodk0XXXNNXX
;;;;::::cc:::;;;;;;;'',;,....,;'.....,:,..';.....';,.......';,...'....;;cc;;,',;,,,,'';;clldk0XXKKKK
::cccccccc:;;;;;;,,,.';;'....;,..'..'cc;..,,......,,........,'........,,;:;,;,,,;,',,.',;::cdk0KK000
::ccc:cclc:;;;;;,,,..,;,....';,.....,:c:..:c;.....',........,.........,,',;,;,,,,,'','..',:::okOK0OO
::ccc::clc;;;;'..'..';;,....';,'';:,'..'..:::'......'.......'.........',.',,,,,,,,,..'....;;:lodk0Ok
::cllc:cl:;;,'.....,;;;.....';;clOOl,.....;:::................',......',..,,,;,,,,;'.'.....;:oxolxOk
:cclllcc:;;,,.....';;;,.....',cc,;:,'...;:,:cl:...............,,..'...',..,,,;,',,;'..'....';:d0xlok
cc:::cc:;;,,'.....';;;'......,cdlodlcl::xxlclll;.......'..............',..',,;,',,;,........,;ckKkoo
lc::;;;,;,'........,;;.......':odxOOOkx0NXOdddl:.....';'''';,.........''...,;;'.,,,;'..'.....;:cdxOk
;;::::;,,'.........';,........,cdxxxxkKNXXXK00d:'...,cllo:,,..''.;l'.......,;;'.',,;'...'....';cdxxk
c::::;;,'...........,,.........;oO0000KXXXXXXXk;';;cdkxxOooocoo:;ll........,;,..'.',....;;....;:lkOk
c:::;,,'... ........,,.........,:ok000KKXXXXXKxldkO0K00KKkoxkxdoOO;........,;'....''....'oc...,:ckXX
:;;;;,...  ... .....,,.......'',ccox0KKKKXXXK0O0XXNXXXXXK0kddold0d..,,.....;,............lkc..';:o0X
;;;:,......'........',.......,;;lxxxOKXXXXXXXKO0XNNNXXXKKKK00KK0o;,;:,.....,.........'...c0Kc..,:lOX
:;,....',;:;..... ...,.......:c::dO0KXXNNNNNXOxKNNNNXXXKKKK00Okddxl:;... ............;:..:0NO;.,:o0K
,''',;;::::,..,.    .'.......,lddldk0KXNNNNNNKKXNNNNNXXXXKKKK00KOo;'.......      ....;l,.;0NKd'':lxO
;:c:::;;:::'.,'.    ..........,lk00OOKXNXXXXXXXXXXXNNNXXXXXXXXXO:'.......      ......,l:.;kXXXl':cok
::::::::::;,;,....   ..........,lxKXXNNNNNXXXXXXXKXXNNNNNXXXXKx;.......         .....'oo,;O00NO:;cdk
::::::::::;;;'.....  ..........,;cd0XXXNNNXK0KXNNNNNNNNNXXXXOl'..........       ....''lk::KXNNXd;ckX
:::c::::;;;;;.......  .........,;;:cx0XNNNNNXXNNNNNNNXXXX0xc'........ ...      ....,;,;oldNNNNWOcckX
:::::cc;,;;;'.. ..... ..........;:;::lkKXNXNNXNNNNXXKOxl:'..........  ...     ....';;;;:cOXKKKXOlcxO
:lolddc;;,;;'......  ............;::;::lkKXXXXX0Oxdol;.............  .....  ..''..';;;;,:k0OOO0Ol:lo
kKKxlc;,,''''....',::,............:c:::::oxkxdlc::::;.............   ........,;,...,;;:;;ldddxxdl:lo
odo:,,'......''''.',codc'.........':cc:::::;::::::::,...........     .'... .';,,,...,;;;lddooxdc;:lo
,'......     ....''''':dxc'..,;,...,clcc::;::::::ccc,..........    . .'.....';;;;;...,;;:ldoloxl:clc
......    ....   ...'''.:do,';cc;'..;cllc:::::cccllc........... .  ...'......,;;;cl,..';:::ldol::lcc
'''''.... .............'..::,',loc,',:clllccclllllo:............... .........',;;coxd:'.,:::lodloxdd
'''''''''....   ........'..'''',dxl;:;:lllllcllllll;..........................',;:lkKXOo::clooloxdoo
...''''''''''..    ...'''....''',xOl:::ccllllclllll:;,.........................',;:dKNWWKOOOkdlooccc
  ....'''''''''..     ..''..'''.';x0o::cooclllcllllcccc:;,'''..................',';:dKXXXX0xdoolcccc
     ..'''''''''..     ..''.'''''':k0d::dOxolcccllllcllllloOOxl;'......';'......','':ok0KOkxoooollll
       ..''''''''.      ...'''''''':kKklcd0KOxolcclllllllld0KKKOl;.....c00d;.....,,'';:dO00kdoxxoxOk
        ..'''''''.        ...''''''';xX0xloOXX0kxxdollllok0XXXXXKko:'..,kXXx,'''..,;'.';lodddddxdx0X
         ..''''''.          ..''''''';dKX0dld0X0kkOOkddoxKNXKO0XXX0x:'..lKXx,',,''',;;;'';:coodkkddO
.          .''''..           ..'''''',,cx0KkcckKOdodxxk0KXXKOkKNNNX0d:'.,k0l','','''',cc,.';:lx00Oxd
..          ...'.              .''',,''',:okk:;ok00OxddOXNXKKXNNXXXNKkl,.co;'',','','',lOkc'';oOXXkx
...          ....               ..''''''''',c:',cdk0XK00XNXNNNNXNNNNNXKx;.''',''''''''';dXNOl,';lkOO
...            .                  .'''''''''''..,::cxKXNNNNNNNNNNNNNNXXXO;.''''''''''',''oKWN0o;',:o
                                   ..''''''''''..;:::okKXNXXXNNNNNNNXXXKd,..','''''''''...:ONWNKx:'.
                                   ..''''''''''..':;;;;:okKXXXNNNNNNNXKd;'...';,,'''''''...,oOKKXKx:
                                   ....'''''''....,;;;;,',cdk0XXXK0XX0o,',''''',,,,,,'''.....;dkxkxd
                                     .''''''''....',,,;,',,',;cxKKkxko,,,''''''''',,,,,,......,colll
                                     .''''''''.....''';;'''''',,cOKOoc,',,''''''''''''',,.......;:cl
                                    ..''''''.......''',,''''''..';xK0l,'''''''''''''''''''.......';c
                                    .'''''.......''''',,'''''''...'l0k,''''''''''''''''''''........,
                                     ..........'''''..''''''''''....co,.'''''''''''''''''''''.......
                                      ......''''''....'''''''''''......'''''''''''''''''''''''''....
                                      ..''''''''.....''''''''''''''. ..'''''''''''''''''''''''''''..
                                       .............''''''''''''''''...'''''''''''''''''''''''''''''
                                          .................''''''''''..''''''''''''''''''''''''''''.
                                                            .....''''''''''''''''''''''''''''''''''.
..                                                               ...'''''''''''''''''''''''.........
'.    .                                                             ...''..''''''''''''.....        
;'.  ...                                                              ...  ....''''....             
;'.  'c.                                                                    .'......                
;,.. ;x; .                                                                  ...                     
;,.. ;0c .                                                                                          
;;...:Kd..                                                                                          
;;'..:Kk...                                                                                         
:;,..,O0, ...                                                                                       
:;;'..dO:...                                                                                       .
;;;,..:xc...                                                                                       ,
c:;;'.'ll,'.  .                                                                                 ....
loc;;..:l,',.                                                                                 ...::.
0Kkc;,.,l,',,.                                                                             ....'.;kd
KXKd;;'.,,.,,'.                                                                           .......'dK
l0X0c''.';',;,'.                                                                         .........c0
;ck0d,...:,';,,.                                                                         ...... ..;k
:',col'.....,;,'.                                                                        .....  ...:
:;'.,dd'  ...',,'.                                                                       ....   ....
:::;.'::..  .''','.            .....                                                     ....   ....
olccc:'',.....'.',.           ..  .....                                  ..              ....   ....
kkxolol;,;'. ..'.''.            .........                               ...               ..   .....
dx0Odll:;;;...''...'.            .........                            ....                .    .....