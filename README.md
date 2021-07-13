#🐍 Kay-O Time Limiter 🇧🇷
##Desliga o computador quando chega um horário determinado.
 
<h2>Introdução</h2>
Olá, sou o Gabs, desenvolvedor de sistemas.<br>
Eu desenvolvi o Kay-O com a função de limitar o horário do funcionamento dos computadores de empresas, evitando trabalhos fora do horário.
 
<h2>Utilização</h2>
Para utiliza-lo, basta criar um atalho do arquivo <b>"Kay-O.exe"</b>, que está na pasta <a href="https://github.com/Gabs-Leo/Kay-O.Time.Limiter/tree/main/dist/Kay-O">"/dist/Kay-O/"</a>, e mover este atalho para o diretório: <br>
<div style="padding: 20px; background-color: gray">
 %AppData%\Microsoft\Windows\Start Menu\Programs\Startup
</div>

<h2>Modificação</h2>
Caso queira alterar o horário em que o PC será desligado, basta alterar a variável <b>shutdown</b>.
Para qualquer modificação feita no código, o instalador deve também ser refeito através do pyinstaller.
 
<h3>Refazendo Instalador</h3>
Para utilizar o pyinstaller e refazer o instalador, basta digitar no terminal: <br>
<div style="padding: 20px; background-color: gray">
 cd C:\Users\Gabs\PycharmProjects\Kay-O
</div>
Isso acessará o diretório em que se encontra a aplicação "Kay-O.pyw", depois, basta digitar: <br>
<div style="padding: 20px; background-color: gray">
 pyinstaller --onefile Kay-O.pyw
</div>
